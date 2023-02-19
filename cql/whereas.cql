// releases

MERGE (release_5de3bfd3fa08:Release{ uuid: '7f0548dd-1cfc-4262-a064-5de3bfd3fa08' })
SET release_5de3bfd3fa08.name = 'Whereas'
SET release_5de3bfd3fa08.country = 'DE'
SET release_5de3bfd3fa08.date = '2007-03-12'
SET release_5de3bfd3fa08.format = 'Digital Media'
SET release_5de3bfd3fa08.musicbrainz = 'http://musicbrainz.org/release/7f0548dd-1cfc-4262-a064-5de3bfd3fa08'
SET release_5de3bfd3fa08.source = 'musicbrainz.org'
SET release_5de3bfd3fa08.timestamp = timestamp()

MERGE (person_017082007047:Person{ uuid: '5f2472a7-50bd-4b2c-8178-017082007047' }) 
SET person_017082007047.name = 'Robert Rodriguez'
SET person_017082007047.gender = 'Male'
SET person_017082007047.disambiguation = 'piano'
SET person_017082007047.discogs = 'https://www.discogs.com/artist/575204'
SET person_017082007047.musicbrainz = 'https://musicbrainz.org/artist/5f2472a7-50bd-4b2c-8178-017082007047'
SET person_017082007047.source = 'musicbrainz.org'
SET person_017082007047.timestamp = timestamp()

MERGE (person_fdfff1522b37:Person{ uuid: '816eedff-76ea-4d09-aabe-fdfff1522b37' }) 
SET person_fdfff1522b37.name = 'Doug Yoel'
SET person_fdfff1522b37.gender = 'Male'
SET person_fdfff1522b37.source = 'musicbrainz.org'
SET person_fdfff1522b37.timestamp = timestamp()

MERGE (person_ae183779dae1:Person{ uuid: '33bba978-5cf5-43e4-a247-ae183779dae1' }) 
SET person_ae183779dae1.name = 'Jaleel Shaw'
SET person_ae183779dae1.gender = 'Male'
SET person_ae183779dae1.country = 'US'
SET person_ae183779dae1.allmusic = 'https://www.allmusic.com/artist/mn0000361733'
SET person_ae183779dae1.discogs = 'https://www.discogs.com/artist/1049749'
SET person_ae183779dae1.viaf = 'http://viaf.org/viaf/277507711'
SET person_ae183779dae1.wikidata = 'https://www.wikidata.org/wiki/Q1679742'
SET person_ae183779dae1.databases = ['http://id.loc.gov/authorities/names/no2008145711', 'https://www.worldcat.org/identities/lccn-no2008145711']
SET person_ae183779dae1.musicbrainz = 'https://musicbrainz.org/artist/33bba978-5cf5-43e4-a247-ae183779dae1'
SET person_ae183779dae1.isni_list = ['http://isni.org/isni/0000000384727890']
SET person_ae183779dae1.source = 'musicbrainz.org'
SET person_ae183779dae1.timestamp = timestamp()

MERGE (person_6f0a331cc1ca:Person{ uuid: '2c090b57-5e9d-49c5-9b71-6f0a331cc1ca' }) 
SET person_6f0a331cc1ca.name = 'Roy Haynes'
SET person_6f0a331cc1ca.gender = 'Male'
SET person_6f0a331cc1ca.disambiguation = 'American jazz drummer and bandleader'
SET person_6f0a331cc1ca.country = 'US'
SET person_6f0a331cc1ca.allmusic = 'https://www.allmusic.com/artist/mn0000290464'
SET person_6f0a331cc1ca.bbc = 'https://www.bbc.co.uk/music/artists/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.discogs = 'https://www.discogs.com/artist/255556'
SET person_6f0a331cc1ca.imdb = 'https://www.imdb.com/name/nm0371542/'
SET person_6f0a331cc1ca.viaf = 'http://viaf.org/viaf/84975999'
SET person_6f0a331cc1ca.wikidata = 'https://www.wikidata.org/wiki/Q448235'
SET person_6f0a331cc1ca.databases = ['http://d-nb.info/gnd/134400623', 'http://id.loc.gov/authorities/names/n81140108', 'https://catalogue.bnf.fr/ark:/12148/cb13895060w', 'http://snaccooperative.org/ark:/99166/w6fj33d4', 'https://www.worldcat.org/identities/lccn-n81140108']
SET person_6f0a331cc1ca.musicbrainz = 'https://musicbrainz.org/artist/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.isni_list = ['http://isni.org/isni/0000000078266176']
SET person_6f0a331cc1ca.source = 'musicbrainz.org'
SET person_6f0a331cc1ca.timestamp = timestamp()

MERGE (person_727e344551dc:Person{ uuid: 'b57ca18c-fe34-4a5d-b896-727e344551dc' }) 
SET person_727e344551dc.name = 'John Sullivan'
SET person_727e344551dc.gender = 'Male'
SET person_727e344551dc.disambiguation = 'bass'
SET person_727e344551dc.country = 'US'
SET person_727e344551dc.discogs = 'https://www.discogs.com/artist/324037'
SET person_727e344551dc.musicbrainz = 'https://musicbrainz.org/artist/b57ca18c-fe34-4a5d-b896-727e344551dc'
SET person_727e344551dc.source = 'musicbrainz.org'
SET person_727e344551dc.timestamp = timestamp()
// labels

MERGE (label_45a4aac43b37:Label{ uuid: 'd3698a68-ef9f-431e-93a0-45a4aac43b37' })
SET label_45a4aac43b37.name= 'Dreyfus Jazz'

// performances

MERGE (perf_dd16167c924c:Performance{ uuid: '00850441-9de9-4a15-b080-dd16167c924c' })
SET perf_dd16167c924c.name = 'Mr. P.C.'
SET perf_dd16167c924c.duration = '10:33'
SET perf_dd16167c924c.begin = '2006-01-20'
SET perf_dd16167c924c.end = '2006-01-22'
SET perf_dd16167c924c.source = 'musicbrainz.org'
SET perf_dd16167c924c.timestamp = timestamp()

MERGE (perf_439f808dabdc:Performance{ uuid: '3e0d5d6b-72e2-49a9-9529-439f808dabdc' })
SET perf_439f808dabdc.name = 'My Heart Belongs to Daddy'
SET perf_439f808dabdc.duration = '11:32'
SET perf_439f808dabdc.begin = '2006-01-20'
SET perf_439f808dabdc.end = '2006-01-22'
SET perf_439f808dabdc.source = 'musicbrainz.org'
SET perf_439f808dabdc.timestamp = timestamp()

MERGE (perf_afb19e246482:Performance{ uuid: 'ec6287f8-9e9d-44e3-bb01-afb19e246482' })
SET perf_afb19e246482.name = 'Like This'
SET perf_afb19e246482.duration = '5:40'
SET perf_afb19e246482.begin = '2006-01-20'
SET perf_afb19e246482.end = '2006-01-22'
SET perf_afb19e246482.source = 'musicbrainz.org'
SET perf_afb19e246482.timestamp = timestamp()

MERGE (perf_296a807f0bd8:Performance{ uuid: 'fdd74e26-14f4-4e11-8450-296a807f0bd8' })
SET perf_296a807f0bd8.name = 'Hippidy Hop (Drum Solo)'
SET perf_296a807f0bd8.duration = '6:58'
SET perf_296a807f0bd8.begin = '2006-01-20'
SET perf_296a807f0bd8.end = '2006-01-22'
SET perf_296a807f0bd8.source = 'musicbrainz.org'
SET perf_296a807f0bd8.timestamp = timestamp()

MERGE (perf_6d088d867cab:Performance{ uuid: '104bf94b-597c-4a2d-b6ce-6d088d867cab' })
SET perf_6d088d867cab.name = 'James'
SET perf_6d088d867cab.duration = '5:57'
SET perf_6d088d867cab.begin = '2006-01-20'
SET perf_6d088d867cab.end = '2006-01-22'
SET perf_6d088d867cab.source = 'musicbrainz.org'
SET perf_6d088d867cab.timestamp = timestamp()

MERGE (perf_6e9bc9437335:Performance{ uuid: '6824f6da-70f3-4d5f-977d-6e9bc9437335' })
SET perf_6e9bc9437335.name = 'Bemsha Swing / True or False'
SET perf_6e9bc9437335.duration = '8:55'
SET perf_6e9bc9437335.begin = '2006-01-20'
SET perf_6e9bc9437335.end = '2006-01-22'
SET perf_6e9bc9437335.source = 'musicbrainz.org'
SET perf_6e9bc9437335.timestamp = timestamp()

MERGE (perf_2ade057eda06:Performance{ uuid: 'dc786991-07eb-4dcd-8044-2ade057eda06' })
SET perf_2ade057eda06.name = 'Inner Urge'
SET perf_2ade057eda06.duration = '11:01'
SET perf_2ade057eda06.begin = '2006-01-20'
SET perf_2ade057eda06.end = '2006-01-22'
SET perf_2ade057eda06.source = 'musicbrainz.org'
SET perf_2ade057eda06.timestamp = timestamp()

MERGE (perf_baecb582ab9a:Performance{ uuid: '3b477610-fc94-4279-a6ab-baecb582ab9a' })
SET perf_baecb582ab9a.name = 'Segment'
SET perf_baecb582ab9a.duration = '8:36'
SET perf_baecb582ab9a.begin = '2006-01-20'
SET perf_baecb582ab9a.end = '2006-01-22'
SET perf_baecb582ab9a.source = 'musicbrainz.org'
SET perf_baecb582ab9a.timestamp = timestamp()



// labels
MERGE (release_5de3bfd3fa08)-[:HAS_LABEL]->(label_45a4aac43b37)


// tracks
MERGE (release_5de3bfd3fa08)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_dd16167c924c)
MERGE (release_5de3bfd3fa08)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_439f808dabdc)
MERGE (release_5de3bfd3fa08)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_afb19e246482)
MERGE (release_5de3bfd3fa08)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_296a807f0bd8)
MERGE (release_5de3bfd3fa08)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_6d088d867cab)
MERGE (release_5de3bfd3fa08)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_6e9bc9437335)
MERGE (release_5de3bfd3fa08)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_2ade057eda06)
MERGE (release_5de3bfd3fa08)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_baecb582ab9a)

// works

MERGE (person_5260b4274ed4:Person{ uuid: '8e8c7417-c905-46b1-b42a-5260b4274ed4' }) 
SET person_5260b4274ed4.name = 'Thelonious Monk'
SET person_5260b4274ed4.gender = 'Male'
SET person_5260b4274ed4.country = 'US'
SET person_5260b4274ed4.allmusic = 'https://www.allmusic.com/artist/mn0000490416'
SET person_5260b4274ed4.bbc = 'https://www.bbc.co.uk/music/artists/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.discogs = 'https://www.discogs.com/artist/145256'
SET person_5260b4274ed4.imdb = 'https://www.imdb.com/name/nm0598243/'
SET person_5260b4274ed4.viaf = 'http://viaf.org/viaf/44485892'
SET person_5260b4274ed4.wikidata = 'https://www.wikidata.org/wiki/Q109612'
SET person_5260b4274ed4.databases = ['http://d-nb.info/gnd/118826158', 'http://id.loc.gov/authorities/names/n82218969', 'https://catalogue.bnf.fr/ark:/12148/cb13897622g', 'http://snaccooperative.org/ark:/99166/w6j38zvn', 'https://rateyourmusic.com/artist/thelonious_monk', 'https://www.worldcat.org/identities/lccn-n82218969']
SET person_5260b4274ed4.musicbrainz = 'https://musicbrainz.org/artist/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.isni_list = ['http://isni.org/isni/0000000120249127']
SET person_5260b4274ed4.source = 'musicbrainz.org'
SET person_5260b4274ed4.timestamp = timestamp()

MERGE (person_9ee947b4ce37:Person{ uuid: 'bcab8301-c7e5-4689-a4ad-9ee947b4ce37' }) 
SET person_9ee947b4ce37.name = 'Joe Henderson'
SET person_9ee947b4ce37.gender = 'Male'
SET person_9ee947b4ce37.disambiguation = 'US jazz tenor saxophonist'
SET person_9ee947b4ce37.country = 'US'
SET person_9ee947b4ce37.allmusic = 'https://www.allmusic.com/artist/mn0000139804'
SET person_9ee947b4ce37.allmusic = 'https://www.allmusic.com/artist/mn0002687715'
SET person_9ee947b4ce37.discogs = 'https://www.discogs.com/artist/10079'
SET person_9ee947b4ce37.viaf = 'http://viaf.org/viaf/115064662'
SET person_9ee947b4ce37.wikidata = 'https://www.wikidata.org/wiki/Q506006'
SET person_9ee947b4ce37.databases = ['http://d-nb.info/gnd/131961454', 'http://id.loc.gov/authorities/names/n82164702', 'https://catalogue.bnf.fr/ark:/12148/cb138951291', 'http://snaccooperative.org/ark:/99166/w6hm8fsd', 'https://nla.gov.au/nla.party-1048452', 'https://openlibrary.org/works/OL5629680A', 'https://rateyourmusic.com/artist/joe_henderson', 'https://www.worldcat.org/identities/lccn-n82164702']
SET person_9ee947b4ce37.musicbrainz = 'https://musicbrainz.org/artist/bcab8301-c7e5-4689-a4ad-9ee947b4ce37'
SET person_9ee947b4ce37.isni_list = ['http://isni.org/isni/0000000081835181']
SET person_9ee947b4ce37.source = 'musicbrainz.org'
SET person_9ee947b4ce37.timestamp = timestamp()

MERGE (person_0ad7756dd538:Person{ uuid: '210b51ef-bece-44c6-aa94-0ad7756dd538' }) 
SET person_0ad7756dd538.name = 'Lyle Mays'
SET person_0ad7756dd538.gender = 'Male'
SET person_0ad7756dd538.country = 'US'
SET person_0ad7756dd538.allmusic = 'https://www.allmusic.com/artist/mn0000171015'
SET person_0ad7756dd538.discogs = 'https://www.discogs.com/artist/222583'
SET person_0ad7756dd538.imdb = 'https://www.imdb.com/name/nm0563077/'
SET person_0ad7756dd538.viaf = 'http://viaf.org/viaf/39562612'
SET person_0ad7756dd538.wikidata = 'https://www.wikidata.org/wiki/Q963426'
SET person_0ad7756dd538.databases = ['http://d-nb.info/gnd/134458974', 'http://id.loc.gov/authorities/names/n78096790', 'https://catalogue.bnf.fr/ark:/12148/cb13897265n', 'https://rateyourmusic.com/artist/lyle_mays', 'https://www.worldcat.org/identities/lccn-n78096790']
SET person_0ad7756dd538.musicbrainz = 'https://musicbrainz.org/artist/210b51ef-bece-44c6-aa94-0ad7756dd538'
SET person_0ad7756dd538.isni_list = ['http://isni.org/isni/000000012278596X']
SET person_0ad7756dd538.source = 'musicbrainz.org'
SET person_0ad7756dd538.timestamp = timestamp()

MERGE (person_72ad46cdb831:Person{ uuid: 'b625448e-bf4a-41c3-a421-72ad46cdb831' }) 
SET person_72ad46cdb831.name = 'John Coltrane'
SET person_72ad46cdb831.gender = 'Male'
SET person_72ad46cdb831.country = 'US'
SET person_72ad46cdb831.allmusic = 'https://www.allmusic.com/artist/mn0000175553'
SET person_72ad46cdb831.bbc = 'https://www.bbc.co.uk/music/artists/b625448e-bf4a-41c3-a421-72ad46cdb831'
SET person_72ad46cdb831.discogs = 'https://www.discogs.com/artist/97545'
SET person_72ad46cdb831.imdb = 'https://www.imdb.com/name/nm0173328/'
SET person_72ad46cdb831.viaf = 'http://viaf.org/viaf/61731379'
SET person_72ad46cdb831.wikidata = 'https://www.wikidata.org/wiki/Q7346'
SET person_72ad46cdb831.databases = ['http://d-nb.info/gnd/118521667', 'http://id.loc.gov/authorities/names/n50031907', 'https://catalogue.bnf.fr/ark:/12148/cb138926615', 'https://ibdb.com/person.php?id=485239', 'http://snaccooperative.org/ark:/99166/w6x92hns', 'https://nla.gov.au/nla.party-1006213', 'https://openlibrary.org/works/OL7513936A', 'https://rateyourmusic.com/artist/john_coltrane', 'https://www.musik-sammler.de/artist/john-coltrane/', 'https://www.whosampled.com/John-Coltrane/', 'https://www.worldcat.org/identities/lccn-n50-031907', 'http://www.45cat.com/artist/john-coltrane', 'http://www.45worlds.com/cdalbum/artist/john-coltrane', 'http://www.45worlds.com/tape/artist/john-coltrane', 'http://www.45worlds.com/vinyl/artist/john-coltrane']
SET person_72ad46cdb831.musicbrainz = 'https://musicbrainz.org/artist/b625448e-bf4a-41c3-a421-72ad46cdb831'
SET person_72ad46cdb831.isni_list = ['http://isni.org/isni/000000012280792X']
SET person_72ad46cdb831.source = 'musicbrainz.org'
SET person_72ad46cdb831.timestamp = timestamp()

MERGE (person_173c16a9a591:Person{ uuid: '733f3f0c-dde8-45e7-a725-173c16a9a591' }) 
SET person_173c16a9a591.name = 'Denzil Best'
SET person_173c16a9a591.gender = 'Male'
SET person_173c16a9a591.country = 'US'
SET person_173c16a9a591.allmusic = 'https://www.allmusic.com/artist/mn0000257524'
SET person_173c16a9a591.discogs = 'https://www.discogs.com/artist/259091'
SET person_173c16a9a591.viaf = 'http://viaf.org/viaf/51874508'
SET person_173c16a9a591.wikidata = 'https://www.wikidata.org/wiki/Q488329'
SET person_173c16a9a591.wikipedia = 'https://en.wikipedia.org/wiki/Denzil_Best'
SET person_173c16a9a591.databases = ['http://d-nb.info/gnd/134626427', 'http://id.loc.gov/authorities/names/nr90016428', 'https://catalogue.bnf.fr/ark:/12148/cb138914752', 'http://snaccooperative.org/ark:/99166/w6gp1n43', 'https://www.worldcat.org/identities/lccn-nr90016428']
SET person_173c16a9a591.musicbrainz = 'https://musicbrainz.org/artist/733f3f0c-dde8-45e7-a725-173c16a9a591'
SET person_173c16a9a591.isni_list = ['http://isni.org/isni/0000000071434886']
SET person_173c16a9a591.source = 'musicbrainz.org'
SET person_173c16a9a591.timestamp = timestamp()

MERGE (person_a37897b950ce:Person{ uuid: '4a94a6cb-e70a-418b-bb53-a37897b950ce' }) 
SET person_a37897b950ce.name = 'Cole Porter'
SET person_a37897b950ce.gender = 'Male'
SET person_a37897b950ce.disambiguation = 'composer'
SET person_a37897b950ce.country = 'US'
SET person_a37897b950ce.allmusic = 'https://www.allmusic.com/artist/mn0000109607'
SET person_a37897b950ce.discogs = 'https://www.discogs.com/artist/264026'
SET person_a37897b950ce.imdb = 'https://www.imdb.com/name/nm0006234/'
SET person_a37897b950ce.viaf = 'http://viaf.org/viaf/5118684'
SET person_a37897b950ce.wikidata = 'https://www.wikidata.org/wiki/Q215120'
SET person_a37897b950ce.databases = ['http://d-nb.info/gnd/11879292X', 'http://id.loc.gov/authorities/names/n80017862', 'https://catalogue.bnf.fr/ark:/12148/cb13898618g', 'https://ibdb.com/person.php?id=12257', 'http://snaccooperative.org/ark:/99166/w6j38s5m', 'https://nla.gov.au/nla.party-949524', 'https://openlibrary.org/works/OL709416A', 'http://soundtrackcollector.com/composer/166/', 'https://rateyourmusic.com/artist/cole_porter', 'https://www.worldcat.org/identities/lccn-n80017862', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Cole&last=Porter&middle=']
SET person_a37897b950ce.musicbrainz = 'https://musicbrainz.org/artist/4a94a6cb-e70a-418b-bb53-a37897b950ce'
SET person_a37897b950ce.isni_list = ['http://isni.org/isni/0000000108653610']
SET person_a37897b950ce.source = 'musicbrainz.org'
SET person_a37897b950ce.timestamp = timestamp()

MERGE (person_f8091d98cf25:Person{ uuid: '7daac7f9-8fcc-485f-a14f-f8091d98cf25' }) 
SET person_f8091d98cf25.name = 'Pat Metheny'
SET person_f8091d98cf25.gender = 'Male'
SET person_f8091d98cf25.country = 'US'
SET person_f8091d98cf25.allmusic = 'https://www.allmusic.com/artist/mn0000179698'
SET person_f8091d98cf25.bbc = 'https://www.bbc.co.uk/music/artists/7daac7f9-8fcc-485f-a14f-f8091d98cf25'
SET person_f8091d98cf25.discogs = 'https://www.discogs.com/artist/20185'
SET person_f8091d98cf25.imdb = 'https://www.imdb.com/name/nm0582533/'
SET person_f8091d98cf25.viaf = 'http://viaf.org/viaf/22188874'
SET person_f8091d98cf25.wikidata = 'https://www.wikidata.org/wiki/Q213887'
SET person_f8091d98cf25.databases = ['http://d-nb.info/gnd/118946803', 'http://id.loc.gov/authorities/names/n78096789', 'https://catalogue.bnf.fr/ark:/12148/cb122016747', 'http://snaccooperative.org/ark:/99166/w6gj10fw', 'https://www.musik-sammler.de/artist/pat-metheny/', 'https://www.progarchives.com/artist.asp?id=2445', 'https://www.worldcat.org/identities/lccn-n78096789']
SET person_f8091d98cf25.musicbrainz = 'https://musicbrainz.org/artist/7daac7f9-8fcc-485f-a14f-f8091d98cf25'
SET person_f8091d98cf25.isni_list = ['http://isni.org/isni/0000000121236985']
SET person_f8091d98cf25.source = 'musicbrainz.org'
SET person_f8091d98cf25.timestamp = timestamp()

MERGE (person_c73775716312:Person{ uuid: 'c7356af9-9ea6-4a78-a55b-c73775716312' }) 
SET person_c73775716312.name = 'Charlie Parker'
SET person_c73775716312.gender = 'Male'
SET person_c73775716312.disambiguation = 'a.k.a. “Bird”, jazz alto saxophonist'
SET person_c73775716312.country = 'US'
SET person_c73775716312.allmusic = 'https://www.allmusic.com/artist/mn0000211758'
SET person_c73775716312.bbc = 'https://www.bbc.co.uk/music/artists/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.discogs = 'https://www.discogs.com/artist/75617'
SET person_c73775716312.imdb = 'https://www.imdb.com/name/nm0662127/'
SET person_c73775716312.viaf = 'http://viaf.org/viaf/10034216'
SET person_c73775716312.wikidata = 'https://www.wikidata.org/wiki/Q103767'
SET person_c73775716312.databases = ['http://d-nb.info/gnd/118739328', 'http://id.loc.gov/authorities/names/n50050327', 'https://catalogue.bnf.fr/ark:/12148/cb13898247z', 'http://snaccooperative.org/ark:/99166/w67086vq', 'https://nla.gov.au/nla.party-911160', 'https://openlibrary.org/works/OL4918032A', 'https://rateyourmusic.com/artist/charlie_parker', 'https://www.musik-sammler.de/artist/charlie-parker/', 'https://www.worldcat.org/identities/lccn-n50050327']
SET person_c73775716312.musicbrainz = 'https://musicbrainz.org/artist/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.isni_list = ['http://isni.org/isni/0000000120955806', 'http://isni.org/isni/0000000368633974']
SET person_c73775716312.source = 'musicbrainz.org'
SET person_c73775716312.timestamp = timestamp()

MERGE (work_01f1b65c688e:Work{ uuid: 'f913cde7-5418-3a1d-bbe5-01f1b65c688e' })
SET work_01f1b65c688e.name = 'My Heart Belongs to Daddy'
SET work_01f1b65c688e.iswc = 'T-070.110.901-4'
SET work_01f1b65c688e.type = 'Song'
SET work_01f1b65c688e.wikidata = 'https://www.wikidata.org/wiki/Q3137581'
SET work_01f1b65c688e.databases = ['https://castalbums.org/songs/My-Heart-Belongs-to-Daddy/27281/']
SET work_01f1b65c688e.musicbrainz = 'https://musicbrainz.org/work/f913cde7-5418-3a1d-bbe5-01f1b65c688e'
SET work_01f1b65c688e.source = 'musicbrainz.org'
SET work_01f1b65c688e.timestamp = timestamp()

MERGE (work_0ffd3097a545:Work{ uuid: '80c3b9e2-1db7-3aea-b99b-0ffd3097a545' })
SET work_0ffd3097a545.name = 'Inner Urge'
SET work_0ffd3097a545.iswc = 'T-070.919.168-3'
SET work_0ffd3097a545.type = 'Song'
SET work_0ffd3097a545.source = 'musicbrainz.org'
SET work_0ffd3097a545.timestamp = timestamp()

MERGE (work_0c2a60e39245:Work{ uuid: '55bc467e-a6f6-3561-87de-0c2a60e39245' })
SET work_0c2a60e39245.name = 'Bemsha Swing'
SET work_0c2a60e39245.iswc = 'T-924.101.469-7'
SET work_0c2a60e39245.type = 'Song'
SET work_0c2a60e39245.wikidata = 'https://www.wikidata.org/wiki/Q816388'
SET work_0c2a60e39245.musicbrainz = 'https://musicbrainz.org/work/55bc467e-a6f6-3561-87de-0c2a60e39245'
SET work_0c2a60e39245.source = 'musicbrainz.org'
SET work_0c2a60e39245.timestamp = timestamp()

MERGE (work_d2abd8079b79:Work{ uuid: 'aac2b2ad-8e45-3abf-8532-d2abd8079b79' })
SET work_d2abd8079b79.name = 'Mr. P.C.'
SET work_d2abd8079b79.iswc = 'T-070.242.324-2'
SET work_d2abd8079b79.type = 'Song'
SET work_d2abd8079b79.wikidata = 'https://www.wikidata.org/wiki/Q3327170'
SET work_d2abd8079b79.musicbrainz = 'https://musicbrainz.org/work/aac2b2ad-8e45-3abf-8532-d2abd8079b79'
SET work_d2abd8079b79.source = 'musicbrainz.org'
SET work_d2abd8079b79.timestamp = timestamp()

MERGE (work_53195ae330bb:Work{ uuid: '239ee894-a97b-3806-ab10-53195ae330bb' })
SET work_53195ae330bb.name = 'Segment'
SET work_53195ae330bb.iswc = 'T-070.940.163-7'
SET work_53195ae330bb.type = 'Song'
SET work_53195ae330bb.musicbrainz = 'https://musicbrainz.org/work/239ee894-a97b-3806-ab10-53195ae330bb'
SET work_53195ae330bb.source = 'musicbrainz.org'
SET work_53195ae330bb.timestamp = timestamp()

MERGE (work_567b5ea2c2bf:Work{ uuid: 'de481d05-d2a8-369d-b1dc-567b5ea2c2bf' })
SET work_567b5ea2c2bf.name = 'James'
SET work_567b5ea2c2bf.iswc = 'T-070.241.328-2'
SET work_567b5ea2c2bf.source = 'musicbrainz.org'
SET work_567b5ea2c2bf.timestamp = timestamp()


// performances of
MERGE (perf_439f808dabdc)-[:PERFORMANCE_OF]->(work_01f1b65c688e)
MERGE (perf_2ade057eda06)-[:PERFORMANCE_OF]->(work_0ffd3097a545)
MERGE (perf_6e9bc9437335)-[:PERFORMANCE_OF {medley: true}]->(work_0c2a60e39245)
MERGE (perf_dd16167c924c)-[:PERFORMANCE_OF]->(work_d2abd8079b79)
MERGE (perf_baecb582ab9a)-[:PERFORMANCE_OF]->(work_53195ae330bb)
MERGE (perf_6d088d867cab)-[:PERFORMANCE_OF]->(work_567b5ea2c2bf)


// composers
MERGE (person_a37897b950ce)-[:COMPOSED]->(work_01f1b65c688e)
MERGE (person_a37897b950ce)-[:WROTE_LYRICS]->(work_01f1b65c688e)
MERGE (person_9ee947b4ce37)-[:COMPOSED]->(work_0ffd3097a545)
MERGE (person_173c16a9a591)-[:COMPOSED]->(work_0c2a60e39245)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_0c2a60e39245)
MERGE (person_72ad46cdb831)-[:COMPOSED]->(work_d2abd8079b79)
MERGE (person_c73775716312)-[:COMPOSED]->(work_53195ae330bb)
MERGE (person_0ad7756dd538)-[:COMPOSED]->(work_567b5ea2c2bf)
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_567b5ea2c2bf)


// place nodes

MERGE (place_f5a838f1f06d:Place{ uuid: '85f487a8-496e-45bd-ade4-f5a838f1f06d' })
SET place_f5a838f1f06d.name = 'Artists\' Quarter'
SET place_f5a838f1f06d.source = 'musicbrainz.org'


// place relationships
MERGE (perf_dd16167c924c)-[:HAS_PLACE { type: 'recorded at', begin: '2006-01-20', end: '2006-01-22' }]->(place_f5a838f1f06d)
MERGE (perf_439f808dabdc)-[:HAS_PLACE { type: 'recorded at', begin: '2006-01-20', end: '2006-01-22' }]->(place_f5a838f1f06d)
MERGE (perf_afb19e246482)-[:HAS_PLACE { type: 'recorded at', begin: '2006-01-20', end: '2006-01-22' }]->(place_f5a838f1f06d)
MERGE (perf_296a807f0bd8)-[:HAS_PLACE { type: 'recorded at', begin: '2006-01-20', end: '2006-01-22' }]->(place_f5a838f1f06d)
MERGE (perf_6d088d867cab)-[:HAS_PLACE { type: 'recorded at', begin: '2006-01-20', end: '2006-01-22' }]->(place_f5a838f1f06d)
MERGE (perf_6e9bc9437335)-[:HAS_PLACE { type: 'recorded at', begin: '2006-01-20', end: '2006-01-22' }]->(place_f5a838f1f06d)
MERGE (perf_2ade057eda06)-[:HAS_PLACE { type: 'recorded at', begin: '2006-01-20', end: '2006-01-22' }]->(place_f5a838f1f06d)
MERGE (perf_baecb582ab9a)-[:HAS_PLACE { type: 'recorded at', begin: '2006-01-20', end: '2006-01-22' }]->(place_f5a838f1f06d)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_dd16167c924c)
MERGE (person_017082007047)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_dd16167c924c)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_dd16167c924c)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_dd16167c924c)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_dd16167c924c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_439f808dabdc)
MERGE (person_017082007047)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_439f808dabdc)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_439f808dabdc)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_439f808dabdc)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_439f808dabdc)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_afb19e246482)
MERGE (person_017082007047)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_afb19e246482)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_afb19e246482)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_afb19e246482)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_afb19e246482)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_296a807f0bd8)
MERGE (person_017082007047)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_296a807f0bd8)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_296a807f0bd8)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_296a807f0bd8)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_296a807f0bd8)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_6d088d867cab)
MERGE (person_017082007047)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6d088d867cab)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_6d088d867cab)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_6d088d867cab)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_6d088d867cab)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_6e9bc9437335)
MERGE (person_017082007047)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6e9bc9437335)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_6e9bc9437335)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_6e9bc9437335)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_6e9bc9437335)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_2ade057eda06)
MERGE (person_017082007047)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2ade057eda06)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_2ade057eda06)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_2ade057eda06)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_2ade057eda06)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_baecb582ab9a)
MERGE (person_017082007047)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_baecb582ab9a)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_baecb582ab9a)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_baecb582ab9a)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_baecb582ab9a)

