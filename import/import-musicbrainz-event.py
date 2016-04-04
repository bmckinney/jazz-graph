#!/usr/bin/python

import sys
import musicbrainzngs as m
from geopy.geocoders import Nominatim


def main(args):

    # examples:
    # MJQ at the White House = 89a92f2f-8aad-4abb-9e54-54c6e531f30e

    leaders = ''
    performances = ''
    participation = ''
    place_list = []
    place_nodes = ''
    place_rels = ''
    artist_list = []
    works_list = []
    performance_list = []

    print "// events"

    for index, uuid in enumerate(args, start=1):

        m.set_useragent("jazz-graph", "0.01", "https://github.com/bmckinney/jazz-graph")

        rel = m.get_event_by_id(uuid, ["artist-rels", "work-rels", "place-rels", "area-rels"])['event']

        # debug
        #for key, value in rel.iteritems():
        #    print key, value

        # convert set list to a list of work ids
        if "setlist" in rel:
            for line in rel['setlist'].splitlines():
                if line.startswith('* ['):
                    works_list.append(line[3:].split('|')[0])

        event_id = uuid.rsplit('-', 1)[1]
        rid = "event_" + uuid.rsplit('-', 1)[1]

        print "\nMERGE (" + rid + ":Event{ uuid: '" + rel['id'] + "' })"

        if "name" in rel:
            print "SET " + rid + ".name = '" + rel['name'] + "'"

        if "life-span" in rel:
            print "SET " + rid + ".date = '" + rel['life-span']['begin'] + "'"

        if "type" in rel:
            print "SET " + rid + ".type = '" + rel['type'] + "'"

        print "SET " + rid + ".musicbrainz = 'http://musicbrainz.org/release/" + rel['id'] + "'"
        print "SET " + rid + ".source = 'musicbrainz.org'"
        print "SET " + rid + ".timestamp = timestamp()"

        # create list of place uuids
        place_begin_date = ''
        place_end_date = ''
        plc = ''
        if "place-relation-list" in rel:
            for place in rel['place-relation-list']:
                if 'begin' in place:
                    place_begin_date = place['begin']
                if 'end' in place:
                    place_end_date = place['end']
                if 'place' in place:
                    place_id = place['place']['id']
                    if place['place']['id'] not in place_list:

                        address = place['place']['address']
                        geolocator = Nominatim()
                        location = geolocator.geocode(address)
                        # print "ADDRESS: " + location.address
                        plc = "place_" + place_id.rsplit('-', 1)[1]
                        place_nodes += "\nMERGE (" + plc + ":Place{ uuid: '" + place_id + "' })\n"
                        place_nodes += "SET " + plc + ".name = '" + place['place']['name'] + "'\n"
                        place_nodes += "SET " + plc + ".address = '" + location.address + "'\n"
                        place_nodes += "SET " + plc + ".lat = '" + repr(location.latitude) + "'\n"
                        place_nodes += "SET " + plc + ".lng = '" + repr(location.longitude) + "'\n"
                        place_nodes += "SET " + plc + ".source = 'musicbrainz.org'\n"

                        place_list.append(place_id)

                    place_rels += "MERGE (" + rid + ")-[:HAS_PLACE { "
                    place_rels += "type: '" + place['type'] + "'"
                    if len(place_begin_date) > 0:
                        place_rels += ", begin: '" + place_begin_date + "'"
                    if len(place_end_date) > 0:
                        place_rels += ", end: '" + place_end_date + "'"
                    place_rels += " }]->"
                    place_rels += "(place_" + place_id.rsplit('-', 1)[1] + ")\n"

        if "artist-relation-list" in rel:

            # artist dictionaries
            ad = []

            for artist in rel['artist-relation-list']:
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

                    if artist['type'] == 'producer':
                        tmp_dict["roles"].append("producer")

                    if artist['type'] == 'vocal':
                        tmp_dict["roles"].append("singer")

                    if artist['type'] == 'recording':
                        tmp_dict["roles"].append("recording engineer")

                    if artist['type'] == 'main performer':
                        tmp_dict["roles"].append("musician")
                        if 'attribute-list' in artist:
                            instruments = []
                            for a in artist['attribute-list']:
                                instruments.append(a)
                                tmp_dict["instruments"].append(a)

            # participation
            for d in ad:
                for workid in works_list:
                    participation += artist_participation(d, "perf_" + event_id + "_" + workid.rsplit('-', 1)[1])

        # performance-place relationships
        for workid in works_list:
            place_rels += "MERGE (" + "perf_" + event_id + "_" + workid.rsplit('-', 1)[1] + ")-[:HAS_PLACE { "
            place_rels += "type: 'performed at', begin: '" + rel['life-span']['begin'] + "', end: '" + rel['life-span']['end'] + "' }]->"
            place_rels += "(" + plc + ")\n"

        if len(artist_list) > 0:
            print_artist_cypher(set(artist_list))

        if len(performances) > 0:
            print "\n// performances"
            print performances

        if len(leaders) > 0:
            print "\n// leaders"
            print leaders

        if works_list:
            print_work_cypher(works_list, performance_list, artist_list, event_id, rel['life-span']['begin'], rel['life-span']['end'])

        if len(place_nodes) > 0:
            print "\n// place nodes"
            print place_nodes

        if len(place_rels) > 0:
            print "\n// place relationships"
            print place_rels

        print "\n// event-performance participation"
        print participation


def print_artist_cypher(uuid_list):

    for index, uuid in enumerate(uuid_list, start=1):

        m.set_useragent("jazz-graph", "0.01", "https://github.com/bmckinney/jazz-graph")

        artist = m.get_artist_by_id(uuid, ["aliases", "tags", "url-rels"])['artist']

        # debug
        # for key, value in artist.iteritems():
        #     print key, value

        aid = "person_" + artist['id'].rsplit('-', 1)[1]

        print "\nMERGE (" + aid + ":Person{ uuid: '" + artist['id'] + "' }) "

        # name
        if "name" in artist:
            print "SET " + aid + ".name = '" + artist['name'] + "'"
        # gender
        if "gender" in artist:
            print "SET " + aid + ".gender = '" + artist['gender'] + "'"
        # sort name
        if "sort_name" in artist:
            print "SET " + aid + ".sort_name = '" + artist['sort_name'] + "'"
        # disambiguation
        if "disambiguation" in artist:
            print "SET " + aid + ".disambiguation = '" + artist['disambiguation'] + "'"
        # country
        if "country" in artist:
            print "SET " + aid + ".country = '" + artist['country'] + "'"
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
            "SET " + aid + ".aliases =  [" + ', '.join("'" + p.encode('utf-8').strip() + "'" for p in alist) + "]"
        # tags
        if 'tag-list' in artist:
            tlist = []
            for tag in artist['tag-list'][:-1]:
                if int(tag['count']) > 1:
                    tlist.append(tag['name'])
            if len(tlist) > 0:
                "SET " + aid + ".tags = [" + ', '.join("'" + p.encode('utf-8').strip() + "'" for p in tlist) + "]"
        # urls
        if 'url-relation-list' in artist:

            dlist = []
            odlist = []

            for url in artist['url-relation-list']:
                if url['type'] == "wikipedia":
                    print "SET " + aid + ".wikipedia = '" + url['target'] + "'"
                if url['type'] == "wikidata":
                    print "SET " + aid + ".wikidata = '" + url['target'] + "'"
                if url['type'] == "VIAF":
                    print "SET " + aid + ".viaf = '" + url['target'] + "'"
                if url['type'] == "IMDb":
                    print "SET " + aid + ".imdb = '" + url['target'] + "'"
                if url['type'] == "discogs":
                    print "SET " + aid + ".discogs = '" + url['target'] + "'"
                if url['type'] == "allmusic":
                    print "SET " + aid + ".allmusic = '" + url['target'] + "'"
                if url['type'] == "BBC Music page":
                    print "SET " + aid + ".bbc = '" + url['target'] + "'"
                if url['type'] == "discography":
                    dlist.append(url['target'])
                if url['type'] == "other databases":
                    odlist.append(url['target'])

            if len(dlist) > 0:
                print "SET " + aid + ".discographies = [" + ', '.join("'" + p.encode('utf-8').strip() +
                                                                      "'" for p in dlist) + "]"

            if len(odlist) > 0:
                print "SET " + aid + ".databases = [" + ', '.join("'" + p.encode('utf-8').strip() +
                                                                  "'" for p in odlist) + "]"

            print "SET " + aid + ".musicbrainz = 'https://musicbrainz.org/artist/" + artist['id'] + "'"

            if 'isni-list' in artist:
                print "SET " + aid + ".isni_list = [" + ', '.join("'http://isni.org/isni/" + p.encode('utf-8').strip()
                                                                  + "'" for p in artist['isni-list']) + "]"

        print "SET " + aid + ".source = 'musicbrainz.org'"
        print "SET " + aid + ".timestamp = timestamp()"


def print_work_cypher(uuid_list, perf_list, artist_list, event_id, begin, end):

    cypher = ''
    composers = ''
    performances = ''
    composer_list = []

    print "\n// works"

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
                cypher += "SET " + wid + ".tags = [" + ', '.join("'" + p.encode('utf-8').strip() +
                                                                 "'" for p in tlist) + "]\n"

        if 'url-relation-list' in work:

            odlist = []

            for url in work['url-relation-list']:
                if url['type'] == "wikipedia":
                    cypher += "SET " + wid + ".wikipedia = '" + url['target'] + "'\n"
                if url['type'] == "wikidata":
                    cypher += "SET " + wid + ".wikidata = '" + url['target'] + "'\n"
                if url['type'] == "discogs":
                    cypher += "SET " + wid + ".discogs = '" + url['target'] + "'\n"
                if url['type'] == "allmusic":
                    cypher += "SET " + wid + ".allmusic = '" + url['target'] + "'\n"
                if url['type'] == "BBC Music page":
                    cypher += "SET " + wid + ".bbc = '" + url['target'] + "'\n"
                if url['type'] == "other databases":
                    odlist.append(url['target'])

            if len(odlist) > 0:
                cypher += "SET " + wid + ".databases = [" + ', '.join("'" + p.encode('utf-8').strip() +
                                                                      "'" for p in odlist) + "]\n"

            cypher += "SET " + wid + ".musicbrainz = 'https://musicbrainz.org/work/" + work['id'] + "'\n"

        cypher += "SET " + wid + ".source = 'musicbrainz.org'\n"
        cypher += "SET " + wid + ".timestamp = timestamp()\n"

        # construct performance id as combination of event id + work id (since musicbrainz doesn't
        # allow for performance objects that aren't recorded, set lists can only reference works
        perfid = "perf_" + event_id + "_" + uuid.rsplit('-', 1)[1]
        wid = "work_" + uuid.rsplit('-', 1)[1]
        performances += "MERGE (" + perfid + ":Performance { uuid: '" + event_id + "-" + uuid + "' })\n"
        performances += "SET " + perfid + ".name = '" + work['title'].replace("'", "\\'") + "'\n"
        performances += "SET " + perfid + ".begin = '" + begin + "'\n"
        performances += "SET " + perfid + ".end = '" + end + "'\n"
        performances += "SET " + perfid + ".source = 'musicbrainz.org'\n"
        performances += "SET " + perfid + ".timestamp = timestamp()\n"
        performances += "MERGE (" + perfid + ")-[:PERFORMANCE_OF]->(" + wid + ")\n\n"

    # 1 - artist/composer nodes
    if len(composer_list) > 0:
        print_artist_cypher(set(composer_list))

    #  2 - work nodes
    print cypher

    # 3 - performance -> work relationships
    if len(performances) > 0:
        print "\n// performances"
        print performances

    # 4 - composer -> work relationships
    if len(composers) > 0:
        print "\n// composers"
        print composers


def dumpclean(obj):
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print k
                dumpclean(v)
            else:
                print '%s : %s' % (k, v)
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                dumpclean(v)
            else:
                print v
    else:
        print obj


def artist_participation(mb, perf):
    retval = ""
    if len(mb["roles"]) > 0:
        retval += "MERGE (" + mb["artist"] + ")-[:PARTICIPATED_IN { roles: [" + \
                  ', '.join("'" + i.encode('utf-8').strip() + "'" for i in mb["roles"]) + "]"
        if len(mb["instruments"]) > 0:
            retval += ", instruments: [" + ', '.join("'" + i.encode('utf-8').strip() +
                                                     "'" for i in mb["instruments"]) + "]"
        retval += " }]->(" + perf + ")\n"
    else:
        print "\n// no roles for " + mb["artist"]

    return retval

if __name__ == "__main__":
    main(sys.argv[1:])
