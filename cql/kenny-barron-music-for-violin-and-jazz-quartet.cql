// releases

MERGE (release_216bbc6ca2eb:Release{ uuid: '7c5c726a-e78f-43e3-b73f-216bbc6ca2eb' })
SET release_216bbc6ca2eb.name = 'Music for Violin & Jazz Quartet'
SET release_216bbc6ca2eb.country = 'US'
SET release_216bbc6ca2eb.date = '1981'
SET release_216bbc6ca2eb.format = '12" Vinyl'
SET release_216bbc6ca2eb.discode = 'JAM#001'
SET release_216bbc6ca2eb.musicbrainz = 'http://musicbrainz.org/release/7c5c726a-e78f-43e3-b73f-216bbc6ca2eb'
SET release_216bbc6ca2eb.source = 'musicbrainz.org'
SET release_216bbc6ca2eb.timestamp = timestamp()

MERGE (person_d085d92bc7d8:Person{ uuid: 'e9e9e70d-0fa4-44d6-a029-d085d92bc7d8' }) 
SET person_d085d92bc7d8.name = 'Michael Cuscuna'
SET person_d085d92bc7d8.gender = 'Male'
SET person_d085d92bc7d8.country = 'US'
SET person_d085d92bc7d8.discogs = 'https://www.discogs.com/artist/252960'
SET person_d085d92bc7d8.viaf = 'http://viaf.org/viaf/32110948'
SET person_d085d92bc7d8.wikidata = 'https://www.wikidata.org/wiki/Q786553'
SET person_d085d92bc7d8.wikipedia = 'https://en.wikipedia.org/wiki/Michael_Cuscuna'
SET person_d085d92bc7d8.databases = ['https://catalogue.bnf.fr/ark:/12148/cb12545629q']
SET person_d085d92bc7d8.musicbrainz = 'https://musicbrainz.org/artist/e9e9e70d-0fa4-44d6-a029-d085d92bc7d8'
SET person_d085d92bc7d8.isni_list = ['http://isni.org/isni/0000000063070488', 'http://isni.org/isni/0000000406937662']
SET person_d085d92bc7d8.source = 'musicbrainz.org'
SET person_d085d92bc7d8.timestamp = timestamp()

MERGE (person_3d9cd1a604da:Person{ uuid: '1c1b612c-484c-4794-9a0f-3d9cd1a604da' }) 
SET person_3d9cd1a604da.name = 'David Stone'
SET person_3d9cd1a604da.gender = 'Male'
SET person_3d9cd1a604da.disambiguation = 'engineer'
SET person_3d9cd1a604da.country = 'US'
SET person_3d9cd1a604da.discogs = 'https://www.discogs.com/artist/245493'
SET person_3d9cd1a604da.databases = ['https://rateyourmusic.com/artist/david_stone_f1/credits/']
SET person_3d9cd1a604da.musicbrainz = 'https://musicbrainz.org/artist/1c1b612c-484c-4794-9a0f-3d9cd1a604da'
SET person_3d9cd1a604da.source = 'musicbrainz.org'
SET person_3d9cd1a604da.timestamp = timestamp()

MERGE (person_374a4ea7c1b7:Person{ uuid: '2a139e3e-2e07-4246-8aac-374a4ea7c1b7' }) 
SET person_374a4ea7c1b7.name = 'NY5'
SET person_374a4ea7c1b7.discogs = 'https://www.discogs.com/artist/2664723'
SET person_374a4ea7c1b7.musicbrainz = 'https://musicbrainz.org/artist/2a139e3e-2e07-4246-8aac-374a4ea7c1b7'
SET person_374a4ea7c1b7.source = 'musicbrainz.org'
SET person_374a4ea7c1b7.timestamp = timestamp()

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
SET person_6f0a331cc1ca.timestamp = timestamp()

MERGE (person_ed7ff1a15814:Person{ uuid: 'dbcce19d-0651-47db-87dd-ed7ff1a15814' }) 
SET person_ed7ff1a15814.name = 'B.J. Miranda'
SET person_ed7ff1a15814.discogs = 'https://www.discogs.com/artist/2664724'
SET person_ed7ff1a15814.musicbrainz = 'https://musicbrainz.org/artist/dbcce19d-0651-47db-87dd-ed7ff1a15814'
SET person_ed7ff1a15814.source = 'musicbrainz.org'
SET person_ed7ff1a15814.timestamp = timestamp()

MERGE (person_10c607803ac5:Person{ uuid: 'a61d8b20-9df6-4f05-81c2-10c607803ac5' }) 
SET person_10c607803ac5.name = 'Buster Williams'
SET person_10c607803ac5.gender = 'Male'
SET person_10c607803ac5.disambiguation = 'US jazz bassist'
SET person_10c607803ac5.country = 'US'
SET person_10c607803ac5.allmusic = 'https://www.allmusic.com/artist/mn0000943189'
SET person_10c607803ac5.discogs = 'https://www.discogs.com/artist/320106'
SET person_10c607803ac5.discogs = 'https://www.discogs.com/artist/74212'
SET person_10c607803ac5.imdb = 'https://www.imdb.com/name/nm1659287/'
SET person_10c607803ac5.viaf = 'http://viaf.org/viaf/119691195'
SET person_10c607803ac5.wikidata = 'https://www.wikidata.org/wiki/Q1017782'
SET person_10c607803ac5.databases = ['http://id.loc.gov/authorities/names/n80093136', 'https://catalogue.bnf.fr/ark:/12148/cb13901173v', 'https://d-nb.info/gnd/134557417', 'https://www.worldcat.org/identities/lccn-n80093136']
SET person_10c607803ac5.musicbrainz = 'https://musicbrainz.org/artist/a61d8b20-9df6-4f05-81c2-10c607803ac5'
SET person_10c607803ac5.isni_list = ['http://isni.org/isni/0000000115806822']
SET person_10c607803ac5.source = 'musicbrainz.org'
SET person_10c607803ac5.timestamp = timestamp()

MERGE (person_59c853a902ab:Person{ uuid: 'f242ab91-985f-44c8-a996-59c853a902ab' }) 
SET person_59c853a902ab.name = 'Ted Dunbar'
SET person_59c853a902ab.gender = 'Male'
SET person_59c853a902ab.country = 'US'
SET person_59c853a902ab.allmusic = 'https://www.allmusic.com/artist/mn0000026822'
SET person_59c853a902ab.discogs = 'https://www.discogs.com/artist/298014'
SET person_59c853a902ab.viaf = 'http://viaf.org/viaf/56798482'
SET person_59c853a902ab.wikidata = 'https://www.wikidata.org/wiki/Q2399762'
SET person_59c853a902ab.wikipedia = 'https://en.wikipedia.org/wiki/Ted_Dunbar'
SET person_59c853a902ab.databases = ['http://id.loc.gov/authorities/names/n88021897', 'https://catalogue.bnf.fr/ark:/12148/cb13925537g', 'https://d-nb.info/gnd/134787447', 'https://rateyourmusic.com/artist/ted_dunbar', 'https://www.worldcat.org/identities/lccn-n88021897']
SET person_59c853a902ab.musicbrainz = 'https://musicbrainz.org/artist/f242ab91-985f-44c8-a996-59c853a902ab'
SET person_59c853a902ab.isni_list = ['http://isni.org/isni/0000000072484957']
SET person_59c853a902ab.source = 'musicbrainz.org'
SET person_59c853a902ab.timestamp = timestamp()

MERGE (person_120e386da267:Person{ uuid: '6b2e6e7c-4289-447c-a3dc-120e386da267' }) 
SET person_120e386da267.name = 'Kenny Barron'
SET person_120e386da267.gender = 'Male'
SET person_120e386da267.country = 'US'
SET person_120e386da267.allmusic = 'https://www.allmusic.com/artist/mn0000081181'
SET person_120e386da267.discogs = 'https://www.discogs.com/artist/65746'
SET person_120e386da267.imdb = 'https://www.imdb.com/name/nm0057686/'
SET person_120e386da267.viaf = 'http://viaf.org/viaf/119903038'
SET person_120e386da267.wikidata = 'https://www.wikidata.org/wiki/Q489233'
SET person_120e386da267.databases = ['http://id.loc.gov/authorities/names/n80124274', 'https://catalogue.bnf.fr/ark:/12148/cb13891186w', 'https://d-nb.info/gnd/134321804', 'http://snaccooperative.org/ark:/99166/w6c5871b', 'https://rateyourmusic.com/artist/kenny_barron', 'https://www.musik-sammler.de/artist/kenny-barron/', 'https://www.worldcat.org/identities/lccn-n80124274']
SET person_120e386da267.musicbrainz = 'https://musicbrainz.org/artist/6b2e6e7c-4289-447c-a3dc-120e386da267'
SET person_120e386da267.isni_list = ['http://isni.org/isni/0000000081889024']
SET person_120e386da267.source = 'musicbrainz.org'
SET person_120e386da267.timestamp = timestamp()

MERGE (person_7de6a3ee9b77:Person{ uuid: 'c9bda94f-d379-4405-a20e-7de6a3ee9b77' }) 
SET person_7de6a3ee9b77.name = 'Michał Urbaniak'
SET person_7de6a3ee9b77.gender = 'Male'
SET person_7de6a3ee9b77.country = 'PL'
SET person_7de6a3ee9b77.allmusic = 'https://www.allmusic.com/artist/mn0000889276'
SET person_7de6a3ee9b77.discogs = 'https://www.discogs.com/artist/455886'
SET person_7de6a3ee9b77.imdb = 'https://www.imdb.com/name/nm0881673/'
SET person_7de6a3ee9b77.viaf = 'http://viaf.org/viaf/32184869'
SET person_7de6a3ee9b77.wikidata = 'https://www.wikidata.org/wiki/Q599896'
SET person_7de6a3ee9b77.wikipedia = 'https://en.wikipedia.org/wiki/Micha%C5%82_Urbaniak'
SET person_7de6a3ee9b77.databases = ['http://id.loc.gov/authorities/names/n88664878', 'https://catalogue.bnf.fr/ark:/12148/cb139006463', 'https://d-nb.info/gnd/134544560', 'https://rateyourmusic.com/artist/michal-urbaniak-1', 'https://www.worldcat.org/identities/lccn-n88664878']
SET person_7de6a3ee9b77.musicbrainz = 'https://musicbrainz.org/artist/c9bda94f-d379-4405-a20e-7de6a3ee9b77'
SET person_7de6a3ee9b77.isni_list = ['http://isni.org/isni/0000000055139342']
SET person_7de6a3ee9b77.source = 'musicbrainz.org'
SET person_7de6a3ee9b77.timestamp = timestamp()
// labels

MERGE (label_5b5f193187e6:Label{ uuid: 'e96be885-132b-4488-bed8-5b5f193187e6' })
SET label_5b5f193187e6.name= 'Jazz America Marketing'

// performances

MERGE (perf_cd9380db1839:Performance{ uuid: '17cbe67e-89a1-45cc-9180-cd9380db1839' })
SET perf_cd9380db1839.name = 'Yeah'
SET perf_cd9380db1839.duration = '5:57'
SET perf_cd9380db1839.begin = '1980-12-17'
SET perf_cd9380db1839.end = '1980-12-18'
SET perf_cd9380db1839.source = 'musicbrainz.org'
SET perf_cd9380db1839.timestamp = timestamp()

MERGE (perf_bfc763905e2c:Performance{ uuid: 'a55875df-45ab-4c2e-95bc-bfc763905e2c' })
SET perf_bfc763905e2c.name = 'Sugar'
SET perf_bfc763905e2c.duration = '6:23'
SET perf_bfc763905e2c.begin = '1980-12-17'
SET perf_bfc763905e2c.end = '1980-12-18'
SET perf_bfc763905e2c.source = 'musicbrainz.org'
SET perf_bfc763905e2c.timestamp = timestamp()

MERGE (perf_2b7d2031ceb0:Performance{ uuid: 'd75ae56c-1f6a-46e8-bbcb-2b7d2031ceb0' })
SET perf_2b7d2031ceb0.name = 'Pretext'
SET perf_2b7d2031ceb0.duration = '2:51'
SET perf_2b7d2031ceb0.begin = '1980-12-17'
SET perf_2b7d2031ceb0.end = '1980-12-18'
SET perf_2b7d2031ceb0.source = 'musicbrainz.org'
SET perf_2b7d2031ceb0.timestamp = timestamp()

MERGE (perf_6502ea842169:Performance{ uuid: '9891721f-e9e0-41b3-87f6-6502ea842169' })
SET perf_6502ea842169.name = 'House of Jade'
SET perf_6502ea842169.duration = '6:29'
SET perf_6502ea842169.begin = '1980-12-17'
SET perf_6502ea842169.end = '1980-12-18'
SET perf_6502ea842169.source = 'musicbrainz.org'
SET perf_6502ea842169.timestamp = timestamp()

MERGE (perf_6b767f2d646b:Performance{ uuid: '64075651-9dcc-493e-befa-6b767f2d646b' })
SET perf_6b767f2d646b.name = 'Silver Serenade'
SET perf_6b767f2d646b.duration = '4:28'
SET perf_6b767f2d646b.begin = '1980-12-17'
SET perf_6b767f2d646b.end = '1980-12-18'
SET perf_6b767f2d646b.source = 'musicbrainz.org'
SET perf_6b767f2d646b.timestamp = timestamp()

MERGE (perf_9b675f50edeb:Performance{ uuid: '944d6cb7-fda5-471e-b4d4-9b675f50edeb' })
SET perf_9b675f50edeb.name = 'Cookin\' At The Continental'
SET perf_9b675f50edeb.duration = '4:48'
SET perf_9b675f50edeb.begin = '1980-12-17'
SET perf_9b675f50edeb.end = '1980-12-18'
SET perf_9b675f50edeb.source = 'musicbrainz.org'
SET perf_9b675f50edeb.timestamp = timestamp()

MERGE (perf_9375c153feb2:Performance{ uuid: '4c1e0f2b-c255-4e34-862f-9375c153feb2' })
SET perf_9375c153feb2.name = 'Kasha'
SET perf_9375c153feb2.duration = '5:44'
SET perf_9375c153feb2.begin = '1980-12-17'
SET perf_9375c153feb2.end = '1980-12-18'
SET perf_9375c153feb2.source = 'musicbrainz.org'
SET perf_9375c153feb2.timestamp = timestamp()

MERGE (perf_c15aba5de72c:Performance{ uuid: '41e384c3-db49-433c-8701-c15aba5de72c' })
SET perf_c15aba5de72c.name = 'Deadline'
SET perf_c15aba5de72c.duration = '5:57'
SET perf_c15aba5de72c.begin = '1980-12-17'
SET perf_c15aba5de72c.end = '1980-12-18'
SET perf_c15aba5de72c.source = 'musicbrainz.org'
SET perf_c15aba5de72c.timestamp = timestamp()



// labels
MERGE (release_216bbc6ca2eb)-[:HAS_LABEL]->(label_5b5f193187e6)


// tracks
MERGE (release_216bbc6ca2eb)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_cd9380db1839)
MERGE (release_216bbc6ca2eb)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_bfc763905e2c)
MERGE (release_216bbc6ca2eb)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_2b7d2031ceb0)
MERGE (release_216bbc6ca2eb)-[:HAS_TRACK {name: 'A4', sequence: 4}]->(perf_6502ea842169)
MERGE (release_216bbc6ca2eb)-[:HAS_TRACK {name: 'B1', sequence: 5}]->(perf_6b767f2d646b)
MERGE (release_216bbc6ca2eb)-[:HAS_TRACK {name: 'B2', sequence: 6}]->(perf_9b675f50edeb)
MERGE (release_216bbc6ca2eb)-[:HAS_TRACK {name: 'B3', sequence: 7}]->(perf_9375c153feb2)
MERGE (release_216bbc6ca2eb)-[:HAS_TRACK {name: 'B4', sequence: 8}]->(perf_c15aba5de72c)


// place nodes

MERGE (place_a2e75881ec31:Place{ uuid: 'be6e9698-2eb1-44bc-b415-a2e75881ec31' })
SET place_a2e75881ec31.name = 'Right Track Recording'
SET place_a2e75881ec31.source = 'musicbrainz.org'


// place relationships
MERGE (perf_cd9380db1839)-[:HAS_PLACE { type: 'recorded at', begin: '1980-12-17', end: '1980-12-18' }]->(place_a2e75881ec31)
MERGE (perf_bfc763905e2c)-[:HAS_PLACE { type: 'recorded at', begin: '1980-12-17', end: '1980-12-18' }]->(place_a2e75881ec31)
MERGE (perf_2b7d2031ceb0)-[:HAS_PLACE { type: 'recorded at', begin: '1980-12-17', end: '1980-12-18' }]->(place_a2e75881ec31)
MERGE (perf_6502ea842169)-[:HAS_PLACE { type: 'recorded at', begin: '1980-12-17', end: '1980-12-18' }]->(place_a2e75881ec31)
MERGE (perf_6b767f2d646b)-[:HAS_PLACE { type: 'recorded at', begin: '1980-12-17', end: '1980-12-18' }]->(place_a2e75881ec31)
MERGE (perf_9b675f50edeb)-[:HAS_PLACE { type: 'recorded at', begin: '1980-12-17', end: '1980-12-18' }]->(place_a2e75881ec31)
MERGE (perf_9375c153feb2)-[:HAS_PLACE { type: 'recorded at', begin: '1980-12-17', end: '1980-12-18' }]->(place_a2e75881ec31)
MERGE (perf_c15aba5de72c)-[:HAS_PLACE { type: 'recorded at', begin: '1980-12-17', end: '1980-12-18' }]->(place_a2e75881ec31)

MERGE (person_7de6a3ee9b77)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['violin'] }]->(perf_cd9380db1839)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_cd9380db1839)
MERGE (person_59c853a902ab)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_cd9380db1839)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_cd9380db1839)
MERGE (person_10c607803ac5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_cd9380db1839)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_cd9380db1839)
MERGE (person_3d9cd1a604da)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_cd9380db1839)
MERGE (person_7de6a3ee9b77)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['violin'] }]->(perf_bfc763905e2c)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bfc763905e2c)
MERGE (person_59c853a902ab)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_bfc763905e2c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_bfc763905e2c)
MERGE (person_10c607803ac5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_bfc763905e2c)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_bfc763905e2c)
MERGE (person_3d9cd1a604da)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_bfc763905e2c)
MERGE (person_7de6a3ee9b77)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['violin'] }]->(perf_2b7d2031ceb0)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2b7d2031ceb0)
MERGE (person_59c853a902ab)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_2b7d2031ceb0)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_2b7d2031ceb0)
MERGE (person_10c607803ac5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_2b7d2031ceb0)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_2b7d2031ceb0)
MERGE (person_3d9cd1a604da)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_2b7d2031ceb0)
MERGE (person_7de6a3ee9b77)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['violin'] }]->(perf_6502ea842169)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6502ea842169)
MERGE (person_59c853a902ab)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_6502ea842169)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6502ea842169)
MERGE (person_10c607803ac5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_6502ea842169)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_6502ea842169)
MERGE (person_3d9cd1a604da)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_6502ea842169)
MERGE (person_7de6a3ee9b77)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['violin'] }]->(perf_6b767f2d646b)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6b767f2d646b)
MERGE (person_59c853a902ab)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_6b767f2d646b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6b767f2d646b)
MERGE (person_10c607803ac5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_6b767f2d646b)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_6b767f2d646b)
MERGE (person_3d9cd1a604da)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_6b767f2d646b)
MERGE (person_7de6a3ee9b77)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['violin'] }]->(perf_9b675f50edeb)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_9b675f50edeb)
MERGE (person_59c853a902ab)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_9b675f50edeb)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9b675f50edeb)
MERGE (person_10c607803ac5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9b675f50edeb)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_9b675f50edeb)
MERGE (person_3d9cd1a604da)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_9b675f50edeb)
MERGE (person_7de6a3ee9b77)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['violin'] }]->(perf_9375c153feb2)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_9375c153feb2)
MERGE (person_59c853a902ab)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_9375c153feb2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9375c153feb2)
MERGE (person_10c607803ac5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9375c153feb2)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_9375c153feb2)
MERGE (person_3d9cd1a604da)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_9375c153feb2)
MERGE (person_7de6a3ee9b77)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['violin'] }]->(perf_c15aba5de72c)
MERGE (person_120e386da267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_c15aba5de72c)
MERGE (person_59c853a902ab)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_c15aba5de72c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_c15aba5de72c)
MERGE (person_10c607803ac5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_c15aba5de72c)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_c15aba5de72c)
MERGE (person_3d9cd1a604da)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_c15aba5de72c)

