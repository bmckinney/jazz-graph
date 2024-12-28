
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_63aa8ffed102:Release{ uuid: '789e791c-69a9-4684-9090-63aa8ffed102' })
SET release_63aa8ffed102.name = 'Remembering Bud Powell'
SET release_63aa8ffed102.disambiguation = 'This is an audio CD, not DTS cd.'
SET release_63aa8ffed102.country = 'US'
SET release_63aa8ffed102.date = '1997'
SET release_63aa8ffed102.format = 'CD'
SET release_63aa8ffed102.discode = 'SCD-9012-2'
SET release_63aa8ffed102.discogs = 'https://www.discogs.com/release/1831774'
SET release_63aa8ffed102.musicbrainz = 'http://musicbrainz.org/release/789e791c-69a9-4684-9090-63aa8ffed102'
SET release_63aa8ffed102.source = 'musicbrainz.org'


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


MERGE (person_4aef822ea97d:Person{ uuid: 'a19d3e1a-ef70-464a-a91c-4aef822ea97d' }) 
SET person_4aef822ea97d.name = 'Bernie Kirsh'
SET person_4aef822ea97d.gender = 'Male'
SET person_4aef822ea97d.country = 'US'
SET person_4aef822ea97d.discogs = 'https://www.discogs.com/artist/315355'
SET person_4aef822ea97d.musicbrainz = 'https://musicbrainz.org/artist/a19d3e1a-ef70-464a-a91c-4aef822ea97d'
SET person_4aef822ea97d.source = 'musicbrainz.org'


MERGE (person_a499d9f33ef6:Person{ uuid: '9ab474cd-a69f-47a7-be0d-a499d9f33ef6' }) 
SET person_a499d9f33ef6.name = 'Ron Moss'
SET person_a499d9f33ef6.gender = 'Male'
SET person_a499d9f33ef6.discogs = 'https://www.discogs.com/artist/373293'
SET person_a499d9f33ef6.musicbrainz = 'https://musicbrainz.org/artist/9ab474cd-a69f-47a7-be0d-a499d9f33ef6'
SET person_a499d9f33ef6.source = 'musicbrainz.org'


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


MERGE (person_7d184cfb43cc:Person{ uuid: 'a2eb4638-ccfe-464f-812c-7d184cfb43cc' }) 
SET person_7d184cfb43cc.name = 'Robert Read'
SET person_7d184cfb43cc.source = 'musicbrainz.org'


MERGE (person_8c2883799052:Person{ uuid: '30907194-57ca-4c7f-8e10-8c2883799052' }) 
SET person_8c2883799052.name = 'Wallace Roney'
SET person_8c2883799052.gender = 'Male'
SET person_8c2883799052.disambiguation = 'jazz trumpeter'
SET person_8c2883799052.country = 'US'
SET person_8c2883799052.allmusic = 'https://www.allmusic.com/artist/mn0000813629'
SET person_8c2883799052.discogs = 'https://www.discogs.com/artist/255141'
SET person_8c2883799052.discogs = 'https://www.discogs.com/artist/3340646'
SET person_8c2883799052.imdb = 'https://www.imdb.com/name/nm0740077/'
SET person_8c2883799052.viaf = 'http://viaf.org/viaf/2659548'
SET person_8c2883799052.wikidata = 'https://www.wikidata.org/wiki/Q343378'
SET person_8c2883799052.databases = ['http://d-nb.info/gnd/134501462', 'http://id.loc.gov/authorities/names/n88634414', 'https://catalogue.bnf.fr/ark:/12148/cb13930787k', 'https://rateyourmusic.com/artist/wallace-roney', 'https://www.worldcat.org/identities/lccn-n88634414']
SET person_8c2883799052.musicbrainz = 'https://musicbrainz.org/artist/30907194-57ca-4c7f-8e10-8c2883799052'
SET person_8c2883799052.isni_list = ['http://isni.org/isni/0000000055130727']
SET person_8c2883799052.source = 'musicbrainz.org'


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

// labels

MERGE (label_8f7fa45e2bba:Label{ uuid: '3a723233-c949-4a55-bc0f-8f7fa45e2bba' })
SET label_8f7fa45e2bba.name= 'Stretch Records'

// performances

MERGE (perf_6138ae4eefb1:Performance{ uuid: '2fc4692c-179a-4756-937a-6138ae4eefb1' })
SET perf_6138ae4eefb1.name = 'Bouncin’ With Bud'
SET perf_6138ae4eefb1.duration = '8:02'
SET perf_6138ae4eefb1.source = 'musicbrainz.org'


MERGE (perf_f15941c3d5c2:Performance{ uuid: '3f74abb5-d2be-4618-80cf-f15941c3d5c2' })
SET perf_f15941c3d5c2.name = 'Mediocre'
SET perf_f15941c3d5c2.duration = '8:52'
SET perf_f15941c3d5c2.source = 'musicbrainz.org'


MERGE (perf_faf2541c0e0a:Performance{ uuid: 'b2669d6d-3090-4252-8648-faf2541c0e0a' })
SET perf_faf2541c0e0a.name = 'Willow Grove'
SET perf_faf2541c0e0a.duration = '9:59'
SET perf_faf2541c0e0a.source = 'musicbrainz.org'


MERGE (perf_737579887a14:Performance{ uuid: 'f05ea106-3e64-4ce1-b460-737579887a14' })
SET perf_737579887a14.name = 'Dusk in Sandi'
SET perf_737579887a14.duration = '8:07'
SET perf_737579887a14.source = 'musicbrainz.org'


MERGE (perf_240a32b5d209:Performance{ uuid: 'bdbffc97-b776-482c-8f39-240a32b5d209' })
SET perf_240a32b5d209.name = 'Oblivion'
SET perf_240a32b5d209.duration = '7:17'
SET perf_240a32b5d209.source = 'musicbrainz.org'


MERGE (perf_264bf52a1a52:Performance{ uuid: '3aebd1e5-a495-4e1f-aff0-264bf52a1a52' })
SET perf_264bf52a1a52.name = 'Bud Powell'
SET perf_264bf52a1a52.duration = '6:27'
SET perf_264bf52a1a52.source = 'musicbrainz.org'


MERGE (perf_24cae3962643:Performance{ uuid: '2c1b25e5-9359-4b25-9ef7-24cae3962643' })
SET perf_24cae3962643.name = 'I’ll Keep Loving You'
SET perf_24cae3962643.duration = '9:11'
SET perf_24cae3962643.source = 'musicbrainz.org'


MERGE (perf_daeb9f16c481:Performance{ uuid: '01bd740f-c600-4438-bf8b-daeb9f16c481' })
SET perf_daeb9f16c481.name = 'Glass Enclosure'
SET perf_daeb9f16c481.duration = '3:20'
SET perf_daeb9f16c481.source = 'musicbrainz.org'


MERGE (perf_0ca2686b3a5f:Performance{ uuid: 'f978030a-bc69-4ad5-ae1f-0ca2686b3a5f' })
SET perf_0ca2686b3a5f.name = 'Tempus Fugit'
SET perf_0ca2686b3a5f.duration = '9:32'
SET perf_0ca2686b3a5f.source = 'musicbrainz.org'


MERGE (perf_e574364cc198:Performance{ uuid: '96cd9f68-3b5f-4cfa-8700-e574364cc198' })
SET perf_e574364cc198.name = 'Celia'
SET perf_e574364cc198.duration = '3:00'
SET perf_e574364cc198.source = 'musicbrainz.org'




// labels
MERGE (release_63aa8ffed102)-[:HAS_LABEL]->(label_8f7fa45e2bba)


// tracks
MERGE (release_63aa8ffed102)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_6138ae4eefb1)
MERGE (release_63aa8ffed102)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_f15941c3d5c2)
MERGE (release_63aa8ffed102)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_faf2541c0e0a)
MERGE (release_63aa8ffed102)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_737579887a14)
MERGE (release_63aa8ffed102)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_240a32b5d209)
MERGE (release_63aa8ffed102)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_264bf52a1a52)
MERGE (release_63aa8ffed102)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_24cae3962643)
MERGE (release_63aa8ffed102)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_daeb9f16c481)
MERGE (release_63aa8ffed102)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_0ca2686b3a5f)
MERGE (release_63aa8ffed102)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_e574364cc198)

// works

MERGE (person_340d64fbb41c:Person{ uuid: 'dbc5809c-7837-4b6f-961e-340d64fbb41c' }) 
SET person_340d64fbb41c.name = 'Bud Powell'
SET person_340d64fbb41c.gender = 'Male'
SET person_340d64fbb41c.country = 'US'
SET person_340d64fbb41c.allmusic = 'https://www.allmusic.com/artist/mn0000640675'
SET person_340d64fbb41c.bbc = 'https://www.bbc.co.uk/music/artists/dbc5809c-7837-4b6f-961e-340d64fbb41c'
SET person_340d64fbb41c.discogs = 'https://www.discogs.com/artist/29992'
SET person_340d64fbb41c.imdb = 'https://www.imdb.com/name/nm0694046/'
SET person_340d64fbb41c.viaf = 'http://viaf.org/viaf/197369'
SET person_340d64fbb41c.wikidata = 'https://www.wikidata.org/wiki/Q312692'
SET person_340d64fbb41c.databases = ['http://d-nb.info/gnd/119379457', 'http://id.loc.gov/authorities/names/n81146628', 'https://catalogue.bnf.fr/ark:/12148/cb13898636d', 'http://snaccooperative.org/ark:/99166/w66j93wh', 'https://rateyourmusic.com/artist/bud_powell', 'https://www.worldcat.org/identities/lccn-n81146628']
SET person_340d64fbb41c.musicbrainz = 'https://musicbrainz.org/artist/dbc5809c-7837-4b6f-961e-340d64fbb41c'
SET person_340d64fbb41c.isni_list = ['http://isni.org/isni/0000000063083027']
SET person_340d64fbb41c.source = 'musicbrainz.org'


MERGE (work_9d1baf9ff1cc:Work{ uuid: '49025c5f-060e-4993-816f-9d1baf9ff1cc' })
SET work_9d1baf9ff1cc.name = 'Bouncing With Bud'
SET work_9d1baf9ff1cc.type = 'Song'
SET work_9d1baf9ff1cc.source = 'musicbrainz.org'


MERGE (work_98d695dbaf1b:Work{ uuid: '421e7a45-be56-459a-a498-98d695dbaf1b' })
SET work_98d695dbaf1b.name = 'Bud Powell'
SET work_98d695dbaf1b.type = 'Song'
SET work_98d695dbaf1b.source = 'musicbrainz.org'


MERGE (work_2f5f0b571320:Work{ uuid: '5d861692-5518-355e-abfb-2f5f0b571320' })
SET work_2f5f0b571320.name = 'Tempus Fugit'
SET work_2f5f0b571320.wikidata = 'https://www.wikidata.org/wiki/Q7699066'
SET work_2f5f0b571320.musicbrainz = 'https://musicbrainz.org/work/5d861692-5518-355e-abfb-2f5f0b571320'
SET work_2f5f0b571320.source = 'musicbrainz.org'


MERGE (work_988648b2a68c:Work{ uuid: 'b3b41322-5bf4-39ef-a9f5-988648b2a68c' })
SET work_988648b2a68c.name = 'Celia'
SET work_988648b2a68c.type = 'Song'
SET work_988648b2a68c.source = 'musicbrainz.org'


MERGE (work_1ae46f2618b8:Work{ uuid: '72e2907e-5e09-4881-af56-1ae46f2618b8' })
SET work_1ae46f2618b8.name = 'Glass Enclosure'
SET work_1ae46f2618b8.iswc = 'T-700.096.288-1'
SET work_1ae46f2618b8.source = 'musicbrainz.org'


MERGE (work_93a77bfc46ef:Work{ uuid: '9787a550-37bc-4079-ae6f-93a77bfc46ef' })
SET work_93a77bfc46ef.name = 'Mediocre'
SET work_93a77bfc46ef.type = 'Song'
SET work_93a77bfc46ef.source = 'musicbrainz.org'


MERGE (work_1cd9abbbfc71:Work{ uuid: 'a52c191a-0b56-487d-836b-1cd9abbbfc71' })
SET work_1cd9abbbfc71.name = 'Willow Grove'
SET work_1cd9abbbfc71.type = 'Song'
SET work_1cd9abbbfc71.source = 'musicbrainz.org'


MERGE (work_c8ccafd61842:Work{ uuid: '20d4af89-323b-41ac-9315-c8ccafd61842' })
SET work_c8ccafd61842.name = 'Oblivion'
SET work_c8ccafd61842.type = 'Song'
SET work_c8ccafd61842.wikipedia = 'https://en.wikipedia.org/wiki/The_Genius_of_Bud_Powell'
SET work_c8ccafd61842.musicbrainz = 'https://musicbrainz.org/work/20d4af89-323b-41ac-9315-c8ccafd61842'
SET work_c8ccafd61842.source = 'musicbrainz.org'


MERGE (work_3a978448f808:Work{ uuid: 'd85ee4f0-bf14-4ace-8ab5-3a978448f808' })
SET work_3a978448f808.name = 'Dusk In Sandi'
SET work_3a978448f808.type = 'Song'
SET work_3a978448f808.source = 'musicbrainz.org'


MERGE (work_7be093476c32:Work{ uuid: 'a534b1b9-eead-4685-b2eb-7be093476c32' })
SET work_7be093476c32.name = 'I\\'ll Keep Loving You'
SET work_7be093476c32.type = 'Song'
SET work_7be093476c32.source = 'musicbrainz.org'



// performances of
MERGE (perf_6138ae4eefb1)-[:PERFORMANCE_OF]->(work_9d1baf9ff1cc)
MERGE (perf_264bf52a1a52)-[:PERFORMANCE_OF]->(work_98d695dbaf1b)
MERGE (perf_0ca2686b3a5f)-[:PERFORMANCE_OF]->(work_2f5f0b571320)
MERGE (perf_e574364cc198)-[:PERFORMANCE_OF]->(work_988648b2a68c)
MERGE (perf_daeb9f16c481)-[:PERFORMANCE_OF]->(work_1ae46f2618b8)
MERGE (perf_f15941c3d5c2)-[:PERFORMANCE_OF]->(work_93a77bfc46ef)
MERGE (perf_faf2541c0e0a)-[:PERFORMANCE_OF]->(work_1cd9abbbfc71)
MERGE (perf_240a32b5d209)-[:PERFORMANCE_OF]->(work_c8ccafd61842)
MERGE (perf_737579887a14)-[:PERFORMANCE_OF]->(work_3a978448f808)
MERGE (perf_24cae3962643)-[:PERFORMANCE_OF]->(work_7be093476c32)


// composers
MERGE (person_340d64fbb41c)-[:COMPOSED]->(work_9d1baf9ff1cc)
MERGE (person_5a269b32b4c2)-[:COMPOSED]->(work_98d695dbaf1b)
MERGE (person_340d64fbb41c)-[:COMPOSED]->(work_2f5f0b571320)
MERGE (person_340d64fbb41c)-[:COMPOSED]->(work_988648b2a68c)
MERGE (person_340d64fbb41c)-[:COMPOSED]->(work_1ae46f2618b8)
MERGE (person_340d64fbb41c)-[:COMPOSED]->(work_93a77bfc46ef)
MERGE (person_340d64fbb41c)-[:COMPOSED]->(work_1cd9abbbfc71)
MERGE (person_340d64fbb41c)-[:COMPOSED]->(work_c8ccafd61842)
MERGE (person_340d64fbb41c)-[:COMPOSED]->(work_3a978448f808)
MERGE (person_340d64fbb41c)-[:COMPOSED]->(work_7be093476c32)


// place nodes

MERGE (place_d0318297fbb8:Place{ uuid: '709695e4-5fcb-4d7f-8fc0-d0318297fbb8' })
SET place_d0318297fbb8.name = 'Mad Hatter Studios'
SET place_d0318297fbb8.source = 'musicbrainz.org'


// place relationships
MERGE (perf_6138ae4eefb1)-[:HAS_PLACE { type: 'mixed at' }]->(place_d0318297fbb8)
MERGE (perf_6138ae4eefb1)-[:HAS_PLACE { type: 'recorded at' }]->(place_d0318297fbb8)
MERGE (perf_f15941c3d5c2)-[:HAS_PLACE { type: 'mixed at' }]->(place_d0318297fbb8)
MERGE (perf_f15941c3d5c2)-[:HAS_PLACE { type: 'recorded at' }]->(place_d0318297fbb8)
MERGE (perf_faf2541c0e0a)-[:HAS_PLACE { type: 'mixed at' }]->(place_d0318297fbb8)
MERGE (perf_faf2541c0e0a)-[:HAS_PLACE { type: 'recorded at' }]->(place_d0318297fbb8)
MERGE (perf_737579887a14)-[:HAS_PLACE { type: 'mixed at' }]->(place_d0318297fbb8)
MERGE (perf_737579887a14)-[:HAS_PLACE { type: 'recorded at' }]->(place_d0318297fbb8)
MERGE (perf_240a32b5d209)-[:HAS_PLACE { type: 'mixed at' }]->(place_d0318297fbb8)
MERGE (perf_240a32b5d209)-[:HAS_PLACE { type: 'recorded at' }]->(place_d0318297fbb8)
MERGE (perf_264bf52a1a52)-[:HAS_PLACE { type: 'mixed at' }]->(place_d0318297fbb8)
MERGE (perf_264bf52a1a52)-[:HAS_PLACE { type: 'recorded at' }]->(place_d0318297fbb8)
MERGE (perf_24cae3962643)-[:HAS_PLACE { type: 'mixed at' }]->(place_d0318297fbb8)
MERGE (perf_24cae3962643)-[:HAS_PLACE { type: 'recorded at' }]->(place_d0318297fbb8)
MERGE (perf_daeb9f16c481)-[:HAS_PLACE { type: 'mixed at' }]->(place_d0318297fbb8)
MERGE (perf_daeb9f16c481)-[:HAS_PLACE { type: 'recorded at' }]->(place_d0318297fbb8)
MERGE (perf_0ca2686b3a5f)-[:HAS_PLACE { type: 'mixed at' }]->(place_d0318297fbb8)
MERGE (perf_0ca2686b3a5f)-[:HAS_PLACE { type: 'recorded at' }]->(place_d0318297fbb8)
MERGE (perf_e574364cc198)-[:HAS_PLACE { type: 'mixed at' }]->(place_d0318297fbb8)
MERGE (perf_e574364cc198)-[:HAS_PLACE { type: 'recorded at' }]->(place_d0318297fbb8)

MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_6138ae4eefb1)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6138ae4eefb1)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_6138ae4eefb1)
MERGE (person_770ba6cf4573)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_6138ae4eefb1)
MERGE (person_8c2883799052)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_6138ae4eefb1)
MERGE (person_4aef822ea97d)-[:PARTICIPATED_IN { roles: ['producer', 'recording engineer'] }]->(perf_6138ae4eefb1)
MERGE (person_a499d9f33ef6)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_6138ae4eefb1)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_f15941c3d5c2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f15941c3d5c2)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_f15941c3d5c2)
MERGE (person_770ba6cf4573)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_f15941c3d5c2)
MERGE (person_8c2883799052)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_f15941c3d5c2)
MERGE (person_4aef822ea97d)-[:PARTICIPATED_IN { roles: ['producer', 'recording engineer'] }]->(perf_f15941c3d5c2)
MERGE (person_a499d9f33ef6)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_f15941c3d5c2)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_faf2541c0e0a)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_faf2541c0e0a)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_faf2541c0e0a)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_faf2541c0e0a)
MERGE (person_770ba6cf4573)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_faf2541c0e0a)
MERGE (person_8c2883799052)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_faf2541c0e0a)
MERGE (person_4aef822ea97d)-[:PARTICIPATED_IN { roles: ['producer', 'recording engineer'] }]->(perf_faf2541c0e0a)
MERGE (person_a499d9f33ef6)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_faf2541c0e0a)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_737579887a14)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_737579887a14)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_737579887a14)
MERGE (person_4aef822ea97d)-[:PARTICIPATED_IN { roles: ['producer', 'recording engineer'] }]->(perf_737579887a14)
MERGE (person_a499d9f33ef6)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_737579887a14)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_240a32b5d209)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_240a32b5d209)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_240a32b5d209)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_240a32b5d209)
MERGE (person_8c2883799052)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_240a32b5d209)
MERGE (person_4aef822ea97d)-[:PARTICIPATED_IN { roles: ['producer', 'recording engineer'] }]->(perf_240a32b5d209)
MERGE (person_a499d9f33ef6)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_240a32b5d209)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_264bf52a1a52)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_264bf52a1a52)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_264bf52a1a52)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_264bf52a1a52)
MERGE (person_8c2883799052)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_264bf52a1a52)
MERGE (person_4aef822ea97d)-[:PARTICIPATED_IN { roles: ['producer', 'recording engineer'] }]->(perf_264bf52a1a52)
MERGE (person_a499d9f33ef6)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_264bf52a1a52)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_24cae3962643)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_24cae3962643)
MERGE (person_770ba6cf4573)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_24cae3962643)
MERGE (person_4aef822ea97d)-[:PARTICIPATED_IN { roles: ['producer', 'recording engineer'] }]->(perf_24cae3962643)
MERGE (person_a499d9f33ef6)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_24cae3962643)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_daeb9f16c481)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_daeb9f16c481)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_daeb9f16c481)
MERGE (person_770ba6cf4573)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_daeb9f16c481)
MERGE (person_8c2883799052)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_daeb9f16c481)
MERGE (person_4aef822ea97d)-[:PARTICIPATED_IN { roles: ['producer', 'recording engineer'] }]->(perf_daeb9f16c481)
MERGE (person_a499d9f33ef6)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_daeb9f16c481)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_0ca2686b3a5f)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_0ca2686b3a5f)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_0ca2686b3a5f)
MERGE (person_770ba6cf4573)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_0ca2686b3a5f)
MERGE (person_8c2883799052)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_0ca2686b3a5f)
MERGE (person_4aef822ea97d)-[:PARTICIPATED_IN { roles: ['producer', 'recording engineer'] }]->(perf_0ca2686b3a5f)
MERGE (person_a499d9f33ef6)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_0ca2686b3a5f)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_e574364cc198)
MERGE (person_4aef822ea97d)-[:PARTICIPATED_IN { roles: ['producer', 'recording engineer'] }]->(perf_e574364cc198)
MERGE (person_a499d9f33ef6)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e574364cc198)



"""
)