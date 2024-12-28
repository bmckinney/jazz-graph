
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_2f2fc4a8a3f6:Release{ uuid: '42bceff9-bd45-4ace-b17d-2f2fc4a8a3f6' })
SET release_2f2fc4a8a3f6.name = 'Now He Sings, Now He Sobs'
SET release_2f2fc4a8a3f6.country = 'GR'
SET release_2f2fc4a8a3f6.date = '1968'
SET release_2f2fc4a8a3f6.format = '12" Vinyl'
SET release_2f2fc4a8a3f6.discode = 'SS 18039'
SET release_2f2fc4a8a3f6.discogs = 'https://www.discogs.com/release/12927682'
SET release_2f2fc4a8a3f6.musicbrainz = 'http://musicbrainz.org/release/42bceff9-bd45-4ace-b17d-2f2fc4a8a3f6'
SET release_2f2fc4a8a3f6.source = 'musicbrainz.org'


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


MERGE (person_be027b7bb16e:Person{ uuid: 'd214235c-cf6f-4c8a-bf68-be027b7bb16e' }) 
SET person_be027b7bb16e.name = 'Miroslav Vitouš'
SET person_be027b7bb16e.gender = 'Male'
SET person_be027b7bb16e.country = 'CZ'
SET person_be027b7bb16e.allmusic = 'https://www.allmusic.com/artist/mn0000499683'
SET person_be027b7bb16e.bbc = 'https://www.bbc.co.uk/music/artists/d214235c-cf6f-4c8a-bf68-be027b7bb16e'
SET person_be027b7bb16e.discogs = 'https://www.discogs.com/artist/128396'
SET person_be027b7bb16e.imdb = 'https://www.imdb.com/name/nm1008417/'
SET person_be027b7bb16e.viaf = 'http://viaf.org/viaf/49409692'
SET person_be027b7bb16e.wikidata = 'https://www.wikidata.org/wiki/Q558162'
SET person_be027b7bb16e.wikipedia = 'https://en.wikipedia.org/wiki/Miroslav_Vitou%C5%A1'
SET person_be027b7bb16e.databases = ['http://d-nb.info/gnd/134547616', 'http://id.loc.gov/authorities/names/n82020005', 'https://catalogue.bnf.fr/ark:/12148/cb13900892t', 'https://www.worldcat.org/identities/lccn-n82020005']
SET person_be027b7bb16e.musicbrainz = 'https://musicbrainz.org/artist/d214235c-cf6f-4c8a-bf68-be027b7bb16e'
SET person_be027b7bb16e.isni_list = ['http://isni.org/isni/000000008128130X']
SET person_be027b7bb16e.source = 'musicbrainz.org'

// labels

MERGE (label_a76d48f0af5a:Label{ uuid: 'd57411c4-1156-408d-9c5e-a76d48f0af5a' })
SET label_a76d48f0af5a.name= 'Solid State Records'

// performances

MERGE (perf_c1dda258cb69:Performance{ uuid: 'd5abc135-70df-4752-a001-c1dda258cb69' })
SET perf_c1dda258cb69.name = 'Steps - What Was'
SET perf_c1dda258cb69.duration = '13:53'
SET perf_c1dda258cb69.begin_date = '1968-03-19'
SET perf_c1dda258cb69.end_date = '1968-03-19'
SET perf_c1dda258cb69.source = 'musicbrainz.org'


MERGE (perf_e558008c68bd:Performance{ uuid: 'c2f9300b-dac6-4a90-b6e4-e558008c68bd' })
SET perf_e558008c68bd.name = 'Matrix'
SET perf_e558008c68bd.duration = '6:29'
SET perf_e558008c68bd.begin_date = '1968-03-14'
SET perf_e558008c68bd.end_date = '1968-03-14'
SET perf_e558008c68bd.source = 'musicbrainz.org'


MERGE (perf_b22e43892da0:Performance{ uuid: 'b4972ab0-254c-476a-a344-b22e43892da0' })
SET perf_b22e43892da0.name = 'How He Sings, Now He Sobs'
SET perf_b22e43892da0.duration = '7:05'
SET perf_b22e43892da0.begin_date = '1968-03-19'
SET perf_b22e43892da0.end_date = '1968-03-19'
SET perf_b22e43892da0.source = 'musicbrainz.org'


MERGE (perf_236e454731f1:Performance{ uuid: 'd5c76003-2ca8-4fdd-879f-236e454731f1' })
SET perf_236e454731f1.name = 'Now He Beats the Drums, Now He Stops'
SET perf_236e454731f1.duration = '10:40'
SET perf_236e454731f1.begin_date = '1968-03-14'
SET perf_236e454731f1.end_date = '1968-03-14'
SET perf_236e454731f1.source = 'musicbrainz.org'


MERGE (perf_2106c0258af1:Performance{ uuid: '637e6877-6f7c-4080-b96a-2106c0258af1' })
SET perf_2106c0258af1.name = 'The Law of Falling and Catching Up'
SET perf_2106c0258af1.duration = '2:28'
SET perf_2106c0258af1.begin_date = '1968-03-14'
SET perf_2106c0258af1.end_date = '1968-03-14'
SET perf_2106c0258af1.source = 'musicbrainz.org'




// labels
MERGE (release_2f2fc4a8a3f6)-[:HAS_LABEL]->(label_a76d48f0af5a)


// tracks
MERGE (release_2f2fc4a8a3f6)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_c1dda258cb69)
MERGE (release_2f2fc4a8a3f6)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_e558008c68bd)
MERGE (release_2f2fc4a8a3f6)-[:HAS_TRACK {name: 'B1', sequence: 3}]->(perf_b22e43892da0)
MERGE (release_2f2fc4a8a3f6)-[:HAS_TRACK {name: 'B2', sequence: 4}]->(perf_236e454731f1)
MERGE (release_2f2fc4a8a3f6)-[:HAS_TRACK {name: 'B3', sequence: 5}]->(perf_2106c0258af1)

// works

MERGE (work_3c31ab032b24:Work{ uuid: '2cf1115d-6f0f-4934-a349-3c31ab032b24' })
SET work_3c31ab032b24.name = 'What Was'
SET work_3c31ab032b24.iswc = 'T-904.321.369-0'
SET work_3c31ab032b24.type = 'Song'
SET work_3c31ab032b24.source = 'musicbrainz.org'


MERGE (work_735e22928ba8:Work{ uuid: 'baf45e22-6117-4a45-b78b-735e22928ba8' })
SET work_735e22928ba8.name = 'Matrix'
SET work_735e22928ba8.type = 'Song'
SET work_735e22928ba8.source = 'musicbrainz.org'



// performances of
MERGE (perf_c1dda258cb69)-[:PERFORMANCE_OF]->(work_3c31ab032b24)
MERGE (perf_e558008c68bd)-[:PERFORMANCE_OF]->(work_735e22928ba8)


// composers
MERGE (person_5a269b32b4c2)-[:COMPOSED]->(work_3c31ab032b24)
MERGE (person_5a269b32b4c2)-[:COMPOSED]->(work_735e22928ba8)


// place nodes

MERGE (place_339e33216fe4:Place{ uuid: '5b2dde24-1bec-470b-9450-339e33216fe4' })
SET place_339e33216fe4.name = 'A&R Recording Studio'
SET place_339e33216fe4.source = 'musicbrainz.org'


// place relationships
MERGE (perf_c1dda258cb69)-[:HAS_PLACE { type: 'recorded at', begin_date: '1968-03-19', end_date: '1968-03-19' }]->(place_339e33216fe4)
MERGE (perf_e558008c68bd)-[:HAS_PLACE { type: 'recorded at', begin_date: '1968-03-14', end_date: '1968-03-14' }]->(place_339e33216fe4)
MERGE (perf_b22e43892da0)-[:HAS_PLACE { type: 'recorded at', begin_date: '1968-03-19', end_date: '1968-03-19' }]->(place_339e33216fe4)
MERGE (perf_236e454731f1)-[:HAS_PLACE { type: 'recorded at', begin_date: '1968-03-14', end_date: '1968-03-14' }]->(place_339e33216fe4)
MERGE (perf_2106c0258af1)-[:HAS_PLACE { type: 'recorded at', begin_date: '1968-03-14', end_date: '1968-03-14' }]->(place_339e33216fe4)

MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_c1dda258cb69)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_c1dda258cb69)
MERGE (person_be027b7bb16e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_c1dda258cb69)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e558008c68bd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e558008c68bd)
MERGE (person_be027b7bb16e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e558008c68bd)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b22e43892da0)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_b22e43892da0)
MERGE (person_be027b7bb16e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_b22e43892da0)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_236e454731f1)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_236e454731f1)
MERGE (person_be027b7bb16e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_236e454731f1)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2106c0258af1)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_2106c0258af1)
MERGE (person_be027b7bb16e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_2106c0258af1)



"""
)