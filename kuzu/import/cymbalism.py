
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_e3227c6712c4:Release{ uuid: 'e3fe66af-4ab9-40d7-95b2-e3227c6712c4' })
SET release_e3227c6712c4.name = 'Cymbalism'
SET release_e3227c6712c4.country = 'US'
SET release_e3227c6712c4.date = '2002-08-20'
SET release_e3227c6712c4.format = 'CD'
SET release_e3227c6712c4.discode = 'OJCCD-1079-2'
SET release_e3227c6712c4.musicbrainz = 'http://musicbrainz.org/release/e3fe66af-4ab9-40d7-95b2-e3227c6712c4'
SET release_e3227c6712c4.source = 'musicbrainz.org'


MERGE (person_c2d5d5613c56:Person{ uuid: '95493156-7000-41b6-bc34-c2d5d5613c56' }) 
SET person_c2d5d5613c56.name = 'Ronnie Mathews'
SET person_c2d5d5613c56.gender = 'Male'
SET person_c2d5d5613c56.country = 'US'
SET person_c2d5d5613c56.allmusic = 'https://www.allmusic.com/artist/mn0000278048'
SET person_c2d5d5613c56.discogs = 'https://www.discogs.com/artist/650343'
SET person_c2d5d5613c56.viaf = 'http://viaf.org/viaf/115064731'
SET person_c2d5d5613c56.wikidata = 'https://www.wikidata.org/wiki/Q2166025'
SET person_c2d5d5613c56.wikipedia = 'https://en.wikipedia.org/wiki/Ronnie_Mathews'
SET person_c2d5d5613c56.databases = ['http://d-nb.info/gnd/134661230', 'http://id.loc.gov/authorities/names/no92002331', 'https://catalogue.bnf.fr/ark:/12148/cb13897214r', 'http://snaccooperative.org/ark:/99166/w6vq6h3n', 'https://www.worldcat.org/identities/lccn-no92002331']
SET person_c2d5d5613c56.musicbrainz = 'https://musicbrainz.org/artist/95493156-7000-41b6-bc34-c2d5d5613c56'
SET person_c2d5d5613c56.isni_list = ['http://isni.org/isni/000000008183519X']
SET person_c2d5d5613c56.source = 'musicbrainz.org'


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


MERGE (person_65155041f61b:Person{ uuid: '605ebbf0-0063-4c7a-b41a-65155041f61b' }) 
SET person_65155041f61b.name = 'Frank Strozier'
SET person_65155041f61b.gender = 'Male'
SET person_65155041f61b.country = 'US'
SET person_65155041f61b.allmusic = 'https://www.allmusic.com/artist/mn0000161891'
SET person_65155041f61b.discogs = 'https://www.discogs.com/artist/295638'
SET person_65155041f61b.viaf = 'http://viaf.org/viaf/69116932'
SET person_65155041f61b.wikidata = 'https://www.wikidata.org/wiki/Q1444274'
SET person_65155041f61b.wikipedia = 'https://en.wikipedia.org/wiki/Frank_Strozier'
SET person_65155041f61b.databases = ['http://d-nb.info/gnd/134977130', 'http://id.loc.gov/authorities/names/n81002387', 'https://catalogue.bnf.fr/ark:/12148/cb13900140n', 'http://snaccooperative.org/ark:/99166/w6hb2m21', 'https://www.worldcat.org/identities/lccn-n81002387']
SET person_65155041f61b.musicbrainz = 'https://musicbrainz.org/artist/605ebbf0-0063-4c7a-b41a-65155041f61b'
SET person_65155041f61b.isni_list = ['http://isni.org/isni/0000000108013357']
SET person_65155041f61b.source = 'musicbrainz.org'


MERGE (person_53bed7cad162:Person{ uuid: 'c3fbbdb0-6383-496f-81d0-53bed7cad162' }) 
SET person_53bed7cad162.name = 'Larry Ridley'
SET person_53bed7cad162.gender = 'Male'
SET person_53bed7cad162.country = 'US'
SET person_53bed7cad162.allmusic = 'https://www.allmusic.com/artist/mn0000110328'
SET person_53bed7cad162.discogs = 'https://www.discogs.com/artist/264870'
SET person_53bed7cad162.viaf = 'http://viaf.org/viaf/37104009'
SET person_53bed7cad162.wikidata = 'https://www.wikidata.org/wiki/Q1724922'
SET person_53bed7cad162.wikipedia = 'https://en.wikipedia.org/wiki/Larry_Ridley'
SET person_53bed7cad162.databases = ['http://d-nb.info/gnd/13475879X', 'http://id.loc.gov/authorities/names/n88616707', 'https://catalogue.bnf.fr/ark:/12148/cb13921986t', 'http://snaccooperative.org/ark:/99166/w6r79wzs', 'https://www.worldcat.org/identities/lccn-n88616707']
SET person_53bed7cad162.musicbrainz = 'https://musicbrainz.org/artist/c3fbbdb0-6383-496f-81d0-53bed7cad162'
SET person_53bed7cad162.isni_list = ['http://isni.org/isni/0000000055140781']
SET person_53bed7cad162.source = 'musicbrainz.org'

// labels

MERGE (label_e8ed14bc22f8:Label{ uuid: '4876cd23-c4ab-4ac5-9b49-e8ed14bc22f8' })
SET label_e8ed14bc22f8.name= 'Original Jazz Classics'

// performances

MERGE (perf_e09cb54003fb:Performance{ uuid: '67120e5e-d047-488e-a328-e09cb54003fb' })
SET perf_e09cb54003fb.name = 'Modette'
SET perf_e09cb54003fb.duration = '9:45'
SET perf_e09cb54003fb.begin_date = '1963-11-10'
SET perf_e09cb54003fb.end_date = '1963-11-10'
SET perf_e09cb54003fb.source = 'musicbrainz.org'


MERGE (perf_616650cf65c6:Performance{ uuid: '309c81d8-f3d7-49f8-b371-616650cf65c6' })
SET perf_616650cf65c6.name = 'I\\'m Getting Sentimental Over You'
SET perf_616650cf65c6.duration = '5:34'
SET perf_616650cf65c6.begin_date = '1963-11-10'
SET perf_616650cf65c6.end_date = '1963-11-10'
SET perf_616650cf65c6.source = 'musicbrainz.org'


MERGE (perf_eeef8bfbe972:Performance{ uuid: 'ac6d8bf6-ee0f-488f-abc5-eeef8bfbe972' })
SET perf_eeef8bfbe972.name = 'Go \\'N\\' Git It!'
SET perf_eeef8bfbe972.duration = '3:52'
SET perf_eeef8bfbe972.begin_date = '1963-11-10'
SET perf_eeef8bfbe972.end_date = '1963-11-10'
SET perf_eeef8bfbe972.source = 'musicbrainz.org'


MERGE (perf_1489c6408967:Performance{ uuid: '5f5376d4-b1fe-447e-9eb6-1489c6408967' })
SET perf_1489c6408967.name = 'La Palomeinding'
SET perf_1489c6408967.duration = '6:38'
SET perf_1489c6408967.begin_date = '1963-11-10'
SET perf_1489c6408967.end_date = '1963-11-10'
SET perf_1489c6408967.source = 'musicbrainz.org'


MERGE (perf_6c687109d78e:Performance{ uuid: 'f44e9143-e3bc-47bf-8864-6c687109d78e' })
SET perf_6c687109d78e.name = 'Medley: Hag/Cymbalism/Oleo'
SET perf_6c687109d78e.duration = '11:05'
SET perf_6c687109d78e.begin_date = '1963-11-10'
SET perf_6c687109d78e.end_date = '1963-11-10'
SET perf_6c687109d78e.source = 'musicbrainz.org'




// labels
MERGE (release_e3227c6712c4)-[:HAS_LABEL]->(label_e8ed14bc22f8)


// tracks
MERGE (release_e3227c6712c4)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_e09cb54003fb)
MERGE (release_e3227c6712c4)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_616650cf65c6)
MERGE (release_e3227c6712c4)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_eeef8bfbe972)
MERGE (release_e3227c6712c4)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_1489c6408967)
MERGE (release_e3227c6712c4)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_6c687109d78e)

// works

MERGE (person_ceec49387371:Person{ uuid: 'c7f9dc85-ebff-4a0c-8957-ceec49387371' }) 
SET person_ceec49387371.name = 'Richard Wyands'
SET person_ceec49387371.gender = 'Male'
SET person_ceec49387371.country = 'US'
SET person_ceec49387371.allmusic = 'https://www.allmusic.com/artist/mn0000850987'
SET person_ceec49387371.discogs = 'https://www.discogs.com/artist/278730'
SET person_ceec49387371.viaf = 'http://viaf.org/viaf/27253612'
SET person_ceec49387371.wikidata = 'https://www.wikidata.org/wiki/Q2150973'
SET person_ceec49387371.wikipedia = 'https://en.wikipedia.org/wiki/Richard_Wyands'
SET person_ceec49387371.databases = ['http://d-nb.info/gnd/134561872', 'http://id.loc.gov/authorities/names/n78071405', 'https://catalogue.bnf.fr/ark:/12148/cb13901299t', 'http://snaccooperative.org/ark:/99166/w62z39bf', 'https://www.worldcat.org/identities/lccn-n78071405']
SET person_ceec49387371.musicbrainz = 'https://musicbrainz.org/artist/c7f9dc85-ebff-4a0c-8957-ceec49387371'
SET person_ceec49387371.isni_list = ['http://isni.org/isni/0000000055137988']
SET person_ceec49387371.source = 'musicbrainz.org'


MERGE (person_6f59d0206e9b:Person{ uuid: '69a6332a-ce91-44d3-94ca-6f59d0206e9b' }) 
SET person_6f59d0206e9b.name = 'George Bassman'
SET person_6f59d0206e9b.gender = 'Male'
SET person_6f59d0206e9b.country = 'US'
SET person_6f59d0206e9b.discogs = 'https://www.discogs.com/artist/638134'
SET person_6f59d0206e9b.wikidata = 'https://www.wikidata.org/wiki/Q1506958'
SET person_6f59d0206e9b.wikipedia = 'https://en.wikipedia.org/wiki/George_Bassman'
SET person_6f59d0206e9b.musicbrainz = 'https://musicbrainz.org/artist/69a6332a-ce91-44d3-94ca-6f59d0206e9b'
SET person_6f59d0206e9b.source = 'musicbrainz.org'


MERGE (person_9ecd8b2daa0d:Person{ uuid: '0fb41597-d1a0-480c-93f3-9ecd8b2daa0d' }) 
SET person_9ecd8b2daa0d.name = 'Ned Washington'
SET person_9ecd8b2daa0d.gender = 'Male'
SET person_9ecd8b2daa0d.country = 'US'
SET person_9ecd8b2daa0d.allmusic = 'https://www.allmusic.com/artist/mn0000324645'
SET person_9ecd8b2daa0d.discogs = 'https://www.discogs.com/artist/299280'
SET person_9ecd8b2daa0d.imdb = 'https://www.imdb.com/name/nm0913513/'
SET person_9ecd8b2daa0d.viaf = 'http://viaf.org/viaf/69121638'
SET person_9ecd8b2daa0d.wikidata = 'https://www.wikidata.org/wiki/Q1973924'
SET person_9ecd8b2daa0d.databases = ['https://rateyourmusic.com/artist/ned_washington']
SET person_9ecd8b2daa0d.musicbrainz = 'https://musicbrainz.org/artist/0fb41597-d1a0-480c-93f3-9ecd8b2daa0d'
SET person_9ecd8b2daa0d.isni_list = ['http://isni.org/isni/0000000081490873']
SET person_9ecd8b2daa0d.source = 'musicbrainz.org'


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


MERGE (work_118ea11c501b:Work{ uuid: 'b5874083-1e54-4022-b46b-118ea11c501b' })
SET work_118ea11c501b.name = 'Go \\'N\\' Git It!'
SET work_118ea11c501b.type = 'Song'
SET work_118ea11c501b.source = 'musicbrainz.org'


MERGE (work_d64518855da9:Work{ uuid: '454a2fd7-6a4a-4eee-8a50-d64518855da9' })
SET work_d64518855da9.name = 'La Palomeinding'
SET work_d64518855da9.type = 'Song'
SET work_d64518855da9.source = 'musicbrainz.org'


MERGE (work_9eda172226f7:Work{ uuid: '9b3dd1a5-0dce-31bb-8df2-9eda172226f7' })
SET work_9eda172226f7.name = 'I’m Getting Sentimental Over You'
SET work_9eda172226f7.iswc = 'T-071.063.924-9'
SET work_9eda172226f7.type = 'Song'
SET work_9eda172226f7.wikidata = 'https://www.wikidata.org/wiki/Q1676202'
SET work_9eda172226f7.musicbrainz = 'https://musicbrainz.org/work/9b3dd1a5-0dce-31bb-8df2-9eda172226f7'
SET work_9eda172226f7.source = 'musicbrainz.org'


MERGE (work_d27a1676e495:Work{ uuid: 'e7ad7ccc-b787-4028-9b24-d27a1676e495' })
SET work_d27a1676e495.name = 'Hag'
SET work_d27a1676e495.type = 'Song'
SET work_d27a1676e495.source = 'musicbrainz.org'


MERGE (work_8ba0d64d22a1:Work{ uuid: '2ed25674-408b-4fe9-9bc0-8ba0d64d22a1' })
SET work_8ba0d64d22a1.name = 'Cymbalism'
SET work_8ba0d64d22a1.type = 'Song'
SET work_8ba0d64d22a1.source = 'musicbrainz.org'


MERGE (work_ec5b55631ea8:Work{ uuid: '9bd0305e-0636-3624-972e-ec5b55631ea8' })
SET work_ec5b55631ea8.name = 'Oleo'
SET work_ec5b55631ea8.iswc = 'T-070.242.658-1'
SET work_ec5b55631ea8.type = 'Song'
SET work_ec5b55631ea8.wikidata = 'https://www.wikidata.org/wiki/Q1385150'
SET work_ec5b55631ea8.musicbrainz = 'https://musicbrainz.org/work/9bd0305e-0636-3624-972e-ec5b55631ea8'
SET work_ec5b55631ea8.source = 'musicbrainz.org'


MERGE (work_18f16f847115:Work{ uuid: '7aacc0fb-fac5-4edb-988f-18f16f847115' })
SET work_18f16f847115.name = 'Modette'
SET work_18f16f847115.type = 'Song'
SET work_18f16f847115.source = 'musicbrainz.org'



// performances of
MERGE (perf_eeef8bfbe972)-[:PERFORMANCE_OF]->(work_118ea11c501b)
MERGE (perf_1489c6408967)-[:PERFORMANCE_OF]->(work_d64518855da9)
MERGE (perf_616650cf65c6)-[:PERFORMANCE_OF]->(work_9eda172226f7)
MERGE (perf_6c687109d78e)-[:PERFORMANCE_OF {medley: true}]->(work_d27a1676e495)
MERGE (perf_6c687109d78e)-[:PERFORMANCE_OF {medley: true}]->(work_8ba0d64d22a1)
MERGE (perf_6c687109d78e)-[:PERFORMANCE_OF {medley: true}]->(work_ec5b55631ea8)
MERGE (perf_e09cb54003fb)-[:PERFORMANCE_OF]->(work_18f16f847115)


// composers
MERGE (person_c2d5d5613c56)-[:COMPOSED]->(work_118ea11c501b)
MERGE (person_65155041f61b)-[:COMPOSED]->(work_d64518855da9)
MERGE (person_6f59d0206e9b)-[:COMPOSED]->(work_9eda172226f7)
MERGE (person_9ecd8b2daa0d)-[:WROTE_LYRICS]->(work_9eda172226f7)
MERGE (person_65155041f61b)-[:COMPOSED]->(work_d27a1676e495)
MERGE (person_6f0a331cc1ca)-[:COMPOSED]->(work_8ba0d64d22a1)
MERGE (person_ceec49387371)-[:COMPOSED]->(work_8ba0d64d22a1)
MERGE (person_bad80243802a)-[:COMPOSED]->(work_ec5b55631ea8)
MERGE (person_65155041f61b)-[:COMPOSED]->(work_18f16f847115)


// place nodes

MERGE (place_569fa8b97644:Place{ uuid: '1165ef7d-371c-4e03-98db-569fa8b97644' })
SET place_569fa8b97644.name = 'Van Gelder Studio'
SET place_569fa8b97644.source = 'musicbrainz.org'


// place relationships
MERGE (perf_e09cb54003fb)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-10', end_date: '1963-11-10' }]->(place_569fa8b97644)
MERGE (perf_616650cf65c6)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-10', end_date: '1963-11-10' }]->(place_569fa8b97644)
MERGE (perf_eeef8bfbe972)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-10', end_date: '1963-11-10' }]->(place_569fa8b97644)
MERGE (perf_1489c6408967)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-10', end_date: '1963-11-10' }]->(place_569fa8b97644)
MERGE (perf_6c687109d78e)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-10', end_date: '1963-11-10' }]->(place_569fa8b97644)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e09cb54003fb)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e09cb54003fb)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e09cb54003fb)
MERGE (person_65155041f61b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_e09cb54003fb)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_616650cf65c6)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_616650cf65c6)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_616650cf65c6)
MERGE (person_65155041f61b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_616650cf65c6)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_eeef8bfbe972)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_eeef8bfbe972)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_eeef8bfbe972)
MERGE (person_65155041f61b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_eeef8bfbe972)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_1489c6408967)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_1489c6408967)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_1489c6408967)
MERGE (person_65155041f61b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_1489c6408967)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6c687109d78e)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6c687109d78e)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_6c687109d78e)
MERGE (person_65155041f61b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_6c687109d78e)



"""
)