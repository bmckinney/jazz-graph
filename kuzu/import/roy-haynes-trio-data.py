
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""


MERGE (release_f6a9d6c86eea:Release{ uuid: 'e8bb8ea9-b4af-4cc7-b209-f6a9d6c86eea' })
SET release_f6a9d6c86eea.name = 'The Roy Haynes Trio'
SET release_f6a9d6c86eea.country = 'US'
SET release_f6a9d6c86eea.date = '2000'
SET release_f6a9d6c86eea.format = 'CD'
SET release_f6a9d6c86eea.discode = '314 543 534-2'
SET release_f6a9d6c86eea.musicbrainz = 'http://musicbrainz.org/release/e8bb8ea9-b4af-4cc7-b209-f6a9d6c86eea'
SET release_f6a9d6c86eea.source = 'musicbrainz.org'


MERGE (person_ebf20ee45f41:Person{ uuid: '8d0e541a-78a2-445f-a2e6-ebf20ee45f41' }) 
SET person_ebf20ee45f41.name = 'Danilo Pérez'
SET person_ebf20ee45f41.gender = 'Male'
SET person_ebf20ee45f41.country = 'PA'
SET person_ebf20ee45f41.wikipedia = 'http://en.wikipedia.org/wiki/Danilo_P%C3%A9rez'
SET person_ebf20ee45f41.viaf = 'http://viaf.org/viaf/74041553'
SET person_ebf20ee45f41.allmusic = 'http://www.allmusic.com/artist/mn0000670875'
SET person_ebf20ee45f41.discogs = 'http://www.discogs.com/artist/59752'
SET person_ebf20ee45f41.wikidata = 'http://www.wikidata.org/wiki/Q1164102'
SET person_ebf20ee45f41.musicbrainz = 'https://musicbrainz.org/artist/8d0e541a-78a2-445f-a2e6-ebf20ee45f41'
SET person_ebf20ee45f41.source = 'musicbrainz.org'


MERGE (person_e5cc86e2f134:Person{ uuid: 'b7999b55-a0b0-4ea5-bcba-e5cc86e2f134' }) 
SET person_e5cc86e2f134.name = 'John Patitucci'
SET person_e5cc86e2f134.gender = 'Male'
SET person_e5cc86e2f134.country = 'US'
SET person_e5cc86e2f134.wikipedia = 'http://en.wikipedia.org/wiki/John_Patitucci'
SET person_e5cc86e2f134.viaf = 'http://viaf.org/viaf/42029940'
SET person_e5cc86e2f134.allmusic = 'http://www.allmusic.com/artist/mn0000188776'
SET person_e5cc86e2f134.discogs = 'http://www.discogs.com/artist/253208'
SET person_e5cc86e2f134.wikidata = 'http://www.wikidata.org/wiki/Q504646'
SET person_e5cc86e2f134.musicbrainz = 'https://musicbrainz.org/artist/b7999b55-a0b0-4ea5-bcba-e5cc86e2f134'
SET person_e5cc86e2f134.source = 'musicbrainz.org'


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

// labels

MERGE (label_00fbcc4fce83:Label{ uuid: '99a24d71-54c1-4d3f-88cc-00fbcc4fce83' })
SET label_00fbcc4fce83.name= 'Verve'

// performances

MERGE (perf_a82d57813460:Performance{ uuid: '56b98ecf-ae54-441a-a4d5-a82d57813460' })
SET perf_a82d57813460.name = 'Wail'
SET perf_a82d57813460.duration = '3:19'
SET perf_a82d57813460.begin_date = '1999-11-23'
SET perf_a82d57813460.end_date = '1999-11-24'
SET perf_a82d57813460.source = 'musicbrainz.org'


MERGE (perf_e0f3424edd37:Performance{ uuid: '9be25d28-90b8-47b5-b6fd-e0f3424edd37' })
SET perf_e0f3424edd37.name = 'Question and Answer'
SET perf_e0f3424edd37.duration = '7:08'
SET perf_e0f3424edd37.begin_date = '1999-11-23'
SET perf_e0f3424edd37.end_date = '1999-11-24'
SET perf_e0f3424edd37.source = 'musicbrainz.org'


MERGE (perf_e18d2d97b850:Performance{ uuid: '0a1f85e9-7422-4aa8-a750-e18d2d97b850' })
SET perf_e18d2d97b850.name = 'Shulie a Bop'
SET perf_e18d2d97b850.duration = '3:34'
SET perf_e18d2d97b850.begin_date = '1999-11-23'
SET perf_e18d2d97b850.end_date = '1999-11-24'
SET perf_e18d2d97b850.source = 'musicbrainz.org'


MERGE (perf_e91a31e0d410:Performance{ uuid: 'c9976758-5810-4c0a-8f17-e91a31e0d410' })
SET perf_e91a31e0d410.name = 'Dear Old Stockholm'
SET perf_e91a31e0d410.duration = '6:05'
SET perf_e91a31e0d410.begin_date = '1999-11-23'
SET perf_e91a31e0d410.end_date = '1999-11-24'
SET perf_e91a31e0d410.source = 'musicbrainz.org'


MERGE (perf_b6c3b5a11e18:Performance{ uuid: '477f343d-f705-4bf1-90fd-b6c3b5a11e18' })
SET perf_b6c3b5a11e18.name = 'It\\'s Easy to Remember'
SET perf_b6c3b5a11e18.duration = '6:40'
SET perf_b6c3b5a11e18.begin_date = '1999-11-23'
SET perf_b6c3b5a11e18.end_date = '1999-11-24'
SET perf_b6c3b5a11e18.source = 'musicbrainz.org'


MERGE (perf_63d287403253:Performance{ uuid: '2368029a-74ed-4c61-a83b-63d287403253' })
SET perf_63d287403253.name = 'Folk Song'
SET perf_63d287403253.duration = '5:33'
SET perf_63d287403253.begin_date = '1999-11-23'
SET perf_63d287403253.end_date = '1999-11-24'
SET perf_63d287403253.source = 'musicbrainz.org'


MERGE (perf_3178b59c7b0b:Performance{ uuid: 'dc41241e-c706-427f-8044-3178b59c7b0b' })
SET perf_3178b59c7b0b.name = 'Sippin\\' at Bells'
SET perf_3178b59c7b0b.duration = '7:07'
SET perf_3178b59c7b0b.begin_date = '1999-09-10'
SET perf_3178b59c7b0b.end_date = '1999-09-11'
SET perf_3178b59c7b0b.source = 'musicbrainz.org'


MERGE (perf_95eca70a29aa:Performance{ uuid: 'cf23ca3e-38bc-4bd6-b520-95eca70a29aa' })
SET perf_95eca70a29aa.name = 'Bright Mississippi'
SET perf_95eca70a29aa.duration = '9:39'
SET perf_95eca70a29aa.begin_date = '1999-09-10'
SET perf_95eca70a29aa.end_date = '1999-09-11'
SET perf_95eca70a29aa.source = 'musicbrainz.org'


MERGE (perf_b370c5065f4e:Performance{ uuid: '2f569d91-7537-4a9c-b5c2-b370c5065f4e' })
SET perf_b370c5065f4e.name = 'Prelude to a Kiss'
SET perf_b370c5065f4e.duration = '7:58'
SET perf_b370c5065f4e.begin_date = '1999-09-10'
SET perf_b370c5065f4e.end_date = '1999-09-11'
SET perf_b370c5065f4e.source = 'musicbrainz.org'


MERGE (perf_93f82b3bc3ba:Performance{ uuid: '45014368-3d3a-4f10-81eb-93f82b3bc3ba' })
SET perf_93f82b3bc3ba.name = 'Green Chimneys'
SET perf_93f82b3bc3ba.duration = '12:28'
SET perf_93f82b3bc3ba.begin_date = '1999-09-10'
SET perf_93f82b3bc3ba.end_date = '1999-09-11'
SET perf_93f82b3bc3ba.source = 'musicbrainz.org'




// labels
MERGE (release_f6a9d6c86eea)-[:HAS_LABEL]->(label_00fbcc4fce83)


// tracks
MERGE (release_f6a9d6c86eea)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_a82d57813460)
MERGE (release_f6a9d6c86eea)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_e0f3424edd37)
MERGE (release_f6a9d6c86eea)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_e18d2d97b850)
MERGE (release_f6a9d6c86eea)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_e91a31e0d410)
MERGE (release_f6a9d6c86eea)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_b6c3b5a11e18)
MERGE (release_f6a9d6c86eea)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_63d287403253)
MERGE (release_f6a9d6c86eea)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_3178b59c7b0b)
MERGE (release_f6a9d6c86eea)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_95eca70a29aa)
MERGE (release_f6a9d6c86eea)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_b370c5065f4e)
MERGE (release_f6a9d6c86eea)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_93f82b3bc3ba)

// works

MERGE (person_340d64fbb41c:Person{ uuid: 'dbc5809c-7837-4b6f-961e-340d64fbb41c' }) 
SET person_340d64fbb41c.name = 'Bud Powell'
SET person_340d64fbb41c.gender = 'Male'
SET person_340d64fbb41c.country = 'US'
SET person_340d64fbb41c.wikipedia = 'http://en.wikipedia.org/wiki/Bud_Powell'
SET person_340d64fbb41c.viaf = 'http://viaf.org/viaf/197369'
SET person_340d64fbb41c.allmusic = 'http://www.allmusic.com/artist/mn0000640675'
SET person_340d64fbb41c.bbc = 'http://www.bbc.co.uk/music/artists/dbc5809c-7837-4b6f-961e-340d64fbb41c'
SET person_340d64fbb41c.discogs = 'http://www.discogs.com/artist/29992'
SET person_340d64fbb41c.wikidata = 'http://www.wikidata.org/wiki/Q312692'
SET person_340d64fbb41c.databases = ['http://rateyourmusic.com/artist/bud_powell']
SET person_340d64fbb41c.musicbrainz = 'https://musicbrainz.org/artist/dbc5809c-7837-4b6f-961e-340d64fbb41c'
SET person_340d64fbb41c.source = 'musicbrainz.org'


MERGE (person_acc0205f7513:Person{ uuid: '346448f5-25a0-4f78-bbd6-acc0205f7513' }) 
SET person_acc0205f7513.name = 'Richard Rodgers'
SET person_acc0205f7513.gender = 'Male'
SET person_acc0205f7513.country = 'US'
SET person_acc0205f7513.wikipedia = 'http://en.wikipedia.org/wiki/Richard_Rodgers'
SET person_acc0205f7513.viaf = 'http://viaf.org/viaf/113475079'
SET person_acc0205f7513.allmusic = 'http://www.allmusic.com/artist/mn0000820913'
SET person_acc0205f7513.bbc = 'http://www.bbc.co.uk/music/artists/346448f5-25a0-4f78-bbd6-acc0205f7513'
SET person_acc0205f7513.discogs = 'http://www.discogs.com/artist/255801'
SET person_acc0205f7513.discogs = 'http://www.discogs.com/artist/604171'
SET person_acc0205f7513.imdb = 'http://www.imdb.com/name/nm0006256/'
SET person_acc0205f7513.wikidata = 'http://www.wikidata.org/wiki/Q269094'
SET person_acc0205f7513.databases = ['http://ibdb.com/person.php?id=8323', 'https://rateyourmusic.com/artist/richard_rodgers']
SET person_acc0205f7513.musicbrainz = 'https://musicbrainz.org/artist/346448f5-25a0-4f78-bbd6-acc0205f7513'
SET person_acc0205f7513.isni_list = ['http://isni.org/isni/0000000121482043']
SET person_acc0205f7513.source = 'musicbrainz.org'


MERGE (person_f8091d98cf25:Person{ uuid: '7daac7f9-8fcc-485f-a14f-f8091d98cf25' }) 
SET person_f8091d98cf25.name = 'Pat Metheny'
SET person_f8091d98cf25.gender = 'Male'
SET person_f8091d98cf25.country = 'US'
SET person_f8091d98cf25.wikipedia = 'http://en.wikipedia.org/wiki/Pat_Metheny'
SET person_f8091d98cf25.viaf = 'http://viaf.org/viaf/22188874'
SET person_f8091d98cf25.allmusic = 'http://www.allmusic.com/artist/mn0000179698'
SET person_f8091d98cf25.bbc = 'http://www.bbc.co.uk/music/artists/7daac7f9-8fcc-485f-a14f-f8091d98cf25'
SET person_f8091d98cf25.discogs = 'http://www.discogs.com/artist/20185'
SET person_f8091d98cf25.imdb = 'http://www.imdb.com/name/nm0582533/'
SET person_f8091d98cf25.wikidata = 'http://www.wikidata.org/wiki/Q213887'
SET person_f8091d98cf25.musicbrainz = 'https://musicbrainz.org/artist/7daac7f9-8fcc-485f-a14f-f8091d98cf25'
SET person_f8091d98cf25.source = 'musicbrainz.org'


MERGE (person_c73775716312:Person{ uuid: 'c7356af9-9ea6-4a78-a55b-c73775716312' }) 
SET person_c73775716312.name = 'Charlie Parker'
SET person_c73775716312.gender = 'Male'
SET person_c73775716312.disambiguation = 'aka "Bird", jazz alto saxophonist'
SET person_c73775716312.country = 'US'
SET person_c73775716312.wikipedia = 'http://en.wikipedia.org/wiki/Charlie_Parker'
SET person_c73775716312.viaf = 'http://viaf.org/viaf/10034216'
SET person_c73775716312.allmusic = 'http://www.allmusic.com/artist/mn0000211758'
SET person_c73775716312.bbc = 'http://www.bbc.co.uk/music/artists/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.discogs = 'http://www.discogs.com/artist/75617'
SET person_c73775716312.imdb = 'http://www.imdb.com/name/nm0662127/'
SET person_c73775716312.wikidata = 'http://www.wikidata.org/wiki/Q103767'
SET person_c73775716312.discographies = ['http://www.jazzdisco.org/bird/', 'http://www.kyushu-ns.ac.jp/~allan/Documents/CP_M.html']
SET person_c73775716312.databases = ['http://rateyourmusic.com/artist/charlie_parker']
SET person_c73775716312.musicbrainz = 'https://musicbrainz.org/artist/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.isni_list = ['http://isni.org/isni/0000000120955806']
SET person_c73775716312.source = 'musicbrainz.org'


MERGE (person_5a269b32b4c2:Person{ uuid: '8446fcca-109e-4c6d-a2ff-5a269b32b4c2' }) 
SET person_5a269b32b4c2.name = 'Chick Corea'
SET person_5a269b32b4c2.gender = 'Male'
SET person_5a269b32b4c2.country = 'US'
SET person_5a269b32b4c2.wikipedia = 'http://en.wikipedia.org/wiki/Chick_Corea'
SET person_5a269b32b4c2.viaf = 'http://viaf.org/viaf/37337806'
SET person_5a269b32b4c2.allmusic = 'http://www.allmusic.com/artist/mn0000110541'
SET person_5a269b32b4c2.bbc = 'http://www.bbc.co.uk/music/artists/8446fcca-109e-4c6d-a2ff-5a269b32b4c2'
SET person_5a269b32b4c2.discogs = 'http://www.discogs.com/artist/37731'
SET person_5a269b32b4c2.wikidata = 'http://www.wikidata.org/wiki/Q192465'
SET person_5a269b32b4c2.discographies = ['http://www.chickcorea.com/discography.html']
SET person_5a269b32b4c2.databases = ['https://rateyourmusic.com/artist/chick_corea']
SET person_5a269b32b4c2.musicbrainz = 'https://musicbrainz.org/artist/8446fcca-109e-4c6d-a2ff-5a269b32b4c2'
SET person_5a269b32b4c2.source = 'musicbrainz.org'


MERGE (person_7eeeb45e411f:Person{ uuid: '3af06bc4-68ad-4cae-bb7a-7eeeb45e411f' }) 
SET person_7eeeb45e411f.name = 'Duke Ellington'
SET person_7eeeb45e411f.gender = 'Male'
SET person_7eeeb45e411f.country = 'US'
SET person_7eeeb45e411f.wikipedia = 'http://en.wikipedia.org/wiki/Duke_Ellington'
SET person_7eeeb45e411f.viaf = 'http://viaf.org/viaf/66651610'
SET person_7eeeb45e411f.allmusic = 'http://www.allmusic.com/artist/mn0000120323'
SET person_7eeeb45e411f.bbc = 'http://www.bbc.co.uk/music/artists/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.discogs = 'http://www.discogs.com/artist/145257'
SET person_7eeeb45e411f.wikidata = 'http://www.wikidata.org/wiki/Q4030'
SET person_7eeeb45e411f.discographies = ['http://www.redhotjazz.com/duke.html']
SET person_7eeeb45e411f.databases = ['http://rateyourmusic.com/artist/duke_ellington']
SET person_7eeeb45e411f.musicbrainz = 'https://musicbrainz.org/artist/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.isni_list = ['http://isni.org/isni/0000000109110810']
SET person_7eeeb45e411f.source = 'musicbrainz.org'


MERGE (person_5260b4274ed4:Person{ uuid: '8e8c7417-c905-46b1-b42a-5260b4274ed4' }) 
SET person_5260b4274ed4.name = 'Thelonious Monk'
SET person_5260b4274ed4.gender = 'Male'
SET person_5260b4274ed4.country = 'US'
SET person_5260b4274ed4.wikipedia = 'http://en.wikipedia.org/wiki/Thelonious_Monk'
SET person_5260b4274ed4.viaf = 'http://viaf.org/viaf/44485892'
SET person_5260b4274ed4.allmusic = 'http://www.allmusic.com/artist/mn0000490416'
SET person_5260b4274ed4.bbc = 'http://www.bbc.co.uk/music/artists/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.discogs = 'http://www.discogs.com/artist/145256'
SET person_5260b4274ed4.imdb = 'http://www.imdb.com/name/nm0598243/'
SET person_5260b4274ed4.wikidata = 'http://www.wikidata.org/wiki/Q109612'
SET person_5260b4274ed4.discographies = ['http://www.howardm.net/tsmonk/tsmonk.php', 'http://www.jazzdisco.org/monk/']
SET person_5260b4274ed4.databases = ['http://rateyourmusic.com/artist/thelonious_monk']
SET person_5260b4274ed4.musicbrainz = 'https://musicbrainz.org/artist/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.isni_list = ['http://isni.org/isni/0000000120249127']
SET person_5260b4274ed4.source = 'musicbrainz.org'


MERGE (person_c85fad20da55:Person{ uuid: '351d8bdf-33a1-45e2-8c04-c85fad20da55' }) 
SET person_c85fad20da55.name = 'Sarah Vaughan'
SET person_c85fad20da55.gender = 'Female'
SET person_c85fad20da55.country = 'US'
SET person_c85fad20da55.wikipedia = 'http://en.wikipedia.org/wiki/Sarah_Vaughan'
SET person_c85fad20da55.viaf = 'http://viaf.org/viaf/112758178'
SET person_c85fad20da55.allmusic = 'http://www.allmusic.com/artist/mn0000204901'
SET person_c85fad20da55.bbc = 'http://www.bbc.co.uk/music/artists/351d8bdf-33a1-45e2-8c04-c85fad20da55'
SET person_c85fad20da55.discogs = 'http://www.discogs.com/artist/8284'
SET person_c85fad20da55.imdb = 'http://www.imdb.com/name/nm0891098/'
SET person_c85fad20da55.wikidata = 'http://www.wikidata.org/wiki/Q229513'
SET person_c85fad20da55.databases = ['http://musicmoz.org/Bands_and_Artists/V/Vaughan,_Sarah/', 'https://rateyourmusic.com/artist/sarah_vaughan']
SET person_c85fad20da55.musicbrainz = 'https://musicbrainz.org/artist/351d8bdf-33a1-45e2-8c04-c85fad20da55'
SET person_c85fad20da55.isni_list = ['http://isni.org/isni/0000000081802574']
SET person_c85fad20da55.source = 'musicbrainz.org'


MERGE (person_76056fca9819:Person{ uuid: '6c1fe174-11fe-42b9-b92f-76056fca9819' }) 
SET person_76056fca9819.name = 'George Treadwell'
SET person_76056fca9819.gender = 'Male'
SET person_76056fca9819.country = 'US'
SET person_76056fca9819.wikipedia = 'http://en.wikipedia.org/wiki/George_Treadwell'
SET person_76056fca9819.allmusic = 'http://www.allmusic.com/artist/mn0000540213'
SET person_76056fca9819.discogs = 'http://www.discogs.com/artist/301974'
SET person_76056fca9819.wikidata = 'http://www.wikidata.org/wiki/Q5545302'
SET person_76056fca9819.databases = ['https://rateyourmusic.com/artist/george_treadwell']
SET person_76056fca9819.musicbrainz = 'https://musicbrainz.org/artist/6c1fe174-11fe-42b9-b92f-76056fca9819'
SET person_76056fca9819.isni_list = ['http://isni.org/isni/0000000063031614']
SET person_76056fca9819.source = 'musicbrainz.org'


MERGE (person_8d40b5dcbc41:Person{ uuid: '9be7f096-97ec-4615-8957-8d40b5dcbc41' }) 
SET person_8d40b5dcbc41.name = '[traditional]'
SET person_8d40b5dcbc41.disambiguation = 'Special Purpose Artist'
SET person_8d40b5dcbc41.allmusic = 'http://www.allmusic.com/artist/mn0000022266'
SET person_8d40b5dcbc41.discogs = 'http://www.discogs.com/artist/151641'
SET person_8d40b5dcbc41.databases = ['http://www.whosampled.com/Traditional-Folk/', 'https://rateyourmusic.com/artist/traditional']
SET person_8d40b5dcbc41.musicbrainz = 'https://musicbrainz.org/artist/9be7f096-97ec-4615-8957-8d40b5dcbc41'
SET person_8d40b5dcbc41.source = 'musicbrainz.org'


MERGE (person_323e6ce46c2a:Person{ uuid: '561d854a-6a28-4aa7-8c99-323e6ce46c2a' }) 
SET person_323e6ce46c2a.name = 'Miles Davis'
SET person_323e6ce46c2a.gender = 'Male'
SET person_323e6ce46c2a.disambiguation = 'jazz trumpeter, bandleader, songwriter'
SET person_323e6ce46c2a.country = 'US'
SET person_323e6ce46c2a.wikipedia = 'http://en.wikipedia.org/wiki/Miles_Davis'
SET person_323e6ce46c2a.viaf = 'http://viaf.org/viaf/97762193'
SET person_323e6ce46c2a.allmusic = 'http://www.allmusic.com/artist/mn0000423829'
SET person_323e6ce46c2a.bbc = 'http://www.bbc.co.uk/music/artists/561d854a-6a28-4aa7-8c99-323e6ce46c2a'
SET person_323e6ce46c2a.discogs = 'http://www.discogs.com/artist/23755'
SET person_323e6ce46c2a.imdb = 'http://www.imdb.com/name/nm0002537/'
SET person_323e6ce46c2a.wikidata = 'http://www.wikidata.org/wiki/Q93341'
SET person_323e6ce46c2a.discographies = ['http://all-blues.de/music/missing.htm', 'http://en.wikipedia.org/wiki/Miles_Davis_discography', 'http://www.plosin.com/milesahead/']
SET person_323e6ce46c2a.databases = ['http://musicmoz.org/Bands_and_Artists/D/Davis,_Miles/', 'http://rateyourmusic.com/artist/miles_davis']
SET person_323e6ce46c2a.musicbrainz = 'https://musicbrainz.org/artist/561d854a-6a28-4aa7-8c99-323e6ce46c2a'
SET person_323e6ce46c2a.isni_list = ['http://isni.org/isni/000000012144707X']
SET person_323e6ce46c2a.source = 'musicbrainz.org'


MERGE (work_232ecf2118a0:Work{ uuid: '2305f33d-094e-30a9-bb7c-232ecf2118a0' })
SET work_232ecf2118a0.name = 'Wail'
SET work_232ecf2118a0.source = 'musicbrainz.org'


MERGE (work_9eae6375ecb0:Work{ uuid: '6ae0f429-cd54-3ac2-b635-9eae6375ecb0' })
SET work_9eae6375ecb0.name = 'Question and Answer'
SET work_9eae6375ecb0.source = 'musicbrainz.org'


MERGE (work_34b69ccb6021:Work{ uuid: 'ada73560-c5da-4321-a049-34b69ccb6021' })
SET work_34b69ccb6021.name = 'Shulie a Bop'
SET work_34b69ccb6021.type = 'Song'
SET work_34b69ccb6021.source = 'musicbrainz.org'


MERGE (work_529eba30435c:Work{ uuid: '0e29de59-030d-4e0f-b30f-529eba30435c' })
SET work_529eba30435c.name = 'Dear Old Stockholm'
SET work_529eba30435c.iswc = 'T-900.312.305-5'
SET work_529eba30435c.type = 'Song'
SET work_529eba30435c.wikipedia = 'http://en.wikipedia.org/wiki/Dear_Old_Stockholm'
SET work_529eba30435c.wikidata = 'http://www.wikidata.org/wiki/Q404991'
SET work_529eba30435c.musicbrainz = 'https://musicbrainz.org/work/0e29de59-030d-4e0f-b30f-529eba30435c'
SET work_529eba30435c.source = 'musicbrainz.org'


MERGE (work_4144ea6dd50c:Work{ uuid: 'fe055727-d9c6-353d-a6c2-4144ea6dd50c' })
SET work_4144ea6dd50c.name = 'It’s Easy to Remember (and So Hard to Forget)'
SET work_4144ea6dd50c.type = 'Song'
SET work_4144ea6dd50c.allmusic = 'http://www.allmusic.com/song/mt0011784189'
SET work_4144ea6dd50c.wikidata = 'http://www.wikidata.org/wiki/Q1456083'
SET work_4144ea6dd50c.musicbrainz = 'https://musicbrainz.org/work/fe055727-d9c6-353d-a6c2-4144ea6dd50c'
SET work_4144ea6dd50c.source = 'musicbrainz.org'


MERGE (work_defeb1e074d1:Work{ uuid: 'c110a6cf-84e3-4f9b-bcee-defeb1e074d1' })
SET work_defeb1e074d1.name = 'Folk Song'
SET work_defeb1e074d1.type = 'Song'
SET work_defeb1e074d1.source = 'musicbrainz.org'


MERGE (work_87f90ecf4d9a:Work{ uuid: 'f314e1b5-45b7-39a9-a077-87f90ecf4d9a' })
SET work_87f90ecf4d9a.name = 'Sippin\\' at Bells'
SET work_87f90ecf4d9a.source = 'musicbrainz.org'


MERGE (work_513adcbc632b:Work{ uuid: '72193fa7-7da8-4a23-90a9-513adcbc632b' })
SET work_513adcbc632b.name = 'Bright Mississippi'
SET work_513adcbc632b.iswc = 'T-070.235.450-4'
SET work_513adcbc632b.type = 'Song'
SET work_513adcbc632b.source = 'musicbrainz.org'


MERGE (work_0da310d29396:Work{ uuid: '6774a429-5d8e-350f-8117-0da310d29396' })
SET work_0da310d29396.name = 'Prelude to a Kiss'
SET work_0da310d29396.iswc = 'T-071.068.525-8'
SET work_0da310d29396.type = 'Song'
SET work_0da310d29396.wikidata = 'http://www.wikidata.org/wiki/Q1579875'
SET work_0da310d29396.musicbrainz = 'https://musicbrainz.org/work/6774a429-5d8e-350f-8117-0da310d29396'
SET work_0da310d29396.source = 'musicbrainz.org'


MERGE (work_88af68626085:Work{ uuid: 'ef6b8ef1-0d16-4c4b-87b0-88af68626085' })
SET work_88af68626085.name = 'Green Chimneys'
SET work_88af68626085.type = 'Song'
SET work_88af68626085.musicbrainz = 'https://musicbrainz.org/work/ef6b8ef1-0d16-4c4b-87b0-88af68626085'
SET work_88af68626085.source = 'musicbrainz.org'



// performances of
MERGE (perf_a82d57813460)-[:PERFORMANCE_OF]->(work_232ecf2118a0)
MERGE (perf_e0f3424edd37)-[:PERFORMANCE_OF]->(work_9eae6375ecb0)
MERGE (perf_e18d2d97b850)-[:PERFORMANCE_OF]->(work_34b69ccb6021)
MERGE (perf_e91a31e0d410)-[:PERFORMANCE_OF]->(work_529eba30435c)
MERGE (perf_b6c3b5a11e18)-[:PERFORMANCE_OF]->(work_4144ea6dd50c)
MERGE (perf_63d287403253)-[:PERFORMANCE_OF]->(work_defeb1e074d1)
MERGE (perf_3178b59c7b0b)-[:PERFORMANCE_OF]->(work_87f90ecf4d9a)
MERGE (perf_95eca70a29aa)-[:PERFORMANCE_OF]->(work_513adcbc632b)
MERGE (perf_b370c5065f4e)-[:PERFORMANCE_OF]->(work_0da310d29396)
MERGE (perf_93f82b3bc3ba)-[:PERFORMANCE_OF]->(work_88af68626085)


// composers
MERGE (person_340d64fbb41c)-[:COMPOSED]->(work_232ecf2118a0)
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_9eae6375ecb0)
MERGE (person_c85fad20da55)-[:COMPOSED]->(work_34b69ccb6021)
MERGE (person_76056fca9819)-[:COMPOSED]->(work_34b69ccb6021)
MERGE (person_8d40b5dcbc41)-[:COMPOSED]->(work_529eba30435c)
MERGE (person_acc0205f7513)-[:COMPOSED]->(work_4144ea6dd50c)
MERGE (person_5a269b32b4c2)-[:COMPOSED]->(work_defeb1e074d1)
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_87f90ecf4d9a)
MERGE (person_c73775716312)-[:COMPOSED]->(work_87f90ecf4d9a)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_513adcbc632b)
MERGE (person_7eeeb45e411f)-[:COMPOSED]->(work_0da310d29396)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_88af68626085)


// place nodes

MERGE (place_decbb365c07f:Place{ uuid: '74e50e58-5deb-4b99-93a2-decbb365c07f' })
SET place_decbb365c07f.name = 'New York'
SET place_decbb365c07f.source = 'musicbrainz.org'

MERGE (place_02f85919f8ff:Place{ uuid: 'aa6471ba-2a97-424e-90ef-02f85919f8ff' })
SET place_02f85919f8ff.name = 'Scullers Jazz Club'
SET place_02f85919f8ff.address = '400, Soldiers Field Road, Allston, Boston, Suffolk County, Massachusetts, 02163, United States of America'
SET place_02f85919f8ff.lat = '42.364305'
SET place_02f85919f8ff.lng = '-71.118153'
SET place_02f85919f8ff.source = 'musicbrainz.org'


// place relationships
MERGE (perf_a82d57813460)-[:HAS_PLACE { type: 'recorded in', begin_date: '1999-11-23', end_date: '1999-11-24' }]->(place_decbb365c07f)
MERGE (perf_e0f3424edd37)-[:HAS_PLACE { type: 'recorded in', begin_date: '1999-11-23', end_date: '1999-11-24' }]->(place_decbb365c07f)
MERGE (perf_e18d2d97b850)-[:HAS_PLACE { type: 'recorded in', begin_date: '1999-11-23', end_date: '1999-11-24' }]->(place_decbb365c07f)
MERGE (perf_e91a31e0d410)-[:HAS_PLACE { type: 'recorded in', begin_date: '1999-11-23', end_date: '1999-11-24' }]->(place_decbb365c07f)
MERGE (perf_b6c3b5a11e18)-[:HAS_PLACE { type: 'recorded in', begin_date: '1999-11-23', end_date: '1999-11-24' }]->(place_decbb365c07f)
MERGE (perf_63d287403253)-[:HAS_PLACE { type: 'recorded in', begin_date: '1999-11-23', end_date: '1999-11-24' }]->(place_decbb365c07f)
MERGE (perf_3178b59c7b0b)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-09-10', end_date: '1999-09-11' }]->(place_02f85919f8ff)
MERGE (perf_95eca70a29aa)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-09-10', end_date: '1999-09-11' }]->(place_02f85919f8ff)
MERGE (perf_b370c5065f4e)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-09-10', end_date: '1999-09-11' }]->(place_02f85919f8ff)
MERGE (perf_93f82b3bc3ba)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-09-10', end_date: '1999-09-11' }]->(place_02f85919f8ff)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_a82d57813460)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a82d57813460)
MERGE (person_e5cc86e2f134)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a82d57813460)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_e0f3424edd37)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e0f3424edd37)
MERGE (person_e5cc86e2f134)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_e0f3424edd37)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_e18d2d97b850)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e18d2d97b850)
MERGE (person_e5cc86e2f134)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_e18d2d97b850)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_e91a31e0d410)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e91a31e0d410)
MERGE (person_e5cc86e2f134)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_e91a31e0d410)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_b6c3b5a11e18)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b6c3b5a11e18)
MERGE (person_e5cc86e2f134)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_b6c3b5a11e18)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_63d287403253)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_63d287403253)
MERGE (person_e5cc86e2f134)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_63d287403253)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_3178b59c7b0b)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_3178b59c7b0b)
MERGE (person_e5cc86e2f134)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_3178b59c7b0b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_95eca70a29aa)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_95eca70a29aa)
MERGE (person_e5cc86e2f134)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_95eca70a29aa)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_b370c5065f4e)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b370c5065f4e)
MERGE (person_e5cc86e2f134)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_b370c5065f4e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_93f82b3bc3ba)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_93f82b3bc3ba)
MERGE (person_e5cc86e2f134)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_93f82b3bc3ba)



"""
)