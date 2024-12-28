
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_38c5ee422f75:Release{ uuid: 'a01a73ef-642e-49d3-8e1a-38c5ee422f75' })
SET release_38c5ee422f75.name = 'Love Letters'
SET release_38c5ee422f75.country = 'DE'
SET release_38c5ee422f75.date = '2003-04-22'
SET release_38c5ee422f75.format = 'CD'
SET release_38c5ee422f75.discode = '510885 2'
SET release_38c5ee422f75.musicbrainz = 'http://musicbrainz.org/release/a01a73ef-642e-49d3-8e1a-38c5ee422f75'
SET release_38c5ee422f75.source = 'musicbrainz.org'


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


MERGE (person_fe4dbff20ad2:Person{ uuid: 'cbfd7f01-87c3-44bf-a3a2-fe4dbff20ad2' }) 
SET person_fe4dbff20ad2.name = 'John Scofield'
SET person_fe4dbff20ad2.gender = 'Male'
SET person_fe4dbff20ad2.country = 'US'
SET person_fe4dbff20ad2.allmusic = 'https://www.allmusic.com/artist/mn0000677991'
SET person_fe4dbff20ad2.bbc = 'https://www.bbc.co.uk/music/artists/cbfd7f01-87c3-44bf-a3a2-fe4dbff20ad2'
SET person_fe4dbff20ad2.discogs = 'https://www.discogs.com/artist/12628'
SET person_fe4dbff20ad2.imdb = 'https://www.imdb.com/name/nm0778604/'
SET person_fe4dbff20ad2.viaf = 'http://viaf.org/viaf/84970552'
SET person_fe4dbff20ad2.wikidata = 'https://www.wikidata.org/wiki/Q357176'
SET person_fe4dbff20ad2.databases = ['http://d-nb.info/gnd/134517997', 'http://id.loc.gov/authorities/names/n78031055', 'https://catalogue.bnf.fr/ark:/12148/cb13899591h', 'http://snaccooperative.org/ark:/99166/w6b70bt7', 'https://www.musik-sammler.de/artist/john-scofield/', 'https://www.worldcat.org/identities/lccn-n78031055']
SET person_fe4dbff20ad2.musicbrainz = 'https://musicbrainz.org/artist/cbfd7f01-87c3-44bf-a3a2-fe4dbff20ad2'
SET person_fe4dbff20ad2.isni_list = ['http://isni.org/isni/0000000115117437']
SET person_fe4dbff20ad2.source = 'musicbrainz.org'


MERGE (person_e691027ebc13:Person{ uuid: '893adada-3551-4aed-aaa1-e691027ebc13' }) 
SET person_e691027ebc13.name = 'David Baker'
SET person_e691027ebc13.gender = 'Male'
SET person_e691027ebc13.disambiguation = 'American engineer and producer - jazz, funk, ...'
SET person_e691027ebc13.country = 'US'
SET person_e691027ebc13.allmusic = 'https://www.allmusic.com/artist/mn0001825990'
SET person_e691027ebc13.discogs = 'https://www.discogs.com/artist/239637'
SET person_e691027ebc13.musicbrainz = 'https://musicbrainz.org/artist/893adada-3551-4aed-aaa1-e691027ebc13'
SET person_e691027ebc13.source = 'musicbrainz.org'


MERGE (person_770ba6cf4573:Person{ uuid: 'b00a17c3-72b2-4e39-96f9-770ba6cf4573' }) 
SET person_770ba6cf4573.name = 'Joshua Redman'
SET person_770ba6cf4573.gender = 'Male'
SET person_770ba6cf4573.disambiguation = 'tenor saxophonist'
SET person_770ba6cf4573.country = 'US'
SET person_770ba6cf4573.allmusic = 'https://www.allmusic.com/artist/mn0000280434'
SET person_770ba6cf4573.bbc = 'https://www.bbc.co.uk/music/artists/b00a17c3-72b2-4e39-96f9-770ba6cf4573'
SET person_770ba6cf4573.discogs = 'https://www.discogs.com/artist/95092'
SET person_770ba6cf4573.viaf = 'http://viaf.org/viaf/67684254'
SET person_770ba6cf4573.wikidata = 'https://www.wikidata.org/wiki/Q361927'
SET person_770ba6cf4573.databases = ['http://d-nb.info/gnd/135535123', 'http://id.loc.gov/authorities/names/nr92022891', 'https://catalogue.bnf.fr/ark:/12148/cb13956232s', 'http://snaccooperative.org/ark:/99166/w6zq6j5w', 'https://rateyourmusic.com/artist/joshua_redman', 'https://www.worldcat.org/identities/lccn-nr92022891']
SET person_770ba6cf4573.musicbrainz = 'https://musicbrainz.org/artist/b00a17c3-72b2-4e39-96f9-770ba6cf4573'
SET person_770ba6cf4573.isni_list = ['http://isni.org/isni/0000000115115423']
SET person_770ba6cf4573.source = 'musicbrainz.org'


MERGE (person_4b132eb0567e:Person{ uuid: 'b7395acd-66bd-444b-93c0-4b132eb0567e' }) 
SET person_4b132eb0567e.name = '伊藤八十八'
SET person_4b132eb0567e.gender = 'Male'
SET person_4b132eb0567e.country = 'JP'
SET person_4b132eb0567e.allmusic = 'https://www.allmusic.com/artist/mn0000679885'
SET person_4b132eb0567e.discogs = 'https://www.discogs.com/artist/4031760'
SET person_4b132eb0567e.discogs = 'https://www.discogs.com/artist/406896'
SET person_4b132eb0567e.musicbrainz = 'https://musicbrainz.org/artist/b7395acd-66bd-444b-93c0-4b132eb0567e'
SET person_4b132eb0567e.source = 'musicbrainz.org'


MERGE (person_b84e43378390:Person{ uuid: '30b01f7e-2af1-4293-a52c-b84e43378390' }) 
SET person_b84e43378390.name = 'David Kikoski'
SET person_b84e43378390.gender = 'Male'
SET person_b84e43378390.country = 'US'
SET person_b84e43378390.allmusic = 'https://www.allmusic.com/artist/mn0000811141'
SET person_b84e43378390.discogs = 'https://www.discogs.com/artist/486649'
SET person_b84e43378390.viaf = 'http://viaf.org/viaf/233486283'
SET person_b84e43378390.wikidata = 'https://www.wikidata.org/wiki/Q1174978'
SET person_b84e43378390.wikipedia = 'https://en.wikipedia.org/wiki/David_Kikoski'
SET person_b84e43378390.databases = ['http://d-nb.info/gnd/134644328', 'http://id.loc.gov/authorities/names/n87142774', 'https://catalogue.bnf.fr/ark:/12148/cb139775835', 'https://www.worldcat.org/identities/lccn-n87142774']
SET person_b84e43378390.musicbrainz = 'https://musicbrainz.org/artist/30b01f7e-2af1-4293-a52c-b84e43378390'
SET person_b84e43378390.isni_list = ['http://isni.org/isni/0000000367948974']
SET person_b84e43378390.source = 'musicbrainz.org'


MERGE (person_dbad528aa58e:Person{ uuid: '7ea233ad-c340-4f62-8678-dbad528aa58e' }) 
SET person_dbad528aa58e.name = 'Dave Holland'
SET person_dbad528aa58e.gender = 'Male'
SET person_dbad528aa58e.disambiguation = 'British jazz bassist and composer'
SET person_dbad528aa58e.country = 'GB'
SET person_dbad528aa58e.allmusic = 'https://www.allmusic.com/artist/mn0000585092'
SET person_dbad528aa58e.bbc = 'https://www.bbc.co.uk/music/artists/7ea233ad-c340-4f62-8678-dbad528aa58e'
SET person_dbad528aa58e.discogs = 'https://www.discogs.com/artist/84214'
SET person_dbad528aa58e.imdb = 'https://www.imdb.com/name/nm1180224/'
SET person_dbad528aa58e.viaf = 'http://viaf.org/viaf/115064351'
SET person_dbad528aa58e.wikidata = 'https://www.wikidata.org/wiki/Q504671'
SET person_dbad528aa58e.databases = ['http://d-nb.info/gnd/134409361', 'http://id.loc.gov/authorities/names/n84163014', 'https://catalogue.bnf.fr/ark:/12148/cb13895278h', 'http://snaccooperative.org/ark:/99166/w6dn45cm', 'https://www.worldcat.org/identities/lccn-n84163014']
SET person_dbad528aa58e.musicbrainz = 'https://musicbrainz.org/artist/7ea233ad-c340-4f62-8678-dbad528aa58e'
SET person_dbad528aa58e.isni_list = ['http://isni.org/isni/0000000084120907']
SET person_dbad528aa58e.source = 'musicbrainz.org'


MERGE (person_a7572c34e806:Person{ uuid: '6035000d-b53b-4b01-b5a0-a7572c34e806' }) 
SET person_a7572c34e806.name = 'Christian McBride'
SET person_a7572c34e806.gender = 'Male'
SET person_a7572c34e806.disambiguation = 'American jazz bassist'
SET person_a7572c34e806.country = 'US'
SET person_a7572c34e806.allmusic = 'https://www.allmusic.com/artist/mn0000103600'
SET person_a7572c34e806.discogs = 'https://www.discogs.com/artist/44565'
SET person_a7572c34e806.viaf = 'http://viaf.org/viaf/85464720'
SET person_a7572c34e806.wikidata = 'https://www.wikidata.org/wiki/Q732319'
SET person_a7572c34e806.databases = ['http://d-nb.info/gnd/134732650', 'http://id.loc.gov/authorities/names/n92023967', 'https://catalogue.bnf.fr/ark:/12148/cb139401069', 'https://www.worldcat.org/identities/lccn-n92023967']
SET person_a7572c34e806.musicbrainz = 'https://musicbrainz.org/artist/6035000d-b53b-4b01-b5a0-a7572c34e806'
SET person_a7572c34e806.isni_list = ['http://isni.org/isni/0000000114765651']
SET person_a7572c34e806.source = 'musicbrainz.org'


MERGE (person_120e386da267:Person{ uuid: '6b2e6e7c-4289-447c-a3dc-120e386da267' }) 
SET person_120e386da267.name = 'Kenny Barron'
SET person_120e386da267.gender = 'Male'
SET person_120e386da267.country = 'US'
SET person_120e386da267.allmusic = 'https://www.allmusic.com/artist/mn0000081181'
SET person_120e386da267.discogs = 'https://www.discogs.com/artist/65746'
SET person_120e386da267.imdb = 'https://www.imdb.com/name/nm0057686/'
SET person_120e386da267.viaf = 'http://viaf.org/viaf/119903038'
SET person_120e386da267.wikidata = 'https://www.wikidata.org/wiki/Q489233'
SET person_120e386da267.databases = ['http://d-nb.info/gnd/134321804', 'http://id.loc.gov/authorities/names/n80124274', 'https://catalogue.bnf.fr/ark:/12148/cb13891186w', 'http://snaccooperative.org/ark:/99166/w6c5871b', 'https://rateyourmusic.com/artist/kenny_barron', 'https://www.musik-sammler.de/artist/kenny-barron/', 'https://www.worldcat.org/identities/lccn-n80124274']
SET person_120e386da267.musicbrainz = 'https://musicbrainz.org/artist/6b2e6e7c-4289-447c-a3dc-120e386da267'
SET person_120e386da267.isni_list = ['http://isni.org/isni/0000000081889024']
SET person_120e386da267.source = 'musicbrainz.org'

// labels

MERGE (label_0400dd45693e:Label{ uuid: '011d1192-6f65-45bd-85c4-0400dd45693e' })
SET label_0400dd45693e.name= 'Columbia'

// performances

MERGE (perf_44d30364913e:Performance{ uuid: '2755b667-4607-4c32-aba9-44d30364913e' })
SET perf_44d30364913e.name = 'The Best Thing For You'
SET perf_44d30364913e.duration = '3:47'
SET perf_44d30364913e.begin_date = '2002-05-23'
SET perf_44d30364913e.end_date = '2002-05-24'
SET perf_44d30364913e.source = 'musicbrainz.org'


MERGE (perf_a0d5f0a50fab:Performance{ uuid: '45b200b8-6956-40f5-a3ce-a0d5f0a50fab' })
SET perf_a0d5f0a50fab.name = 'That Old Feeling'
SET perf_a0d5f0a50fab.duration = '6:28'
SET perf_a0d5f0a50fab.begin_date = '2002-05-23'
SET perf_a0d5f0a50fab.end_date = '2002-05-24'
SET perf_a0d5f0a50fab.source = 'musicbrainz.org'


MERGE (perf_d450d50e0f1d:Performance{ uuid: '650af645-6930-4982-a981-d450d50e0f1d' })
SET perf_d450d50e0f1d.name = 'Afro Blue'
SET perf_d450d50e0f1d.duration = '7:15'
SET perf_d450d50e0f1d.begin_date = '2002-05-23'
SET perf_d450d50e0f1d.end_date = '2002-05-24'
SET perf_d450d50e0f1d.source = 'musicbrainz.org'


MERGE (perf_8d3f63b8f928:Performance{ uuid: '15375eaf-cf88-453e-b287-8d3f63b8f928' })
SET perf_8d3f63b8f928.name = 'Qué Pasa'
SET perf_8d3f63b8f928.duration = '7:31'
SET perf_8d3f63b8f928.begin_date = '2002-05-23'
SET perf_8d3f63b8f928.end_date = '2002-05-24'
SET perf_8d3f63b8f928.source = 'musicbrainz.org'


MERGE (perf_2fc72540fb4c:Performance{ uuid: '6f94fcec-1fe7-4641-bf05-2fc72540fb4c' })
SET perf_2fc72540fb4c.name = 'How Deep Is the Ocean?'
SET perf_2fc72540fb4c.duration = '6:33'
SET perf_2fc72540fb4c.begin_date = '2002-05-23'
SET perf_2fc72540fb4c.end_date = '2002-05-24'
SET perf_2fc72540fb4c.source = 'musicbrainz.org'


MERGE (perf_96f9537748a5:Performance{ uuid: 'b8cc133f-3dfa-460f-8506-96f9537748a5' })
SET perf_96f9537748a5.name = 'Love Letters'
SET perf_96f9537748a5.duration = '7:42'
SET perf_96f9537748a5.begin_date = '2002-05-23'
SET perf_96f9537748a5.end_date = '2002-05-24'
SET perf_96f9537748a5.source = 'musicbrainz.org'


MERGE (perf_c910cfa5d309:Performance{ uuid: 'f4c88776-f8a4-4277-b565-c910cfa5d309' })
SET perf_c910cfa5d309.name = 'My Shining Hour'
SET perf_c910cfa5d309.duration = '5:46'
SET perf_c910cfa5d309.begin_date = '2002-05-23'
SET perf_c910cfa5d309.end_date = '2002-05-24'
SET perf_c910cfa5d309.source = 'musicbrainz.org'


MERGE (perf_33c003013c39:Performance{ uuid: 'ae9971cb-db31-4c03-aba9-33c003013c39' })
SET perf_33c003013c39.name = 'Stompin\\' at the Savoy'
SET perf_33c003013c39.duration = '7:13'
SET perf_33c003013c39.begin_date = '2002-05-23'
SET perf_33c003013c39.end_date = '2002-05-24'
SET perf_33c003013c39.source = 'musicbrainz.org'


MERGE (perf_5b7a5bbfe18b:Performance{ uuid: '2134b2b0-6855-4a53-b60a-5b7a5bbfe18b' })
SET perf_5b7a5bbfe18b.name = 'Shades Of Senegal 2'
SET perf_5b7a5bbfe18b.duration = '4:18'
SET perf_5b7a5bbfe18b.begin_date = '2002-05-23'
SET perf_5b7a5bbfe18b.end_date = '2002-05-24'
SET perf_5b7a5bbfe18b.source = 'musicbrainz.org'




// labels
MERGE (release_38c5ee422f75)-[:HAS_LABEL]->(label_0400dd45693e)


// tracks
MERGE (release_38c5ee422f75)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_44d30364913e)
MERGE (release_38c5ee422f75)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_a0d5f0a50fab)
MERGE (release_38c5ee422f75)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_d450d50e0f1d)
MERGE (release_38c5ee422f75)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_8d3f63b8f928)
MERGE (release_38c5ee422f75)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_2fc72540fb4c)
MERGE (release_38c5ee422f75)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_96f9537748a5)
MERGE (release_38c5ee422f75)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_c910cfa5d309)
MERGE (release_38c5ee422f75)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_33c003013c39)
MERGE (release_38c5ee422f75)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_5b7a5bbfe18b)

// works

MERGE (person_9ab6e2c50af6:Person{ uuid: '915f84de-eac2-4e78-99ad-9ab6e2c50af6' }) 
SET person_9ab6e2c50af6.name = 'Mongo Santamaría'
SET person_9ab6e2c50af6.gender = 'Male'
SET person_9ab6e2c50af6.disambiguation = 'Cuban jazz percussionist'
SET person_9ab6e2c50af6.country = 'CU'
SET person_9ab6e2c50af6.allmusic = 'https://www.allmusic.com/artist/mn0000591104'
SET person_9ab6e2c50af6.discogs = 'https://www.discogs.com/artist/79342'
SET person_9ab6e2c50af6.viaf = 'http://viaf.org/viaf/49409306'
SET person_9ab6e2c50af6.wikidata = 'https://www.wikidata.org/wiki/Q472644'
SET person_9ab6e2c50af6.databases = ['http://d-nb.info/gnd/134576047', 'http://id.loc.gov/authorities/names/n83189403', 'https://catalogue.bnf.fr/ark:/12148/cb13899391z', 'http://snaccooperative.org/ark:/99166/w63r27v6', 'https://rateyourmusic.com/artist/mongo_santamaria', 'https://www.musik-sammler.de/artist/mongo-santamaria/', 'https://www.worldcat.org/identities/lccn-n83189403']
SET person_9ab6e2c50af6.musicbrainz = 'https://musicbrainz.org/artist/915f84de-eac2-4e78-99ad-9ab6e2c50af6'
SET person_9ab6e2c50af6.isni_list = ['http://isni.org/isni/0000000108993834']
SET person_9ab6e2c50af6.source = 'musicbrainz.org'


MERGE (person_8c848a4765b6:Person{ uuid: 'd185d986-ee96-4fd3-bd61-8c848a4765b6' }) 
SET person_8c848a4765b6.name = 'Horace Silver'
SET person_8c848a4765b6.gender = 'Male'
SET person_8c848a4765b6.country = 'US'
SET person_8c848a4765b6.allmusic = 'https://www.allmusic.com/artist/mn0000267354'
SET person_8c848a4765b6.discogs = 'https://www.discogs.com/artist/29973'
SET person_8c848a4765b6.imdb = 'https://www.imdb.com/name/nm0798701/'
SET person_8c848a4765b6.viaf = 'http://viaf.org/viaf/8537804'
SET person_8c848a4765b6.wikidata = 'https://www.wikidata.org/wiki/Q365560'
SET person_8c848a4765b6.databases = ['http://d-nb.info/gnd/132099594', 'http://id.loc.gov/authorities/names/n82003124', 'https://catalogue.bnf.fr/ark:/12148/cb13899777h', 'http://snaccooperative.org/ark:/99166/w6p015gr', 'https://rateyourmusic.com/artist/horace_silver', 'https://www.musik-sammler.de/artist/horace-silver/', 'https://www.worldcat.org/identities/lccn-n82003124']
SET person_8c848a4765b6.musicbrainz = 'https://musicbrainz.org/artist/d185d986-ee96-4fd3-bd61-8c848a4765b6'
SET person_8c848a4765b6.isni_list = ['http://isni.org/isni/0000000108681996']
SET person_8c848a4765b6.source = 'musicbrainz.org'


MERGE (person_e8714dc021fd:Person{ uuid: '19cd620e-3fcf-4081-b5f4-e8714dc021fd' }) 
SET person_e8714dc021fd.name = 'Sammy Fain'
SET person_e8714dc021fd.gender = 'Male'
SET person_e8714dc021fd.country = 'US'
SET person_e8714dc021fd.allmusic = 'https://www.allmusic.com/artist/mn0000944872'
SET person_e8714dc021fd.discogs = 'https://www.discogs.com/artist/290093'
SET person_e8714dc021fd.imdb = 'https://www.imdb.com/name/nm0006066/'
SET person_e8714dc021fd.viaf = 'http://viaf.org/viaf/79169379'
SET person_e8714dc021fd.wikidata = 'https://www.wikidata.org/wiki/Q742896'
SET person_e8714dc021fd.databases = ['http://d-nb.info/gnd/103837175', 'http://id.loc.gov/authorities/names/n93022038', 'https://catalogue.bnf.fr/ark:/12148/cb13940014n', 'https://ibdb.com/person.php?id=11649', 'http://snaccooperative.org/ark:/99166/w6x92n72', 'https://nla.gov.au/nla.party-1144384', 'https://rateyourmusic.com/artist/sammy_fain', 'https://www.worldcat.org/identities/lccn-n93022038/']
SET person_e8714dc021fd.musicbrainz = 'https://musicbrainz.org/artist/19cd620e-3fcf-4081-b5f4-e8714dc021fd'
SET person_e8714dc021fd.isni_list = ['http://isni.org/isni/0000000114756683']
SET person_e8714dc021fd.source = 'musicbrainz.org'


MERGE (person_eb9dc9f506b5:Person{ uuid: '5e645519-a175-4fe0-9a9b-eb9dc9f506b5' }) 
SET person_eb9dc9f506b5.name = 'Irving Berlin'
SET person_eb9dc9f506b5.gender = 'Male'
SET person_eb9dc9f506b5.country = 'US'
SET person_eb9dc9f506b5.allmusic = 'https://www.allmusic.com/artist/mn0000103748'
SET person_eb9dc9f506b5.bbc = 'https://www.bbc.co.uk/music/artists/5e645519-a175-4fe0-9a9b-eb9dc9f506b5'
SET person_eb9dc9f506b5.discogs = 'https://www.discogs.com/artist/508131'
SET person_eb9dc9f506b5.imdb = 'https://www.imdb.com/name/nm0000927/'
SET person_eb9dc9f506b5.viaf = 'http://viaf.org/viaf/19864566'
SET person_eb9dc9f506b5.wikidata = 'https://www.wikidata.org/wiki/Q128746'
SET person_eb9dc9f506b5.databases = ['http://d-nb.info/gnd/118850776', 'http://id.loc.gov/authorities/names/n50026116', 'https://catalogue.bnf.fr/ark:/12148/cb13891411t', 'https://ibdb.com/person.php?id=6452', 'http://snaccooperative.org/ark:/99166/w6sg3n6g', 'https://nla.gov.au/nla.party-1286386', 'https://openlibrary.org/works/OL1429622A', 'https://rateyourmusic.com/artist/irving_berlin', 'https://www.worldcat.org/identities/lccn-n50026116/', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Irving&last=Berlin&middle=']
SET person_eb9dc9f506b5.musicbrainz = 'https://musicbrainz.org/artist/5e645519-a175-4fe0-9a9b-eb9dc9f506b5'
SET person_eb9dc9f506b5.isni_list = ['http://isni.org/isni/0000000108769971']
SET person_eb9dc9f506b5.source = 'musicbrainz.org'


MERGE (person_91000e35bc46:Person{ uuid: '8ba56dd4-a9e1-410f-9b1e-91000e35bc46' }) 
SET person_91000e35bc46.name = 'Edward Heyman'
SET person_91000e35bc46.gender = 'Male'
SET person_91000e35bc46.country = 'US'
SET person_91000e35bc46.allmusic = 'https://www.allmusic.com/artist/mn0000795422'
SET person_91000e35bc46.discogs = 'https://www.discogs.com/artist/607246'
SET person_91000e35bc46.imdb = 'https://www.imdb.com/name/nm0382269/'
SET person_91000e35bc46.viaf = 'http://viaf.org/viaf/118204894'
SET person_91000e35bc46.wikidata = 'https://www.wikidata.org/wiki/Q4355574'
SET person_91000e35bc46.databases = ['http://d-nb.info/gnd/139673237', 'http://id.loc.gov/authorities/names/n86140056', 'https://catalogue.bnf.fr/ark:/12148/cb14838432c', 'http://snaccooperative.org/ark:/99166/w6m91467', 'https://nla.gov.au/nla.party-844812', 'https://rateyourmusic.com/artist/edward_heyman', 'https://www.ibdb.com/person.php?id=11852', 'https://www.worldcat.org/identities/lccn-n86140056/']
SET person_91000e35bc46.musicbrainz = 'https://musicbrainz.org/artist/8ba56dd4-a9e1-410f-9b1e-91000e35bc46'
SET person_91000e35bc46.isni_list = ['http://isni.org/isni/000000012148820X']
SET person_91000e35bc46.source = 'musicbrainz.org'


MERGE (person_376736bb6cde:Person{ uuid: '3508f3fd-3b18-493c-a362-376736bb6cde' }) 
SET person_376736bb6cde.name = 'Harold Arlen'
SET person_376736bb6cde.gender = 'Male'
SET person_376736bb6cde.country = 'US'
SET person_376736bb6cde.allmusic = 'https://www.allmusic.com/artist/mn0000060306'
SET person_376736bb6cde.discogs = 'https://www.discogs.com/artist/301975'
SET person_376736bb6cde.imdb = 'https://www.imdb.com/name/nm0002182/'
SET person_376736bb6cde.viaf = 'http://viaf.org/viaf/59268723'
SET person_376736bb6cde.wikidata = 'https://www.wikidata.org/wiki/Q448644'
SET person_376736bb6cde.databases = ['http://d-nb.info/gnd/119401193', 'http://id.loc.gov/authorities/names/n82155108', 'https://catalogue.bnf.fr/ark:/12148/cb13890872w', 'https://ibdb.com/person.php?id=11319', 'https://id.ndl.go.jp/auth/ndlna/001155326', 'http://snaccooperative.org/ark:/99166/w6z899sq', 'https://nla.gov.au/anbd.aut-an35107300', 'https://openlibrary.org/works/OL342313A', 'https://rateyourmusic.com/artist/harold_arlen', 'https://www.worldcat.org/identities/containsVIAFID/59268723']
SET person_376736bb6cde.musicbrainz = 'https://musicbrainz.org/artist/3508f3fd-3b18-493c-a362-376736bb6cde'
SET person_376736bb6cde.isni_list = ['http://isni.org/isni/0000000083863098', 'http://isni.org/isni/0000000368517543']
SET person_376736bb6cde.source = 'musicbrainz.org'


MERGE (person_ac11abc26771:Person{ uuid: '8ecae52e-9c89-4b61-99d8-ac11abc26771' }) 
SET person_ac11abc26771.name = 'Chick Webb'
SET person_ac11abc26771.gender = 'Male'
SET person_ac11abc26771.country = 'US'
SET person_ac11abc26771.allmusic = 'https://www.allmusic.com/artist/mn0000110604'
SET person_ac11abc26771.discogs = 'https://www.discogs.com/artist/294491'
SET person_ac11abc26771.imdb = 'https://www.imdb.com/name/nm1352264/'
SET person_ac11abc26771.viaf = 'http://viaf.org/viaf/198704'
SET person_ac11abc26771.wikidata = 'https://www.wikidata.org/wiki/Q505749'
SET person_ac11abc26771.wikipedia = 'https://en.wikipedia.org/wiki/Chick_Webb'
SET person_ac11abc26771.databases = ['http://d-nb.info/gnd/123318246', 'http://id.loc.gov/authorities/names/n84007220', 'https://catalogue.bnf.fr/ark:/12148/cb139259754', 'https://ibdb.com/person.php?id=83877', 'http://snaccooperative.org/ark:/99166/w6d53z00', 'https://www.worldcat.org/identities/lccn-n84007220']
SET person_ac11abc26771.musicbrainz = 'https://musicbrainz.org/artist/8ecae52e-9c89-4b61-99d8-ac11abc26771'
SET person_ac11abc26771.isni_list = ['http://isni.org/isni/0000000080795990']
SET person_ac11abc26771.source = 'musicbrainz.org'


MERGE (person_f285898a455b:Person{ uuid: '4d8cacfc-145e-42db-b779-f285898a455b' }) 
SET person_f285898a455b.name = 'Lew Brown'
SET person_f285898a455b.gender = 'Male'
SET person_f285898a455b.country = 'US'
SET person_f285898a455b.allmusic = 'https://www.allmusic.com/artist/mn0000217246'
SET person_f285898a455b.discogs = 'https://www.discogs.com/artist/690853'
SET person_f285898a455b.imdb = 'https://www.imdb.com/name/nm0114095/'
SET person_f285898a455b.viaf = 'http://viaf.org/viaf/32264521'
SET person_f285898a455b.wikidata = 'https://www.wikidata.org/wiki/Q4096110'
SET person_f285898a455b.databases = ['http://d-nb.info/gnd/1117735591', 'http://id.loc.gov/authorities/names/no90010584', 'https://catalogue.bnf.fr/ark:/12148/cb148427757', 'http://snaccooperative.org/ark:/99166/w6pw4b5w', 'https://nla.gov.au/nla.party-1167685', 'https://www.ibdb.com/person.php?id=7310', 'https://www.worldcat.org/identities/lccn-no90010584/']
SET person_f285898a455b.musicbrainz = 'https://musicbrainz.org/artist/4d8cacfc-145e-42db-b779-f285898a455b'
SET person_f285898a455b.isni_list = ['http://isni.org/isni/0000000073574911']
SET person_f285898a455b.source = 'musicbrainz.org'


MERGE (person_0cdf22c48565:Person{ uuid: '338f9d5d-9327-4f01-bb99-0cdf22c48565' }) 
SET person_0cdf22c48565.name = 'Victor Young'
SET person_0cdf22c48565.gender = 'Male'
SET person_0cdf22c48565.disambiguation = 'American composer, arranger, violinist & conductor'
SET person_0cdf22c48565.country = 'US'
SET person_0cdf22c48565.allmusic = 'https://www.allmusic.com/artist/mn0000959775'
SET person_0cdf22c48565.discogs = 'https://www.discogs.com/artist/370725'
SET person_0cdf22c48565.imdb = 'https://www.imdb.com/name/nm0000082/'
SET person_0cdf22c48565.viaf = 'http://viaf.org/viaf/100232829'
SET person_0cdf22c48565.wikidata = 'https://www.wikidata.org/wiki/Q365199'
SET person_0cdf22c48565.databases = ['http://d-nb.info/gnd/133160297', 'http://id.loc.gov/authorities/names/n87911854', 'https://catalogue.bnf.fr/ark:/12148/cb139013544', 'https://ibdb.com/person.php?id=12609', 'http://snaccooperative.org/ark:/99166/w6862fdw', 'https://nla.gov.au/nla.party-1140987', 'https://openlibrary.org/works/OL7177117A', 'http://soundtrackcollector.com/composer/47/', 'https://rateyourmusic.com/artist/victor_young', 'https://www.worldcat.org/identities/lccn-n87911854/', 'http://www.45worlds.com/78rpm/artist/victor-young']
SET person_0cdf22c48565.musicbrainz = 'https://musicbrainz.org/artist/338f9d5d-9327-4f01-bb99-0cdf22c48565'
SET person_0cdf22c48565.isni_list = ['http://isni.org/isni/0000000116917487']
SET person_0cdf22c48565.source = 'musicbrainz.org'


MERGE (person_2b3e7beaf00a:Person{ uuid: 'b342d50e-401c-4c77-b7e4-2b3e7beaf00a' }) 
SET person_2b3e7beaf00a.name = 'Johnny Mercer'
SET person_2b3e7beaf00a.gender = 'Male'
SET person_2b3e7beaf00a.country = 'US'
SET person_2b3e7beaf00a.allmusic = 'https://www.allmusic.com/artist/mn0000244406'
SET person_2b3e7beaf00a.bbc = 'https://www.bbc.co.uk/music/artists/b342d50e-401c-4c77-b7e4-2b3e7beaf00a'
SET person_2b3e7beaf00a.discogs = 'https://www.discogs.com/artist/164574'
SET person_2b3e7beaf00a.imdb = 'https://www.imdb.com/name/nm0006197/'
SET person_2b3e7beaf00a.viaf = 'http://viaf.org/viaf/79167222'
SET person_2b3e7beaf00a.wikidata = 'https://www.wikidata.org/wiki/Q363698'
SET person_2b3e7beaf00a.databases = ['http://d-nb.info/gnd/118801031', 'http://id.loc.gov/authorities/names/n82078485', 'https://catalogue.bnf.fr/ark:/12148/cb138974071', 'http://snaccooperative.org/ark:/99166/w65140xb', 'https://nla.gov.au/nla.party-1213050', 'http://soundtrackcollector.com/composer/3036/', 'https://rateyourmusic.com/artist/johnny_mercer', 'https://www.ibdb.com/person.php?id=12137', 'https://www.worldcat.org/identities/lccn-n82078485/']
SET person_2b3e7beaf00a.musicbrainz = 'https://musicbrainz.org/artist/b342d50e-401c-4c77-b7e4-2b3e7beaf00a'
SET person_2b3e7beaf00a.isni_list = ['http://isni.org/isni/0000000120183877']
SET person_2b3e7beaf00a.source = 'musicbrainz.org'


MERGE (person_cb1a4cebdccc:Person{ uuid: '2d7bd2fd-c6c2-49be-9200-cb1a4cebdccc' }) 
SET person_cb1a4cebdccc.name = 'Andy Razaf'
SET person_cb1a4cebdccc.gender = 'Male'
SET person_cb1a4cebdccc.country = 'US'
SET person_cb1a4cebdccc.discogs = 'https://www.discogs.com/artist/301998'
SET person_cb1a4cebdccc.imdb = 'https://www.imdb.com/name/nm0713596/'
SET person_cb1a4cebdccc.viaf = 'http://viaf.org/viaf/66657738'
SET person_cb1a4cebdccc.wikidata = 'https://www.wikidata.org/wiki/Q117741'
SET person_cb1a4cebdccc.databases = ['http://d-nb.info/gnd/119151642', 'http://id.loc.gov/authorities/names/n87121589', 'https://catalogue.bnf.fr/ark:/12148/cb139586718', 'http://snaccooperative.org/ark:/99166/w6x92bsh', 'https://nla.gov.au/nla.party-1506542', 'https://www.ibdb.com/person.php?id=4135', 'https://www.worldcat.org/identities/lccn-n87121589/']
SET person_cb1a4cebdccc.musicbrainz = 'https://musicbrainz.org/artist/2d7bd2fd-c6c2-49be-9200-cb1a4cebdccc'
SET person_cb1a4cebdccc.isni_list = ['http://isni.org/isni/0000000081465627']
SET person_cb1a4cebdccc.source = 'musicbrainz.org'


MERGE (person_1cacb5e1632e:Person{ uuid: 'b09ae88f-4156-4caa-b129-1cacb5e1632e' }) 
SET person_1cacb5e1632e.name = 'Benny Goodman'
SET person_1cacb5e1632e.gender = 'Male'
SET person_1cacb5e1632e.disambiguation = 'clarinetist and bandleader'
SET person_1cacb5e1632e.country = 'US'
SET person_1cacb5e1632e.allmusic = 'https://www.allmusic.com/artist/mn0000163133'
SET person_1cacb5e1632e.bbc = 'https://www.bbc.co.uk/music/artists/b09ae88f-4156-4caa-b129-1cacb5e1632e'
SET person_1cacb5e1632e.discogs = 'https://www.discogs.com/artist/254768'
SET person_1cacb5e1632e.imdb = 'https://www.imdb.com/name/nm0329015/'
SET person_1cacb5e1632e.viaf = 'http://viaf.org/viaf/7573997'
SET person_1cacb5e1632e.wikidata = 'https://www.wikidata.org/wiki/Q46755'
SET person_1cacb5e1632e.databases = ['http://d-nb.info/gnd/118696424', 'http://id.loc.gov/authorities/names/n81139256', 'https://catalogue.bnf.fr/ark:/12148/cb13894604t', 'https://ibdb.com/person.php?id=11766', 'http://snaccooperative.org/ark:/99166/w6xp73km', 'https://nla.gov.au/nla.party-450056', 'https://openlibrary.org/works/OL1069190A', 'https://rateyourmusic.com/artist/benny_goodman', 'https://www.worldcat.org/identities/lccn-n81139256']
SET person_1cacb5e1632e.musicbrainz = 'https://musicbrainz.org/artist/b09ae88f-4156-4caa-b129-1cacb5e1632e'
SET person_1cacb5e1632e.isni_list = ['http://isni.org/isni/0000000123197959']
SET person_1cacb5e1632e.source = 'musicbrainz.org'


MERGE (person_eb7212752719:Person{ uuid: '79842485-d513-4057-a55f-eb7212752719' }) 
SET person_eb7212752719.name = 'Edgar Sampson'
SET person_eb7212752719.gender = 'Male'
SET person_eb7212752719.country = 'US'
SET person_eb7212752719.allmusic = 'https://www.allmusic.com/artist/mn0000181398'
SET person_eb7212752719.discogs = 'https://www.discogs.com/artist/307404'
SET person_eb7212752719.viaf = 'http://viaf.org/viaf/27253069'
SET person_eb7212752719.wikidata = 'https://www.wikidata.org/wiki/Q347078'
SET person_eb7212752719.databases = ['http://d-nb.info/gnd/135029465', 'http://id.loc.gov/authorities/names/n95057734', 'https://catalogue.bnf.fr/ark:/12148/cb138993642', 'https://ibdb.com/person.php?id=83878', 'http://snaccooperative.org/ark:/99166/w6k653nt', 'https://nla.gov.au/nla.party-1532787', 'https://www.worldcat.org/identities/lccn-n95057734']
SET person_eb7212752719.musicbrainz = 'https://musicbrainz.org/artist/79842485-d513-4057-a55f-eb7212752719'
SET person_eb7212752719.isni_list = ['http://isni.org/isni/0000000094557643']
SET person_eb7212752719.source = 'musicbrainz.org'


MERGE (work_01da3aea65da:Work{ uuid: '4c6f9ac1-7a0b-375c-aed7-01da3aea65da' })
SET work_01da3aea65da.name = 'The Best Thing for You (Would Be Me)'
SET work_01da3aea65da.iswc = 'T-070.011.025-3'
SET work_01da3aea65da.type = 'Song'
SET work_01da3aea65da.wikidata = 'https://www.wikidata.org/wiki/Q7716826'
SET work_01da3aea65da.musicbrainz = 'https://musicbrainz.org/work/4c6f9ac1-7a0b-375c-aed7-01da3aea65da'
SET work_01da3aea65da.source = 'musicbrainz.org'


MERGE (work_cb427891e0cd:Work{ uuid: '5757fff7-068f-3328-8eb0-cb427891e0cd' })
SET work_cb427891e0cd.name = 'How Deep Is the Ocean?'
SET work_cb427891e0cd.iswc = 'T-070.074.569-2'
SET work_cb427891e0cd.type = 'Song'
SET work_cb427891e0cd.wikidata = 'https://www.wikidata.org/wiki/Q4352749'
SET work_cb427891e0cd.musicbrainz = 'https://musicbrainz.org/work/5757fff7-068f-3328-8eb0-cb427891e0cd'
SET work_cb427891e0cd.source = 'musicbrainz.org'


MERGE (work_eb65b2b4552d:Work{ uuid: 'f282be5d-3b27-3f85-b971-eb65b2b4552d' })
SET work_eb65b2b4552d.name = 'That Old Feeling'
SET work_eb65b2b4552d.iswc = 'T-070.178.692-6'
SET work_eb65b2b4552d.type = 'Song'
SET work_eb65b2b4552d.tags = ['pop', 'r&b']
SET work_eb65b2b4552d.wikidata = 'https://www.wikidata.org/wiki/Q7711251'
SET work_eb65b2b4552d.musicbrainz = 'https://musicbrainz.org/work/f282be5d-3b27-3f85-b971-eb65b2b4552d'
SET work_eb65b2b4552d.source = 'musicbrainz.org'


MERGE (work_9eac816a7d66:Work{ uuid: 'c9740ef0-62c7-3b69-9a83-9eac816a7d66' })
SET work_9eac816a7d66.name = 'Afro Blue'
SET work_9eac816a7d66.type = 'Song'
SET work_9eac816a7d66.wikipedia = 'https://en.wikipedia.org/wiki/Afro_Blue'
SET work_9eac816a7d66.musicbrainz = 'https://musicbrainz.org/work/c9740ef0-62c7-3b69-9a83-9eac816a7d66'
SET work_9eac816a7d66.source = 'musicbrainz.org'


MERGE (work_eae069a2075c:Work{ uuid: '98d6dbeb-8672-39ef-a10f-eae069a2075c' })
SET work_eae069a2075c.name = 'Stompin’ at the Savoy'
SET work_eae069a2075c.iswc = 'T-911.816.271-3'
SET work_eae069a2075c.type = 'Song'
SET work_eae069a2075c.wikidata = 'https://www.wikidata.org/wiki/Q7618804'
SET work_eae069a2075c.musicbrainz = 'https://musicbrainz.org/work/98d6dbeb-8672-39ef-a10f-eae069a2075c'
SET work_eae069a2075c.source = 'musicbrainz.org'


MERGE (work_d6873c05519f:Work{ uuid: '1a8713eb-e554-31e6-a839-d6873c05519f' })
SET work_d6873c05519f.name = 'Que Pasa?'
SET work_d6873c05519f.iswc = 'T-901.297.458-2'
SET work_d6873c05519f.type = 'Song'
SET work_d6873c05519f.source = 'musicbrainz.org'


MERGE (work_4e014a8daa19:Work{ uuid: '81a1fc19-f05f-35cd-a621-4e014a8daa19' })
SET work_4e014a8daa19.name = 'My Shining Hour'
SET work_4e014a8daa19.iswc = 'T-070.111.362-3'
SET work_4e014a8daa19.type = 'Song'
SET work_4e014a8daa19.wikidata = 'https://www.wikidata.org/wiki/Q6946371'
SET work_4e014a8daa19.musicbrainz = 'https://musicbrainz.org/work/81a1fc19-f05f-35cd-a621-4e014a8daa19'
SET work_4e014a8daa19.source = 'musicbrainz.org'


MERGE (work_52f958d826fd:Work{ uuid: 'ba83bc4d-d41e-390a-848a-52f958d826fd' })
SET work_52f958d826fd.name = 'Love Letters'
SET work_52f958d826fd.iswc = 'T-070.097.372-3'
SET work_52f958d826fd.type = 'Song'
SET work_52f958d826fd.wikidata = 'https://www.wikidata.org/wiki/Q2687406'
SET work_52f958d826fd.wikipedia = 'https://en.wikipedia.org/wiki/Love_Letters_(song)'
SET work_52f958d826fd.musicbrainz = 'https://musicbrainz.org/work/ba83bc4d-d41e-390a-848a-52f958d826fd'
SET work_52f958d826fd.source = 'musicbrainz.org'



// performances of
MERGE (perf_44d30364913e)-[:PERFORMANCE_OF]->(work_01da3aea65da)
MERGE (perf_2fc72540fb4c)-[:PERFORMANCE_OF]->(work_cb427891e0cd)
MERGE (perf_a0d5f0a50fab)-[:PERFORMANCE_OF]->(work_eb65b2b4552d)
MERGE (perf_d450d50e0f1d)-[:PERFORMANCE_OF]->(work_9eac816a7d66)
MERGE (perf_33c003013c39)-[:PERFORMANCE_OF]->(work_eae069a2075c)
MERGE (perf_8d3f63b8f928)-[:PERFORMANCE_OF]->(work_d6873c05519f)
MERGE (perf_c910cfa5d309)-[:PERFORMANCE_OF]->(work_4e014a8daa19)
MERGE (perf_96f9537748a5)-[:PERFORMANCE_OF]->(work_52f958d826fd)


// composers
MERGE (person_eb9dc9f506b5)-[:COMPOSED]->(work_01da3aea65da)
MERGE (person_eb9dc9f506b5)-[:WROTE_LYRICS]->(work_01da3aea65da)
MERGE (person_eb9dc9f506b5)-[:COMPOSED]->(work_cb427891e0cd)
MERGE (person_eb9dc9f506b5)-[:WROTE_LYRICS]->(work_cb427891e0cd)
MERGE (person_e8714dc021fd)-[:COMPOSED]->(work_eb65b2b4552d)
MERGE (person_f285898a455b)-[:WROTE_LYRICS]->(work_eb65b2b4552d)
MERGE (person_9ab6e2c50af6)-[:COMPOSED]->(work_9eac816a7d66)
MERGE (person_1cacb5e1632e)-[:COMPOSED]->(work_eae069a2075c)
MERGE (person_eb7212752719)-[:COMPOSED]->(work_eae069a2075c)
MERGE (person_ac11abc26771)-[:COMPOSED]->(work_eae069a2075c)
MERGE (person_cb1a4cebdccc)-[:WROTE_LYRICS]->(work_eae069a2075c)
MERGE (person_8c848a4765b6)-[:COMPOSED]->(work_d6873c05519f)
MERGE (person_376736bb6cde)-[:COMPOSED]->(work_4e014a8daa19)
MERGE (person_2b3e7beaf00a)-[:WROTE_LYRICS]->(work_4e014a8daa19)
MERGE (person_0cdf22c48565)-[:COMPOSED]->(work_52f958d826fd)
MERGE (person_91000e35bc46)-[:WROTE_LYRICS]->(work_52f958d826fd)


// place nodes

MERGE (place_4744282c857d:Place{ uuid: 'fc12e55a-8ca7-49c2-8427-4744282c857d' })
SET place_4744282c857d.name = 'Avatar Studios'
SET place_4744282c857d.source = 'musicbrainz.org'


// place relationships
MERGE (perf_44d30364913e)-[:HAS_PLACE { type: 'recorded at', begin_date: '2002-05-23', end_date: '2002-05-24' }]->(place_4744282c857d)
MERGE (perf_a0d5f0a50fab)-[:HAS_PLACE { type: 'recorded at', begin_date: '2002-05-23', end_date: '2002-05-24' }]->(place_4744282c857d)
MERGE (perf_d450d50e0f1d)-[:HAS_PLACE { type: 'recorded at', begin_date: '2002-05-23', end_date: '2002-05-24' }]->(place_4744282c857d)
MERGE (perf_8d3f63b8f928)-[:HAS_PLACE { type: 'recorded at', begin_date: '2002-05-23', end_date: '2002-05-24' }]->(place_4744282c857d)
MERGE (perf_2fc72540fb4c)-[:HAS_PLACE { type: 'recorded at', begin_date: '2002-05-23', end_date: '2002-05-24' }]->(place_4744282c857d)
MERGE (perf_96f9537748a5)-[:HAS_PLACE { type: 'recorded at', begin_date: '2002-05-23', end_date: '2002-05-24' }]->(place_4744282c857d)
MERGE (perf_c910cfa5d309)-[:HAS_PLACE { type: 'recorded at', begin_date: '2002-05-23', end_date: '2002-05-24' }]->(place_4744282c857d)
MERGE (perf_33c003013c39)-[:HAS_PLACE { type: 'recorded at', begin_date: '2002-05-23', end_date: '2002-05-24' }]->(place_4744282c857d)
MERGE (perf_5b7a5bbfe18b)-[:HAS_PLACE { type: 'recorded at', begin_date: '2002-05-23', end_date: '2002-05-24' }]->(place_4744282c857d)

MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_44d30364913e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_44d30364913e)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_44d30364913e)
MERGE (person_770ba6cf4573)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_44d30364913e)
MERGE (person_4b132eb0567e)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_44d30364913e)
MERGE (person_e691027ebc13)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_44d30364913e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_a0d5f0a50fab)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a0d5f0a50fab)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a0d5f0a50fab)
MERGE (person_fe4dbff20ad2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_a0d5f0a50fab)
MERGE (person_4b132eb0567e)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_a0d5f0a50fab)
MERGE (person_e691027ebc13)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a0d5f0a50fab)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_d450d50e0f1d)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_d450d50e0f1d)
MERGE (person_fe4dbff20ad2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_d450d50e0f1d)
MERGE (person_4b132eb0567e)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_d450d50e0f1d)
MERGE (person_e691027ebc13)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_d450d50e0f1d)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8d3f63b8f928)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_8d3f63b8f928)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_8d3f63b8f928)
MERGE (person_770ba6cf4573)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_8d3f63b8f928)
MERGE (person_4b132eb0567e)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_8d3f63b8f928)
MERGE (person_e691027ebc13)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_8d3f63b8f928)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2fc72540fb4c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_2fc72540fb4c)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_2fc72540fb4c)
MERGE (person_4b132eb0567e)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_2fc72540fb4c)
MERGE (person_e691027ebc13)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_2fc72540fb4c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_96f9537748a5)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_96f9537748a5)
MERGE (person_fe4dbff20ad2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_96f9537748a5)
MERGE (person_4b132eb0567e)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_96f9537748a5)
MERGE (person_e691027ebc13)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_96f9537748a5)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_c910cfa5d309)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_c910cfa5d309)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_c910cfa5d309)
MERGE (person_770ba6cf4573)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_c910cfa5d309)
MERGE (person_4b132eb0567e)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_c910cfa5d309)
MERGE (person_e691027ebc13)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_c910cfa5d309)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_33c003013c39)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_33c003013c39)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_33c003013c39)
MERGE (person_fe4dbff20ad2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_33c003013c39)
MERGE (person_4b132eb0567e)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_33c003013c39)
MERGE (person_e691027ebc13)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_33c003013c39)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_5b7a5bbfe18b)
MERGE (person_4b132eb0567e)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_5b7a5bbfe18b)
MERGE (person_e691027ebc13)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_5b7a5bbfe18b)



"""
)