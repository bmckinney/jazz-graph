
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""


MERGE (release_51005f3e9dd3:Release{ uuid: 'ab9af066-a61b-32ce-9cfb-51005f3e9dd3' })
SET release_51005f3e9dd3.name = 'Cracklin\\''
SET release_51005f3e9dd3.country = 'US'
SET release_51005f3e9dd3.date = '1994'
SET release_51005f3e9dd3.format = 'CD'
SET release_51005f3e9dd3.discode = 'OJCCD-818-2'
SET release_51005f3e9dd3.musicbrainz = 'http://musicbrainz.org/release/ab9af066-a61b-32ce-9cfb-51005f3e9dd3'
SET release_51005f3e9dd3.source = 'musicbrainz.org'


MERGE (person_685553120062:Person{ uuid: '26608e21-906d-4d33-b910-685553120062' })
SET person_685553120062.name = 'Booker Ervin'
SET person_685553120062.gender = 'Male'
SET person_685553120062.country = 'US'
SET person_685553120062.wikipedia = 'http://en.wikipedia.org/wiki/Booker_Ervin'
SET person_685553120062.viaf = 'http://viaf.org/viaf/14958104'
SET person_685553120062.allmusic = 'http://www.allmusic.com/artist/mn0000097426'
SET person_685553120062.discogs = 'http://www.discogs.com/artist/253063'
SET person_685553120062.wikidata = 'http://www.wikidata.org/wiki/Q892998'
SET person_685553120062.musicbrainz = 'https://musicbrainz.org/artist/26608e21-906d-4d33-b910-685553120062'
SET person_685553120062.source = 'musicbrainz.org'


MERGE (person_c2d5d5613c56:Person{ uuid: '95493156-7000-41b6-bc34-c2d5d5613c56' })
SET person_c2d5d5613c56.name = 'Ronnie Mathews'
SET person_c2d5d5613c56.gender = 'Male'
SET person_c2d5d5613c56.country = 'US'
SET person_c2d5d5613c56.wikipedia = 'http://en.wikipedia.org/wiki/Ronnie_Mathews'
SET person_c2d5d5613c56.allmusic = 'http://www.allmusic.com/artist/mn0000278048'
SET person_c2d5d5613c56.discogs = 'http://www.discogs.com/artist/650343'
SET person_c2d5d5613c56.wikidata = 'http://www.wikidata.org/wiki/Q2166025'
SET person_c2d5d5613c56.musicbrainz = 'https://musicbrainz.org/artist/95493156-7000-41b6-bc34-c2d5d5613c56'
SET person_c2d5d5613c56.source = 'musicbrainz.org'


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


MERGE (person_05d508e09a73:Person{ uuid: 'f0707f1d-55e1-46b6-8a9c-05d508e09a73' })
SET person_05d508e09a73.name = 'Rudy van Gelder'
SET person_05d508e09a73.gender = 'Male'
SET person_05d508e09a73.country = 'US'
SET person_05d508e09a73.wikipedia = 'http://en.wikipedia.org/wiki/Rudy_Van_Gelder'
SET person_05d508e09a73.viaf = 'http://viaf.org/viaf/33997197'
SET person_05d508e09a73.allmusic = 'http://www.allmusic.com/artist/mn0000305301'
SET person_05d508e09a73.discogs = 'http://www.discogs.com/artist/252966'
SET person_05d508e09a73.wikidata = 'http://www.wikidata.org/wiki/Q945681'
SET person_05d508e09a73.databases = ['http://rateyourmusic.com/artist/rudy_van_gelder']
SET person_05d508e09a73.musicbrainz = 'https://musicbrainz.org/artist/f0707f1d-55e1-46b6-8a9c-05d508e09a73'
SET person_05d508e09a73.isni_list = ['http://isni.org/isni/0000000019691076']
SET person_05d508e09a73.source = 'musicbrainz.org'


MERGE (person_53bed7cad162:Person{ uuid: 'c3fbbdb0-6383-496f-81d0-53bed7cad162' })
SET person_53bed7cad162.name = 'Larry Ridley'
SET person_53bed7cad162.gender = 'Male'
SET person_53bed7cad162.country = 'US'
SET person_53bed7cad162.wikipedia = 'http://en.wikipedia.org/wiki/Larry_Ridley'
SET person_53bed7cad162.viaf = 'http://viaf.org/viaf/37104009'
SET person_53bed7cad162.discogs = 'http://www.discogs.com/artist/264870'
SET person_53bed7cad162.wikidata = 'http://www.wikidata.org/wiki/Q1724922'
SET person_53bed7cad162.musicbrainz = 'https://musicbrainz.org/artist/c3fbbdb0-6383-496f-81d0-53bed7cad162'
SET person_53bed7cad162.source = 'musicbrainz.org'

// labels

MERGE (label_f72e264c0f66:Label{ uuid: '11847c89-4b2c-4866-84c3-f72e264c0f66' })
SET label_f72e264c0f66.name= 'Prestige'

// performances

MERGE (perf_2865981e2b0c:Performance{ uuid: '9c407e75-ea4d-4b1c-9f44-2865981e2b0c' })
SET perf_2865981e2b0c.name = 'Scoochie'
SET perf_2865981e2b0c.duration = '5:53'
SET perf_2865981e2b0c.begin_date = '1963-04-10'
SET perf_2865981e2b0c.end_date = '1963-04-10'
SET perf_2865981e2b0c.source = 'musicbrainz.org'


MERGE (perf_fb2f7250c8d2:Performance{ uuid: 'a582296e-39ea-446f-96c1-fb2f7250c8d2' })
SET perf_fb2f7250c8d2.name = 'Dorian'
SET perf_fb2f7250c8d2.duration = '6:48'
SET perf_fb2f7250c8d2.begin_date = '1963-04-10'
SET perf_fb2f7250c8d2.end_date = '1963-04-10'
SET perf_fb2f7250c8d2.source = 'musicbrainz.org'


MERGE (perf_346f6ab4efb2:Performance{ uuid: '87b62749-e545-4c04-99e1-346f6ab4efb2' })
SET perf_346f6ab4efb2.name = 'Sketch of Melba'
SET perf_346f6ab4efb2.duration = '7:37'
SET perf_346f6ab4efb2.begin_date = '1963-04-10'
SET perf_346f6ab4efb2.end_date = '1963-04-10'
SET perf_346f6ab4efb2.source = 'musicbrainz.org'


MERGE (perf_0bd288baf159:Performance{ uuid: '35be5a56-5c49-4118-9876-0bd288baf159' })
SET perf_0bd288baf159.name = 'Honeydew'
SET perf_0bd288baf159.duration = '3:46'
SET perf_0bd288baf159.begin_date = '1963-04-10'
SET perf_0bd288baf159.end_date = '1963-04-10'
SET perf_0bd288baf159.source = 'musicbrainz.org'


MERGE (perf_b4ac1bfbd494:Performance{ uuid: '5cbe35e7-4343-4ca6-a1db-b4ac1bfbd494' })
SET perf_b4ac1bfbd494.name = 'Under Paris Skies'
SET perf_b4ac1bfbd494.duration = '7:40'
SET perf_b4ac1bfbd494.begin_date = '1963-04-10'
SET perf_b4ac1bfbd494.end_date = '1963-04-10'
SET perf_b4ac1bfbd494.source = 'musicbrainz.org'


MERGE (perf_437b5ae06389:Performance{ uuid: '89b33262-bd32-49f3-9bcc-437b5ae06389' })
SET perf_437b5ae06389.name = 'Bad News Blues'
SET perf_437b5ae06389.duration = '6:49'
SET perf_437b5ae06389.begin_date = '1963-04-10'
SET perf_437b5ae06389.end_date = '1963-04-10'
SET perf_437b5ae06389.source = 'musicbrainz.org'




// labels
MERGE (release_51005f3e9dd3)-[:HAS_LABEL]->(label_f72e264c0f66)


// tracks
MERGE (release_51005f3e9dd3)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_2865981e2b0c)
MERGE (release_51005f3e9dd3)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_fb2f7250c8d2)
MERGE (release_51005f3e9dd3)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_346f6ab4efb2)
MERGE (release_51005f3e9dd3)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_0bd288baf159)
MERGE (release_51005f3e9dd3)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_b4ac1bfbd494)
MERGE (release_51005f3e9dd3)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_437b5ae06389)

// works

MERGE (person_e7a4eae7d725:Person{ uuid: 'fa8b0006-69cd-429e-a061-e7a4eae7d725' })
SET person_e7a4eae7d725.name = 'Hubert Giraud'
SET person_e7a4eae7d725.gender = 'Male'
SET person_e7a4eae7d725.country = 'FR'
SET person_e7a4eae7d725.wikipedia = 'http://en.wikipedia.org/wiki/Hubert_Giraud'
SET person_e7a4eae7d725.discogs = 'http://www.discogs.com/artist/1011050'
SET person_e7a4eae7d725.discogs = 'http://www.discogs.com/artist/648196'
SET person_e7a4eae7d725.wikidata = 'http://www.wikidata.org/wiki/Q3142015'
SET person_e7a4eae7d725.musicbrainz = 'https://musicbrainz.org/artist/fa8b0006-69cd-429e-a061-e7a4eae7d725'
SET person_e7a4eae7d725.source = 'musicbrainz.org'


MERGE (person_91075fd0f5af:Person{ uuid: '7e198258-7093-46ac-a71e-91075fd0f5af' })
SET person_91075fd0f5af.name = 'Randy Weston'
SET person_91075fd0f5af.gender = 'Male'
SET person_91075fd0f5af.country = 'US'
SET person_91075fd0f5af.wikipedia = 'http://en.wikipedia.org/wiki/Randy_Weston'
SET person_91075fd0f5af.viaf = 'http://viaf.org/viaf/24788821'
SET person_91075fd0f5af.allmusic = 'http://www.allmusic.com/artist/mn0000396908'
SET person_91075fd0f5af.discogs = 'http://www.discogs.com/artist/281957'
SET person_91075fd0f5af.wikidata = 'http://www.wikidata.org/wiki/Q1371187'
SET person_91075fd0f5af.databases = ['https://rateyourmusic.com/artist/randy_weston']
SET person_91075fd0f5af.musicbrainz = 'https://musicbrainz.org/artist/7e198258-7093-46ac-a71e-91075fd0f5af'
SET person_91075fd0f5af.isni_list = ['http://isni.org/isni/0000000081037964']
SET person_91075fd0f5af.source = 'musicbrainz.org'


MERGE (work_d6ef04098a09:Work{ uuid: '253f917b-6ed7-4051-90ae-d6ef04098a09' })
SET work_d6ef04098a09.name = 'Scoochie'
SET work_d6ef04098a09.type = 'Song'
SET work_d6ef04098a09.source = 'musicbrainz.org'


MERGE (work_e65155869d84:Work{ uuid: '45ad7883-9c70-4fca-a299-e65155869d84' })
SET work_e65155869d84.name = 'Dorian'
SET work_e65155869d84.type = 'Song'
SET work_e65155869d84.source = 'musicbrainz.org'


MERGE (work_85aa1b85bd22:Work{ uuid: '2ef881bc-2582-429c-abb9-85aa1b85bd22' })
SET work_85aa1b85bd22.name = 'Sketch of Melba'
SET work_85aa1b85bd22.type = 'Song'
SET work_85aa1b85bd22.source = 'musicbrainz.org'


MERGE (work_05894933adb6:Work{ uuid: '9fe1774b-bcfd-49de-8596-05894933adb6' })
SET work_05894933adb6.name = 'Honeydew'
SET work_05894933adb6.type = 'Song'
SET work_05894933adb6.source = 'musicbrainz.org'


MERGE (work_9daf98dcd262:Work{ uuid: 'cf05712e-97a4-4038-8c9e-9daf98dcd262' })
SET work_9daf98dcd262.name = 'Under Paris Skies'
SET work_9daf98dcd262.type = 'Song'
SET work_9daf98dcd262.source = 'musicbrainz.org'


MERGE (work_749894e93196:Work{ uuid: '8106441b-f893-4dcb-a5b4-749894e93196' })
SET work_749894e93196.name = 'Bad News Blues'
SET work_749894e93196.type = 'Song'
SET work_749894e93196.source = 'musicbrainz.org'



// performances of
MERGE (perf_2865981e2b0c)-[:PERFORMANCE_OF]->(work_d6ef04098a09)
MERGE (perf_fb2f7250c8d2)-[:PERFORMANCE_OF]->(work_e65155869d84)
MERGE (perf_346f6ab4efb2)-[:PERFORMANCE_OF]->(work_85aa1b85bd22)
MERGE (perf_0bd288baf159)-[:PERFORMANCE_OF]->(work_05894933adb6)
MERGE (perf_b4ac1bfbd494)-[:PERFORMANCE_OF]->(work_9daf98dcd262)
MERGE (perf_437b5ae06389)-[:PERFORMANCE_OF]->(work_749894e93196)


// composers
MERGE (person_685553120062)-[:COMPOSED]->(work_d6ef04098a09)
MERGE (person_c2d5d5613c56)-[:COMPOSED]->(work_e65155869d84)
MERGE (person_91075fd0f5af)-[:COMPOSED]->(work_85aa1b85bd22)
MERGE (person_c2d5d5613c56)-[:COMPOSED]->(work_05894933adb6)
MERGE (person_e7a4eae7d725)-[:COMPOSED]->(work_9daf98dcd262)
MERGE (person_6f0a331cc1ca)-[:COMPOSED]->(work_749894e93196)


// place nodes

MERGE (place_569fa8b97644:Place{ uuid: '1165ef7d-371c-4e03-98db-569fa8b97644' })
SET place_569fa8b97644.name = 'Van Gelder Studio'
SET place_569fa8b97644.address = '445, Sylvan Avenue, Englewood Cliffs, Bergen County, New Jersey, 07632, United States of America'
SET place_569fa8b97644.lat = '40.8764374074488'
SET place_569fa8b97644.lng = '-73.9519546846822'
SET place_569fa8b97644.source = 'musicbrainz.org'


// place relationships
MERGE (perf_2865981e2b0c)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-04-10', end_date: '1963-04-10' }]->(place_569fa8b97644)
MERGE (perf_fb2f7250c8d2)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-04-10', end_date: '1963-04-10' }]->(place_569fa8b97644)
MERGE (perf_346f6ab4efb2)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-04-10', end_date: '1963-04-10' }]->(place_569fa8b97644)
MERGE (perf_0bd288baf159)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-04-10', end_date: '1963-04-10' }]->(place_569fa8b97644)
MERGE (perf_b4ac1bfbd494)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-04-10', end_date: '1963-04-10' }]->(place_569fa8b97644)
MERGE (perf_437b5ae06389)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-04-10', end_date: '1963-04-10' }]->(place_569fa8b97644)

MERGE (person_685553120062)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_2865981e2b0c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_2865981e2b0c)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2865981e2b0c)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_2865981e2b0c)
MERGE (person_685553120062)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_fb2f7250c8d2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_fb2f7250c8d2)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_fb2f7250c8d2)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_fb2f7250c8d2)
MERGE (person_685553120062)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_346f6ab4efb2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_346f6ab4efb2)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_346f6ab4efb2)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_346f6ab4efb2)
MERGE (person_685553120062)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_0bd288baf159)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_0bd288baf159)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_0bd288baf159)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_0bd288baf159)
MERGE (person_685553120062)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_b4ac1bfbd494)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_b4ac1bfbd494)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b4ac1bfbd494)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_b4ac1bfbd494)
MERGE (person_685553120062)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_437b5ae06389)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_437b5ae06389)
MERGE (person_c2d5d5613c56)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_437b5ae06389)
MERGE (person_53bed7cad162)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_437b5ae06389)


"""
)