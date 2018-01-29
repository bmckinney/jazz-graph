// releases

MERGE (release_c6541eb039a4:Release{ uuid: '0799b10f-b191-429d-94c4-c6541eb039a4' })
SET release_c6541eb039a4.name = 'Live at the Jazz Showcase in Chicago, Volume One'
SET release_c6541eb039a4.country = 'DE'
SET release_c6541eb039a4.date = '1981'
SET release_c6541eb039a4.format = 'CD'
SET release_c6541eb039a4.discode = '3099-2'
SET release_c6541eb039a4.musicbrainz = 'http://musicbrainz.org/release/0799b10f-b191-429d-94c4-c6541eb039a4'
SET release_c6541eb039a4.source = 'musicbrainz.org'
SET release_c6541eb039a4.timestamp = timestamp()

MERGE (person_22a5fbaaf713:Person{ uuid: 'cf362673-150d-4a99-8e7b-22a5fbaaf713' })
SET person_22a5fbaaf713.name = 'Cecil McBee'
SET person_22a5fbaaf713.gender = 'Male'
SET person_22a5fbaaf713.country = 'US'
SET person_22a5fbaaf713.allmusic = 'http://www.allmusic.com/artist/mn0000739015'
SET person_22a5fbaaf713.wikipedia = 'https://en.wikipedia.org/wiki/Cecil_McBee'
SET person_22a5fbaaf713.discogs = 'https://www.discogs.com/artist/258511'
SET person_22a5fbaaf713.wikidata = 'https://www.wikidata.org/wiki/Q1052331'
SET person_22a5fbaaf713.musicbrainz = 'https://musicbrainz.org/artist/cf362673-150d-4a99-8e7b-22a5fbaaf713'
SET person_22a5fbaaf713.source = 'musicbrainz.org'
SET person_22a5fbaaf713.timestamp = timestamp()

MERGE (person_6f0a331cc1ca:Person{ uuid: '2c090b57-5e9d-49c5-9b71-6f0a331cc1ca' })
SET person_6f0a331cc1ca.name = 'Roy Haynes'
SET person_6f0a331cc1ca.gender = 'Male'
SET person_6f0a331cc1ca.country = 'US'
SET person_6f0a331cc1ca.viaf = 'http://viaf.org/viaf/84975999'
SET person_6f0a331cc1ca.allmusic = 'http://www.allmusic.com/artist/mn0000290464'
SET person_6f0a331cc1ca.bbc = 'http://www.bbc.co.uk/music/artists/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.imdb = 'http://www.imdb.com/name/nm0371542/'
SET person_6f0a331cc1ca.wikipedia = 'https://en.wikipedia.org/wiki/Roy_Haynes'
SET person_6f0a331cc1ca.discogs = 'https://www.discogs.com/artist/255556'
SET person_6f0a331cc1ca.wikidata = 'https://www.wikidata.org/wiki/Q448235'
SET person_6f0a331cc1ca.musicbrainz = 'https://musicbrainz.org/artist/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.isni_list = ['http://isni.org/isni/0000000078266176']
SET person_6f0a331cc1ca.source = 'musicbrainz.org'
SET person_6f0a331cc1ca.timestamp = timestamp()

MERGE (person_ae03cc4ea6bb:Person{ uuid: '0becbf36-027e-4b92-9689-ae03cc4ea6bb' })
SET person_ae03cc4ea6bb.name = 'Hampton Hawes'
SET person_ae03cc4ea6bb.gender = 'Male'
SET person_ae03cc4ea6bb.country = 'US'
SET person_ae03cc4ea6bb.viaf = 'http://viaf.org/viaf/115955414'
SET person_ae03cc4ea6bb.allmusic = 'http://www.allmusic.com/artist/mn0000558596'
SET person_ae03cc4ea6bb.wikipedia = 'https://en.wikipedia.org/wiki/Hampton_Hawes'
SET person_ae03cc4ea6bb.discogs = 'https://www.discogs.com/artist/59251'
SET person_ae03cc4ea6bb.wikidata = 'https://www.wikidata.org/wiki/Q1307036'
SET person_ae03cc4ea6bb.databases = ['https://rateyourmusic.com/artist/hampton_hawes']
SET person_ae03cc4ea6bb.musicbrainz = 'https://musicbrainz.org/artist/0becbf36-027e-4b92-9689-ae03cc4ea6bb'
SET person_ae03cc4ea6bb.isni_list = ['http://isni.org/isni/0000000084128618']
SET person_ae03cc4ea6bb.source = 'musicbrainz.org'
SET person_ae03cc4ea6bb.timestamp = timestamp()
// labels

MERGE (label_2d8831fa760f:Label{ uuid: '1f78d416-5a0d-43c5-9946-2d8831fa760f' })
SET label_2d8831fa760f.name= 'Enja Records'

// performances

MERGE (perf_af9ae9b383d2:Performance{ uuid: 'b44adb0b-12ce-4919-b029-af9ae9b383d2' })
SET perf_af9ae9b383d2.name = 'House Announcer'
SET perf_af9ae9b383d2.duration = '0:53'
SET perf_af9ae9b383d2.begin = '1973-06'
SET perf_af9ae9b383d2.end = '1973-06'
SET perf_af9ae9b383d2.source = 'musicbrainz.org'
SET perf_af9ae9b383d2.timestamp = timestamp()

MERGE (perf_41394d042c7b:Performance{ uuid: 'c54dde3e-6cf1-49f4-8280-41394d042c7b' })
SET perf_41394d042c7b.name = 'Stella by Starlight'
SET perf_41394d042c7b.duration = '12:57'
SET perf_41394d042c7b.begin = '1973-06'
SET perf_41394d042c7b.end = '1973-06'
SET perf_41394d042c7b.source = 'musicbrainz.org'
SET perf_41394d042c7b.timestamp = timestamp()

MERGE (perf_1bf3e2497da1:Performance{ uuid: '2c2a7670-51cf-4c9f-b335-1bf3e2497da1' })
SET perf_1bf3e2497da1.name = 'Bluebird'
SET perf_1bf3e2497da1.duration = '9:34'
SET perf_1bf3e2497da1.begin = '1973-06'
SET perf_1bf3e2497da1.end = '1973-06'
SET perf_1bf3e2497da1.source = 'musicbrainz.org'
SET perf_1bf3e2497da1.timestamp = timestamp()

MERGE (perf_cc85895de4a9:Performance{ uuid: 'a34826b9-ac75-40b2-81ac-cc85895de4a9' })
SET perf_cc85895de4a9.name = 'Spanish Moods'
SET perf_cc85895de4a9.duration = '14:57'
SET perf_cc85895de4a9.begin = '1973-06'
SET perf_cc85895de4a9.end = '1973-06'
SET perf_cc85895de4a9.source = 'musicbrainz.org'
SET perf_cc85895de4a9.timestamp = timestamp()

MERGE (perf_5d38c5e12446:Performance{ uuid: '4bc500a6-4a2c-4257-86f3-5d38c5e12446' })
SET perf_5d38c5e12446.name = 'St. Thomas'
SET perf_5d38c5e12446.duration = '7:14'
SET perf_5d38c5e12446.begin = '1973-06'
SET perf_5d38c5e12446.end = '1973-06'
SET perf_5d38c5e12446.source = 'musicbrainz.org'
SET perf_5d38c5e12446.timestamp = timestamp()



// labels
MERGE (release_c6541eb039a4)-[:HAS_LABEL]->(label_2d8831fa760f)


// tracks
MERGE (release_c6541eb039a4)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_af9ae9b383d2)
MERGE (release_c6541eb039a4)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_41394d042c7b)
MERGE (release_c6541eb039a4)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_1bf3e2497da1)
MERGE (release_c6541eb039a4)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_cc85895de4a9)
MERGE (release_c6541eb039a4)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_5d38c5e12446)

// works

MERGE (person_bad80243802a:Person{ uuid: '3b47247e-5b57-49b6-a0ed-bad80243802a' })
SET person_bad80243802a.name = 'Sonny Rollins'
SET person_bad80243802a.gender = 'Male'
SET person_bad80243802a.country = 'US'
SET person_bad80243802a.viaf = 'http://viaf.org/viaf/7368226'
SET person_bad80243802a.allmusic = 'http://www.allmusic.com/artist/mn0000039656'
SET person_bad80243802a.bbc = 'http://www.bbc.co.uk/music/artists/3b47247e-5b57-49b6-a0ed-bad80243802a'
SET person_bad80243802a.wikipedia = 'https://en.wikipedia.org/wiki/Sonny_Rollins'
SET person_bad80243802a.discogs = 'https://www.discogs.com/artist/145264'
SET person_bad80243802a.wikidata = 'https://www.wikidata.org/wiki/Q299208'
SET person_bad80243802a.databases = ['http://d-nb.info/gnd/118749552', 'https://rateyourmusic.com/artist/sonny_rollins', 'https://www.musik-sammler.de/artist/sonny-rollins/', 'https://www.worldcat.org/identities/lccn-n82-144213']
SET person_bad80243802a.musicbrainz = 'https://musicbrainz.org/artist/3b47247e-5b57-49b6-a0ed-bad80243802a'
SET person_bad80243802a.isni_list = ['http://isni.org/isni/0000000110367920']
SET person_bad80243802a.source = 'musicbrainz.org'
SET person_bad80243802a.timestamp = timestamp()

MERGE (person_c73775716312:Person{ uuid: 'c7356af9-9ea6-4a78-a55b-c73775716312' })
SET person_c73775716312.name = 'Charlie Parker'
SET person_c73775716312.gender = 'Male'
SET person_c73775716312.disambiguation = 'aka "Bird", jazz alto saxophonist'
SET person_c73775716312.country = 'US'
SET person_c73775716312.viaf = 'http://viaf.org/viaf/10034216'
SET person_c73775716312.allmusic = 'http://www.allmusic.com/artist/mn0000211758'
SET person_c73775716312.bbc = 'http://www.bbc.co.uk/music/artists/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.imdb = 'http://www.imdb.com/name/nm0662127/'
SET person_c73775716312.wikipedia = 'https://en.wikipedia.org/wiki/Charlie_Parker'
SET person_c73775716312.discogs = 'https://www.discogs.com/artist/75617'
SET person_c73775716312.wikidata = 'https://www.wikidata.org/wiki/Q103767'
SET person_c73775716312.discographies = ['http://www.jazzdisco.org/bird/', 'http://www.kyushu-ns.ac.jp/~allan/Documents/CP_M.html']
SET person_c73775716312.databases = ['http://rateyourmusic.com/artist/charlie_parker', 'https://www.musik-sammler.de/artist/charlie-parker/']
SET person_c73775716312.musicbrainz = 'https://musicbrainz.org/artist/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.isni_list = ['http://isni.org/isni/0000000120955806']
SET person_c73775716312.source = 'musicbrainz.org'
SET person_c73775716312.timestamp = timestamp()

MERGE (person_0cdf22c48565:Person{ uuid: '338f9d5d-9327-4f01-bb99-0cdf22c48565' })
SET person_0cdf22c48565.name = 'Victor Young'
SET person_0cdf22c48565.gender = 'Male'
SET person_0cdf22c48565.country = 'US'
SET person_0cdf22c48565.viaf = 'http://viaf.org/viaf/100232829'
SET person_0cdf22c48565.allmusic = 'http://www.allmusic.com/artist/mn0000959775'
SET person_0cdf22c48565.imdb = 'http://www.imdb.com/name/nm0000082/'
SET person_0cdf22c48565.wikipedia = 'https://en.wikipedia.org/wiki/Victor_Young'
SET person_0cdf22c48565.discogs = 'https://www.discogs.com/artist/370725'
SET person_0cdf22c48565.wikidata = 'https://www.wikidata.org/wiki/Q365199'
SET person_0cdf22c48565.databases = ['http://ibdb.com/person.php?id=12609', 'http://soundtrackcollector.com/composer/47/', 'https://rateyourmusic.com/artist/victor_young']
SET person_0cdf22c48565.musicbrainz = 'https://musicbrainz.org/artist/338f9d5d-9327-4f01-bb99-0cdf22c48565'
SET person_0cdf22c48565.isni_list = ['http://isni.org/isni/0000000116917487']
SET person_0cdf22c48565.source = 'musicbrainz.org'
SET person_0cdf22c48565.timestamp = timestamp()

MERGE (work_01e21de3052b:Work{ uuid: '5d0c44f3-0cf4-42ba-9957-01e21de3052b' })
SET work_01e21de3052b.name = 'Spanish Mood'
SET work_01e21de3052b.iswc = 'T-700.066.086-8'
SET work_01e21de3052b.type = 'Song'
SET work_01e21de3052b.source = 'musicbrainz.org'
SET work_01e21de3052b.timestamp = timestamp()

MERGE (work_55af2c96908a:Work{ uuid: '0abe6ce7-802a-3746-802a-55af2c96908a' })
SET work_55af2c96908a.name = 'St. Thomas'
SET work_55af2c96908a.type = 'Song'
SET work_55af2c96908a.source = 'musicbrainz.org'
SET work_55af2c96908a.timestamp = timestamp()

MERGE (work_1939b5fbded8:Work{ uuid: '36d6439b-55c0-4655-9ec8-1939b5fbded8' })
SET work_1939b5fbded8.name = 'Bluebird'
SET work_1939b5fbded8.type = 'Song'
SET work_1939b5fbded8.source = 'musicbrainz.org'
SET work_1939b5fbded8.timestamp = timestamp()

MERGE (work_8e1e602deada:Work{ uuid: 'cddc1524-251c-30a7-9cf0-8e1e602deada' })
SET work_8e1e602deada.name = 'Stella by Starlight'
SET work_8e1e602deada.iswc = 'T-070.137.735-6'
SET work_8e1e602deada.type = 'Song'
SET work_8e1e602deada.wikidata = 'https://www.wikidata.org/wiki/Q598915'
SET work_8e1e602deada.musicbrainz = 'https://musicbrainz.org/work/cddc1524-251c-30a7-9cf0-8e1e602deada'
SET work_8e1e602deada.source = 'musicbrainz.org'
SET work_8e1e602deada.timestamp = timestamp()


// performances of
MERGE (perf_cc85895de4a9)-[:PERFORMANCE_OF]->(work_01e21de3052b)
MERGE (perf_5d38c5e12446)-[:PERFORMANCE_OF]->(work_55af2c96908a)
MERGE (perf_1bf3e2497da1)-[:PERFORMANCE_OF]->(work_1939b5fbded8)
MERGE (perf_41394d042c7b)-[:PERFORMANCE_OF]->(work_8e1e602deada)


// composers
MERGE (person_ae03cc4ea6bb)-[:COMPOSED]->(work_01e21de3052b)
MERGE (person_bad80243802a)-[:COMPOSED]->(work_55af2c96908a)
MERGE (person_c73775716312)-[:COMPOSED]->(work_1939b5fbded8)
MERGE (person_0cdf22c48565)-[:COMPOSED]->(work_8e1e602deada)


// place nodes

MERGE (place_895e86c9956c:Place{ uuid: '3bf5bb2b-7277-44db-a5b0-895e86c9956c' })
SET place_895e86c9956c.name = 'Jazz Showcase'
SET place_895e86c9956c.address = 'Jazz Showcase, 806, South Plymouth Court, Dearborn Park, Chicago, Cook County, Illinois, 60611, United States of America'
SET place_895e86c9956c.lat = '41.8717526'
SET place_895e86c9956c.lng = '-87.6287938'
SET place_895e86c9956c.source = 'musicbrainz.org'


// place relationships
MERGE (perf_af9ae9b383d2)-[:HAS_PLACE { type: 'recorded at', begin: '1973-06', end: '1973-06' }]->(place_895e86c9956c)
MERGE (perf_41394d042c7b)-[:HAS_PLACE { type: 'recorded at', begin: '1973-06', end: '1973-06' }]->(place_895e86c9956c)
MERGE (perf_1bf3e2497da1)-[:HAS_PLACE { type: 'recorded at', begin: '1973-06', end: '1973-06' }]->(place_895e86c9956c)
MERGE (perf_cc85895de4a9)-[:HAS_PLACE { type: 'recorded at', begin: '1973-06', end: '1973-06' }]->(place_895e86c9956c)
MERGE (perf_5d38c5e12446)-[:HAS_PLACE { type: 'recorded at', begin: '1973-06', end: '1973-06' }]->(place_895e86c9956c)

MERGE (person_ae03cc4ea6bb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_41394d042c7b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_41394d042c7b)
MERGE (person_22a5fbaaf713)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_41394d042c7b)
MERGE (person_ae03cc4ea6bb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_1bf3e2497da1)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_1bf3e2497da1)
MERGE (person_22a5fbaaf713)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_1bf3e2497da1)
MERGE (person_ae03cc4ea6bb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_cc85895de4a9)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_cc85895de4a9)
MERGE (person_22a5fbaaf713)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_cc85895de4a9)
MERGE (person_ae03cc4ea6bb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5d38c5e12446)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_5d38c5e12446)
MERGE (person_22a5fbaaf713)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_5d38c5e12446)
