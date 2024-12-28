
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_2340918a2080:Release{ uuid: 'ef1418a4-30a2-3add-bc38-2340918a2080' })
SET release_2340918a2080.name = 'Far Cry'
SET release_2340918a2080.country = 'JP'
SET release_2340918a2080.date = '1999-11-20'
SET release_2340918a2080.format = 'CD'
SET release_2340918a2080.discode = 'VICJ-60430'
SET release_2340918a2080.musicbrainz = 'http://musicbrainz.org/release/ef1418a4-30a2-3add-bc38-2340918a2080'
SET release_2340918a2080.source = 'musicbrainz.org'


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


MERGE (person_272833ecca94:Person{ uuid: 'f2008882-e914-4c8a-a3fe-272833ecca94' }) 
SET person_272833ecca94.name = 'Booker Little'
SET person_272833ecca94.gender = 'Male'
SET person_272833ecca94.country = 'US'
SET person_272833ecca94.discogs = 'https://www.discogs.com/artist/271897'
SET person_272833ecca94.viaf = 'http://viaf.org/viaf/196902'
SET person_272833ecca94.wikidata = 'https://www.wikidata.org/wiki/Q892997'
SET person_272833ecca94.wikipedia = 'https://en.wikipedia.org/wiki/Booker_Little'
SET person_272833ecca94.databases = ['http://d-nb.info/gnd/134592662', 'http://id.loc.gov/authorities/names/n92016496', 'https://catalogue.bnf.fr/ark:/12148/cb138967006', 'http://snaccooperative.org/ark:/99166/w6kt4nq5', 'https://www.worldcat.org/identities/lccn-n92016496']
SET person_272833ecca94.musicbrainz = 'https://musicbrainz.org/artist/f2008882-e914-4c8a-a3fe-272833ecca94'
SET person_272833ecca94.isni_list = ['http://isni.org/isni/0000000055129670']
SET person_272833ecca94.source = 'musicbrainz.org'


MERGE (person_07467bdf0f71:Person{ uuid: 'badda5cf-f2c5-4dc2-b3d3-07467bdf0f71' }) 
SET person_07467bdf0f71.name = 'Eric Dolphy'
SET person_07467bdf0f71.gender = 'Male'
SET person_07467bdf0f71.country = 'US'
SET person_07467bdf0f71.allmusic = 'https://www.allmusic.com/artist/mn0000800100'
SET person_07467bdf0f71.bbc = 'https://www.bbc.co.uk/music/artists/badda5cf-f2c5-4dc2-b3d3-07467bdf0f71'
SET person_07467bdf0f71.discogs = 'https://www.discogs.com/artist/145272'
SET person_07467bdf0f71.imdb = 'https://www.imdb.com/name/nm0231238/'
SET person_07467bdf0f71.viaf = 'http://viaf.org/viaf/66651545'
SET person_07467bdf0f71.wikidata = 'https://www.wikidata.org/wiki/Q367508'
SET person_07467bdf0f71.databases = ['http://d-nb.info/gnd/118812866', 'http://id.loc.gov/authorities/names/n81035956', 'https://catalogue.bnf.fr/ark:/12148/cb13893337q', 'http://snaccooperative.org/ark:/99166/w6s18p3z', 'https://nla.gov.au/nla.party-910562', 'https://rateyourmusic.com/artist/eric_dolphy', 'https://www.worldcat.org/identities/lccn-n81035956']
SET person_07467bdf0f71.musicbrainz = 'https://musicbrainz.org/artist/badda5cf-f2c5-4dc2-b3d3-07467bdf0f71'
SET person_07467bdf0f71.isni_list = ['http://isni.org/isni/000000008146531X']
SET person_07467bdf0f71.source = 'musicbrainz.org'


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
SET person_e044666c4828.databases = ['http://d-nb.info/gnd/134344332', 'http://id.loc.gov/authorities/names/n81014576', 'https://catalogue.bnf.fr/ark:/12148/cb138922167', 'http://snaccooperative.org/ark:/99166/w67m16sc', 'https://rateyourmusic.com/artist/ron_carter', 'https://www.worldcat.org/identities/lccn-n81014576']
SET person_e044666c4828.musicbrainz = 'https://musicbrainz.org/artist/57db3f59-9c58-4f68-a00e-e044666c4828'
SET person_e044666c4828.isni_list = ['http://isni.org/isni/0000000114394862']
SET person_e044666c4828.source = 'musicbrainz.org'


MERGE (person_05d508e09a73:Person{ uuid: 'f0707f1d-55e1-46b6-8a9c-05d508e09a73' }) 
SET person_05d508e09a73.name = 'Rudy van Gelder'
SET person_05d508e09a73.gender = 'Male'
SET person_05d508e09a73.country = 'US'
SET person_05d508e09a73.allmusic = 'https://www.allmusic.com/artist/mn0000305301'
SET person_05d508e09a73.discogs = 'https://www.discogs.com/artist/252966'
SET person_05d508e09a73.viaf = 'http://viaf.org/viaf/33997197'
SET person_05d508e09a73.wikidata = 'https://www.wikidata.org/wiki/Q945681'
SET person_05d508e09a73.databases = ['http://d-nb.info/gnd/133648508', 'http://id.loc.gov/authorities/names/no00020144', 'https://rateyourmusic.com/artist/rudy_van_gelder', 'https://www.worldcat.org/identities/lccn-no00020144']
SET person_05d508e09a73.musicbrainz = 'https://musicbrainz.org/artist/f0707f1d-55e1-46b6-8a9c-05d508e09a73'
SET person_05d508e09a73.isni_list = ['http://isni.org/isni/0000000019691076']
SET person_05d508e09a73.source = 'musicbrainz.org'


MERGE (person_84a8b7f41799:Person{ uuid: '3f627e4e-4d29-45f0-8dd0-84a8b7f41799' }) 
SET person_84a8b7f41799.name = 'Jaki Byard'
SET person_84a8b7f41799.gender = 'Male'
SET person_84a8b7f41799.country = 'US'
SET person_84a8b7f41799.allmusic = 'https://www.allmusic.com/artist/mn0000112535'
SET person_84a8b7f41799.discogs = 'https://www.discogs.com/artist/252610'
SET person_84a8b7f41799.viaf = 'http://viaf.org/viaf/61731187'
SET person_84a8b7f41799.wikidata = 'https://www.wikidata.org/wiki/Q1346401'
SET person_84a8b7f41799.databases = ['http://d-nb.info/gnd/134582888', 'http://id.loc.gov/authorities/names/n78048954', 'https://catalogue.bnf.fr/ark:/12148/cb138920338', 'http://snaccooperative.org/ark:/99166/w6pg2qp8', 'https://www.worldcat.org/identities/lccn-n78048954']
SET person_84a8b7f41799.musicbrainz = 'https://musicbrainz.org/artist/3f627e4e-4d29-45f0-8dd0-84a8b7f41799'
SET person_84a8b7f41799.isni_list = ['http://isni.org/isni/0000000096156501']
SET person_84a8b7f41799.source = 'musicbrainz.org'

// labels

MERGE (label_d510b586b396:Label{ uuid: '3690758a-3ec1-4fd3-a250-d510b586b396' })
SET label_d510b586b396.name= 'New Jazz'

// performances

MERGE (perf_13599bc2b2e3:Performance{ uuid: 'f2e3397a-53f7-4c46-ac30-13599bc2b2e3' })
SET perf_13599bc2b2e3.name = 'Mrs. Parker of K.C. (Bird’s Mother)'
SET perf_13599bc2b2e3.duration = '8:03'
SET perf_13599bc2b2e3.begin_date = '1960-12-21'
SET perf_13599bc2b2e3.end_date = '1960-12-21'
SET perf_13599bc2b2e3.source = 'musicbrainz.org'


MERGE (perf_0254bc871a82:Performance{ uuid: '3c0379bd-cc7f-4212-b30b-0254bc871a82' })
SET perf_0254bc871a82.name = 'Ode to Charlie Parker'
SET perf_0254bc871a82.duration = '8:44'
SET perf_0254bc871a82.begin_date = '1960-12-21'
SET perf_0254bc871a82.end_date = '1960-12-21'
SET perf_0254bc871a82.source = 'musicbrainz.org'


MERGE (perf_67398f5cc444:Performance{ uuid: 'c2f8fb3e-aa0b-4934-8a30-67398f5cc444' })
SET perf_67398f5cc444.name = 'Far Cry'
SET perf_67398f5cc444.duration = '3:55'
SET perf_67398f5cc444.begin_date = '1960-12-21'
SET perf_67398f5cc444.end_date = '1960-12-21'
SET perf_67398f5cc444.source = 'musicbrainz.org'


MERGE (perf_9c6d496ca697:Performance{ uuid: 'ac028929-2c52-45f5-aff9-9c6d496ca697' })
SET perf_9c6d496ca697.name = 'Miss Ann'
SET perf_9c6d496ca697.duration = '4:17'
SET perf_9c6d496ca697.begin_date = '1960-12-21'
SET perf_9c6d496ca697.end_date = '1960-12-21'
SET perf_9c6d496ca697.source = 'musicbrainz.org'


MERGE (perf_70cff758d1aa:Performance{ uuid: 'e7ec3a5e-2c45-4d28-8427-70cff758d1aa' })
SET perf_70cff758d1aa.name = 'Left Alone'
SET perf_70cff758d1aa.duration = '6:41'
SET perf_70cff758d1aa.begin_date = '1960-12-21'
SET perf_70cff758d1aa.end_date = '1960-12-21'
SET perf_70cff758d1aa.source = 'musicbrainz.org'


MERGE (perf_8a94e8d512b0:Performance{ uuid: 'b4ef1a07-fb71-439e-9403-8a94e8d512b0' })
SET perf_8a94e8d512b0.name = 'Tenderly'
SET perf_8a94e8d512b0.duration = '4:20'
SET perf_8a94e8d512b0.begin_date = '1960-12-21'
SET perf_8a94e8d512b0.end_date = '1960-12-21'
SET perf_8a94e8d512b0.source = 'musicbrainz.org'


MERGE (perf_2d42fbefd2d4:Performance{ uuid: '11f4444d-a5cd-4d5e-acb1-2d42fbefd2d4' })
SET perf_2d42fbefd2d4.name = 'It\\'s Magic'
SET perf_2d42fbefd2d4.duration = '5:41'
SET perf_2d42fbefd2d4.source = 'musicbrainz.org'


MERGE (perf_ea8ac99d1f55:Performance{ uuid: 'c5fe6652-a2e5-45ad-9c48-ea8ac99d1f55' })
SET perf_ea8ac99d1f55.name = 'Serene'
SET perf_ea8ac99d1f55.duration = '6:37'
SET perf_ea8ac99d1f55.source = 'musicbrainz.org'




// labels
MERGE (release_2340918a2080)-[:HAS_LABEL]->(label_d510b586b396)


// tracks
MERGE (release_2340918a2080)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_13599bc2b2e3)
MERGE (release_2340918a2080)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_0254bc871a82)
MERGE (release_2340918a2080)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_67398f5cc444)
MERGE (release_2340918a2080)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_9c6d496ca697)
MERGE (release_2340918a2080)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_70cff758d1aa)
MERGE (release_2340918a2080)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_8a94e8d512b0)
MERGE (release_2340918a2080)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_2d42fbefd2d4)
MERGE (release_2340918a2080)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_ea8ac99d1f55)

// works

MERGE (person_3c1adc1846c5:Person{ uuid: 'b306fa03-712b-42c8-b866-3c1adc1846c5' }) 
SET person_3c1adc1846c5.name = 'Jack Lawrence'
SET person_3c1adc1846c5.gender = 'Male'
SET person_3c1adc1846c5.disambiguation = 'US songwriter'
SET person_3c1adc1846c5.country = 'US'
SET person_3c1adc1846c5.allmusic = 'https://www.allmusic.com/artist/mn0000101087'
SET person_3c1adc1846c5.discogs = 'https://www.discogs.com/artist/638169'
SET person_3c1adc1846c5.imdb = 'https://www.imdb.com/name/nm0492805/'
SET person_3c1adc1846c5.viaf = 'http://viaf.org/viaf/118975192'
SET person_3c1adc1846c5.wikidata = 'https://www.wikidata.org/wiki/Q2452637'
SET person_3c1adc1846c5.databases = ['https://ibdb.com/person.php?id=12029', 'https://rateyourmusic.com/artist/jack_lawrence']
SET person_3c1adc1846c5.musicbrainz = 'https://musicbrainz.org/artist/b306fa03-712b-42c8-b866-3c1adc1846c5'
SET person_3c1adc1846c5.isni_list = ['http://isni.org/isni/000000010939311X']
SET person_3c1adc1846c5.source = 'musicbrainz.org'


MERGE (person_ede5033bc6f7:Person{ uuid: '3f658e7f-4f44-4493-942c-ede5033bc6f7' }) 
SET person_ede5033bc6f7.name = 'Mal Waldron'
SET person_ede5033bc6f7.gender = 'Male'
SET person_ede5033bc6f7.disambiguation = 'American jazz pianist'
SET person_ede5033bc6f7.country = 'US'
SET person_ede5033bc6f7.allmusic = 'https://www.allmusic.com/artist/mn0000665824'
SET person_ede5033bc6f7.discogs = 'https://www.discogs.com/artist/260727'
SET person_ede5033bc6f7.imdb = 'https://www.imdb.com/name/nm0907310/'
SET person_ede5033bc6f7.viaf = 'http://viaf.org/viaf/49409732'
SET person_ede5033bc6f7.wikidata = 'https://www.wikidata.org/wiki/Q955767'
SET person_ede5033bc6f7.databases = ['http://d-nb.info/gnd/124273513', 'http://id.loc.gov/authorities/names/n83147700', 'https://catalogue.bnf.fr/ark:/12148/cb13900958x', 'http://snaccooperative.org/ark:/99166/w6gn13r6', 'https://www.worldcat.org/identities/lccn-n83147700']
SET person_ede5033bc6f7.musicbrainz = 'https://musicbrainz.org/artist/3f658e7f-4f44-4493-942c-ede5033bc6f7'
SET person_ede5033bc6f7.isni_list = ['http://isni.org/isni/0000000081281326']
SET person_ede5033bc6f7.source = 'musicbrainz.org'


MERGE (person_b557ee602aed:Person{ uuid: 'd59c4cda-11d9-48db-8bfe-b557ee602aed' }) 
SET person_b557ee602aed.name = 'Billie Holiday'
SET person_b557ee602aed.gender = 'Female'
SET person_b557ee602aed.country = 'US'
SET person_b557ee602aed.allmusic = 'https://www.allmusic.com/artist/mn0000079016'
SET person_b557ee602aed.bbc = 'https://www.bbc.co.uk/music/artists/d59c4cda-11d9-48db-8bfe-b557ee602aed'
SET person_b557ee602aed.discogs = 'https://www.discogs.com/artist/33589'
SET person_b557ee602aed.imdb = 'https://www.imdb.com/name/nm0390507/'
SET person_b557ee602aed.viaf = 'http://viaf.org/viaf/14857262'
SET person_b557ee602aed.wikidata = 'https://www.wikidata.org/wiki/Q104358'
SET person_b557ee602aed.databases = ['http://d-nb.info/gnd/118706454', 'http://id.loc.gov/authorities/names/n50033023', 'https://catalogue.bnf.fr/ark:/12148/cb12402944q', 'https://ibdb.com/person.php?id=45383', 'http://snaccooperative.org/ark:/99166/w6n87bns', 'https://nla.gov.au/nla.party-862795', 'https://openlibrary.org/works/OL1349619A', 'https://rateyourmusic.com/artist/billie_holiday', 'https://www.musik-sammler.de/artist/billie-holiday/', 'https://www.worldcat.org/identities/lccn-n50033023']
SET person_b557ee602aed.musicbrainz = 'https://musicbrainz.org/artist/d59c4cda-11d9-48db-8bfe-b557ee602aed'
SET person_b557ee602aed.isni_list = ['http://isni.org/isni/0000000110215599', 'http://isni.org/isni/0000000368571283']
SET person_b557ee602aed.source = 'musicbrainz.org'


MERGE (person_be361b3d02e0:Person{ uuid: 'a88b4657-2c3b-4d0f-b95f-be361b3d02e0' }) 
SET person_be361b3d02e0.name = 'Walter Gross'
SET person_be361b3d02e0.gender = 'Male'
SET person_be361b3d02e0.disambiguation = 'American composer'
SET person_be361b3d02e0.country = 'US'
SET person_be361b3d02e0.allmusic = 'https://www.allmusic.com/artist/mn0000228862'
SET person_be361b3d02e0.discogs = 'https://www.discogs.com/artist/277973'
SET person_be361b3d02e0.imdb = 'https://www.imdb.com/name/nm1056630/'
SET person_be361b3d02e0.viaf = 'http://viaf.org/viaf/63215378'
SET person_be361b3d02e0.wikidata = 'https://www.wikidata.org/wiki/Q746609'
SET person_be361b3d02e0.databases = ['http://d-nb.info/gnd/1102712523', 'http://id.loc.gov/authorities/names/n93017864', 'https://catalogue.bnf.fr/ark:/12148/cb13797506s', 'http://snaccooperative.org/ark:/99166/w6rr1wmf', 'https://www.worldcat.org/identities/lccn-n93017864']
SET person_be361b3d02e0.musicbrainz = 'https://musicbrainz.org/artist/a88b4657-2c3b-4d0f-b95f-be361b3d02e0'
SET person_be361b3d02e0.isni_list = ['http://isni.org/isni/0000000114460647']
SET person_be361b3d02e0.source = 'musicbrainz.org'


MERGE (work_b4b21205b478:Work{ uuid: 'bd937925-7381-37e7-8308-b4b21205b478' })
SET work_b4b21205b478.name = 'Tenderly'
SET work_b4b21205b478.iswc = 'T-070.178.445-3'
SET work_b4b21205b478.type = 'Song'
SET work_b4b21205b478.wikidata = 'https://www.wikidata.org/wiki/Q615638'
SET work_b4b21205b478.musicbrainz = 'https://musicbrainz.org/work/bd937925-7381-37e7-8308-b4b21205b478'
SET work_b4b21205b478.source = 'musicbrainz.org'


MERGE (work_64314511a19b:Work{ uuid: '76627a89-2bbd-3165-9e40-64314511a19b' })
SET work_64314511a19b.name = 'Sorino (a.k.a. Serene)'
SET work_64314511a19b.iswc = 'T-700.061.616-2'
SET work_64314511a19b.type = 'Song'
SET work_64314511a19b.source = 'musicbrainz.org'


MERGE (work_2da36d12171a:Work{ uuid: 'a6f10e30-15e6-4d4b-996a-2da36d12171a' })
SET work_2da36d12171a.name = 'Far Cry'
SET work_2da36d12171a.iswc = 'T-070.253.997-6'
SET work_2da36d12171a.type = 'Song'
SET work_2da36d12171a.source = 'musicbrainz.org'


MERGE (work_05fc95e6f206:Work{ uuid: '213c59b7-5811-478d-8f3b-05fc95e6f206' })
SET work_05fc95e6f206.name = 'Miss Ann'
SET work_05fc95e6f206.type = 'Song'
SET work_05fc95e6f206.source = 'musicbrainz.org'


MERGE (work_6222dd8bd809:Work{ uuid: 'f69cd696-f945-421a-989e-6222dd8bd809' })
SET work_6222dd8bd809.name = 'Ode to Charlie Parker'
SET work_6222dd8bd809.iswc = 'T-700.049.642-6'
SET work_6222dd8bd809.type = 'Song'
SET work_6222dd8bd809.source = 'musicbrainz.org'


MERGE (work_82871701ac8e:Work{ uuid: 'fea26742-143f-4913-8882-82871701ac8e' })
SET work_82871701ac8e.name = 'Mrs. Parker of K.C. (Bird\\'s Mother)'
SET work_82871701ac8e.iswc = 'T-070.230.302-3'
SET work_82871701ac8e.type = 'Song'
SET work_82871701ac8e.source = 'musicbrainz.org'


MERGE (work_d5e9796f881c:Work{ uuid: '68b1f07d-562d-30c5-9f7c-d5e9796f881c' })
SET work_d5e9796f881c.name = 'Left Alone'
SET work_d5e9796f881c.type = 'Song'
SET work_d5e9796f881c.wikipedia = 'https://en.wikipedia.org/wiki/Left_Alone_(song)'
SET work_d5e9796f881c.musicbrainz = 'https://musicbrainz.org/work/68b1f07d-562d-30c5-9f7c-d5e9796f881c'
SET work_d5e9796f881c.source = 'musicbrainz.org'



// performances of
MERGE (perf_8a94e8d512b0)-[:PERFORMANCE_OF]->(work_b4b21205b478)
MERGE (perf_ea8ac99d1f55)-[:PERFORMANCE_OF]->(work_64314511a19b)
MERGE (perf_67398f5cc444)-[:PERFORMANCE_OF]->(work_2da36d12171a)
MERGE (perf_9c6d496ca697)-[:PERFORMANCE_OF]->(work_05fc95e6f206)
MERGE (perf_0254bc871a82)-[:PERFORMANCE_OF]->(work_6222dd8bd809)
MERGE (perf_13599bc2b2e3)-[:PERFORMANCE_OF]->(work_82871701ac8e)
MERGE (perf_70cff758d1aa)-[:PERFORMANCE_OF]->(work_d5e9796f881c)


// composers
MERGE (person_be361b3d02e0)-[:COMPOSED]->(work_b4b21205b478)
MERGE (person_3c1adc1846c5)-[:WROTE_LYRICS]->(work_b4b21205b478)
MERGE (person_07467bdf0f71)-[:COMPOSED]->(work_64314511a19b)
MERGE (person_07467bdf0f71)-[:COMPOSED]->(work_2da36d12171a)
MERGE (person_07467bdf0f71)-[:COMPOSED]->(work_05fc95e6f206)
MERGE (person_84a8b7f41799)-[:COMPOSED]->(work_6222dd8bd809)
MERGE (person_84a8b7f41799)-[:COMPOSED]->(work_82871701ac8e)
MERGE (person_ede5033bc6f7)-[:COMPOSED]->(work_d5e9796f881c)
MERGE (person_b557ee602aed)-[:WROTE_LYRICS]->(work_d5e9796f881c)


// place nodes

MERGE (place_569fa8b97644:Place{ uuid: '1165ef7d-371c-4e03-98db-569fa8b97644' })
SET place_569fa8b97644.name = 'Van Gelder Studio'
SET place_569fa8b97644.source = 'musicbrainz.org'


// place relationships
MERGE (perf_13599bc2b2e3)-[:HAS_PLACE { type: 'recorded at', begin_date: '1960-12-21', end_date: '1960-12-21' }]->(place_569fa8b97644)
MERGE (perf_0254bc871a82)-[:HAS_PLACE { type: 'recorded at', begin_date: '1960-12-21', end_date: '1960-12-21' }]->(place_569fa8b97644)
MERGE (perf_67398f5cc444)-[:HAS_PLACE { type: 'recorded at', begin_date: '1960-12-21', end_date: '1960-12-21' }]->(place_569fa8b97644)
MERGE (perf_9c6d496ca697)-[:HAS_PLACE { type: 'recorded at', begin_date: '1960-12-21', end_date: '1960-12-21' }]->(place_569fa8b97644)
MERGE (perf_70cff758d1aa)-[:HAS_PLACE { type: 'recorded at', begin_date: '1960-12-21', end_date: '1960-12-21' }]->(place_569fa8b97644)
MERGE (perf_8a94e8d512b0)-[:HAS_PLACE { type: 'recorded at', begin_date: '1960-12-21', end_date: '1960-12-21' }]->(place_569fa8b97644)

MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_13599bc2b2e3)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_13599bc2b2e3)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass clarinet'] }]->(perf_13599bc2b2e3)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_13599bc2b2e3)
MERGE (person_272833ecca94)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_13599bc2b2e3)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_13599bc2b2e3)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_0254bc871a82)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_0254bc871a82)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute'] }]->(perf_0254bc871a82)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_0254bc871a82)
MERGE (person_272833ecca94)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_0254bc871a82)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_0254bc871a82)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_67398f5cc444)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_67398f5cc444)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_67398f5cc444)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_67398f5cc444)
MERGE (person_272833ecca94)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_67398f5cc444)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_67398f5cc444)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_9c6d496ca697)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_9c6d496ca697)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_9c6d496ca697)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9c6d496ca697)
MERGE (person_272833ecca94)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_9c6d496ca697)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_9c6d496ca697)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_70cff758d1aa)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_70cff758d1aa)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute'] }]->(perf_70cff758d1aa)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_70cff758d1aa)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_70cff758d1aa)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_8a94e8d512b0)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_8a94e8d512b0)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2d42fbefd2d4)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_2d42fbefd2d4)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'bass clarinet'] }]->(perf_2d42fbefd2d4)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_2d42fbefd2d4)
MERGE (person_272833ecca94)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_2d42fbefd2d4)
MERGE (person_84a8b7f41799)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ea8ac99d1f55)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_ea8ac99d1f55)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'bass clarinet'] }]->(perf_ea8ac99d1f55)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_ea8ac99d1f55)
MERGE (person_272833ecca94)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_ea8ac99d1f55)



"""
)