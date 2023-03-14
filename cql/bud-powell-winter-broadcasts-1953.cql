// releases

MERGE (release_d56f49d1bd7a:Release{ uuid: '8526ddd2-c51c-4e1e-8187-d56f49d1bd7a' })
SET release_d56f49d1bd7a.name = 'Winter Broadcasts 1953'
SET release_d56f49d1bd7a.date = '1993'
SET release_d56f49d1bd7a.format = 'CD'
SET release_d56f49d1bd7a.musicbrainz = 'http://musicbrainz.org/release/8526ddd2-c51c-4e1e-8187-d56f49d1bd7a'
SET release_d56f49d1bd7a.source = 'musicbrainz.org'
SET release_d56f49d1bd7a.timestamp = timestamp()

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
SET person_340d64fbb41c.timestamp = timestamp()

MERGE (person_1d4909875ca1:Person{ uuid: '28f6d494-d44b-4bd3-aed9-1d4909875ca1' }) 
SET person_1d4909875ca1.name = 'Oscar Pettiford'
SET person_1d4909875ca1.gender = 'Male'
SET person_1d4909875ca1.country = 'US'
SET person_1d4909875ca1.allmusic = 'https://www.allmusic.com/artist/mn0000896298'
SET person_1d4909875ca1.discogs = 'https://www.discogs.com/artist/255767'
SET person_1d4909875ca1.imdb = 'https://www.imdb.com/name/nm0678652/'
SET person_1d4909875ca1.viaf = 'http://viaf.org/viaf/24788159'
SET person_1d4909875ca1.wikidata = 'https://www.wikidata.org/wiki/Q497183'
SET person_1d4909875ca1.wikipedia = 'https://en.wikipedia.org/wiki/Oscar_Pettiford'
SET person_1d4909875ca1.databases = ['http://d-nb.info/gnd/133111644', 'http://id.loc.gov/authorities/names/n85098446', 'https://catalogue.bnf.fr/ark:/12148/cb13898427w', 'http://snaccooperative.org/ark:/99166/w6df7c1p', 'https://rateyourmusic.com/artist/oscar-pettiford', 'https://www.worldcat.org/identities/lccn-n85098446']
SET person_1d4909875ca1.musicbrainz = 'https://musicbrainz.org/artist/28f6d494-d44b-4bd3-aed9-1d4909875ca1'
SET person_1d4909875ca1.isni_list = ['http://isni.org/isni/0000000081037921']
SET person_1d4909875ca1.source = 'musicbrainz.org'
SET person_1d4909875ca1.timestamp = timestamp()

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
SET person_6f0a331cc1ca.timestamp = timestamp()

// performances

MERGE (perf_46fc9e45df60:Performance{ uuid: '7d7eeecd-dd35-4db3-bcbf-46fc9e45df60' })
SET perf_46fc9e45df60.name = 'Tea for Two'
SET perf_46fc9e45df60.duration = '5:38'
SET perf_46fc9e45df60.source = 'musicbrainz.org'
SET perf_46fc9e45df60.timestamp = timestamp()

MERGE (perf_6667405bd6e2:Performance{ uuid: 'a2ab7b7a-9d9e-452d-9b51-6667405bd6e2' })
SET perf_6667405bd6e2.name = 'It Could Happen to You'
SET perf_6667405bd6e2.duration = '3:34'
SET perf_6667405bd6e2.source = 'musicbrainz.org'
SET perf_6667405bd6e2.timestamp = timestamp()

MERGE (perf_b5857883c913:Performance{ uuid: '4b2ea8ff-6865-431f-8fc3-b5857883c913' })
SET perf_b5857883c913.name = 'Lover Come Back to Me'
SET perf_b5857883c913.duration = '6:59'
SET perf_b5857883c913.source = 'musicbrainz.org'
SET perf_b5857883c913.timestamp = timestamp()

MERGE (perf_26ea14bf9969:Performance{ uuid: 'aab952c8-00df-4bbd-a3ea-26ea14bf9969' })
SET perf_26ea14bf9969.name = 'Lullaby of Birdland'
SET perf_26ea14bf9969.duration = '2:56'
SET perf_26ea14bf9969.source = 'musicbrainz.org'
SET perf_26ea14bf9969.timestamp = timestamp()

MERGE (perf_fd20062aecdd:Performance{ uuid: '74ea5d40-5007-4353-bf8f-fd20062aecdd' })
SET perf_fd20062aecdd.name = 'I Want to Be Happy'
SET perf_fd20062aecdd.duration = '3:32'
SET perf_fd20062aecdd.source = 'musicbrainz.org'
SET perf_fd20062aecdd.timestamp = timestamp()

MERGE (perf_b9b2fe62cb76:Performance{ uuid: '864f3b8a-8adc-4eb2-afae-b9b2fe62cb76' })
SET perf_b9b2fe62cb76.name = 'Embracable You'
SET perf_b9b2fe62cb76.duration = '4:15'
SET perf_b9b2fe62cb76.source = 'musicbrainz.org'
SET perf_b9b2fe62cb76.timestamp = timestamp()

MERGE (perf_c4b7dac3a1dd:Performance{ uuid: '086858ac-f5e5-4fe9-ad27-c4b7dac3a1dd' })
SET perf_c4b7dac3a1dd.name = 'I\'ve Got You Under My Skin'
SET perf_c4b7dac3a1dd.duration = '2:43'
SET perf_c4b7dac3a1dd.source = 'musicbrainz.org'
SET perf_c4b7dac3a1dd.timestamp = timestamp()

MERGE (perf_bf7b7faaf378:Performance{ uuid: '1267aead-a4a7-4379-b8f0-bf7b7faaf378' })
SET perf_bf7b7faaf378.name = 'Ornithology'
SET perf_bf7b7faaf378.duration = '3:01'
SET perf_bf7b7faaf378.source = 'musicbrainz.org'
SET perf_bf7b7faaf378.timestamp = timestamp()


// tracks
MERGE (release_d56f49d1bd7a)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_46fc9e45df60)
MERGE (release_d56f49d1bd7a)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_6667405bd6e2)
MERGE (release_d56f49d1bd7a)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_b5857883c913)
MERGE (release_d56f49d1bd7a)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_26ea14bf9969)
MERGE (release_d56f49d1bd7a)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_fd20062aecdd)
MERGE (release_d56f49d1bd7a)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_b9b2fe62cb76)
MERGE (release_d56f49d1bd7a)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_c4b7dac3a1dd)
MERGE (release_d56f49d1bd7a)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_bf7b7faaf378)

// works

MERGE (person_8825529afd5d:Person{ uuid: 'c9b9ec99-b592-4556-aa0b-8825529afd5d' }) 
SET person_8825529afd5d.name = 'Johnny Burke'
SET person_8825529afd5d.gender = 'Male'
SET person_8825529afd5d.disambiguation = 'American lyricist, 1908-1964'
SET person_8825529afd5d.country = 'US'
SET person_8825529afd5d.allmusic = 'https://www.allmusic.com/artist/mn0001053846'
SET person_8825529afd5d.discogs = 'https://www.discogs.com/artist/301993'
SET person_8825529afd5d.imdb = 'https://www.imdb.com/name/nm0121741/'
SET person_8825529afd5d.viaf = 'http://viaf.org/viaf/76583294'
SET person_8825529afd5d.wikidata = 'https://www.wikidata.org/wiki/Q743229'
SET person_8825529afd5d.databases = ['http://d-nb.info/gnd/102085412X', 'http://id.loc.gov/authorities/names/no89004670', 'https://catalogue.bnf.fr/ark:/12148/cb148427966', 'http://snaccooperative.org/ark:/99166/w6z61w7v', 'https://nla.gov.au/nla.party-887950', 'https://rateyourmusic.com/artist/johnny_burke_f1', 'https://www.ibdb.com/person.php?id=11462', 'https://www.worldcat.org/identities/lccn-no89004670/']
SET person_8825529afd5d.musicbrainz = 'https://musicbrainz.org/artist/c9b9ec99-b592-4556-aa0b-8825529afd5d'
SET person_8825529afd5d.isni_list = ['http://isni.org/isni/0000000071400010']
SET person_8825529afd5d.source = 'musicbrainz.org'
SET person_8825529afd5d.timestamp = timestamp()

MERGE (person_a37897b950ce:Person{ uuid: '4a94a6cb-e70a-418b-bb53-a37897b950ce' }) 
SET person_a37897b950ce.name = 'Cole Porter'
SET person_a37897b950ce.gender = 'Male'
SET person_a37897b950ce.disambiguation = 'composer'
SET person_a37897b950ce.country = 'US'
SET person_a37897b950ce.allmusic = 'https://www.allmusic.com/artist/mn0000109607'
SET person_a37897b950ce.discogs = 'https://www.discogs.com/artist/264026'
SET person_a37897b950ce.imdb = 'https://www.imdb.com/name/nm0006234/'
SET person_a37897b950ce.viaf = 'http://viaf.org/viaf/5118684'
SET person_a37897b950ce.wikidata = 'https://www.wikidata.org/wiki/Q215120'
SET person_a37897b950ce.databases = ['http://d-nb.info/gnd/11879292X', 'http://id.loc.gov/authorities/names/n80017862', 'https://catalogue.bnf.fr/ark:/12148/cb13898618g', 'https://ibdb.com/person.php?id=12257', 'http://snaccooperative.org/ark:/99166/w6j38s5m', 'https://nla.gov.au/nla.party-949524', 'https://openlibrary.org/works/OL709416A', 'http://soundtrackcollector.com/composer/166/', 'https://rateyourmusic.com/artist/cole_porter', 'https://www.worldcat.org/identities/lccn-n80017862', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Cole&last=Porter&middle=']
SET person_a37897b950ce.musicbrainz = 'https://musicbrainz.org/artist/4a94a6cb-e70a-418b-bb53-a37897b950ce'
SET person_a37897b950ce.isni_list = ['http://isni.org/isni/0000000108653610']
SET person_a37897b950ce.source = 'musicbrainz.org'
SET person_a37897b950ce.timestamp = timestamp()

MERGE (person_191ca24ad661:Person{ uuid: '7e43f216-d19c-4668-a939-191ca24ad661' }) 
SET person_191ca24ad661.name = 'Vincent Youmans'
SET person_191ca24ad661.gender = 'Male'
SET person_191ca24ad661.country = 'US'
SET person_191ca24ad661.discogs = 'https://www.discogs.com/artist/301996'
SET person_191ca24ad661.imdb = 'https://www.imdb.com/name/nm0949207/'
SET person_191ca24ad661.viaf = 'http://viaf.org/viaf/74039292'
SET person_191ca24ad661.wikidata = 'https://www.wikidata.org/wiki/Q746951'
SET person_191ca24ad661.databases = ['http://d-nb.info/gnd/11880815X', 'http://id.loc.gov/authorities/names/n80107199', 'https://catalogue.bnf.fr/ark:/12148/cb13901338w', 'https://ibdb.com/person.php?id=12607', 'http://snaccooperative.org/ark:/99166/w66t1fkb', 'https://nla.gov.au/nla.party-1227269', 'https://openlibrary.org/works/OL7514377A', 'https://www.worldcat.org/identities/lccn-n80107199/']
SET person_191ca24ad661.musicbrainz = 'https://musicbrainz.org/artist/7e43f216-d19c-4668-a939-191ca24ad661'
SET person_191ca24ad661.isni_list = ['http://isni.org/isni/0000000081543066']
SET person_191ca24ad661.source = 'musicbrainz.org'
SET person_191ca24ad661.timestamp = timestamp()

MERGE (person_98b47fc19825:Person{ uuid: 'f31022a9-f702-430d-9315-98b47fc19825' }) 
SET person_98b47fc19825.name = 'Irving Caesar'
SET person_98b47fc19825.gender = 'Male'
SET person_98b47fc19825.country = 'US'
SET person_98b47fc19825.allmusic = 'https://www.allmusic.com/artist/mn0000773150'
SET person_98b47fc19825.discogs = 'https://www.discogs.com/artist/301994'
SET person_98b47fc19825.imdb = 'https://www.imdb.com/name/nm0128371/'
SET person_98b47fc19825.viaf = 'http://viaf.org/viaf/54415815'
SET person_98b47fc19825.wikidata = 'https://www.wikidata.org/wiki/Q1284219'
SET person_98b47fc19825.databases = ['http://d-nb.info/gnd/135139783', 'http://id.loc.gov/authorities/names/no90027480', 'https://catalogue.bnf.fr/ark:/12148/cb14849329n', 'https://ibdb.com/person.php?id=6455', 'http://snaccooperative.org/ark:/99166/w6jd5b8j', 'https://nla.gov.au/nla.party-1203672', 'https://rateyourmusic.com/artist/irving_caesar', 'https://www.worldcat.org/identities/lccn-no90027480/']
SET person_98b47fc19825.musicbrainz = 'https://musicbrainz.org/artist/f31022a9-f702-430d-9315-98b47fc19825'
SET person_98b47fc19825.isni_list = ['http://isni.org/isni/0000000121337209']
SET person_98b47fc19825.source = 'musicbrainz.org'
SET person_98b47fc19825.timestamp = timestamp()

MERGE (person_9205b2f8f171:Person{ uuid: 'a383f062-e527-4a57-98b0-9205b2f8f171' }) 
SET person_9205b2f8f171.name = 'Oscar Hammerstein II'
SET person_9205b2f8f171.gender = 'Male'
SET person_9205b2f8f171.disambiguation = 'of Rodgers & Hammerstein'
SET person_9205b2f8f171.country = 'US'
SET person_9205b2f8f171.allmusic = 'https://www.allmusic.com/artist/mn0000804858'
SET person_9205b2f8f171.discogs = 'https://www.discogs.com/artist/253375'
SET person_9205b2f8f171.imdb = 'https://www.imdb.com/name/nm0358564/'
SET person_9205b2f8f171.viaf = 'http://viaf.org/viaf/196386'
SET person_9205b2f8f171.wikidata = 'https://www.wikidata.org/wiki/Q319693'
SET person_9205b2f8f171.databases = ['http://d-nb.info/gnd/11872018X', 'http://id.loc.gov/authorities/names/n50020012', 'https://catalogue.bnf.fr/ark:/12148/cb13894931j', 'https://ibdb.com/person.php?id=7965', 'http://snaccooperative.org/ark:/99166/w6vf7qf7', 'https://nla.gov.au/nla.party-869608', 'https://openlibrary.org/works/OL577328A', 'https://rateyourmusic.com/artist/oscar_hammerstein_ii', 'https://www.worldcat.org/identities/lccn-n50020012/']
SET person_9205b2f8f171.musicbrainz = 'https://musicbrainz.org/artist/a383f062-e527-4a57-98b0-9205b2f8f171'
SET person_9205b2f8f171.isni_list = ['http://isni.org/isni/0000000117358007']
SET person_9205b2f8f171.source = 'musicbrainz.org'
SET person_9205b2f8f171.timestamp = timestamp()

MERGE (person_a6d92136636f:Person{ uuid: '8d3f8b43-0d28-4500-900e-a6d92136636f' }) 
SET person_a6d92136636f.name = 'Jimmy Van Heusen'
SET person_a6d92136636f.gender = 'Male'
SET person_a6d92136636f.country = 'US'
SET person_a6d92136636f.allmusic = 'https://www.allmusic.com/artist/mn0000309464'
SET person_a6d92136636f.allmusic = 'https://www.allmusic.com/artist/mn0003168282'
SET person_a6d92136636f.discogs = 'https://www.discogs.com/artist/255313'
SET person_a6d92136636f.imdb = 'https://www.imdb.com/name/nm0006329/'
SET person_a6d92136636f.viaf = 'http://viaf.org/viaf/54338466'
SET person_a6d92136636f.wikidata = 'https://www.wikidata.org/wiki/Q33124'
SET person_a6d92136636f.databases = ['http://d-nb.info/gnd/134545370', 'http://id.loc.gov/authorities/names/n87146380', 'https://catalogue.bnf.fr/ark:/12148/cb13952105n', 'https://ibdb.com/person.php?id=12521', 'http://snaccooperative.org/ark:/99166/w6zc82bn', 'https://nla.gov.au/nla.party-887953', 'https://rateyourmusic.com/artist/jimmy_van_heusen', 'https://www.worldcat.org/identities/lccn-n87146380/']
SET person_a6d92136636f.musicbrainz = 'https://musicbrainz.org/artist/8d3f8b43-0d28-4500-900e-a6d92136636f'
SET person_a6d92136636f.isni_list = ['http://isni.org/isni/0000000081333253']
SET person_a6d92136636f.source = 'musicbrainz.org'
SET person_a6d92136636f.timestamp = timestamp()

MERGE (person_560575963ee1:Person{ uuid: '7dc2579e-4619-4087-ac78-560575963ee1' }) 
SET person_560575963ee1.name = 'B. Y. Forster'
SET person_560575963ee1.gender = 'Male'
SET person_560575963ee1.disambiguation = 'pseudonym of George David Weiss'
SET person_560575963ee1.country = 'US'
SET person_560575963ee1.source = 'musicbrainz.org'
SET person_560575963ee1.timestamp = timestamp()

MERGE (person_b693a808a158:Person{ uuid: '65744963-191a-44ef-a3c7-b693a808a158' }) 
SET person_b693a808a158.name = 'George Gershwin'
SET person_b693a808a158.gender = 'Male'
SET person_b693a808a158.disambiguation = 'composer'
SET person_b693a808a158.country = 'US'
SET person_b693a808a158.allmusic = 'https://www.allmusic.com/artist/mn0000197918'
SET person_b693a808a158.bbc = 'https://www.bbc.co.uk/music/artists/65744963-191a-44ef-a3c7-b693a808a158'
SET person_b693a808a158.discogs = 'https://www.discogs.com/artist/261293'
SET person_b693a808a158.imdb = 'https://www.imdb.com/name/nm0006097/'
SET person_b693a808a158.viaf = 'http://viaf.org/viaf/61554329'
SET person_b693a808a158.wikidata = 'https://www.wikidata.org/wiki/Q123829'
SET person_b693a808a158.databases = ['http://d-nb.info/gnd/118639226', 'http://id.loc.gov/authorities/names/n79077265', 'https://catalogue.bnf.fr/ark:/12148/cb119493251', 'https://ibdb.com/person.php?id=5813', 'http://snaccooperative.org/ark:/99166/w6x065dx', 'https://nla.gov.au/nla.party-832382', 'https://openlibrary.org/works/OL67761A', 'http://soundtrackcollector.com/composer/33/', 'https://rateyourmusic.com/artist/george_gershwin', 'https://www.worldcat.org/identities/lccn-n79077265']
SET person_b693a808a158.musicbrainz = 'https://musicbrainz.org/artist/65744963-191a-44ef-a3c7-b693a808a158'
SET person_b693a808a158.isni_list = ['http://isni.org/isni/0000000121355968']
SET person_b693a808a158.source = 'musicbrainz.org'
SET person_b693a808a158.timestamp = timestamp()

MERGE (person_db94dd8e2e52:Person{ uuid: '3c2caff5-ffbc-4711-9e4e-db94dd8e2e52' }) 
SET person_db94dd8e2e52.name = 'Sigmund Romberg'
SET person_db94dd8e2e52.gender = 'Male'
SET person_db94dd8e2e52.country = 'US'
SET person_db94dd8e2e52.allmusic = 'https://www.allmusic.com/artist/mn0000686744'
SET person_db94dd8e2e52.discogs = 'https://www.discogs.com/artist/253376'
SET person_db94dd8e2e52.imdb = 'https://www.imdb.com/name/nm0739146/'
SET person_db94dd8e2e52.viaf = 'http://viaf.org/viaf/46947501'
SET person_db94dd8e2e52.wikidata = 'https://www.wikidata.org/wiki/Q742945'
SET person_db94dd8e2e52.databases = ['http://d-nb.info/gnd/119147025', 'http://id.loc.gov/authorities/names/n84212849', 'https://catalogue.bnf.fr/ark:/12148/cb13899141v', 'https://ibdb.com/person.php?id=8686', 'http://snaccooperative.org/ark:/99166/w66w98qs', 'https://nla.gov.au/nla.party-1044652', 'https://openlibrary.org/works/OL2296799A', 'https://rateyourmusic.com/artist/sigmund_romberg', 'https://www.worldcat.org/identities/lccn-n84212849/']
SET person_db94dd8e2e52.musicbrainz = 'https://musicbrainz.org/artist/3c2caff5-ffbc-4711-9e4e-db94dd8e2e52'
SET person_db94dd8e2e52.isni_list = ['http://isni.org/isni/0000000083797326']
SET person_db94dd8e2e52.source = 'musicbrainz.org'
SET person_db94dd8e2e52.timestamp = timestamp()

MERGE (person_c73775716312:Person{ uuid: 'c7356af9-9ea6-4a78-a55b-c73775716312' }) 
SET person_c73775716312.name = 'Charlie Parker'
SET person_c73775716312.gender = 'Male'
SET person_c73775716312.disambiguation = 'a.k.a. “Bird”, jazz alto saxophonist'
SET person_c73775716312.country = 'US'
SET person_c73775716312.allmusic = 'https://www.allmusic.com/artist/mn0000211758'
SET person_c73775716312.bbc = 'https://www.bbc.co.uk/music/artists/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.discogs = 'https://www.discogs.com/artist/75617'
SET person_c73775716312.imdb = 'https://www.imdb.com/name/nm0662127/'
SET person_c73775716312.viaf = 'http://viaf.org/viaf/10034216'
SET person_c73775716312.wikidata = 'https://www.wikidata.org/wiki/Q103767'
SET person_c73775716312.databases = ['http://d-nb.info/gnd/118739328', 'http://id.loc.gov/authorities/names/n50050327', 'https://catalogue.bnf.fr/ark:/12148/cb13898247z', 'http://snaccooperative.org/ark:/99166/w67086vq', 'https://nla.gov.au/nla.party-911160', 'https://openlibrary.org/works/OL4918032A', 'https://rateyourmusic.com/artist/charlie_parker', 'https://www.musik-sammler.de/artist/charlie-parker/', 'https://www.worldcat.org/identities/lccn-n50050327']
SET person_c73775716312.musicbrainz = 'https://musicbrainz.org/artist/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.isni_list = ['http://isni.org/isni/0000000120955806', 'http://isni.org/isni/0000000368633974']
SET person_c73775716312.source = 'musicbrainz.org'
SET person_c73775716312.timestamp = timestamp()

MERGE (person_df9db18b28e9:Person{ uuid: 'ef83af4c-4da9-47d1-b9bd-df9db18b28e9' }) 
SET person_df9db18b28e9.name = 'George Shearing'
SET person_df9db18b28e9.gender = 'Male'
SET person_df9db18b28e9.country = 'GB'
SET person_df9db18b28e9.allmusic = 'https://www.allmusic.com/artist/mn0000642664'
SET person_df9db18b28e9.discogs = 'https://www.discogs.com/artist/59407'
SET person_df9db18b28e9.imdb = 'https://www.imdb.com/name/nm0790471/'
SET person_df9db18b28e9.viaf = 'http://viaf.org/viaf/37103429'
SET person_df9db18b28e9.wikidata = 'https://www.wikidata.org/wiki/Q349346'
SET person_df9db18b28e9.databases = ['http://d-nb.info/gnd/129402613', 'http://id.loc.gov/authorities/names/n81015302', 'https://catalogue.bnf.fr/ark:/12148/cb13899721w', 'http://snaccooperative.org/ark:/99166/w6j39n8p', 'https://www.worldcat.org/identities/lccn-n81015302']
SET person_df9db18b28e9.musicbrainz = 'https://musicbrainz.org/artist/ef83af4c-4da9-47d1-b9bd-df9db18b28e9'
SET person_df9db18b28e9.isni_list = ['http://isni.org/isni/0000000120239981']
SET person_df9db18b28e9.source = 'musicbrainz.org'
SET person_df9db18b28e9.timestamp = timestamp()

MERGE (person_a4cb6fbe4434:Person{ uuid: '57e1817c-4ff5-4079-9381-a4cb6fbe4434' }) 
SET person_a4cb6fbe4434.name = 'Benny Harris'
SET person_a4cb6fbe4434.gender = 'Male'
SET person_a4cb6fbe4434.country = 'US'
SET person_a4cb6fbe4434.allmusic = 'https://www.allmusic.com/artist/mn0000792654'
SET person_a4cb6fbe4434.discogs = 'https://www.discogs.com/artist/415785'
SET person_a4cb6fbe4434.viaf = 'http://viaf.org/viaf/56799353'
SET person_a4cb6fbe4434.wikidata = 'https://www.wikidata.org/wiki/Q818056'
SET person_a4cb6fbe4434.wikipedia = 'https://en.wikipedia.org/wiki/Benny_Harris'
SET person_a4cb6fbe4434.databases = ['http://id.loc.gov/authorities/names/no00031677', 'https://catalogue.bnf.fr/ark:/12148/cb13931543n', 'http://snaccooperative.org/ark:/99166/w65f1g1g', 'https://www.worldcat.org/identities/lccn-no00031677']
SET person_a4cb6fbe4434.musicbrainz = 'https://musicbrainz.org/artist/57e1817c-4ff5-4079-9381-a4cb6fbe4434'
SET person_a4cb6fbe4434.isni_list = ['http://isni.org/isni/0000000038894792']
SET person_a4cb6fbe4434.source = 'musicbrainz.org'
SET person_a4cb6fbe4434.timestamp = timestamp()

MERGE (person_322e34240ffc:Person{ uuid: '509086c2-9cc8-4e77-89e9-322e34240ffc' }) 
SET person_322e34240ffc.name = 'Ira Gershwin'
SET person_322e34240ffc.gender = 'Male'
SET person_322e34240ffc.country = 'US'
SET person_322e34240ffc.allmusic = 'https://www.allmusic.com/artist/mn0000200301'
SET person_322e34240ffc.discogs = 'https://www.discogs.com/artist/264105'
SET person_322e34240ffc.imdb = 'https://www.imdb.com/name/nm0314857/'
SET person_322e34240ffc.viaf = 'http://viaf.org/viaf/39519496'
SET person_322e34240ffc.wikidata = 'https://www.wikidata.org/wiki/Q61059'
SET person_322e34240ffc.databases = ['http://d-nb.info/gnd/119500027', 'http://id.loc.gov/authorities/names/n50076010', 'https://catalogue.bnf.fr/ark:/12148/cb13194929s', 'https://ibdb.com/person.php?id=6435', 'http://snaccooperative.org/ark:/99166/w60w94tm', 'https://nla.gov.au/nla.party-965252', 'https://openlibrary.org/works/OL233692A', 'https://rateyourmusic.com/artist/ira_gershwin', 'https://www.worldcat.org/identities/lccn-n50076010/']
SET person_322e34240ffc.musicbrainz = 'https://musicbrainz.org/artist/509086c2-9cc8-4e77-89e9-322e34240ffc'
SET person_322e34240ffc.isni_list = ['http://isni.org/isni/0000000108901469']
SET person_322e34240ffc.source = 'musicbrainz.org'
SET person_322e34240ffc.timestamp = timestamp()

MERGE (work_4411df467d9b:Work{ uuid: 'bc51cec1-1c4d-3b1b-83a7-4411df467d9b' })
SET work_4411df467d9b.name = 'Lullaby of Birdland'
SET work_4411df467d9b.iswc = 'T-070.268.678-9'
SET work_4411df467d9b.type = 'Song'
SET work_4411df467d9b.wikidata = 'https://www.wikidata.org/wiki/Q1434051'
SET work_4411df467d9b.musicbrainz = 'https://musicbrainz.org/work/bc51cec1-1c4d-3b1b-83a7-4411df467d9b'
SET work_4411df467d9b.source = 'musicbrainz.org'
SET work_4411df467d9b.timestamp = timestamp()

MERGE (work_7c0d2793d8d9:Work{ uuid: '13869248-f36a-3fe0-a8bd-7c0d2793d8d9' })
SET work_7c0d2793d8d9.name = 'Embraceable You'
SET work_7c0d2793d8d9.iswc = 'T-010.433.969-6'
SET work_7c0d2793d8d9.type = 'Song'
SET work_7c0d2793d8d9.wikidata = 'https://www.wikidata.org/wiki/Q753607'
SET work_7c0d2793d8d9.musicbrainz = 'https://musicbrainz.org/work/13869248-f36a-3fe0-a8bd-7c0d2793d8d9'
SET work_7c0d2793d8d9.source = 'musicbrainz.org'
SET work_7c0d2793d8d9.timestamp = timestamp()

MERGE (work_5c9cfcd50e62:Work{ uuid: '1f69a658-acd8-32ca-9d6d-5c9cfcd50e62' })
SET work_5c9cfcd50e62.name = 'I’ve Got You Under My Skin'
SET work_5c9cfcd50e62.iswc = 'T-070.907.808-9'
SET work_5c9cfcd50e62.type = 'Song'
SET work_5c9cfcd50e62.wikidata = 'https://www.wikidata.org/wiki/Q2165861'
SET work_5c9cfcd50e62.musicbrainz = 'https://musicbrainz.org/work/1f69a658-acd8-32ca-9d6d-5c9cfcd50e62'
SET work_5c9cfcd50e62.source = 'musicbrainz.org'
SET work_5c9cfcd50e62.timestamp = timestamp()

MERGE (work_8752c89c7034:Work{ uuid: '4ee0ac5c-a2d2-3f7c-991a-8752c89c7034' })
SET work_8752c89c7034.name = 'I Want to Be Happy'
SET work_8752c89c7034.iswc = 'T-070.904.673-0'
SET work_8752c89c7034.type = 'Song'
SET work_8752c89c7034.wikidata = 'https://www.wikidata.org/wiki/Q5979567'
SET work_8752c89c7034.wikipedia = 'https://en.wikipedia.org/wiki/I_Want_to_Be_Happy'
SET work_8752c89c7034.musicbrainz = 'https://musicbrainz.org/work/4ee0ac5c-a2d2-3f7c-991a-8752c89c7034'
SET work_8752c89c7034.source = 'musicbrainz.org'
SET work_8752c89c7034.timestamp = timestamp()

MERGE (work_bc5765ec131f:Work{ uuid: '6c3b2860-0c5f-38fc-9e92-bc5765ec131f' })
SET work_bc5765ec131f.name = 'Ornithology'
SET work_bc5765ec131f.source = 'musicbrainz.org'
SET work_bc5765ec131f.timestamp = timestamp()

MERGE (work_096f8295111c:Work{ uuid: '2b10cff9-a483-306f-9bfa-096f8295111c' })
SET work_096f8295111c.name = 'Lover, Come Back to Me'
SET work_096f8295111c.iswc = 'T-070.097.652-8'
SET work_096f8295111c.type = 'Song'
SET work_096f8295111c.wikidata = 'https://www.wikidata.org/wiki/Q939331'
SET work_096f8295111c.musicbrainz = 'https://musicbrainz.org/work/2b10cff9-a483-306f-9bfa-096f8295111c'
SET work_096f8295111c.source = 'musicbrainz.org'
SET work_096f8295111c.timestamp = timestamp()

MERGE (work_eb25c8dae551:Work{ uuid: '8bb32887-ef94-3365-be5f-eb25c8dae551' })
SET work_eb25c8dae551.name = 'Tea for Two'
SET work_eb25c8dae551.iswc = 'T-070.178.141-0'
SET work_eb25c8dae551.type = 'Song'
SET work_eb25c8dae551.wikidata = 'https://www.wikidata.org/wiki/Q1725760'
SET work_eb25c8dae551.musicbrainz = 'https://musicbrainz.org/work/8bb32887-ef94-3365-be5f-eb25c8dae551'
SET work_eb25c8dae551.source = 'musicbrainz.org'
SET work_eb25c8dae551.timestamp = timestamp()

MERGE (work_caa47b30366c:Work{ uuid: '6d489d45-3e3b-3bd9-a178-caa47b30366c' })
SET work_caa47b30366c.name = 'It Could Happen to You'
SET work_caa47b30366c.iswc = 'T-070.907.037-0'
SET work_caa47b30366c.type = 'Song'
SET work_caa47b30366c.wikidata = 'https://www.wikidata.org/wiki/Q820861'
SET work_caa47b30366c.musicbrainz = 'https://musicbrainz.org/work/6d489d45-3e3b-3bd9-a178-caa47b30366c'
SET work_caa47b30366c.source = 'musicbrainz.org'
SET work_caa47b30366c.timestamp = timestamp()


// performances of
MERGE (perf_26ea14bf9969)-[:PERFORMANCE_OF]->(work_4411df467d9b)
MERGE (perf_b9b2fe62cb76)-[:PERFORMANCE_OF]->(work_7c0d2793d8d9)
MERGE (perf_c4b7dac3a1dd)-[:PERFORMANCE_OF]->(work_5c9cfcd50e62)
MERGE (perf_fd20062aecdd)-[:PERFORMANCE_OF]->(work_8752c89c7034)
MERGE (perf_bf7b7faaf378)-[:PERFORMANCE_OF]->(work_bc5765ec131f)
MERGE (perf_b5857883c913)-[:PERFORMANCE_OF]->(work_096f8295111c)
MERGE (perf_46fc9e45df60)-[:PERFORMANCE_OF]->(work_eb25c8dae551)
MERGE (perf_6667405bd6e2)-[:PERFORMANCE_OF]->(work_caa47b30366c)


// composers
MERGE (person_df9db18b28e9)-[:COMPOSED]->(work_4411df467d9b)
MERGE (person_560575963ee1)-[:WROTE_LYRICS]->(work_4411df467d9b)
MERGE (person_b693a808a158)-[:COMPOSED]->(work_7c0d2793d8d9)
MERGE (person_322e34240ffc)-[:WROTE_LYRICS]->(work_7c0d2793d8d9)
MERGE (person_a37897b950ce)-[:COMPOSED]->(work_5c9cfcd50e62)
MERGE (person_a37897b950ce)-[:WROTE_LYRICS]->(work_5c9cfcd50e62)
MERGE (person_98b47fc19825)-[:COMPOSED]->(work_8752c89c7034)
MERGE (person_191ca24ad661)-[:COMPOSED]->(work_8752c89c7034)
MERGE (person_98b47fc19825)-[:WROTE_LYRICS]->(work_8752c89c7034)
MERGE (person_a4cb6fbe4434)-[:COMPOSED]->(work_bc5765ec131f)
MERGE (person_c73775716312)-[:COMPOSED]->(work_bc5765ec131f)
MERGE (person_db94dd8e2e52)-[:COMPOSED]->(work_096f8295111c)
MERGE (person_9205b2f8f171)-[:WROTE_LYRICS]->(work_096f8295111c)
MERGE (person_191ca24ad661)-[:COMPOSED]->(work_eb25c8dae551)
MERGE (person_98b47fc19825)-[:WROTE_LYRICS]->(work_eb25c8dae551)
MERGE (person_a6d92136636f)-[:COMPOSED]->(work_caa47b30366c)
MERGE (person_8825529afd5d)-[:WROTE_LYRICS]->(work_caa47b30366c)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_46fc9e45df60)
MERGE (person_1d4909875ca1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_46fc9e45df60)
MERGE (person_340d64fbb41c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_46fc9e45df60)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6667405bd6e2)
MERGE (person_1d4909875ca1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_6667405bd6e2)
MERGE (person_340d64fbb41c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6667405bd6e2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_b5857883c913)
MERGE (person_1d4909875ca1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_b5857883c913)
MERGE (person_340d64fbb41c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b5857883c913)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_26ea14bf9969)
MERGE (person_1d4909875ca1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_26ea14bf9969)
MERGE (person_340d64fbb41c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_26ea14bf9969)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_fd20062aecdd)
MERGE (person_1d4909875ca1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_fd20062aecdd)
MERGE (person_340d64fbb41c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_fd20062aecdd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_b9b2fe62cb76)
MERGE (person_1d4909875ca1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_b9b2fe62cb76)
MERGE (person_340d64fbb41c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b9b2fe62cb76)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_c4b7dac3a1dd)
MERGE (person_1d4909875ca1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_c4b7dac3a1dd)
MERGE (person_340d64fbb41c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_c4b7dac3a1dd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_bf7b7faaf378)
MERGE (person_1d4909875ca1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_bf7b7faaf378)
MERGE (person_340d64fbb41c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bf7b7faaf378)

