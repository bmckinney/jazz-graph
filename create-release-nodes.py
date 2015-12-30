import sys
import musicbrainzngs as m
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()


def main(args):

    # examples:
    # kind of blue = 79ed3ff2-1b33-3245-8755-947554bc8b3d

    tracks = ''
    leaders = ''
    labels = ''

    print "// releases"

    for index, uuid in enumerate(args, start=1):

        m.set_useragent("jazz-graph", "0.01", "https://github.com/bmckinney/jazz-graph")

        rel = m.get_release_by_id(uuid, ["artist-credits", "url-rels", "labels", "discids", "recordings"])['release']

        # debug
        # for key, value in rel.iteritems():
        #     print key, value

        rid = "release_" + uuid.rsplit('-', 1)[1]

        print "MERGE \n(" + rid + ":Release{"

        if "title" in rel:
            print "\tname: '" + rel['title'] + "',"

        if "disambiguation" in rel:
            print "\tdisambiguation: '" + rel['disambiguation'] + "',"

        if "country" in rel:
            print "\tcountry: '" + rel['country'] + "',"

        if "date" in rel:
            print "\tdate: '" + rel['date'] + "',"

        if 'medium-list' in rel:
            if 'format' in rel['medium-list'][0]:
                print "\tformat: '" + rel['medium-list'][0]['format'] + "',"

            if 'track-list' in rel['medium-list'][0]:
                for track in rel['medium-list'][0]['track-list']:
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

                        tid = "perf_" + track['recording']['id'].rsplit('-', 1)[1]
                        tracks += "MERGE (" + rid + ")-[:HAS_TRACK " + props + "]->(" + tid + ")\n"

        if 'label-info-list' in rel:
            if 'catalog-number' in rel['label-info-list'][0]:
                print "\tdiscode: '" + rel['label-info-list'][0]['catalog-number'] + "',"

        # leader relationship
        if 'artist-credit' in rel:
            for artist in rel['artist-credit']:
                aid = "artist_" + artist['artist']['id'].rsplit('-', 1)[1]
                leaders += "MERGE (" + rid + ")-[:HAS_LEADER]->(" + aid + ")"

        if 'url-relation-list' in rel:

            for url in rel['url-relation-list']:
                if url['type'] == "wikipedia":
                    print "\twikipedia: '" + url['target'] + "',"
                if url['type'] == "wikidata":
                    print "\twikidata: '" + url['target'] + "',"
                if url['type'] == "VIAF":
                    print "\tviaf: '" + url['target'] + "',"
                if url['type'] == "IMDb":
                    print "\timdb: '" + url['target'] + "',"
                if url['type'] == "discogs":
                    print "\tdiscogs: '" + url['target'] + "',"
                if url['type'] == "allmusic":
                    print "\tallmusic: '" + url['target'] + "',"
                if url['type'] == "BBC Music page":
                    print "\tbbc: '" + url['target'] + "',"

        print "\tmusicbrainz: 'http://musicbrainz.org/release/" + rel['id'] + "',"

        print "\tuuid: '" + rel['id'] + "'"

        print "})"

        if 'label-info-list' in rel:
            for label in rel['label-info-list']:
                lid = "label_" + label['label']['id'].rsplit('-', 1)[1]
                print "// labels"
                print "MERGE \n(" + lid + ":Label{"
                print "\tname: '" + label['label']['name'] + "',"
                print "\tuuid: '" + label['label']['id'] + "'"
                print "})"
                labels += "MERGE (" + rid + ")-[:HAS_LABEL]->(" + lid + ")\n"

        if len(labels) > 0:
            print "\n// labels"
            print labels

        if len(tracks) > 0:
            print "\n// tracks"
            print tracks

        if len(leaders) > 0:
            print "\n// leaders"
            print leaders

if __name__ == "__main__":
    main(sys.argv[1:])
