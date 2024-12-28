
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_7a357fcf315a:Release{ uuid: '6f0e8389-4055-4eab-8ac5-7a357fcf315a' })
SET release_7a357fcf315a.name = 'Roy-Alty'
SET release_7a357fcf315a.country = 'DE'
SET release_7a357fcf315a.date = '2011-09-26'
SET release_7a357fcf315a.format = 'Digital Media'
SET release_7a357fcf315a.musicbrainz = 'http://musicbrainz.org/release/6f0e8389-4055-4eab-8ac5-7a357fcf315a'
SET release_7a357fcf315a.source = 'musicbrainz.org'


MERGE (person_db33730eb9a8:Person{ uuid: '07b6ae81-497e-4d8d-a546-db33730eb9a8' }) 
SET person_db33730eb9a8.name = 'David Wong'
SET person_db33730eb9a8.gender = 'Male'
SET person_db33730eb9a8.disambiguation = 'jazz bassist'
SET person_db33730eb9a8.country = 'US'
SET person_db33730eb9a8.source = 'musicbrainz.org'


MERGE (person_e552e95b3414:Person{ uuid: '8cdf780e-b909-4d25-9060-e552e95b3414' }) 
SET person_e552e95b3414.name = 'Roy Hargrove'
SET person_e552e95b3414.gender = 'Male'
SET person_e552e95b3414.country = 'US'
SET person_e552e95b3414.allmusic = 'https://www.allmusic.com/artist/mn0000345426'
SET person_e552e95b3414.discogs = 'https://www.discogs.com/artist/99438'
SET person_e552e95b3414.viaf = 'http://viaf.org/viaf/202111'
SET person_e552e95b3414.wikidata = 'https://www.wikidata.org/wiki/Q648750'
SET person_e552e95b3414.databases = ['http://d-nb.info/gnd/134692756', 'https://catalogue.bnf.fr/ark:/12148/cb13949049g', 'https://id.loc.gov/authorities/names/n92014464', 'http://snaccooperative.org/ark:/99166/w6hc1h53', 'https://rateyourmusic.com/artist/roy-hargrove', 'https://www.musik-sammler.de/artist/roy-hargrove/', 'https://www.worldcat.org/identities/lccn-n92014464']
SET person_e552e95b3414.musicbrainz = 'https://musicbrainz.org/artist/8cdf780e-b909-4d25-9060-e552e95b3414'
SET person_e552e95b3414.isni_list = ['http://isni.org/isni/0000000114869901']
SET person_e552e95b3414.source = 'musicbrainz.org'


MERGE (person_c69ca344fbf9:Person{ uuid: 'df4b8f80-4e31-45d3-85fa-c69ca344fbf9' }) 
SET person_c69ca344fbf9.name = 'Craig Haynes'
SET person_c69ca344fbf9.gender = 'Male'
SET person_c69ca344fbf9.disambiguation = 'US drummer, son of Roy Haynes'
SET person_c69ca344fbf9.country = 'US'
SET person_c69ca344fbf9.source = 'musicbrainz.org'


MERGE (person_9fbfb804134b:Person{ uuid: '6788b047-292d-43c6-a781-9fbfb804134b' }) 
SET person_9fbfb804134b.name = 'Martin Bejerano'
SET person_9fbfb804134b.gender = 'Male'
SET person_9fbfb804134b.allmusic = 'https://www.allmusic.com/artist/mn0000317681'
SET person_9fbfb804134b.discogs = 'https://www.discogs.com/artist/991779'
SET person_9fbfb804134b.wikidata = 'https://www.wikidata.org/wiki/Q19665888'
SET person_9fbfb804134b.musicbrainz = 'https://musicbrainz.org/artist/6788b047-292d-43c6-a781-9fbfb804134b'
SET person_9fbfb804134b.source = 'musicbrainz.org'


MERGE (person_7d2af4d4d728:Person{ uuid: 'f36ec9b1-6487-4511-87a1-7d2af4d4d728' }) 
SET person_7d2af4d4d728.name = 'Scott Petito'
SET person_7d2af4d4d728.gender = 'Male'
SET person_7d2af4d4d728.country = 'US'
SET person_7d2af4d4d728.discogs = 'https://www.discogs.com/artist/260164'
SET person_7d2af4d4d728.musicbrainz = 'https://musicbrainz.org/artist/f36ec9b1-6487-4511-87a1-7d2af4d4d728'
SET person_7d2af4d4d728.source = 'musicbrainz.org'


MERGE (person_e52968d43c57:Person{ uuid: 'ae1b45c1-764d-4507-8fe0-e52968d43c57' }) 
SET person_e52968d43c57.name = 'Roberto Quintero'
SET person_e52968d43c57.gender = 'Male'
SET person_e52968d43c57.source = 'musicbrainz.org'


MERGE (person_017082007047:Person{ uuid: '5f2472a7-50bd-4b2c-8178-017082007047' }) 
SET person_017082007047.name = 'Robert Rodriguez'
SET person_017082007047.gender = 'Male'
SET person_017082007047.disambiguation = 'piano'
SET person_017082007047.discogs = 'https://www.discogs.com/artist/575204'
SET person_017082007047.musicbrainz = 'https://musicbrainz.org/artist/5f2472a7-50bd-4b2c-8178-017082007047'
SET person_017082007047.source = 'musicbrainz.org'


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


MERGE (person_338556fa6693:Person{ uuid: '610a028f-aa19-43d4-afc0-338556fa6693' }) 
SET person_338556fa6693.name = 'Marcus Strickland'
SET person_338556fa6693.gender = 'Male'
SET person_338556fa6693.country = 'US'
SET person_338556fa6693.allmusic = 'https://www.allmusic.com/artist/mn0000569607'
SET person_338556fa6693.discogs = 'https://www.discogs.com/artist/659990'
SET person_338556fa6693.viaf = 'http://viaf.org/viaf/61273738'
SET person_338556fa6693.wikidata = 'https://www.wikidata.org/wiki/Q1894385'
SET person_338556fa6693.wikipedia = 'https://en.wikipedia.org/wiki/Marcus_Strickland'
SET person_338556fa6693.databases = ['http://d-nb.info/gnd/135244889', 'http://id.loc.gov/authorities/names/no2005025702', 'https://catalogue.bnf.fr/ark:/12148/cb150923392', 'https://www.worldcat.org/identities/lccn-no2005025702']
SET person_338556fa6693.musicbrainz = 'https://musicbrainz.org/artist/610a028f-aa19-43d4-afc0-338556fa6693'
SET person_338556fa6693.isni_list = ['http://isni.org/isni/0000000078480762']
SET person_338556fa6693.source = 'musicbrainz.org'


MERGE (person_fdfff1522b37:Person{ uuid: '816eedff-76ea-4d09-aabe-fdfff1522b37' }) 
SET person_fdfff1522b37.name = 'Doug Yoel'
SET person_fdfff1522b37.gender = 'Male'
SET person_fdfff1522b37.source = 'musicbrainz.org'


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
SET person_5a269b32b4c2.databases = ['http://d-nb.info/gnd/119238489', 'http://id.loc.gov/authorities/names/n81080890', 'https://catalogue.bnf.fr/ark:/12148/cb13892744v', 'https://rateyourmusic.com/artist/chick_corea', 'https://www.worldcat.org/identities/lccn-n81080890']
SET person_5a269b32b4c2.musicbrainz = 'https://musicbrainz.org/artist/8446fcca-109e-4c6d-a2ff-5a269b32b4c2'
SET person_5a269b32b4c2.isni_list = ['http://isni.org/isni/0000000121285074']
SET person_5a269b32b4c2.source = 'musicbrainz.org'

// labels

MERGE (label_45a4aac43b37:Label{ uuid: 'd3698a68-ef9f-431e-93a0-45a4aac43b37' })
SET label_45a4aac43b37.name= 'Dreyfus Jazz'

// performances

MERGE (perf_256d35662254:Performance{ uuid: 'eabdfc35-fe65-4cc5-917d-256d35662254' })
SET perf_256d35662254.name = 'Grand Street'
SET perf_256d35662254.duration = '5:59'
SET perf_256d35662254.begin_date = '2011-01-16'
SET perf_256d35662254.end_date = '2011-01-18'
SET perf_256d35662254.source = 'musicbrainz.org'


MERGE (perf_8f050c89224f:Performance{ uuid: '06338240-ea16-4459-b28e-8f050c89224f' })
SET perf_8f050c89224f.name = 'They Call The Wind Mariah'
SET perf_8f050c89224f.duration = '3:43'
SET perf_8f050c89224f.begin_date = '2011-01-16'
SET perf_8f050c89224f.end_date = '2011-01-18'
SET perf_8f050c89224f.source = 'musicbrainz.org'


MERGE (perf_0fc2cacfea1c:Performance{ uuid: '27485b77-7578-4806-a392-0fc2cacfea1c' })
SET perf_0fc2cacfea1c.name = 'Off Minor'
SET perf_0fc2cacfea1c.duration = '8:44'
SET perf_0fc2cacfea1c.begin_date = '2011-01-16'
SET perf_0fc2cacfea1c.end_date = '2011-01-18'
SET perf_0fc2cacfea1c.source = 'musicbrainz.org'


MERGE (perf_a55812840fcd:Performance{ uuid: '404d0bf6-e30c-4bf1-8a2a-a55812840fcd' })
SET perf_a55812840fcd.name = 'These Foolish Things'
SET perf_a55812840fcd.duration = '8:25'
SET perf_a55812840fcd.begin_date = '2011-01-16'
SET perf_a55812840fcd.end_date = '2011-01-18'
SET perf_a55812840fcd.source = 'musicbrainz.org'


MERGE (perf_464592892c18:Performance{ uuid: 'dc5070e6-7892-492e-ade8-464592892c18' })
SET perf_464592892c18.name = 'Milestones'
SET perf_464592892c18.duration = '5:31'
SET perf_464592892c18.begin_date = '2011-01-16'
SET perf_464592892c18.end_date = '2011-01-18'
SET perf_464592892c18.source = 'musicbrainz.org'


MERGE (perf_932007e853bd:Performance{ uuid: '112a8e3d-f8b3-4342-b36c-932007e853bd' })
SET perf_932007e853bd.name = 'Tin Tin Deo'
SET perf_932007e853bd.duration = '8:45'
SET perf_932007e853bd.begin_date = '2011-01-16'
SET perf_932007e853bd.end_date = '2011-01-18'
SET perf_932007e853bd.source = 'musicbrainz.org'


MERGE (perf_bea6434a5349:Performance{ uuid: '6de73e23-be46-4412-b5ea-bea6434a5349' })
SET perf_bea6434a5349.name = 'All The Bars Are Opens'
SET perf_bea6434a5349.duration = '7:46'
SET perf_bea6434a5349.begin_date = '2011-01-16'
SET perf_bea6434a5349.end_date = '2011-01-18'
SET perf_bea6434a5349.source = 'musicbrainz.org'


MERGE (perf_aadd9824071e:Performance{ uuid: 'c1a110b1-72aa-49ff-bb6a-aadd9824071e' })
SET perf_aadd9824071e.name = 'Pinky'
SET perf_aadd9824071e.duration = '3:53'
SET perf_aadd9824071e.begin_date = '2011-01-16'
SET perf_aadd9824071e.end_date = '2011-01-18'
SET perf_aadd9824071e.source = 'musicbrainz.org'


MERGE (perf_fd2b485aac42:Performance{ uuid: 'a69849d0-8380-4798-9352-fd2b485aac42' })
SET perf_fd2b485aac42.name = 'Equipoise'
SET perf_fd2b485aac42.duration = '6:50'
SET perf_fd2b485aac42.begin_date = '2011-01-16'
SET perf_fd2b485aac42.end_date = '2011-01-18'
SET perf_fd2b485aac42.source = 'musicbrainz.org'


MERGE (perf_f842db03718b:Performance{ uuid: '6fb087b7-5266-4a97-88c6-f842db03718b' })
SET perf_f842db03718b.name = 'Passion Dance'
SET perf_f842db03718b.duration = '7:02'
SET perf_f842db03718b.begin_date = '2011-01-16'
SET perf_f842db03718b.end_date = '2011-01-18'
SET perf_f842db03718b.source = 'musicbrainz.org'


MERGE (perf_e3cea1fb965b:Performance{ uuid: '22b25b22-cd9a-471b-880a-e3cea1fb965b' })
SET perf_e3cea1fb965b.name = 'Introspection (Bonus Track)'
SET perf_e3cea1fb965b.duration = '5:04'
SET perf_e3cea1fb965b.begin_date = '2011-01-16'
SET perf_e3cea1fb965b.end_date = '2011-01-18'
SET perf_e3cea1fb965b.source = 'musicbrainz.org'




// labels
MERGE (release_7a357fcf315a)-[:HAS_LABEL]->(label_45a4aac43b37)


// tracks
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_256d35662254)
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_8f050c89224f)
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_0fc2cacfea1c)
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_a55812840fcd)
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_464592892c18)
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_932007e853bd)
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_bea6434a5349)
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_aadd9824071e)
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_fd2b485aac42)
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_f842db03718b)
MERGE (release_7a357fcf315a)-[:HAS_TRACK {name: '11', sequence: 11}]->(perf_e3cea1fb965b)

// works

MERGE (person_5bf00afc3eaf:Person{ uuid: 'a13ede92-5e64-43ac-a5a6-5bf00afc3eaf' }) 
SET person_5bf00afc3eaf.name = 'Eric Maschwitz'
SET person_5bf00afc3eaf.gender = 'Male'
SET person_5bf00afc3eaf.country = 'GB'
SET person_5bf00afc3eaf.allmusic = 'https://www.allmusic.com/artist/mn0000824948'
SET person_5bf00afc3eaf.discogs = 'https://www.discogs.com/artist/669134'
SET person_5bf00afc3eaf.discogs = 'https://www.discogs.com/artist/693833'
SET person_5bf00afc3eaf.imdb = 'https://www.imdb.com/name/nm0556178/'
SET person_5bf00afc3eaf.viaf = 'http://viaf.org/viaf/23153688'
SET person_5bf00afc3eaf.wikidata = 'https://www.wikidata.org/wiki/Q1351469'
SET person_5bf00afc3eaf.wikipedia = 'https://en.wikipedia.org/wiki/Eric_Maschwitz'
SET person_5bf00afc3eaf.databases = ['http://d-nb.info/gnd/12715051X', 'https://catalogue.bnf.fr/ark:/12148/cb14768955v', 'https://openlibrary.org/works/OL2300851A']
SET person_5bf00afc3eaf.musicbrainz = 'https://musicbrainz.org/artist/a13ede92-5e64-43ac-a5a6-5bf00afc3eaf'
SET person_5bf00afc3eaf.isni_list = ['http://isni.org/isni/0000000109502208']
SET person_5bf00afc3eaf.source = 'musicbrainz.org'


MERGE (person_d5ce334cef0a:Person{ uuid: '1c8a91b9-5e5d-472a-bbc0-d5ce334cef0a' }) 
SET person_d5ce334cef0a.name = 'Jack Strachey'
SET person_d5ce334cef0a.gender = 'Male'
SET person_d5ce334cef0a.country = 'GB'
SET person_d5ce334cef0a.allmusic = 'https://www.allmusic.com/artist/mn0000104686'
SET person_d5ce334cef0a.discogs = 'https://www.discogs.com/artist/669136'
SET person_d5ce334cef0a.wikidata = 'https://www.wikidata.org/wiki/Q6115366'
SET person_d5ce334cef0a.wikipedia = 'https://en.wikipedia.org/wiki/Jack_Strachey'
SET person_d5ce334cef0a.databases = ['https://rateyourmusic.com/artist/jack_strachey']
SET person_d5ce334cef0a.musicbrainz = 'https://musicbrainz.org/artist/1c8a91b9-5e5d-472a-bbc0-d5ce334cef0a'
SET person_d5ce334cef0a.isni_list = ['http://isni.org/isni/0000000080871906']
SET person_d5ce334cef0a.source = 'musicbrainz.org'


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


MERGE (person_488eae967a08:Person{ uuid: 'd686b5cb-e00a-45c6-91c0-488eae967a08' }) 
SET person_488eae967a08.name = 'Walter “Gil” Fuller'
SET person_488eae967a08.gender = 'Male'
SET person_488eae967a08.disambiguation = 'jazz composer & arranger'
SET person_488eae967a08.country = 'US'
SET person_488eae967a08.allmusic = 'https://www.allmusic.com/artist/mn0000662080'
SET person_488eae967a08.allmusic = 'https://www.allmusic.com/artist/mn0002785554'
SET person_488eae967a08.discogs = 'https://www.discogs.com/artist/322262'
SET person_488eae967a08.wikidata = 'https://www.wikidata.org/wiki/Q1523819'
SET person_488eae967a08.databases = ['https://rateyourmusic.com/artist/gil_fuller']
SET person_488eae967a08.musicbrainz = 'https://musicbrainz.org/artist/d686b5cb-e00a-45c6-91c0-488eae967a08'
SET person_488eae967a08.isni_list = ['http://isni.org/isni/0000000055167861']
SET person_488eae967a08.source = 'musicbrainz.org'


MERGE (person_4869a613d37f:Person{ uuid: '673d3a45-5f49-4b5e-9910-4869a613d37f' }) 
SET person_4869a613d37f.name = 'Frederick Loewe'
SET person_4869a613d37f.gender = 'Male'
SET person_4869a613d37f.country = 'DE'
SET person_4869a613d37f.discogs = 'https://www.discogs.com/artist/418708'
SET person_4869a613d37f.imdb = 'https://www.imdb.com/name/nm0517350/'
SET person_4869a613d37f.viaf = 'http://viaf.org/viaf/84079242'
SET person_4869a613d37f.wikidata = 'https://www.wikidata.org/wiki/Q551678'
SET person_4869a613d37f.databases = ['http://d-nb.info/gnd/118573950', 'http://id.loc.gov/authorities/names/n50047986', 'https://catalogue.bnf.fr/ark:/12148/cb138967513', 'http://snaccooperative.org/ark:/99166/w6n29xkm', 'https://nla.gov.au/nla.party-1039355', 'https://openlibrary.org/works/OL857779A', 'https://www.ibdb.com/person.php?id=5688', 'https://www.worldcat.org/identities/lccn-n50047986']
SET person_4869a613d37f.musicbrainz = 'https://musicbrainz.org/artist/673d3a45-5f49-4b5e-9910-4869a613d37f'
SET person_4869a613d37f.isni_list = ['http://isni.org/isni/0000000117726690']
SET person_4869a613d37f.source = 'musicbrainz.org'


MERGE (person_8971e7a2912e:Person{ uuid: '22fe7b6f-af38-458e-87bd-8971e7a2912e' }) 
SET person_8971e7a2912e.name = 'McCoy Tyner'
SET person_8971e7a2912e.gender = 'Male'
SET person_8971e7a2912e.disambiguation = 'jazz pianist'
SET person_8971e7a2912e.country = 'US'
SET person_8971e7a2912e.allmusic = 'https://www.allmusic.com/artist/mn0000868092'
SET person_8971e7a2912e.bbc = 'https://www.bbc.co.uk/music/artists/22fe7b6f-af38-458e-87bd-8971e7a2912e'
SET person_8971e7a2912e.discogs = 'https://www.discogs.com/artist/10620'
SET person_8971e7a2912e.imdb = 'https://www.imdb.com/name/nm1743784/'
SET person_8971e7a2912e.viaf = 'http://viaf.org/viaf/84970893'
SET person_8971e7a2912e.wikidata = 'https://www.wikidata.org/wiki/Q318619'
SET person_8971e7a2912e.databases = ['http://d-nb.info/gnd/134543734', 'http://id.loc.gov/authorities/names/n81058256', 'https://catalogue.bnf.fr/ark:/12148/cb139006254', 'http://snaccooperative.org/ark:/99166/w6183cz4', 'https://www.worldcat.org/identities/lccn-n81-058256']
SET person_8971e7a2912e.musicbrainz = 'https://musicbrainz.org/artist/22fe7b6f-af38-458e-87bd-8971e7a2912e'
SET person_8971e7a2912e.isni_list = ['http://isni.org/isni/0000000120184511']
SET person_8971e7a2912e.source = 'musicbrainz.org'


MERGE (person_f2852d147c2e:Person{ uuid: '56b7ad8e-3c4f-4f14-914d-f2852d147c2e' }) 
SET person_f2852d147c2e.name = 'Alan Jay Lerner'
SET person_f2852d147c2e.gender = 'Male'
SET person_f2852d147c2e.country = 'US'
SET person_f2852d147c2e.discogs = 'https://www.discogs.com/artist/370715'
SET person_f2852d147c2e.imdb = 'https://www.imdb.com/name/nm0503585/'
SET person_f2852d147c2e.viaf = 'http://viaf.org/viaf/54336505'
SET person_f2852d147c2e.wikidata = 'https://www.wikidata.org/wiki/Q961893'
SET person_f2852d147c2e.databases = ['http://d-nb.info/gnd/119042967', 'http://id.loc.gov/authorities/names/n50050417', 'https://catalogue.bnf.fr/ark:/12148/cb13937266x', 'http://snaccooperative.org/ark:/99166/w6sf2wv5', 'https://nla.gov.au/nla.party-903408', 'https://openlibrary.org/works/OL579079A', 'https://www.ibdb.com/person.php?id=3945', 'https://www.worldcat.org/identities/lccn-n50050417']
SET person_f2852d147c2e.musicbrainz = 'https://musicbrainz.org/artist/56b7ad8e-3c4f-4f14-914d-f2852d147c2e'
SET person_f2852d147c2e.isni_list = ['http://isni.org/isni/0000000115708798']
SET person_f2852d147c2e.source = 'musicbrainz.org'


MERGE (person_f180a2b2aaf0:Person{ uuid: 'a569ac3b-f21b-4773-84a6-f180a2b2aaf0' }) 
SET person_f180a2b2aaf0.name = 'Stanley Cowell'
SET person_f180a2b2aaf0.gender = 'Male'
SET person_f180a2b2aaf0.country = 'US'
SET person_f180a2b2aaf0.allmusic = 'https://www.allmusic.com/artist/mn0000011303'
SET person_f180a2b2aaf0.discogs = 'https://www.discogs.com/artist/152684'
SET person_f180a2b2aaf0.imdb = 'https://www.imdb.com/name/nm0184714/'
SET person_f180a2b2aaf0.viaf = 'http://viaf.org/viaf/84970497'
SET person_f180a2b2aaf0.wikidata = 'https://www.wikidata.org/wiki/Q345934'
SET person_f180a2b2aaf0.databases = ['http://d-nb.info/gnd/134655648', 'http://id.loc.gov/authorities/names/n81149292', 'https://catalogue.bnf.fr/ark:/12148/cb13892810t', 'http://snaccooperative.org/ark:/99166/w6029r8m', 'https://www.worldcat.org/identities/lccn-n81149292']
SET person_f180a2b2aaf0.musicbrainz = 'https://musicbrainz.org/artist/a569ac3b-f21b-4773-84a6-f180a2b2aaf0'
SET person_f180a2b2aaf0.isni_list = ['http://isni.org/isni/0000000081607496']
SET person_f180a2b2aaf0.source = 'musicbrainz.org'


MERGE (person_afa0632abd19:Person{ uuid: '7c0e243d-30e5-472f-b5db-afa0632abd19' }) 
SET person_afa0632abd19.name = 'Harry Link'
SET person_afa0632abd19.gender = 'Male'
SET person_afa0632abd19.disambiguation = 'US vaudeville actor & songwriter'
SET person_afa0632abd19.country = 'US'
SET person_afa0632abd19.allmusic = 'https://www.allmusic.com/artist/mn0000664719'
SET person_afa0632abd19.discogs = 'https://www.discogs.com/artist/669135'
SET person_afa0632abd19.wikidata = 'https://www.wikidata.org/wiki/Q5670641'
SET person_afa0632abd19.wikipedia = 'https://en.wikipedia.org/wiki/Harry_Link'
SET person_afa0632abd19.musicbrainz = 'https://musicbrainz.org/artist/7c0e243d-30e5-472f-b5db-afa0632abd19'
SET person_afa0632abd19.isni_list = ['http://isni.org/isni/0000000109502857']
SET person_afa0632abd19.source = 'musicbrainz.org'


MERGE (person_fb68a00bad70:Person{ uuid: '505047e5-0398-426e-b22a-fb68a00bad70' }) 
SET person_fb68a00bad70.name = 'Chano Pozo'
SET person_fb68a00bad70.gender = 'Male'
SET person_fb68a00bad70.country = 'CU'
SET person_fb68a00bad70.allmusic = 'https://www.allmusic.com/artist/mn0000166796'
SET person_fb68a00bad70.discogs = 'https://www.discogs.com/artist/314413'
SET person_fb68a00bad70.viaf = 'http://viaf.org/viaf/74040239'
SET person_fb68a00bad70.wikidata = 'https://www.wikidata.org/wiki/Q1062320'
SET person_fb68a00bad70.wikipedia = 'https://en.wikipedia.org/wiki/Chano_Pozo'
SET person_fb68a00bad70.databases = ['https://rateyourmusic.com/artist/chano_pozo']
SET person_fb68a00bad70.musicbrainz = 'https://musicbrainz.org/artist/505047e5-0398-426e-b22a-fb68a00bad70'
SET person_fb68a00bad70.isni_list = ['http://isni.org/isni/0000000110295445']
SET person_fb68a00bad70.source = 'musicbrainz.org'


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
SET person_bad80243802a.databases = ['http://d-nb.info/gnd/118749552', 'http://id.loc.gov/authorities/names/n82144213', 'https://catalogue.bnf.fr/ark:/12148/cb138991337', 'http://snaccooperative.org/ark:/99166/w6bg2vq8', 'https://rateyourmusic.com/artist/sonny_rollins', 'https://www.musik-sammler.de/artist/sonny-rollins/', 'https://www.worldcat.org/identities/lccn-n82-144213']
SET person_bad80243802a.musicbrainz = 'https://musicbrainz.org/artist/3b47247e-5b57-49b6-a0ed-bad80243802a'
SET person_bad80243802a.isni_list = ['http://isni.org/isni/0000000110367920']
SET person_bad80243802a.source = 'musicbrainz.org'


MERGE (person_323e6ce46c2a:Person{ uuid: '561d854a-6a28-4aa7-8c99-323e6ce46c2a' }) 
SET person_323e6ce46c2a.name = 'Miles Davis'
SET person_323e6ce46c2a.gender = 'Male'
SET person_323e6ce46c2a.disambiguation = 'jazz trumpeter, bandleader, songwriter'
SET person_323e6ce46c2a.country = 'US'
SET person_323e6ce46c2a.allmusic = 'https://www.allmusic.com/artist/mn0000423829'
SET person_323e6ce46c2a.bbc = 'https://www.bbc.co.uk/music/artists/561d854a-6a28-4aa7-8c99-323e6ce46c2a'
SET person_323e6ce46c2a.discogs = 'https://www.discogs.com/artist/23755'
SET person_323e6ce46c2a.imdb = 'https://www.imdb.com/name/nm0002537/'
SET person_323e6ce46c2a.viaf = 'http://viaf.org/viaf/97762193'
SET person_323e6ce46c2a.wikidata = 'https://www.wikidata.org/wiki/Q93341'
SET person_323e6ce46c2a.databases = ['http://d-nb.info/gnd/118524046', 'http://id.loc.gov/authorities/names/n50035608', 'http://musicmoz.org/Bands_and_Artists/D/Davis,_Miles/', 'https://catalogue.bnf.fr/ark:/12148/cb13893030g', 'http://snaccooperative.org/ark:/99166/w68k7wq0', 'https://openlibrary.org/works/OL4359245A', 'https://rateyourmusic.com/artist/miles_davis', 'https://www.muziekweb.nl/Link/M00000286446/', 'https://www.worldcat.org/identities/lccn-n50035608', 'http://www.45cat.com/artist/miles-davis', 'http://www.45worlds.com/78rpm/artist/miles-davis', 'http://www.45worlds.com/cdalbum/artist/miles-davis', 'http://www.45worlds.com/live/artist/miles-davis', 'http://www.45worlds.com/tape/artist/miles-davis', 'http://www.45worlds.com/vinyl/artist/miles-davis']
SET person_323e6ce46c2a.musicbrainz = 'https://musicbrainz.org/artist/561d854a-6a28-4aa7-8c99-323e6ce46c2a'
SET person_323e6ce46c2a.isni_list = ['http://isni.org/isni/000000012144707X']
SET person_323e6ce46c2a.source = 'musicbrainz.org'


MERGE (work_0156522f107a:Work{ uuid: '4e8506d4-6c8e-339a-940c-0156522f107a' })
SET work_0156522f107a.name = 'Passion Dance'
SET work_0156522f107a.type = 'Song'
SET work_0156522f107a.source = 'musicbrainz.org'


MERGE (work_633f4a78d8bd:Work{ uuid: '70f39971-9897-4423-85bd-633f4a78d8bd' })
SET work_633f4a78d8bd.name = 'Grand Street'
SET work_633f4a78d8bd.iswc = 'T-071.572.139-3'
SET work_633f4a78d8bd.type = 'Song'
SET work_633f4a78d8bd.source = 'musicbrainz.org'


MERGE (work_14a23f4f5723:Work{ uuid: '3eb13fd1-40f9-441e-95bc-14a23f4f5723' })
SET work_14a23f4f5723.name = 'Off Minor'
SET work_14a23f4f5723.iswc = 'T-010.169.130-8'
SET work_14a23f4f5723.type = 'Song'
SET work_14a23f4f5723.source = 'musicbrainz.org'


MERGE (work_493e3e1ec02e:Work{ uuid: 'f69f9d65-c634-4635-9786-493e3e1ec02e' })
SET work_493e3e1ec02e.name = 'Equipoise'
SET work_493e3e1ec02e.type = 'Song'
SET work_493e3e1ec02e.source = 'musicbrainz.org'


MERGE (work_6dff23096b62:Work{ uuid: '8e897f2c-285a-327b-bb74-6dff23096b62' })
SET work_6dff23096b62.name = 'Milestones'
SET work_6dff23096b62.iswc = 'T-070.242.198-4'
SET work_6dff23096b62.type = 'Song'
SET work_6dff23096b62.wikidata = 'https://www.wikidata.org/wiki/Q1934679'
SET work_6dff23096b62.musicbrainz = 'https://musicbrainz.org/work/8e897f2c-285a-327b-bb74-6dff23096b62'
SET work_6dff23096b62.source = 'musicbrainz.org'


MERGE (work_f977bcd57451:Work{ uuid: '6261d6d4-caa9-31f0-8ab4-f977bcd57451' })
SET work_f977bcd57451.name = 'These Foolish Things (Remind Me of You)'
SET work_f977bcd57451.iswc = 'T-900.163.042-8'
SET work_f977bcd57451.type = 'Song'
SET work_f977bcd57451.wikidata = 'https://www.wikidata.org/wiki/Q780019'
SET work_f977bcd57451.musicbrainz = 'https://musicbrainz.org/work/6261d6d4-caa9-31f0-8ab4-f977bcd57451'
SET work_f977bcd57451.source = 'musicbrainz.org'


MERGE (work_5349dc063710:Work{ uuid: 'c1f2ac91-4c1c-48ce-9479-5349dc063710' })
SET work_5349dc063710.name = 'Tin Tin Deo'
SET work_5349dc063710.iswc = 'T-901.538.554-3'
SET work_5349dc063710.type = 'Song'
SET work_5349dc063710.musicbrainz = 'https://musicbrainz.org/work/c1f2ac91-4c1c-48ce-9479-5349dc063710'
SET work_5349dc063710.source = 'musicbrainz.org'


MERGE (work_f83dfba3a2df:Work{ uuid: 'a9fb3563-bb85-3037-b895-f83dfba3a2df' })
SET work_f83dfba3a2df.name = 'They Call the Wind Maria'
SET work_f83dfba3a2df.iswc = 'T-070.179.497-9'
SET work_f83dfba3a2df.type = 'Song'
SET work_f83dfba3a2df.wikidata = 'https://www.wikidata.org/wiki/Q7783665'
SET work_f83dfba3a2df.musicbrainz = 'https://musicbrainz.org/work/a9fb3563-bb85-3037-b895-f83dfba3a2df'
SET work_f83dfba3a2df.source = 'musicbrainz.org'



// performances of
MERGE (perf_f842db03718b)-[:PERFORMANCE_OF]->(work_0156522f107a)
MERGE (perf_256d35662254)-[:PERFORMANCE_OF]->(work_633f4a78d8bd)
MERGE (perf_0fc2cacfea1c)-[:PERFORMANCE_OF]->(work_14a23f4f5723)
MERGE (perf_fd2b485aac42)-[:PERFORMANCE_OF]->(work_493e3e1ec02e)
MERGE (perf_464592892c18)-[:PERFORMANCE_OF]->(work_6dff23096b62)
MERGE (perf_a55812840fcd)-[:PERFORMANCE_OF]->(work_f977bcd57451)
MERGE (perf_932007e853bd)-[:PERFORMANCE_OF]->(work_5349dc063710)
MERGE (perf_8f050c89224f)-[:PERFORMANCE_OF]->(work_f83dfba3a2df)


// composers
MERGE (person_8971e7a2912e)-[:COMPOSED]->(work_0156522f107a)
MERGE (person_bad80243802a)-[:COMPOSED]->(work_633f4a78d8bd)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_14a23f4f5723)
MERGE (person_f180a2b2aaf0)-[:COMPOSED]->(work_493e3e1ec02e)
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_6dff23096b62)
MERGE (person_d5ce334cef0a)-[:COMPOSED]->(work_f977bcd57451)
MERGE (person_afa0632abd19)-[:COMPOSED]->(work_f977bcd57451)
MERGE (person_5bf00afc3eaf)-[:WROTE_LYRICS]->(work_f977bcd57451)
MERGE (person_488eae967a08)-[:COMPOSED]->(work_5349dc063710)
MERGE (person_fb68a00bad70)-[:COMPOSED]->(work_5349dc063710)
MERGE (person_4869a613d37f)-[:COMPOSED]->(work_f83dfba3a2df)
MERGE (person_f2852d147c2e)-[:WROTE_LYRICS]->(work_f83dfba3a2df)


// place nodes

MERGE (place_a0051ba78758:Place{ uuid: '2cd039ba-e0a7-4c57-be1c-a0051ba78758' })
SET place_a0051ba78758.name = 'NRS Recording Studios'
SET place_a0051ba78758.source = 'musicbrainz.org'

MERGE (place_3a9fad8b26a6:Place{ uuid: '7cde5fff-fdb3-40d7-be6f-3a9fad8b26a6' })
SET place_3a9fad8b26a6.name = 'Skyline Studios'
SET place_3a9fad8b26a6.source = 'musicbrainz.org'


// place relationships
MERGE (perf_256d35662254)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_256d35662254)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)
MERGE (perf_8f050c89224f)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_8f050c89224f)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)
MERGE (perf_0fc2cacfea1c)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_0fc2cacfea1c)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)
MERGE (perf_a55812840fcd)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_a55812840fcd)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)
MERGE (perf_464592892c18)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_464592892c18)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)
MERGE (perf_932007e853bd)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_932007e853bd)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)
MERGE (perf_bea6434a5349)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_bea6434a5349)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)
MERGE (perf_aadd9824071e)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_aadd9824071e)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)
MERGE (perf_fd2b485aac42)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_fd2b485aac42)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)
MERGE (perf_f842db03718b)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_f842db03718b)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)
MERGE (perf_e3cea1fb965b)-[:HAS_PLACE { type: 'mixed at' }]->(place_a0051ba78758)
MERGE (perf_e3cea1fb965b)-[:HAS_PLACE { type: 'recorded at', begin_date: '2011-01-16', end_date: '2011-01-18' }]->(place_3a9fad8b26a6)

MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_256d35662254)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_256d35662254)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_256d35662254)
MERGE (person_db33730eb9a8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_256d35662254)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_256d35662254)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_256d35662254)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_8f050c89224f)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_8f050c89224f)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_8f050c89224f)
MERGE (person_db33730eb9a8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_8f050c89224f)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_8f050c89224f)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_8f050c89224f)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_0fc2cacfea1c)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_0fc2cacfea1c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_0fc2cacfea1c)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_0fc2cacfea1c)
MERGE (person_db33730eb9a8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_0fc2cacfea1c)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_0fc2cacfea1c)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_0fc2cacfea1c)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_a55812840fcd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_a55812840fcd)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_a55812840fcd)
MERGE (person_db33730eb9a8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a55812840fcd)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a55812840fcd)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_a55812840fcd)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_464592892c18)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_464592892c18)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_464592892c18)
MERGE (person_db33730eb9a8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_464592892c18)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_464592892c18)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_464592892c18)
MERGE (person_9fbfb804134b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_932007e853bd)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass', 'claves'] }]->(perf_932007e853bd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer', 'singer'], instruments: ['drums (drum set)'] }]->(perf_932007e853bd)
MERGE (person_e52968d43c57)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['congas', 'percussion'] }]->(perf_932007e853bd)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'shakers'] }]->(perf_932007e853bd)
MERGE (person_db33730eb9a8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_932007e853bd)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_932007e853bd)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_932007e853bd)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bea6434a5349)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_bea6434a5349)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_bea6434a5349)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_bea6434a5349)
MERGE (person_db33730eb9a8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_bea6434a5349)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_bea6434a5349)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_bea6434a5349)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_aadd9824071e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_aadd9824071e)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_aadd9824071e)
MERGE (person_db33730eb9a8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_aadd9824071e)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_aadd9824071e)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_aadd9824071e)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_fd2b485aac42)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_fd2b485aac42)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_fd2b485aac42)
MERGE (person_db33730eb9a8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_fd2b485aac42)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_fd2b485aac42)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_fd2b485aac42)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_f842db03718b)
MERGE (person_c69ca344fbf9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['congas'] }]->(perf_f842db03718b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_f842db03718b)
MERGE (person_017082007047)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f842db03718b)
MERGE (person_ae183779dae1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_f842db03718b)
MERGE (person_338556fa6693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_f842db03718b)
MERGE (person_db33730eb9a8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_f842db03718b)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_f842db03718b)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_f842db03718b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e3cea1fb965b)
MERGE (person_7d2af4d4d728)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_e3cea1fb965b)



"""
)