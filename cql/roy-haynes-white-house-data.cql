
// performers

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
SET person_6f0a331cc1ca.timestamp = timestamp()

MERGE (person_5a269b32b4c2:Person{ uuid: '8446fcca-109e-4c6d-a2ff-5a269b32b4c2' })
SET person_5a269b32b4c2.name = 'Chick Corea'
SET person_5a269b32b4c2.gender = 'Male'
SET person_5a269b32b4c2.country = 'US'
SET person_5a269b32b4c2.wikipedia = 'http://en.wikipedia.org/wiki/Chick_Corea'
SET person_5a269b32b4c2.viaf = 'http://viaf.org/viaf/37337806'
SET person_5a269b32b4c2.allmusic = 'http://www.allmusic.com/artist/mn0000110541'
SET person_5a269b32b4c2.bbc = 'http://www.bbc.co.uk/music/artists/8446fcca-109e-4c6d-a2ff-5a269b32b4c2'
SET person_5a269b32b4c2.discogs = 'http://www.discogs.com/artist/37731'
SET person_5a269b32b4c2.wikidata = 'http://www.wikidata.org/wiki/Q192465'
SET person_5a269b32b4c2.discographies = ['http://www.chickcorea.com/discography.html']
SET person_5a269b32b4c2.databases = ['https://rateyourmusic.com/artist/chick_corea']
SET person_5a269b32b4c2.musicbrainz = 'https://musicbrainz.org/artist/8446fcca-109e-4c6d-a2ff-5a269b32b4c2'
SET person_5a269b32b4c2.source = 'musicbrainz.org'
SET person_5a269b32b4c2.timestamp = timestamp()

MERGE (person_be027b7bb16e:Person{ uuid: 'd214235c-cf6f-4c8a-bf68-be027b7bb16e' })
SET person_be027b7bb16e.name = 'Miroslav Vitouš'
SET person_be027b7bb16e.gender = 'Male'
SET person_be027b7bb16e.country = 'CZ'
SET person_be027b7bb16e.wikipedia = 'http://en.wikipedia.org/wiki/Miroslav_Vitou%C5%A1'
SET person_be027b7bb16e.viaf = 'http://viaf.org/viaf/49409692'
SET person_be027b7bb16e.allmusic = 'http://www.allmusic.com/artist/mn0000499683'
SET person_be027b7bb16e.bbc = 'http://www.bbc.co.uk/music/artists/d214235c-cf6f-4c8a-bf68-be027b7bb16e'
SET person_be027b7bb16e.discogs = 'http://www.discogs.com/artist/128396'
SET person_be027b7bb16e.wikidata = 'http://www.wikidata.org/wiki/Q558162'
SET person_be027b7bb16e.musicbrainz = 'https://musicbrainz.org/artist/d214235c-cf6f-4c8a-bf68-be027b7bb16e'
SET person_be027b7bb16e.source = 'musicbrainz.org'
SET person_be027b7bb16e.timestamp = timestamp()

// works

MERGE (work_268199324401:Work{ uuid: '048b4b7a-07c4-3e33-959f-268199324401' })
SET work_268199324401.name = 'Autumn Leaves'
SET work_268199324401.iswc = 'T-070.002.297-4'
SET work_268199324401.type = 'Song'
SET work_268199324401.wikidata = 'http://www.wikidata.org/wiki/Q789392'
SET work_268199324401.wikipedia = 'https://en.wikipedia.org/wiki/Autumn_Leaves_(1945_song)'
SET work_268199324401.musicbrainz = 'https://musicbrainz.org/work/048b4b7a-07c4-3e33-959f-268199324401'
SET work_268199324401.source = 'musicbrainz.org'
SET work_268199324401.timestamp = timestamp()

MERGE (person_635888a66dea:Person{ uuid: '114ec00a-c6cf-42cf-af03-635888a66dea' })
SET person_635888a66dea.name = 'Joseph Kosma'
SET person_635888a66dea.gender = 'Male'
SET person_635888a66dea.country = 'FR'
SET person_635888a66dea.wikipedia = 'http://en.wikipedia.org/wiki/Joseph_Kosma'
SET person_635888a66dea.viaf = 'http://viaf.org/viaf/10033644'
SET person_635888a66dea.discogs = 'http://www.discogs.com/artist/445911'
SET person_635888a66dea.wikidata = 'http://www.wikidata.org/wiki/Q213661'
SET person_635888a66dea.musicbrainz = 'https://musicbrainz.org/artist/114ec00a-c6cf-42cf-af03-635888a66dea'
SET person_635888a66dea.source = 'musicbrainz.org'
SET person_635888a66dea.timestamp = timestamp()

MERGE (person_635888a66dea)-[:COMPOSED]->(work_268199324401)

MERGE (work_ecaeddf44a98:Work{ uuid: 'ee619352-ce88-3fe2-a065-ecaeddf44a98' })
SET work_ecaeddf44a98.name = 'Rhythm-a-Ning'
SET work_ecaeddf44a98.source = 'musicbrainz.org'
SET work_ecaeddf44a98.timestamp = timestamp()

MERGE (person_5260b4274ed4:Person{ uuid: '8e8c7417-c905-46b1-b42a-5260b4274ed4' })
SET person_5260b4274ed4.name = 'Thelonious Monk'
SET person_5260b4274ed4.gender = 'Male'
SET person_5260b4274ed4.country = 'US'
SET person_5260b4274ed4.wikipedia = 'http://en.wikipedia.org/wiki/Thelonious_Monk'
SET person_5260b4274ed4.viaf = 'http://viaf.org/viaf/44485892'
SET person_5260b4274ed4.allmusic = 'http://www.allmusic.com/artist/mn0000490416'
SET person_5260b4274ed4.bbc = 'http://www.bbc.co.uk/music/artists/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.discogs = 'http://www.discogs.com/artist/145256'
SET person_5260b4274ed4.imdb = 'http://www.imdb.com/name/nm0598243/'
SET person_5260b4274ed4.wikidata = 'http://www.wikidata.org/wiki/Q109612'
SET person_5260b4274ed4.discographies = ['http://www.howardm.net/tsmonk/tsmonk.php', 'http://www.jazzdisco.org/monk/']
SET person_5260b4274ed4.databases = ['http://rateyourmusic.com/artist/thelonious_monk']
SET person_5260b4274ed4.musicbrainz = 'https://musicbrainz.org/artist/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.isni_list = ['http://isni.org/isni/0000000120249127']
SET person_5260b4274ed4.source = 'musicbrainz.org'
SET person_5260b4274ed4.timestamp = timestamp()

MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_ecaeddf44a98)

// performances

MERGE (perf_bb946f2aa19b:Performance{ uuid: '0cda8844-34e3-4d58-b380-bb946f2aa19b' })
SET perf_bb946f2aa19b.name = 'Autumn Leaves'
SET perf_bb946f2aa19b.duration = '2:20'
SET perf_bb946f2aa19b.source = 'youtube.com'
SET perf_bb946f2aa19b.source = 'https://www.youtube.com/watch?v=8OJyVXXWwDc'
SET perf_bb946f2aa19b.youtube = timestamp()

MERGE (perf_9f0367c15b86:Performance{ uuid: '374ad1f6-87d0-4060-9964-9f0367c15b86' })
SET perf_9f0367c15b86.name = 'Rhythm-a-Ning'
SET perf_9f0367c15b86.duration = '6:35'
SET perf_9f0367c15b86.source = 'youtube.com'
SET perf_9f0367c15b86.youtube = 'https://www.youtube.com/watch?v=8OJyVXXWwDc'
SET perf_9f0367c15b86.timestamp = timestamp()

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_bb946f2aa19b)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bb946f2aa19b)
MERGE (person_be027b7bb16e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_bb946f2aa19b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_9f0367c15b86)
MERGE (person_5a269b32b4c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_9f0367c15b86)
MERGE (person_be027b7bb16e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_9f0367c15b86)

// performances of
MERGE (perf_bb946f2aa19b)-[:PERFORMANCE_OF]->(work_268199324401)
MERGE (perf_9f0367c15b86)-[:PERFORMANCE_OF]->(work_ecaeddf44a98)

// place nodes
MERGE (place_13c91aabaa00:Place{ uuid: '5df4ac64-d016-4ecf-96b6-13c91aabaa00' })
SET place_13c91aabaa00.name = 'White House'
SET place_13c91aabaa00.address = 'White House, 1600, Pennsylvania Avenue Northwest, Monumental Core, Logan Circle, Washington, District of Columbia, 20500, United States of America'
SET place_13c91aabaa00.lat = '38.8976989'
SET place_13c91aabaa00.lng = '-77.036553192281'
SET place_13c91aabaa00.source = 'musicbrainz.org'

// place relationships
MERGE (perf_bb946f2aa19b)-[:HAS_PLACE { type: 'recorded at', begin: '1982-12-04', end: '1982-12-04' }]->(place_13c91aabaa00)
MERGE (perf_9f0367c15b86)-[:HAS_PLACE { type: 'recorded at', begin: '1982-12-04', end: '1982-12-04' }]->(place_13c91aabaa00)

