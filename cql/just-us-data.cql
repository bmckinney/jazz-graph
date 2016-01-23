
MERGE (release_8ca6fae1264e:Release{ uuid: '78e71895-5953-3c2e-b6ba-8ca6fae1264e' })
SET release_8ca6fae1264e.name = 'Just Us'
SET release_8ca6fae1264e.country = 'JP'
SET release_8ca6fae1264e.date = '2000-01-21'
SET release_8ca6fae1264e.format = 'CD'
SET release_8ca6fae1264e.discode = 'VICJ-60469'
SET release_8ca6fae1264e.musicbrainz = 'http://musicbrainz.org/release/78e71895-5953-3c2e-b6ba-8ca6fae1264e'
SET release_8ca6fae1264e.source = 'musicbrainz.org'
SET release_8ca6fae1264e.timestamp = timestamp()

MERGE (person_15c256572eeb:Person{ uuid: '663e0a03-7bef-4023-a788-15c256572eeb' })
SET person_15c256572eeb.name = 'Eddie DeHaas'
SET person_15c256572eeb.gender = 'Male'
SET person_15c256572eeb.source = 'musicbrainz.org'
SET person_15c256572eeb.timestamp = timestamp()

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
SET person_6f0a331cc1ca.timestamp = timestamp()

MERGE (person_ceec49387371:Person{ uuid: 'c7f9dc85-ebff-4a0c-8957-ceec49387371' })
SET person_ceec49387371.name = 'Richard Wyands'
SET person_ceec49387371.gender = 'Male'
SET person_ceec49387371.country = 'US'
SET person_ceec49387371.wikipedia = 'http://en.wikipedia.org/wiki/Richard_Wyands'
SET person_ceec49387371.viaf = 'http://viaf.org/viaf/27253612'
SET person_ceec49387371.allmusic = 'http://www.allmusic.com/artist/mn0000850987'
SET person_ceec49387371.discogs = 'http://www.discogs.com/artist/278730'
SET person_ceec49387371.wikidata = 'http://www.wikidata.org/wiki/Q2150973'
SET person_ceec49387371.musicbrainz = 'https://musicbrainz.org/artist/c7f9dc85-ebff-4a0c-8957-ceec49387371'
SET person_ceec49387371.source = 'musicbrainz.org'
SET person_ceec49387371.timestamp = timestamp()
// labels

MERGE (label_f72e264c0f66:Label{ uuid: '11847c89-4b2c-4866-84c3-f72e264c0f66' })
SET label_f72e264c0f66.name= 'Prestige'

// performances

MERGE (perf_a1aa979861b5:Performance{ uuid: 'eb8dcc28-b03d-4d4a-b6be-a1aa979861b5' })
SET perf_a1aa979861b5.name = 'Down Home'
SET perf_a1aa979861b5.duration = '7:29'
SET perf_a1aa979861b5.begin = '1960-07-05'
SET perf_a1aa979861b5.end = '1960-07-05'
SET perf_a1aa979861b5.source = 'musicbrainz.org'
SET perf_a1aa979861b5.timestamp = timestamp()

MERGE (perf_43efb8c88986:Performance{ uuid: '7168e4db-fc82-4592-9a6b-43efb8c88986' })
SET perf_43efb8c88986.name = 'Sweet and Lovely'
SET perf_43efb8c88986.duration = '6:59'
SET perf_43efb8c88986.begin = '1960-07-05'
SET perf_43efb8c88986.end = '1960-07-05'
SET perf_43efb8c88986.source = 'musicbrainz.org'
SET perf_43efb8c88986.timestamp = timestamp()

MERGE (perf_a7f9c8902ea0:Performance{ uuid: '0c560d88-a6d6-474b-9d34-a7f9c8902ea0' })
SET perf_a7f9c8902ea0.name = 'As Long as There\'s Music'
SET perf_a7f9c8902ea0.duration = '3:46'
SET perf_a7f9c8902ea0.begin = '1960-07-05'
SET perf_a7f9c8902ea0.end = '1960-07-05'
SET perf_a7f9c8902ea0.source = 'musicbrainz.org'
SET perf_a7f9c8902ea0.timestamp = timestamp()

MERGE (perf_7d7692083d82:Performance{ uuid: '0004236f-1f6b-4d53-ac54-7d7692083d82' })
SET perf_7d7692083d82.name = 'Well Now'
SET perf_7d7692083d82.duration = '1:59'
SET perf_7d7692083d82.begin = '1960-07-05'
SET perf_7d7692083d82.end = '1960-07-05'
SET perf_7d7692083d82.source = 'musicbrainz.org'
SET perf_7d7692083d82.timestamp = timestamp()

MERGE (perf_b6b236622a8d:Performance{ uuid: '47880e6f-4179-4848-9b79-b6b236622a8d' })
SET perf_b6b236622a8d.name = 'Cymbalism'
SET perf_b6b236622a8d.duration = '7:02'
SET perf_b6b236622a8d.begin = '1960-07-05'
SET perf_b6b236622a8d.end = '1960-07-05'
SET perf_b6b236622a8d.source = 'musicbrainz.org'
SET perf_b6b236622a8d.timestamp = timestamp()

MERGE (perf_e634084a87fd:Performance{ uuid: '4ea309a6-97f4-4380-bbbd-e634084a87fd' })
SET perf_e634084a87fd.name = 'Con Alma'
SET perf_e634084a87fd.duration = '6:34'
SET perf_e634084a87fd.begin = '1960-07-05'
SET perf_e634084a87fd.end = '1960-07-05'
SET perf_e634084a87fd.source = 'musicbrainz.org'
SET perf_e634084a87fd.timestamp = timestamp()

MERGE (perf_11f71603068f:Performance{ uuid: 'db1070a0-26bc-475c-a459-11f71603068f' })
SET perf_11f71603068f.name = 'Speak Low'
SET perf_11f71603068f.duration = '7:04'
SET perf_11f71603068f.begin = '1960-07-05'
SET perf_11f71603068f.end = '1960-07-05'
SET perf_11f71603068f.source = 'musicbrainz.org'
SET perf_11f71603068f.timestamp = timestamp()



// labels
MERGE (release_8ca6fae1264e)-[:HAS_LABEL]->(label_f72e264c0f66)


// tracks
MERGE (release_8ca6fae1264e)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_a1aa979861b5)
MERGE (release_8ca6fae1264e)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_43efb8c88986)
MERGE (release_8ca6fae1264e)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_a7f9c8902ea0)
MERGE (release_8ca6fae1264e)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_7d7692083d82)
MERGE (release_8ca6fae1264e)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_b6b236622a8d)
MERGE (release_8ca6fae1264e)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_e634084a87fd)
MERGE (release_8ca6fae1264e)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_11f71603068f)

// works

MERGE (person_3fbbe73d09b4:Person{ uuid: '1b3a1e49-2494-441c-9818-3fbbe73d09b4' })
SET person_3fbbe73d09b4.name = 'Jule Styne'
SET person_3fbbe73d09b4.gender = 'Male'
SET person_3fbbe73d09b4.country = 'GB'
SET person_3fbbe73d09b4.wikipedia = 'http://en.wikipedia.org/wiki/Jule_Styne'
SET person_3fbbe73d09b4.viaf = 'http://viaf.org/viaf/94213715'
SET person_3fbbe73d09b4.allmusic = 'http://www.allmusic.com/artist/mn0000304458'
SET person_3fbbe73d09b4.discogs = 'http://www.discogs.com/artist/341663'
SET person_3fbbe73d09b4.imdb = 'http://www.imdb.com/name/nm0006312/'
SET person_3fbbe73d09b4.wikidata = 'http://www.wikidata.org/wiki/Q587741'
SET person_3fbbe73d09b4.databases = ['http://ibdb.com/person.php?id=12466', 'http://rateyourmusic.com/artist/jule_styne']
SET person_3fbbe73d09b4.musicbrainz = 'https://musicbrainz.org/artist/1b3a1e49-2494-441c-9818-3fbbe73d09b4'
SET person_3fbbe73d09b4.isni_list = ['http://isni.org/isni/0000000114778217']
SET person_3fbbe73d09b4.source = 'musicbrainz.org'
SET person_3fbbe73d09b4.timestamp = timestamp()

MERGE (person_65998d0d35b5:Person{ uuid: 'e9ba8ccb-505f-4e5c-b909-65998d0d35b5' })
SET person_65998d0d35b5.name = 'Dizzy Gillespie'
SET person_65998d0d35b5.gender = 'Male'
SET person_65998d0d35b5.country = 'US'
SET person_65998d0d35b5.wikipedia = 'http://en.wikipedia.org/wiki/Dizzy_Gillespie'
SET person_65998d0d35b5.viaf = 'http://viaf.org/viaf/77110276'
SET person_65998d0d35b5.allmusic = 'http://www.allmusic.com/artist/mn0000162677'
SET person_65998d0d35b5.bbc = 'http://www.bbc.co.uk/music/artists/e9ba8ccb-505f-4e5c-b909-65998d0d35b5'
SET person_65998d0d35b5.discogs = 'http://www.discogs.com/artist/64694'
SET person_65998d0d35b5.wikidata = 'http://www.wikidata.org/wiki/Q49575'
SET person_65998d0d35b5.discographies = ['http://www.jazzdisco.org/dizzy-gillespie/']
SET person_65998d0d35b5.databases = ['http://rateyourmusic.com/artist/dizzy_gillespie']
SET person_65998d0d35b5.musicbrainz = 'https://musicbrainz.org/artist/e9ba8ccb-505f-4e5c-b909-65998d0d35b5'
SET person_65998d0d35b5.isni_list = ['http://isni.org/isni/0000000109181520']
SET person_65998d0d35b5.source = 'musicbrainz.org'
SET person_65998d0d35b5.timestamp = timestamp()

MERGE (person_b25208100fd0:Person{ uuid: '2d5efda1-5547-48dd-9a0f-b25208100fd0' })
SET person_b25208100fd0.name = 'Charles N. Daniels'
SET person_b25208100fd0.gender = 'Male'
SET person_b25208100fd0.disambiguation = 'US composer'
SET person_b25208100fd0.country = 'US'
SET person_b25208100fd0.wikipedia = 'http://en.wikipedia.org/wiki/Charles_N._Daniels_(music)'
SET person_b25208100fd0.discogs = 'http://www.discogs.com/artist/917383'
SET person_b25208100fd0.wikidata = 'http://www.wikidata.org/wiki/Q5081189'
SET person_b25208100fd0.musicbrainz = 'https://musicbrainz.org/artist/2d5efda1-5547-48dd-9a0f-b25208100fd0'
SET person_b25208100fd0.source = 'musicbrainz.org'
SET person_b25208100fd0.timestamp = timestamp()

MERGE (person_b35a9c6f0316:Person{ uuid: '006307bc-af41-4da1-aa11-b35a9c6f0316' })
SET person_b35a9c6f0316.name = 'Curtis Fuller'
SET person_b35a9c6f0316.gender = 'Male'
SET person_b35a9c6f0316.country = 'US'
SET person_b35a9c6f0316.wikipedia = 'http://en.wikipedia.org/wiki/Curtis_Fuller'
SET person_b35a9c6f0316.viaf = 'http://viaf.org/viaf/86418036'
SET person_b35a9c6f0316.allmusic = 'http://www.allmusic.com/artist/mn0000139566'
SET person_b35a9c6f0316.discogs = 'http://www.discogs.com/artist/257250'
SET person_b35a9c6f0316.wikidata = 'http://www.wikidata.org/wiki/Q1145565'
SET person_b35a9c6f0316.musicbrainz = 'https://musicbrainz.org/artist/006307bc-af41-4da1-aa11-b35a9c6f0316'
SET person_b35a9c6f0316.isni_list = ['http://isni.org/isni/0000000114509340']
SET person_b35a9c6f0316.source = 'musicbrainz.org'
SET person_b35a9c6f0316.timestamp = timestamp()

MERGE (person_ed56a0d6c7fc:Person{ uuid: 'c24c5333-1e31-4971-b786-ed56a0d6c7fc' })
SET person_ed56a0d6c7fc.name = 'Gus Arnheim'
SET person_ed56a0d6c7fc.gender = 'Male'
SET person_ed56a0d6c7fc.country = 'US'
SET person_ed56a0d6c7fc.wikipedia = 'http://en.wikipedia.org/wiki/Gus_Arnheim'
SET person_ed56a0d6c7fc.imdb = 'http://www.imdb.com/name/nm0036280/'
SET person_ed56a0d6c7fc.wikidata = 'http://www.wikidata.org/wiki/Q135420'
SET person_ed56a0d6c7fc.musicbrainz = 'https://musicbrainz.org/artist/c24c5333-1e31-4971-b786-ed56a0d6c7fc'
SET person_ed56a0d6c7fc.source = 'musicbrainz.org'
SET person_ed56a0d6c7fc.timestamp = timestamp()

MERGE (person_4f7500861060:Person{ uuid: '0e738f68-783c-4a6a-80ae-4f7500861060' })
SET person_4f7500861060.name = 'Kurt Weill'
SET person_4f7500861060.gender = 'Male'
SET person_4f7500861060.country = 'DE'
SET person_4f7500861060.wikipedia = 'http://en.wikipedia.org/wiki/Kurt_Weill'
SET person_4f7500861060.viaf = 'http://viaf.org/viaf/76501825'
SET person_4f7500861060.allmusic = 'http://www.allmusic.com/artist/mn0000683446'
SET person_4f7500861060.discogs = 'http://www.discogs.com/artist/407111'
SET person_4f7500861060.imdb = 'http://www.imdb.com/name/nm0918044/'
SET person_4f7500861060.wikidata = 'http://www.wikidata.org/wiki/Q55004'
SET person_4f7500861060.databases = ['http://ibdb.com/person.php?id=7112', 'https://rateyourmusic.com/artist/kurt_weill']
SET person_4f7500861060.musicbrainz = 'https://musicbrainz.org/artist/0e738f68-783c-4a6a-80ae-4f7500861060'
SET person_4f7500861060.isni_list = ['http://isni.org/isni/0000000114753562']
SET person_4f7500861060.source = 'musicbrainz.org'
SET person_4f7500861060.timestamp = timestamp()

MERGE (work_c714a14941d2:Work{ uuid: 'c77345a8-18fb-4170-ad4b-c714a14941d2' })
SET work_c714a14941d2.name = 'Down Home'
SET work_c714a14941d2.type = 'Song'
SET work_c714a14941d2.source = 'musicbrainz.org'
SET work_c714a14941d2.timestamp = timestamp()

MERGE (work_f86be1ae6c62:Work{ uuid: '9d5bae50-2991-3d93-9e6a-f86be1ae6c62' })
SET work_f86be1ae6c62.name = 'Sweet and Lovely'
SET work_f86be1ae6c62.iswc = 'T-070.138.671-1'
SET work_f86be1ae6c62.type = 'Song'
SET work_f86be1ae6c62.musicbrainz = 'https://musicbrainz.org/work/9d5bae50-2991-3d93-9e6a-f86be1ae6c62'
SET work_f86be1ae6c62.source = 'musicbrainz.org'
SET work_f86be1ae6c62.timestamp = timestamp()

MERGE (work_4676886257ee:Work{ uuid: '71acd4fa-8678-4185-90ef-4676886257ee' })
SET work_4676886257ee.name = 'As Long as There\'s Music'
SET work_4676886257ee.type = 'Song'
SET work_4676886257ee.source = 'musicbrainz.org'
SET work_4676886257ee.timestamp = timestamp()

MERGE (work_f2d5a99d852f:Work{ uuid: 'd65fbba5-10cd-42da-a2a3-f2d5a99d852f' })
SET work_f2d5a99d852f.name = 'Well Now'
SET work_f2d5a99d852f.type = 'Song'
SET work_f2d5a99d852f.source = 'musicbrainz.org'
SET work_f2d5a99d852f.timestamp = timestamp()

MERGE (work_8ba0d64d22a1:Work{ uuid: '2ed25674-408b-4fe9-9bc0-8ba0d64d22a1' })
SET work_8ba0d64d22a1.name = 'Cymbalism'
SET work_8ba0d64d22a1.type = 'Song'
SET work_8ba0d64d22a1.source = 'musicbrainz.org'
SET work_8ba0d64d22a1.timestamp = timestamp()

MERGE (work_ec918ff7c18b:Work{ uuid: 'c2f72471-0d70-4d32-937c-ec918ff7c18b' })
SET work_ec918ff7c18b.name = 'Con Alma'
SET work_ec918ff7c18b.iswc = 'T-070.025.690-1'
SET work_ec918ff7c18b.type = 'Song'
SET work_ec918ff7c18b.wikidata = 'http://www.wikidata.org/wiki/Q1123428'
SET work_ec918ff7c18b.musicbrainz = 'https://musicbrainz.org/work/c2f72471-0d70-4d32-937c-ec918ff7c18b'
SET work_ec918ff7c18b.source = 'musicbrainz.org'
SET work_ec918ff7c18b.timestamp = timestamp()

MERGE (work_13a3125d3c19:Work{ uuid: '9721f999-fdb5-3331-94da-13a3125d3c19' })
SET work_13a3125d3c19.name = 'One Touch of Venus: Speak Low'
SET work_13a3125d3c19.type = 'Song'
SET work_13a3125d3c19.wikidata = 'http://www.wikidata.org/wiki/Q1799926'
SET work_13a3125d3c19.musicbrainz = 'https://musicbrainz.org/work/9721f999-fdb5-3331-94da-13a3125d3c19'
SET work_13a3125d3c19.source = 'musicbrainz.org'
SET work_13a3125d3c19.timestamp = timestamp()


// performances of
MERGE (perf_a1aa979861b5)-[:PERFORMANCE_OF]->(work_c714a14941d2)
MERGE (perf_43efb8c88986)-[:PERFORMANCE_OF]->(work_f86be1ae6c62)
MERGE (perf_a7f9c8902ea0)-[:PERFORMANCE_OF]->(work_4676886257ee)
MERGE (perf_7d7692083d82)-[:PERFORMANCE_OF]->(work_f2d5a99d852f)
MERGE (perf_b6b236622a8d)-[:PERFORMANCE_OF]->(work_8ba0d64d22a1)
MERGE (perf_e634084a87fd)-[:PERFORMANCE_OF]->(work_ec918ff7c18b)
MERGE (perf_11f71603068f)-[:PERFORMANCE_OF]->(work_13a3125d3c19)


// composers
MERGE (person_b35a9c6f0316)-[:COMPOSED]->(work_c714a14941d2)
MERGE (person_b25208100fd0)-[:COMPOSED]->(work_f86be1ae6c62)
MERGE (person_ed56a0d6c7fc)-[:COMPOSED]->(work_f86be1ae6c62)
MERGE (person_3fbbe73d09b4)-[:COMPOSED]->(work_4676886257ee)
MERGE (person_6f0a331cc1ca)-[:COMPOSED]->(work_f2d5a99d852f)
MERGE (person_6f0a331cc1ca)-[:COMPOSED]->(work_8ba0d64d22a1)
MERGE (person_ceec49387371)-[:COMPOSED]->(work_8ba0d64d22a1)
MERGE (person_65998d0d35b5)-[:COMPOSED]->(work_ec918ff7c18b)
MERGE (person_4f7500861060)-[:COMPOSED]->(work_13a3125d3c19)


// place nodes

MERGE (place_569fa8b97644:Place{ uuid: '1165ef7d-371c-4e03-98db-569fa8b97644' })
SET place_569fa8b97644.name = 'Van Gelder Studio'
SET place_569fa8b97644.address = '445, Sylvan Avenue, Englewood Cliffs, Bergen County, New Jersey, 07632, United States of America'
SET place_569fa8b97644.lat = '40.8764374074488'
SET place_569fa8b97644.lng = '-73.9519546846822'
SET place_569fa8b97644.source = 'musicbrainz.org'

MERGE (place_decbb365c07f:Place{ uuid: '74e50e58-5deb-4b99-93a2-decbb365c07f' })
SET place_decbb365c07f.name = 'New York'
SET place_decbb365c07f.source = 'musicbrainz.org'


// place relationships
MERGE (perf_a1aa979861b5)-[:HAS_PLACE { type: 'recorded at', begin: '1960-07-05', end: '1960-07-05' }]->(place_569fa8b97644)
MERGE (perf_a1aa979861b5)-[:HAS_PLACE { type: 'recorded in', begin: '1960-07-05', end: '1960-07-05' }]->(place_decbb365c07f)
MERGE (perf_43efb8c88986)-[:HAS_PLACE { type: 'recorded at', begin: '1960-07-05', end: '1960-07-05' }]->(place_569fa8b97644)
MERGE (perf_43efb8c88986)-[:HAS_PLACE { type: 'recorded in', begin: '1960-07-05', end: '1960-07-05' }]->(place_decbb365c07f)
MERGE (perf_a7f9c8902ea0)-[:HAS_PLACE { type: 'recorded at', begin: '1960-07-05', end: '1960-07-05' }]->(place_569fa8b97644)
MERGE (perf_a7f9c8902ea0)-[:HAS_PLACE { type: 'recorded in', begin: '1960-07-05', end: '1960-07-05' }]->(place_decbb365c07f)
MERGE (perf_7d7692083d82)-[:HAS_PLACE { type: 'recorded at', begin: '1960-07-05', end: '1960-07-05' }]->(place_569fa8b97644)
MERGE (perf_b6b236622a8d)-[:HAS_PLACE { type: 'recorded at', begin: '1960-07-05', end: '1960-07-05' }]->(place_569fa8b97644)
MERGE (perf_e634084a87fd)-[:HAS_PLACE { type: 'recorded at', begin: '1960-07-05', end: '1960-07-05' }]->(place_569fa8b97644)
MERGE (perf_11f71603068f)-[:HAS_PLACE { type: 'recorded at', begin: '1960-07-05', end: '1960-07-05' }]->(place_569fa8b97644)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_a1aa979861b5)
MERGE (person_15c256572eeb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a1aa979861b5)
MERGE (person_ceec49387371)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a1aa979861b5)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_43efb8c88986)
MERGE (person_15c256572eeb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_43efb8c88986)
MERGE (person_ceec49387371)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_43efb8c88986)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_a7f9c8902ea0)
MERGE (person_15c256572eeb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a7f9c8902ea0)
MERGE (person_ceec49387371)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a7f9c8902ea0)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_7d7692083d82)
MERGE (person_15c256572eeb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_7d7692083d82)
MERGE (person_ceec49387371)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_7d7692083d82)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_b6b236622a8d)
MERGE (person_15c256572eeb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_b6b236622a8d)
MERGE (person_ceec49387371)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b6b236622a8d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_e634084a87fd)
MERGE (person_15c256572eeb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_e634084a87fd)
MERGE (person_ceec49387371)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e634084a87fd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_11f71603068f)
MERGE (person_15c256572eeb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_11f71603068f)
MERGE (person_ceec49387371)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_11f71603068f)

