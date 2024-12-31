
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_5365210722a1:Release{ uuid: '4c3f687b-dffc-4bdd-bb69-5365210722a1' })
SET release_5365210722a1.name = 'PanaMonk'
SET release_5365210722a1.country = 'US'
SET release_5365210722a1.date = '1996-05-21'
SET release_5365210722a1.format = 'CD'
SET release_5365210722a1.discode = 'IMPD190'
SET release_5365210722a1.discogs = 'https://www.discogs.com/release/1653611'
SET release_5365210722a1.musicbrainz = 'http://musicbrainz.org/release/4c3f687b-dffc-4bdd-bb69-5365210722a1'
SET release_5365210722a1.source = 'musicbrainz.org'


MERGE (person_2fb64f98a555:Person{ uuid: '166e748d-7d6a-4d7f-a6f7-2fb64f98a555' }) 
SET person_2fb64f98a555.name = 'Chris Albert'
SET person_2fb64f98a555.gender = 'Male'
SET person_2fb64f98a555.disambiguation = 'US engineer'
SET person_2fb64f98a555.country = 'US'
SET person_2fb64f98a555.discogs = 'https://www.discogs.com/artist/222823'
SET person_2fb64f98a555.databases = ['https://rateyourmusic.com/artist/chris_albert']
SET person_2fb64f98a555.musicbrainz = 'https://musicbrainz.org/artist/166e748d-7d6a-4d7f-a6f7-2fb64f98a555'
SET person_2fb64f98a555.source = 'musicbrainz.org'


MERGE (person_bfc85160b95e:Person{ uuid: 'f7b9e2b0-19d6-45f7-852e-bfc85160b95e' }) 
SET person_bfc85160b95e.name = 'Mike Krowiak'
SET person_bfc85160b95e.gender = 'Male'
SET person_bfc85160b95e.country = 'US'
SET person_bfc85160b95e.discogs = 'https://www.discogs.com/artist/303328'
SET person_bfc85160b95e.musicbrainz = 'https://musicbrainz.org/artist/f7b9e2b0-19d6-45f7-852e-bfc85160b95e'
SET person_bfc85160b95e.source = 'musicbrainz.org'


MERGE (person_ebf20ee45f41:Person{ uuid: '8d0e541a-78a2-445f-a2e6-ebf20ee45f41' }) 
SET person_ebf20ee45f41.name = 'Danilo Pérez'
SET person_ebf20ee45f41.gender = 'Male'
SET person_ebf20ee45f41.country = 'PA'
SET person_ebf20ee45f41.allmusic = 'https://www.allmusic.com/artist/mn0000670875'
SET person_ebf20ee45f41.discogs = 'https://www.discogs.com/artist/59752'
SET person_ebf20ee45f41.viaf = 'http://viaf.org/viaf/74041553'
SET person_ebf20ee45f41.wikidata = 'https://www.wikidata.org/wiki/Q1164102'
SET person_ebf20ee45f41.databases = ['http://id.loc.gov/authorities/names/no92038063', 'https://catalogue.bnf.fr/ark:/12148/cb139395009', 'https://d-nb.info/gnd/134797000', 'https://www.worldcat.org/identities/lccn-no92038063']
SET person_ebf20ee45f41.musicbrainz = 'https://musicbrainz.org/artist/8d0e541a-78a2-445f-a2e6-ebf20ee45f41'
SET person_ebf20ee45f41.isni_list = ['http://isni.org/isni/0000000078396069']
SET person_ebf20ee45f41.source = 'musicbrainz.org'


MERGE (person_dbdeef81688d:Person{ uuid: '3ff9970b-323e-440d-8ff6-dbdeef81688d' }) 
SET person_dbdeef81688d.name = 'Tommy LiPuma'
SET person_dbdeef81688d.gender = 'Male'
SET person_dbdeef81688d.country = 'US'
SET person_dbdeef81688d.discogs = 'https://www.discogs.com/artist/114262'
SET person_dbdeef81688d.imdb = 'https://www.imdb.com/name/nm0513879/'
SET person_dbdeef81688d.viaf = 'http://viaf.org/viaf/121562525'
SET person_dbdeef81688d.wikidata = 'https://www.wikidata.org/wiki/Q729227'
SET person_dbdeef81688d.databases = ['http://id.loc.gov/authorities/names/nr2003000254', 'https://www.worldcat.org/identities/lccn-nr2003000254']
SET person_dbdeef81688d.musicbrainz = 'https://musicbrainz.org/artist/3ff9970b-323e-440d-8ff6-dbdeef81688d'
SET person_dbdeef81688d.isni_list = ['http://isni.org/isni/0000000080220732']
SET person_dbdeef81688d.source = 'musicbrainz.org'


MERGE (person_4781ca060134:Person{ uuid: 'c7230059-e1f0-420a-8710-4781ca060134' }) 
SET person_4781ca060134.name = 'Al Schmitt'
SET person_4781ca060134.gender = 'Male'
SET person_4781ca060134.country = 'US'
SET person_4781ca060134.allmusic = 'https://www.allmusic.com/artist/mn0000933071'
SET person_4781ca060134.discogs = 'https://www.discogs.com/artist/227789'
SET person_4781ca060134.imdb = 'https://www.imdb.com/name/nm1491056/'
SET person_4781ca060134.viaf = 'http://viaf.org/viaf/66137273'
SET person_4781ca060134.wikidata = 'https://www.wikidata.org/wiki/Q4704778'
SET person_4781ca060134.databases = ['http://id.loc.gov/authorities/names/no2002037498', 'https://d-nb.info/gnd/1170697259', 'https://rateyourmusic.com/artist/al-schmitt', 'https://www.worldcat.org/identities/lccn-no2002037498/']
SET person_4781ca060134.musicbrainz = 'https://musicbrainz.org/artist/c7230059-e1f0-420a-8710-4781ca060134'
SET person_4781ca060134.isni_list = ['http://isni.org/isni/000000004195213X']
SET person_4781ca060134.source = 'musicbrainz.org'


MERGE (person_704d0a027013:Person{ uuid: '748dc2ef-09e9-46de-bfc8-704d0a027013' }) 
SET person_704d0a027013.name = 'Olga Román'
SET person_704d0a027013.gender = 'Female'
SET person_704d0a027013.country = 'ES'
SET person_704d0a027013.discogs = 'https://www.discogs.com/artist/1104835'
SET person_704d0a027013.wikidata = 'https://www.wikidata.org/wiki/Q7086670'
SET person_704d0a027013.wikipedia = 'https://en.wikipedia.org/wiki/Olga_Rom%C3%A1n'
SET person_704d0a027013.musicbrainz = 'https://musicbrainz.org/artist/748dc2ef-09e9-46de-bfc8-704d0a027013'
SET person_704d0a027013.source = 'musicbrainz.org'


MERGE (person_ca1108430882:Person{ uuid: '17d78170-7194-4603-8dbb-ca1108430882' }) 
SET person_ca1108430882.name = 'Avishai Cohen'
SET person_ca1108430882.gender = 'Male'
SET person_ca1108430882.disambiguation = 'Israeli jazz bassist'
SET person_ca1108430882.country = 'IL'
SET person_ca1108430882.allmusic = 'https://www.allmusic.com/artist/mn0000071908'
SET person_ca1108430882.discogs = 'https://www.discogs.com/artist/304734'
SET person_ca1108430882.imdb = 'https://www.imdb.com/name/nm1722445/'
SET person_ca1108430882.viaf = 'http://viaf.org/viaf/98429134'
SET person_ca1108430882.wikidata = 'https://www.wikidata.org/wiki/Q388320'
SET person_ca1108430882.databases = ['http://id.loc.gov/authorities/names/no98043100', 'https://catalogue.bnf.fr/ark:/12148/cb140444389', 'https://d-nb.info/gnd/135124832', 'http://snaccooperative.org/ark:/99166/w6gx5bfb', 'https://www.worldcat.org/identities/lccn-no98043100']
SET person_ca1108430882.musicbrainz = 'https://musicbrainz.org/artist/17d78170-7194-4603-8dbb-ca1108430882'
SET person_ca1108430882.isni_list = ['http://isni.org/isni/0000000119533307']
SET person_ca1108430882.source = 'musicbrainz.org'


MERGE (person_77dd63a33dcb:Person{ uuid: '7062af1b-b491-40a2-9d82-77dd63a33dcb' }) 
SET person_77dd63a33dcb.name = 'Terri Lyne Carrington'
SET person_77dd63a33dcb.gender = 'Female'
SET person_77dd63a33dcb.country = 'US'
SET person_77dd63a33dcb.allmusic = 'https://www.allmusic.com/artist/mn0000022508'
SET person_77dd63a33dcb.discogs = 'https://www.discogs.com/artist/275597'
SET person_77dd63a33dcb.viaf = 'http://viaf.org/viaf/96940266'
SET person_77dd63a33dcb.wikidata = 'https://www.wikidata.org/wiki/Q466966'
SET person_77dd63a33dcb.databases = ['http://id.loc.gov/authorities/names/n88625985', 'https://catalogue.bnf.fr/ark:/12148/cb139337879', 'https://d-nb.info/gnd/134638514', 'https://rateyourmusic.com/artist/terri_lyne_carrington', 'https://www.worldcat.org/identities/lccn-n88625985']
SET person_77dd63a33dcb.musicbrainz = 'https://musicbrainz.org/artist/7062af1b-b491-40a2-9d82-77dd63a33dcb'
SET person_77dd63a33dcb.isni_list = ['http://isni.org/isni/0000000114782064']
SET person_77dd63a33dcb.source = 'musicbrainz.org'


MERGE (person_71bbb076f5d5:Person{ uuid: 'd1f941ab-04e4-491d-ae27-71bbb076f5d5' }) 
SET person_71bbb076f5d5.name = 'Jeffrey “Tain” Watts'
SET person_71bbb076f5d5.gender = 'Male'
SET person_71bbb076f5d5.disambiguation = 'jazz drummer'
SET person_71bbb076f5d5.country = 'US'
SET person_71bbb076f5d5.allmusic = 'https://www.allmusic.com/artist/mn0000235787'
SET person_71bbb076f5d5.discogs = 'https://www.discogs.com/artist/253394'
SET person_71bbb076f5d5.viaf = 'http://viaf.org/viaf/119622817'
SET person_71bbb076f5d5.wikidata = 'https://www.wikidata.org/wiki/Q1686362'
SET person_71bbb076f5d5.databases = ['http://id.loc.gov/authorities/names/n84145398', 'https://catalogue.bnf.fr/ark:/12148/cb13901041z', 'https://d-nb.info/gnd/134551672', 'http://snaccooperative.org/ark:/99166/w66r5nts', 'https://www.worldcat.org/identities/lccn-n84145398']
SET person_71bbb076f5d5.musicbrainz = 'https://musicbrainz.org/artist/d1f941ab-04e4-491d-ae27-71bbb076f5d5'
SET person_71bbb076f5d5.isni_list = ['http://isni.org/isni/000000011480696X']
SET person_71bbb076f5d5.source = 'musicbrainz.org'

// labels

MERGE (label_8fb76f3e6ca9:Label{ uuid: '93c3b044-2b4e-4239-a73b-8fb76f3e6ca9' })
SET label_8fb76f3e6ca9.name= 'impulse!'

// performances

MERGE (perf_93680e5f578f:Performance{ uuid: '0153f3c5-5174-4bc6-b054-93680e5f578f' })
SET perf_93680e5f578f.name = 'Monk\\'s Mood 1'
SET perf_93680e5f578f.duration = '0:42'
SET perf_93680e5f578f.begin_date = '1996-01-03'
SET perf_93680e5f578f.end_date = '1996-01-04'
SET perf_93680e5f578f.source = 'musicbrainz.org'


MERGE (perf_9d6be0ea2272:Performance{ uuid: '2d6be3e3-5f9c-4c47-b518-9d6be0ea2272' })
SET perf_9d6be0ea2272.name = 'PanaMonk'
SET perf_9d6be0ea2272.duration = '4:22'
SET perf_9d6be0ea2272.begin_date = '1996-01-03'
SET perf_9d6be0ea2272.end_date = '1996-01-04'
SET perf_9d6be0ea2272.source = 'musicbrainz.org'


MERGE (perf_6ba70f3ff4e9:Performance{ uuid: 'f3ef71ef-4ebf-4fd7-9964-6ba70f3ff4e9' })
SET perf_6ba70f3ff4e9.name = 'Bright Mississippi'
SET perf_6ba70f3ff4e9.duration = '5:39'
SET perf_6ba70f3ff4e9.begin_date = '1996-01-03'
SET perf_6ba70f3ff4e9.end_date = '1996-01-04'
SET perf_6ba70f3ff4e9.source = 'musicbrainz.org'


MERGE (perf_a8388f1808cb:Performance{ uuid: '3842118d-14c4-4710-a881-a8388f1808cb' })
SET perf_a8388f1808cb.name = 'Think of One'
SET perf_a8388f1808cb.duration = '4:17'
SET perf_a8388f1808cb.begin_date = '1996-01-03'
SET perf_a8388f1808cb.end_date = '1996-01-04'
SET perf_a8388f1808cb.source = 'musicbrainz.org'


MERGE (perf_e72cdce04a87:Performance{ uuid: '6fbe200a-9b95-4490-8e2f-e72cdce04a87' })
SET perf_e72cdce04a87.name = 'Mercedes\\' Mood'
SET perf_e72cdce04a87.duration = '4:51'
SET perf_e72cdce04a87.begin_date = '1996-01-03'
SET perf_e72cdce04a87.end_date = '1996-01-04'
SET perf_e72cdce04a87.source = 'musicbrainz.org'


MERGE (perf_92de23888673:Performance{ uuid: '20e1e002-362b-4515-9566-92de23888673' })
SET perf_92de23888673.name = 'Hot Bean Strut'
SET perf_92de23888673.duration = '5:13'
SET perf_92de23888673.begin_date = '1996-01-03'
SET perf_92de23888673.end_date = '1996-01-04'
SET perf_92de23888673.source = 'musicbrainz.org'


MERGE (perf_a9ac49175b7b:Performance{ uuid: 'd5a74a08-e4ab-410b-ad7a-a9ac49175b7b' })
SET perf_a9ac49175b7b.name = 'Reflections'
SET perf_a9ac49175b7b.duration = '5:54'
SET perf_a9ac49175b7b.begin_date = '1996-01-03'
SET perf_a9ac49175b7b.end_date = '1996-01-04'
SET perf_a9ac49175b7b.source = 'musicbrainz.org'


MERGE (perf_abdec8745d9c:Performance{ uuid: '897f29ee-279d-4700-a0dd-abdec8745d9c' })
SET perf_abdec8745d9c.name = 'September in Rio'
SET perf_abdec8745d9c.duration = '3:54'
SET perf_abdec8745d9c.begin_date = '1996-01-03'
SET perf_abdec8745d9c.end_date = '1996-01-04'
SET perf_abdec8745d9c.source = 'musicbrainz.org'


MERGE (perf_43b03d21ac63:Performance{ uuid: '46c369d8-f0db-4893-8952-43b03d21ac63' })
SET perf_43b03d21ac63.name = 'Everything Happens to Me'
SET perf_43b03d21ac63.duration = '6:26'
SET perf_43b03d21ac63.begin_date = '1996-01-03'
SET perf_43b03d21ac63.end_date = '1996-01-04'
SET perf_43b03d21ac63.source = 'musicbrainz.org'


MERGE (perf_e362fe6400da:Performance{ uuid: '68f1db2b-7333-45bc-b3c3-e362fe6400da' })
SET perf_e362fe6400da.name = '\\'Round Midnight'
SET perf_e362fe6400da.duration = '5:25'
SET perf_e362fe6400da.begin_date = '1996-01-03'
SET perf_e362fe6400da.end_date = '1996-01-04'
SET perf_e362fe6400da.source = 'musicbrainz.org'


MERGE (perf_ee6e239b850d:Performance{ uuid: '53122a4e-4125-4052-a251-ee6e239b850d' })
SET perf_ee6e239b850d.name = 'Evidence / Four in One'
SET perf_ee6e239b850d.duration = '4:44'
SET perf_ee6e239b850d.begin_date = '1996-01-03'
SET perf_ee6e239b850d.end_date = '1996-01-04'
SET perf_ee6e239b850d.source = 'musicbrainz.org'


MERGE (perf_b002947efb42:Performance{ uuid: '792badc0-75b3-4d2d-a6e6-b002947efb42' })
SET perf_b002947efb42.name = 'Monk\\'s Mood 2'
SET perf_b002947efb42.duration = '0:43'
SET perf_b002947efb42.begin_date = '1996-01-03'
SET perf_b002947efb42.end_date = '1996-01-04'
SET perf_b002947efb42.source = 'musicbrainz.org'




// labels
MERGE (release_5365210722a1)-[:HAS_LABEL]->(label_8fb76f3e6ca9)


// tracks
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_93680e5f578f)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_9d6be0ea2272)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_6ba70f3ff4e9)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_a8388f1808cb)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_e72cdce04a87)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_92de23888673)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_a9ac49175b7b)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_abdec8745d9c)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_43b03d21ac63)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_e362fe6400da)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '11', sequence: 11}]->(perf_ee6e239b850d)
MERGE (release_5365210722a1)-[:HAS_TRACK {name: '12', sequence: 12}]->(perf_b002947efb42)

// works

MERGE (person_37e17d15cdab:Person{ uuid: '8598186d-826e-4860-b8c7-37e17d15cdab' }) 
SET person_37e17d15cdab.name = 'Bernie Hanighen'
SET person_37e17d15cdab.gender = 'Male'
SET person_37e17d15cdab.country = 'US'
SET person_37e17d15cdab.allmusic = 'https://www.allmusic.com/artist/mn0000049803'
SET person_37e17d15cdab.discogs = 'https://www.discogs.com/artist/264203'
SET person_37e17d15cdab.imdb = 'https://www.imdb.com/name/nm0359887/'
SET person_37e17d15cdab.viaf = 'http://viaf.org/viaf/78318349'
SET person_37e17d15cdab.wikidata = 'https://www.wikidata.org/wiki/Q4894399'
SET person_37e17d15cdab.databases = ['http://id.loc.gov/authorities/names/no00016569', 'https://adp.library.ucsb.edu/names/108341', 'https://catalogue.bnf.fr/ark:/12148/cb13798018n', 'https://d-nb.info/gnd/134902696', 'http://snaccooperative.org/ark:/99166/w6vj8k79', 'https://nla.gov.au/nla.party-1496866', 'https://rateyourmusic.com/artist/bernie_hanighen', 'https://www.ibdb.com/person.php?id=12695', 'https://www.worldcat.org/identities/lccn-no00016569/']
SET person_37e17d15cdab.musicbrainz = 'https://musicbrainz.org/artist/8598186d-826e-4860-b8c7-37e17d15cdab'
SET person_37e17d15cdab.isni_list = ['http://isni.org/isni/0000000039653181']
SET person_37e17d15cdab.source = 'musicbrainz.org'


MERGE (person_224ffa1c263c:Person{ uuid: '754ed78e-d5c5-4a5f-846d-224ffa1c263c' }) 
SET person_224ffa1c263c.name = 'Cootie Williams'
SET person_224ffa1c263c.gender = 'Male'
SET person_224ffa1c263c.country = 'US'
SET person_224ffa1c263c.allmusic = 'https://www.allmusic.com/artist/mn0000780401'
SET person_224ffa1c263c.discogs = 'https://www.discogs.com/artist/258696'
SET person_224ffa1c263c.imdb = 'https://www.imdb.com/name/nm1102362/'
SET person_224ffa1c263c.viaf = 'http://viaf.org/viaf/35779900'
SET person_224ffa1c263c.wikidata = 'https://www.wikidata.org/wiki/Q523899'
SET person_224ffa1c263c.databases = ['http://id.loc.gov/authorities/names/n81095925', 'https://adp.library.ucsb.edu/names/103275', 'https://catalogue.bnf.fr/ark:/12148/cb13901176w', 'https://d-nb.info/gnd/134557468', 'http://snaccooperative.org/ark:/99166/w6j10pt5', 'https://rateyourmusic.com/artist/cootie_williams', 'https://www.worldcat.org/identities/lccn-n81095925']
SET person_224ffa1c263c.musicbrainz = 'https://musicbrainz.org/artist/754ed78e-d5c5-4a5f-846d-224ffa1c263c'
SET person_224ffa1c263c.isni_list = ['http://isni.org/isni/0000000081896996', 'http://isni.org/isni/0000000120129248']
SET person_224ffa1c263c.source = 'musicbrainz.org'


MERGE (person_5260b4274ed4:Person{ uuid: '8e8c7417-c905-46b1-b42a-5260b4274ed4' }) 
SET person_5260b4274ed4.name = 'Thelonious Monk'
SET person_5260b4274ed4.gender = 'Male'
SET person_5260b4274ed4.country = 'US'
SET person_5260b4274ed4.allmusic = 'https://www.allmusic.com/artist/mn0000490416'
SET person_5260b4274ed4.bbc = 'https://www.bbc.co.uk/music/artists/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.discogs = 'https://www.discogs.com/artist/145256'
SET person_5260b4274ed4.imdb = 'https://www.imdb.com/name/nm0598243/'
SET person_5260b4274ed4.viaf = 'http://viaf.org/viaf/44485892'
SET person_5260b4274ed4.wikidata = 'https://www.wikidata.org/wiki/Q109612'
SET person_5260b4274ed4.databases = ['http://id.loc.gov/authorities/names/n82218969', 'https://catalogue.bnf.fr/ark:/12148/cb13897622g', 'https://d-nb.info/gnd/118826158', 'http://snaccooperative.org/ark:/99166/w6j38zvn', 'https://rateyourmusic.com/artist/thelonious_monk', 'https://www.worldcat.org/identities/lccn-n82218969']
SET person_5260b4274ed4.musicbrainz = 'https://musicbrainz.org/artist/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.isni_list = ['http://isni.org/isni/0000000120249127']
SET person_5260b4274ed4.source = 'musicbrainz.org'


MERGE (work_513adcbc632b:Work{ uuid: '72193fa7-7da8-4a23-90a9-513adcbc632b' })
SET work_513adcbc632b.name = 'Bright Mississippi'
SET work_513adcbc632b.iswc = 'T-070.235.450-4'
SET work_513adcbc632b.type = 'Song'
SET work_513adcbc632b.source = 'musicbrainz.org'


MERGE (work_1fb072ab2042:Work{ uuid: 'f99aa87a-d665-3d56-8df6-1fb072ab2042' })
SET work_1fb072ab2042.name = '’Round Midnight'
SET work_1fb072ab2042.iswc = 'T-070.002.363-7'
SET work_1fb072ab2042.type = 'Song'
SET work_1fb072ab2042.tags = ['jazz']
SET work_1fb072ab2042.wikidata = 'https://www.wikidata.org/wiki/Q383357'
SET work_1fb072ab2042.databases = ['http://id.loc.gov/authorities/names/no00058463', 'https://d-nb.info/gnd/1031479511', 'https://www.worldcat.org/identities/lccn-no00058463']
SET work_1fb072ab2042.musicbrainz = 'https://musicbrainz.org/work/f99aa87a-d665-3d56-8df6-1fb072ab2042'
SET work_1fb072ab2042.source = 'musicbrainz.org'


MERGE (work_c6cfe3b5cb12:Work{ uuid: '63ca960f-0c70-309f-b9f0-c6cfe3b5cb12' })
SET work_c6cfe3b5cb12.name = 'Reflections'
SET work_c6cfe3b5cb12.iswc = 'T-700.057.164-4'
SET work_c6cfe3b5cb12.type = 'Song'
SET work_c6cfe3b5cb12.source = 'musicbrainz.org'


MERGE (work_3bfe4c12c91f:Work{ uuid: '26e6980c-5e30-3e37-8c9f-3bfe4c12c91f' })
SET work_3bfe4c12c91f.name = 'Monk’s Mood'
SET work_3bfe4c12c91f.iswc = 'T-070.242.256-7'
SET work_3bfe4c12c91f.type = 'Song'
SET work_3bfe4c12c91f.musicbrainz = 'https://musicbrainz.org/work/26e6980c-5e30-3e37-8c9f-3bfe4c12c91f'
SET work_3bfe4c12c91f.source = 'musicbrainz.org'


MERGE (work_1fcc2e48951a:Work{ uuid: '091fb98b-4a04-3a59-9a50-1fcc2e48951a' })
SET work_1fcc2e48951a.name = 'Think of One'
SET work_1fcc2e48951a.type = 'Song'
SET work_1fcc2e48951a.source = 'musicbrainz.org'



// performances of
MERGE (perf_6ba70f3ff4e9)-[:PERFORMANCE_OF]->(work_513adcbc632b)
MERGE (perf_e362fe6400da)-[:PERFORMANCE_OF]->(work_1fb072ab2042)
MERGE (perf_a9ac49175b7b)-[:PERFORMANCE_OF]->(work_c6cfe3b5cb12)
MERGE (perf_93680e5f578f)-[:PERFORMANCE_OF]->(work_3bfe4c12c91f)
MERGE (perf_b002947efb42)-[:PERFORMANCE_OF]->(work_3bfe4c12c91f)
MERGE (perf_a8388f1808cb)-[:PERFORMANCE_OF]->(work_1fcc2e48951a)


// composers
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_513adcbc632b)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_1fb072ab2042)
MERGE (person_224ffa1c263c)-[:COMPOSED]->(work_1fb072ab2042)
MERGE (person_37e17d15cdab)-[:WROTE_LYRICS]->(work_1fb072ab2042)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_c6cfe3b5cb12)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_3bfe4c12c91f)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_1fcc2e48951a)


// place nodes

MERGE (place_6e44f7dfcf98:Place{ uuid: '859fdb68-9363-4ea0-b35a-6e44f7dfcf98' })
SET place_6e44f7dfcf98.name = 'Power Station at BerkleeNYC'
SET place_6e44f7dfcf98.source = 'musicbrainz.org'


// place relationships
MERGE (perf_93680e5f578f)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_9d6be0ea2272)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_6ba70f3ff4e9)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_a8388f1808cb)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_e72cdce04a87)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_92de23888673)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_a9ac49175b7b)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_abdec8745d9c)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_43b03d21ac63)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_e362fe6400da)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_ee6e239b850d)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)
MERGE (perf_b002947efb42)-[:HAS_PLACE { type: 'recorded at', begin_date: '1996-01-03', end_date: '1996-01-04' }]->(place_6e44f7dfcf98)

MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_93680e5f578f)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_93680e5f578f)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_93680e5f578f)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_93680e5f578f)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_93680e5f578f)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_9d6be0ea2272)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_9d6be0ea2272)
MERGE (person_71bbb076f5d5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9d6be0ea2272)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_9d6be0ea2272)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_9d6be0ea2272)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_9d6be0ea2272)
MERGE (person_77dd63a33dcb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6ba70f3ff4e9)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_6ba70f3ff4e9)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6ba70f3ff4e9)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_6ba70f3ff4e9)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_6ba70f3ff4e9)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_6ba70f3ff4e9)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a8388f1808cb)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a8388f1808cb)
MERGE (person_71bbb076f5d5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a8388f1808cb)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a8388f1808cb)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_a8388f1808cb)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a8388f1808cb)
MERGE (person_77dd63a33dcb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e72cdce04a87)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_e72cdce04a87)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e72cdce04a87)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_e72cdce04a87)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e72cdce04a87)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_e72cdce04a87)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_92de23888673)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_92de23888673)
MERGE (person_71bbb076f5d5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_92de23888673)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_92de23888673)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_92de23888673)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_92de23888673)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a9ac49175b7b)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a9ac49175b7b)
MERGE (person_71bbb076f5d5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a9ac49175b7b)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a9ac49175b7b)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_a9ac49175b7b)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a9ac49175b7b)
MERGE (person_77dd63a33dcb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_abdec8745d9c)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_abdec8745d9c)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_abdec8745d9c)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_abdec8745d9c)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_abdec8745d9c)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_abdec8745d9c)
MERGE (person_704d0a027013)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_abdec8745d9c)
MERGE (person_77dd63a33dcb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_43b03d21ac63)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_43b03d21ac63)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_43b03d21ac63)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_43b03d21ac63)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_43b03d21ac63)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_43b03d21ac63)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_e362fe6400da)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e362fe6400da)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_e362fe6400da)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e362fe6400da)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_e362fe6400da)
MERGE (person_77dd63a33dcb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_ee6e239b850d)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_ee6e239b850d)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ee6e239b850d)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_ee6e239b850d)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_ee6e239b850d)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_ee6e239b850d)
MERGE (person_ca1108430882)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_b002947efb42)
MERGE (person_ebf20ee45f41)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b002947efb42)
MERGE (person_4781ca060134)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_b002947efb42)
MERGE (person_dbdeef81688d)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_b002947efb42)
MERGE (person_2fb64f98a555)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_b002947efb42)



"""
)