
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""


MERGE (release_9b2fe9761e20:Release{ uuid: '8b6162f0-2876-44b2-842c-9b2fe9761e20' })
SET release_9b2fe9761e20.name = 'We Three'
SET release_9b2fe9761e20.country = 'US'
SET release_9b2fe9761e20.date = '1958-11-14'
SET release_9b2fe9761e20.format = '12" Vinyl'
SET release_9b2fe9761e20.discode = 'NJ-8210'
SET release_9b2fe9761e20.discogs = 'http://www.discogs.com/release/3543935'
SET release_9b2fe9761e20.musicbrainz = 'http://musicbrainz.org/release/8b6162f0-2876-44b2-842c-9b2fe9761e20'
SET release_9b2fe9761e20.source = 'musicbrainz.org'


MERGE (person_7de13124b970:Person{ uuid: 'b6ff4fd0-03ae-41a6-942e-7de13124b970' }) 
SET person_7de13124b970.name = 'Paul Chambers'
SET person_7de13124b970.gender = 'Male'
SET person_7de13124b970.disambiguation = 'US jazz bassist'
SET person_7de13124b970.country = 'US'
SET person_7de13124b970.wikipedia = 'http://en.wikipedia.org/wiki/Paul_Chambers'
SET person_7de13124b970.viaf = 'http://viaf.org/viaf/100313280'
SET person_7de13124b970.discogs = 'http://www.discogs.com/artist/259778'
SET person_7de13124b970.wikidata = 'http://www.wikidata.org/wiki/Q541659'
SET person_7de13124b970.musicbrainz = 'https://musicbrainz.org/artist/b6ff4fd0-03ae-41a6-942e-7de13124b970'
SET person_7de13124b970.source = 'musicbrainz.org'


MERGE (person_0a240b6d10c9:Person{ uuid: 'e77a6903-a064-4048-b9b9-0a240b6d10c9' }) 
SET person_0a240b6d10c9.name = 'Phineas Newborn, Jr.'
SET person_0a240b6d10c9.gender = 'Male'
SET person_0a240b6d10c9.country = 'US'
SET person_0a240b6d10c9.wikipedia = 'http://en.wikipedia.org/wiki/Phineas_Newborn,_Jr.'
SET person_0a240b6d10c9.allmusic = 'http://www.allmusic.com/artist/mn0000335889'
SET person_0a240b6d10c9.discogs = 'http://www.discogs.com/artist/824909'
SET person_0a240b6d10c9.wikidata = 'http://www.wikidata.org/wiki/Q707599'
SET person_0a240b6d10c9.musicbrainz = 'https://musicbrainz.org/artist/e77a6903-a064-4048-b9b9-0a240b6d10c9'
SET person_0a240b6d10c9.source = 'musicbrainz.org'


MERGE (person_6f0a331cc1ca:Person{ uuid: '2c090b57-5e9d-49c5-9b71-6f0a331cc1ca' }) 
SET person_6f0a331cc1ca.name = 'Roy Haynes'
SET person_6f0a331cc1ca.gender = 'Male'
SET person_6f0a331cc1ca.country = 'US'
SET person_6f0a331cc1ca.wikipedia = 'http://en.wikipedia.org/wiki/Roy_Haynes'
SET person_6f0a331cc1ca.viaf = 'http://viaf.org/viaf/84975999'
SET person_6f0a331cc1ca.allmusic = 'http://www.allmusic.com/artist/mn0000290464'
SET person_6f0a331cc1ca.bbc = 'http://www.bbc.co.uk/music/artists/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.discogs = 'http://www.discogs.com/artist/255556'
SET person_6f0a331cc1ca.imdb = 'http://www.imdb.com/name/nm0371542/'
SET person_6f0a331cc1ca.wikidata = 'http://www.wikidata.org/wiki/Q448235'
SET person_6f0a331cc1ca.musicbrainz = 'https://musicbrainz.org/artist/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.source = 'musicbrainz.org'


MERGE (person_05d508e09a73:Person{ uuid: 'f0707f1d-55e1-46b6-8a9c-05d508e09a73' }) 
SET person_05d508e09a73.name = 'Rudy van Gelder'
SET person_05d508e09a73.gender = 'Male'
SET person_05d508e09a73.country = 'US'
SET person_05d508e09a73.wikipedia = 'http://en.wikipedia.org/wiki/Rudy_Van_Gelder'
SET person_05d508e09a73.viaf = 'http://viaf.org/viaf/33997197'
SET person_05d508e09a73.allmusic = 'http://www.allmusic.com/artist/mn0000305301'
SET person_05d508e09a73.discogs = 'http://www.discogs.com/artist/252966'
SET person_05d508e09a73.wikidata = 'http://www.wikidata.org/wiki/Q945681'
SET person_05d508e09a73.databases = ['http://rateyourmusic.com/artist/rudy_van_gelder']
SET person_05d508e09a73.musicbrainz = 'https://musicbrainz.org/artist/f0707f1d-55e1-46b6-8a9c-05d508e09a73'
SET person_05d508e09a73.isni_list = ['http://isni.org/isni/0000000019691076']
SET person_05d508e09a73.source = 'musicbrainz.org'


MERGE (person_b804df7fa6bb:Person{ uuid: '68c93572-8296-49ea-b94e-b804df7fa6bb' }) 
SET person_b804df7fa6bb.name = 'Esmond Edwards'
SET person_b804df7fa6bb.discogs = 'http://www.discogs.com/artist/254944'
SET person_b804df7fa6bb.musicbrainz = 'https://musicbrainz.org/artist/68c93572-8296-49ea-b94e-b804df7fa6bb'
SET person_b804df7fa6bb.source = 'musicbrainz.org'

// labels

MERGE (label_d510b586b396:Label{ uuid: '3690758a-3ec1-4fd3-a250-d510b586b396' })
SET label_d510b586b396.name= 'New Jazz'

// performances

MERGE (perf_bbea3daffeb7:Performance{ uuid: 'fdafa68d-b309-4f98-b3fe-bbea3daffeb7' })
SET perf_bbea3daffeb7.name = 'Reflection'
SET perf_bbea3daffeb7.duration = '4:21'
SET perf_bbea3daffeb7.begin_date = '1958-11-14'
SET perf_bbea3daffeb7.end_date = '1958-11-14'
SET perf_bbea3daffeb7.source = 'musicbrainz.org'


MERGE (perf_1c08b9e8c968:Performance{ uuid: '64d04739-f2ae-4b00-892f-1c08b9e8c968' })
SET perf_1c08b9e8c968.name = 'Sugar Ray'
SET perf_1c08b9e8c968.duration = '6:24'
SET perf_1c08b9e8c968.begin_date = '1958-11-14'
SET perf_1c08b9e8c968.end_date = '1958-11-14'
SET perf_1c08b9e8c968.source = 'musicbrainz.org'


MERGE (perf_334a8a3a4ddf:Performance{ uuid: '03efdfb2-dbdb-493b-afd6-334a8a3a4ddf' })
SET perf_334a8a3a4ddf.name = 'Solitaire'
SET perf_334a8a3a4ddf.duration = '8:50'
SET perf_334a8a3a4ddf.begin_date = '1958-11-14'
SET perf_334a8a3a4ddf.end_date = '1958-11-14'
SET perf_334a8a3a4ddf.source = 'musicbrainz.org'


MERGE (perf_a73108bfed4d:Performance{ uuid: '89fabf91-b971-4fad-a1a0-a73108bfed4d' })
SET perf_a73108bfed4d.name = 'After Hours'
SET perf_a73108bfed4d.duration = '11:18'
SET perf_a73108bfed4d.begin_date = '1958-11-14'
SET perf_a73108bfed4d.end_date = '1958-11-14'
SET perf_a73108bfed4d.source = 'musicbrainz.org'


MERGE (perf_c50dbbe879b6:Performance{ uuid: '11a3bf1a-4864-44b9-b567-c50dbbe879b6' })
SET perf_c50dbbe879b6.name = 'Sneakin\\' Around'
SET perf_c50dbbe879b6.duration = '4:22'
SET perf_c50dbbe879b6.begin_date = '1958-11-14'
SET perf_c50dbbe879b6.end_date = '1958-11-14'
SET perf_c50dbbe879b6.source = 'musicbrainz.org'


MERGE (perf_5f5e00f800f9:Performance{ uuid: 'feedca3b-e48e-46c7-9ea1-5f5e00f800f9' })
SET perf_5f5e00f800f9.name = 'Our Delight'
SET perf_5f5e00f800f9.duration = '4:00'
SET perf_5f5e00f800f9.begin_date = '1958-11-14'
SET perf_5f5e00f800f9.end_date = '1958-11-14'
SET perf_5f5e00f800f9.source = 'musicbrainz.org'




// labels
MERGE (release_9b2fe9761e20)-[:HAS_LABEL]->(label_d510b586b396)


// tracks
MERGE (release_9b2fe9761e20)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_bbea3daffeb7)
MERGE (release_9b2fe9761e20)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_1c08b9e8c968)
MERGE (release_9b2fe9761e20)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_334a8a3a4ddf)
MERGE (release_9b2fe9761e20)-[:HAS_TRACK {name: 'B1', sequence: 4}]->(perf_a73108bfed4d)
MERGE (release_9b2fe9761e20)-[:HAS_TRACK {name: 'B2', sequence: 5}]->(perf_c50dbbe879b6)
MERGE (release_9b2fe9761e20)-[:HAS_TRACK {name: 'B3', sequence: 6}]->(perf_5f5e00f800f9)

// works

MERGE (person_931a54846f84:Person{ uuid: '5e95d04a-a9cb-49f6-99f3-931a54846f84' }) 
SET person_931a54846f84.name = 'Reneé Borek'
SET person_931a54846f84.source = 'musicbrainz.org'


MERGE (person_b2577f0db548:Person{ uuid: '2ebdd071-96b6-4869-b3bf-b2577f0db548' }) 
SET person_b2577f0db548.name = 'Carl Nutter'
SET person_b2577f0db548.gender = 'Male'
SET person_b2577f0db548.source = 'musicbrainz.org'


MERGE (person_3345ea8ba761:Person{ uuid: '52763c17-465b-48e9-9e2b-3345ea8ba761' }) 
SET person_3345ea8ba761.name = 'Tadd Dameron'
SET person_3345ea8ba761.gender = 'Male'
SET person_3345ea8ba761.country = 'US'
SET person_3345ea8ba761.wikipedia = 'http://en.wikipedia.org/wiki/Tadd_Dameron'
SET person_3345ea8ba761.viaf = 'http://viaf.org/viaf/7554707'
SET person_3345ea8ba761.allmusic = 'http://www.allmusic.com/artist/mn0000016759'
SET person_3345ea8ba761.discogs = 'http://www.discogs.com/artist/251783'
SET person_3345ea8ba761.wikidata = 'http://www.wikidata.org/wiki/Q498736'
SET person_3345ea8ba761.musicbrainz = 'https://musicbrainz.org/artist/52763c17-465b-48e9-9e2b-3345ea8ba761'
SET person_3345ea8ba761.source = 'musicbrainz.org'


MERGE (person_50eee4665342:Person{ uuid: 'd506bd73-942c-4055-b89e-50eee4665342' }) 
SET person_50eee4665342.name = 'Avery Parrish'
SET person_50eee4665342.gender = 'Male'
SET person_50eee4665342.country = 'US'
SET person_50eee4665342.wikipedia = 'http://en.wikipedia.org/wiki/Avery_Parrish'
SET person_50eee4665342.allmusic = 'http://www.allmusic.com/artist/mn0000063735'
SET person_50eee4665342.discogs = 'http://www.discogs.com/artist/732209'
SET person_50eee4665342.wikidata = 'http://www.wikidata.org/wiki/Q790660'
SET person_50eee4665342.musicbrainz = 'https://musicbrainz.org/artist/d506bd73-942c-4055-b89e-50eee4665342'
SET person_50eee4665342.isni_list = ['http://isni.org/isni/0000000059369655']
SET person_50eee4665342.source = 'musicbrainz.org'


MERGE (person_0ee1f149d993:Person{ uuid: '4c2b8324-d69f-4464-baf2-0ee1f149d993' }) 
SET person_0ee1f149d993.name = 'King Guion'
SET person_0ee1f149d993.gender = 'Male'
SET person_0ee1f149d993.source = 'musicbrainz.org'


MERGE (person_2b5190ea3e38:Person{ uuid: '7feee525-a8ff-4a59-85f6-2b5190ea3e38' }) 
SET person_2b5190ea3e38.name = 'Ray Bryant'
SET person_2b5190ea3e38.gender = 'Male'
SET person_2b5190ea3e38.country = 'US'
SET person_2b5190ea3e38.wikipedia = 'http://en.wikipedia.org/wiki/Ray_Bryant'
SET person_2b5190ea3e38.viaf = 'http://viaf.org/viaf/119766558'
SET person_2b5190ea3e38.allmusic = 'http://www.allmusic.com/artist/mn0000869265'
SET person_2b5190ea3e38.discogs = 'http://www.discogs.com/artist/98585'
SET person_2b5190ea3e38.wikidata = 'http://www.wikidata.org/wiki/Q492143'
SET person_2b5190ea3e38.databases = ['https://rateyourmusic.com/artist/ray_bryant']
SET person_2b5190ea3e38.musicbrainz = 'https://musicbrainz.org/artist/7feee525-a8ff-4a59-85f6-2b5190ea3e38'
SET person_2b5190ea3e38.isni_list = ['http://isni.org/isni/0000000077322949', 'http://isni.org/isni/0000000114634846']
SET person_2b5190ea3e38.source = 'musicbrainz.org'


MERGE (work_347f904882c9:Work{ uuid: '05289922-ad8e-37a4-8c7a-347f904882c9' })
SET work_347f904882c9.name = 'Reflection'
SET work_347f904882c9.source = 'musicbrainz.org'


MERGE (work_6397a4cf8fc1:Work{ uuid: '9d13a3cd-3eaa-46b3-b108-6397a4cf8fc1' })
SET work_6397a4cf8fc1.name = 'Sugar Ray'
SET work_6397a4cf8fc1.iswc = 'T-700.068.135-8'
SET work_6397a4cf8fc1.type = 'Song'
SET work_6397a4cf8fc1.source = 'musicbrainz.org'


MERGE (work_d44bf3a8267a:Work{ uuid: '8ca8f1e7-e703-4928-84d8-d44bf3a8267a' })
SET work_d44bf3a8267a.name = 'Solitaire'
SET work_d44bf3a8267a.type = 'Song'
SET work_d44bf3a8267a.source = 'musicbrainz.org'


MERGE (work_bd21241fd538:Work{ uuid: 'c442f906-a24b-4f48-9208-bd21241fd538' })
SET work_bd21241fd538.name = 'After Hours'
SET work_bd21241fd538.type = 'Song'
SET work_bd21241fd538.wikidata = 'http://www.wikidata.org/wiki/Q4690511'
SET work_bd21241fd538.musicbrainz = 'https://musicbrainz.org/work/c442f906-a24b-4f48-9208-bd21241fd538'
SET work_bd21241fd538.source = 'musicbrainz.org'


MERGE (work_1ba97413425f:Work{ uuid: 'd19f859b-28eb-4422-98a4-1ba97413425f' })
SET work_1ba97413425f.name = 'Sneakin\\' Around'
SET work_1ba97413425f.type = 'Song'
SET work_1ba97413425f.source = 'musicbrainz.org'


MERGE (work_98220f5c81a2:Work{ uuid: 'd667490d-0af7-4672-a94d-98220f5c81a2' })
SET work_98220f5c81a2.name = 'Our Delight'
SET work_98220f5c81a2.type = 'Song'
SET work_98220f5c81a2.source = 'musicbrainz.org'



// performances of
MERGE (perf_bbea3daffeb7)-[:PERFORMANCE_OF]->(work_347f904882c9)
MERGE (perf_1c08b9e8c968)-[:PERFORMANCE_OF]->(work_6397a4cf8fc1)
MERGE (perf_334a8a3a4ddf)-[:PERFORMANCE_OF]->(work_d44bf3a8267a)
MERGE (perf_a73108bfed4d)-[:PERFORMANCE_OF]->(work_bd21241fd538)
MERGE (perf_c50dbbe879b6)-[:PERFORMANCE_OF]->(work_1ba97413425f)
MERGE (perf_5f5e00f800f9)-[:PERFORMANCE_OF]->(work_98220f5c81a2)


// composers
MERGE (person_2b5190ea3e38)-[:COMPOSED]->(work_347f904882c9)
MERGE (person_0a240b6d10c9)-[:COMPOSED]->(work_6397a4cf8fc1)
MERGE (person_b2577f0db548)-[:COMPOSED]->(work_d44bf3a8267a)
MERGE (person_0ee1f149d993)-[:COMPOSED]->(work_d44bf3a8267a)
MERGE (person_931a54846f84)-[:COMPOSED]->(work_d44bf3a8267a)
MERGE (person_50eee4665342)-[:COMPOSED]->(work_bd21241fd538)
MERGE (person_2b5190ea3e38)-[:COMPOSED]->(work_1ba97413425f)
MERGE (person_3345ea8ba761)-[:COMPOSED]->(work_98220f5c81a2)

// place nodes

MERGE (place_fa7e90fdbab8:Place{ uuid: 'c7227463-931e-406a-8138-fa7e90fdbab8' })
SET place_fa7e90fdbab8.name = 'Van Gelder Studio'
SET place_fa7e90fdbab8.address = '25, Prospect Avenue, Hackensack, Bergen County, New Jersey, 07601, United States of America'
SET place_fa7e90fdbab8.lat = '40.8841946428571'
SET place_fa7e90fdbab8.lng = '-74.0579705'
SET place_fa7e90fdbab8.source = 'musicbrainz.org'


// place relationships
MERGE (perf_bbea3daffeb7)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-11-14', end_date: '1958-11-14' }]->(place_fa7e90fdbab8)
MERGE (perf_1c08b9e8c968)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-11-14', end_date: '1958-11-14' }]->(place_fa7e90fdbab8)
MERGE (perf_334a8a3a4ddf)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-11-14', end_date: '1958-11-14' }]->(place_fa7e90fdbab8)
MERGE (perf_a73108bfed4d)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-11-14', end_date: '1958-11-14' }]->(place_fa7e90fdbab8)
MERGE (perf_c50dbbe879b6)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-11-14', end_date: '1958-11-14' }]->(place_fa7e90fdbab8)
MERGE (perf_5f5e00f800f9)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-11-14', end_date: '1958-11-14' }]->(place_fa7e90fdbab8)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_bbea3daffeb7)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_bbea3daffeb7)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_bbea3daffeb7)
MERGE (person_0a240b6d10c9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bbea3daffeb7)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_bbea3daffeb7)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_1c08b9e8c968)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_1c08b9e8c968)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_1c08b9e8c968)
MERGE (person_0a240b6d10c9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_1c08b9e8c968)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_1c08b9e8c968)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_334a8a3a4ddf)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_334a8a3a4ddf)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_334a8a3a4ddf)
MERGE (person_0a240b6d10c9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_334a8a3a4ddf)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_334a8a3a4ddf)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_a73108bfed4d)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_a73108bfed4d)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a73108bfed4d)
MERGE (person_0a240b6d10c9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a73108bfed4d)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a73108bfed4d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_c50dbbe879b6)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_c50dbbe879b6)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_c50dbbe879b6)
MERGE (person_0a240b6d10c9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_c50dbbe879b6)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_c50dbbe879b6)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_5f5e00f800f9)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_5f5e00f800f9)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_5f5e00f800f9)
MERGE (person_0a240b6d10c9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5f5e00f800f9)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_5f5e00f800f9)



"""
)