
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_3162ad253ec3:Release{ uuid: 'a9f73046-296c-4d50-843f-3162ad253ec3' })
SET release_3162ad253ec3.name = 'Here\\'s Jaki'
SET release_3162ad253ec3.country = 'US'
SET release_3162ad253ec3.date = '1961'
SET release_3162ad253ec3.format = 'CD'
SET release_3162ad253ec3.discode = 'NJ 8256'
SET release_3162ad253ec3.discogs = 'https://www.discogs.com/release/5728157'
SET release_3162ad253ec3.musicbrainz = 'http://musicbrainz.org/release/a9f73046-296c-4d50-843f-3162ad253ec3'
SET release_3162ad253ec3.source = 'musicbrainz.org'


MERGE (person_84a8b7f41799:Person{ uuid: '3f627e4e-4d29-45f0-8dd0-84a8b7f41799' }) 
SET person_84a8b7f41799.name = 'Jaki Byard'
SET person_84a8b7f41799.gender = 'Male'
SET person_84a8b7f41799.country = 'US'
SET person_84a8b7f41799.allmusic = 'https://www.allmusic.com/artist/mn0000112535'
SET person_84a8b7f41799.discogs = 'https://www.discogs.com/artist/252610'
SET person_84a8b7f41799.viaf = 'http://viaf.org/viaf/61731187'
SET person_84a8b7f41799.wikidata = 'https://www.wikidata.org/wiki/Q1346401'
SET person_84a8b7f41799.databases = ['http://d-nb.info/gnd/134582888', 'http://id.loc.gov/authorities/names/n78048954', 'https://catalogue.bnf.fr/ark:/12148/cb138920338', 'http://snaccooperative.org/ark:/99166/w6pg2qp8', 'https://www.worldcat.org/identities/lccn-n78048954']
SET person_84a8b7f41799.musicbrainz = 'https://musicbrainz.org/artist/3f627e4e-4d29-45f0-8dd0-84a8b7f41799'
SET person_84a8b7f41799.isni_list = ['http://isni.org/isni/0000000096156501']
SET person_84a8b7f41799.source = 'musicbrainz.org'


MERGE (person_b804df7fa6bb:Person{ uuid: '68c93572-8296-49ea-b94e-b804df7fa6bb' }) 
SET person_b804df7fa6bb.name = 'Esmond Edwards'
SET person_b804df7fa6bb.gender = 'Male'
SET person_b804df7fa6bb.country = 'US'
SET person_b804df7fa6bb.discogs = 'https://www.discogs.com/artist/254944'
SET person_b804df7fa6bb.wikidata = 'https://www.wikidata.org/wiki/Q1367939'
SET person_b804df7fa6bb.musicbrainz = 'https://musicbrainz.org/artist/68c93572-8296-49ea-b94e-b804df7fa6bb'
SET person_b804df7fa6bb.source = 'musicbrainz.org'


MERGE (person_05d508e09a73:Person{ uuid: 'f0707f1d-55e1-46b6-8a9c-05d508e09a73' }) 
SET person_05d508e09a73.name = 'Rudy van Gelder'
SET person_05d508e09a73.gender = 'Male'
SET person_05d508e09a73.country = 'US'
SET person_05d508e09a73.allmusic = 'https://www.allmusic.com/artist/mn0000305301'
SET person_05d508e09a73.discogs = 'https://www.discogs.com/artist/252966'
SET person_05d508e09a73.viaf = 'http://viaf.org/viaf/33997197'
SET person_05d508e09a73.wikidata = 'https://www.wikidata.org/wiki/Q945681'
SET person_05d508e09a73.databases = ['http://d-nb.info/gnd/133648508', 'http://id.loc.gov/authorities/names/no00020144', 'https://rateyourmusic.com/artist/rudy_van_gelder', 'https://www.worldcat.org/identities/lccn-no00020144']
SET person_05d508e09a73.musicbrainz = 'https://musicbrainz.org/artist/f0707f1d-55e1-46b6-8a9c-05d508e09a73'
SET person_05d508e09a73.isni_list = ['http://isni.org/isni/0000000019691076']
SET person_05d508e09a73.source = 'musicbrainz.org'


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


MERGE (person_e044666c4828:Person{ uuid: '57db3f59-9c58-4f68-a00e-e044666c4828' }) 
SET person_e044666c4828.name = 'Ron Carter'
SET person_e044666c4828.gender = 'Male'
SET person_e044666c4828.disambiguation = 'US jazz double-bassist'
SET person_e044666c4828.country = 'US'
SET person_e044666c4828.allmusic = 'https://www.allmusic.com/artist/mn0000275832'
SET person_e044666c4828.discogs = 'https://www.discogs.com/artist/95088'
SET person_e044666c4828.imdb = 'https://www.imdb.com/name/nm0141909/'
SET person_e044666c4828.viaf = 'http://viaf.org/viaf/22326766'
SET person_e044666c4828.wikidata = 'https://www.wikidata.org/wiki/Q434593'
SET person_e044666c4828.databases = ['http://d-nb.info/gnd/134344332', 'http://id.loc.gov/authorities/names/n81014576', 'https://catalogue.bnf.fr/ark:/12148/cb138922167', 'http://snaccooperative.org/ark:/99166/w67m16sc', 'https://rateyourmusic.com/artist/ron_carter', 'https://www.worldcat.org/identities/lccn-n81014576']
SET person_e044666c4828.musicbrainz = 'https://musicbrainz.org/artist/57db3f59-9c58-4f68-a00e-e044666c4828'
SET person_e044666c4828.isni_list = ['http://isni.org/isni/0000000114394862']
SET person_e044666c4828.source = 'musicbrainz.org'

// labels

MERGE (label_d510b586b396:Label{ uuid: '3690758a-3ec1-4fd3-a250-d510b586b396' })
SET label_d510b586b396.name= 'New Jazz'

// performances

MERGE (perf_42af3d6eae5e:Performance{ uuid: 'fed06def-d2af-48c6-9ab2-42af3d6eae5e' })
SET perf_42af3d6eae5e.name = 'Cinco y quatro'
SET perf_42af3d6eae5e.duration = '6:26'
SET perf_42af3d6eae5e.begin_date = '1961-03-14'
SET perf_42af3d6eae5e.end_date = '1961-03-14'
SET perf_42af3d6eae5e.source = 'musicbrainz.org'


MERGE (perf_854362548e3d:Performance{ uuid: '7e275575-5bf7-4902-9f86-854362548e3d' })
SET perf_854362548e3d.name = 'Mellow Septet'
SET perf_854362548e3d.duration = '5:38'
SET perf_854362548e3d.begin_date = '1961-03-14'
SET perf_854362548e3d.end_date = '1961-03-14'
SET perf_854362548e3d.source = 'musicbrainz.org'


MERGE (perf_bcdfd629eeda:Performance{ uuid: '0b8913b6-73dc-4f2d-8acd-bcdfd629eeda' })
SET perf_bcdfd629eeda.name = 'Garnerin\\' a Bit'
SET perf_bcdfd629eeda.duration = '5:49'
SET perf_bcdfd629eeda.begin_date = '1961-03-14'
SET perf_bcdfd629eeda.end_date = '1961-03-14'
SET perf_bcdfd629eeda.source = 'musicbrainz.org'


MERGE (perf_c8b936cd8610:Performance{ uuid: 'c01c2fd4-34b2-41e1-a96a-c8b936cd8610' })
SET perf_c8b936cd8610.name = 'Giant Steps'
SET perf_c8b936cd8610.duration = '2:22'
SET perf_c8b936cd8610.begin_date = '1961-03-14'
SET perf_c8b936cd8610.end_date = '1961-03-14'
SET perf_c8b936cd8610.source = 'musicbrainz.org'


MERGE (perf_720aeeb4bbff:Performance{ uuid: '67e12dca-1b53-4806-833c-720aeeb4bbff' })
SET perf_720aeeb4bbff.name = 'Bess You Is My Woman / It Ain\\'t Necessarily So'
SET perf_720aeeb4bbff.duration = '9:53'
SET perf_720aeeb4bbff.begin_date = '1961-03-14'
SET perf_720aeeb4bbff.end_date = '1961-03-14'
SET perf_720aeeb4bbff.source = 'musicbrainz.org'


MERGE (perf_bd15ad3842a2:Performance{ uuid: '9715b422-696e-4cfd-ac79-bd15ad3842a2' })
SET perf_bd15ad3842a2.name = 'To My Wife'
SET perf_bd15ad3842a2.duration = '5:13'
SET perf_bd15ad3842a2.begin_date = '1961-03-14'
SET perf_bd15ad3842a2.end_date = '1961-03-14'
SET perf_bd15ad3842a2.source = 'musicbrainz.org'


MERGE (perf_4bcf2c2e508d:Performance{ uuid: '7e919484-a27d-4bce-ad88-4bcf2c2e508d' })
SET perf_4bcf2c2e508d.name = 'D.D.L.J.'
SET perf_4bcf2c2e508d.duration = '3:49'
SET perf_4bcf2c2e508d.begin_date = '1961-03-14'
SET perf_4bcf2c2e508d.end_date = '1961-03-14'
SET perf_4bcf2c2e508d.source = 'musicbrainz.org'




// labels
MERGE (release_3162ad253ec3)-[:HAS_LABEL]->(label_d510b586b396)


// tracks
MERGE (release_3162ad253ec3)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_42af3d6eae5e)
MERGE (release_3162ad253ec3)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_854362548e3d)
MERGE (release_3162ad253ec3)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_bcdfd629eeda)
MERGE (release_3162ad253ec3)-[:HAS_TRACK {name: 'A4', sequence: 4}]->(perf_c8b936cd8610)
MERGE (release_3162ad253ec3)-[:HAS_TRACK {name: 'B1', sequence: 5}]->(perf_720aeeb4bbff)
MERGE (release_3162ad253ec3)-[:HAS_TRACK {name: 'B2', sequence: 6}]->(perf_bd15ad3842a2)
MERGE (release_3162ad253ec3)-[:HAS_TRACK {name: 'B3', sequence: 7}]->(perf_4bcf2c2e508d)

// works

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


MERGE (person_b693a808a158:Person{ uuid: '65744963-191a-44ef-a3c7-b693a808a158' }) 
SET person_b693a808a158.name = 'George Gershwin'
SET person_b693a808a158.gender = 'Male'
SET person_b693a808a158.disambiguation = 'composer'
SET person_b693a808a158.country = 'US'
SET person_b693a808a158.allmusic = 'https://www.allmusic.com/artist/mn0000197918'
SET person_b693a808a158.bbc = 'https://www.bbc.co.uk/music/artists/65744963-191a-44ef-a3c7-b693a808a158'
SET person_b693a808a158.discogs = 'https://www.discogs.com/artist/261293'
SET person_b693a808a158.imdb = 'https://www.imdb.com/name/nm0006097/'
SET person_b693a808a158.viaf = 'http://viaf.org/viaf/61554329'
SET person_b693a808a158.wikidata = 'https://www.wikidata.org/wiki/Q123829'
SET person_b693a808a158.databases = ['http://d-nb.info/gnd/118639226', 'http://id.loc.gov/authorities/names/n79077265', 'https://catalogue.bnf.fr/ark:/12148/cb119493251', 'https://ibdb.com/person.php?id=5813', 'http://snaccooperative.org/ark:/99166/w6x065dx', 'https://nla.gov.au/nla.party-832382', 'https://openlibrary.org/works/OL67761A', 'http://soundtrackcollector.com/composer/33/', 'https://rateyourmusic.com/artist/george_gershwin', 'https://www.worldcat.org/identities/lccn-n79077265']
SET person_b693a808a158.musicbrainz = 'https://musicbrainz.org/artist/65744963-191a-44ef-a3c7-b693a808a158'
SET person_b693a808a158.isni_list = ['http://isni.org/isni/0000000121355968']
SET person_b693a808a158.source = 'musicbrainz.org'


MERGE (person_7fc9841b2cd9:Person{ uuid: 'bf23ae35-d26d-4180-b7da-7fc9841b2cd9' }) 
SET person_7fc9841b2cd9.name = 'Dorothy Heyward'
SET person_7fc9841b2cd9.gender = 'Female'
SET person_7fc9841b2cd9.disambiguation = 'playwright'
SET person_7fc9841b2cd9.country = 'US'
SET person_7fc9841b2cd9.discogs = 'https://www.discogs.com/artist/631840'
SET person_7fc9841b2cd9.imdb = 'https://www.imdb.com/name/nm0382378/'
SET person_7fc9841b2cd9.viaf = 'http://viaf.org/viaf/103290527'
SET person_7fc9841b2cd9.wikidata = 'https://www.wikidata.org/wiki/Q1250307'
SET person_7fc9841b2cd9.databases = ['http://d-nb.info/gnd/173807763', 'http://id.loc.gov/authorities/names/n87870897', 'https://catalogue.bnf.fr/ark:/12148/cb148597994', 'http://snaccooperative.org/ark:/99166/w6tq6gq0', 'https://openlibrary.org/works/OL1010347A', 'https://www.ibdb.com/person.php?id=5115', 'https://www.worldcat.org/identities/lccn-n87870897']
SET person_7fc9841b2cd9.musicbrainz = 'https://musicbrainz.org/artist/bf23ae35-d26d-4180-b7da-7fc9841b2cd9'
SET person_7fc9841b2cd9.isni_list = ['http://isni.org/isni/0000000109298841']
SET person_7fc9841b2cd9.source = 'musicbrainz.org'


MERGE (person_322e34240ffc:Person{ uuid: '509086c2-9cc8-4e77-89e9-322e34240ffc' }) 
SET person_322e34240ffc.name = 'Ira Gershwin'
SET person_322e34240ffc.gender = 'Male'
SET person_322e34240ffc.country = 'US'
SET person_322e34240ffc.allmusic = 'https://www.allmusic.com/artist/mn0000200301'
SET person_322e34240ffc.discogs = 'https://www.discogs.com/artist/264105'
SET person_322e34240ffc.imdb = 'https://www.imdb.com/name/nm0314857/'
SET person_322e34240ffc.viaf = 'http://viaf.org/viaf/39519496'
SET person_322e34240ffc.wikidata = 'https://www.wikidata.org/wiki/Q61059'
SET person_322e34240ffc.databases = ['http://d-nb.info/gnd/119500027', 'http://id.loc.gov/authorities/names/n50076010', 'https://catalogue.bnf.fr/ark:/12148/cb13194929s', 'https://ibdb.com/person.php?id=6435', 'http://snaccooperative.org/ark:/99166/w60w94tm', 'https://nla.gov.au/nla.party-965252', 'https://openlibrary.org/works/OL233692A', 'https://rateyourmusic.com/artist/ira_gershwin', 'https://www.worldcat.org/identities/lccn-n50076010/']
SET person_322e34240ffc.musicbrainz = 'https://musicbrainz.org/artist/509086c2-9cc8-4e77-89e9-322e34240ffc'
SET person_322e34240ffc.isni_list = ['http://isni.org/isni/0000000108901469']
SET person_322e34240ffc.source = 'musicbrainz.org'


MERGE (person_78dbf8b49b1b:Person{ uuid: '82953e0d-464a-4fb8-80fc-78dbf8b49b1b' }) 
SET person_78dbf8b49b1b.name = 'DuBose Heyward'
SET person_78dbf8b49b1b.gender = 'Male'
SET person_78dbf8b49b1b.country = 'US'
SET person_78dbf8b49b1b.allmusic = 'https://www.allmusic.com/artist/mn0000206446'
SET person_78dbf8b49b1b.discogs = 'https://www.discogs.com/artist/264106'
SET person_78dbf8b49b1b.imdb = 'https://www.imdb.com/name/nm0371738/'
SET person_78dbf8b49b1b.viaf = 'http://viaf.org/viaf/34476077'
SET person_78dbf8b49b1b.wikidata = 'https://www.wikidata.org/wiki/Q2382900'
SET person_78dbf8b49b1b.databases = ['http://d-nb.info/gnd/122186702', 'http://id.loc.gov/authorities/names/n50041800', 'https://catalogue.bnf.fr/ark:/12148/cb12052658x', 'http://snaccooperative.org/ark:/99166/w66q28zj', 'https://nla.gov.au/nla.party-943272', 'https://openlibrary.org/works/OL586886A', 'https://rateyourmusic.com/artist/dubose_heyward', 'https://www.ibdb.com/person.php?id=5141', 'https://www.worldcat.org/identities/lccn-n50041800']
SET person_78dbf8b49b1b.musicbrainz = 'https://musicbrainz.org/artist/82953e0d-464a-4fb8-80fc-78dbf8b49b1b'
SET person_78dbf8b49b1b.isni_list = ['http://isni.org/isni/0000000108863028']
SET person_78dbf8b49b1b.source = 'musicbrainz.org'


MERGE (work_6ff5e304f72a:Work{ uuid: '826c6acc-1f69-3dfc-8fda-6ff5e304f72a' })
SET work_6ff5e304f72a.name = 'Bess, You Is My Woman Now'
SET work_6ff5e304f72a.type = 'Song'
SET work_6ff5e304f72a.wikidata = 'https://www.wikidata.org/wiki/Q4896356'
SET work_6ff5e304f72a.musicbrainz = 'https://musicbrainz.org/work/826c6acc-1f69-3dfc-8fda-6ff5e304f72a'
SET work_6ff5e304f72a.source = 'musicbrainz.org'


MERGE (work_2cc1ade322c8:Work{ uuid: '8812f327-e92e-37b9-bdc4-2cc1ade322c8' })
SET work_2cc1ade322c8.name = 'It Ain’t Necessarily So'
SET work_2cc1ade322c8.iswc = 'T-070.907.010-9'
SET work_2cc1ade322c8.type = 'Song'
SET work_2cc1ade322c8.wikidata = 'https://www.wikidata.org/wiki/Q2920365'
SET work_2cc1ade322c8.musicbrainz = 'https://musicbrainz.org/work/8812f327-e92e-37b9-bdc4-2cc1ade322c8'
SET work_2cc1ade322c8.source = 'musicbrainz.org'


MERGE (work_f7b6a2e17b89:Work{ uuid: 'c53130a9-3173-37d2-bedd-f7b6a2e17b89' })
SET work_f7b6a2e17b89.name = 'Giant Steps'
SET work_f7b6a2e17b89.iswc = 'T-070.234.217-3'
SET work_f7b6a2e17b89.type = 'Song'
SET work_f7b6a2e17b89.wikidata = 'https://www.wikidata.org/wiki/Q3105303'
SET work_f7b6a2e17b89.musicbrainz = 'https://musicbrainz.org/work/c53130a9-3173-37d2-bedd-f7b6a2e17b89'
SET work_f7b6a2e17b89.source = 'musicbrainz.org'



// performances of
MERGE (perf_720aeeb4bbff)-[:PERFORMANCE_OF {medley: true}]->(work_6ff5e304f72a)
MERGE (perf_720aeeb4bbff)-[:PERFORMANCE_OF {medley: true}]->(work_2cc1ade322c8)
MERGE (perf_c8b936cd8610)-[:PERFORMANCE_OF]->(work_f7b6a2e17b89)


// composers
MERGE (person_b693a808a158)-[:COMPOSED]->(work_6ff5e304f72a)
MERGE (person_322e34240ffc)-[:WROTE_LYRICS]->(work_6ff5e304f72a)
MERGE (person_78dbf8b49b1b)-[:WROTE_LYRICS]->(work_6ff5e304f72a)
MERGE (person_b693a808a158)-[:COMPOSED]->(work_2cc1ade322c8)
MERGE (person_322e34240ffc)-[:WROTE_LYRICS]->(work_2cc1ade322c8)
MERGE (person_7fc9841b2cd9)-[:WROTE_LYRICS]->(work_2cc1ade322c8)
MERGE (person_78dbf8b49b1b)-[:WROTE_LYRICS]->(work_2cc1ade322c8)
MERGE (person_72ad46cdb831)-[:COMPOSED]->(work_f7b6a2e17b89)


// place nodes

MERGE (place_569fa8b97644:Place{ uuid: '1165ef7d-371c-4e03-98db-569fa8b97644' })
SET place_569fa8b97644.name = 'Van Gelder Studio'
SET place_569fa8b97644.source = 'musicbrainz.org'


// place relationships
MERGE (perf_42af3d6eae5e)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-03-14', end_date: '1961-03-14' }]->(place_569fa8b97644)
MERGE (perf_854362548e3d)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-03-14', end_date: '1961-03-14' }]->(place_569fa8b97644)
MERGE (perf_bcdfd629eeda)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-03-14', end_date: '1961-03-14' }]->(place_569fa8b97644)
MERGE (perf_c8b936cd8610)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-03-14', end_date: '1961-03-14' }]->(place_569fa8b97644)
MERGE (perf_720aeeb4bbff)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-03-14', end_date: '1961-03-14' }]->(place_569fa8b97644)
MERGE (perf_bd15ad3842a2)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-03-14', end_date: '1961-03-14' }]->(place_569fa8b97644)
MERGE (perf_4bcf2c2e508d)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-03-14', end_date: '1961-03-14' }]->(place_569fa8b97644)

MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_42af3d6eae5e)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_42af3d6eae5e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_42af3d6eae5e)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_42af3d6eae5e)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_42af3d6eae5e)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_854362548e3d)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_854362548e3d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_854362548e3d)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_854362548e3d)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_854362548e3d)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bcdfd629eeda)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_bcdfd629eeda)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_bcdfd629eeda)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_bcdfd629eeda)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_bcdfd629eeda)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_c8b936cd8610)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_c8b936cd8610)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_c8b936cd8610)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_c8b936cd8610)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_c8b936cd8610)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_720aeeb4bbff)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_720aeeb4bbff)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_720aeeb4bbff)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_720aeeb4bbff)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_720aeeb4bbff)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bd15ad3842a2)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_bd15ad3842a2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_bd15ad3842a2)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_bd15ad3842a2)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_bd15ad3842a2)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_4bcf2c2e508d)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_4bcf2c2e508d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_4bcf2c2e508d)
MERGE (person_b804df7fa6bb)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_4bcf2c2e508d)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_4bcf2c2e508d)



"""
)