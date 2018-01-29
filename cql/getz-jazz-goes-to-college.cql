// events

MERGE (event_9f3753384ec0:Event{ uuid: '57318943-a385-4a5e-82da-9f3753384ec0' })
SET event_9f3753384ec0.name = 'Jazz Goes To College'
SET event_9f3753384ec0.date = '1966-11-14'
SET event_9f3753384ec0.type = 'Concert'
SET event_9f3753384ec0.musicbrainz = 'http://musicbrainz.org/release/57318943-a385-4a5e-82da-9f3753384ec0'
SET event_9f3753384ec0.source = 'musicbrainz.org'
SET event_9f3753384ec0.timestamp = timestamp()

MERGE (person_b1f20fcef5dc:Person{ uuid: '7b5b8b1b-414b-44e8-862f-b1f20fcef5dc' })
SET person_b1f20fcef5dc.name = 'Gary Burton'
SET person_b1f20fcef5dc.gender = 'Male'
SET person_b1f20fcef5dc.country = 'US'
SET person_b1f20fcef5dc.viaf = 'http://viaf.org/viaf/85329553'
SET person_b1f20fcef5dc.allmusic = 'http://www.allmusic.com/artist/mn0000738182'
SET person_b1f20fcef5dc.bbc = 'http://www.bbc.co.uk/music/artists/7b5b8b1b-414b-44e8-862f-b1f20fcef5dc'
SET person_b1f20fcef5dc.imdb = 'http://www.imdb.com/name/nm0123585/'
SET person_b1f20fcef5dc.wikipedia = 'https://en.wikipedia.org/wiki/Gary_Burton'
SET person_b1f20fcef5dc.discogs = 'https://www.discogs.com/artist/256558'
SET person_b1f20fcef5dc.wikidata = 'https://www.wikidata.org/wiki/Q353096'
SET person_b1f20fcef5dc.musicbrainz = 'https://musicbrainz.org/artist/7b5b8b1b-414b-44e8-862f-b1f20fcef5dc'
SET person_b1f20fcef5dc.isni_list = ['http://isni.org/isni/000000011074903X']
SET person_b1f20fcef5dc.source = 'musicbrainz.org'
SET person_b1f20fcef5dc.timestamp = timestamp()

MERGE (person_c9306385ffb0:Person{ uuid: 'd94cd4f9-3178-4cc5-9e96-c9306385ffb0' })
SET person_c9306385ffb0.name = 'Steve Swallow'
SET person_c9306385ffb0.gender = 'Male'
SET person_c9306385ffb0.country = 'US'
SET person_c9306385ffb0.viaf = 'http://viaf.org/viaf/42026809'
SET person_c9306385ffb0.allmusic = 'http://www.allmusic.com/artist/mn0000042344'
SET person_c9306385ffb0.bbc = 'http://www.bbc.co.uk/music/artists/d94cd4f9-3178-4cc5-9e96-c9306385ffb0'
SET person_c9306385ffb0.wikipedia = 'https://en.wikipedia.org/wiki/Steve_Swallow'
SET person_c9306385ffb0.discogs = 'https://www.discogs.com/artist/284204'
SET person_c9306385ffb0.wikidata = 'https://www.wikidata.org/wiki/Q708266'
SET person_c9306385ffb0.musicbrainz = 'https://musicbrainz.org/artist/d94cd4f9-3178-4cc5-9e96-c9306385ffb0'
SET person_c9306385ffb0.source = 'musicbrainz.org'
SET person_c9306385ffb0.timestamp = timestamp()

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

MERGE (person_afe9622fab32:Person{ uuid: '8f2422ab-0ec6-4c92-80c4-afe9622fab32' })
SET person_afe9622fab32.name = 'Stan Getz'
SET person_afe9622fab32.gender = 'Male'
SET person_afe9622fab32.country = 'US'
SET person_afe9622fab32.viaf = 'http://viaf.org/viaf/113597520'
SET person_afe9622fab32.allmusic = 'http://www.allmusic.com/artist/mn0000742899'
SET person_afe9622fab32.imdb = 'http://www.imdb.com/name/nm0315295/'
SET person_afe9622fab32.wikipedia = 'https://en.wikipedia.org/wiki/Stan_Getz'
SET person_afe9622fab32.discogs = 'https://www.discogs.com/artist/30486'
SET person_afe9622fab32.wikidata = 'https://www.wikidata.org/wiki/Q30587'
SET person_afe9622fab32.discographies = ['http://weave.me/app/weave.html?Stan_Getz']
SET person_afe9622fab32.databases = ['http://d-nb.info/gnd/119189941', 'http://rateyourmusic.com/artist/stan_getz', 'https://openlibrary.org/works/OL6199421A', 'https://www.musik-sammler.de/artist/stan-getz/', 'https://www.worldcat.org/identities/lccn-n81-018141']
SET person_afe9622fab32.musicbrainz = 'https://musicbrainz.org/artist/8f2422ab-0ec6-4c92-80c4-afe9622fab32'
SET person_afe9622fab32.isni_list = ['http://isni.org/isni/0000000110330511']
SET person_afe9622fab32.source = 'musicbrainz.org'
SET person_afe9622fab32.timestamp = timestamp()

// works

MERGE (person_edced1f8cde0:Person{ uuid: '7a8dbe84-f4c0-4457-bfa3-edced1f8cde0' })
SET person_edced1f8cde0.name = 'Antônio Carlos Jobim'
SET person_edced1f8cde0.gender = 'Male'
SET person_edced1f8cde0.disambiguation = 'Tom Jobim'
SET person_edced1f8cde0.country = 'BR'
SET person_edced1f8cde0.viaf = 'http://viaf.org/viaf/51875584'
SET person_edced1f8cde0.allmusic = 'http://www.allmusic.com/artist/mn0000781837'
SET person_edced1f8cde0.bbc = 'http://www.bbc.co.uk/music/artists/7a8dbe84-f4c0-4457-bfa3-edced1f8cde0'
SET person_edced1f8cde0.imdb = 'http://www.imdb.com/name/nm0423388/'
SET person_edced1f8cde0.wikipedia = 'https://en.wikipedia.org/wiki/Ant%C3%B4nio_Carlos_Jobim'
SET person_edced1f8cde0.discogs = 'https://www.discogs.com/artist/27991'
SET person_edced1f8cde0.wikidata = 'https://www.wikidata.org/wiki/Q200131'
SET person_edced1f8cde0.discographies = ['http://www.bjbear71.com/Jobim/tom.html']
SET person_edced1f8cde0.databases = ['http://rateyourmusic.com/artist/antonio_carlos_jobim', 'https://www.musik-sammler.de/artist/antonio-carlos-jobim/']
SET person_edced1f8cde0.musicbrainz = 'https://musicbrainz.org/artist/7a8dbe84-f4c0-4457-bfa3-edced1f8cde0'
SET person_edced1f8cde0.isni_list = ['http://isni.org/isni/0000000122798998']
SET person_edced1f8cde0.source = 'musicbrainz.org'
SET person_edced1f8cde0.timestamp = timestamp()

MERGE (person_df200f669450:Person{ uuid: 'f6b335b1-8623-4979-987e-df200f669450' })
SET person_df200f669450.name = 'Manning Sherwin'
SET person_df200f669450.gender = 'Male'
SET person_df200f669450.country = 'US'
SET person_df200f669450.wikipedia = 'https://en.wikipedia.org/wiki/Manning_Sherwin'
SET person_df200f669450.wikidata = 'https://www.wikidata.org/wiki/Q15500700'
SET person_df200f669450.musicbrainz = 'https://musicbrainz.org/artist/f6b335b1-8623-4979-987e-df200f669450'
SET person_df200f669450.source = 'musicbrainz.org'
SET person_df200f669450.timestamp = timestamp()

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

MERGE (person_d49d0d34971d:Person{ uuid: 'b3a87cc9-5fd1-4450-8cea-d49d0d34971d' })
SET person_d49d0d34971d.name = 'Philippe-Gérard'
SET person_d49d0d34971d.gender = 'Male'
SET person_d49d0d34971d.disambiguation = 'French composer'
SET person_d49d0d34971d.country = 'FR'
SET person_d49d0d34971d.allmusic = 'http://www.allmusic.com/artist/mn0001671807'
SET person_d49d0d34971d.imdb = 'http://www.imdb.com/name/nm0680024/'
SET person_d49d0d34971d.wikipedia = 'https://fr.wikipedia.org/wiki/Philippe-G%C3%A9rard_(compositeur)'
SET person_d49d0d34971d.discogs = 'https://www.discogs.com/artist/648056'
SET person_d49d0d34971d.wikidata = 'https://www.wikidata.org/wiki/Q1930858'
SET person_d49d0d34971d.musicbrainz = 'https://musicbrainz.org/artist/b3a87cc9-5fd1-4450-8cea-d49d0d34971d'
SET person_d49d0d34971d.source = 'musicbrainz.org'
SET person_d49d0d34971d.timestamp = timestamp()

MERGE (person_1fb9cd74ab66:Person{ uuid: '9d1b5faa-96b9-4061-b1e9-1fb9cd74ab66' })
SET person_1fb9cd74ab66.name = 'Bob Brookmeyer'
SET person_1fb9cd74ab66.gender = 'Male'
SET person_1fb9cd74ab66.country = 'US'
SET person_1fb9cd74ab66.viaf = 'http://viaf.org/viaf/56795511'
SET person_1fb9cd74ab66.allmusic = 'http://www.allmusic.com/artist/mn0000051233'
SET person_1fb9cd74ab66.bbc = 'http://www.bbc.co.uk/music/artists/9d1b5faa-96b9-4061-b1e9-1fb9cd74ab66'
SET person_1fb9cd74ab66.wikipedia = 'https://en.wikipedia.org/wiki/Bob_Brookmeyer'
SET person_1fb9cd74ab66.discogs = 'https://www.discogs.com/artist/265425'
SET person_1fb9cd74ab66.wikidata = 'https://www.wikidata.org/wiki/Q494982'
SET person_1fb9cd74ab66.musicbrainz = 'https://musicbrainz.org/artist/9d1b5faa-96b9-4061-b1e9-1fb9cd74ab66'
SET person_1fb9cd74ab66.source = 'musicbrainz.org'
SET person_1fb9cd74ab66.timestamp = timestamp()

MERGE (person_7dae0b1312fc:Person{ uuid: '1c01cf84-07c7-408a-b5a8-7dae0b1312fc' })
SET person_7dae0b1312fc.name = 'Vinicius de Moraes'
SET person_7dae0b1312fc.gender = 'Male'
SET person_7dae0b1312fc.country = 'BR'
SET person_7dae0b1312fc.viaf = 'http://viaf.org/viaf/7574761'
SET person_7dae0b1312fc.allmusic = 'http://www.allmusic.com/artist/mn0000219243'
SET person_7dae0b1312fc.imdb = 'http://www.imdb.com/name/nm0210460/'
SET person_7dae0b1312fc.wikipedia = 'https://en.wikipedia.org/wiki/Vinicius_de_Moraes'
SET person_7dae0b1312fc.wikipedia = 'https://pt.wikipedia.org/wiki/Vinicius_de_Moraes'
SET person_7dae0b1312fc.discogs = 'https://www.discogs.com/artist/315789'
SET person_7dae0b1312fc.wikidata = 'https://www.wikidata.org/wiki/Q333856'
SET person_7dae0b1312fc.databases = ['http://rateyourmusic.com/artist/vinicius_de_moraes']
SET person_7dae0b1312fc.musicbrainz = 'https://musicbrainz.org/artist/1c01cf84-07c7-408a-b5a8-7dae0b1312fc'
SET person_7dae0b1312fc.isni_list = ['http://isni.org/isni/0000000121195941']
SET person_7dae0b1312fc.source = 'musicbrainz.org'
SET person_7dae0b1312fc.timestamp = timestamp()

MERGE (work_264eba69e9b5:Work{ uuid: '1b963c92-c5a6-39cf-a411-264eba69e9b5' })
SET work_264eba69e9b5.name = 'A Nightingale Sang in Berkeley Square'
SET work_264eba69e9b5.iswc = 'T-070.152.584-9'
SET work_264eba69e9b5.type = 'Song'
SET work_264eba69e9b5.wikidata = 'https://www.wikidata.org/wiki/Q4658646'
SET work_264eba69e9b5.musicbrainz = 'https://musicbrainz.org/work/1b963c92-c5a6-39cf-a411-264eba69e9b5'
SET work_264eba69e9b5.source = 'musicbrainz.org'
SET work_264eba69e9b5.timestamp = timestamp()

MERGE (work_2f30f5bc7873:Work{ uuid: '70686324-ef44-456f-adfb-2f30f5bc7873' })
SET work_2f30f5bc7873.name = 'A Singing Song'
SET work_2f30f5bc7873.type = 'Song'
SET work_2f30f5bc7873.source = 'musicbrainz.org'
SET work_2f30f5bc7873.timestamp = timestamp()

MERGE (work_544fa4101167:Work{ uuid: '53372c2f-30d9-4084-ba3f-544fa4101167' })
SET work_544fa4101167.name = 'O morro não tem vez'
SET work_544fa4101167.iswc = 'T-041.645.288-4'
SET work_544fa4101167.type = 'Song'
SET work_544fa4101167.source = 'musicbrainz.org'
SET work_544fa4101167.timestamp = timestamp()

MERGE (work_94997c14683d:Work{ uuid: 'bc0ebeea-f7e3-4707-853a-94997c14683d' })
SET work_94997c14683d.name = 'When the World Was Young'
SET work_94997c14683d.type = 'Song'
SET work_94997c14683d.wikidata = 'https://www.wikidata.org/wiki/Q2137978'
SET work_94997c14683d.musicbrainz = 'https://musicbrainz.org/work/bc0ebeea-f7e3-4707-853a-94997c14683d'
SET work_94997c14683d.source = 'musicbrainz.org'
SET work_94997c14683d.timestamp = timestamp()

MERGE (work_e359abfdf494:Work{ uuid: '9646b833-1bc0-4cb7-9910-e359abfdf494' })
SET work_e359abfdf494.name = 'Six, Nix, Quix, Flix'
SET work_e359abfdf494.source = 'musicbrainz.org'
SET work_e359abfdf494.timestamp = timestamp()

MERGE (work_a364c904a125:Work{ uuid: '858ebb4b-edd7-39ee-9120-a364c904a125' })
SET work_a364c904a125.name = 'Scrapple From the Apple'
SET work_a364c904a125.source = 'musicbrainz.org'
SET work_a364c904a125.timestamp = timestamp()

MERGE (work_5a72968d8f02:Work{ uuid: '641baadf-5b63-415d-9636-5a72968d8f02' })
SET work_5a72968d8f02.name = 'The Sunset Dell'
SET work_5a72968d8f02.type = 'Song'
SET work_5a72968d8f02.source = 'musicbrainz.org'
SET work_5a72968d8f02.timestamp = timestamp()

MERGE (work_d8491fc97651:Work{ uuid: '807b8169-cb39-30c7-a9e2-d8491fc97651' })
SET work_d8491fc97651.name = 'Desafinado'
SET work_d8491fc97651.iswc = 'T-071.080.063-7'
SET work_d8491fc97651.type = 'Song'
SET work_d8491fc97651.wikidata = 'https://www.wikidata.org/wiki/Q277804'
SET work_d8491fc97651.musicbrainz = 'https://musicbrainz.org/work/807b8169-cb39-30c7-a9e2-d8491fc97651'
SET work_d8491fc97651.source = 'musicbrainz.org'
SET work_d8491fc97651.timestamp = timestamp()

MERGE (work_0bbf509de643:Work{ uuid: '3561046c-bf32-488d-9386-0bbf509de643' })
SET work_0bbf509de643.name = 'Jive Hoot'
SET work_0bbf509de643.iswc = 'T-700.032.569-1'
SET work_0bbf509de643.type = 'Song'
SET work_0bbf509de643.source = 'musicbrainz.org'
SET work_0bbf509de643.timestamp = timestamp()


// performances
MERGE (perf_9f3753384ec0_264eba69e9b5:Performance { uuid: '9f3753384ec0-1b963c92-c5a6-39cf-a411-264eba69e9b5' })
SET perf_9f3753384ec0_264eba69e9b5.name = 'A Nightingale Sang in Berkeley Square'
SET perf_9f3753384ec0_264eba69e9b5.begin = '1966-11-14'
SET perf_9f3753384ec0_264eba69e9b5.end = '1966-11-14'
SET perf_9f3753384ec0_264eba69e9b5.source = 'musicbrainz.org'
SET perf_9f3753384ec0_264eba69e9b5.timestamp = timestamp()
MERGE (perf_9f3753384ec0_264eba69e9b5)-[:PERFORMANCE_OF]->(work_264eba69e9b5)

MERGE (perf_9f3753384ec0_2f30f5bc7873:Performance { uuid: '9f3753384ec0-70686324-ef44-456f-adfb-2f30f5bc7873' })
SET perf_9f3753384ec0_2f30f5bc7873.name = 'A Singing Song'
SET perf_9f3753384ec0_2f30f5bc7873.begin = '1966-11-14'
SET perf_9f3753384ec0_2f30f5bc7873.end = '1966-11-14'
SET perf_9f3753384ec0_2f30f5bc7873.source = 'musicbrainz.org'
SET perf_9f3753384ec0_2f30f5bc7873.timestamp = timestamp()
MERGE (perf_9f3753384ec0_2f30f5bc7873)-[:PERFORMANCE_OF]->(work_2f30f5bc7873)

MERGE (perf_9f3753384ec0_544fa4101167:Performance { uuid: '9f3753384ec0-53372c2f-30d9-4084-ba3f-544fa4101167' })
SET perf_9f3753384ec0_544fa4101167.name = 'O morro não tem vez'
SET perf_9f3753384ec0_544fa4101167.begin = '1966-11-14'
SET perf_9f3753384ec0_544fa4101167.end = '1966-11-14'
SET perf_9f3753384ec0_544fa4101167.source = 'musicbrainz.org'
SET perf_9f3753384ec0_544fa4101167.timestamp = timestamp()
MERGE (perf_9f3753384ec0_544fa4101167)-[:PERFORMANCE_OF]->(work_544fa4101167)

MERGE (perf_9f3753384ec0_94997c14683d:Performance { uuid: '9f3753384ec0-bc0ebeea-f7e3-4707-853a-94997c14683d' })
SET perf_9f3753384ec0_94997c14683d.name = 'When the World Was Young'
SET perf_9f3753384ec0_94997c14683d.begin = '1966-11-14'
SET perf_9f3753384ec0_94997c14683d.end = '1966-11-14'
SET perf_9f3753384ec0_94997c14683d.source = 'musicbrainz.org'
SET perf_9f3753384ec0_94997c14683d.timestamp = timestamp()
MERGE (perf_9f3753384ec0_94997c14683d)-[:PERFORMANCE_OF]->(work_94997c14683d)

MERGE (perf_9f3753384ec0_e359abfdf494:Performance { uuid: '9f3753384ec0-9646b833-1bc0-4cb7-9910-e359abfdf494' })
SET perf_9f3753384ec0_e359abfdf494.name = 'Six, Nix, Quix, Flix'
SET perf_9f3753384ec0_e359abfdf494.begin = '1966-11-14'
SET perf_9f3753384ec0_e359abfdf494.end = '1966-11-14'
SET perf_9f3753384ec0_e359abfdf494.source = 'musicbrainz.org'
SET perf_9f3753384ec0_e359abfdf494.timestamp = timestamp()
MERGE (perf_9f3753384ec0_e359abfdf494)-[:PERFORMANCE_OF]->(work_e359abfdf494)

MERGE (perf_9f3753384ec0_a364c904a125:Performance { uuid: '9f3753384ec0-858ebb4b-edd7-39ee-9120-a364c904a125' })
SET perf_9f3753384ec0_a364c904a125.name = 'Scrapple From the Apple'
SET perf_9f3753384ec0_a364c904a125.begin = '1966-11-14'
SET perf_9f3753384ec0_a364c904a125.end = '1966-11-14'
SET perf_9f3753384ec0_a364c904a125.source = 'musicbrainz.org'
SET perf_9f3753384ec0_a364c904a125.timestamp = timestamp()
MERGE (perf_9f3753384ec0_a364c904a125)-[:PERFORMANCE_OF]->(work_a364c904a125)

MERGE (perf_9f3753384ec0_5a72968d8f02:Performance { uuid: '9f3753384ec0-641baadf-5b63-415d-9636-5a72968d8f02' })
SET perf_9f3753384ec0_5a72968d8f02.name = 'The Sunset Dell'
SET perf_9f3753384ec0_5a72968d8f02.begin = '1966-11-14'
SET perf_9f3753384ec0_5a72968d8f02.end = '1966-11-14'
SET perf_9f3753384ec0_5a72968d8f02.source = 'musicbrainz.org'
SET perf_9f3753384ec0_5a72968d8f02.timestamp = timestamp()
MERGE (perf_9f3753384ec0_5a72968d8f02)-[:PERFORMANCE_OF]->(work_5a72968d8f02)

MERGE (perf_9f3753384ec0_d8491fc97651:Performance { uuid: '9f3753384ec0-807b8169-cb39-30c7-a9e2-d8491fc97651' })
SET perf_9f3753384ec0_d8491fc97651.name = 'Desafinado'
SET perf_9f3753384ec0_d8491fc97651.begin = '1966-11-14'
SET perf_9f3753384ec0_d8491fc97651.end = '1966-11-14'
SET perf_9f3753384ec0_d8491fc97651.source = 'musicbrainz.org'
SET perf_9f3753384ec0_d8491fc97651.timestamp = timestamp()
MERGE (perf_9f3753384ec0_d8491fc97651)-[:PERFORMANCE_OF]->(work_d8491fc97651)

MERGE (perf_9f3753384ec0_0bbf509de643:Performance { uuid: '9f3753384ec0-3561046c-bf32-488d-9386-0bbf509de643' })
SET perf_9f3753384ec0_0bbf509de643.name = 'Jive Hoot'
SET perf_9f3753384ec0_0bbf509de643.begin = '1966-11-14'
SET perf_9f3753384ec0_0bbf509de643.end = '1966-11-14'
SET perf_9f3753384ec0_0bbf509de643.source = 'musicbrainz.org'
SET perf_9f3753384ec0_0bbf509de643.timestamp = timestamp()
MERGE (perf_9f3753384ec0_0bbf509de643)-[:PERFORMANCE_OF]->(work_0bbf509de643)



// composers
MERGE (person_df200f669450)-[:COMPOSED]->(work_264eba69e9b5)
MERGE (person_b1f20fcef5dc)-[:COMPOSED]->(work_2f30f5bc7873)
MERGE (person_7dae0b1312fc)-[:COMPOSED]->(work_544fa4101167)
MERGE (person_edced1f8cde0)-[:COMPOSED]->(work_544fa4101167)
MERGE (person_d49d0d34971d)-[:COMPOSED]->(work_94997c14683d)
MERGE (person_b1f20fcef5dc)-[:COMPOSED]->(work_e359abfdf494)
MERGE (person_c73775716312)-[:COMPOSED]->(work_a364c904a125)
MERGE (person_b1f20fcef5dc)-[:COMPOSED]->(work_5a72968d8f02)
MERGE (person_edced1f8cde0)-[:COMPOSED]->(work_d8491fc97651)
MERGE (person_1fb9cd74ab66)-[:COMPOSED]->(work_0bbf509de643)


// place nodes

MERGE (place_ca0bc246d14b:Place{ uuid: '557d5a17-aa63-4391-b287-ca0bc246d14b' })
SET place_ca0bc246d14b.name = 'London School of Economics'
SET place_ca0bc246d14b.source = 'musicbrainz.org'


// place relationships
MERGE (event_9f3753384ec0)-[:HAS_PLACE { type: 'held at' }]->(place_ca0bc246d14b)
MERGE (perf_9f3753384ec0_264eba69e9b5)-[:HAS_PLACE { type: 'performed at', begin: '1966-11-14', end: '1966-11-14' }]->(place_ca0bc246d14b)
MERGE (perf_9f3753384ec0_2f30f5bc7873)-[:HAS_PLACE { type: 'performed at', begin: '1966-11-14', end: '1966-11-14' }]->(place_ca0bc246d14b)
MERGE (perf_9f3753384ec0_544fa4101167)-[:HAS_PLACE { type: 'performed at', begin: '1966-11-14', end: '1966-11-14' }]->(place_ca0bc246d14b)
MERGE (perf_9f3753384ec0_94997c14683d)-[:HAS_PLACE { type: 'performed at', begin: '1966-11-14', end: '1966-11-14' }]->(place_ca0bc246d14b)
MERGE (perf_9f3753384ec0_e359abfdf494)-[:HAS_PLACE { type: 'performed at', begin: '1966-11-14', end: '1966-11-14' }]->(place_ca0bc246d14b)
MERGE (perf_9f3753384ec0_a364c904a125)-[:HAS_PLACE { type: 'performed at', begin: '1966-11-14', end: '1966-11-14' }]->(place_ca0bc246d14b)
MERGE (perf_9f3753384ec0_5a72968d8f02)-[:HAS_PLACE { type: 'performed at', begin: '1966-11-14', end: '1966-11-14' }]->(place_ca0bc246d14b)
MERGE (perf_9f3753384ec0_d8491fc97651)-[:HAS_PLACE { type: 'performed at', begin: '1966-11-14', end: '1966-11-14' }]->(place_ca0bc246d14b)
MERGE (perf_9f3753384ec0_0bbf509de643)-[:HAS_PLACE { type: 'performed at', begin: '1966-11-14', end: '1966-11-14' }]->(place_ca0bc246d14b)


// event->performance relationships
MERGE (event_9f3753384ec0)-[:HAS_PERFORMANCE { begin: '1966-11-14', end: '1966-11-14' }]->(perf_9f3753384ec0_264eba69e9b5)
MERGE (event_9f3753384ec0)-[:HAS_PERFORMANCE { begin: '1966-11-14', end: '1966-11-14' }]->(perf_9f3753384ec0_2f30f5bc7873)
MERGE (event_9f3753384ec0)-[:HAS_PERFORMANCE { begin: '1966-11-14', end: '1966-11-14' }]->(perf_9f3753384ec0_544fa4101167)
MERGE (event_9f3753384ec0)-[:HAS_PERFORMANCE { begin: '1966-11-14', end: '1966-11-14' }]->(perf_9f3753384ec0_94997c14683d)
MERGE (event_9f3753384ec0)-[:HAS_PERFORMANCE { begin: '1966-11-14', end: '1966-11-14' }]->(perf_9f3753384ec0_e359abfdf494)
MERGE (event_9f3753384ec0)-[:HAS_PERFORMANCE { begin: '1966-11-14', end: '1966-11-14' }]->(perf_9f3753384ec0_a364c904a125)
MERGE (event_9f3753384ec0)-[:HAS_PERFORMANCE { begin: '1966-11-14', end: '1966-11-14' }]->(perf_9f3753384ec0_5a72968d8f02)
MERGE (event_9f3753384ec0)-[:HAS_PERFORMANCE { begin: '1966-11-14', end: '1966-11-14' }]->(perf_9f3753384ec0_d8491fc97651)
MERGE (event_9f3753384ec0)-[:HAS_PERFORMANCE { begin: '1966-11-14', end: '1966-11-14' }]->(perf_9f3753384ec0_0bbf509de643)


// event-performance participation
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_9f3753384ec0_264eba69e9b5)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_9f3753384ec0_2f30f5bc7873)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_9f3753384ec0_544fa4101167)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_9f3753384ec0_94997c14683d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_9f3753384ec0_e359abfdf494)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_9f3753384ec0_a364c904a125)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_9f3753384ec0_5a72968d8f02)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_9f3753384ec0_d8491fc97651)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_9f3753384ec0_0bbf509de643)
MERGE (person_b1f20fcef5dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_9f3753384ec0_264eba69e9b5)
MERGE (person_b1f20fcef5dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_9f3753384ec0_2f30f5bc7873)
MERGE (person_b1f20fcef5dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_9f3753384ec0_544fa4101167)
MERGE (person_b1f20fcef5dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_9f3753384ec0_94997c14683d)
MERGE (person_b1f20fcef5dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_9f3753384ec0_e359abfdf494)
MERGE (person_b1f20fcef5dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_9f3753384ec0_a364c904a125)
MERGE (person_b1f20fcef5dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_9f3753384ec0_5a72968d8f02)
MERGE (person_b1f20fcef5dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_9f3753384ec0_d8491fc97651)
MERGE (person_b1f20fcef5dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_9f3753384ec0_0bbf509de643)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9f3753384ec0_264eba69e9b5)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9f3753384ec0_2f30f5bc7873)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9f3753384ec0_544fa4101167)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9f3753384ec0_94997c14683d)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9f3753384ec0_e359abfdf494)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9f3753384ec0_a364c904a125)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9f3753384ec0_5a72968d8f02)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9f3753384ec0_d8491fc97651)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9f3753384ec0_0bbf509de643)
MERGE (person_c9306385ffb0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9f3753384ec0_264eba69e9b5)
MERGE (person_c9306385ffb0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9f3753384ec0_2f30f5bc7873)
MERGE (person_c9306385ffb0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9f3753384ec0_544fa4101167)
MERGE (person_c9306385ffb0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9f3753384ec0_94997c14683d)
MERGE (person_c9306385ffb0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9f3753384ec0_e359abfdf494)
MERGE (person_c9306385ffb0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9f3753384ec0_a364c904a125)
MERGE (person_c9306385ffb0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9f3753384ec0_5a72968d8f02)
MERGE (person_c9306385ffb0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9f3753384ec0_d8491fc97651)
MERGE (person_c9306385ffb0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9f3753384ec0_0bbf509de643)
