
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_db117db93a31:Release{ uuid: '3d3bd781-18f0-4150-b8c3-db117db93a31' })
SET release_db117db93a31.name = 'The Way Ahead'
SET release_db117db93a31.country = 'US'
SET release_db117db93a31.date = '1968'
SET release_db117db93a31.format = '12" Vinyl'
SET release_db117db93a31.discode = 'AS-9170'
SET release_db117db93a31.discogs = 'https://www.discogs.com/release/530795'
SET release_db117db93a31.musicbrainz = 'http://musicbrainz.org/release/3d3bd781-18f0-4150-b8c3-db117db93a31'
SET release_db117db93a31.source = 'musicbrainz.org'


MERGE (person_328d3c172106:Person{ uuid: '5ceff60b-8183-49bf-a855-328d3c172106' }) 
SET person_328d3c172106.name = 'Archie Shepp'
SET person_328d3c172106.gender = 'Male'
SET person_328d3c172106.country = 'US'
SET person_328d3c172106.allmusic = 'https://www.allmusic.com/artist/mn0000503279'
SET person_328d3c172106.bbc = 'https://www.bbc.co.uk/music/artists/5ceff60b-8183-49bf-a855-328d3c172106'
SET person_328d3c172106.discogs = 'https://www.discogs.com/artist/10514'
SET person_328d3c172106.imdb = 'https://www.imdb.com/name/nm0791906/'
SET person_328d3c172106.viaf = 'http://viaf.org/viaf/44396851'
SET person_328d3c172106.wikidata = 'https://www.wikidata.org/wiki/Q200791'
SET person_328d3c172106.databases = ['http://d-nb.info/gnd/12063158X', 'http://id.loc.gov/authorities/names/n82012141', 'https://catalogue.bnf.fr/ark:/12148/cb124638725', 'http://snaccooperative.org/ark:/99166/w68d02mb', 'https://rateyourmusic.com/artist/archie_shepp', 'https://www.worldcat.org/identities/lccn-n82012141']
SET person_328d3c172106.musicbrainz = 'https://musicbrainz.org/artist/5ceff60b-8183-49bf-a855-328d3c172106'
SET person_328d3c172106.isni_list = ['http://isni.org/isni/0000000079744002']
SET person_328d3c172106.source = 'musicbrainz.org'


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


MERGE (person_5d34a371947e:Person{ uuid: '98d1fb70-7ada-46fa-930b-5d34a371947e' }) 
SET person_5d34a371947e.name = 'Walter Davis Jr.'
SET person_5d34a371947e.gender = 'Male'
SET person_5d34a371947e.disambiguation = 'American hard bop pianist'
SET person_5d34a371947e.country = 'US'
SET person_5d34a371947e.allmusic = 'https://www.allmusic.com/artist/mn0000227539'
SET person_5d34a371947e.discogs = 'https://www.discogs.com/artist/347792'
SET person_5d34a371947e.imdb = 'https://www.imdb.com/name/nm0204116/'
SET person_5d34a371947e.viaf = 'http://viaf.org/viaf/94093713'
SET person_5d34a371947e.wikidata = 'https://www.wikidata.org/wiki/Q721383'
SET person_5d34a371947e.databases = ['http://id.loc.gov/authorities/names/n86857260', 'https://catalogue.bnf.fr/ark:/12148/cb13893036j', 'http://snaccooperative.org/ark:/99166/w6476pqf', 'https://www.worldcat.org/identities/lccn-n86857260']
SET person_5d34a371947e.musicbrainz = 'https://musicbrainz.org/artist/98d1fb70-7ada-46fa-930b-5d34a371947e'
SET person_5d34a371947e.isni_list = ['http://isni.org/isni/0000000114954487']
SET person_5d34a371947e.source = 'musicbrainz.org'


MERGE (person_622741725a24:Person{ uuid: 'e73a9a6f-4636-4fbf-887d-622741725a24' }) 
SET person_622741725a24.name = 'Jimmy Owens'
SET person_622741725a24.gender = 'Male'
SET person_622741725a24.disambiguation = 'jazz trumpeter'
SET person_622741725a24.country = 'US'
SET person_622741725a24.allmusic = 'https://www.allmusic.com/artist/mn0000085955'
SET person_622741725a24.discogs = 'https://www.discogs.com/artist/272756'
SET person_622741725a24.viaf = 'http://viaf.org/viaf/74038559'
SET person_622741725a24.wikidata = 'https://www.wikidata.org/wiki/Q1689415'
SET person_622741725a24.wikipedia = 'https://en.wikipedia.org/wiki/Jimmy_Owens_(musician)'
SET person_622741725a24.databases = ['http://d-nb.info/gnd/134699912', 'http://id.loc.gov/authorities/names/n91081089', 'https://catalogue.bnf.fr/ark:/12148/cb138981528', 'https://www.worldcat.org/identities/lccn-n91081089']
SET person_622741725a24.musicbrainz = 'https://musicbrainz.org/artist/e73a9a6f-4636-4fbf-887d-622741725a24'
SET person_622741725a24.isni_list = ['http://isni.org/isni/0000000080504313']
SET person_622741725a24.source = 'musicbrainz.org'


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


MERGE (person_3b7d6ea5b139:Person{ uuid: 'd833ca14-1104-44b6-a90a-3b7d6ea5b139' }) 
SET person_3b7d6ea5b139.name = 'Beaver Harris'
SET person_3b7d6ea5b139.gender = 'Male'
SET person_3b7d6ea5b139.disambiguation = 'jazz drummer'
SET person_3b7d6ea5b139.country = 'US'
SET person_3b7d6ea5b139.allmusic = 'https://www.allmusic.com/artist/mn0000162122'
SET person_3b7d6ea5b139.discogs = 'https://www.discogs.com/artist/282468'
SET person_3b7d6ea5b139.viaf = 'http://viaf.org/viaf/51875424'
SET person_3b7d6ea5b139.wikidata = 'https://www.wikidata.org/wiki/Q813484'
SET person_3b7d6ea5b139.wikipedia = 'https://en.wikipedia.org/wiki/Beaver_Harris'
SET person_3b7d6ea5b139.databases = ['http://d-nb.info/gnd/134398335', 'http://id.loc.gov/authorities/names/n84104203', 'https://catalogue.bnf.fr/ark:/12148/cb13894980r', 'http://snaccooperative.org/ark:/99166/w67n487h', 'https://rateyourmusic.com/artist/beaver_harris', 'https://www.worldcat.org/identities/lccn-n84104203']
SET person_3b7d6ea5b139.musicbrainz = 'https://musicbrainz.org/artist/d833ca14-1104-44b6-a90a-3b7d6ea5b139'
SET person_3b7d6ea5b139.isni_list = ['http://isni.org/isni/0000000071434894']
SET person_3b7d6ea5b139.source = 'musicbrainz.org'


MERGE (person_0ab0782360e8:Person{ uuid: '2098836b-6ee4-45fd-a5cc-0ab0782360e8' }) 
SET person_0ab0782360e8.name = 'Grachan Moncur III'
SET person_0ab0782360e8.gender = 'Male'
SET person_0ab0782360e8.disambiguation = 'trombonist'
SET person_0ab0782360e8.country = 'US'
SET person_0ab0782360e8.allmusic = 'https://www.allmusic.com/artist/mn0000803589'
SET person_0ab0782360e8.discogs = 'https://www.discogs.com/artist/253102'
SET person_0ab0782360e8.viaf = 'http://viaf.org/viaf/54333298'
SET person_0ab0782360e8.wikidata = 'https://www.wikidata.org/wiki/Q489239'
SET person_0ab0782360e8.databases = ['http://d-nb.info/gnd/134465261', 'http://id.loc.gov/authorities/names/n91066945', 'https://catalogue.bnf.fr/ark:/12148/cb13897616j', 'https://ibdb.com/person.php?id=95716', 'https://rateyourmusic.com/artist/grachan_moncur_iii', 'https://www.worldcat.org/identities/lccn-n91066945']
SET person_0ab0782360e8.musicbrainz = 'https://musicbrainz.org/artist/2098836b-6ee4-45fd-a5cc-0ab0782360e8'
SET person_0ab0782360e8.isni_list = ['http://isni.org/isni/0000000114443935']
SET person_0ab0782360e8.source = 'musicbrainz.org'

// labels

MERGE (label_8fb76f3e6ca9:Label{ uuid: '93c3b044-2b4e-4239-a73b-8fb76f3e6ca9' })
SET label_8fb76f3e6ca9.name= 'impulse!'

// performances

MERGE (perf_0fefbd09d5d2:Performance{ uuid: '236d7756-1437-4be9-915d-0fefbd09d5d2' })
SET perf_0fefbd09d5d2.name = 'Damn If I Know (The Stroller)'
SET perf_0fefbd09d5d2.duration = '6:19'
SET perf_0fefbd09d5d2.begin_date = '1968-01-29'
SET perf_0fefbd09d5d2.end_date = '1968-01-29'
SET perf_0fefbd09d5d2.source = 'musicbrainz.org'


MERGE (perf_12eb141a2a33:Performance{ uuid: '08c59f41-29b0-4369-979a-12eb141a2a33' })
SET perf_12eb141a2a33.name = 'Frankenstein'
SET perf_12eb141a2a33.duration = '13:53'
SET perf_12eb141a2a33.begin_date = '1968-01-29'
SET perf_12eb141a2a33.end_date = '1968-01-29'
SET perf_12eb141a2a33.source = 'musicbrainz.org'


MERGE (perf_7e52592c2dde:Performance{ uuid: 'ab0fde77-e8a8-4715-bc07-7e52592c2dde' })
SET perf_7e52592c2dde.name = 'Fiesta'
SET perf_7e52592c2dde.duration = '9:57'
SET perf_7e52592c2dde.begin_date = '1968-01-29'
SET perf_7e52592c2dde.end_date = '1968-01-29'
SET perf_7e52592c2dde.source = 'musicbrainz.org'


MERGE (perf_5aa05576e6dc:Performance{ uuid: 'e5f08adb-35d6-42cf-a91c-5aa05576e6dc' })
SET perf_5aa05576e6dc.name = 'Sophisticated Lady'
SET perf_5aa05576e6dc.duration = '7:11'
SET perf_5aa05576e6dc.begin_date = '1968-01-29'
SET perf_5aa05576e6dc.end_date = '1968-01-29'
SET perf_5aa05576e6dc.source = 'musicbrainz.org'




// labels
MERGE (release_db117db93a31)-[:HAS_LABEL]->(label_8fb76f3e6ca9)


// tracks
MERGE (release_db117db93a31)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_0fefbd09d5d2)
MERGE (release_db117db93a31)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_12eb141a2a33)
MERGE (release_db117db93a31)-[:HAS_TRACK {name: 'B1', sequence: 3}]->(perf_7e52592c2dde)
MERGE (release_db117db93a31)-[:HAS_TRACK {name: 'B2', sequence: 4}]->(perf_5aa05576e6dc)

// works

MERGE (person_46c176108274:Person{ uuid: '5123e60d-2ce4-45d1-8ad2-46c176108274' }) 
SET person_46c176108274.name = 'Mitchell Parish'
SET person_46c176108274.gender = 'Male'
SET person_46c176108274.country = 'US'
SET person_46c176108274.allmusic = 'https://www.allmusic.com/artist/mn0000571437'
SET person_46c176108274.allmusic = 'https://www.allmusic.com/artist/mn0002636996'
SET person_46c176108274.discogs = 'https://www.discogs.com/artist/521962'
SET person_46c176108274.imdb = 'https://www.imdb.com/name/nm0661695/'
SET person_46c176108274.viaf = 'http://viaf.org/viaf/107582173'
SET person_46c176108274.wikidata = 'https://www.wikidata.org/wiki/Q1379565'
SET person_46c176108274.databases = ['http://d-nb.info/gnd/1014608678', 'http://id.loc.gov/authorities/names/n90602103', 'https://catalogue.bnf.fr/ark:/12148/cb13807297d', 'https://ibdb.com/person.php?id=13175', 'http://snaccooperative.org/ark:/99166/w6157mcw', 'https://nla.gov.au/nla.party-979279', 'https://rateyourmusic.com/artist/mitchell_parish', 'https://www.ibdb.com/broadway-cast-staff/michael-hyman-peretz-108385', 'https://www.ibdb.com/broadway-cast-staff/m-parrish-74424', 'https://www.worldcat.org/identities/lccn-n90602103/']
SET person_46c176108274.musicbrainz = 'https://musicbrainz.org/artist/5123e60d-2ce4-45d1-8ad2-46c176108274'
SET person_46c176108274.isni_list = ['http://isni.org/isni/0000000119187395']
SET person_46c176108274.source = 'musicbrainz.org'


MERGE (person_1ef2fece51ce:Person{ uuid: '2a2bf494-ac80-4ac9-901f-1ef2fece51ce' }) 
SET person_1ef2fece51ce.name = 'Irving Mills'
SET person_1ef2fece51ce.gender = 'Male'
SET person_1ef2fece51ce.country = 'US'
SET person_1ef2fece51ce.allmusic = 'https://www.allmusic.com/artist/mn0000084993'
SET person_1ef2fece51ce.discogs = 'https://www.discogs.com/artist/307446'
SET person_1ef2fece51ce.imdb = 'https://www.imdb.com/name/nm0590030/'
SET person_1ef2fece51ce.viaf = 'http://viaf.org/viaf/76500944'
SET person_1ef2fece51ce.wikidata = 'https://www.wikidata.org/wiki/Q1292110'
SET person_1ef2fece51ce.databases = ['http://d-nb.info/gnd/135465664', 'http://id.loc.gov/authorities/names/n88621778', 'https://catalogue.bnf.fr/ark:/12148/cb13897535j', 'https://ibdb.com/person.php?id=83868', 'http://snaccooperative.org/ark:/99166/w6f50280', 'https://nla.gov.au/nla.party-1528202', 'https://rateyourmusic.com/artist/irving_mills', 'https://www.worldcat.org/identities/lccn-n88621778/']
SET person_1ef2fece51ce.musicbrainz = 'https://musicbrainz.org/artist/2a2bf494-ac80-4ac9-901f-1ef2fece51ce'
SET person_1ef2fece51ce.isni_list = ['http://isni.org/isni/0000000081569522']
SET person_1ef2fece51ce.source = 'musicbrainz.org'


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
SET person_7eeeb45e411f.databases = ['http://d-nb.info/gnd/118529994', 'http://id.loc.gov/authorities/names/n50080187', 'https://catalogue.bnf.fr/ark:/12148/cb13893638w', 'https://ibdb.com/person.php?id=11631', 'http://snaccooperative.org/ark:/99166/w6639nkm', 'https://nla.gov.au/nla.party-815399', 'https://openlibrary.org/works/OL1953949A', 'https://rateyourmusic.com/artist/duke_ellington', 'https://www.worldcat.org/identities/lccn-n50080187/']
SET person_7eeeb45e411f.musicbrainz = 'https://musicbrainz.org/artist/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.isni_list = ['http://isni.org/isni/0000000109110810']
SET person_7eeeb45e411f.source = 'musicbrainz.org'


MERGE (work_6f1cda2f66ea:Work{ uuid: 'b831f84a-b8d4-30cf-a875-6f1cda2f66ea' })
SET work_6f1cda2f66ea.name = 'Sophisticated Lady'
SET work_6f1cda2f66ea.iswc = 'T-071.070.417-8'
SET work_6f1cda2f66ea.type = 'Song'
SET work_6f1cda2f66ea.wikidata = 'https://www.wikidata.org/wiki/Q1851091'
SET work_6f1cda2f66ea.musicbrainz = 'https://musicbrainz.org/work/b831f84a-b8d4-30cf-a875-6f1cda2f66ea'
SET work_6f1cda2f66ea.source = 'musicbrainz.org'



// performances of
MERGE (perf_5aa05576e6dc)-[:PERFORMANCE_OF]->(work_6f1cda2f66ea)


// composers
MERGE (person_7eeeb45e411f)-[:COMPOSED]->(work_6f1cda2f66ea)
MERGE (person_1ef2fece51ce)-[:WROTE_LYRICS]->(work_6f1cda2f66ea)
MERGE (person_46c176108274)-[:WROTE_LYRICS]->(work_6f1cda2f66ea)


// place nodes

MERGE (place_a65602ff96ff:Place{ uuid: 'e6d0ec38-898d-4410-86cb-a65602ff96ff' })
SET place_a65602ff96ff.name = 'RCA Studios'
SET place_a65602ff96ff.source = 'musicbrainz.org'


// place relationships
MERGE (perf_0fefbd09d5d2)-[:HAS_PLACE { type: 'recorded at', begin_date: '1968-01-29', end_date: '1968-01-29' }]->(place_a65602ff96ff)
MERGE (perf_12eb141a2a33)-[:HAS_PLACE { type: 'recorded at', begin_date: '1968-01-29', end_date: '1968-01-29' }]->(place_a65602ff96ff)
MERGE (perf_7e52592c2dde)-[:HAS_PLACE { type: 'recorded at', begin_date: '1968-01-29', end_date: '1968-01-29' }]->(place_a65602ff96ff)
MERGE (perf_5aa05576e6dc)-[:HAS_PLACE { type: 'recorded at', begin_date: '1968-01-29', end_date: '1968-01-29' }]->(place_a65602ff96ff)

MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_0fefbd09d5d2)
MERGE (person_5d34a371947e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_0fefbd09d5d2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_0fefbd09d5d2)
MERGE (person_0ab0782360e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_0fefbd09d5d2)
MERGE (person_622741725a24)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_0fefbd09d5d2)
MERGE (person_328d3c172106)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_0fefbd09d5d2)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_12eb141a2a33)
MERGE (person_5d34a371947e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_12eb141a2a33)
MERGE (person_3b7d6ea5b139)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_12eb141a2a33)
MERGE (person_0ab0782360e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_12eb141a2a33)
MERGE (person_622741725a24)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_12eb141a2a33)
MERGE (person_328d3c172106)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_12eb141a2a33)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_7e52592c2dde)
MERGE (person_5d34a371947e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_7e52592c2dde)
MERGE (person_3b7d6ea5b139)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_7e52592c2dde)
MERGE (person_0ab0782360e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_7e52592c2dde)
MERGE (person_622741725a24)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_7e52592c2dde)
MERGE (person_328d3c172106)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_7e52592c2dde)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_5aa05576e6dc)
MERGE (person_5d34a371947e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5aa05576e6dc)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_5aa05576e6dc)
MERGE (person_0ab0782360e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_5aa05576e6dc)
MERGE (person_622741725a24)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_5aa05576e6dc)
MERGE (person_328d3c172106)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_5aa05576e6dc)



"""
)