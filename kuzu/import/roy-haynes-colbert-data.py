
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

MERGE (person_4c7f5fcc9599:Person{ uuid: 'a2a72dba-3a08-43c4-859c-4c7f5fcc9599' })
SET person_4c7f5fcc9599.name = 'Jon Batiste'
SET person_4c7f5fcc9599.gender = 'Male'
SET person_4c7f5fcc9599.country = 'US'
SET person_4c7f5fcc9599.discogs = 'http://www.discogs.com/artist/2067949'
SET person_4c7f5fcc9599.imdb = 'http://www.imdb.com/name/nm4456022/'
SET person_4c7f5fcc9599.wikidata = 'http://www.wikidata.org/wiki/Q6272528'
SET person_4c7f5fcc9599.wikipedia = 'https://en.wikipedia.org/wiki/Jon_Batiste'
SET person_4c7f5fcc9599.musicbrainz = 'https://musicbrainz.org/artist/a2a72dba-3a08-43c4-859c-4c7f5fcc9599'
SET person_4c7f5fcc9599.source = 'musicbrainz.org'


MERGE (person_6f0a331cc1ca:Person{ uuid: '2c090b57-5e9d-49c5-9b71-6f0a331cc1ca' })
SET person_6f0a331cc1ca.name = 'Roy Haynes'
SET person_6f0a331cc1ca.gender = 'Male'
SET person_6f0a331cc1ca.country = 'US'
SET person_6f0a331cc1ca.wikipedia = 'http://en.wikipedia.org/wiki/Roy_Haynes'
SET person_6f0a331cc1ca.viaf = 'http://viaf.org/viaf/84975999'
SET person_6f0a331cc1ca.allmusic = 'http://www.allmusic.com/artist/mn0000290464'
SET person_6f0a331cc1ca.bbc = 'http://www.bbc.co.uk/music/artists/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.discogs = 'http://www.discogs.com/artist/255556'
SET person_6f0a331cc1ca.imdb = 'http://www.imdb.com/name/nm0371542/'
SET person_6f0a331cc1ca.wikidata = 'http://www.wikidata.org/wiki/Q448235'
SET person_6f0a331cc1ca.musicbrainz = 'https://musicbrainz.org/artist/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.source = 'musicbrainz.org'


MERGE (person_8e102a36f7a5:Person{ uuid: '9f73aa40-9c79-4dd5-b699-8e102a36f7a5' })
SET person_8e102a36f7a5.name = 'Stay Human'
SET person_8e102a36f7a5.country = 'US'
SET person_8e102a36f7a5.wikipedia = 'https://en.wikipedia.org/wiki/Stay_Human_(band)'
SET person_8e102a36f7a5.musicbrainz = 'https://musicbrainz.org/artist/9f73aa40-9c79-4dd5-b699-8e102a36f7a5'
SET person_8e102a36f7a5.source = 'musicbrainz.org'


// performances

MERGE (perf_81092fa4290e:Performance{ uuid: 'f230ca2b-6067-477b-b632-81092fa4290e' })
SET perf_81092fa4290e.name = 'James'
SET perf_81092fa4290e.disambiguation = 'live, 2016-04-21: The Late Show with Stephen Colbert'
SET perf_81092fa4290e.begin_date = '2016-04-21'
SET perf_81092fa4290e.end_date = '2016-04-21'
SET perf_81092fa4290e.source = 'musicbrainz.org'


// works

MERGE (person_f8091d98cf25:Person{ uuid: '7daac7f9-8fcc-485f-a14f-f8091d98cf25' })
SET person_f8091d98cf25.name = 'Pat Metheny'
SET person_f8091d98cf25.gender = 'Male'
SET person_f8091d98cf25.country = 'US'
SET person_f8091d98cf25.wikipedia = 'http://en.wikipedia.org/wiki/Pat_Metheny'
SET person_f8091d98cf25.viaf = 'http://viaf.org/viaf/22188874'
SET person_f8091d98cf25.allmusic = 'http://www.allmusic.com/artist/mn0000179698'
SET person_f8091d98cf25.bbc = 'http://www.bbc.co.uk/music/artists/7daac7f9-8fcc-485f-a14f-f8091d98cf25'
SET person_f8091d98cf25.discogs = 'http://www.discogs.com/artist/20185'
SET person_f8091d98cf25.imdb = 'http://www.imdb.com/name/nm0582533/'
SET person_f8091d98cf25.wikidata = 'http://www.wikidata.org/wiki/Q213887'
SET person_f8091d98cf25.musicbrainz = 'https://musicbrainz.org/artist/7daac7f9-8fcc-485f-a14f-f8091d98cf25'
SET person_f8091d98cf25.source = 'musicbrainz.org'


MERGE (person_0ad7756dd538:Person{ uuid: '210b51ef-bece-44c6-aa94-0ad7756dd538' })
SET person_0ad7756dd538.name = 'Lyle Mays'
SET person_0ad7756dd538.gender = 'Male'
SET person_0ad7756dd538.country = 'US'
SET person_0ad7756dd538.wikipedia = 'http://en.wikipedia.org/wiki/Lyle_Mays'
SET person_0ad7756dd538.viaf = 'http://viaf.org/viaf/39562612'
SET person_0ad7756dd538.allmusic = 'http://www.allmusic.com/artist/mn0000171015'
SET person_0ad7756dd538.discogs = 'http://www.discogs.com/artist/222583'
SET person_0ad7756dd538.wikidata = 'http://www.wikidata.org/wiki/Q963426'
SET person_0ad7756dd538.databases = ['http://rateyourmusic.com/artist/lyle_mays']
SET person_0ad7756dd538.musicbrainz = 'https://musicbrainz.org/artist/210b51ef-bece-44c6-aa94-0ad7756dd538'
SET person_0ad7756dd538.source = 'musicbrainz.org'


MERGE (work_567b5ea2c2bf:Work{ uuid: 'de481d05-d2a8-369d-b1dc-567b5ea2c2bf' })
SET work_567b5ea2c2bf.name = 'James'
SET work_567b5ea2c2bf.iswc = 'T-070.241.328-2'
SET work_567b5ea2c2bf.source = 'musicbrainz.org'



// performances of
MERGE (perf_81092fa4290e)-[:PERFORMANCE_OF]->(work_567b5ea2c2bf)


// composers
MERGE (person_0ad7756dd538)-[:COMPOSED]->(work_567b5ea2c2bf)
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_567b5ea2c2bf)


// place nodes

MERGE (place_487980a9febf:Place{ uuid: '51eb5f29-b535-411c-9676-487980a9febf' })
SET place_487980a9febf.name = 'Ed Sullivan Theater'
SET place_487980a9febf.address = '1697, Broadway, Lincoln Square, Manhattan, New York County, NYC, New York, 10019, United States of America'
SET place_487980a9febf.lat = '40.7637878'
SET place_487980a9febf.lng = '-73.9828182'
SET place_487980a9febf.source = 'musicbrainz.org'


// place relationships
MERGE (perf_81092fa4290e)-[:HAS_PLACE { type: 'recorded at', begin_date: '2016-04-21', end_date: '2016-04-21' }]->(place_487980a9febf)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_81092fa4290e)
MERGE (person_8e102a36f7a5)-[:PARTICIPATED_IN { roles: ['unknown'] }]->(perf_81092fa4290e)
MERGE (person_4c7f5fcc9599)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_81092fa4290e)



"""
)