// releases

MERGE (release_ddbf215fcbf6:Release{ uuid: '3b331893-fd63-498e-bdce-ddbf215fcbf6' })
SET release_ddbf215fcbf6.name = 'Encounters'
SET release_ddbf215fcbf6.country = 'AU'
SET release_ddbf215fcbf6.date = '1990'
SET release_ddbf215fcbf6.format = 'CD'
SET release_ddbf215fcbf6.discode = '846 220-2'
SET release_ddbf215fcbf6.discogs = 'https://www.discogs.com/release/11128110'
SET release_ddbf215fcbf6.musicbrainz = 'http://musicbrainz.org/release/3b331893-fd63-498e-bdce-ddbf215fcbf6'
SET release_ddbf215fcbf6.source = 'musicbrainz.org'
SET release_ddbf215fcbf6.timestamp = timestamp()

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
SET person_dbad528aa58e.databases = ['http://id.loc.gov/authorities/names/n84163014', 'https://catalogue.bnf.fr/ark:/12148/cb13895278h', 'https://d-nb.info/gnd/134409361', 'http://snaccooperative.org/ark:/99166/w6dn45cm', 'https://www.worldcat.org/identities/lccn-n84163014']
SET person_dbad528aa58e.musicbrainz = 'https://musicbrainz.org/artist/7ea233ad-c340-4f62-8678-dbad528aa58e'
SET person_dbad528aa58e.isni_list = ['http://isni.org/isni/0000000084120907']
SET person_dbad528aa58e.source = 'musicbrainz.org'
SET person_dbad528aa58e.timestamp = timestamp()

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

MERGE (person_792a7369efb1:Person{ uuid: 'ff59386b-0bdd-4800-a44d-792a7369efb1' }) 
SET person_792a7369efb1.name = 'Mark Isaacs'
SET person_792a7369efb1.gender = 'Male'
SET person_792a7369efb1.country = 'AU'
SET person_792a7369efb1.discogs = 'https://www.discogs.com/artist/1438422'
SET person_792a7369efb1.imdb = 'https://www.imdb.com/name/nm1094315/'
SET person_792a7369efb1.viaf = 'http://viaf.org/viaf/70623008'
SET person_792a7369efb1.wikidata = 'https://www.wikidata.org/wiki/Q20652541'
SET person_792a7369efb1.databases = ['http://id.loc.gov/authorities/names/nr96043015', 'https://nla.gov.au/nla.party-556364', 'https://www.worldcat.org/identities/lccn-nr96043015/']
SET person_792a7369efb1.musicbrainz = 'https://musicbrainz.org/artist/ff59386b-0bdd-4800-a44d-792a7369efb1'
SET person_792a7369efb1.isni_list = ['http://isni.org/isni/000000011474501X']
SET person_792a7369efb1.source = 'musicbrainz.org'
SET person_792a7369efb1.timestamp = timestamp()

MERGE (person_f014a10fb3f2:Person{ uuid: '1fcaf7ef-ecf4-43c3-a5d6-f014a10fb3f2' }) 
SET person_f014a10fb3f2.name = 'Rob Eaton'
SET person_f014a10fb3f2.gender = 'Male'
SET person_f014a10fb3f2.country = 'US'
SET person_f014a10fb3f2.allmusic = 'https://www.allmusic.com/artist/mn0000229578'
SET person_f014a10fb3f2.discogs = 'https://www.discogs.com/artist/255341'
SET person_f014a10fb3f2.wikipedia = 'https://en.wikipedia.org/wiki/Rob_Eaton'
SET person_f014a10fb3f2.databases = ['https://rateyourmusic.com/artist/rob_eaton']
SET person_f014a10fb3f2.musicbrainz = 'https://musicbrainz.org/artist/1fcaf7ef-ecf4-43c3-a5d6-f014a10fb3f2'
SET person_f014a10fb3f2.source = 'musicbrainz.org'
SET person_f014a10fb3f2.timestamp = timestamp()

MERGE (person_106fa16feac8:Person{ uuid: '24cf7017-f2ad-410d-8657-106fa16feac8' }) 
SET person_106fa16feac8.name = 'Martin Benge'
SET person_106fa16feac8.gender = 'Male'
SET person_106fa16feac8.country = 'AU'
SET person_106fa16feac8.discogs = 'https://www.discogs.com/artist/894227'
SET person_106fa16feac8.musicbrainz = 'https://musicbrainz.org/artist/24cf7017-f2ad-410d-8657-106fa16feac8'
SET person_106fa16feac8.source = 'musicbrainz.org'
SET person_106fa16feac8.timestamp = timestamp()
// labels

MERGE (label_1e39bdaa2853:Label{ uuid: 'f851036f-6a2c-4fca-a575-1e39bdaa2853' })
SET label_1e39bdaa2853.name= 'ABC Records'

// performances

MERGE (perf_d378772758ca:Performance{ uuid: 'e3cc69e2-ae2d-4dbf-abe4-d378772758ca' })
SET perf_d378772758ca.name = 'First Encounters'
SET perf_d378772758ca.duration = '3:39'
SET perf_d378772758ca.begin = '1988-12'
SET perf_d378772758ca.end = '1988-12'
SET perf_d378772758ca.source = 'musicbrainz.org'
SET perf_d378772758ca.timestamp = timestamp()

MERGE (perf_a015092adf8e:Performance{ uuid: 'e0aeffb8-853c-4ecd-8923-a015092adf8e' })
SET perf_a015092adf8e.name = 'Exclamation'
SET perf_a015092adf8e.duration = '3:35'
SET perf_a015092adf8e.begin = '1988-12'
SET perf_a015092adf8e.end = '1988-12'
SET perf_a015092adf8e.source = 'musicbrainz.org'
SET perf_a015092adf8e.timestamp = timestamp()

MERGE (perf_e29b537be1d6:Performance{ uuid: 'b203fa7a-04ee-4470-a6dd-e29b537be1d6' })
SET perf_e29b537be1d6.name = 'Incantation'
SET perf_e29b537be1d6.duration = '3:07'
SET perf_e29b537be1d6.begin = '1988-12'
SET perf_e29b537be1d6.end = '1988-12'
SET perf_e29b537be1d6.source = 'musicbrainz.org'
SET perf_e29b537be1d6.timestamp = timestamp()

MERGE (perf_a93aeae26f53:Performance{ uuid: 'e262fc96-4c56-4bd3-899d-a93aeae26f53' })
SET perf_a93aeae26f53.name = 'Rumours'
SET perf_a93aeae26f53.duration = '5:17'
SET perf_a93aeae26f53.begin = '1988-12'
SET perf_a93aeae26f53.end = '1988-12'
SET perf_a93aeae26f53.source = 'musicbrainz.org'
SET perf_a93aeae26f53.timestamp = timestamp()

MERGE (perf_105d7320bc37:Performance{ uuid: '61f04971-d535-4099-8dc9-105d7320bc37' })
SET perf_105d7320bc37.name = 'Jewelette'
SET perf_105d7320bc37.duration = '3:26'
SET perf_105d7320bc37.begin = '1988-12'
SET perf_105d7320bc37.end = '1988-12'
SET perf_105d7320bc37.source = 'musicbrainz.org'
SET perf_105d7320bc37.timestamp = timestamp()

MERGE (perf_5407706c29c0:Performance{ uuid: 'e0f26f4f-f358-40e5-b7c7-5407706c29c0' })
SET perf_5407706c29c0.name = 'Direct Input'
SET perf_5407706c29c0.duration = '4:14'
SET perf_5407706c29c0.begin = '1988-12'
SET perf_5407706c29c0.end = '1988-12'
SET perf_5407706c29c0.source = 'musicbrainz.org'
SET perf_5407706c29c0.timestamp = timestamp()

MERGE (perf_9b7d14cf7264:Performance{ uuid: 'b109316d-0440-45c0-82d6-9b7d14cf7264' })
SET perf_9b7d14cf7264.name = 'Ringside'
SET perf_9b7d14cf7264.duration = '2:19'
SET perf_9b7d14cf7264.begin = '1988-12'
SET perf_9b7d14cf7264.end = '1988-12'
SET perf_9b7d14cf7264.source = 'musicbrainz.org'
SET perf_9b7d14cf7264.timestamp = timestamp()

MERGE (perf_5226bf34262d:Performance{ uuid: 'c8a80e9b-1abc-418e-a1ba-5226bf34262d' })
SET perf_5226bf34262d.name = 'Tai-Min'
SET perf_5226bf34262d.duration = '5:10'
SET perf_5226bf34262d.begin = '1988-12'
SET perf_5226bf34262d.end = '1988-12'
SET perf_5226bf34262d.source = 'musicbrainz.org'
SET perf_5226bf34262d.timestamp = timestamp()



// labels
MERGE (release_ddbf215fcbf6)-[:HAS_LABEL]->(label_1e39bdaa2853)


// tracks
MERGE (release_ddbf215fcbf6)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_d378772758ca)
MERGE (release_ddbf215fcbf6)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_a015092adf8e)
MERGE (release_ddbf215fcbf6)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_e29b537be1d6)
MERGE (release_ddbf215fcbf6)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_a93aeae26f53)
MERGE (release_ddbf215fcbf6)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_105d7320bc37)
MERGE (release_ddbf215fcbf6)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_5407706c29c0)
MERGE (release_ddbf215fcbf6)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_9b7d14cf7264)
MERGE (release_ddbf215fcbf6)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_5226bf34262d)

// works

MERGE (work_f5f81bc9d92b:Work{ uuid: '7b6248f6-8a15-4198-8411-f5f81bc9d92b' })
SET work_f5f81bc9d92b.name = 'Jewelette'
SET work_f5f81bc9d92b.source = 'musicbrainz.org'
SET work_f5f81bc9d92b.timestamp = timestamp()

MERGE (work_a46b74911e5c:Work{ uuid: '7bfac7ea-2688-46b7-adca-a46b74911e5c' })
SET work_a46b74911e5c.name = 'Incantation'
SET work_a46b74911e5c.source = 'musicbrainz.org'
SET work_a46b74911e5c.timestamp = timestamp()

MERGE (work_de0be0358ef0:Work{ uuid: 'e7bfb0a5-a45c-4a45-a2a8-de0be0358ef0' })
SET work_de0be0358ef0.name = 'Rumours'
SET work_de0be0358ef0.source = 'musicbrainz.org'
SET work_de0be0358ef0.timestamp = timestamp()

MERGE (work_07775b42d8ac:Work{ uuid: '069dc6ca-4da7-4c8b-b9f2-07775b42d8ac' })
SET work_07775b42d8ac.name = 'Direct Input'
SET work_07775b42d8ac.source = 'musicbrainz.org'
SET work_07775b42d8ac.timestamp = timestamp()

MERGE (work_c8bde3d4abc6:Work{ uuid: '1c9d7bd1-83a5-4520-9470-c8bde3d4abc6' })
SET work_c8bde3d4abc6.name = 'Ringside'
SET work_c8bde3d4abc6.source = 'musicbrainz.org'
SET work_c8bde3d4abc6.timestamp = timestamp()

MERGE (work_0b97cee0c748:Work{ uuid: 'b55fab36-f5c6-4d06-952f-0b97cee0c748' })
SET work_0b97cee0c748.name = 'Exclamation'
SET work_0b97cee0c748.source = 'musicbrainz.org'
SET work_0b97cee0c748.timestamp = timestamp()

MERGE (work_226860e459f3:Work{ uuid: '6725fd41-5f0e-48b0-85af-226860e459f3' })
SET work_226860e459f3.name = 'Tai-Min'
SET work_226860e459f3.source = 'musicbrainz.org'
SET work_226860e459f3.timestamp = timestamp()

MERGE (work_05f4f364f890:Work{ uuid: 'd5ca2952-a09e-4e8f-984c-05f4f364f890' })
SET work_05f4f364f890.name = 'First Encounters'
SET work_05f4f364f890.source = 'musicbrainz.org'
SET work_05f4f364f890.timestamp = timestamp()


// performances of
MERGE (perf_105d7320bc37)-[:PERFORMANCE_OF]->(work_f5f81bc9d92b)
MERGE (perf_e29b537be1d6)-[:PERFORMANCE_OF]->(work_a46b74911e5c)
MERGE (perf_a93aeae26f53)-[:PERFORMANCE_OF]->(work_de0be0358ef0)
MERGE (perf_5407706c29c0)-[:PERFORMANCE_OF]->(work_07775b42d8ac)
MERGE (perf_9b7d14cf7264)-[:PERFORMANCE_OF]->(work_c8bde3d4abc6)
MERGE (perf_a015092adf8e)-[:PERFORMANCE_OF]->(work_0b97cee0c748)
MERGE (perf_5226bf34262d)-[:PERFORMANCE_OF]->(work_226860e459f3)
MERGE (perf_d378772758ca)-[:PERFORMANCE_OF]->(work_05f4f364f890)


// composers
MERGE (person_792a7369efb1)-[:COMPOSED]->(work_f5f81bc9d92b)
MERGE (person_6f0a331cc1ca)-[:COMPOSED]->(work_a46b74911e5c)
MERGE (person_dbad528aa58e)-[:COMPOSED]->(work_a46b74911e5c)
MERGE (person_792a7369efb1)-[:COMPOSED]->(work_a46b74911e5c)
MERGE (person_6f0a331cc1ca)-[:COMPOSED]->(work_de0be0358ef0)
MERGE (person_dbad528aa58e)-[:COMPOSED]->(work_de0be0358ef0)
MERGE (person_792a7369efb1)-[:COMPOSED]->(work_de0be0358ef0)
MERGE (person_792a7369efb1)-[:COMPOSED]->(work_07775b42d8ac)
MERGE (person_6f0a331cc1ca)-[:COMPOSED]->(work_c8bde3d4abc6)
MERGE (person_dbad528aa58e)-[:COMPOSED]->(work_c8bde3d4abc6)
MERGE (person_6f0a331cc1ca)-[:COMPOSED]->(work_0b97cee0c748)
MERGE (person_dbad528aa58e)-[:COMPOSED]->(work_0b97cee0c748)
MERGE (person_792a7369efb1)-[:COMPOSED]->(work_0b97cee0c748)
MERGE (person_6f0a331cc1ca)-[:COMPOSED]->(work_226860e459f3)
MERGE (person_dbad528aa58e)-[:COMPOSED]->(work_226860e459f3)
MERGE (person_792a7369efb1)-[:COMPOSED]->(work_226860e459f3)
MERGE (person_6f0a331cc1ca)-[:COMPOSED]->(work_05f4f364f890)
MERGE (person_dbad528aa58e)-[:COMPOSED]->(work_05f4f364f890)
MERGE (person_792a7369efb1)-[:COMPOSED]->(work_05f4f364f890)


// place nodes

MERGE (place_20dd53f6e532:Place{ uuid: '7df4ad4d-bceb-434f-9753-20dd53f6e532' })
SET place_20dd53f6e532.name = 'Studios 301'
SET place_20dd53f6e532.source = 'musicbrainz.org'

MERGE (place_6e44f7dfcf98:Place{ uuid: '859fdb68-9363-4ea0-b35a-6e44f7dfcf98' })
SET place_6e44f7dfcf98.name = 'Power Station at BerkleeNYC'
SET place_6e44f7dfcf98.source = 'musicbrainz.org'


// place relationships
MERGE (perf_d378772758ca)-[:HAS_PLACE { type: 'mixed at', begin: '1989-10', end: '1989-10' }]->(place_20dd53f6e532)
MERGE (perf_d378772758ca)-[:HAS_PLACE { type: 'recorded at', begin: '1988-12', end: '1988-12' }]->(place_6e44f7dfcf98)
MERGE (perf_a015092adf8e)-[:HAS_PLACE { type: 'mixed at', begin: '1989-10', end: '1989-10' }]->(place_20dd53f6e532)
MERGE (perf_a015092adf8e)-[:HAS_PLACE { type: 'recorded at', begin: '1988-12', end: '1988-12' }]->(place_6e44f7dfcf98)
MERGE (perf_e29b537be1d6)-[:HAS_PLACE { type: 'mixed at', begin: '1989-10', end: '1989-10' }]->(place_20dd53f6e532)
MERGE (perf_e29b537be1d6)-[:HAS_PLACE { type: 'recorded at', begin: '1988-12', end: '1988-12' }]->(place_6e44f7dfcf98)
MERGE (perf_a93aeae26f53)-[:HAS_PLACE { type: 'mixed at', begin: '1989-10', end: '1989-10' }]->(place_20dd53f6e532)
MERGE (perf_a93aeae26f53)-[:HAS_PLACE { type: 'recorded at', begin: '1988-12', end: '1988-12' }]->(place_6e44f7dfcf98)
MERGE (perf_105d7320bc37)-[:HAS_PLACE { type: 'mixed at', begin: '1989-10', end: '1989-10' }]->(place_20dd53f6e532)
MERGE (perf_105d7320bc37)-[:HAS_PLACE { type: 'recorded at', begin: '1988-12', end: '1988-12' }]->(place_6e44f7dfcf98)
MERGE (perf_5407706c29c0)-[:HAS_PLACE { type: 'mixed at', begin: '1989-10', end: '1989-10' }]->(place_20dd53f6e532)
MERGE (perf_5407706c29c0)-[:HAS_PLACE { type: 'recorded at', begin: '1988-12', end: '1988-12' }]->(place_6e44f7dfcf98)
MERGE (perf_9b7d14cf7264)-[:HAS_PLACE { type: 'mixed at', begin: '1989-10', end: '1989-10' }]->(place_20dd53f6e532)
MERGE (perf_9b7d14cf7264)-[:HAS_PLACE { type: 'recorded at', begin: '1988-12', end: '1988-12' }]->(place_6e44f7dfcf98)
MERGE (perf_5226bf34262d)-[:HAS_PLACE { type: 'mixed at', begin: '1989-10', end: '1989-10' }]->(place_20dd53f6e532)
MERGE (perf_5226bf34262d)-[:HAS_PLACE { type: 'recorded at', begin: '1988-12', end: '1988-12' }]->(place_6e44f7dfcf98)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_d378772758ca)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_d378772758ca)
MERGE (person_792a7369efb1)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_d378772758ca)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_d378772758ca)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a015092adf8e)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_a015092adf8e)
MERGE (person_792a7369efb1)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_a015092adf8e)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a015092adf8e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e29b537be1d6)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e29b537be1d6)
MERGE (person_792a7369efb1)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_e29b537be1d6)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_e29b537be1d6)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a93aeae26f53)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_a93aeae26f53)
MERGE (person_792a7369efb1)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_a93aeae26f53)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a93aeae26f53)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_105d7320bc37)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_105d7320bc37)
MERGE (person_792a7369efb1)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_105d7320bc37)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_105d7320bc37)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_5407706c29c0)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_5407706c29c0)
MERGE (person_792a7369efb1)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_5407706c29c0)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_5407706c29c0)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9b7d14cf7264)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_9b7d14cf7264)
MERGE (person_792a7369efb1)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_9b7d14cf7264)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_9b7d14cf7264)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_5226bf34262d)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_5226bf34262d)
MERGE (person_792a7369efb1)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['piano'] }]->(perf_5226bf34262d)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_5226bf34262d)

