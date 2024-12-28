
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_123e1b9b64b4:Release{ uuid: 'aeb100a0-8294-4045-b23b-123e1b9b64b4' })
SET release_123e1b9b64b4.name = 'All the Things We Are'
SET release_123e1b9b64b4.country = 'US'
SET release_123e1b9b64b4.date = '1976'
SET release_123e1b9b64b4.format = 'Vinyl'
SET release_123e1b9b64b4.discode = '1684-2'
SET release_123e1b9b64b4.musicbrainz = 'http://musicbrainz.org/release/aeb100a0-8294-4045-b23b-123e1b9b64b4'
SET release_123e1b9b64b4.source = 'musicbrainz.org'


MERGE (person_602b776f5306:Person{ uuid: '4e5f99db-d181-4317-9124-602b776f5306' })
SET person_602b776f5306.name = 'Anthony Braxton'
SET person_602b776f5306.gender = 'Male'
SET person_602b776f5306.country = 'US'
SET person_602b776f5306.viaf = 'http://viaf.org/viaf/64191124'
SET person_602b776f5306.allmusic = 'http://www.allmusic.com/artist/mn0000924030'
SET person_602b776f5306.bbc = 'http://www.bbc.co.uk/music/artists/4e5f99db-d181-4317-9124-602b776f5306'
SET person_602b776f5306.wikipedia = 'https://en.wikipedia.org/wiki/Anthony_Braxton'
SET person_602b776f5306.discogs = 'https://www.discogs.com/artist/200818'
SET person_602b776f5306.wikidata = 'https://www.wikidata.org/wiki/Q572924'
SET person_602b776f5306.discographies = ['http://www.restructures.net/BraxDisco/BraxDisco.htm']
SET person_602b776f5306.databases = ['https://rateyourmusic.com/artist/anthony_braxton']
SET person_602b776f5306.musicbrainz = 'https://musicbrainz.org/artist/4e5f99db-d181-4317-9124-602b776f5306'
SET person_602b776f5306.source = 'musicbrainz.org'


MERGE (person_7753fb0739aa:Person{ uuid: '9136db51-46ba-4208-afd6-7753fb0739aa' })
SET person_7753fb0739aa.name = 'Lee Konitz'
SET person_7753fb0739aa.gender = 'Male'
SET person_7753fb0739aa.country = 'US'
SET person_7753fb0739aa.viaf = 'http://viaf.org/viaf/71373696'
SET person_7753fb0739aa.allmusic = 'http://www.allmusic.com/artist/mn0000227776'
SET person_7753fb0739aa.bbc = 'http://www.bbc.co.uk/music/artists/9136db51-46ba-4208-afd6-7753fb0739aa'
SET person_7753fb0739aa.imdb = 'http://www.imdb.com/name/nm0465170/'
SET person_7753fb0739aa.wikipedia = 'https://en.wikipedia.org/wiki/Lee_Konitz'
SET person_7753fb0739aa.discogs = 'https://www.discogs.com/artist/259092'
SET person_7753fb0739aa.wikidata = 'https://www.wikidata.org/wiki/Q453393'
SET person_7753fb0739aa.databases = ['https://d-nb.info/gnd/12060003X', 'https://rateyourmusic.com/artist/lee_konitz']
SET person_7753fb0739aa.musicbrainz = 'https://musicbrainz.org/artist/9136db51-46ba-4208-afd6-7753fb0739aa'
SET person_7753fb0739aa.isni_list = ['http://isni.org/isni/0000000114745669']
SET person_7753fb0739aa.source = 'musicbrainz.org'


MERGE (person_8be01f64b4ea:Person{ uuid: '9d7283cd-a00c-469d-99f6-8be01f64b4ea' })
SET person_8be01f64b4ea.name = 'Jack Six'
SET person_8be01f64b4ea.gender = 'Male'
SET person_8be01f64b4ea.country = 'US'
SET person_8be01f64b4ea.allmusic = 'http://www.allmusic.com/artist/mn0000688926'
SET person_8be01f64b4ea.discogs = 'https://www.discogs.com/artist/251690'
SET person_8be01f64b4ea.wikidata = 'https://www.wikidata.org/wiki/Q19624438'
SET person_8be01f64b4ea.musicbrainz = 'https://musicbrainz.org/artist/9d7283cd-a00c-469d-99f6-8be01f64b4ea'
SET person_8be01f64b4ea.source = 'musicbrainz.org'


MERGE (person_3f66d505061b:Person{ uuid: 'de0222a6-e1c4-403d-8b01-3f66d505061b' })
SET person_3f66d505061b.name = 'Dave Brubeck'
SET person_3f66d505061b.gender = 'Male'
SET person_3f66d505061b.country = 'US'
SET person_3f66d505061b.viaf = 'http://viaf.org/viaf/14957683'
SET person_3f66d505061b.allmusic = 'http://www.allmusic.com/artist/mn0000958533'
SET person_3f66d505061b.bbc = 'http://www.bbc.co.uk/music/artists/de0222a6-e1c4-403d-8b01-3f66d505061b'
SET person_3f66d505061b.imdb = 'http://www.imdb.com/name/nm0115399/'
SET person_3f66d505061b.wikipedia = 'https://en.wikipedia.org/wiki/Dave_Brubeck'
SET person_3f66d505061b.discogs = 'https://www.discogs.com/artist/37737'
SET person_3f66d505061b.wikidata = 'https://www.wikidata.org/wiki/Q108597'
SET person_3f66d505061b.discographies = ['http://www.jazzdisco.org/dave-brubeck/catalog/']
SET person_3f66d505061b.databases = ['http://rateyourmusic.com/artist/dave_brubeck', 'http://www.45cat.com/artist/dave-brubeck']
SET person_3f66d505061b.musicbrainz = 'https://musicbrainz.org/artist/de0222a6-e1c4-403d-8b01-3f66d505061b'
SET person_3f66d505061b.isni_list = ['http://isni.org/isni/000000011021617X']
SET person_3f66d505061b.source = 'musicbrainz.org'


MERGE (person_b1735bffe235:Person{ uuid: '337ead4d-6988-4e31-a11e-b1735bffe235' })
SET person_b1735bffe235.name = 'Alan Dawson'
SET person_b1735bffe235.gender = 'Male'
SET person_b1735bffe235.country = 'US'
SET person_b1735bffe235.viaf = 'http://viaf.org/viaf/54332181'
SET person_b1735bffe235.allmusic = 'http://www.allmusic.com/artist/mn0000628636'
SET person_b1735bffe235.wikipedia = 'https://en.wikipedia.org/wiki/Alan_Dawson'
SET person_b1735bffe235.discogs = 'https://www.discogs.com/artist/251688'
SET person_b1735bffe235.wikidata = 'https://www.wikidata.org/wiki/Q716878'
SET person_b1735bffe235.musicbrainz = 'https://musicbrainz.org/artist/337ead4d-6988-4e31-a11e-b1735bffe235'
SET person_b1735bffe235.source = 'musicbrainz.org'


MERGE (person_d085d92bc7d8:Person{ uuid: 'e9e9e70d-0fa4-44d6-a029-d085d92bc7d8' })
SET person_d085d92bc7d8.name = 'Michael Cuscuna'
SET person_d085d92bc7d8.country = 'US'
SET person_d085d92bc7d8.viaf = 'http://viaf.org/viaf/32110948'
SET person_d085d92bc7d8.wikipedia = 'https://en.wikipedia.org/wiki/Michael_Cuscuna'
SET person_d085d92bc7d8.discogs = 'https://www.discogs.com/artist/252960'
SET person_d085d92bc7d8.wikidata = 'https://www.wikidata.org/wiki/Q786553'
SET person_d085d92bc7d8.musicbrainz = 'https://musicbrainz.org/artist/e9e9e70d-0fa4-44d6-a029-d085d92bc7d8'
SET person_d085d92bc7d8.source = 'musicbrainz.org'


MERGE (person_6f0a331cc1ca:Person{ uuid: '2c090b57-5e9d-49c5-9b71-6f0a331cc1ca' })
SET person_6f0a331cc1ca.name = 'Roy Haynes'
SET person_6f0a331cc1ca.gender = 'Male'
SET person_6f0a331cc1ca.country = 'US'
SET person_6f0a331cc1ca.viaf = 'http://viaf.org/viaf/84975999'
SET person_6f0a331cc1ca.allmusic = 'http://www.allmusic.com/artist/mn0000290464'
SET person_6f0a331cc1ca.bbc = 'http://www.bbc.co.uk/music/artists/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.imdb = 'http://www.imdb.com/name/nm0371542/'
SET person_6f0a331cc1ca.wikipedia = 'https://en.wikipedia.org/wiki/Roy_Haynes'
SET person_6f0a331cc1ca.discogs = 'https://www.discogs.com/artist/255556'
SET person_6f0a331cc1ca.wikidata = 'https://www.wikidata.org/wiki/Q448235'
SET person_6f0a331cc1ca.musicbrainz = 'https://musicbrainz.org/artist/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.isni_list = ['http://isni.org/isni/0000000078266176']
SET person_6f0a331cc1ca.source = 'musicbrainz.org'

// labels

MERGE (label_8181173339c7:Label{ uuid: '50c384a2-0b44-401b-b893-8181173339c7' })
SET label_8181173339c7.name= 'Atlantic'

// performances

MERGE (perf_95d02e60adc1:Performance{ uuid: 'e8809d9e-bf69-40d4-ab78-95d02e60adc1' })
SET perf_95d02e60adc1.name = 'Like Someone in Love'
SET perf_95d02e60adc1.duration = '6:22'
SET perf_95d02e60adc1.source = 'musicbrainz.org'


MERGE (perf_2bf61e9ec6ca:Performance{ uuid: '220c78aa-8a0f-4edd-8302-2bf61e9ec6ca' })
SET perf_2bf61e9ec6ca.name = 'In Your Own Sweet Way'
SET perf_2bf61e9ec6ca.duration = '7:40'
SET perf_2bf61e9ec6ca.source = 'musicbrainz.org'


MERGE (perf_23be1068017f:Performance{ uuid: '7054bab4-1d2c-48e9-9d27-23be1068017f' })
SET perf_23be1068017f.name = 'All the Things You Are'
SET perf_23be1068017f.duration = '7:28'
SET perf_23be1068017f.source = 'musicbrainz.org'


MERGE (perf_adb89b45d9f7:Performance{ uuid: '1cbb5df1-ef81-48bd-9287-adb89b45d9f7' })
SET perf_adb89b45d9f7.name = 'Jimmy van Heusen Medley: Deep in a Dream / Like Someone in Love / Here\\'s That Rainy Day / Polka Dots and Moonbeams / It Could Happen to You'
SET perf_adb89b45d9f7.duration = '20:49'
SET perf_adb89b45d9f7.source = 'musicbrainz.org'


MERGE (perf_e38c81078d0c:Performance{ uuid: '462ded8a-3c28-4837-ab46-e38c81078d0c' })
SET perf_e38c81078d0c.name = 'Don\\'t Get Around Much Anymore'
SET perf_e38c81078d0c.duration = '2:47'
SET perf_e38c81078d0c.source = 'musicbrainz.org'




// labels
MERGE (release_123e1b9b64b4)-[:HAS_LABEL]->(label_8181173339c7)


// tracks
MERGE (release_123e1b9b64b4)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_95d02e60adc1)
MERGE (release_123e1b9b64b4)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_2bf61e9ec6ca)
MERGE (release_123e1b9b64b4)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_23be1068017f)
MERGE (release_123e1b9b64b4)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_adb89b45d9f7)
MERGE (release_123e1b9b64b4)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_e38c81078d0c)

// works

MERGE (person_7eeeb45e411f:Person{ uuid: '3af06bc4-68ad-4cae-bb7a-7eeeb45e411f' })
SET person_7eeeb45e411f.name = 'Duke Ellington'
SET person_7eeeb45e411f.gender = 'Male'
SET person_7eeeb45e411f.disambiguation = 'American composer, pianist, & jazz bandleader'
SET person_7eeeb45e411f.country = 'US'
SET person_7eeeb45e411f.viaf = 'http://viaf.org/viaf/66651610'
SET person_7eeeb45e411f.allmusic = 'http://www.allmusic.com/artist/mn0000120323'
SET person_7eeeb45e411f.bbc = 'http://www.bbc.co.uk/music/artists/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.imdb = 'http://www.imdb.com/name/nm0254153/'
SET person_7eeeb45e411f.wikipedia = 'https://en.wikipedia.org/wiki/Duke_Ellington'
SET person_7eeeb45e411f.discogs = 'https://www.discogs.com/artist/145257'
SET person_7eeeb45e411f.wikidata = 'https://www.wikidata.org/wiki/Q4030'
SET person_7eeeb45e411f.discographies = ['http://www.redhotjazz.com/duke.html']
SET person_7eeeb45e411f.databases = ['http://d-nb.info/gnd/118529994', 'http://ibdb.com/person.php?id=11631', 'http://rateyourmusic.com/artist/duke_ellington', 'https://www.worldcat.org/identities/lccn-n50080187/']
SET person_7eeeb45e411f.musicbrainz = 'https://musicbrainz.org/artist/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.isni_list = ['http://isni.org/isni/0000000109110810']
SET person_7eeeb45e411f.source = 'musicbrainz.org'


MERGE (person_f324ef1bf494:Person{ uuid: '8fb64b2e-db8b-4579-ad08-f324ef1bf494' })
SET person_f324ef1bf494.name = 'Jerome Kern'
SET person_f324ef1bf494.gender = 'Male'
SET person_f324ef1bf494.country = 'US'
SET person_f324ef1bf494.viaf = 'http://viaf.org/viaf/196726'
SET person_f324ef1bf494.imdb = 'http://www.imdb.com/name/nm0006153/'
SET person_f324ef1bf494.wikipedia = 'https://en.wikipedia.org/wiki/Jerome_Kern'
SET person_f324ef1bf494.discogs = 'https://www.discogs.com/artist/166685'
SET person_f324ef1bf494.wikidata = 'https://www.wikidata.org/wiki/Q313270'
SET person_f324ef1bf494.databases = ['http://d-nb.info/gnd/118777084', 'http://ibdb.com/person.php?id=6711', 'http://www.lortel.org/Archives/CreditableEntity/11862', 'https://nla.gov.au/anbd.aut-an36379903', 'https://www.worldcat.org/identities/lccn-n80-149466']
SET person_f324ef1bf494.musicbrainz = 'https://musicbrainz.org/artist/8fb64b2e-db8b-4579-ad08-f324ef1bf494'
SET person_f324ef1bf494.isni_list = ['http://isni.org/isni/000000010861737X']
SET person_f324ef1bf494.source = 'musicbrainz.org'


MERGE (person_a6d92136636f:Person{ uuid: '8d3f8b43-0d28-4500-900e-a6d92136636f' })
SET person_a6d92136636f.name = 'Jimmy Van Heusen'
SET person_a6d92136636f.gender = 'Male'
SET person_a6d92136636f.country = 'US'
SET person_a6d92136636f.viaf = 'http://viaf.org/viaf/54338466'
SET person_a6d92136636f.allmusic = 'http://www.allmusic.com/artist/mn0000309464'
SET person_a6d92136636f.allmusic = 'http://www.allmusic.com/artist/mn0003168282'
SET person_a6d92136636f.imdb = 'http://www.imdb.com/name/nm0006329/'
SET person_a6d92136636f.wikipedia = 'https://en.wikipedia.org/wiki/Jimmy_Van_Heusen'
SET person_a6d92136636f.discogs = 'https://www.discogs.com/artist/255313'
SET person_a6d92136636f.wikidata = 'https://www.wikidata.org/wiki/Q33124'
SET person_a6d92136636f.databases = ['http://ibdb.com/person.php?id=12521', 'https://rateyourmusic.com/artist/jimmy_van_heusen']
SET person_a6d92136636f.musicbrainz = 'https://musicbrainz.org/artist/8d3f8b43-0d28-4500-900e-a6d92136636f'
SET person_a6d92136636f.isni_list = ['http://isni.org/isni/0000000081333253']
SET person_a6d92136636f.source = 'musicbrainz.org'


MERGE (work_ad4a192fd542:Work{ uuid: '5894be54-19fa-3668-bb08-ad4a192fd542' })
SET work_ad4a192fd542.name = 'Like Someone in Love'
SET work_ad4a192fd542.iswc = 'T-070.095.943-8'
SET work_ad4a192fd542.type = 'Song'
SET work_ad4a192fd542.wikidata = 'https://www.wikidata.org/wiki/Q6547136'
SET work_ad4a192fd542.musicbrainz = 'https://musicbrainz.org/work/5894be54-19fa-3668-bb08-ad4a192fd542'
SET work_ad4a192fd542.source = 'musicbrainz.org'


MERGE (work_caa47b30366c:Work{ uuid: '6d489d45-3e3b-3bd9-a178-caa47b30366c' })
SET work_caa47b30366c.name = 'It Could Happen to You'
SET work_caa47b30366c.iswc = 'T-070.907.037-0'
SET work_caa47b30366c.type = 'Song'
SET work_caa47b30366c.wikidata = 'https://www.wikidata.org/wiki/Q820861'
SET work_caa47b30366c.musicbrainz = 'https://musicbrainz.org/work/6d489d45-3e3b-3bd9-a178-caa47b30366c'
SET work_caa47b30366c.source = 'musicbrainz.org'


MERGE (work_fef963759bfa:Work{ uuid: 'f32a8ad2-1196-3e41-85dd-fef963759bfa' })
SET work_fef963759bfa.name = 'Polka Dots and Moonbeams'
SET work_fef963759bfa.source = 'musicbrainz.org'


MERGE (work_dde2db33efca:Work{ uuid: 'ad3199e2-5395-3254-842f-dde2db33efca' })
SET work_dde2db33efca.name = 'Here\\'s That Rainy Day'
SET work_dde2db33efca.type = 'Song'
SET work_dde2db33efca.wikidata = 'https://www.wikidata.org/wiki/Q15132711'
SET work_dde2db33efca.musicbrainz = 'https://musicbrainz.org/work/ad3199e2-5395-3254-842f-dde2db33efca'
SET work_dde2db33efca.source = 'musicbrainz.org'


MERGE (work_870a5caa1fe1:Work{ uuid: '57d2f184-b33c-3ad1-92a1-870a5caa1fe1' })
SET work_870a5caa1fe1.name = 'Don’t Get Around Much Anymore'
SET work_870a5caa1fe1.iswc = 'T-070.039.705-2'
SET work_870a5caa1fe1.type = 'Song'
SET work_870a5caa1fe1.wikipedia = 'https://en.wikipedia.org/wiki/Don%27t_Get_Around_Much_Anymore'
SET work_870a5caa1fe1.musicbrainz = 'https://musicbrainz.org/work/57d2f184-b33c-3ad1-92a1-870a5caa1fe1'
SET work_870a5caa1fe1.source = 'musicbrainz.org'


MERGE (work_dd12dcb5ff89:Work{ uuid: '7d0e572e-2238-3a44-8191-dd12dcb5ff89' })
SET work_dd12dcb5ff89.name = 'In Your Own Sweet Way'
SET work_dd12dcb5ff89.type = 'Song'
SET work_dd12dcb5ff89.source = 'musicbrainz.org'


MERGE (work_8617e9e5ec3c:Work{ uuid: 'd684b0d5-476b-31bd-97cf-8617e9e5ec3c' })
SET work_8617e9e5ec3c.name = 'Deep in a Dream'
SET work_8617e9e5ec3c.source = 'musicbrainz.org'


MERGE (work_f04324e0f525:Work{ uuid: '6c0ae4fc-2893-363a-a3e9-f04324e0f525' })
SET work_f04324e0f525.name = 'All the Things You Are'
SET work_f04324e0f525.iswc = 'T-070.000.803-2'
SET work_f04324e0f525.type = 'Song'
SET work_f04324e0f525.wikidata = 'https://www.wikidata.org/wiki/Q1410072'
SET work_f04324e0f525.musicbrainz = 'https://musicbrainz.org/work/6c0ae4fc-2893-363a-a3e9-f04324e0f525'
SET work_f04324e0f525.source = 'musicbrainz.org'



// performances of
MERGE (perf_adb89b45d9f7)-[:PERFORMANCE_OF]->(work_ad4a192fd542)
MERGE (perf_95d02e60adc1)-[:PERFORMANCE_OF]->(work_ad4a192fd542)
MERGE (perf_adb89b45d9f7)-[:PERFORMANCE_OF]->(work_caa47b30366c)
MERGE (perf_adb89b45d9f7)-[:PERFORMANCE_OF]->(work_fef963759bfa)
MERGE (perf_adb89b45d9f7)-[:PERFORMANCE_OF]->(work_dde2db33efca)
MERGE (perf_e38c81078d0c)-[:PERFORMANCE_OF]->(work_870a5caa1fe1)
MERGE (perf_2bf61e9ec6ca)-[:PERFORMANCE_OF]->(work_dd12dcb5ff89)
MERGE (perf_adb89b45d9f7)-[:PERFORMANCE_OF]->(work_8617e9e5ec3c)
MERGE (perf_23be1068017f)-[:PERFORMANCE_OF]->(work_f04324e0f525)


// composers
MERGE (person_a6d92136636f)-[:COMPOSED]->(work_ad4a192fd542)
MERGE (person_a6d92136636f)-[:COMPOSED]->(work_caa47b30366c)
MERGE (person_a6d92136636f)-[:COMPOSED]->(work_fef963759bfa)
MERGE (person_a6d92136636f)-[:COMPOSED]->(work_dde2db33efca)
MERGE (person_7eeeb45e411f)-[:COMPOSED]->(work_870a5caa1fe1)
MERGE (person_3f66d505061b)-[:COMPOSED]->(work_dd12dcb5ff89)
MERGE (person_a6d92136636f)-[:COMPOSED]->(work_8617e9e5ec3c)
MERGE (person_f324ef1bf494)-[:COMPOSED]->(work_f04324e0f525)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_95d02e60adc1)
MERGE (person_7753fb0739aa)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_95d02e60adc1)
MERGE (person_8be01f64b4ea)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_95d02e60adc1)
MERGE (person_3f66d505061b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_95d02e60adc1)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_95d02e60adc1)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_2bf61e9ec6ca)
MERGE (person_602b776f5306)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_2bf61e9ec6ca)
MERGE (person_8be01f64b4ea)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_2bf61e9ec6ca)
MERGE (person_3f66d505061b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2bf61e9ec6ca)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_2bf61e9ec6ca)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_23be1068017f)
MERGE (person_602b776f5306)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_23be1068017f)
MERGE (person_7753fb0739aa)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_23be1068017f)
MERGE (person_8be01f64b4ea)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_23be1068017f)
MERGE (person_3f66d505061b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_23be1068017f)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_23be1068017f)
MERGE (person_b1735bffe235)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_adb89b45d9f7)
MERGE (person_8be01f64b4ea)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_adb89b45d9f7)
MERGE (person_3f66d505061b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_adb89b45d9f7)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_adb89b45d9f7)
MERGE (person_7753fb0739aa)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_e38c81078d0c)
MERGE (person_3f66d505061b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e38c81078d0c)
MERGE (person_d085d92bc7d8)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e38c81078d0c)


"""
)