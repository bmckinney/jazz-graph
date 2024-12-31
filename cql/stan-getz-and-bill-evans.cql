// releases

MERGE (release_e71e710fef1f:Release{ uuid: 'f990c0ae-8b2d-49bd-ae87-e71e710fef1f' })
SET release_e71e710fef1f.name = 'Stan Getz & Bill Evans'
SET release_e71e710fef1f.country = 'US'
SET release_e71e710fef1f.date = '1973'
SET release_e71e710fef1f.format = '12" Vinyl'
SET release_e71e710fef1f.discode = 'V6-8833'
SET release_e71e710fef1f.musicbrainz = 'http://musicbrainz.org/release/f990c0ae-8b2d-49bd-ae87-e71e710fef1f'
SET release_e71e710fef1f.source = 'musicbrainz.org'
SET release_e71e710fef1f.timestamp = timestamp()

MERGE (person_d7529f22d78a:Person{ uuid: '82c19813-15ec-4b5f-a06a-d7529f22d78a' }) 
SET person_d7529f22d78a.name = 'Creed Taylor'
SET person_d7529f22d78a.gender = 'Male'
SET person_d7529f22d78a.country = 'US'
SET person_d7529f22d78a.allmusic = 'https://www.allmusic.com/artist/mn0000135180'
SET person_d7529f22d78a.discogs = 'https://www.discogs.com/artist/97480'
SET person_d7529f22d78a.viaf = 'http://viaf.org/viaf/268476531'
SET person_d7529f22d78a.wikidata = 'https://www.wikidata.org/wiki/Q1139476'
SET person_d7529f22d78a.databases = ['http://id.loc.gov/authorities/names/no98027837', 'https://catalogue.bnf.fr/ark:/12148/cb14643938g', 'https://d-nb.info/gnd/1023707462', 'https://rateyourmusic.com/artist/creed_taylor', 'https://www.worldcat.org/identities/lccn-no98027837']
SET person_d7529f22d78a.musicbrainz = 'https://musicbrainz.org/artist/82c19813-15ec-4b5f-a06a-d7529f22d78a'
SET person_d7529f22d78a.isni_list = ['http://isni.org/isni/0000000383306568']
SET person_d7529f22d78a.source = 'musicbrainz.org'
SET person_d7529f22d78a.timestamp = timestamp()

MERGE (person_bed4063208e7:Person{ uuid: 'd5ac66e4-ea5d-4ebb-9e0d-bed4063208e7' }) 
SET person_bed4063208e7.name = 'Elvin Jones'
SET person_bed4063208e7.gender = 'Male'
SET person_bed4063208e7.disambiguation = 'jazz drummer'
SET person_bed4063208e7.country = 'US'
SET person_bed4063208e7.allmusic = 'https://www.allmusic.com/artist/mn0000179379'
SET person_bed4063208e7.discogs = 'https://www.discogs.com/artist/135885'
SET person_bed4063208e7.imdb = 'https://www.imdb.com/name/nm0428033/'
SET person_bed4063208e7.viaf = 'http://viaf.org/viaf/51875623'
SET person_bed4063208e7.wikidata = 'https://www.wikidata.org/wiki/Q357179'
SET person_bed4063208e7.databases = ['http://id.loc.gov/authorities/names/n81058238', 'https://catalogue.bnf.fr/ark:/12148/cb13895719c', 'https://d-nb.info/gnd/129060917', 'http://snaccooperative.org/ark:/99166/w6x48sqj', 'https://nla.gov.au/nla.party-1067547', 'https://rateyourmusic.com/artist/elvin_jones', 'https://www.worldcat.org/identities/lccn-n81058238']
SET person_bed4063208e7.musicbrainz = 'https://musicbrainz.org/artist/d5ac66e4-ea5d-4ebb-9e0d-bed4063208e7'
SET person_bed4063208e7.isni_list = ['http://isni.org/isni/0000000116420593']
SET person_bed4063208e7.source = 'musicbrainz.org'
SET person_bed4063208e7.timestamp = timestamp()

MERGE (person_afe9622fab32:Person{ uuid: '8f2422ab-0ec6-4c92-80c4-afe9622fab32' }) 
SET person_afe9622fab32.name = 'Stan Getz'
SET person_afe9622fab32.gender = 'Male'
SET person_afe9622fab32.country = 'US'
SET person_afe9622fab32.allmusic = 'https://www.allmusic.com/artist/mn0000742899'
SET person_afe9622fab32.discogs = 'https://www.discogs.com/artist/30486'
SET person_afe9622fab32.imdb = 'https://www.imdb.com/name/nm0315295/'
SET person_afe9622fab32.viaf = 'http://viaf.org/viaf/113597520'
SET person_afe9622fab32.wikidata = 'https://www.wikidata.org/wiki/Q30587'
SET person_afe9622fab32.databases = ['http://id.loc.gov/authorities/names/n81018141', 'https://adp.library.ucsb.edu/names/203669', 'https://catalogue.bnf.fr/ark:/12148/cb138944199', 'https://d-nb.info/gnd/119189941', 'http://snaccooperative.org/ark:/99166/w6v12bd6', 'https://nla.gov.au/nla.party-1024123', 'https://openlibrary.org/works/OL6199421A', 'https://rateyourmusic.com/artist/stan_getz', 'https://www.musik-sammler.de/artist/stan-getz/', 'https://www.worldcat.org/identities/lccn-n81-018141']
SET person_afe9622fab32.musicbrainz = 'https://musicbrainz.org/artist/8f2422ab-0ec6-4c92-80c4-afe9622fab32'
SET person_afe9622fab32.isni_list = ['http://isni.org/isni/0000000110330511']
SET person_afe9622fab32.source = 'musicbrainz.org'
SET person_afe9622fab32.timestamp = timestamp()

MERGE (person_ff9017878cdd:Person{ uuid: 'b59843a1-bb97-45f0-84b9-ff9017878cdd' }) 
SET person_ff9017878cdd.name = 'Richard Davis'
SET person_ff9017878cdd.gender = 'Male'
SET person_ff9017878cdd.disambiguation = 'American jazz bassist'
SET person_ff9017878cdd.country = 'US'
SET person_ff9017878cdd.allmusic = 'https://www.allmusic.com/artist/mn0000851653'
SET person_ff9017878cdd.discogs = 'https://www.discogs.com/artist/263441'
SET person_ff9017878cdd.viaf = 'http://viaf.org/viaf/120739764'
SET person_ff9017878cdd.wikidata = 'https://www.wikidata.org/wiki/Q716851'
SET person_ff9017878cdd.databases = ['http://id.loc.gov/authorities/names/n81015291', 'https://adp.library.ucsb.edu/names/202409', 'https://catalogue.bnf.fr/ark:/12148/cb13893033h', 'https://d-nb.info/gnd/134355792', 'http://snaccooperative.org/ark:/99166/w66d6dj7', 'https://rateyourmusic.com/artist/richard_davis', 'https://www.worldcat.org/identities/lccn-n81015291']
SET person_ff9017878cdd.musicbrainz = 'https://musicbrainz.org/artist/b59843a1-bb97-45f0-84b9-ff9017878cdd'
SET person_ff9017878cdd.isni_list = ['http://isni.org/isni/0000000079564079']
SET person_ff9017878cdd.source = 'musicbrainz.org'
SET person_ff9017878cdd.timestamp = timestamp()

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
SET person_e044666c4828.databases = ['http://id.loc.gov/authorities/names/n81014576', 'https://adp.library.ucsb.edu/names/307458', 'https://catalogue.bnf.fr/ark:/12148/cb138922167', 'https://d-nb.info/gnd/134344332', 'http://snaccooperative.org/ark:/99166/w67m16sc', 'https://rateyourmusic.com/artist/ron_carter', 'https://www.worldcat.org/identities/lccn-n81014576']
SET person_e044666c4828.musicbrainz = 'https://musicbrainz.org/artist/57db3f59-9c58-4f68-a00e-e044666c4828'
SET person_e044666c4828.isni_list = ['http://isni.org/isni/0000000114394862']
SET person_e044666c4828.source = 'musicbrainz.org'
SET person_e044666c4828.timestamp = timestamp()

MERGE (person_6c57b03a4e36:Person{ uuid: '8247a3f2-3a8e-4256-b322-6c57b03a4e36' }) 
SET person_6c57b03a4e36.name = 'Bill Evans'
SET person_6c57b03a4e36.gender = 'Male'
SET person_6c57b03a4e36.disambiguation = 'pianist'
SET person_6c57b03a4e36.country = 'US'
SET person_6c57b03a4e36.allmusic = 'https://www.allmusic.com/artist/mn0000764702'
SET person_6c57b03a4e36.bbc = 'https://www.bbc.co.uk/music/artists/8247a3f2-3a8e-4256-b322-6c57b03a4e36'
SET person_6c57b03a4e36.discogs = 'https://www.discogs.com/artist/252310'
SET person_6c57b03a4e36.imdb = 'https://www.imdb.com/name/nm0262572/'
SET person_6c57b03a4e36.viaf = 'http://viaf.org/viaf/29717820'
SET person_6c57b03a4e36.wikidata = 'https://www.wikidata.org/wiki/Q208205'
SET person_6c57b03a4e36.databases = ['http://id.loc.gov/authorities/names/n81147281', 'https://adp.library.ucsb.edu/names/203037', 'https://castalbums.org/people/Bill-Evans-1/11965', 'https://catalogue.bnf.fr/ark:/12148/cb13893736g', 'https://d-nb.info/gnd/137724519', 'https://id.oclc.org/worldcat/entity/E39PBJf8xcCTxHr9htXyQxwpyd', 'https://musicmoz.org/Bands_and_Artists/E/Evans,_Bill/', 'http://snaccooperative.org/ark:/99166/w6v411q5', 'https://openlibrary.org/authors/OL6591650A', 'https://openlibrary.org/authors/OL7514955A', 'https://operabase.com/a2242729', 'https://rateyourmusic.com/artist/bill_evans', 'https://www.dramonline.org/composers/evans-bill', 'https://www.librarything.com/author/evansbill-1-5203912', 'https://www.musik-sammler.de/artist/175764/', 'https://www.muziekweb.nl/Link/M00000255981/POPULAR/', 'https://www.themoviedb.org/person/137953', 'https://www.whosampled.com/Bill-Evans/', 'https://www.worldcat.org/identities/lccn-n81-147281', 'http://www.maniadb.com/artist/117793']
SET person_6c57b03a4e36.musicbrainz = 'https://musicbrainz.org/artist/8247a3f2-3a8e-4256-b322-6c57b03a4e36'
SET person_6c57b03a4e36.isni_list = ['http://isni.org/isni/0000000121261603']
SET person_6c57b03a4e36.source = 'musicbrainz.org'
SET person_6c57b03a4e36.timestamp = timestamp()
// labels

MERGE (label_00fbcc4fce83:Label{ uuid: '99a24d71-54c1-4d3f-88cc-00fbcc4fce83' })
SET label_00fbcc4fce83.name= 'Verve'

// performances

MERGE (perf_414af61aa29f:Performance{ uuid: '75f5135d-03ee-405d-b6f5-414af61aa29f' })
SET perf_414af61aa29f.name = 'Night and Day'
SET perf_414af61aa29f.duration = '6:48'
SET perf_414af61aa29f.begin = '1964-05-06'
SET perf_414af61aa29f.end = '1964-05-06'
SET perf_414af61aa29f.source = 'musicbrainz.org'
SET perf_414af61aa29f.timestamp = timestamp()

MERGE (perf_5e8fae86fb4f:Performance{ uuid: '29b31c4c-3b78-4802-b226-5e8fae86fb4f' })
SET perf_5e8fae86fb4f.name = 'But Beautiful'
SET perf_5e8fae86fb4f.duration = '4:42'
SET perf_5e8fae86fb4f.begin = '1964-05-06'
SET perf_5e8fae86fb4f.end = '1964-05-06'
SET perf_5e8fae86fb4f.source = 'musicbrainz.org'
SET perf_5e8fae86fb4f.timestamp = timestamp()

MERGE (perf_229954f7d189:Performance{ uuid: 'f984c460-c37e-4742-bc84-229954f7d189' })
SET perf_229954f7d189.name = 'Funkallero'
SET perf_229954f7d189.duration = '6:42'
SET perf_229954f7d189.begin = '1964-05-06'
SET perf_229954f7d189.end = '1964-05-06'
SET perf_229954f7d189.source = 'musicbrainz.org'
SET perf_229954f7d189.timestamp = timestamp()

MERGE (perf_10ca9224f107:Performance{ uuid: 'a2d91040-b34d-481f-88f3-10ca9224f107' })
SET perf_10ca9224f107.name = 'My Heart Stood Still'
SET perf_10ca9224f107.duration = '8:37'
SET perf_10ca9224f107.begin = '1964-05-05'
SET perf_10ca9224f107.end = '1964-05-05'
SET perf_10ca9224f107.source = 'musicbrainz.org'
SET perf_10ca9224f107.timestamp = timestamp()

MERGE (perf_e67b21f1ebe1:Performance{ uuid: '64eb038e-d27e-4f10-97b4-e67b21f1ebe1' })
SET perf_e67b21f1ebe1.name = 'Melinda'
SET perf_e67b21f1ebe1.duration = '5:04'
SET perf_e67b21f1ebe1.begin = '1964-05-05'
SET perf_e67b21f1ebe1.end = '1964-05-05'
SET perf_e67b21f1ebe1.source = 'musicbrainz.org'
SET perf_e67b21f1ebe1.timestamp = timestamp()

MERGE (perf_a7752d73af38:Performance{ uuid: '43caebc7-76ce-4c8a-9cf9-a7752d73af38' })
SET perf_a7752d73af38.name = 'Grandfather’s Waltz'
SET perf_a7752d73af38.duration = '6:28'
SET perf_a7752d73af38.begin = '1964-05-05'
SET perf_a7752d73af38.end = '1964-05-05'
SET perf_a7752d73af38.source = 'musicbrainz.org'
SET perf_a7752d73af38.timestamp = timestamp()



// labels
MERGE (release_e71e710fef1f)-[:HAS_LABEL]->(label_00fbcc4fce83)


// tracks
MERGE (release_e71e710fef1f)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_414af61aa29f)
MERGE (release_e71e710fef1f)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_5e8fae86fb4f)
MERGE (release_e71e710fef1f)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_229954f7d189)
MERGE (release_e71e710fef1f)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_10ca9224f107)
MERGE (release_e71e710fef1f)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_e67b21f1ebe1)
MERGE (release_e71e710fef1f)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_a7752d73af38)

// works

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
SET person_a6d92136636f.databases = ['http://id.loc.gov/authorities/names/n87146380', 'https://adp.library.ucsb.edu/names/105592', 'https://catalogue.bnf.fr/ark:/12148/cb13952105n', 'https://d-nb.info/gnd/134545370', 'https://ibdb.com/person.php?id=12521', 'http://snaccooperative.org/ark:/99166/w6zc82bn', 'https://nla.gov.au/nla.party-887953', 'https://rateyourmusic.com/artist/jimmy_van_heusen', 'https://www.worldcat.org/identities/lccn-n87146380/']
SET person_a6d92136636f.musicbrainz = 'https://musicbrainz.org/artist/8d3f8b43-0d28-4500-900e-a6d92136636f'
SET person_a6d92136636f.isni_list = ['http://isni.org/isni/0000000081333253']
SET person_a6d92136636f.source = 'musicbrainz.org'
SET person_a6d92136636f.timestamp = timestamp()

MERGE (person_f2852d147c2e:Person{ uuid: '56b7ad8e-3c4f-4f14-914d-f2852d147c2e' }) 
SET person_f2852d147c2e.name = 'Alan Jay Lerner'
SET person_f2852d147c2e.gender = 'Male'
SET person_f2852d147c2e.country = 'US'
SET person_f2852d147c2e.discogs = 'https://www.discogs.com/artist/573746'
SET person_f2852d147c2e.imdb = 'https://www.imdb.com/name/nm0503585/'
SET person_f2852d147c2e.viaf = 'http://viaf.org/viaf/54336505'
SET person_f2852d147c2e.wikidata = 'https://www.wikidata.org/wiki/Q961893'
SET person_f2852d147c2e.databases = ['http://id.loc.gov/authorities/names/n50050417', 'https://adp.library.ucsb.edu/names/359390', 'https://catalogue.bnf.fr/ark:/12148/cb13937266x', 'https://d-nb.info/gnd/119042967', 'http://snaccooperative.org/ark:/99166/w6sf2wv5', 'https://nla.gov.au/nla.party-903408', 'https://openlibrary.org/works/OL579079A', 'https://www.ibdb.com/person.php?id=3945', 'https://www.worldcat.org/identities/lccn-n50050417']
SET person_f2852d147c2e.musicbrainz = 'https://musicbrainz.org/artist/56b7ad8e-3c4f-4f14-914d-f2852d147c2e'
SET person_f2852d147c2e.isni_list = ['http://isni.org/isni/0000000115708798']
SET person_f2852d147c2e.source = 'musicbrainz.org'
SET person_f2852d147c2e.timestamp = timestamp()

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
SET person_a37897b950ce.databases = ['http://id.loc.gov/authorities/names/n80017862', 'https://adp.library.ucsb.edu/names/102688', 'https://catalogue.bnf.fr/ark:/12148/cb13898618g', 'https://d-nb.info/gnd/11879292X', 'https://ibdb.com/person.php?id=12257', 'http://snaccooperative.org/ark:/99166/w6j38s5m', 'https://nla.gov.au/nla.party-949524', 'https://openlibrary.org/works/OL709416A', 'http://soundtrackcollector.com/composer/166/', 'https://rateyourmusic.com/artist/cole_porter', 'https://www.worldcat.org/identities/lccn-n80017862', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Cole&last=Porter&middle=']
SET person_a37897b950ce.musicbrainz = 'https://musicbrainz.org/artist/4a94a6cb-e70a-418b-bb53-a37897b950ce'
SET person_a37897b950ce.isni_list = ['http://isni.org/isni/0000000108653610']
SET person_a37897b950ce.source = 'musicbrainz.org'
SET person_a37897b950ce.timestamp = timestamp()

MERGE (person_70ea6e449256:Person{ uuid: '92523400-af50-4c0d-9785-70ea6e449256' }) 
SET person_70ea6e449256.name = 'Lars Färnlöf'
SET person_70ea6e449256.gender = 'Male'
SET person_70ea6e449256.country = 'SE'
SET person_70ea6e449256.discogs = 'https://www.discogs.com/artist/691514'
SET person_70ea6e449256.viaf = 'http://viaf.org/viaf/71336468'
SET person_70ea6e449256.wikidata = 'https://www.wikidata.org/wiki/Q5863146'
SET person_70ea6e449256.databases = ['http://id.loc.gov/authorities/names/nr2003031036', 'https://catalogue.bnf.fr/ark:/12148/cb166516406', 'https://rateyourmusic.com/artist/lars_farnlof', 'https://www.worldcat.org/identities/lccn-nr2003031036']
SET person_70ea6e449256.musicbrainz = 'https://musicbrainz.org/artist/92523400-af50-4c0d-9785-70ea6e449256'
SET person_70ea6e449256.isni_list = ['http://isni.org/isni/000000005339215X']
SET person_70ea6e449256.source = 'musicbrainz.org'
SET person_70ea6e449256.timestamp = timestamp()

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
SET person_8825529afd5d.databases = ['http://id.loc.gov/authorities/names/no89004670', 'https://adp.library.ucsb.edu/names/108757', 'https://catalogue.bnf.fr/ark:/12148/cb148427966', 'https://d-nb.info/gnd/102085412X', 'http://snaccooperative.org/ark:/99166/w6z61w7v', 'https://nla.gov.au/nla.party-887950', 'https://rateyourmusic.com/artist/johnny_burke_f1', 'https://www.ibdb.com/person.php?id=11462', 'https://www.worldcat.org/identities/lccn-no89004670/']
SET person_8825529afd5d.musicbrainz = 'https://musicbrainz.org/artist/c9b9ec99-b592-4556-aa0b-8825529afd5d'
SET person_8825529afd5d.isni_list = ['http://isni.org/isni/0000000071400010']
SET person_8825529afd5d.source = 'musicbrainz.org'
SET person_8825529afd5d.timestamp = timestamp()

MERGE (person_1904aa4268f4:Person{ uuid: '3fb75d97-5dfd-4e72-9aee-1904aa4268f4' }) 
SET person_1904aa4268f4.name = 'Lorenz Hart'
SET person_1904aa4268f4.gender = 'Male'
SET person_1904aa4268f4.country = 'US'
SET person_1904aa4268f4.allmusic = 'https://www.allmusic.com/artist/mn0000209620'
SET person_1904aa4268f4.discogs = 'https://www.discogs.com/artist/255800'
SET person_1904aa4268f4.imdb = 'https://www.imdb.com/name/nm0366414/'
SET person_1904aa4268f4.viaf = 'http://viaf.org/viaf/5122279'
SET person_1904aa4268f4.wikidata = 'https://www.wikidata.org/wiki/Q725828'
SET person_1904aa4268f4.databases = ['http://id.loc.gov/authorities/names/n81097890', 'https://adp.library.ucsb.edu/names/103285', 'https://catalogue.bnf.fr/ark:/12148/cb13939224g', 'https://d-nb.info/gnd/118720538', 'https://ibdb.com/Person/View/11244', 'http://snaccooperative.org/ark:/99166/w6x34z1s', 'https://nla.gov.au/nla.party-1266476', 'https://openlibrary.org/works/OL446542A', 'https://rateyourmusic.com/artist/lorenz_hart', 'https://www.worldcat.org/identities/lccn-n81097890/', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Lorenz&last=Hart&middle=']
SET person_1904aa4268f4.musicbrainz = 'https://musicbrainz.org/artist/3fb75d97-5dfd-4e72-9aee-1904aa4268f4'
SET person_1904aa4268f4.isni_list = ['http://isni.org/isni/0000000083526307']
SET person_1904aa4268f4.source = 'musicbrainz.org'
SET person_1904aa4268f4.timestamp = timestamp()

MERGE (person_403cf9a97220:Person{ uuid: '72037b48-1b88-457f-b5c7-403cf9a97220' }) 
SET person_403cf9a97220.name = 'Burton Lane'
SET person_403cf9a97220.gender = 'Male'
SET person_403cf9a97220.country = 'US'
SET person_403cf9a97220.discogs = 'https://www.discogs.com/artist/2560975'
SET person_403cf9a97220.discogs = 'https://www.discogs.com/artist/622065'
SET person_403cf9a97220.imdb = 'https://www.imdb.com/name/nm0485263/'
SET person_403cf9a97220.viaf = 'http://viaf.org/viaf/116566644'
SET person_403cf9a97220.wikidata = 'https://www.wikidata.org/wiki/Q364143'
SET person_403cf9a97220.databases = ['http://id.loc.gov/authorities/names/n84007674', 'https://adp.library.ucsb.edu/names/104446', 'https://catalogue.bnf.fr/ark:/12148/cb13937265k', 'https://d-nb.info/gnd/130216747', 'http://snaccooperative.org/ark:/99166/w6hq42c0', 'https://nla.gov.au/nla.party-1528597', 'https://openlibrary.org/works/OL2137045A', 'https://www.ibdb.com/person.php?id=12021', 'https://www.worldcat.org/identities/lccn-n84007674/']
SET person_403cf9a97220.musicbrainz = 'https://musicbrainz.org/artist/72037b48-1b88-457f-b5c7-403cf9a97220'
SET person_403cf9a97220.isni_list = ['http://isni.org/isni/0000000081854454']
SET person_403cf9a97220.source = 'musicbrainz.org'
SET person_403cf9a97220.timestamp = timestamp()

MERGE (person_acc0205f7513:Person{ uuid: '346448f5-25a0-4f78-bbd6-acc0205f7513' }) 
SET person_acc0205f7513.name = 'Richard Rodgers'
SET person_acc0205f7513.gender = 'Male'
SET person_acc0205f7513.disambiguation = 'composer'
SET person_acc0205f7513.country = 'US'
SET person_acc0205f7513.allmusic = 'https://www.allmusic.com/artist/mn0000820913'
SET person_acc0205f7513.bbc = 'https://www.bbc.co.uk/music/artists/346448f5-25a0-4f78-bbd6-acc0205f7513'
SET person_acc0205f7513.discogs = 'https://www.discogs.com/artist/255801'
SET person_acc0205f7513.imdb = 'https://www.imdb.com/name/nm0006256/'
SET person_acc0205f7513.viaf = 'http://viaf.org/viaf/113475079'
SET person_acc0205f7513.wikidata = 'https://www.wikidata.org/wiki/Q269094'
SET person_acc0205f7513.databases = ['http://id.loc.gov/authorities/names/n50048058', 'https://adp.library.ucsb.edu/names/102086', 'https://catalogue.bnf.fr/ark:/12148/cb13899099w', 'https://d-nb.info/gnd/118790862', 'https://ibdb.com/person.php?id=8323', 'http://snaccooperative.org/ark:/99166/w69h6cvt', 'https://nla.gov.au/nla.party-1015762', 'https://openlibrary.org/works/OL35365A', 'https://rateyourmusic.com/artist/richard_rodgers', 'https://www.worldcat.org/identities/lccn-n50048058/']
SET person_acc0205f7513.musicbrainz = 'https://musicbrainz.org/artist/346448f5-25a0-4f78-bbd6-acc0205f7513'
SET person_acc0205f7513.isni_list = ['http://isni.org/isni/0000000121482043']
SET person_acc0205f7513.source = 'musicbrainz.org'
SET person_acc0205f7513.timestamp = timestamp()

MERGE (person_68b293fe9b2e:Person{ uuid: '13dd9c7f-6d78-441c-9939-68b293fe9b2e' }) 
SET person_68b293fe9b2e.name = 'Gene Lees'
SET person_68b293fe9b2e.gender = 'Male'
SET person_68b293fe9b2e.country = 'CA'
SET person_68b293fe9b2e.discogs = 'https://www.discogs.com/artist/566918'
SET person_68b293fe9b2e.imdb = 'https://www.imdb.com/name/nm0498724/'
SET person_68b293fe9b2e.viaf = 'http://viaf.org/viaf/49886486'
SET person_68b293fe9b2e.wikidata = 'https://www.wikidata.org/wiki/Q453388'
SET person_68b293fe9b2e.databases = ['http://id.loc.gov/authorities/names/n81027835', 'https://catalogue.bnf.fr/ark:/12148/cb13770167s', 'https://d-nb.info/gnd/1089827008', 'http://snaccooperative.org/ark:/99166/w6b57gfx', 'https://nla.gov.au/nla.party-1234164', 'https://www.worldcat.org/identities/lccn-n81027835']
SET person_68b293fe9b2e.musicbrainz = 'https://musicbrainz.org/artist/13dd9c7f-6d78-441c-9939-68b293fe9b2e'
SET person_68b293fe9b2e.isni_list = ['http://isni.org/isni/0000000116393484']
SET person_68b293fe9b2e.source = 'musicbrainz.org'
SET person_68b293fe9b2e.timestamp = timestamp()

MERGE (work_3ffa436aeecf:Work{ uuid: 'b841d91d-70d9-4b8b-8cfc-3ffa436aeecf' })
SET work_3ffa436aeecf.name = 'Grandfather’s Waltz'
SET work_3ffa436aeecf.iswc = 'T-000.184.900-8'
SET work_3ffa436aeecf.type = 'Song'
SET work_3ffa436aeecf.source = 'musicbrainz.org'
SET work_3ffa436aeecf.timestamp = timestamp()

MERGE (work_18bdc7c469f0:Work{ uuid: '5c66c8da-85bb-3ecb-8f3f-18bdc7c469f0' })
SET work_18bdc7c469f0.name = 'Night and Day'
SET work_18bdc7c469f0.iswc = 'T-070.152.461-9'
SET work_18bdc7c469f0.type = 'Song'
SET work_18bdc7c469f0.wikidata = 'https://www.wikidata.org/wiki/Q1477068'
SET work_18bdc7c469f0.musicbrainz = 'https://musicbrainz.org/work/5c66c8da-85bb-3ecb-8f3f-18bdc7c469f0'
SET work_18bdc7c469f0.source = 'musicbrainz.org'
SET work_18bdc7c469f0.timestamp = timestamp()

MERGE (work_2d4413756389:Work{ uuid: 'a9aeb803-1185-3f59-98b0-2d4413756389' })
SET work_2d4413756389.name = 'My Heart Stood Still'
SET work_2d4413756389.iswc = 'T-070.110.973-0'
SET work_2d4413756389.type = 'Song'
SET work_2d4413756389.wikidata = 'https://www.wikidata.org/wiki/Q16387196'
SET work_2d4413756389.musicbrainz = 'https://musicbrainz.org/work/a9aeb803-1185-3f59-98b0-2d4413756389'
SET work_2d4413756389.source = 'musicbrainz.org'
SET work_2d4413756389.timestamp = timestamp()

MERGE (work_c5547c35c7f0:Work{ uuid: '8ad0746a-c922-4353-a8cf-c5547c35c7f0' })
SET work_c5547c35c7f0.name = 'Funkallero'
SET work_c5547c35c7f0.type = 'Song'
SET work_c5547c35c7f0.source = 'musicbrainz.org'
SET work_c5547c35c7f0.timestamp = timestamp()

MERGE (work_2938a219ebf9:Work{ uuid: '10f9d66d-700a-3267-9551-2938a219ebf9' })
SET work_2938a219ebf9.name = 'But Beautiful'
SET work_2938a219ebf9.iswc = 'T-070.012.870-6'
SET work_2938a219ebf9.type = 'Song'
SET work_2938a219ebf9.wikidata = 'https://www.wikidata.org/wiki/Q5002309'
SET work_2938a219ebf9.musicbrainz = 'https://musicbrainz.org/work/10f9d66d-700a-3267-9551-2938a219ebf9'
SET work_2938a219ebf9.source = 'musicbrainz.org'
SET work_2938a219ebf9.timestamp = timestamp()

MERGE (work_eddb9a6794f6:Work{ uuid: 'f7b0eeea-4fd5-3dcf-886b-eddb9a6794f6' })
SET work_eddb9a6794f6.name = 'Melinda'
SET work_eddb9a6794f6.iswc = 'T-070.112.147-2'
SET work_eddb9a6794f6.type = 'Song'
SET work_eddb9a6794f6.musicbrainz = 'https://musicbrainz.org/work/f7b0eeea-4fd5-3dcf-886b-eddb9a6794f6'
SET work_eddb9a6794f6.source = 'musicbrainz.org'
SET work_eddb9a6794f6.timestamp = timestamp()


// performances of
MERGE (perf_a7752d73af38)-[:PERFORMANCE_OF]->(work_3ffa436aeecf)
MERGE (perf_414af61aa29f)-[:PERFORMANCE_OF]->(work_18bdc7c469f0)
MERGE (perf_10ca9224f107)-[:PERFORMANCE_OF]->(work_2d4413756389)
MERGE (perf_229954f7d189)-[:PERFORMANCE_OF]->(work_c5547c35c7f0)
MERGE (perf_5e8fae86fb4f)-[:PERFORMANCE_OF]->(work_2938a219ebf9)
MERGE (perf_e67b21f1ebe1)-[:PERFORMANCE_OF]->(work_eddb9a6794f6)


// composers
MERGE (person_70ea6e449256)-[:COMPOSED]->(work_3ffa436aeecf)
MERGE (person_68b293fe9b2e)-[:WROTE_LYRICS]->(work_3ffa436aeecf)
MERGE (person_a37897b950ce)-[:COMPOSED]->(work_18bdc7c469f0)
MERGE (person_a37897b950ce)-[:WROTE_LYRICS]->(work_18bdc7c469f0)
MERGE (person_acc0205f7513)-[:COMPOSED]->(work_2d4413756389)
MERGE (person_1904aa4268f4)-[:WROTE_LYRICS]->(work_2d4413756389)
MERGE (person_6c57b03a4e36)-[:COMPOSED]->(work_c5547c35c7f0)
MERGE (person_a6d92136636f)-[:COMPOSED]->(work_2938a219ebf9)
MERGE (person_8825529afd5d)-[:WROTE_LYRICS]->(work_2938a219ebf9)
MERGE (person_403cf9a97220)-[:COMPOSED]->(work_eddb9a6794f6)
MERGE (person_f2852d147c2e)-[:WROTE_LYRICS]->(work_eddb9a6794f6)


// place nodes

MERGE (place_569fa8b97644:Place{ uuid: '1165ef7d-371c-4e03-98db-569fa8b97644' })
SET place_569fa8b97644.name = 'Van Gelder Studio'
SET place_569fa8b97644.source = 'musicbrainz.org'


// place relationships
MERGE (perf_414af61aa29f)-[:HAS_PLACE { type: 'recorded at', begin: '1964-05-06', end: '1964-05-06' }]->(place_569fa8b97644)
MERGE (perf_5e8fae86fb4f)-[:HAS_PLACE { type: 'recorded at', begin: '1964-05-06', end: '1964-05-06' }]->(place_569fa8b97644)
MERGE (perf_229954f7d189)-[:HAS_PLACE { type: 'recorded at', begin: '1964-05-06', end: '1964-05-06' }]->(place_569fa8b97644)
MERGE (perf_10ca9224f107)-[:HAS_PLACE { type: 'recorded at', begin: '1964-05-05', end: '1964-05-05' }]->(place_569fa8b97644)
MERGE (perf_e67b21f1ebe1)-[:HAS_PLACE { type: 'recorded at', begin: '1964-05-05', end: '1964-05-05' }]->(place_569fa8b97644)
MERGE (perf_a7752d73af38)-[:HAS_PLACE { type: 'recorded at', begin: '1964-05-05', end: '1964-05-05' }]->(place_569fa8b97644)

MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_414af61aa29f)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_414af61aa29f)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_414af61aa29f)
MERGE (person_bed4063208e7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_414af61aa29f)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_414af61aa29f)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_5e8fae86fb4f)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5e8fae86fb4f)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_5e8fae86fb4f)
MERGE (person_bed4063208e7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_5e8fae86fb4f)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_5e8fae86fb4f)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_229954f7d189)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_229954f7d189)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_229954f7d189)
MERGE (person_bed4063208e7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_229954f7d189)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_229954f7d189)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_10ca9224f107)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_10ca9224f107)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_10ca9224f107)
MERGE (person_bed4063208e7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_10ca9224f107)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_10ca9224f107)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e67b21f1ebe1)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e67b21f1ebe1)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_e67b21f1ebe1)
MERGE (person_bed4063208e7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e67b21f1ebe1)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e67b21f1ebe1)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_a7752d73af38)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a7752d73af38)
MERGE (person_afe9622fab32)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_a7752d73af38)
MERGE (person_bed4063208e7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a7752d73af38)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_a7752d73af38)

