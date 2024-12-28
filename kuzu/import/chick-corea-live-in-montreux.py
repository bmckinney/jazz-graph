
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_b584661409ba:Release{ uuid: '3d2245c1-c0c1-431d-ab9e-b584661409ba' })
SET release_b584661409ba.name = 'Live in Montreux'
SET release_b584661409ba.country = 'US'
SET release_b584661409ba.date = '1994'
SET release_b584661409ba.format = 'CD'
SET release_b584661409ba.discode = 'STD-1112'
SET release_b584661409ba.discogs = 'https://www.discogs.com/release/11193543'
SET release_b584661409ba.musicbrainz = 'http://musicbrainz.org/release/3d2245c1-c0c1-431d-ab9e-b584661409ba'
SET release_b584661409ba.source = 'musicbrainz.org'


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
SET person_9ee947b4ce37.databases = ['http://id.loc.gov/authorities/names/n82164702', 'https://catalogue.bnf.fr/ark:/12148/cb138951291', 'https://d-nb.info/gnd/131961454', 'http://snaccooperative.org/ark:/99166/w6hm8fsd', 'https://nla.gov.au/nla.party-1048452', 'https://openlibrary.org/works/OL5629680A', 'https://rateyourmusic.com/artist/joe_henderson', 'https://www.worldcat.org/identities/lccn-n82164702']
SET person_9ee947b4ce37.musicbrainz = 'https://musicbrainz.org/artist/bcab8301-c7e5-4689-a4ad-9ee947b4ce37'
SET person_9ee947b4ce37.isni_list = ['http://isni.org/isni/0000000081835181']
SET person_9ee947b4ce37.source = 'musicbrainz.org'


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


MERGE (person_644705f6e4f4:Person{ uuid: '0cd9e25c-1cb1-45e3-aba2-644705f6e4f4' }) 
SET person_644705f6e4f4.name = 'Gary Peacock'
SET person_644705f6e4f4.gender = 'Male'
SET person_644705f6e4f4.disambiguation = 'American jazz bassist'
SET person_644705f6e4f4.country = 'US'
SET person_644705f6e4f4.allmusic = 'https://www.allmusic.com/artist/mn0000153503'
SET person_644705f6e4f4.discogs = 'https://www.discogs.com/artist/255129'
SET person_644705f6e4f4.imdb = 'https://www.imdb.com/name/nm1034190/'
SET person_644705f6e4f4.viaf = 'http://viaf.org/viaf/119979251'
SET person_644705f6e4f4.wikidata = 'https://www.wikidata.org/wiki/Q466198'
SET person_644705f6e4f4.databases = ['http://id.loc.gov/authorities/names/n81058247', 'https://catalogue.bnf.fr/ark:/12148/cb13898318n', 'https://d-nb.info/gnd/134481836', 'https://rateyourmusic.com/artist/gary_peacock', 'https://www.worldcat.org/identities/lccn-n81058247']
SET person_644705f6e4f4.musicbrainz = 'https://musicbrainz.org/artist/0cd9e25c-1cb1-45e3-aba2-644705f6e4f4'
SET person_644705f6e4f4.isni_list = ['http://isni.org/isni/0000000081889913']
SET person_644705f6e4f4.source = 'musicbrainz.org'

// labels

MERGE (label_8f7fa45e2bba:Label{ uuid: '3a723233-c949-4a55-bc0f-8f7fa45e2bba' })
SET label_8f7fa45e2bba.name= 'Stretch Records'

// performances

MERGE (perf_8b995a080d68:Performance{ uuid: '18cd506a-9f41-4784-84f5-8b995a080d68' })
SET perf_8b995a080d68.name = 'Introduction'
SET perf_8b995a080d68.disambiguation = 'live in Montreux'
SET perf_8b995a080d68.duration = '0:52'
SET perf_8b995a080d68.source = 'musicbrainz.org'


MERGE (perf_3f8645bf2102:Performance{ uuid: 'f4fe9a1e-4cd4-4569-99b3-3f8645bf2102' })
SET perf_3f8645bf2102.name = 'Hairy Canary'
SET perf_3f8645bf2102.disambiguation = 'live in Montreux'
SET perf_3f8645bf2102.duration = '10:28'
SET perf_3f8645bf2102.source = 'musicbrainz.org'


MERGE (perf_74a9e950969c:Performance{ uuid: '86c4f78d-6579-4013-9f12-74a9e950969c' })
SET perf_74a9e950969c.name = 'Folk Song'
SET perf_74a9e950969c.disambiguation = 'live in Montreux'
SET perf_74a9e950969c.duration = '9:10'
SET perf_74a9e950969c.source = 'musicbrainz.org'


MERGE (perf_193ee350d5de:Performance{ uuid: 'cfee06b3-7be9-4071-8b46-193ee350d5de' })
SET perf_193ee350d5de.name = 'Psalm'
SET perf_193ee350d5de.disambiguation = 'live in Montreux'
SET perf_193ee350d5de.duration = '12:50'
SET perf_193ee350d5de.source = 'musicbrainz.org'


MERGE (perf_108497475758:Performance{ uuid: 'e48c0bf2-400c-4b0a-a568-108497475758' })
SET perf_108497475758.name = 'Quintet #2'
SET perf_108497475758.disambiguation = 'live in Montreux'
SET perf_108497475758.duration = '8:54'
SET perf_108497475758.source = 'musicbrainz.org'


MERGE (perf_d9b09bb98117:Performance{ uuid: '8f8e3dcf-f49c-461f-a33a-d9b09bb98117' })
SET perf_d9b09bb98117.name = 'Up, Up And...'
SET perf_d9b09bb98117.disambiguation = 'live in Montreux'
SET perf_d9b09bb98117.duration = '8:12'
SET perf_d9b09bb98117.source = 'musicbrainz.org'


MERGE (perf_17bcf3098346:Performance{ uuid: '8de191ad-697b-4e98-8bb6-17bcf3098346' })
SET perf_17bcf3098346.name = 'Trinkle, Tinkle'
SET perf_17bcf3098346.disambiguation = 'live in Montreux'
SET perf_17bcf3098346.duration = '10:21'
SET perf_17bcf3098346.source = 'musicbrainz.org'


MERGE (perf_d1246407aa28:Performance{ uuid: '8a8b68e4-25ca-43ca-9837-d1246407aa28' })
SET perf_d1246407aa28.name = 'So In Love'
SET perf_d1246407aa28.disambiguation = 'live in Montreux'
SET perf_d1246407aa28.duration = '6:36'
SET perf_d1246407aa28.source = 'musicbrainz.org'


MERGE (perf_b2fceb026108:Performance{ uuid: '8a820d95-cf67-4d1b-a206-b2fceb026108' })
SET perf_b2fceb026108.name = 'Drum Interlude'
SET perf_b2fceb026108.disambiguation = 'live in Montreux'
SET perf_b2fceb026108.duration = '4:09'
SET perf_b2fceb026108.source = 'musicbrainz.org'


MERGE (perf_41f4ee5e4ba2:Performance{ uuid: '6ad4ffca-4087-4237-880f-41f4ee5e4ba2' })
SET perf_41f4ee5e4ba2.name = 'Slippery When Wet, Intro Of Band'
SET perf_41f4ee5e4ba2.disambiguation = 'live in Montreux'
SET perf_41f4ee5e4ba2.duration = '1:57'
SET perf_41f4ee5e4ba2.source = 'musicbrainz.org'




// labels
MERGE (release_b584661409ba)-[:HAS_LABEL]->(label_8f7fa45e2bba)


// tracks
MERGE (release_b584661409ba)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_8b995a080d68)
MERGE (release_b584661409ba)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_3f8645bf2102)
MERGE (release_b584661409ba)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_74a9e950969c)
MERGE (release_b584661409ba)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_193ee350d5de)
MERGE (release_b584661409ba)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_108497475758)
MERGE (release_b584661409ba)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_d9b09bb98117)
MERGE (release_b584661409ba)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_17bcf3098346)
MERGE (release_b584661409ba)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_d1246407aa28)
MERGE (release_b584661409ba)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_b2fceb026108)
MERGE (release_b584661409ba)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_41f4ee5e4ba2)

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
SET person_5260b4274ed4.databases = ['http://id.loc.gov/authorities/names/n82218969', 'https://catalogue.bnf.fr/ark:/12148/cb13897622g', 'https://d-nb.info/gnd/118826158', 'http://snaccooperative.org/ark:/99166/w6j38zvn', 'https://rateyourmusic.com/artist/thelonious_monk', 'https://www.worldcat.org/identities/lccn-n82218969']
SET person_5260b4274ed4.musicbrainz = 'https://musicbrainz.org/artist/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.isni_list = ['http://isni.org/isni/0000000120249127']
SET person_5260b4274ed4.source = 'musicbrainz.org'


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
SET person_a37897b950ce.databases = ['http://id.loc.gov/authorities/names/n80017862', 'https://adp.library.ucsb.edu/names/102688', 'https://catalogue.bnf.fr/ark:/12148/cb13898618g', 'https://d-nb.info/gnd/11879292X', 'https://ibdb.com/person.php?id=12257', 'http://snaccooperative.org/ark:/99166/w6j38s5m', 'https://nla.gov.au/nla.party-949524', 'https://openlibrary.org/works/OL709416A', 'http://soundtrackcollector.com/composer/166/', 'https://rateyourmusic.com/artist/cole_porter', 'https://www.worldcat.org/identities/lccn-n80017862', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Cole&last=Porter&middle=']
SET person_a37897b950ce.musicbrainz = 'https://musicbrainz.org/artist/4a94a6cb-e70a-418b-bb53-a37897b950ce'
SET person_a37897b950ce.isni_list = ['http://isni.org/isni/0000000108653610']
SET person_a37897b950ce.source = 'musicbrainz.org'


MERGE (work_defeb1e074d1:Work{ uuid: 'c110a6cf-84e3-4f9b-bcee-defeb1e074d1' })
SET work_defeb1e074d1.name = 'Folk Song'
SET work_defeb1e074d1.type = 'Song'
SET work_defeb1e074d1.source = 'musicbrainz.org'


MERGE (work_9624ba2d7b35:Work{ uuid: '8e32b10c-dab3-31b8-a072-9624ba2d7b35' })
SET work_9624ba2d7b35.name = 'So in Love'
SET work_9624ba2d7b35.iswc = 'T-070.136.283-5'
SET work_9624ba2d7b35.type = 'Song'
SET work_9624ba2d7b35.wikidata = 'https://www.wikidata.org/wiki/Q7549717'
SET work_9624ba2d7b35.musicbrainz = 'https://musicbrainz.org/work/8e32b10c-dab3-31b8-a072-9624ba2d7b35'
SET work_9624ba2d7b35.source = 'musicbrainz.org'


MERGE (work_ee39c88445cf:Work{ uuid: '5b305852-db2f-41fc-ae40-ee39c88445cf' })
SET work_ee39c88445cf.name = 'Psalm'
SET work_ee39c88445cf.iswc = 'T-904.321.189-8'
SET work_ee39c88445cf.type = 'Song'
SET work_ee39c88445cf.source = 'musicbrainz.org'


MERGE (work_1003e9b588f3:Work{ uuid: '067eccc9-5533-34b9-a676-1003e9b588f3' })
SET work_1003e9b588f3.name = 'Trinkle Tinkle'
SET work_1003e9b588f3.iswc = 'T-070.247.478-9'
SET work_1003e9b588f3.type = 'Song'
SET work_1003e9b588f3.source = 'musicbrainz.org'



// performances of
MERGE (perf_74a9e950969c)-[:PERFORMANCE_OF]->(work_defeb1e074d1)
MERGE (perf_d1246407aa28)-[:PERFORMANCE_OF]->(work_9624ba2d7b35)
MERGE (perf_193ee350d5de)-[:PERFORMANCE_OF]->(work_ee39c88445cf)
MERGE (perf_17bcf3098346)-[:PERFORMANCE_OF]->(work_1003e9b588f3)


// composers
MERGE (person_5a269b32b4c2)-[:COMPOSED]->(work_defeb1e074d1)
MERGE (person_a37897b950ce)-[:COMPOSED]->(work_9624ba2d7b35)
MERGE (person_a37897b950ce)-[:WROTE_LYRICS]->(work_9624ba2d7b35)
MERGE (person_5a269b32b4c2)-[:COMPOSED]->(work_ee39c88445cf)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_1003e9b588f3)

MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8b995a080d68)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_8b995a080d68)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_8b995a080d68)
MERGE (person_644705f6e4f4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_8b995a080d68)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_3f8645bf2102)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_3f8645bf2102)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_3f8645bf2102)
MERGE (person_644705f6e4f4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_3f8645bf2102)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_74a9e950969c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_74a9e950969c)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_74a9e950969c)
MERGE (person_644705f6e4f4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_74a9e950969c)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_193ee350d5de)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_193ee350d5de)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_193ee350d5de)
MERGE (person_644705f6e4f4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_193ee350d5de)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_108497475758)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_108497475758)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_108497475758)
MERGE (person_644705f6e4f4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_108497475758)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d9b09bb98117)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_d9b09bb98117)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_d9b09bb98117)
MERGE (person_644705f6e4f4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_d9b09bb98117)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_17bcf3098346)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_17bcf3098346)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_17bcf3098346)
MERGE (person_644705f6e4f4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_17bcf3098346)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d1246407aa28)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_d1246407aa28)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_d1246407aa28)
MERGE (person_644705f6e4f4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_d1246407aa28)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b2fceb026108)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_b2fceb026108)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_b2fceb026108)
MERGE (person_644705f6e4f4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_b2fceb026108)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_41f4ee5e4ba2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_41f4ee5e4ba2)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_41f4ee5e4ba2)
MERGE (person_644705f6e4f4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_41f4ee5e4ba2)



"""
)