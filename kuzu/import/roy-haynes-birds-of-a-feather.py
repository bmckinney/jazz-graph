
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_221b69ac220c:Release{ uuid: '26e69872-e7dd-47d5-ba31-221b69ac220c' })
SET release_221b69ac220c.name = 'Birds of a Feather: A Tribute to Charlie Parker'
SET release_221b69ac220c.country = 'US'
SET release_221b69ac220c.date = '2001'
SET release_221b69ac220c.format = 'CD'
SET release_221b69ac220c.discode = 'FDM 36625-2'
SET release_221b69ac220c.discogs = 'https://www.discogs.com/release/7511108'
SET release_221b69ac220c.musicbrainz = 'http://musicbrainz.org/release/26e69872-e7dd-47d5-ba31-221b69ac220c'
SET release_221b69ac220c.source = 'musicbrainz.org'


MERGE (person_f8e34f4b8388:Person{ uuid: '54dc0f70-d729-4030-8e0c-f8e34f4b8388' }) 
SET person_f8e34f4b8388.name = 'Troy Halderson'
SET person_f8e34f4b8388.discogs = 'https://www.discogs.com/artist/476071'
SET person_f8e34f4b8388.musicbrainz = 'https://musicbrainz.org/artist/54dc0f70-d729-4030-8e0c-f8e34f4b8388'
SET person_f8e34f4b8388.source = 'musicbrainz.org'


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


MERGE (person_786008422061:Person{ uuid: 'd72e6ce3-641f-46a4-b5a7-786008422061' }) 
SET person_786008422061.name = 'Kenny Garrett'
SET person_786008422061.gender = 'Male'
SET person_786008422061.country = 'US'
SET person_786008422061.allmusic = 'https://www.allmusic.com/artist/mn0000767404'
SET person_786008422061.discogs = 'https://www.discogs.com/artist/55729'
SET person_786008422061.viaf = 'http://viaf.org/viaf/24791747'
SET person_786008422061.wikidata = 'https://www.wikidata.org/wiki/Q711059'
SET person_786008422061.databases = ['http://d-nb.info/gnd/134717678', 'http://id.loc.gov/authorities/names/nr91029864', 'https://catalogue.bnf.fr/ark:/12148/cb139411981', 'https://www.worldcat.org/identities/lccn-nr91029864']
SET person_786008422061.musicbrainz = 'https://musicbrainz.org/artist/d72e6ce3-641f-46a4-b5a7-786008422061'
SET person_786008422061.isni_list = ['http://isni.org/isni/0000000081038051']
SET person_786008422061.source = 'musicbrainz.org'


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


MERGE (person_be44af37c184:Person{ uuid: 'be8557cb-403f-40d6-b2bc-be44af37c184' }) 
SET person_be44af37c184.name = 'Don Sickler'
SET person_be44af37c184.gender = 'Male'
SET person_be44af37c184.country = 'US'
SET person_be44af37c184.allmusic = 'https://www.allmusic.com/artist/mn0000194331'
SET person_be44af37c184.discogs = 'https://www.discogs.com/artist/315595'
SET person_be44af37c184.viaf = 'http://viaf.org/viaf/19868511'
SET person_be44af37c184.wikidata = 'https://www.wikidata.org/wiki/Q1239507'
SET person_be44af37c184.wikipedia = 'https://en.wikipedia.org/wiki/Don_Sickler'
SET person_be44af37c184.databases = ['http://d-nb.info/gnd/1021050571', 'http://id.loc.gov/authorities/names/n91065899', 'https://catalogue.bnf.fr/ark:/12148/cb13927921p', 'https://www.worldcat.org/identities/lccn-n91065899']
SET person_be44af37c184.musicbrainz = 'https://musicbrainz.org/artist/be8557cb-403f-40d6-b2bc-be44af37c184'
SET person_be44af37c184.isni_list = ['http://isni.org/isni/0000000063090622']
SET person_be44af37c184.source = 'musicbrainz.org'


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


MERGE (person_e69b5939694a:Person{ uuid: '50403d09-df0f-4ec6-ab47-e69b5939694a' }) 
SET person_e69b5939694a.name = 'Jim Anderson'
SET person_e69b5939694a.gender = 'Male'
SET person_e69b5939694a.disambiguation = 'engineer'
SET person_e69b5939694a.country = 'US'
SET person_e69b5939694a.allmusic = 'https://www.allmusic.com/artist/mn0000334914'
SET person_e69b5939694a.allmusic = 'https://www.allmusic.com/artist/mn0001632502'
SET person_e69b5939694a.allmusic = 'https://www.allmusic.com/artist/mn0001969487'
SET person_e69b5939694a.discogs = 'https://www.discogs.com/artist/1623413'
SET person_e69b5939694a.discogs = 'https://www.discogs.com/artist/282077'
SET person_e69b5939694a.wikidata = 'https://www.wikidata.org/wiki/Q6193392'
SET person_e69b5939694a.databases = ['https://rateyourmusic.com/artist/jim_anderson_f1']
SET person_e69b5939694a.musicbrainz = 'https://musicbrainz.org/artist/50403d09-df0f-4ec6-ab47-e69b5939694a'
SET person_e69b5939694a.source = 'musicbrainz.org'

// labels

MERGE (label_45a4aac43b37:Label{ uuid: 'd3698a68-ef9f-431e-93a0-45a4aac43b37' })
SET label_45a4aac43b37.name= 'Dreyfus Jazz'

// performances

MERGE (perf_399a8c947308:Performance{ uuid: '23a1bae4-746c-4652-917a-399a8c947308' })
SET perf_399a8c947308.name = 'Diverse'
SET perf_399a8c947308.duration = '5:20'
SET perf_399a8c947308.begin_date = '2001-03-26'
SET perf_399a8c947308.end_date = '2001-03-27'
SET perf_399a8c947308.source = 'musicbrainz.org'


MERGE (perf_e3a12f4fd075:Performance{ uuid: '36ad905e-ec36-4d41-961b-e3a12f4fd075' })
SET perf_e3a12f4fd075.name = 'Ah Leu Cha'
SET perf_e3a12f4fd075.duration = '5:14'
SET perf_e3a12f4fd075.begin_date = '2001-03-26'
SET perf_e3a12f4fd075.end_date = '2001-03-27'
SET perf_e3a12f4fd075.source = 'musicbrainz.org'


MERGE (perf_33ca1aa8ddbc:Performance{ uuid: 'b0a34918-ac84-4876-9fd4-33ca1aa8ddbc' })
SET perf_33ca1aa8ddbc.name = 'April in Paris'
SET perf_33ca1aa8ddbc.duration = '5:15'
SET perf_33ca1aa8ddbc.begin_date = '2001-03-26'
SET perf_33ca1aa8ddbc.end_date = '2001-03-27'
SET perf_33ca1aa8ddbc.source = 'musicbrainz.org'


MERGE (perf_8bd8bf1dec01:Performance{ uuid: '7c33b8c3-45fa-4763-9957-8bd8bf1dec01' })
SET perf_8bd8bf1dec01.name = 'Moose the Mooch'
SET perf_8bd8bf1dec01.duration = '5:40'
SET perf_8bd8bf1dec01.begin_date = '2001-03-26'
SET perf_8bd8bf1dec01.end_date = '2001-03-27'
SET perf_8bd8bf1dec01.source = 'musicbrainz.org'


MERGE (perf_4e8823cca77d:Performance{ uuid: '09679a4e-7ed6-45b5-b8de-4e8823cca77d' })
SET perf_4e8823cca77d.name = 'Now\\'s the Time'
SET perf_4e8823cca77d.duration = '6:05'
SET perf_4e8823cca77d.begin_date = '2001-03-26'
SET perf_4e8823cca77d.end_date = '2001-03-27'
SET perf_4e8823cca77d.source = 'musicbrainz.org'


MERGE (perf_0034e5ea20d5:Performance{ uuid: '6bb9f845-4f12-48ec-abb3-0034e5ea20d5' })
SET perf_0034e5ea20d5.name = 'Rocker'
SET perf_0034e5ea20d5.duration = '6:02'
SET perf_0034e5ea20d5.begin_date = '2001-03-26'
SET perf_0034e5ea20d5.end_date = '2001-03-27'
SET perf_0034e5ea20d5.source = 'musicbrainz.org'


MERGE (perf_33073b8f7517:Performance{ uuid: '1b23ac3a-f09c-407f-885e-33073b8f7517' })
SET perf_33073b8f7517.name = 'Barbados'
SET perf_33073b8f7517.duration = '5:02'
SET perf_33073b8f7517.begin_date = '2001-03-26'
SET perf_33073b8f7517.end_date = '2001-03-27'
SET perf_33073b8f7517.source = 'musicbrainz.org'


MERGE (perf_2e5d707e695e:Performance{ uuid: '2acebd1f-70e0-41d1-b5c5-2e5d707e695e' })
SET perf_2e5d707e695e.name = 'Yardbird Suite'
SET perf_2e5d707e695e.duration = '4:48'
SET perf_2e5d707e695e.begin_date = '2001-03-26'
SET perf_2e5d707e695e.end_date = '2001-03-27'
SET perf_2e5d707e695e.source = 'musicbrainz.org'


MERGE (perf_e102a6fb774b:Performance{ uuid: 'f431f13d-d7fd-4592-8369-e102a6fb774b' })
SET perf_e102a6fb774b.name = 'The Gypsy'
SET perf_e102a6fb774b.duration = '6:44'
SET perf_e102a6fb774b.begin_date = '2001-03-26'
SET perf_e102a6fb774b.end_date = '2001-03-27'
SET perf_e102a6fb774b.source = 'musicbrainz.org'


MERGE (perf_4815ba011225:Performance{ uuid: 'ce4e95de-d552-4040-81c9-4815ba011225' })
SET perf_4815ba011225.name = 'My Heart Belongs to Daddy'
SET perf_4815ba011225.duration = '7:03'
SET perf_4815ba011225.begin_date = '2001-03-26'
SET perf_4815ba011225.end_date = '2001-03-27'
SET perf_4815ba011225.source = 'musicbrainz.org'


MERGE (perf_f053def5991d:Performance{ uuid: 'af6b7db2-a0a4-44c2-ab76-f053def5991d' })
SET perf_f053def5991d.name = 'What Is This Thing Called Love'
SET perf_f053def5991d.duration = '7:24'
SET perf_f053def5991d.begin_date = '2001-03-26'
SET perf_f053def5991d.end_date = '2001-03-27'
SET perf_f053def5991d.source = 'musicbrainz.org'




// labels
MERGE (release_221b69ac220c)-[:HAS_LABEL]->(label_45a4aac43b37)


// tracks
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_399a8c947308)
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_e3a12f4fd075)
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_33ca1aa8ddbc)
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_8bd8bf1dec01)
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_4e8823cca77d)
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_0034e5ea20d5)
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_33073b8f7517)
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_2e5d707e695e)
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_e102a6fb774b)
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_4815ba011225)
MERGE (release_221b69ac220c)-[:HAS_TRACK {name: '11', sequence: 11}]->(perf_f053def5991d)

// works

MERGE (person_71aaf0f6b267:Person{ uuid: '68f19808-1f7b-46d4-bd1d-71aaf0f6b267' }) 
SET person_71aaf0f6b267.name = 'Gerry Mulligan'
SET person_71aaf0f6b267.gender = 'Male'
SET person_71aaf0f6b267.country = 'US'
SET person_71aaf0f6b267.allmusic = 'https://www.allmusic.com/artist/mn0000542549'
SET person_71aaf0f6b267.bbc = 'https://www.bbc.co.uk/music/artists/68f19808-1f7b-46d4-bd1d-71aaf0f6b267'
SET person_71aaf0f6b267.discogs = 'https://www.discogs.com/artist/37733'
SET person_71aaf0f6b267.imdb = 'https://www.imdb.com/name/nm0612302/'
SET person_71aaf0f6b267.viaf = 'http://viaf.org/viaf/22328253'
SET person_71aaf0f6b267.wikidata = 'https://www.wikidata.org/wiki/Q156535'
SET person_71aaf0f6b267.databases = ['http://d-nb.info/gnd/134469100', 'http://id.loc.gov/authorities/names/n82153045', 'https://catalogue.bnf.fr/ark:/12148/cb138977969', 'https://ibdb.com/person.php?id=107163', 'http://snaccooperative.org/ark:/99166/w66m3d6p', 'https://nla.gov.au/nla.party-910559', 'https://rateyourmusic.com/artist/gerry_mulligan', 'https://www.musik-sammler.de/artist/gerry-mulligan/', 'https://www.worldcat.org/identities/lccn-n82153045']
SET person_71aaf0f6b267.musicbrainz = 'https://musicbrainz.org/artist/68f19808-1f7b-46d4-bd1d-71aaf0f6b267'
SET person_71aaf0f6b267.isni_list = ['http://isni.org/isni/0000000081014850']
SET person_71aaf0f6b267.source = 'musicbrainz.org'


MERGE (person_a956823443d6:Person{ uuid: 'd1df7704-378a-4ae2-9f1b-a956823443d6' }) 
SET person_a956823443d6.name = 'Billy Reid'
SET person_a956823443d6.gender = 'Male'
SET person_a956823443d6.disambiguation = 'UK orchestra leader and songwriter'
SET person_a956823443d6.country = 'GB'
SET person_a956823443d6.discogs = 'https://www.discogs.com/artist/818580'
SET person_a956823443d6.wikidata = 'https://www.wikidata.org/wiki/Q4913224'
SET person_a956823443d6.musicbrainz = 'https://musicbrainz.org/artist/d1df7704-378a-4ae2-9f1b-a956823443d6'
SET person_a956823443d6.source = 'musicbrainz.org'


MERGE (person_6a07564b5394:Person{ uuid: '794e6b10-e8e2-4fb1-9013-6a07564b5394' }) 
SET person_6a07564b5394.name = 'Vernon Duke'
SET person_6a07564b5394.gender = 'Male'
SET person_6a07564b5394.country = 'US'
SET person_6a07564b5394.allmusic = 'https://www.allmusic.com/artist/mn0000095859'
SET person_6a07564b5394.discogs = 'https://www.discogs.com/artist/614342'
SET person_6a07564b5394.imdb = 'https://www.imdb.com/name/nm0241216/'
SET person_6a07564b5394.viaf = 'http://viaf.org/viaf/51891012'
SET person_6a07564b5394.wikidata = 'https://www.wikidata.org/wiki/Q519693'
SET person_6a07564b5394.databases = ['http://d-nb.info/gnd/10382247X', 'http://id.loc.gov/authorities/names/n80125365', 'https://catalogue.bnf.fr/ark:/12148/cb14044916c', 'https://ibdb.com/person.php?id=8943', 'http://snaccooperative.org/ark:/99166/w6280g8k', 'https://nla.gov.au/nla.party-1525253', 'https://openlibrary.org/works/OL2274232A', 'https://rateyourmusic.com/artist/vernon_duke', 'https://www.worldcat.org/identities/lccn-n80125365/']
SET person_6a07564b5394.musicbrainz = 'https://musicbrainz.org/artist/794e6b10-e8e2-4fb1-9013-6a07564b5394'
SET person_6a07564b5394.isni_list = ['http://isni.org/isni/0000000081307426']
SET person_6a07564b5394.source = 'musicbrainz.org'


MERGE (person_cabff6fab531:Person{ uuid: '42e52c03-27bb-4545-8924-cabff6fab531' }) 
SET person_cabff6fab531.name = 'Yip Harburg'
SET person_cabff6fab531.gender = 'Male'
SET person_cabff6fab531.country = 'US'
SET person_cabff6fab531.allmusic = 'https://www.allmusic.com/artist/mn0000806535'
SET person_cabff6fab531.discogs = 'https://www.discogs.com/artist/573556'
SET person_cabff6fab531.imdb = 'https://www.imdb.com/name/nm0361971/'
SET person_cabff6fab531.viaf = 'http://viaf.org/viaf/120709724'
SET person_cabff6fab531.wikidata = 'https://www.wikidata.org/wiki/Q1273621'
SET person_cabff6fab531.databases = ['http://d-nb.info/gnd/11919158X', 'http://id.loc.gov/authorities/names/n85342788', 'https://catalogue.bnf.fr/ark:/12148/cb13798046w', 'https://ibdb.com/person.php?id=5177', 'http://snaccooperative.org/ark:/99166/w6q9253m', 'https://nla.gov.au/nla.party-877568', 'https://openlibrary.org/works/OL6933834A', 'https://rateyourmusic.com/artist/e_y__yip_harburg', 'https://www.worldcat.org/identities/lccn-n85342788/']
SET person_cabff6fab531.musicbrainz = 'https://musicbrainz.org/artist/42e52c03-27bb-4545-8924-cabff6fab531'
SET person_cabff6fab531.isni_list = ['http://isni.org/isni/0000000117013279', 'http://isni.org/isni/0000000372914779']
SET person_cabff6fab531.source = 'musicbrainz.org'


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


MERGE (work_2a1757f513bf:Work{ uuid: '7b1251db-40e7-391e-9680-2a1757f513bf' })
SET work_2a1757f513bf.name = 'The Gypsy'
SET work_2a1757f513bf.iswc = 'T-010.323.210-5'
SET work_2a1757f513bf.type = 'Song'
SET work_2a1757f513bf.wikidata = 'https://www.wikidata.org/wiki/Q2372232'
SET work_2a1757f513bf.musicbrainz = 'https://musicbrainz.org/work/7b1251db-40e7-391e-9680-2a1757f513bf'
SET work_2a1757f513bf.source = 'musicbrainz.org'


MERGE (work_54a7cadb9ccc:Work{ uuid: 'c3cfa4f9-e429-3599-a3b0-54a7cadb9ccc' })
SET work_54a7cadb9ccc.name = 'Yardbird Suite'
SET work_54a7cadb9ccc.wikidata = 'https://www.wikidata.org/wiki/Q4353511'
SET work_54a7cadb9ccc.musicbrainz = 'https://musicbrainz.org/work/c3cfa4f9-e429-3599-a3b0-54a7cadb9ccc'
SET work_54a7cadb9ccc.source = 'musicbrainz.org'


MERGE (work_4d4f5066e485:Work{ uuid: '2adc274e-85ba-3620-91b8-4d4f5066e485' })
SET work_4d4f5066e485.name = 'April in Paris'
SET work_4d4f5066e485.iswc = 'T-070.882.094-3'
SET work_4d4f5066e485.type = 'Song'
SET work_4d4f5066e485.wikidata = 'https://www.wikidata.org/wiki/Q4355132'
SET work_4d4f5066e485.musicbrainz = 'https://musicbrainz.org/work/2adc274e-85ba-3620-91b8-4d4f5066e485'
SET work_4d4f5066e485.source = 'musicbrainz.org'


MERGE (work_cbf706729862:Work{ uuid: 'e8e34f28-f9f2-32bf-a0c7-cbf706729862' })
SET work_cbf706729862.name = 'Now’s the Time'
SET work_cbf706729862.iswc = 'T-070.242.588-4'
SET work_cbf706729862.type = 'Song'
SET work_cbf706729862.source = 'musicbrainz.org'


MERGE (work_b69b8384c8ff:Work{ uuid: '8e1a20a2-9894-490b-aa0a-b69b8384c8ff' })
SET work_b69b8384c8ff.name = 'Barbados'
SET work_b69b8384c8ff.iswc = 'T-070.880.744-6'
SET work_b69b8384c8ff.type = 'Song'
SET work_b69b8384c8ff.musicbrainz = 'https://musicbrainz.org/work/8e1a20a2-9894-490b-aa0a-b69b8384c8ff'
SET work_b69b8384c8ff.source = 'musicbrainz.org'


MERGE (work_01f1b65c688e:Work{ uuid: 'f913cde7-5418-3a1d-bbe5-01f1b65c688e' })
SET work_01f1b65c688e.name = 'My Heart Belongs to Daddy'
SET work_01f1b65c688e.iswc = 'T-070.110.901-4'
SET work_01f1b65c688e.type = 'Song'
SET work_01f1b65c688e.wikidata = 'https://www.wikidata.org/wiki/Q3137581'
SET work_01f1b65c688e.databases = ['https://castalbums.org/songs/My-Heart-Belongs-to-Daddy/27281/']
SET work_01f1b65c688e.musicbrainz = 'https://musicbrainz.org/work/f913cde7-5418-3a1d-bbe5-01f1b65c688e'
SET work_01f1b65c688e.source = 'musicbrainz.org'


MERGE (work_d72f024ce580:Work{ uuid: 'c9bda91e-8400-313f-8c93-d72f024ce580' })
SET work_d72f024ce580.name = 'Moose the Mooche'
SET work_d72f024ce580.musicbrainz = 'https://musicbrainz.org/work/c9bda91e-8400-313f-8c93-d72f024ce580'
SET work_d72f024ce580.source = 'musicbrainz.org'


MERGE (work_8e3b4ea1176b:Work{ uuid: '790c02d2-b392-4a4e-8b2e-8e3b4ea1176b' })
SET work_8e3b4ea1176b.name = 'Ah-Leu-Cha'
SET work_8e3b4ea1176b.iswc = 'T-010.320.310-6'
SET work_8e3b4ea1176b.type = 'Song'
SET work_8e3b4ea1176b.wikidata = 'https://www.wikidata.org/wiki/Q4694845'
SET work_8e3b4ea1176b.musicbrainz = 'https://musicbrainz.org/work/790c02d2-b392-4a4e-8b2e-8e3b4ea1176b'
SET work_8e3b4ea1176b.source = 'musicbrainz.org'


MERGE (work_d30ab24f9f3e:Work{ uuid: '70eb376f-0fbb-324c-9dcb-d30ab24f9f3e' })
SET work_d30ab24f9f3e.name = 'What Is This Thing Called Love?'
SET work_d30ab24f9f3e.iswc = 'T-070.198.566-1'
SET work_d30ab24f9f3e.type = 'Song'
SET work_d30ab24f9f3e.wikidata = 'https://www.wikidata.org/wiki/Q860211'
SET work_d30ab24f9f3e.musicbrainz = 'https://musicbrainz.org/work/70eb376f-0fbb-324c-9dcb-d30ab24f9f3e'
SET work_d30ab24f9f3e.source = 'musicbrainz.org'


MERGE (work_da6e0329a6b9:Work{ uuid: '4480f8cc-d991-30a3-af5e-da6e0329a6b9' })
SET work_da6e0329a6b9.name = 'Diverse'
SET work_da6e0329a6b9.iswc = 'T-700.009.644-8'
SET work_da6e0329a6b9.type = 'Song'
SET work_da6e0329a6b9.source = 'musicbrainz.org'


MERGE (work_f6ba8cf28d17:Work{ uuid: '3d6f428c-5b7d-489d-852b-f6ba8cf28d17' })
SET work_f6ba8cf28d17.name = 'Rocker'
SET work_f6ba8cf28d17.iswc = 'T-070.126.974-0'
SET work_f6ba8cf28d17.type = 'Song'
SET work_f6ba8cf28d17.source = 'musicbrainz.org'



// performances of
MERGE (perf_e102a6fb774b)-[:PERFORMANCE_OF]->(work_2a1757f513bf)
MERGE (perf_2e5d707e695e)-[:PERFORMANCE_OF]->(work_54a7cadb9ccc)
MERGE (perf_33ca1aa8ddbc)-[:PERFORMANCE_OF]->(work_4d4f5066e485)
MERGE (perf_4e8823cca77d)-[:PERFORMANCE_OF]->(work_cbf706729862)
MERGE (perf_33073b8f7517)-[:PERFORMANCE_OF]->(work_b69b8384c8ff)
MERGE (perf_4815ba011225)-[:PERFORMANCE_OF]->(work_01f1b65c688e)
MERGE (perf_8bd8bf1dec01)-[:PERFORMANCE_OF]->(work_d72f024ce580)
MERGE (perf_e3a12f4fd075)-[:PERFORMANCE_OF]->(work_8e3b4ea1176b)
MERGE (perf_f053def5991d)-[:PERFORMANCE_OF]->(work_d30ab24f9f3e)
MERGE (perf_399a8c947308)-[:PERFORMANCE_OF]->(work_da6e0329a6b9)
MERGE (perf_0034e5ea20d5)-[:PERFORMANCE_OF]->(work_f6ba8cf28d17)


// composers
MERGE (person_a956823443d6)-[:COMPOSED]->(work_2a1757f513bf)
MERGE (person_a956823443d6)-[:WROTE_LYRICS]->(work_2a1757f513bf)
MERGE (person_c73775716312)-[:COMPOSED]->(work_54a7cadb9ccc)
MERGE (person_6a07564b5394)-[:COMPOSED]->(work_4d4f5066e485)
MERGE (person_cabff6fab531)-[:WROTE_LYRICS]->(work_4d4f5066e485)
MERGE (person_c73775716312)-[:COMPOSED]->(work_cbf706729862)
MERGE (person_c73775716312)-[:COMPOSED]->(work_b69b8384c8ff)
MERGE (person_a37897b950ce)-[:COMPOSED]->(work_01f1b65c688e)
MERGE (person_a37897b950ce)-[:WROTE_LYRICS]->(work_01f1b65c688e)
MERGE (person_c73775716312)-[:COMPOSED]->(work_d72f024ce580)
MERGE (person_c73775716312)-[:COMPOSED]->(work_8e3b4ea1176b)
MERGE (person_a37897b950ce)-[:COMPOSED]->(work_d30ab24f9f3e)
MERGE (person_a37897b950ce)-[:WROTE_LYRICS]->(work_d30ab24f9f3e)
MERGE (person_71aaf0f6b267)-[:COMPOSED]->(work_f6ba8cf28d17)


// place nodes

MERGE (place_045855c0a0d4:Place{ uuid: 'd4fb6481-b2cd-434d-aa71-045855c0a0d4' })
SET place_045855c0a0d4.name = 'Manhattan Center Studios'
SET place_045855c0a0d4.source = 'musicbrainz.org'

MERGE (place_8d4d9825e5a9:Place{ uuid: '7ad2d698-0e3a-413c-a239-8d4d9825e5a9' })
SET place_8d4d9825e5a9.name = 'Clinton Recording Studios'
SET place_8d4d9825e5a9.source = 'musicbrainz.org'


// place relationships
MERGE (perf_399a8c947308)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_399a8c947308)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)
MERGE (perf_e3a12f4fd075)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_e3a12f4fd075)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)
MERGE (perf_33ca1aa8ddbc)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_33ca1aa8ddbc)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)
MERGE (perf_8bd8bf1dec01)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_8bd8bf1dec01)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)
MERGE (perf_4e8823cca77d)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_4e8823cca77d)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)
MERGE (perf_0034e5ea20d5)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_0034e5ea20d5)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)
MERGE (perf_33073b8f7517)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_33073b8f7517)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)
MERGE (perf_2e5d707e695e)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_2e5d707e695e)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)
MERGE (perf_e102a6fb774b)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_e102a6fb774b)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)
MERGE (perf_4815ba011225)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_4815ba011225)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)
MERGE (perf_f053def5991d)-[:HAS_PLACE { type: 'mixed at' }]->(place_045855c0a0d4)
MERGE (perf_f053def5991d)-[:HAS_PLACE { type: 'recorded at', begin_date: '2001-03-26', end_date: '2001-03-27' }]->(place_8d4d9825e5a9)

MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_399a8c947308)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_399a8c947308)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_399a8c947308)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_399a8c947308)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_399a8c947308)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_399a8c947308)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_e3a12f4fd075)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_e3a12f4fd075)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_e3a12f4fd075)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e3a12f4fd075)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e3a12f4fd075)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e3a12f4fd075)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_33ca1aa8ddbc)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_33ca1aa8ddbc)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_33ca1aa8ddbc)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_33ca1aa8ddbc)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_33ca1aa8ddbc)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_33ca1aa8ddbc)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_8bd8bf1dec01)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_8bd8bf1dec01)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_8bd8bf1dec01)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_8bd8bf1dec01)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8bd8bf1dec01)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_8bd8bf1dec01)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_4e8823cca77d)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_4e8823cca77d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_4e8823cca77d)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_4e8823cca77d)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_4e8823cca77d)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_4e8823cca77d)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_0034e5ea20d5)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_0034e5ea20d5)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_0034e5ea20d5)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_0034e5ea20d5)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_0034e5ea20d5)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_0034e5ea20d5)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_33073b8f7517)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_33073b8f7517)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_33073b8f7517)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_33073b8f7517)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_33073b8f7517)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_33073b8f7517)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_2e5d707e695e)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_2e5d707e695e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_2e5d707e695e)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_2e5d707e695e)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2e5d707e695e)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_2e5d707e695e)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_e102a6fb774b)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_e102a6fb774b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_e102a6fb774b)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e102a6fb774b)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e102a6fb774b)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e102a6fb774b)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_4815ba011225)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_4815ba011225)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_4815ba011225)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_4815ba011225)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_4815ba011225)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_4815ba011225)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_f053def5991d)
MERGE (person_e552e95b3414)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_f053def5991d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_f053def5991d)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_f053def5991d)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f053def5991d)
MERGE (person_be44af37c184)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_f053def5991d)



"""
)