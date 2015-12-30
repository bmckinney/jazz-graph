import sys
import musicbrainzngs as m
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()


def main(args):

    # examples:
    # so what = 2fafd730-423f-342e-b6c7-3a7d6599a72e
    # freddie freeloader = 500ecdf1-a82e-3afc-9268-382bacca0923
    # blue in green = 54d591f2-e928-3263-b963-d7943efb9a03
    # Flamenco Sketches = 36ff917b-6e10-3ee0-9e42-c46c80a82e1b
    # All Blues = 46e6bfc3-5f37-3e6e-a2be-1938072b1375

    rels = ''
    perfs = ''

    print "// works"

    for index, uuid in enumerate(args, start=1):

        m.set_useragent("jazz-graph", "0.01", "https://github.com/bmckinney/jazz-graph")

        work = m.get_work_by_id(uuid, ["tags", "url-rels", "artist-rels", "recording-rels"])['work']

        # debug
        # for key, value in work.iteritems():
        #     print key, value

        wid = "work_" + uuid.rsplit('-', 1)[1]

        print "MERGE \n(" + wid + ":Work{"

        if "title" in work:
            print "\tname: '" + work['title'].replace("'", "\'") + "',"

        if 'iswc' in work:
            print "\tiswc: '" + work['iswc'] + "',"

        if 'type' in work:
            print "\ttype: '" + work['type'] + "',"

        if 'tag-list' in work:
            tlist = []
            for tag in work['tag-list'][:-1]:
                if int(tag['count']) > 0:
                    tlist.append(tag['name'])
            if len(tlist) > 0:
                print "\ttags: [" + ', '.join("'"+str(p)+"'" for p in tlist) + "],"

        if 'url-relation-list' in work:

            odlist = []

            for url in work['url-relation-list']:
                if url['type'] == "wikipedia":
                    print "\twikipedia: '" + url['target'] + "',"
                if url['type'] == "wikidata":
                    print "\twikidata: '" + url['target'] + "',"
                if url['type'] == "discogs":
                    print "\tdiscogs: '" + url['target'] + "',"
                if url['type'] == "allmusic":
                    print "\tallmusic: '" + url['target'] + "',"
                if url['type'] == "BBC Music page":
                    print "\tbbc: '" + url['target'] + "',"
                if url['type'] == "other databases":
                    odlist.append(url['target'])

            if len(odlist) > 0:
                print "\tdatabases: [" + ', '.join("'"+str(p)+"'" for p in odlist) + "],"

            print "\tmusicbrainz: 'https://musicbrainz.org/work/" + work['id'] + "',"

        print "\tuuid: '" + work['id'] + "'"

        print "})"

        if 'recording-relation-list' in work:

            for rec in work['recording-relation-list']:
                if rec['type'] == "performance":
                    perfid = "perf_" + rec['target'].rsplit('-', 1)[1]
                    wid = "work_" + uuid.rsplit('-', 1)[1]

                    print "MERGE \n(" + perfid + ":Performance{"
                    if "recording" in rec:
                        if 'title' in rec['recording']:
                            print "\tname: '" + rec['recording']['title'].replace("'", "\\'") + "',"
                        if 'disambiguation' in rec['recording']:
                            print "\tdisambiguation: '" + rec['recording']['disambiguation'].replace("'", "\'") + "',"
                        if 'length' in rec['recording']:
                            minutes, milliseconds = divmod(int(rec['recording']['length']), 60000)
                            seconds = float(milliseconds) / 1000
                            s = "%i:%02i" % (minutes, seconds)
                            print "\tduration: '" + s + "',"
                        print "\tuuid: '" + rec['target'] + "'"
                        print "})"

                        perfs += "MERGE (" + perfid + ")-[:PERFORMANCE_OF]->(" + wid + ")\n"

        if 'artist-relation-list' in work:

            for rel in work['artist-relation-list']:
                if rel['type'] == "composer":
                    aid = "artist_" + rel['target'].rsplit('-', 1)[1]
                    wid = "work_" + uuid.rsplit('-', 1)[1]
                    rels += "MERGE (" + aid + ")-[:COMPOSED]->(" + wid + ")\n"\

    if len(perfs) > 0:
        print "\n// performances of"
        print perfs

    if len(rels) > 0:
        print "\n// composers"
        print rels

if __name__ == "__main__":
    main(sys.argv[1:])
