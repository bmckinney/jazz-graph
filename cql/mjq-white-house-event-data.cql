// events

MERGE (event_54c6e531f30e:Event{ uuid: '89a92f2f-8aad-4abb-9e54-54c6e531f30e' })
SET event_54c6e531f30e.name = 'Modern Jazz Quartet at the White House'
SET event_54c6e531f30e.date = '1969-10-21'
SET event_54c6e531f30e.type = 'Concert'
SET event_54c6e531f30e.musicbrainz = 'http://musicbrainz.org/release/89a92f2f-8aad-4abb-9e54-54c6e531f30e'
SET event_54c6e531f30e.source = 'musicbrainz.org'
SET event_54c6e531f30e.timestamp = timestamp()

MERGE (person_5b0bb4641cb9:Person{ uuid: '2e38e1de-2890-4620-8467-5b0bb4641cb9' })
SET person_5b0bb4641cb9.name = 'Milt Jackson'
SET person_5b0bb4641cb9.gender = 'Male'
SET person_5b0bb4641cb9.country = 'US'
SET person_5b0bb4641cb9.wikipedia = 'http://en.wikipedia.org/wiki/Milt_Jackson'
SET person_5b0bb4641cb9.viaf = 'http://viaf.org/viaf/39562146'
SET person_5b0bb4641cb9.allmusic = 'http://www.allmusic.com/artist/mn0000489845'
SET person_5b0bb4641cb9.discogs = 'http://www.discogs.com/artist/149254'
SET person_5b0bb4641cb9.wikidata = 'http://www.wikidata.org/wiki/Q435665'
SET person_5b0bb4641cb9.databases = ['http://rateyourmusic.com/artist/milt_jackson']
SET person_5b0bb4641cb9.musicbrainz = 'https://musicbrainz.org/artist/2e38e1de-2890-4620-8467-5b0bb4641cb9'
SET person_5b0bb4641cb9.isni_list = ['http://isni.org/isni/0000000083744603']
SET person_5b0bb4641cb9.source = 'musicbrainz.org'
SET person_5b0bb4641cb9.timestamp = timestamp()

MERGE (person_b847dbf75b6f:Person{ uuid: '534362cd-66ed-45a8-9cba-b847dbf75b6f' })
SET person_b847dbf75b6f.name = 'Percy Heath'
SET person_b847dbf75b6f.gender = 'Male'
SET person_b847dbf75b6f.country = 'US'
SET person_b847dbf75b6f.wikipedia = 'http://en.wikipedia.org/wiki/Percy_Heath'
SET person_b847dbf75b6f.viaf = 'http://viaf.org/viaf/71578162'
SET person_b847dbf75b6f.allmusic = 'http://www.allmusic.com/artist/mn0000256575'
SET person_b847dbf75b6f.discogs = 'http://www.discogs.com/artist/253445'
SET person_b847dbf75b6f.wikidata = 'http://www.wikidata.org/wiki/Q981283'
SET person_b847dbf75b6f.musicbrainz = 'https://musicbrainz.org/artist/534362cd-66ed-45a8-9cba-b847dbf75b6f'
SET person_b847dbf75b6f.source = 'musicbrainz.org'
SET person_b847dbf75b6f.timestamp = timestamp()

MERGE (person_669d71b68bc5:Person{ uuid: 'be347fef-e406-4c1b-8698-669d71b68bc5' })
SET person_669d71b68bc5.name = 'John Lewis'
SET person_669d71b68bc5.gender = 'Male'
SET person_669d71b68bc5.disambiguation = 'pianist, member of Modern Jazz Quartet'
SET person_669d71b68bc5.country = 'US'
SET person_669d71b68bc5.wikipedia = 'http://en.wikipedia.org/wiki/John_Lewis_(pianist)'
SET person_669d71b68bc5.viaf = 'http://viaf.org/viaf/94096772'
SET person_669d71b68bc5.allmusic = 'http://www.allmusic.com/artist/mn0000424292'
SET person_669d71b68bc5.discogs = 'http://www.discogs.com/artist/267675'
SET person_669d71b68bc5.imdb = 'http://www.imdb.com/name/nm0507368/'
SET person_669d71b68bc5.wikidata = 'http://www.wikidata.org/wiki/Q353943'
SET person_669d71b68bc5.databases = ['https://rateyourmusic.com/artist/john_lewis']
SET person_669d71b68bc5.musicbrainz = 'https://musicbrainz.org/artist/be347fef-e406-4c1b-8698-669d71b68bc5'
SET person_669d71b68bc5.isni_list = ['http://isni.org/isni/0000000106555937']
SET person_669d71b68bc5.source = 'musicbrainz.org'
SET person_669d71b68bc5.timestamp = timestamp()

MERGE (person_5ac8601350ba:Person{ uuid: '75472b2f-55ca-47bb-a192-5ac8601350ba' })
SET person_5ac8601350ba.name = 'The Modern Jazz Quartet'
SET person_5ac8601350ba.country = 'US'
SET person_5ac8601350ba.wikipedia = 'http://en.wikipedia.org/wiki/Modern_Jazz_Quartet'
SET person_5ac8601350ba.allmusic = 'http://www.allmusic.com/artist/mn0000567325'
SET person_5ac8601350ba.discogs = 'http://www.discogs.com/artist/254990'
SET person_5ac8601350ba.wikidata = 'http://www.wikidata.org/wiki/Q830379'
SET person_5ac8601350ba.databases = ['https://rateyourmusic.com/artist/the_modern_jazz_quartet']
SET person_5ac8601350ba.musicbrainz = 'https://musicbrainz.org/artist/75472b2f-55ca-47bb-a192-5ac8601350ba'
SET person_5ac8601350ba.isni_list = ['http://isni.org/isni/000000011956623X']
SET person_5ac8601350ba.source = 'musicbrainz.org'
SET person_5ac8601350ba.timestamp = timestamp()

MERGE (person_a38456b1b48e:Person{ uuid: '4f1dc71a-d679-4d5d-b590-a38456b1b48e' })
SET person_a38456b1b48e.name = 'Connie Kay'
SET person_a38456b1b48e.gender = 'Male'
SET person_a38456b1b48e.country = 'US'
SET person_a38456b1b48e.wikipedia = 'http://en.wikipedia.org/wiki/Connie_Kay'
SET person_a38456b1b48e.viaf = 'http://viaf.org/viaf/76500549'
SET person_a38456b1b48e.allmusic = 'http://www.allmusic.com/artist/mn0000116605'
SET person_a38456b1b48e.discogs = 'http://www.discogs.com/artist/251782'
SET person_a38456b1b48e.wikidata = 'http://www.wikidata.org/wiki/Q431520'
SET person_a38456b1b48e.musicbrainz = 'https://musicbrainz.org/artist/4f1dc71a-d679-4d5d-b590-a38456b1b48e'
SET person_a38456b1b48e.source = 'musicbrainz.org'
SET person_a38456b1b48e.timestamp = timestamp()

// works

MERGE (person_221e418c8959:Person{ uuid: 'fde4460b-868a-493e-8c53-221e418c8959' })
SET person_221e418c8959.name = 'Joaquín Rodrigo'
SET person_221e418c8959.gender = 'Male'
SET person_221e418c8959.disambiguation = 'Spanish composer and virtuoso pianist'
SET person_221e418c8959.country = 'ES'
SET person_221e418c8959.wikipedia = 'http://en.wikipedia.org/wiki/Joaqu%C3%ADn_Rodrigo'
SET person_221e418c8959.viaf = 'http://viaf.org/viaf/59270736'
SET person_221e418c8959.allmusic = 'http://www.allmusic.com/artist/mn0000254674'
SET person_221e418c8959.allmusic = 'http://www.allmusic.com/artist/mn0002503034'
SET person_221e418c8959.discogs = 'http://www.discogs.com/artist/523642'
SET person_221e418c8959.imdb = 'http://www.imdb.com/name/nm0735006/'
SET person_221e418c8959.wikidata = 'http://www.wikidata.org/wiki/Q151084'
SET person_221e418c8959.databases = ['http://www.classicalarchives.com/composer/7188.html']
SET person_221e418c8959.musicbrainz = 'https://musicbrainz.org/artist/fde4460b-868a-493e-8c53-221e418c8959'
SET person_221e418c8959.isni_list = ['http://isni.org/isni/0000000109062011']
SET person_221e418c8959.source = 'musicbrainz.org'
SET person_221e418c8959.timestamp = timestamp()

MERGE (work_01c8b424d9a8:Work{ uuid: 'c31fc7a6-b08e-4a82-8f46-01c8b424d9a8' })
SET work_01c8b424d9a8.name = 'The Blue Necklace'
SET work_01c8b424d9a8.iswc = 'T-700.002.947-2'
SET work_01c8b424d9a8.type = 'Song'
SET work_01c8b424d9a8.source = 'musicbrainz.org'
SET work_01c8b424d9a8.timestamp = timestamp()

MERGE (work_4c065caef2be:Work{ uuid: '56b80e1e-e775-4ea3-91d0-4c065caef2be' })
SET work_4c065caef2be.name = 'Visitor from Venus'
SET work_4c065caef2be.iswc = 'T-700.076.533-5'
SET work_4c065caef2be.type = 'Song'
SET work_4c065caef2be.source = 'musicbrainz.org'
SET work_4c065caef2be.timestamp = timestamp()

MERGE (work_fcbfb1ba114f:Work{ uuid: '31979722-7314-455e-b2ad-fcbfb1ba114f' })
SET work_fcbfb1ba114f.name = 'Visitor from Mars'
SET work_fcbfb1ba114f.iswc = 'T-700.076.532-4'
SET work_fcbfb1ba114f.type = 'Song'
SET work_fcbfb1ba114f.source = 'musicbrainz.org'
SET work_fcbfb1ba114f.timestamp = timestamp()

MERGE (work_7d5036a3f70a:Work{ uuid: 'df754996-c4f2-36a5-8323-7d5036a3f70a' })
SET work_7d5036a3f70a.name = 'Concierto de Aranjuez: II. Adagio'
SET work_7d5036a3f70a.source = 'musicbrainz.org'
SET work_7d5036a3f70a.timestamp = timestamp()

MERGE (work_e130f06c5ade:Work{ uuid: '0cdbdfdf-6160-46e7-b467-e130f06c5ade' })
SET work_e130f06c5ade.name = 'The Jasmin Tree'
SET work_e130f06c5ade.type = 'Song'
SET work_e130f06c5ade.source = 'musicbrainz.org'
SET work_e130f06c5ade.timestamp = timestamp()


// performances
MERGE (perf_54c6e531f30e_01c8b424d9a8:Performance { uuid: '54c6e531f30e-c31fc7a6-b08e-4a82-8f46-01c8b424d9a8' })
SET perf_54c6e531f30e_01c8b424d9a8.name = 'The Blue Necklace'
SET perf_54c6e531f30e_01c8b424d9a8.begin = '1969-10-21'
SET perf_54c6e531f30e_01c8b424d9a8.end = '1969-10-21'
SET perf_54c6e531f30e_01c8b424d9a8.source = 'musicbrainz.org'
SET perf_54c6e531f30e_01c8b424d9a8.timestamp = timestamp()
MERGE (perf_54c6e531f30e_01c8b424d9a8)-[:PERFORMANCE_OF]->(work_01c8b424d9a8)

MERGE (perf_54c6e531f30e_4c065caef2be:Performance { uuid: '54c6e531f30e-56b80e1e-e775-4ea3-91d0-4c065caef2be' })
SET perf_54c6e531f30e_4c065caef2be.name = 'Visitor from Venus'
SET perf_54c6e531f30e_4c065caef2be.begin = '1969-10-21'
SET perf_54c6e531f30e_4c065caef2be.end = '1969-10-21'
SET perf_54c6e531f30e_4c065caef2be.source = 'musicbrainz.org'
SET perf_54c6e531f30e_4c065caef2be.timestamp = timestamp()
MERGE (perf_54c6e531f30e_4c065caef2be)-[:PERFORMANCE_OF]->(work_4c065caef2be)

MERGE (perf_54c6e531f30e_fcbfb1ba114f:Performance { uuid: '54c6e531f30e-31979722-7314-455e-b2ad-fcbfb1ba114f' })
SET perf_54c6e531f30e_fcbfb1ba114f.name = 'Visitor from Mars'
SET perf_54c6e531f30e_fcbfb1ba114f.begin = '1969-10-21'
SET perf_54c6e531f30e_fcbfb1ba114f.end = '1969-10-21'
SET perf_54c6e531f30e_fcbfb1ba114f.source = 'musicbrainz.org'
SET perf_54c6e531f30e_fcbfb1ba114f.timestamp = timestamp()
MERGE (perf_54c6e531f30e_fcbfb1ba114f)-[:PERFORMANCE_OF]->(work_fcbfb1ba114f)

MERGE (perf_54c6e531f30e_7d5036a3f70a:Performance { uuid: '54c6e531f30e-df754996-c4f2-36a5-8323-7d5036a3f70a' })
SET perf_54c6e531f30e_7d5036a3f70a.name = 'Concierto de Aranjuez: II. Adagio'
SET perf_54c6e531f30e_7d5036a3f70a.begin = '1969-10-21'
SET perf_54c6e531f30e_7d5036a3f70a.end = '1969-10-21'
SET perf_54c6e531f30e_7d5036a3f70a.source = 'musicbrainz.org'
SET perf_54c6e531f30e_7d5036a3f70a.timestamp = timestamp()
MERGE (perf_54c6e531f30e_7d5036a3f70a)-[:PERFORMANCE_OF]->(work_7d5036a3f70a)

MERGE (perf_54c6e531f30e_e130f06c5ade:Performance { uuid: '54c6e531f30e-0cdbdfdf-6160-46e7-b467-e130f06c5ade' })
SET perf_54c6e531f30e_e130f06c5ade.name = 'The Jasmin Tree'
SET perf_54c6e531f30e_e130f06c5ade.begin = '1969-10-21'
SET perf_54c6e531f30e_e130f06c5ade.end = '1969-10-21'
SET perf_54c6e531f30e_e130f06c5ade.source = 'musicbrainz.org'
SET perf_54c6e531f30e_e130f06c5ade.timestamp = timestamp()
MERGE (perf_54c6e531f30e_e130f06c5ade)-[:PERFORMANCE_OF]->(work_e130f06c5ade)



// composers
MERGE (person_669d71b68bc5)-[:COMPOSED]->(work_01c8b424d9a8)
MERGE (person_669d71b68bc5)-[:COMPOSED]->(work_4c065caef2be)
MERGE (person_669d71b68bc5)-[:COMPOSED]->(work_fcbfb1ba114f)
MERGE (person_221e418c8959)-[:COMPOSED]->(work_7d5036a3f70a)
MERGE (person_669d71b68bc5)-[:COMPOSED]->(work_e130f06c5ade)


// place nodes

MERGE (place_13c91aabaa00:Place{ uuid: '5df4ac64-d016-4ecf-96b6-13c91aabaa00' })
SET place_13c91aabaa00.name = 'White House'
SET place_13c91aabaa00.address = 'White House, 1600, Pennsylvania Avenue Northwest, Monumental Core, Logan Circle, Washington, District of Columbia, 20500, United States of America'
SET place_13c91aabaa00.lat = '38.8976989'
SET place_13c91aabaa00.lng = '-77.036553192281'
SET place_13c91aabaa00.source = 'musicbrainz.org'


// place relationships
MERGE (event_54c6e531f30e)-[:HAS_PLACE { type: 'held at' }]->(place_13c91aabaa00)
MERGE (perf_54c6e531f30e_01c8b424d9a8)-[:HAS_PLACE { type: 'performed at', begin: '1969-10-21', end: '1969-10-21' }]->(place_13c91aabaa00)
MERGE (perf_54c6e531f30e_4c065caef2be)-[:HAS_PLACE { type: 'performed at', begin: '1969-10-21', end: '1969-10-21' }]->(place_13c91aabaa00)
MERGE (perf_54c6e531f30e_fcbfb1ba114f)-[:HAS_PLACE { type: 'performed at', begin: '1969-10-21', end: '1969-10-21' }]->(place_13c91aabaa00)
MERGE (perf_54c6e531f30e_7d5036a3f70a)-[:HAS_PLACE { type: 'performed at', begin: '1969-10-21', end: '1969-10-21' }]->(place_13c91aabaa00)
MERGE (perf_54c6e531f30e_e130f06c5ade)-[:HAS_PLACE { type: 'performed at', begin: '1969-10-21', end: '1969-10-21' }]->(place_13c91aabaa00)


// event->performance relationships
MERGE (event_54c6e531f30e)-[:HAS_PERFORMANCE { begin: '1969-10-21', end: '1969-10-21' }]->(perf_54c6e531f30e_01c8b424d9a8)
MERGE (event_54c6e531f30e)-[:HAS_PERFORMANCE { begin: '1969-10-21', end: '1969-10-21' }]->(perf_54c6e531f30e_4c065caef2be)
MERGE (event_54c6e531f30e)-[:HAS_PERFORMANCE { begin: '1969-10-21', end: '1969-10-21' }]->(perf_54c6e531f30e_fcbfb1ba114f)
MERGE (event_54c6e531f30e)-[:HAS_PERFORMANCE { begin: '1969-10-21', end: '1969-10-21' }]->(perf_54c6e531f30e_7d5036a3f70a)
MERGE (event_54c6e531f30e)-[:HAS_PERFORMANCE { begin: '1969-10-21', end: '1969-10-21' }]->(perf_54c6e531f30e_e130f06c5ade)


// event-performance participation
MERGE (person_5b0bb4641cb9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_54c6e531f30e_01c8b424d9a8)
MERGE (person_5b0bb4641cb9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_54c6e531f30e_4c065caef2be)
MERGE (person_5b0bb4641cb9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_54c6e531f30e_fcbfb1ba114f)
MERGE (person_5b0bb4641cb9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_54c6e531f30e_7d5036a3f70a)
MERGE (person_5b0bb4641cb9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_54c6e531f30e_e130f06c5ade)
MERGE (person_a38456b1b48e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_54c6e531f30e_01c8b424d9a8)
MERGE (person_a38456b1b48e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_54c6e531f30e_4c065caef2be)
MERGE (person_a38456b1b48e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_54c6e531f30e_fcbfb1ba114f)
MERGE (person_a38456b1b48e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_54c6e531f30e_7d5036a3f70a)
MERGE (person_a38456b1b48e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_54c6e531f30e_e130f06c5ade)
MERGE (person_b847dbf75b6f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_54c6e531f30e_01c8b424d9a8)
MERGE (person_b847dbf75b6f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_54c6e531f30e_4c065caef2be)
MERGE (person_b847dbf75b6f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_54c6e531f30e_fcbfb1ba114f)
MERGE (person_b847dbf75b6f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_54c6e531f30e_7d5036a3f70a)
MERGE (person_b847dbf75b6f)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_54c6e531f30e_e130f06c5ade)
MERGE (person_5ac8601350ba)-[:PARTICIPATED_IN { roles: ['musician'] }]->(perf_54c6e531f30e_01c8b424d9a8)
MERGE (person_5ac8601350ba)-[:PARTICIPATED_IN { roles: ['musician'] }]->(perf_54c6e531f30e_4c065caef2be)
MERGE (person_5ac8601350ba)-[:PARTICIPATED_IN { roles: ['musician'] }]->(perf_54c6e531f30e_fcbfb1ba114f)
MERGE (person_5ac8601350ba)-[:PARTICIPATED_IN { roles: ['musician'] }]->(perf_54c6e531f30e_7d5036a3f70a)
MERGE (person_5ac8601350ba)-[:PARTICIPATED_IN { roles: ['musician'] }]->(perf_54c6e531f30e_e130f06c5ade)
MERGE (person_669d71b68bc5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_54c6e531f30e_01c8b424d9a8)
MERGE (person_669d71b68bc5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_54c6e531f30e_4c065caef2be)
MERGE (person_669d71b68bc5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_54c6e531f30e_fcbfb1ba114f)
MERGE (person_669d71b68bc5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_54c6e531f30e_7d5036a3f70a)
MERGE (person_669d71b68bc5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_54c6e531f30e_e130f06c5ade)
