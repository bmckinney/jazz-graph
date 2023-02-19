#!/usr/bin/python

import sys
import logging
import musicbrainzngs as m
from geopy.geocoders import Nominatim

logging.basicConfig(filename='import-musicbrainz-release.log', encoding='utf-8', level=logging.DEBUG)

def main(args):

    # examples:
    # kind of blue = 79ed3ff2-1b33-3245-8755-947554bc8b3d

    tracks = ''
    leaders = ''
    labels = ''
    performances = ''
    participation = ''
    place_list = []
    area_list = []
    place_nodes = ''
    place_rels = ''
    artist_list = []
    works_list = []
    performance_list = []

    print ("// releases")

    for index, uuid in enumerate(args, start=1):

        m.set_useragent("jazz-graph", "0.01", "https://github.com/bmckinney/jazz-graph")

        rel = m.get_release_by_id(uuid, ["artist-credits", "url-rels", "labels", "discids", "recordings"])['release']

        # debug
        # for key, value in rel.iteritems():
        #     print key, value

        # logging.debug("RELEASE")
        # logging.debug(rel)

        rid = "release_" + uuid.rsplit('-', 1)[1]

        # create list of artist uuids and print cypher
        if "artist-credit" in rel:
            for artist in rel['artist-credit']:
                if 'artist' in artist:
                    artist_list.append(artist['artist']['id'])
            # print_artist_cypher(artist_list)

        print ("\nMERGE (" + rid + ":Release{ uuid: '" + rel['id'] + "' })")

        if "title" in rel:
            print ("SET " + rid + ".name = '" + rel['title'].replace("'", "\\'") + "'")

        if "disambiguation" in rel:
            print ("SET " + rid + ".disambiguation = '" + rel['disambiguation'] + "'")

        if "country" in rel:
            print ("SET " + rid + ".country = '" + rel['country'] + "'")

        if "date" in rel:
            print ("SET " + rid + ".date = '" + rel['date'] + "'")

        if 'medium-list' in rel:

            # multiple medium lists where multi-CD, etc.
            for medium in rel['medium-list']:

                if 'format' in medium:
                    print ("SET " + rid + ".format = '" + medium['format'] + "'")

                if 'track-list' in medium:
                    for track in medium['track-list']:
                        if 'recording' in track:
                            props = ''
                            if 'number' in track:
                                props += "name: '" + track['number'] + "'"
                            if 'position' in track:
                                if len(props) > 0:
                                    props += ", "
                                props += "sequence: " + track['position']
                            if len(props) > 0:
                                props = "{" + props + "}"

                            # get recordings (performances)
                            rec = m.get_recording_by_id(track['recording']['id'],
                                                        ["artist-rels", "work-rels", "place-rels", "area-rels"])['recording']

                            # debug
                            # for key, value in rec.iteritems():
                            #     print key, value

                            logging.debug("RECORDING")
                            logging.debug(rec)

                            # add to list of performance uuids
                            performance_list.append(track['recording']['id'])

                            perfid = "perf_" + track['recording']['id'].rsplit('-', 1)[1]

                            if "artist-relation-list" in rec:

                                # artist dictionaries
                                ad = []

                                for artist in rec['artist-relation-list']:
                                    if 'artist' in artist:
                                        artist_list.append(artist['artist']['id'])
                                        tmp_artist_id = artist['artist']['id']

                                        tmp_dict = {}
                                        has_artist = False
                                        for d in ad:
                                            if d["artist"] == "person_" + tmp_artist_id.rsplit('-', 1)[1]:
                                                has_artist = True
                                                tmp_dict = d
                                                break

                                        if not has_artist:
                                            tmp_dict = {"artist": "person_" + tmp_artist_id.rsplit('-', 1)[1],
                                                        "roles": [], "instruments": []}
                                            ad.append(tmp_dict)

                                    if 'type' in artist:
                                        # types: instrument, producer, recording, vocal
                                        if artist['type'] == 'instrument':
                                            if 'attribute-list' in artist:
                                                instruments = []
                                                for a in artist['attribute-list']:
                                                    instruments.append(a)
                                                    tmp_dict["instruments"].append(a)
                                                    has_musician = False
                                                    for r in tmp_dict["roles"]:
                                                        if r == "musician":
                                                            has_musician = True
                                                            break
                                                    if not has_musician:
                                                        tmp_dict["roles"].append("musician")

                                        if artist['type'] == 'producer':
                                            tmp_dict["roles"].append("producer")

                                        if artist['type'] == 'vocal':
                                            tmp_dict["roles"].append("singer")

                                        if artist['type'] == 'recording':
                                            tmp_dict["roles"].append("recording engineer")

                                # print dictionaries
                                for d in ad:
                                    participation += artist_participation(d, perfid)

                            # create list of works uuids
                            if "work-relation-list" in rec:
                                for work in rec['work-relation-list']:
                                    if 'work' in work:
                                        works_list.append(work['work']['id'])

                            # create list of place uuids
                            place_begin_date = ''
                            place_end_date = ''
                            if "place-relation-list" in rec:

                                logging.debug("PLACE:")
                                logging.debug(rec['place-relation-list'])

                                for place in rec['place-relation-list']:
                                    if 'begin' in place:
                                        place_begin_date = place['begin']
                                    if 'end' in place:
                                        place_end_date = place['end']
                                    if 'place' in place:
                                        place_id = place['place']['id']
                                        if place['place']['id'] not in place_list:

                                            plc = "place_" + place_id.rsplit('-', 1)[1]
                                            place_nodes += "\nMERGE (" + plc + ":Place{ uuid: '" + place_id + "' })\n"
                                            place_nodes += "SET " + plc + ".name = '" + place['place']['name'] + "'\n"

                                            if 'address' in place['place']:
                                                #print "PLACE: " + place['place']['address']
                                                address = place['place']['address']

                                                # try to expand the address with geopy
                                                # geolocator = Nominatim(user_agent="mckinney.sw@gmail.com")
                                                # location = geolocator.geocode(address)
                                                # if location is not None:
                                                #     place_nodes += "SET " + plc + ".address = '" + location.address + "'\n"
                                                #     place_nodes += "SET " + plc + ".lat = '" + repr(location.latitude) + "'\n"
                                                #     place_nodes += "SET " + plc + ".lng = '" + repr(location.longitude) + "'\n"
                                                # else:
                                                #     place_nodes += "SET " + plc + ".address = '" + address + "'\n"

                                            # place -> area
                                            if 'area' in place['place']:
                                                area = place['place']['area']
                                                place_nodes += "SET " + plc + ".area = '" + area + "'\n"

                                            place_nodes += "SET " + plc + ".source = 'musicbrainz.org'\n"

                                            place_list.append(place_id)

                                        place_rels += "MERGE (" + perfid + ")-[:HAS_PLACE { "
                                        place_rels += "type: '" + place['type'] + "'"
                                        if len(place_begin_date) > 0:
                                            place_rels += ", begin: '" + place_begin_date + "'"
                                        if len(place_end_date) > 0:
                                            place_rels += ", end: '" + place_end_date + "'"
                                        place_rels += " }]->"
                                        place_rels += "(place_" + place_id.rsplit('-', 1)[1] + ")\n"

                            # create list of place uuids for musicbrainz areas
                            if "area-relation-list" in rec:
                                for area in rec['area-relation-list']:
                                    if 'begin' in area:
                                        place_begin_date = area['begin']
                                    if 'end' in area:
                                        place_end_date = area['end']
                                    if 'area' in area:
                                        area_id = area['area']['id']
                                        # avoid dupes
                                        if area['area']['id'] not in area_list:

                                            plc = "place_" + area_id.rsplit('-', 1)[1]
                                            place_nodes += "\nMERGE (" + plc + ":Place{ uuid: '" + area_id + "' })\n"
                                            place_nodes += "SET " + plc + ".name = '" + area['area']['name'] + "'\n"
                                            place_nodes += "SET " + plc + ".source = 'musicbrainz.org'\n"
                                            area_list.append(area_id)

                                        place_rels += "MERGE (" + perfid + ")-[:HAS_PLACE { "
                                        place_rels += "type: '" + area['type'] + "'"
                                        if len(place_begin_date) > 0:
                                            place_rels += ", begin: '" + place_begin_date + "'"
                                        if len(place_end_date) > 0:
                                            place_rels += ", end: '" + place_end_date + "'"
                                        place_rels += " }]->"
                                        place_rels += "(place_" + area_id.rsplit('-', 1)[1] + ")\n"

                        performances += "\nMERGE (" + perfid + ":Performance{ uuid: '" + rec['id'] + "' })\n"
                        if 'title' in rec:
                            performances += "SET " + perfid + ".name = '" + rec['title'].replace("'", "\\'") + "'\n"
                        if 'disambiguation' in rec:
                            performances += "SET " + perfid + ".disambiguation = '" + \
                                            rec['disambiguation'].replace("'", "\\'") + "'\n"
                        if 'length' in rec:
                            minutes, milliseconds = divmod(int(rec['length']), 60000)
                            seconds = float(milliseconds) / 1000
                            s = "%i:%02i" % (minutes, seconds)
                            performances += "SET " + perfid + ".duration = '" + s + "'\n"
                        if len(place_begin_date) > 0:
                            performances += "SET " + perfid + ".begin = '" + place_begin_date + "'\n"
                        if len(place_end_date) > 0:
                            performances += "SET " + perfid + ".end = '" + place_end_date + "'\n"
                        performances += "SET " + perfid + ".source = 'musicbrainz.org'\n"
                        performances += "SET " + perfid + ".timestamp = timestamp()\n"

                        # debug
                        # for key, value in rec.iteritems():
                        #     print key, value

                        tid = "perf_" + track['recording']['id'].rsplit('-', 1)[1]
                        tracks += "MERGE (" + rid + ")-[:HAS_TRACK " + props + "]->(" + tid + ")\n"

        if 'label-info-list' in rel:
            if len(rel['label-info-list']) > 0:
                if 'catalog-number' in rel['label-info-list'][0]:
                    print ("SET " + rid + ".discode = '" + rel['label-info-list'][0]['catalog-number'] + "'")

        # leader relationship
        # if 'artist-credit' in rel:
        #     for artist in rel['artist-credit']:
        #         if 'artist' in artist:
        #             aid = "artist_" + artist['artist']['id'].rsplit('-', 1)[1]
        #             leaders += "MERGE (" + rid + ")-[:HAS_LEADER]->(" + aid + ")\n"

        if 'url-relation-list' in rel:

            for url in rel['url-relation-list']:
                url_target = url['target']
                url_target = url_target.replace("'", "%27")
                if url['type'] == "wikipedia":
                    print ("SET " + rid + ".wikipedia = '" + url_target + "'")
                if url['type'] == "wikidata":
                    print ("SET " + rid + ".wikidata = '" + url_target + "'")
                if url['type'] == "VIAF":
                    print ("SET " + rid + ".viaf = '" + url_target + "'")
                if url['type'] == "IMDb":
                    print ("SET " + rid + ".imdb = '" + url_target + "'")
                if url['type'] == "discogs":
                    print ("SET " + rid + ".discogs = '" + url_target + "'")
                if url['type'] == "allmusic":
                    print ("SET " + rid + ".allmusic = '" + url_target + "'")
                if url['type'] == "BBC Music page":
                    print ("SET " + rid + ".bbc = '" + url_target + "'")

        print ("SET " + rid + ".musicbrainz = 'http://musicbrainz.org/release/" + rel['id'] + "'")
        print ("SET " + rid + ".source = 'musicbrainz.org'")
        print ("SET " + rid + ".timestamp = timestamp()")

        if len(artist_list) > 0:
            print_artist_cypher(set(artist_list))

        if 'label-info-list' in rel:
            for label in rel['label-info-list']:
                lid = "label_" + label['label']['id'].rsplit('-', 1)[1]
                print ("// labels")
                print ("\nMERGE (" + lid + ":Label{ uuid: '" + label['label']['id'] + "' })")
                print ("SET " + lid + ".name= '" + label['label']['name'] + "'")
                labels += "MERGE (" + rid + ")-[:HAS_LABEL]->(" + lid + ")\n"

        if len(performances) > 0:
            print ("\n// performances")
            print (performances)

        if len(labels) > 0:
            print ("\n\n// labels")
            print (labels)

        if len(tracks) > 0:
            print ("\n// tracks")
            print (tracks)

        if len(leaders) > 0:
            print ("\n// leaders")
            print (leaders)

        if works_list:
            print_work_cypher(works_list, performance_list, artist_list)

        if len(place_nodes) > 0:
            print ("\n// place nodes")
            print (place_nodes)

        if len(place_rels) > 0:
            print ("\n// place relationships")
            print (place_rels)

        print (participation)


def print_artist_cypher(uuid_list):

    for index, uuid in enumerate(uuid_list, start=1):

        m.set_useragent("jazz-graph", "0.01", "https://github.com/bmckinney/jazz-graph")

        artist = m.get_artist_by_id(uuid, ["aliases", "tags", "url-rels"])['artist']

        # debug
        # for key, value in artist.iteritems():
        #     print key, value

        aid = "person_" + artist['id'].rsplit('-', 1)[1]

        print ("\nMERGE (" + aid + ":Person{ uuid: '" + artist['id'] + "' }) ")

        # name
        if "name" in artist:
            print ("SET " + aid + ".name = '" + artist['name'] + "'")
        # gender
        if "gender" in artist:
            print ("SET " + aid + ".gender = '" + artist['gender'] + "'")
        # sort name
        if "sort_name" in artist:
            print ("SET " + aid + ".sort_name = '" + artist['sort_name'] + "'")
        # disambiguation
        if "disambiguation" in artist:
            print ("SET " + aid + ".disambiguation = '" + artist['disambiguation'] + "'")
        # country
        if "country" in artist:
            print ("SET " + aid + ".country = '" + artist['country'] + "'")
        # birth date
        if 'life-span' in artist and 'begin' in artist['life-span']:
            "SET " + aid + ".birth_date = '" + artist['life-span']['begin'] + "'"
        # death date
        if 'life-span' in artist and 'end' in artist['life-span']:
            "SET " + aid + ".death_date = '" + artist['life-span']['end'] + "'"
        # aliases
        if 'alias-list' in artist:
            alist = []
            for a in artist['alias-list']:
                alist.append(a['alias'])
            "SET " + aid + ".aliases =  [" + ', '.join("'" + p.strip() + "'" for p in alist) + "]"
        # tags
        if 'tag-list' in artist:
            tlist = []
            for tag in artist['tag-list'][:-1]:
                if int(tag['count']) > 1:
                    tlist.append(tag['name'])
            if len(tlist) > 0:
                "SET " + aid + ".tags = [" + ', '.join("'" + p.strip() + "'" for p in tlist) + "]"
        # urls
        if 'url-relation-list' in artist:

            dlist = []
            odlist = []

            for url in artist['url-relation-list']:
                url_target = url['target']
                url_target = url_target.replace("'", "%27")
                if url['type'] == "wikipedia":
                    print ("SET " + aid + ".wikipedia = '" + url_target + "'")
                if url['type'] == "wikidata":
                    print ("SET " + aid + ".wikidata = '" + url_target + "'")
                if url['type'] == "VIAF":
                    print ("SET " + aid + ".viaf = '" + url_target + "'")
                if url['type'] == "IMDb":
                    print ("SET " + aid + ".imdb = '" + url_target + "'")
                if url['type'] == "discogs":
                    print ("SET " + aid + ".discogs = '" + url_target + "'")
                if url['type'] == "allmusic":
                    print ("SET " + aid + ".allmusic = '" + url_target + "'")
                if url['type'] == "BBC Music page":
                    print ("SET " + aid + ".bbc = '" + url_target + "'")
                if url['type'] == "discography":
                    dlist.append(url_target)
                if url['type'] == "other databases":
                    odlist.append(url_target)

            if len(dlist) > 0:
                print ("SET " + aid + ".discographies = [" + ', '.join("'" + p.strip() + "'" for p in dlist) + "]")

            if len(odlist) > 0:
                print ("SET " + aid + ".databases = [" + ', '.join("'" + p.strip() + "'" for p in odlist) + "]")

            print ("SET " + aid + ".musicbrainz = 'https://musicbrainz.org/artist/" + artist['id'] + "'")

            if 'isni-list' in artist:
                print ("SET " + aid + ".isni_list = [" + ', '.join("'http://isni.org/isni/" + p.strip()
                                                                  + "'" for p in artist['isni-list']) + "]")

        print ("SET " + aid + ".source = 'musicbrainz.org'")
        print ("SET " + aid + ".timestamp = timestamp()")


def print_work_cypher(uuid_list, perf_list, artist_list):

    cypher = ''
    composers = ''
    performances = ''
    composer_list = []

    print ("// works")
    # dedupe in case of medleys
    uuid_list = list(set(uuid_list))

    for index, uuid in enumerate(uuid_list, start=1):

        m.set_useragent("jazz-graph", "0.01", "https://github.com/bmckinney/jazz-graph")

        work = m.get_work_by_id(uuid, ["tags", "url-rels", "artist-rels", "recording-rels"])['work']

        # debug
        # for key, value in work.iteritems():
        #     print key, value

        wid = "work_" + uuid.rsplit('-', 1)[1]

        # generate artist-composer list
        if 'artist-relation-list' in work:
            for rel in work['artist-relation-list']:
                if rel['type'] == "composer" or rel['type'] == "writer":

                    aid = "person_" + rel['target'].rsplit('-', 1)[1]
                    wid = "work_" + uuid.rsplit('-', 1)[1]
                    composers += "MERGE (" + aid + ")-[:COMPOSED]->(" + wid + ")\n"

                    # don't duplicate artists where they are also performers on the release
                    if rel['target'] not in artist_list:
                        composer_list.append(rel['target'])
                if rel['type'] == "lyricist":

                    aid = "person_" + rel['target'].rsplit('-', 1)[1]
                    wid = "work_" + uuid.rsplit('-', 1)[1]
                    composers += "MERGE (" + aid + ")-[:WROTE_LYRICS]->(" + wid + ")\n"

                    # don't duplicate artists where they are also performers on the release
                    if rel['target'] not in artist_list:
                        composer_list.append(rel['target'])


        cypher += "\nMERGE (" + wid + ":Work{ uuid: '" + work['id'] + "' })\n"

        if "title" in work:
            cypher += "SET " + wid + ".name = '" + work['title'].replace("'", "\\'") + "'\n"

        if 'iswc' in work:
            cypher += "SET " + wid + ".iswc = '" + work['iswc'] + "'\n"

        if 'type' in work:
            cypher += "SET " + wid + ".type = '" + work['type'] + "'\n"

        if 'tag-list' in work:
            tlist = []
            for tag in work['tag-list'][:-1]:
                if int(tag['count']) > 0:
                    tlist.append(tag['name'])
            if len(tlist) > 0:
                cypher += "SET " + wid + ".tags = [" + ', '.join("'" + p.strip() +
                                                                 "'" for p in tlist) + "]\n"

        if 'url-relation-list' in work:

            odlist = []

            for url in work['url-relation-list']:
                url_target = url['target']
                url_target = url_target.replace("'", "%27")
                if url['type'] == "wikipedia":
                    cypher += "SET " + wid + ".wikipedia = '" + url_target + "'\n"
                if url['type'] == "wikidata":
                    cypher += "SET " + wid + ".wikidata = '" + url_target + "'\n"
                if url['type'] == "discogs":
                    cypher += "SET " + wid + ".discogs = '" + url_target + "'\n"
                if url['type'] == "allmusic":
                    cypher += "SET " + wid + ".allmusic = '" + url_target + "'\n"
                if url['type'] == "BBC Music page":
                    cypher += "SET " + wid + ".bbc = '" + url_target + "'\n"
                if url['type'] == "other databases":
                    odlist.append(url_target)

            if len(odlist) > 0:
                cypher += "SET " + wid + ".databases = [" + ', '.join("'" + p.strip() +
                                                                      "'" for p in odlist) + "]\n"

            cypher += "SET " + wid + ".musicbrainz = 'https://musicbrainz.org/work/" + work['id'] + "'\n"

        cypher += "SET " + wid + ".source = 'musicbrainz.org'\n"
        cypher += "SET " + wid + ".timestamp = timestamp()\n"

        if 'recording-relation-list' in work:
            for rec in work['recording-relation-list']:
                if rec['type'] == "performance":
                    if rec['target'] in perf_list:
                        perfid = "perf_" + rec['target'].rsplit('-', 1)[1]
                        wid = "work_" + uuid.rsplit('-', 1)[1]
                        is_medley = ""
                        if 'attribute-list' in rec:
                            for attrib in rec['attribute-list']:
                                if attrib == 'medley':
                                    is_medley = " {medley: true}"
                        performances += "MERGE (" + perfid + ")-[:PERFORMANCE_OF" + is_medley + "]->(" + wid + ")\n"

    # 1 - artist/composer nodes
    if len(composer_list) > 0:
        print_artist_cypher(set(composer_list))

    #  2 - work nodes
    print (cypher)

    # 3 - performance -> work relationships
    if len(performances) > 0:
        print ("\n// performances of")
        print (performances)

    # 4 - composer -> work relationships
    if len(composers) > 0:
        print ("\n// composers")
        print (composers)


def dumpclean(obj):
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print (k)
                dumpclean(v)
            else:
                print ('%s : %s' % (k, v))
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                dumpclean(v)
            else:
                print (v)
    else:
        print (obj)


def artist_participation(mb, perf):
    retval = ""
    if len(mb["roles"]) > 0:
        retval += "MERGE (" + mb["artist"] + ")-[:PARTICIPATED_IN { roles: [" + \
                  ', '.join("'" + i.strip() + "'" for i in mb["roles"]) + "]"
        if len(mb["instruments"]) > 0:
            retval += ", instruments: [" + ', '.join("'" + i.strip() +
                                                     "'" for i in mb["instruments"]) + "]"
        retval += " }]->(" + perf + ")\n"
    return retval

if __name__ == "__main__":
    main(sys.argv[1:])
