#!/usr/bin/python

import sys
import logging
import musicbrainzngs as m


def main(args):

    uuid = args[0]

    m.set_useragent("jazz-graph", "0.01", "https://github.com/bmckinney/jazz-graph")

    artist = m.get_artist_by_id(uuid, ["aliases", "tags", "url-rels"])['artist']

    # debug
    # for key, value in artist.iteritems():
    #     print(key, value)

    aid = "person_" + artist['id'].rsplit('-', 1)[1]

    print("\nMERGE (" + aid + ":Person{ uuid: '" + artist['id'] + "' }) ")

    # name
    if "name" in artist:
        print("SET " + aid + ".name = '" + artist['name'] + "'")
    # gender
    if "gender" in artist:
        print("SET " + aid + ".gender = '" + artist['gender'] + "'")
    # sort name
    if "sort_name" in artist:
        print("SET " + aid + ".sort_name = '" + artist['sort_name'] + "'")
    # disambiguation
    if "disambiguation" in artist:
        print("SET " + aid + ".disambiguation = '" + artist['disambiguation'] + "'")
    # country
    if "country" in artist:
        print("SET " + aid + ".country = '" + artist['country'] + "'")
    # birth date
    if 'life-span' in artist and 'begin' in artist['life-span']:
        print("SET " + aid + ".birth_date = '" + artist['life-span']['begin'] + "'")
    # death date
    if 'life-span' in artist and 'end' in artist['life-span']:
        print("SET " + aid + ".death_date = '" + artist['life-span']['end'] + "'")
    # aliases
    if 'alias-list' in artist:
        alist = []
        for a in artist['alias-list']:
            alist.append(a['alias'])
        print("SET " + aid + ".aliases =  [" + ', '.join("'" + p.encode('utf-8').strip() + "'" for p in alist) + "]")
    # tags
    if 'tag-list' in artist:
        tlist = []
        for tag in artist['tag-list'][:-1]:
            if int(tag['count']) > 1:
                tlist.append(tag['name'])
        if len(tlist) > 0:
            print("SET " + aid + ".tags = [" + ', '.join("'" + p.encode('utf-8').strip() + "'" for p in tlist) + "]")
    # urls
    if 'url-relation-list' in artist:

        dlist = []
        odlist = []

        for url in artist['url-relation-list']:
            if url['type'] == "wikipedia":
                print("SET " + aid + ".wikipedia = '" + url['target'] + "'")
            if url['type'] == "wikidata":
                print("SET " + aid + ".wikidata = '" + url['target'] + "'")
            if url['type'] == "VIAF":
                print("SET " + aid + ".viaf = '" + url['target'] + "'")
            if url['type'] == "IMDb":
                print("SET " + aid + ".imdb = '" + url['target'] + "'")
            if url['type'] == "discogs":
                print("SET " + aid + ".discogs = '" + url['target'] + "'")
            if url['type'] == "allmusic":
                print("SET " + aid + ".allmusic = '" + url['target'] + "'")
            if url['type'] == "BBC Music page":
                print("SET " + aid + ".bbc = '" + url['target'] + "'")
            if url['type'] == "discography":
                dlist.append(url['target'])
            if url['type'] == "other databases":
                odlist.append(url['target'])

        if len(dlist) > 0:
            print("SET " + aid + ".discographies = [" + ', '.join("'" + p.encode('utf-8').strip() + "'" for p in dlist) + "]")

        if len(odlist) > 0:
            print("SET " + aid + ".databases = [" + ', '.join("'" + p.encode('utf-8').strip() + "'" for p in odlist) + "]")

        print("SET " + aid + ".musicbrainz = 'https://musicbrainz.org/artist/" + artist['id'] + "'")

        if 'isni-list' in artist:
            print("SET " + aid + ".isni_list = [" + ', '.join("'http://isni.org/isni/" + p.encode('utf-8').strip() + "'" for p in artist['isni-list']) + "]")

    print("SET " + aid + ".source = 'musicbrainz.org'")
    print("SET " + aid + ".timestamp = timestamp()")

if __name__ == "__main__":
    main(sys.argv[1:])