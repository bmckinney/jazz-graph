
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_098d963b2d7b:Release{ uuid: '0871d683-127d-48d7-98c8-098d963b2d7b' })
SET release_098d963b2d7b.name = 'A Grand Night for Swinging'
SET release_098d963b2d7b.country = 'US'
SET release_098d963b2d7b.date = '2008'
SET release_098d963b2d7b.format = 'CD'
SET release_098d963b2d7b.discode = 'HCD 7180'
SET release_098d963b2d7b.discogs = 'https://www.discogs.com/release/14963873'
SET release_098d963b2d7b.musicbrainz = 'http://musicbrainz.org/release/0871d683-127d-48d7-98c8-098d963b2d7b'
SET release_098d963b2d7b.source = 'musicbrainz.org'


MERGE (person_c60f48477ed2:Person{ uuid: '4a0c1055-ec66-47a0-a668-c60f48477ed2' }) 
SET person_c60f48477ed2.name = 'Mary Lou Williams'
SET person_c60f48477ed2.gender = 'Female'
SET person_c60f48477ed2.country = 'US'
SET person_c60f48477ed2.allmusic = 'https://www.allmusic.com/artist/mn0000859820'
SET person_c60f48477ed2.discogs = 'https://www.discogs.com/artist/59405'
SET person_c60f48477ed2.imdb = 'https://www.imdb.com/name/nm0931278/'
SET person_c60f48477ed2.viaf = 'http://viaf.org/viaf/105289239'
SET person_c60f48477ed2.wikidata = 'https://www.wikidata.org/wiki/Q126677'
SET person_c60f48477ed2.databases = ['http://id.loc.gov/authorities/names/n82025133', 'https://adp.library.ucsb.edu/names/103504', 'https://catalogue.bnf.fr/ark:/12148/cb13901196h', 'https://d-nb.info/gnd/122051920', 'https://ibdb.com/person.php?id=65084', 'http://snaccooperative.org/ark:/99166/w6kd29q4', 'https://www.worldcat.org/identities/lccn-n82025133']
SET person_c60f48477ed2.musicbrainz = 'https://musicbrainz.org/artist/4a0c1055-ec66-47a0-a668-c60f48477ed2'
SET person_c60f48477ed2.isni_list = ['http://isni.org/isni/0000000082867900']
SET person_c60f48477ed2.source = 'musicbrainz.org'


MERGE (person_a5edbd34a30b:Person{ uuid: '1c963225-b505-4fdb-9068-a5edbd34a30b' }) 
SET person_a5edbd34a30b.name = 'Joe Fields'
SET person_a5edbd34a30b.gender = 'Male'
SET person_a5edbd34a30b.disambiguation = 'American jazz producer'
SET person_a5edbd34a30b.country = 'US'
SET person_a5edbd34a30b.discogs = 'https://www.discogs.com/artist/258367'
SET person_a5edbd34a30b.wikidata = 'https://www.wikidata.org/wiki/Q6209827'
SET person_a5edbd34a30b.wikipedia = 'https://en.wikipedia.org/wiki/Joe_Fields_(producer)'
SET person_a5edbd34a30b.musicbrainz = 'https://musicbrainz.org/artist/1c963225-b505-4fdb-9068-a5edbd34a30b'
SET person_a5edbd34a30b.source = 'musicbrainz.org'


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


MERGE (person_b839144f4f7f:Person{ uuid: '245a481f-228d-4a5f-939c-b839144f4f7f' }) 
SET person_b839144f4f7f.name = 'Ronnie Boykins'
SET person_b839144f4f7f.gender = 'Male'
SET person_b839144f4f7f.country = 'US'
SET person_b839144f4f7f.allmusic = 'https://www.allmusic.com/artist/mn0000845616'
SET person_b839144f4f7f.discogs = 'https://www.discogs.com/artist/256607'
SET person_b839144f4f7f.viaf = 'http://viaf.org/viaf/74039394'
SET person_b839144f4f7f.wikidata = 'https://www.wikidata.org/wiki/Q1756516'
SET person_b839144f4f7f.wikipedia = 'https://en.wikipedia.org/wiki/Ronnie_Boykins'
SET person_b839144f4f7f.databases = ['http://id.loc.gov/authorities/names/n78052997', 'https://catalogue.bnf.fr/ark:/12148/cb139219964', 'https://d-nb.info/gnd/134820509', 'https://www.worldcat.org/identities/lccn-n78052997']
SET person_b839144f4f7f.musicbrainz = 'https://musicbrainz.org/artist/245a481f-228d-4a5f-939c-b839144f4f7f'
SET person_b839144f4f7f.isni_list = ['http://isni.org/isni/0000000055151202']
SET person_b839144f4f7f.source = 'musicbrainz.org'

// labels

MERGE (label_5f75b69d9a88:Label{ uuid: '4d94bc50-cb9a-4ebc-b998-5f75b69d9a88' })
SET label_5f75b69d9a88.name= 'HighNote Records, Inc.'

// performances

MERGE (perf_90fc46e856db:Performance{ uuid: 'bc213bc0-251a-4de7-a088-90fc46e856db' })
SET perf_90fc46e856db.name = 'A Grand Night for Swinging'
SET perf_90fc46e856db.duration = '6:58'
SET perf_90fc46e856db.begin_date = '1976'
SET perf_90fc46e856db.end_date = '1976'
SET perf_90fc46e856db.source = 'musicbrainz.org'


MERGE (perf_90fa128f405b:Performance{ uuid: '888966f8-0bd3-4f30-931d-90fa128f405b' })
SET perf_90fa128f405b.name = 'I Can\\'t Get Started'
SET perf_90fa128f405b.duration = '4:48'
SET perf_90fa128f405b.begin_date = '1976'
SET perf_90fa128f405b.end_date = '1976'
SET perf_90fa128f405b.source = 'musicbrainz.org'


MERGE (perf_89b6f6be359c:Performance{ uuid: 'f6926a3b-d073-4f0a-aa7e-89b6f6be359c' })
SET perf_89b6f6be359c.name = 'My Funny Valentine'
SET perf_89b6f6be359c.duration = '4:53'
SET perf_89b6f6be359c.begin_date = '1976'
SET perf_89b6f6be359c.end_date = '1976'
SET perf_89b6f6be359c.source = 'musicbrainz.org'


MERGE (perf_953073877615:Performance{ uuid: '60671a87-be0d-4bc4-95de-953073877615' })
SET perf_953073877615.name = 'Bag\\'s Blues'
SET perf_953073877615.duration = '6:29'
SET perf_953073877615.begin_date = '1976'
SET perf_953073877615.end_date = '1976'
SET perf_953073877615.source = 'musicbrainz.org'


MERGE (perf_f017f2cf304c:Performance{ uuid: 'd1203c22-7ced-4e4b-8323-f017f2cf304c' })
SET perf_f017f2cf304c.name = 'St. Louis Blues'
SET perf_f017f2cf304c.duration = '7:31'
SET perf_f017f2cf304c.begin_date = '1976'
SET perf_f017f2cf304c.end_date = '1976'
SET perf_f017f2cf304c.source = 'musicbrainz.org'


MERGE (perf_7b345d55e4e9:Performance{ uuid: '3f0e1d9b-f6b5-4896-9579-7b345d55e4e9' })
SET perf_7b345d55e4e9.name = 'Baby Man'
SET perf_7b345d55e4e9.duration = '5:58'
SET perf_7b345d55e4e9.begin_date = '1976'
SET perf_7b345d55e4e9.end_date = '1976'
SET perf_7b345d55e4e9.source = 'musicbrainz.org'


MERGE (perf_7d693bab8af2:Performance{ uuid: 'bbb1460a-326b-4d46-b76d-7d693bab8af2' })
SET perf_7d693bab8af2.name = 'Caravan'
SET perf_7d693bab8af2.duration = '6:54'
SET perf_7d693bab8af2.begin_date = '1976'
SET perf_7d693bab8af2.end_date = '1976'
SET perf_7d693bab8af2.source = 'musicbrainz.org'


MERGE (perf_c8292c517d7f:Performance{ uuid: '299b2277-10f4-4b69-935f-c8292c517d7f' })
SET perf_c8292c517d7f.name = 'A Grand Night for Swinging'
SET perf_c8292c517d7f.duration = '4:30'
SET perf_c8292c517d7f.begin_date = '1976'
SET perf_c8292c517d7f.end_date = '1976'
SET perf_c8292c517d7f.source = 'musicbrainz.org'


MERGE (perf_1fc3aabcc162:Performance{ uuid: '91d8f3d5-4414-4f35-8d67-1fc3aabcc162' })
SET perf_1fc3aabcc162.name = 'Interview With Mary Lou Williams'
SET perf_1fc3aabcc162.duration = '4:40'
SET perf_1fc3aabcc162.begin_date = '1976'
SET perf_1fc3aabcc162.end_date = '1976'
SET perf_1fc3aabcc162.source = 'musicbrainz.org'




// labels
MERGE (release_098d963b2d7b)-[:HAS_LABEL]->(label_5f75b69d9a88)


// tracks
MERGE (release_098d963b2d7b)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_90fc46e856db)
MERGE (release_098d963b2d7b)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_90fa128f405b)
MERGE (release_098d963b2d7b)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_89b6f6be359c)
MERGE (release_098d963b2d7b)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_953073877615)
MERGE (release_098d963b2d7b)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_f017f2cf304c)
MERGE (release_098d963b2d7b)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_7b345d55e4e9)
MERGE (release_098d963b2d7b)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_7d693bab8af2)
MERGE (release_098d963b2d7b)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_c8292c517d7f)
MERGE (release_098d963b2d7b)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_1fc3aabcc162)


// place nodes

MERGE (place_7fbf7b58fd64:Place{ uuid: '1a554411-62ec-4718-9984-7fbf7b58fd64' })
SET place_7fbf7b58fd64.name = 'The Downtown Club, Statler Hilton'
SET place_7fbf7b58fd64.source = 'musicbrainz.org'


// place relationships
MERGE (perf_90fc46e856db)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976', end_date: '1976' }]->(place_7fbf7b58fd64)
MERGE (perf_90fa128f405b)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976', end_date: '1976' }]->(place_7fbf7b58fd64)
MERGE (perf_89b6f6be359c)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976', end_date: '1976' }]->(place_7fbf7b58fd64)
MERGE (perf_953073877615)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976', end_date: '1976' }]->(place_7fbf7b58fd64)
MERGE (perf_f017f2cf304c)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976', end_date: '1976' }]->(place_7fbf7b58fd64)
MERGE (perf_7b345d55e4e9)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976', end_date: '1976' }]->(place_7fbf7b58fd64)
MERGE (perf_7d693bab8af2)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976', end_date: '1976' }]->(place_7fbf7b58fd64)
MERGE (perf_c8292c517d7f)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976', end_date: '1976' }]->(place_7fbf7b58fd64)
MERGE (perf_1fc3aabcc162)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976', end_date: '1976' }]->(place_7fbf7b58fd64)

MERGE (person_b839144f4f7f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_90fc46e856db)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_90fc46e856db)
MERGE (person_c60f48477ed2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_90fc46e856db)
MERGE (person_a5edbd34a30b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_90fc46e856db)
MERGE (person_b839144f4f7f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_90fa128f405b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_90fa128f405b)
MERGE (person_c60f48477ed2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_90fa128f405b)
MERGE (person_a5edbd34a30b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_90fa128f405b)
MERGE (person_b839144f4f7f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_89b6f6be359c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_89b6f6be359c)
MERGE (person_c60f48477ed2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_89b6f6be359c)
MERGE (person_a5edbd34a30b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_89b6f6be359c)
MERGE (person_b839144f4f7f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_953073877615)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_953073877615)
MERGE (person_c60f48477ed2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_953073877615)
MERGE (person_a5edbd34a30b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_953073877615)
MERGE (person_b839144f4f7f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_f017f2cf304c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f017f2cf304c)
MERGE (person_c60f48477ed2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f017f2cf304c)
MERGE (person_a5edbd34a30b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_f017f2cf304c)
MERGE (person_b839144f4f7f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_7b345d55e4e9)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_7b345d55e4e9)
MERGE (person_c60f48477ed2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_7b345d55e4e9)
MERGE (person_a5edbd34a30b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_7b345d55e4e9)
MERGE (person_b839144f4f7f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_7d693bab8af2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_7d693bab8af2)
MERGE (person_c60f48477ed2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_7d693bab8af2)
MERGE (person_a5edbd34a30b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_7d693bab8af2)
MERGE (person_b839144f4f7f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_c8292c517d7f)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_c8292c517d7f)
MERGE (person_c60f48477ed2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_c8292c517d7f)
MERGE (person_a5edbd34a30b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_c8292c517d7f)
MERGE (person_b839144f4f7f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_1fc3aabcc162)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_1fc3aabcc162)
MERGE (person_c60f48477ed2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_1fc3aabcc162)
MERGE (person_a5edbd34a30b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_1fc3aabcc162)



"""
)