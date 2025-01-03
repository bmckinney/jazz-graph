
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_d218efd601ce:Release{ uuid: '5751234e-082d-4066-b0d8-d218efd601ce' })
SET release_d218efd601ce.name = 'True or False'
SET release_d218efd601ce.country = 'XE'
SET release_d218efd601ce.date = '1986'
SET release_d218efd601ce.format = 'CD'
SET release_d218efd601ce.discode = 'FRL-CD 007'
SET release_d218efd601ce.discogs = 'https://www.discogs.com/release/4163933'
SET release_d218efd601ce.musicbrainz = 'http://musicbrainz.org/release/5751234e-082d-4066-b0d8-d218efd601ce'
SET release_d218efd601ce.source = 'musicbrainz.org'


MERGE (person_8fd88fabb154:Person{ uuid: 'ae8c831c-feec-485d-9ff6-8fd88fabb154' }) 
SET person_8fd88fabb154.name = 'Ed Howard'
SET person_8fd88fabb154.gender = 'Male'
SET person_8fd88fabb154.disambiguation = 'bass player'
SET person_8fd88fabb154.country = 'US'
SET person_8fd88fabb154.allmusic = 'https://www.allmusic.com/artist/mn0000161279'
SET person_8fd88fabb154.discogs = 'https://www.discogs.com/artist/349386'
SET person_8fd88fabb154.viaf = 'http://viaf.org/viaf/32207997'
SET person_8fd88fabb154.wikidata = 'https://www.wikidata.org/wiki/Q1282376'
SET person_8fd88fabb154.databases = ['http://id.loc.gov/authorities/names/no99041140', 'https://catalogue.bnf.fr/ark:/12148/cb14188087c', 'https://d-nb.info/gnd/135067499', 'https://www.worldcat.org/identities/lccn-no99041140']
SET person_8fd88fabb154.musicbrainz = 'https://musicbrainz.org/artist/ae8c831c-feec-485d-9ff6-8fd88fabb154'
SET person_8fd88fabb154.isni_list = ['http://isni.org/isni/0000000077317066']
SET person_8fd88fabb154.source = 'musicbrainz.org'


MERGE (person_c561811b3eba:Person{ uuid: 'd9b17257-9c57-4797-8ce4-c561811b3eba' }) 
SET person_c561811b3eba.name = 'Jean-Paul Rodrique'
SET person_c561811b3eba.gender = 'Male'
SET person_c561811b3eba.allmusic = 'https://www.allmusic.com/artist/mn0000231902'
SET person_c561811b3eba.musicbrainz = 'https://musicbrainz.org/artist/d9b17257-9c57-4797-8ce4-c561811b3eba'
SET person_c561811b3eba.source = 'musicbrainz.org'


MERGE (person_b551ad55e0c1:Person{ uuid: 'eae802a4-781d-4c0a-8133-b551ad55e0c1' }) 
SET person_b551ad55e0c1.name = 'Hervé Le Guil'
SET person_b551ad55e0c1.gender = 'Male'
SET person_b551ad55e0c1.disambiguation = 'Engineer'
SET person_b551ad55e0c1.source = 'musicbrainz.org'


MERGE (person_e47b5bbe8b9a:Person{ uuid: '138c975d-d55e-48b8-9b4c-e47b5bbe8b9a' }) 
SET person_e47b5bbe8b9a.name = 'Ralph Moore'
SET person_e47b5bbe8b9a.gender = 'Male'
SET person_e47b5bbe8b9a.disambiguation = 'jazz tenor saxophonist'
SET person_e47b5bbe8b9a.country = 'GB'
SET person_e47b5bbe8b9a.allmusic = 'https://www.allmusic.com/artist/mn0000387210'
SET person_e47b5bbe8b9a.discogs = 'https://www.discogs.com/artist/552908'
SET person_e47b5bbe8b9a.viaf = 'http://viaf.org/viaf/5120918'
SET person_e47b5bbe8b9a.wikidata = 'https://www.wikidata.org/wiki/Q2129719'
SET person_e47b5bbe8b9a.databases = ['http://id.loc.gov/authorities/names/no98000088', 'https://catalogue.bnf.fr/ark:/12148/cb13930788x', 'https://d-nb.info/gnd/134579259', 'https://www.worldcat.org/identities/lccn-no98000088']
SET person_e47b5bbe8b9a.musicbrainz = 'https://musicbrainz.org/artist/138c975d-d55e-48b8-9b4c-e47b5bbe8b9a'
SET person_e47b5bbe8b9a.isni_list = ['http://isni.org/isni/0000000078389571']
SET person_e47b5bbe8b9a.source = 'musicbrainz.org'


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
SET person_6f0a331cc1ca.databases = ['http://id.loc.gov/authorities/names/n81140108', 'https://adp.library.ucsb.edu/names/320530', 'https://catalogue.bnf.fr/ark:/12148/cb13895060w', 'https://d-nb.info/gnd/134400623', 'http://snaccooperative.org/ark:/99166/w6fj33d4', 'https://www.worldcat.org/identities/lccn-n81140108']
SET person_6f0a331cc1ca.musicbrainz = 'https://musicbrainz.org/artist/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.isni_list = ['http://isni.org/isni/0000000078266176']
SET person_6f0a331cc1ca.source = 'musicbrainz.org'


MERGE (person_b84e43378390:Person{ uuid: '30b01f7e-2af1-4293-a52c-b84e43378390' }) 
SET person_b84e43378390.name = 'David Kikoski'
SET person_b84e43378390.gender = 'Male'
SET person_b84e43378390.country = 'US'
SET person_b84e43378390.allmusic = 'https://www.allmusic.com/artist/mn0000811141'
SET person_b84e43378390.discogs = 'https://www.discogs.com/artist/486649'
SET person_b84e43378390.viaf = 'http://viaf.org/viaf/233486283'
SET person_b84e43378390.wikidata = 'https://www.wikidata.org/wiki/Q1174978'
SET person_b84e43378390.wikipedia = 'https://en.wikipedia.org/wiki/David_Kikoski'
SET person_b84e43378390.databases = ['http://id.loc.gov/authorities/names/n87142774', 'https://catalogue.bnf.fr/ark:/12148/cb139775835', 'https://d-nb.info/gnd/134644328', 'https://www.worldcat.org/identities/lccn-n87142774']
SET person_b84e43378390.musicbrainz = 'https://musicbrainz.org/artist/30b01f7e-2af1-4293-a52c-b84e43378390'
SET person_b84e43378390.isni_list = ['http://isni.org/isni/0000000367948974']
SET person_b84e43378390.source = 'musicbrainz.org'

// labels

MERGE (label_574483ee61ae:Label{ uuid: '78099549-0306-405a-91fb-574483ee61ae' })
SET label_574483ee61ae.name= 'Free Lance'

// performances

MERGE (perf_6fa81cb09eb2:Performance{ uuid: 'a2d91107-3438-4b7c-9cb4-6fa81cb09eb2' })
SET perf_6fa81cb09eb2.name = 'Limehouse Blues'
SET perf_6fa81cb09eb2.duration = '5:04'
SET perf_6fa81cb09eb2.source = 'musicbrainz.org'


MERGE (perf_e1d04799e1bd:Performance{ uuid: '807f4f9d-c865-4acc-98aa-e1d04799e1bd' })
SET perf_e1d04799e1bd.name = 'In a Sentimental Mood'
SET perf_e1d04799e1bd.duration = '7:19'
SET perf_e1d04799e1bd.begin_date = '1986-10-30'
SET perf_e1d04799e1bd.end_date = '1986-10-30'
SET perf_e1d04799e1bd.source = 'musicbrainz.org'


MERGE (perf_dfc7d3d1225d:Performance{ uuid: '90afec99-5a43-4ac7-8bad-dfc7d3d1225d' })
SET perf_dfc7d3d1225d.name = 'The Everywhere Calypso'
SET perf_dfc7d3d1225d.duration = '9:21'
SET perf_dfc7d3d1225d.begin_date = '1986-10-30'
SET perf_dfc7d3d1225d.end_date = '1986-10-30'
SET perf_dfc7d3d1225d.source = 'musicbrainz.org'


MERGE (perf_9a41800fdc9e:Performance{ uuid: '0217f536-f9e9-4b75-a20c-9a41800fdc9e' })
SET perf_9a41800fdc9e.name = 'Big Foot'
SET perf_9a41800fdc9e.duration = '4:38'
SET perf_9a41800fdc9e.begin_date = '1986-10-30'
SET perf_9a41800fdc9e.end_date = '1986-10-30'
SET perf_9a41800fdc9e.source = 'musicbrainz.org'


MERGE (perf_95027d90fd39:Performance{ uuid: 'ae8b1723-d6b4-4421-b972-95027d90fd39' })
SET perf_95027d90fd39.name = 'Psalm'
SET perf_95027d90fd39.duration = '12:27'
SET perf_95027d90fd39.begin_date = '1986-10-30'
SET perf_95027d90fd39.end_date = '1986-10-30'
SET perf_95027d90fd39.source = 'musicbrainz.org'


MERGE (perf_1bbf8914ea6c:Performance{ uuid: 'bef25749-2342-464c-9890-1bbf8914ea6c' })
SET perf_1bbf8914ea6c.name = 'True or False'
SET perf_1bbf8914ea6c.duration = '2:40'
SET perf_1bbf8914ea6c.source = 'musicbrainz.org'


MERGE (perf_00d6774c99e5:Performance{ uuid: '214290e5-d8cc-4493-a4bd-00d6774c99e5' })
SET perf_00d6774c99e5.name = 'Played Twice'
SET perf_00d6774c99e5.duration = '5:16'
SET perf_00d6774c99e5.begin_date = '1986-10-30'
SET perf_00d6774c99e5.end_date = '1986-10-30'
SET perf_00d6774c99e5.source = 'musicbrainz.org'


MERGE (perf_4280729d97a4:Performance{ uuid: '59ef05dc-3938-4dff-a21e-4280729d97a4' })
SET perf_4280729d97a4.name = 'Bud Powell'
SET perf_4280729d97a4.duration = '9:37'
SET perf_4280729d97a4.begin_date = '1986-10-30'
SET perf_4280729d97a4.end_date = '1986-10-30'
SET perf_4280729d97a4.source = 'musicbrainz.org'


MERGE (perf_8891954aab69:Performance{ uuid: 'a5083bf3-4779-4daf-b3c0-8891954aab69' })
SET perf_8891954aab69.name = 'Free-Fi-Fo-Rum'
SET perf_8891954aab69.duration = '8:18'
SET perf_8891954aab69.source = 'musicbrainz.org'




// labels
MERGE (release_d218efd601ce)-[:HAS_LABEL]->(label_574483ee61ae)


// tracks
MERGE (release_d218efd601ce)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_6fa81cb09eb2)
MERGE (release_d218efd601ce)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_e1d04799e1bd)
MERGE (release_d218efd601ce)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_dfc7d3d1225d)
MERGE (release_d218efd601ce)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_9a41800fdc9e)
MERGE (release_d218efd601ce)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_95027d90fd39)
MERGE (release_d218efd601ce)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_1bbf8914ea6c)
MERGE (release_d218efd601ce)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_00d6774c99e5)
MERGE (release_d218efd601ce)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_4280729d97a4)
MERGE (release_d218efd601ce)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_8891954aab69)

// works

MERGE (person_1ef2fece51ce:Person{ uuid: '2a2bf494-ac80-4ac9-901f-1ef2fece51ce' }) 
SET person_1ef2fece51ce.name = 'Irving Mills'
SET person_1ef2fece51ce.gender = 'Male'
SET person_1ef2fece51ce.country = 'US'
SET person_1ef2fece51ce.allmusic = 'https://www.allmusic.com/artist/mn0000084993'
SET person_1ef2fece51ce.discogs = 'https://www.discogs.com/artist/307446'
SET person_1ef2fece51ce.imdb = 'https://www.imdb.com/name/nm0590030/'
SET person_1ef2fece51ce.viaf = 'http://viaf.org/viaf/76500944'
SET person_1ef2fece51ce.wikidata = 'https://www.wikidata.org/wiki/Q1292110'
SET person_1ef2fece51ce.databases = ['http://id.loc.gov/authorities/names/n88621778', 'https://catalogue.bnf.fr/ark:/12148/cb13897535j', 'https://d-nb.info/gnd/135465664', 'https://ibdb.com/person.php?id=83868', 'http://snaccooperative.org/ark:/99166/w6f50280', 'https://nla.gov.au/nla.party-1528202', 'https://rateyourmusic.com/artist/irving_mills', 'https://www.worldcat.org/identities/lccn-n88621778/']
SET person_1ef2fece51ce.musicbrainz = 'https://musicbrainz.org/artist/2a2bf494-ac80-4ac9-901f-1ef2fece51ce'
SET person_1ef2fece51ce.isni_list = ['http://isni.org/isni/0000000081569522']
SET person_1ef2fece51ce.source = 'musicbrainz.org'


MERGE (person_5a269b32b4c2:Person{ uuid: '8446fcca-109e-4c6d-a2ff-5a269b32b4c2' }) 
SET person_5a269b32b4c2.name = 'Chick Corea'
SET person_5a269b32b4c2.gender = 'Male'
SET person_5a269b32b4c2.disambiguation = 'jazz pianist'
SET person_5a269b32b4c2.country = 'US'
SET person_5a269b32b4c2.allmusic = 'https://www.allmusic.com/artist/mn0000110541'
SET person_5a269b32b4c2.discogs = 'https://www.discogs.com/artist/37731'
SET person_5a269b32b4c2.imdb = 'https://www.imdb.com/name/nm0179706/'
SET person_5a269b32b4c2.viaf = 'http://viaf.org/viaf/37337806'
SET person_5a269b32b4c2.wikidata = 'https://www.wikidata.org/wiki/Q192465'
SET person_5a269b32b4c2.databases = ['http://id.loc.gov/authorities/names/n81080890', 'https://adp.library.ucsb.edu/names/309754', 'https://catalogue.bnf.fr/ark:/12148/cb13892744v', 'https://d-nb.info/gnd/119238489', 'https://rateyourmusic.com/artist/chick_corea', 'https://www.worldcat.org/identities/lccn-n81080890']
SET person_5a269b32b4c2.musicbrainz = 'https://musicbrainz.org/artist/8446fcca-109e-4c6d-a2ff-5a269b32b4c2'
SET person_5a269b32b4c2.isni_list = ['http://isni.org/isni/0000000121285074']
SET person_5a269b32b4c2.source = 'musicbrainz.org'


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
SET person_5260b4274ed4.databases = ['http://id.loc.gov/authorities/names/n82218969', 'https://catalogue.bnf.fr/ark:/12148/cb13897622g', 'https://d-nb.info/gnd/118826158', 'http://snaccooperative.org/ark:/99166/w6j38zvn', 'https://rateyourmusic.com/artist/thelonious_monk', 'https://www.worldcat.org/identities/lccn-n82218969']
SET person_5260b4274ed4.musicbrainz = 'https://musicbrainz.org/artist/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.isni_list = ['http://isni.org/isni/0000000120249127']
SET person_5260b4274ed4.source = 'musicbrainz.org'


MERGE (person_bad80243802a:Person{ uuid: '3b47247e-5b57-49b6-a0ed-bad80243802a' }) 
SET person_bad80243802a.name = 'Sonny Rollins'
SET person_bad80243802a.gender = 'Male'
SET person_bad80243802a.country = 'US'
SET person_bad80243802a.allmusic = 'https://www.allmusic.com/artist/mn0000039656'
SET person_bad80243802a.bbc = 'https://www.bbc.co.uk/music/artists/3b47247e-5b57-49b6-a0ed-bad80243802a'
SET person_bad80243802a.discogs = 'https://www.discogs.com/artist/145264'
SET person_bad80243802a.imdb = 'https://www.imdb.com/name/nm0738456/'
SET person_bad80243802a.viaf = 'http://viaf.org/viaf/7368226'
SET person_bad80243802a.wikidata = 'https://www.wikidata.org/wiki/Q299208'
SET person_bad80243802a.databases = ['http://id.loc.gov/authorities/names/n82144213', 'https://catalogue.bnf.fr/ark:/12148/cb138991337', 'https://d-nb.info/gnd/118749552', 'http://snaccooperative.org/ark:/99166/w6bg2vq8', 'https://rateyourmusic.com/artist/sonny_rollins', 'https://www.musik-sammler.de/artist/sonny-rollins/', 'https://www.worldcat.org/identities/lccn-n82-144213']
SET person_bad80243802a.musicbrainz = 'https://musicbrainz.org/artist/3b47247e-5b57-49b6-a0ed-bad80243802a'
SET person_bad80243802a.isni_list = ['http://isni.org/isni/0000000110367920']
SET person_bad80243802a.source = 'musicbrainz.org'


MERGE (person_7eeeb45e411f:Person{ uuid: '3af06bc4-68ad-4cae-bb7a-7eeeb45e411f' }) 
SET person_7eeeb45e411f.name = 'Duke Ellington'
SET person_7eeeb45e411f.gender = 'Male'
SET person_7eeeb45e411f.disambiguation = 'US composer, pianist & jazz bandleader'
SET person_7eeeb45e411f.country = 'US'
SET person_7eeeb45e411f.allmusic = 'https://www.allmusic.com/artist/mn0000120323'
SET person_7eeeb45e411f.bbc = 'https://www.bbc.co.uk/music/artists/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.discogs = 'https://www.discogs.com/artist/145257'
SET person_7eeeb45e411f.imdb = 'https://www.imdb.com/name/nm0254153/'
SET person_7eeeb45e411f.viaf = 'http://viaf.org/viaf/66651610'
SET person_7eeeb45e411f.wikidata = 'https://www.wikidata.org/wiki/Q4030'
SET person_7eeeb45e411f.databases = ['http://id.loc.gov/authorities/names/n50080187', 'https://adp.library.ucsb.edu/names/102155', 'https://catalogue.bnf.fr/ark:/12148/cb13893638w', 'https://d-nb.info/gnd/118529994', 'https://ibdb.com/person.php?id=11631', 'http://snaccooperative.org/ark:/99166/w6639nkm', 'https://nla.gov.au/nla.party-815399', 'https://openlibrary.org/works/OL1953949A', 'https://rateyourmusic.com/artist/duke_ellington', 'https://www.worldcat.org/identities/lccn-n50080187/']
SET person_7eeeb45e411f.musicbrainz = 'https://musicbrainz.org/artist/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.isni_list = ['http://isni.org/isni/0000000109110810']
SET person_7eeeb45e411f.source = 'musicbrainz.org'


MERGE (person_c73775716312:Person{ uuid: 'c7356af9-9ea6-4a78-a55b-c73775716312' }) 
SET person_c73775716312.name = 'Charlie Parker'
SET person_c73775716312.gender = 'Male'
SET person_c73775716312.disambiguation = 'a.k.a. “Bird”, jazz alto saxophonist'
SET person_c73775716312.country = 'US'
SET person_c73775716312.allmusic = 'https://www.allmusic.com/artist/mn0000211758'
SET person_c73775716312.bbc = 'https://www.bbc.co.uk/music/artists/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.discogs = 'https://www.discogs.com/artist/1424206'
SET person_c73775716312.discogs = 'https://www.discogs.com/artist/753336'
SET person_c73775716312.discogs = 'https://www.discogs.com/artist/75617'
SET person_c73775716312.imdb = 'https://www.imdb.com/name/nm0662127/'
SET person_c73775716312.viaf = 'http://viaf.org/viaf/10034216'
SET person_c73775716312.wikidata = 'https://www.wikidata.org/wiki/Q103767'
SET person_c73775716312.databases = ['http://id.loc.gov/authorities/names/n50050327', 'https://adp.library.ucsb.edu/names/336464', 'https://catalogue.bnf.fr/ark:/12148/cb13898247z', 'https://d-nb.info/gnd/118739328', 'http://snaccooperative.org/ark:/99166/w67086vq', 'https://nla.gov.au/nla.party-911160', 'https://openlibrary.org/works/OL4918032A', 'https://rateyourmusic.com/artist/charlie_parker', 'https://www.musik-sammler.de/artist/charlie-parker/', 'https://www.worldcat.org/identities/lccn-n50050327']
SET person_c73775716312.musicbrainz = 'https://musicbrainz.org/artist/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.isni_list = ['http://isni.org/isni/0000000120955806', 'http://isni.org/isni/0000000368633974']
SET person_c73775716312.source = 'musicbrainz.org'


MERGE (person_355432882659:Person{ uuid: 'e96287e1-c455-45df-8875-355432882659' }) 
SET person_355432882659.name = 'Mann Curtis'
SET person_355432882659.gender = 'Male'
SET person_355432882659.country = 'US'
SET person_355432882659.allmusic = 'https://www.allmusic.com/artist/mn0000957528'
SET person_355432882659.discogs = 'https://www.discogs.com/artist/638167'
SET person_355432882659.discogs = 'https://www.discogs.com/artist/705636'
SET person_355432882659.imdb = 'https://www.imdb.com/name/nm0193437/'
SET person_355432882659.viaf = 'http://viaf.org/viaf/64273858'
SET person_355432882659.wikidata = 'https://www.wikidata.org/wiki/Q6750983'
SET person_355432882659.databases = ['http://id.loc.gov/authorities/names/no2007031393', 'https://adp.library.ucsb.edu/names/113468', 'https://catalogue.bnf.fr/ark:/12148/cb14838791q', 'https://d-nb.info/gnd/1183296061', 'https://ibdb.com/person.php?id=89878', 'http://snaccooperative.org/ark:/99166/w6kj3jqs', 'https://nla.gov.au/nla.party-1529195', 'https://www.worldcat.org/identities/lccn-no2007031393']
SET person_355432882659.musicbrainz = 'https://musicbrainz.org/artist/e96287e1-c455-45df-8875-355432882659'
SET person_355432882659.isni_list = ['http://isni.org/isni/0000000444569565']
SET person_355432882659.source = 'musicbrainz.org'


MERGE (work_ee39c88445cf:Work{ uuid: '5b305852-db2f-41fc-ae40-ee39c88445cf' })
SET work_ee39c88445cf.name = 'Psalm'
SET work_ee39c88445cf.iswc = 'T-904.321.189-8'
SET work_ee39c88445cf.type = 'Song'
SET work_ee39c88445cf.source = 'musicbrainz.org'


MERGE (work_615608b459e0:Work{ uuid: '68cba0e7-4082-4f5f-b1d4-615608b459e0' })
SET work_615608b459e0.name = 'Played Twice'
SET work_615608b459e0.iswc = 'T-700.054.153-9'
SET work_615608b459e0.type = 'Song'
SET work_615608b459e0.source = 'musicbrainz.org'


MERGE (work_f1250f0d5668:Work{ uuid: 'ef0943b6-88d9-4d57-82a8-f1250f0d5668' })
SET work_f1250f0d5668.name = 'Big Foot'
SET work_f1250f0d5668.type = 'Song'
SET work_f1250f0d5668.wikidata = 'https://www.wikidata.org/wiki/Q4905709'
SET work_f1250f0d5668.musicbrainz = 'https://musicbrainz.org/work/ef0943b6-88d9-4d57-82a8-f1250f0d5668'
SET work_f1250f0d5668.source = 'musicbrainz.org'


MERGE (work_98d695dbaf1b:Work{ uuid: '421e7a45-be56-459a-a498-98d695dbaf1b' })
SET work_98d695dbaf1b.name = 'Bud Powell'
SET work_98d695dbaf1b.type = 'Song'
SET work_98d695dbaf1b.source = 'musicbrainz.org'


MERGE (work_66bf486ed223:Work{ uuid: 'ded7f209-8a98-4980-930c-66bf486ed223' })
SET work_66bf486ed223.name = 'The Everywhere Calypso'
SET work_66bf486ed223.iswc = 'T-070.881.354-0'
SET work_66bf486ed223.source = 'musicbrainz.org'


MERGE (work_5e6c198757eb:Work{ uuid: '276e1824-a584-3c58-a4ee-5e6c198757eb' })
SET work_5e6c198757eb.name = 'In a Sentimental Mood'
SET work_5e6c198757eb.iswc = 'T-011.245.032-4'
SET work_5e6c198757eb.type = 'Song'
SET work_5e6c198757eb.wikidata = 'https://www.wikidata.org/wiki/Q1660683'
SET work_5e6c198757eb.musicbrainz = 'https://musicbrainz.org/work/276e1824-a584-3c58-a4ee-5e6c198757eb'
SET work_5e6c198757eb.source = 'musicbrainz.org'



// performances of
MERGE (perf_95027d90fd39)-[:PERFORMANCE_OF]->(work_ee39c88445cf)
MERGE (perf_00d6774c99e5)-[:PERFORMANCE_OF]->(work_615608b459e0)
MERGE (perf_9a41800fdc9e)-[:PERFORMANCE_OF]->(work_f1250f0d5668)
MERGE (perf_4280729d97a4)-[:PERFORMANCE_OF]->(work_98d695dbaf1b)
MERGE (perf_dfc7d3d1225d)-[:PERFORMANCE_OF]->(work_66bf486ed223)
MERGE (perf_e1d04799e1bd)-[:PERFORMANCE_OF]->(work_5e6c198757eb)


// composers
MERGE (person_5a269b32b4c2)-[:COMPOSED]->(work_ee39c88445cf)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_615608b459e0)
MERGE (person_c73775716312)-[:COMPOSED]->(work_f1250f0d5668)
MERGE (person_5a269b32b4c2)-[:COMPOSED]->(work_98d695dbaf1b)
MERGE (person_bad80243802a)-[:COMPOSED]->(work_66bf486ed223)
MERGE (person_7eeeb45e411f)-[:COMPOSED]->(work_5e6c198757eb)
MERGE (person_355432882659)-[:WROTE_LYRICS]->(work_5e6c198757eb)
MERGE (person_1ef2fece51ce)-[:WROTE_LYRICS]->(work_5e6c198757eb)


// place nodes

MERGE (place_bc1759b1a048:Place{ uuid: '53a8ccaa-e9c6-4e3f-8293-bc1759b1a048' })
SET place_bc1759b1a048.name = 'Magnetic Terrace'
SET place_bc1759b1a048.source = 'musicbrainz.org'


// place relationships
MERGE (perf_e1d04799e1bd)-[:HAS_PLACE { type: 'recorded at', begin_date: '1986-10-30', end_date: '1986-10-30' }]->(place_bc1759b1a048)
MERGE (perf_dfc7d3d1225d)-[:HAS_PLACE { type: 'recorded at', begin_date: '1986-10-30', end_date: '1986-10-30' }]->(place_bc1759b1a048)
MERGE (perf_9a41800fdc9e)-[:HAS_PLACE { type: 'recorded at', begin_date: '1986-10-30', end_date: '1986-10-30' }]->(place_bc1759b1a048)
MERGE (perf_95027d90fd39)-[:HAS_PLACE { type: 'recorded at', begin_date: '1986-10-30', end_date: '1986-10-30' }]->(place_bc1759b1a048)
MERGE (perf_00d6774c99e5)-[:HAS_PLACE { type: 'recorded at', begin_date: '1986-10-30', end_date: '1986-10-30' }]->(place_bc1759b1a048)
MERGE (perf_4280729d97a4)-[:HAS_PLACE { type: 'recorded at', begin_date: '1986-10-30', end_date: '1986-10-30' }]->(place_bc1759b1a048)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e1d04799e1bd)
MERGE (person_8fd88fabb154)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e1d04799e1bd)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e1d04799e1bd)
MERGE (person_e47b5bbe8b9a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_e1d04799e1bd)
MERGE (person_c561811b3eba)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e1d04799e1bd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_dfc7d3d1225d)
MERGE (person_8fd88fabb154)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_dfc7d3d1225d)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_dfc7d3d1225d)
MERGE (person_e47b5bbe8b9a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_dfc7d3d1225d)
MERGE (person_c561811b3eba)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_dfc7d3d1225d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9a41800fdc9e)
MERGE (person_8fd88fabb154)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_9a41800fdc9e)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_9a41800fdc9e)
MERGE (person_e47b5bbe8b9a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9a41800fdc9e)
MERGE (person_c561811b3eba)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_9a41800fdc9e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_95027d90fd39)
MERGE (person_8fd88fabb154)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_95027d90fd39)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_95027d90fd39)
MERGE (person_e47b5bbe8b9a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_95027d90fd39)
MERGE (person_c561811b3eba)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_95027d90fd39)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_00d6774c99e5)
MERGE (person_8fd88fabb154)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_00d6774c99e5)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_00d6774c99e5)
MERGE (person_e47b5bbe8b9a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_00d6774c99e5)
MERGE (person_c561811b3eba)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_00d6774c99e5)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_4280729d97a4)
MERGE (person_8fd88fabb154)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_4280729d97a4)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_4280729d97a4)
MERGE (person_e47b5bbe8b9a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_4280729d97a4)
MERGE (person_c561811b3eba)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_4280729d97a4)



"""
)