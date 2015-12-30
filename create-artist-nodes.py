import sys
import musicbrainzngs as m
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()


def main(args):

    # examples:
    # miles davis = 561d854a-6a28-4aa7-8c99-323e6ce46c2a
    # cannonball adderly = a4c73ebe-b2c7-4f13-b99d-2fe1f9f27da8
    # john coltrane = b625448e-bf4a-41c3-a421-72ad46cdb831
    # wynton kelly = d3f9352c-18e2-47a0-802c-13d821490e42
    # bill evans = 8247a3f2-3a8e-4256-b322-6c57b03a4e36
    # paul chambers = b6ff4fd0-03ae-41a6-942e-7de13124b970
    # jimmy cobb = d0cbf65a-541b-476a-996c-fe2cd264bbd0
    # gil evans = 83b1d510-c4ae-485b-91bf-c69b63044dd6
    # teo macero = 64e2e449-234c-480d-89d3-d5fead5a7988
    # irving townsend = 5ca16cfc-f480-4203-93e7-f35080d12d60
    # fred plaut = febc30e8-5033-4c65-b25c-084c872be8e5
    # roy haynes = 2c090b57-5e9d-49c5-9b71-6f0a331cc1ca

    for index, uuid in enumerate(args, start=1):

        m.set_useragent("jazz-graph", "0.01", "https://github.com/bmckinney/jazz-graph")

        artist = m.get_artist_by_id(uuid, ["aliases", "tags", "url-rels"])['artist']

        # debug
        # for key, value in artist.iteritems():
        #     print key, value

        aid = "artist_" + artist['id'].rsplit('-', 1)[1]

        print "MERGE \n(" + aid + ":Artist{"

        if "name" in artist:
            print "\tname: '" + artist['name'] + "',"

        if 'gender' in artist:
            print "\tgender: '" + artist['gender'] + "',"

        if 'sort-name' in artist:
            print "\tsort_name: '" + artist['sort-name'] + "',"

        if 'disambiguation' in artist:
            print "\tdisambiguation: '" + artist['disambiguation'] + "',"

        if 'country' in artist:
            print "\tcountry: '" + artist['country'] + "',"

        if 'life-span' in artist and 'begin' in artist['life-span']:
            print "\tbirth_date: '" + artist['life-span']['begin'] + "',"

        if 'life-span' in artist and 'end' in artist['life-span']:
            print "\tdeath_date: '" + artist['life-span']['end'] + "',"

        if 'alias-list' in artist:
            alist = []
            for a in artist['alias-list']:
                alist.append(a['alias'])
            print "\taliases: [" + ', '.join("'"+str(p)+"'" for p in alist) + "],"

        if 'tag-list' in artist:
            tlist = []
            for tag in artist['tag-list'][:-1]:
                if int(tag['count']) > 1:
                    tlist.append(tag['name'])
            if len(tlist) > 0:
                print "\ttags: [" + ', '.join("'"+str(p)+"'" for p in tlist) + "],"

        if 'url-relation-list' in artist:

            dlist = []
            odlist = []

            for url in artist['url-relation-list']:
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
                if url['type'] == "discography":
                    dlist.append(url['target'])
                if url['type'] == "other databases":
                    odlist.append(url['target'])

            if len(dlist) > 0:
                print "\tdiscographies: [" + ', '.join("'"+str(p)+"'" for p in dlist) + "],"

            if len(odlist) > 0:
                print "\tdatabases: [" + ', '.join("'"+str(p)+"'" for p in odlist) + "],"

            print "\tmusicbrainz: 'https://musicbrainz.org/artist/" + artist['id'] + "',"

            if 'isni-list' in artist:
                print "\tisni_list: [" + ', '.join("'http://isni.org/isni/"+str(p)+"'" for p in artist['isni-list']) \
                      + "],"

        print "\tuuid: '" + artist['id'] + "'"

        print "})"

if __name__ == "__main__":
    main(sys.argv[1:])
