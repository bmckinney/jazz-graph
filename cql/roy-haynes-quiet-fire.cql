// releases

MERGE (release_3bbb7af52e4e:Release{ uuid: 'aa091dc7-5a23-492b-a8e8-3bbb7af52e4e' })
SET release_3bbb7af52e4e.name = 'Quiet Fire'
SET release_3bbb7af52e4e.country = 'US'
SET release_3bbb7af52e4e.date = '2004-09-01'
SET release_3bbb7af52e4e.format = 'CD'
SET release_3bbb7af52e4e.discode = 'GCD 95005-2'
SET release_3bbb7af52e4e.allmusic = 'https://www.allmusic.com/album/release/mr0000478434'
SET release_3bbb7af52e4e.discogs = 'https://www.discogs.com/release/5792710'
SET release_3bbb7af52e4e.musicbrainz = 'http://musicbrainz.org/release/aa091dc7-5a23-492b-a8e8-3bbb7af52e4e'
SET release_3bbb7af52e4e.source = 'musicbrainz.org'
SET release_3bbb7af52e4e.timestamp = timestamp()

MERGE (person_ba539b0ef93c:Person{ uuid: '7cf86f47-fbb0-44a5-949e-ba539b0ef93c' }) 
SET person_ba539b0ef93c.name = 'Baker Bigsby'
SET person_ba539b0ef93c.gender = 'Male'
SET person_ba539b0ef93c.country = 'US'
SET person_ba539b0ef93c.discogs = 'https://www.discogs.com/artist/363563'
SET person_ba539b0ef93c.musicbrainz = 'https://musicbrainz.org/artist/7cf86f47-fbb0-44a5-949e-ba539b0ef93c'
SET person_ba539b0ef93c.source = 'musicbrainz.org'
SET person_ba539b0ef93c.timestamp = timestamp()

MERGE (person_bb48278688a0:Person{ uuid: '6c9ca088-9da0-404f-ae61-bb48278688a0' }) 
SET person_bb48278688a0.name = 'Peter Knapp'
SET person_bb48278688a0.gender = 'Male'
SET person_bb48278688a0.disambiguation = 'bass'
SET person_bb48278688a0.discogs = 'https://www.discogs.com/artist/947179'
SET person_bb48278688a0.musicbrainz = 'https://musicbrainz.org/artist/6c9ca088-9da0-404f-ae61-bb48278688a0'
SET person_bb48278688a0.source = 'musicbrainz.org'
SET person_bb48278688a0.timestamp = timestamp()

MERGE (person_3b8d23ba518a:Person{ uuid: '9a6358be-4223-40f5-a8ee-3b8d23ba518a' }) 
SET person_3b8d23ba518a.name = 'Baxter Fillmore'
SET person_3b8d23ba518a.discogs = 'https://www.discogs.com/artist/1488637'
SET person_3b8d23ba518a.musicbrainz = 'https://musicbrainz.org/artist/9a6358be-4223-40f5-a8ee-3b8d23ba518a'
SET person_3b8d23ba518a.source = 'musicbrainz.org'
SET person_3b8d23ba518a.timestamp = timestamp()

MERGE (person_8fe19080caaf:Person{ uuid: 'edbe5d7f-9511-4dfe-847a-8fe19080caaf' }) 
SET person_8fe19080caaf.name = 'Bobby Hutcherson'
SET person_8fe19080caaf.gender = 'Male'
SET person_8fe19080caaf.country = 'US'
SET person_8fe19080caaf.allmusic = 'https://www.allmusic.com/artist/mn0000081231'
SET person_8fe19080caaf.discogs = 'https://www.discogs.com/artist/29968'
SET person_8fe19080caaf.imdb = 'https://www.imdb.com/name/nm0404201/'
SET person_8fe19080caaf.viaf = 'http://viaf.org/viaf/85517308'
SET person_8fe19080caaf.wikidata = 'https://www.wikidata.org/wiki/Q888571'
SET person_8fe19080caaf.databases = ['http://d-nb.info/gnd/134413393', 'http://id.loc.gov/authorities/names/n81149294', 'https://catalogue.bnf.fr/ark:/12148/cb13895429v', 'https://rateyourmusic.com/artist/bobby_hutcherson', 'https://www.musik-sammler.de/artist/bobby-hutcherson/', 'https://www.worldcat.org/identities/lccn-n81-149294']
SET person_8fe19080caaf.musicbrainz = 'https://musicbrainz.org/artist/edbe5d7f-9511-4dfe-847a-8fe19080caaf'
SET person_8fe19080caaf.isni_list = ['http://isni.org/isni/0000000114505729']
SET person_8fe19080caaf.source = 'musicbrainz.org'
SET person_8fe19080caaf.timestamp = timestamp()

MERGE (person_ac19da0b921c:Person{ uuid: 'e37848cb-455c-4963-bdff-ac19da0b921c' }) 
SET person_ac19da0b921c.name = 'John Klemmer'
SET person_ac19da0b921c.gender = 'Male'
SET person_ac19da0b921c.country = 'US'
SET person_ac19da0b921c.allmusic = 'https://www.allmusic.com/artist/mn0000192260'
SET person_ac19da0b921c.discogs = 'https://www.discogs.com/artist/50123'
SET person_ac19da0b921c.viaf = 'http://viaf.org/viaf/59269987'
SET person_ac19da0b921c.wikidata = 'https://www.wikidata.org/wiki/Q1700723'
SET person_ac19da0b921c.databases = ['http://d-nb.info/gnd/134979400', 'http://id.loc.gov/authorities/names/n91122087', 'https://catalogue.bnf.fr/ark:/12148/cb13896037m', 'https://rateyourmusic.com/artist/john_klemmer', 'https://www.worldcat.org/identities/lccn-n91122087']
SET person_ac19da0b921c.musicbrainz = 'https://musicbrainz.org/artist/e37848cb-455c-4963-bdff-ac19da0b921c'
SET person_ac19da0b921c.isni_list = ['http://isni.org/isni/0000000063105900']
SET person_ac19da0b921c.source = 'musicbrainz.org'
SET person_ac19da0b921c.timestamp = timestamp()

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
SET person_e044666c4828.timestamp = timestamp()

MERGE (person_f180a2b2aaf0:Person{ uuid: 'a569ac3b-f21b-4773-84a6-f180a2b2aaf0' }) 
SET person_f180a2b2aaf0.name = 'Stanley Cowell'
SET person_f180a2b2aaf0.gender = 'Male'
SET person_f180a2b2aaf0.country = 'US'
SET person_f180a2b2aaf0.allmusic = 'https://www.allmusic.com/artist/mn0000011303'
SET person_f180a2b2aaf0.discogs = 'https://www.discogs.com/artist/152684'
SET person_f180a2b2aaf0.imdb = 'https://www.imdb.com/name/nm0184714/'
SET person_f180a2b2aaf0.viaf = 'http://viaf.org/viaf/84970497'
SET person_f180a2b2aaf0.wikidata = 'https://www.wikidata.org/wiki/Q345934'
SET person_f180a2b2aaf0.databases = ['http://d-nb.info/gnd/134655648', 'http://id.loc.gov/authorities/names/n81149292', 'https://catalogue.bnf.fr/ark:/12148/cb13892810t', 'http://snaccooperative.org/ark:/99166/w6029r8m', 'https://www.worldcat.org/identities/lccn-n81149292']
SET person_f180a2b2aaf0.musicbrainz = 'https://musicbrainz.org/artist/a569ac3b-f21b-4773-84a6-f180a2b2aaf0'
SET person_f180a2b2aaf0.isni_list = ['http://isni.org/isni/0000000081607496']
SET person_f180a2b2aaf0.source = 'musicbrainz.org'
SET person_f180a2b2aaf0.timestamp = timestamp()

MERGE (person_41d78c725ce3:Person{ uuid: '7d3aa1dd-5e8b-47f3-a65b-41d78c725ce3' }) 
SET person_41d78c725ce3.name = 'George Cables'
SET person_41d78c725ce3.gender = 'Male'
SET person_41d78c725ce3.country = 'US'
SET person_41d78c725ce3.allmusic = 'https://www.allmusic.com/artist/mn0000634700'
SET person_41d78c725ce3.discogs = 'https://www.discogs.com/artist/255116'
SET person_41d78c725ce3.viaf = 'http://viaf.org/viaf/32182693'
SET person_41d78c725ce3.wikidata = 'https://www.wikidata.org/wiki/Q365812'
SET person_41d78c725ce3.databases = ['http://d-nb.info/gnd/134341910', 'http://id.loc.gov/authorities/names/n80093137', 'https://catalogue.bnf.fr/ark:/12148/cb138920516', 'http://snaccooperative.org/ark:/99166/w6c2630f', 'https://www.worldcat.org/identities/lccn-n80093137']
SET person_41d78c725ce3.musicbrainz = 'https://musicbrainz.org/artist/7d3aa1dd-5e8b-47f3-a65b-41d78c725ce3'
SET person_41d78c725ce3.isni_list = ['http://isni.org/isni/0000000115112388']
SET person_41d78c725ce3.source = 'musicbrainz.org'
SET person_41d78c725ce3.timestamp = timestamp()

MERGE (person_22a5fbaaf713:Person{ uuid: 'cf362673-150d-4a99-8e7b-22a5fbaaf713' }) 
SET person_22a5fbaaf713.name = 'Cecil McBee'
SET person_22a5fbaaf713.gender = 'Male'
SET person_22a5fbaaf713.country = 'US'
SET person_22a5fbaaf713.allmusic = 'https://www.allmusic.com/artist/mn0000739015'
SET person_22a5fbaaf713.discogs = 'https://www.discogs.com/artist/258511'
SET person_22a5fbaaf713.viaf = 'http://viaf.org/viaf/49408740'
SET person_22a5fbaaf713.wikidata = 'https://www.wikidata.org/wiki/Q1052331'
SET person_22a5fbaaf713.databases = ['http://d-nb.info/gnd/134450612', 'http://id.loc.gov/authorities/names/n78048853', 'https://catalogue.bnf.fr/ark:/12148/cb13897275z', 'https://www.worldcat.org/identities/lccn-n78048853']
SET person_22a5fbaaf713.musicbrainz = 'https://musicbrainz.org/artist/cf362673-150d-4a99-8e7b-22a5fbaaf713'
SET person_22a5fbaaf713.isni_list = ['http://isni.org/isni/0000000079949972']
SET person_22a5fbaaf713.source = 'musicbrainz.org'
SET person_22a5fbaaf713.timestamp = timestamp()

MERGE (person_2099544918fe:Person{ uuid: 'faba4b14-49c5-4128-9e31-2099544918fe' }) 
SET person_2099544918fe.name = 'Dave Jackson'
SET person_2099544918fe.gender = 'Male'
SET person_2099544918fe.disambiguation = 'bassist'
SET person_2099544918fe.country = 'US'
SET person_2099544918fe.discogs = 'https://www.discogs.com/artist/2794799'
SET person_2099544918fe.musicbrainz = 'https://musicbrainz.org/artist/faba4b14-49c5-4128-9e31-2099544918fe'
SET person_2099544918fe.source = 'musicbrainz.org'
SET person_2099544918fe.timestamp = timestamp()

MERGE (person_176a3521680f:Person{ uuid: 'be718f29-078b-49e6-bcc4-176a3521680f' }) 
SET person_176a3521680f.name = 'Phil Kaffel'
SET person_176a3521680f.gender = 'Male'
SET person_176a3521680f.country = 'US'
SET person_176a3521680f.allmusic = 'https://www.allmusic.com/artist/mn0000848163'
SET person_176a3521680f.discogs = 'https://www.discogs.com/artist/156347'
SET person_176a3521680f.databases = ['https://rateyourmusic.com/artist/phil_kaffel']
SET person_176a3521680f.musicbrainz = 'https://musicbrainz.org/artist/be718f29-078b-49e6-bcc4-176a3521680f'
SET person_176a3521680f.source = 'musicbrainz.org'
SET person_176a3521680f.timestamp = timestamp()

MERGE (person_15c58dce8f26:Person{ uuid: 'ba72fa6c-7fbc-42ca-b4a8-15c58dce8f26' }) 
SET person_15c58dce8f26.name = 'Kenneth Nash'
SET person_15c58dce8f26.gender = 'Male'
SET person_15c58dce8f26.discogs = 'https://www.discogs.com/artist/309767'
SET person_15c58dce8f26.musicbrainz = 'https://musicbrainz.org/artist/ba72fa6c-7fbc-42ca-b4a8-15c58dce8f26'
SET person_15c58dce8f26.source = 'musicbrainz.org'
SET person_15c58dce8f26.timestamp = timestamp()

MERGE (person_a7fbd89f7779:Person{ uuid: 'ebdd22ea-8d8a-4be5-a51b-a7fbd89f7779' }) 
SET person_a7fbd89f7779.name = 'Eddie Bill Harris'
SET person_a7fbd89f7779.gender = 'Male'
SET person_a7fbd89f7779.disambiguation = 'engineer'
SET person_a7fbd89f7779.discogs = 'https://www.discogs.com/artist/305123'
SET person_a7fbd89f7779.musicbrainz = 'https://musicbrainz.org/artist/ebdd22ea-8d8a-4be5-a51b-a7fbd89f7779'
SET person_a7fbd89f7779.source = 'musicbrainz.org'
SET person_a7fbd89f7779.timestamp = timestamp()

MERGE (person_994c0b94aa4d:Person{ uuid: 'b9c4885c-ac98-4354-b3ad-994c0b94aa4d' }) 
SET person_994c0b94aa4d.name = 'Ricardo Strobert'
SET person_994c0b94aa4d.gender = 'Male'
SET person_994c0b94aa4d.disambiguation = 'saxophonist and flutist'
SET person_994c0b94aa4d.country = 'US'
SET person_994c0b94aa4d.discogs = 'https://www.discogs.com/artist/1669032'
SET person_994c0b94aa4d.musicbrainz = 'https://musicbrainz.org/artist/b9c4885c-ac98-4354-b3ad-994c0b94aa4d'
SET person_994c0b94aa4d.source = 'musicbrainz.org'
SET person_994c0b94aa4d.timestamp = timestamp()

MERGE (person_da3f335093a1:Person{ uuid: 'c492873b-5d95-4c93-b424-da3f335093a1' }) 
SET person_da3f335093a1.name = 'Milcho Leviev'
SET person_da3f335093a1.gender = 'Male'
SET person_da3f335093a1.country = 'BG'
SET person_da3f335093a1.allmusic = 'https://www.allmusic.com/artist/mn0000897581'
SET person_da3f335093a1.discogs = 'https://www.discogs.com/artist/280705'
SET person_da3f335093a1.imdb = 'https://www.imdb.com/name/nm0505527/'
SET person_da3f335093a1.viaf = 'http://viaf.org/viaf/79169945'
SET person_da3f335093a1.wikidata = 'https://www.wikidata.org/wiki/Q358753'
SET person_da3f335093a1.wikipedia = 'https://en.wikipedia.org/wiki/Milcho_Leviev'
SET person_da3f335093a1.databases = ['http://d-nb.info/gnd/129467383', 'http://id.loc.gov/authorities/names/n82234926', 'https://catalogue.bnf.fr/ark:/12148/cb13948649w', 'https://rateyourmusic.com/artist/milcho_leviev', 'https://www.worldcat.org/identities/lccn-n82234926']
SET person_da3f335093a1.musicbrainz = 'https://musicbrainz.org/artist/c492873b-5d95-4c93-b424-da3f335093a1'
SET person_da3f335093a1.isni_list = ['http://isni.org/isni/0000000078396579']
SET person_da3f335093a1.source = 'musicbrainz.org'
SET person_da3f335093a1.timestamp = timestamp()

MERGE (person_20039cafef7b:Person{ uuid: '56fbc674-7d57-4fc0-b36c-20039cafef7b' }) 
SET person_20039cafef7b.name = 'Ed Michel'
SET person_20039cafef7b.discogs = 'https://www.discogs.com/artist/166631'
SET person_20039cafef7b.imdb = 'https://www.imdb.com/name/nm2123705/'
SET person_20039cafef7b.wikidata = 'https://www.wikidata.org/wiki/Q92309803'
SET person_20039cafef7b.musicbrainz = 'https://musicbrainz.org/artist/56fbc674-7d57-4fc0-b36c-20039cafef7b'
SET person_20039cafef7b.source = 'musicbrainz.org'
SET person_20039cafef7b.timestamp = timestamp()

MERGE (person_9ee947b4ce37:Person{ uuid: 'bcab8301-c7e5-4689-a4ad-9ee947b4ce37' }) 
SET person_9ee947b4ce37.name = 'Joe Henderson'
SET person_9ee947b4ce37.gender = 'Male'
SET person_9ee947b4ce37.disambiguation = 'US jazz tenor saxophonist'
SET person_9ee947b4ce37.country = 'US'
SET person_9ee947b4ce37.allmusic = 'https://www.allmusic.com/artist/mn0000139804'
SET person_9ee947b4ce37.allmusic = 'https://www.allmusic.com/artist/mn0002687715'
SET person_9ee947b4ce37.discogs = 'https://www.discogs.com/artist/10079'
SET person_9ee947b4ce37.viaf = 'http://viaf.org/viaf/115064662'
SET person_9ee947b4ce37.wikidata = 'https://www.wikidata.org/wiki/Q506006'
SET person_9ee947b4ce37.databases = ['http://d-nb.info/gnd/131961454', 'http://id.loc.gov/authorities/names/n82164702', 'https://catalogue.bnf.fr/ark:/12148/cb138951291', 'http://snaccooperative.org/ark:/99166/w6hm8fsd', 'https://nla.gov.au/nla.party-1048452', 'https://openlibrary.org/works/OL5629680A', 'https://rateyourmusic.com/artist/joe_henderson', 'https://www.worldcat.org/identities/lccn-n82164702']
SET person_9ee947b4ce37.musicbrainz = 'https://musicbrainz.org/artist/bcab8301-c7e5-4689-a4ad-9ee947b4ce37'
SET person_9ee947b4ce37.isni_list = ['http://isni.org/isni/0000000081835181']
SET person_9ee947b4ce37.source = 'musicbrainz.org'
SET person_9ee947b4ce37.timestamp = timestamp()

MERGE (person_823edc2a7c02:Person{ uuid: '5ca31148-6257-44eb-bb0d-823edc2a7c02' }) 
SET person_823edc2a7c02.name = 'Marcus Fiorillo'
SET person_823edc2a7c02.gender = 'Male'
SET person_823edc2a7c02.disambiguation = 'Jazz guitarist'
SET person_823edc2a7c02.discogs = 'https://www.discogs.com/artist/1282894'
SET person_823edc2a7c02.musicbrainz = 'https://musicbrainz.org/artist/5ca31148-6257-44eb-bb0d-823edc2a7c02'
SET person_823edc2a7c02.source = 'musicbrainz.org'
SET person_823edc2a7c02.timestamp = timestamp()

MERGE (person_a00dfdfd4013:Person{ uuid: 'f8f465ca-08f4-40ee-af1d-a00dfdfd4013' }) 
SET person_a00dfdfd4013.name = 'Nyya Lark'
SET person_a00dfdfd4013.discogs = 'https://www.discogs.com/artist/373030'
SET person_a00dfdfd4013.musicbrainz = 'https://musicbrainz.org/artist/f8f465ca-08f4-40ee-af1d-a00dfdfd4013'
SET person_a00dfdfd4013.source = 'musicbrainz.org'
SET person_a00dfdfd4013.timestamp = timestamp()
// labels

MERGE (label_b3591da0e289:Label{ uuid: '31d1382a-cc94-4829-9949-b3591da0e289' })
SET label_b3591da0e289.name= 'Galaxy'

// performances

MERGE (perf_e33d873d572d:Performance{ uuid: 'b66843f7-1eb7-4dd9-abc9-e33d873d572d' })
SET perf_e33d873d572d.name = 'Thank You Thank You'
SET perf_e33d873d572d.duration = '6:55'
SET perf_e33d873d572d.source = 'musicbrainz.org'
SET perf_e33d873d572d.timestamp = timestamp()

MERGE (perf_5ddd932379ef:Performance{ uuid: 'bd02b580-d8ae-4367-9a59-5ddd932379ef' })
SET perf_5ddd932379ef.name = 'Bullfight'
SET perf_5ddd932379ef.duration = '11:08'
SET perf_5ddd932379ef.source = 'musicbrainz.org'
SET perf_5ddd932379ef.timestamp = timestamp()

MERGE (perf_0905d963fd04:Performance{ uuid: '0ed14c8c-5c69-4d62-aacf-0905d963fd04' })
SET perf_0905d963fd04.name = 'Quiet Fire'
SET perf_0905d963fd04.duration = '8:14'
SET perf_0905d963fd04.source = 'musicbrainz.org'
SET perf_0905d963fd04.timestamp = timestamp()

MERGE (perf_fe387b8c3b8f:Performance{ uuid: 'bcd3e532-61f7-4278-8455-fe387b8c3b8f' })
SET perf_fe387b8c3b8f.name = 'Processional'
SET perf_fe387b8c3b8f.duration = '5:24'
SET perf_fe387b8c3b8f.source = 'musicbrainz.org'
SET perf_fe387b8c3b8f.timestamp = timestamp()

MERGE (perf_3e11ee1cc728:Performance{ uuid: 'b2bdea63-1aa0-49a7-9ced-3e11ee1cc728' })
SET perf_3e11ee1cc728.name = 'Sweet Song'
SET perf_3e11ee1cc728.duration = '6:19'
SET perf_3e11ee1cc728.source = 'musicbrainz.org'
SET perf_3e11ee1cc728.timestamp = timestamp()

MERGE (perf_c8df8cf41d25:Performance{ uuid: '8aa3ae07-2d18-4e8d-912a-c8df8cf41d25' })
SET perf_c8df8cf41d25.name = 'Vistalite'
SET perf_c8df8cf41d25.duration = '5:55'
SET perf_c8df8cf41d25.begin = '1978-07-12'
SET perf_c8df8cf41d25.end = '1978-07-12'
SET perf_c8df8cf41d25.source = 'musicbrainz.org'
SET perf_c8df8cf41d25.timestamp = timestamp()

MERGE (perf_7878d4c76ad2:Performance{ uuid: 'a0deee26-de71-4d11-8270-7878d4c76ad2' })
SET perf_7878d4c76ad2.name = 'More Pain Than Purpose'
SET perf_7878d4c76ad2.duration = '5:42'
SET perf_7878d4c76ad2.begin = '1978-07-12'
SET perf_7878d4c76ad2.end = '1978-07-12'
SET perf_7878d4c76ad2.source = 'musicbrainz.org'
SET perf_7878d4c76ad2.timestamp = timestamp()

MERGE (perf_cc55f524d4dd:Performance{ uuid: '5e33bf59-1234-4be3-8664-cc55f524d4dd' })
SET perf_cc55f524d4dd.name = 'Wonderin’'
SET perf_cc55f524d4dd.duration = '4:06'
SET perf_cc55f524d4dd.begin = '1978-07-20'
SET perf_cc55f524d4dd.end = '1978-07-20'
SET perf_cc55f524d4dd.source = 'musicbrainz.org'
SET perf_cc55f524d4dd.timestamp = timestamp()

MERGE (perf_a7d56571a164:Performance{ uuid: '16ede158-fde8-421a-b1e2-a7d56571a164' })
SET perf_a7d56571a164.name = 'Venus Eyes'
SET perf_a7d56571a164.duration = '4:39'
SET perf_a7d56571a164.begin = '1978-07-12'
SET perf_a7d56571a164.end = '1978-07-12'
SET perf_a7d56571a164.source = 'musicbrainz.org'
SET perf_a7d56571a164.timestamp = timestamp()

MERGE (perf_f56544069f50:Performance{ uuid: 'ad929ef0-0f7d-4009-b766-f56544069f50' })
SET perf_f56544069f50.name = 'Rok Out'
SET perf_f56544069f50.duration = '6:32'
SET perf_f56544069f50.begin = '1978-07-12'
SET perf_f56544069f50.end = '1978-07-12'
SET perf_f56544069f50.source = 'musicbrainz.org'
SET perf_f56544069f50.timestamp = timestamp()

MERGE (perf_a00999496098:Performance{ uuid: '87ef3152-e4e8-49fe-8969-a00999496098' })
SET perf_a00999496098.name = 'Water Children'
SET perf_a00999496098.duration = '6:42'
SET perf_a00999496098.begin = '1978-07-20'
SET perf_a00999496098.end = '1978-07-20'
SET perf_a00999496098.source = 'musicbrainz.org'
SET perf_a00999496098.timestamp = timestamp()

MERGE (perf_444c14964ef5:Performance{ uuid: 'c2450f1f-2da6-4f89-a34c-444c14964ef5' })
SET perf_444c14964ef5.name = 'Invitation'
SET perf_444c14964ef5.duration = '6:02'
SET perf_444c14964ef5.begin = '1978-07-12'
SET perf_444c14964ef5.end = '1978-07-12'
SET perf_444c14964ef5.source = 'musicbrainz.org'
SET perf_444c14964ef5.timestamp = timestamp()



// labels
MERGE (release_3bbb7af52e4e)-[:HAS_LABEL]->(label_b3591da0e289)


// tracks
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_e33d873d572d)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_5ddd932379ef)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_0905d963fd04)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_fe387b8c3b8f)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_3e11ee1cc728)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_c8df8cf41d25)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_7878d4c76ad2)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_cc55f524d4dd)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_a7d56571a164)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_f56544069f50)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '11', sequence: 11}]->(perf_a00999496098)
MERGE (release_3bbb7af52e4e)-[:HAS_TRACK {name: '12', sequence: 12}]->(perf_444c14964ef5)

// works

MERGE (person_6dc142afdb48:Person{ uuid: 'b7d69ea7-2f72-43cf-881b-6dc142afdb48' }) 
SET person_6dc142afdb48.name = 'Paul Francis Webster'
SET person_6dc142afdb48.gender = 'Male'
SET person_6dc142afdb48.country = 'US'
SET person_6dc142afdb48.allmusic = 'https://www.allmusic.com/artist/mn0000751096'
SET person_6dc142afdb48.discogs = 'https://www.discogs.com/artist/290092'
SET person_6dc142afdb48.imdb = 'https://www.imdb.com/name/nm0916990/'
SET person_6dc142afdb48.viaf = 'http://viaf.org/viaf/42031713'
SET person_6dc142afdb48.wikidata = 'https://www.wikidata.org/wiki/Q1620897'
SET person_6dc142afdb48.databases = ['http://d-nb.info/gnd/130174289', 'http://id.loc.gov/authorities/names/n85273911', 'https://catalogue.bnf.fr/ark:/12148/cb14839021v', 'https://ibdb.com/person.php?id=12555', 'http://snaccooperative.org/ark:/99166/w6hv020x', 'https://rateyourmusic.com/artist/paul_francis_webster', 'https://www.worldcat.org/identities/lccn-n85273911']
SET person_6dc142afdb48.musicbrainz = 'https://musicbrainz.org/artist/b7d69ea7-2f72-43cf-881b-6dc142afdb48'
SET person_6dc142afdb48.isni_list = ['http://isni.org/isni/0000000081210130']
SET person_6dc142afdb48.source = 'musicbrainz.org'
SET person_6dc142afdb48.timestamp = timestamp()

MERGE (person_6b36e322507b:Person{ uuid: 'cdc82126-9892-4bed-864d-6b36e322507b' }) 
SET person_6b36e322507b.name = 'Bronisław Kaper'
SET person_6b36e322507b.gender = 'Male'
SET person_6b36e322507b.country = 'US'
SET person_6b36e322507b.allmusic = 'https://www.allmusic.com/artist/mn0003217868'
SET person_6b36e322507b.discogs = 'https://www.discogs.com/artist/715404'
SET person_6b36e322507b.imdb = 'https://www.imdb.com/name/nm0006147/'
SET person_6b36e322507b.viaf = 'http://viaf.org/viaf/59273738'
SET person_6b36e322507b.wikidata = 'https://www.wikidata.org/wiki/Q927472'
SET person_6b36e322507b.databases = ['http://d-nb.info/gnd/130206156', 'http://id.loc.gov/authorities/names/n79075647', 'https://catalogue.bnf.fr/ark:/12148/cb139401963', 'https://nla.gov.au/nla.party-1082410', 'http://soundtrackcollector.com/composer/88/', 'https://www.ibdb.com/person.php?id=11976', 'https://www.worldcat.org/identities/lccn-n79075647']
SET person_6b36e322507b.musicbrainz = 'https://musicbrainz.org/artist/cdc82126-9892-4bed-864d-6b36e322507b'
SET person_6b36e322507b.isni_list = ['http://isni.org/isni/0000000121351385']
SET person_6b36e322507b.source = 'musicbrainz.org'
SET person_6b36e322507b.timestamp = timestamp()

MERGE (work_c66457806795:Work{ uuid: '2c0204b1-5eb0-3880-a3c6-c66457806795' })
SET work_c66457806795.name = 'Invitation'
SET work_c66457806795.iswc = 'T-070.906.798-0'
SET work_c66457806795.type = 'Song'
SET work_c66457806795.wikidata = 'https://www.wikidata.org/wiki/Q21072671'
SET work_c66457806795.musicbrainz = 'https://musicbrainz.org/work/2c0204b1-5eb0-3880-a3c6-c66457806795'
SET work_c66457806795.source = 'musicbrainz.org'
SET work_c66457806795.timestamp = timestamp()


// performances of
MERGE (perf_444c14964ef5)-[:PERFORMANCE_OF]->(work_c66457806795)


// composers
MERGE (person_6b36e322507b)-[:COMPOSED]->(work_c66457806795)
MERGE (person_6dc142afdb48)-[:WROTE_LYRICS]->(work_c66457806795)


// place nodes

MERGE (place_ed799acd07f4:Place{ uuid: '2dcf4314-71a2-421f-ba77-ed799acd07f4' })
SET place_ed799acd07f4.name = 'Fantasy Studios'
SET place_ed799acd07f4.source = 'musicbrainz.org'


// place relationships
MERGE (perf_c8df8cf41d25)-[:HAS_PLACE { type: 'recorded at', begin: '1978-07-12', end: '1978-07-12' }]->(place_ed799acd07f4)
MERGE (perf_7878d4c76ad2)-[:HAS_PLACE { type: 'recorded at', begin: '1978-07-12', end: '1978-07-12' }]->(place_ed799acd07f4)
MERGE (perf_cc55f524d4dd)-[:HAS_PLACE { type: 'recorded at', begin: '1978-07-20', end: '1978-07-20' }]->(place_ed799acd07f4)
MERGE (perf_a7d56571a164)-[:HAS_PLACE { type: 'recorded at', begin: '1978-07-12', end: '1978-07-12' }]->(place_ed799acd07f4)
MERGE (perf_f56544069f50)-[:HAS_PLACE { type: 'recorded at', begin: '1978-07-12', end: '1978-07-12' }]->(place_ed799acd07f4)
MERGE (perf_a00999496098)-[:HAS_PLACE { type: 'recorded at', begin: '1978-07-20', end: '1978-07-20' }]->(place_ed799acd07f4)
MERGE (perf_444c14964ef5)-[:HAS_PLACE { type: 'recorded at', begin: '1978-07-12', end: '1978-07-12' }]->(place_ed799acd07f4)

MERGE (person_41d78c725ce3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric piano'] }]->(perf_e33d873d572d)
MERGE (person_8fe19080caaf)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_e33d873d572d)
MERGE (person_ac19da0b921c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_e33d873d572d)
MERGE (person_e044666c4828)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e33d873d572d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e33d873d572d)
MERGE (person_20039cafef7b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e33d873d572d)
MERGE (person_41d78c725ce3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric piano'] }]->(perf_5ddd932379ef)
MERGE (person_823edc2a7c02)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_5ddd932379ef)
MERGE (person_8fe19080caaf)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_5ddd932379ef)
MERGE (person_da3f335093a1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5ddd932379ef)
MERGE (person_15c58dce8f26)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_5ddd932379ef)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_5ddd932379ef)
MERGE (person_22a5fbaaf713)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_5ddd932379ef)
MERGE (person_20039cafef7b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_5ddd932379ef)
MERGE (person_41d78c725ce3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano', 'electric piano'] }]->(perf_0905d963fd04)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_0905d963fd04)
MERGE (person_22a5fbaaf713)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_0905d963fd04)
MERGE (person_15c58dce8f26)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_0905d963fd04)
MERGE (person_20039cafef7b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_0905d963fd04)
MERGE (person_41d78c725ce3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric piano'] }]->(perf_fe387b8c3b8f)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_fe387b8c3b8f)
MERGE (person_15c58dce8f26)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_fe387b8c3b8f)
MERGE (person_20039cafef7b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_fe387b8c3b8f)
MERGE (person_41d78c725ce3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric piano'] }]->(perf_3e11ee1cc728)
MERGE (person_f180a2b2aaf0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_3e11ee1cc728)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_3e11ee1cc728)
MERGE (person_8fe19080caaf)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_3e11ee1cc728)
MERGE (person_22a5fbaaf713)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_3e11ee1cc728)
MERGE (person_20039cafef7b)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_3e11ee1cc728)
MERGE (person_f180a2b2aaf0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric piano'] }]->(perf_c8df8cf41d25)
MERGE (person_823edc2a7c02)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_c8df8cf41d25)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)', 'bell tree'] }]->(perf_c8df8cf41d25)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_c8df8cf41d25)
MERGE (person_2099544918fe)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric bass guitar'] }]->(perf_c8df8cf41d25)
MERGE (person_15c58dce8f26)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_c8df8cf41d25)
MERGE (person_994c0b94aa4d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute'] }]->(perf_c8df8cf41d25)
MERGE (person_f180a2b2aaf0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_7878d4c76ad2)
MERGE (person_823edc2a7c02)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_7878d4c76ad2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)', 'bell tree'] }]->(perf_7878d4c76ad2)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_7878d4c76ad2)
MERGE (person_2099544918fe)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric bass guitar'] }]->(perf_7878d4c76ad2)
MERGE (person_994c0b94aa4d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute'] }]->(perf_7878d4c76ad2)
MERGE (person_41d78c725ce3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric piano'] }]->(perf_cc55f524d4dd)
MERGE (person_f180a2b2aaf0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric piano'] }]->(perf_cc55f524d4dd)
MERGE (person_823edc2a7c02)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_cc55f524d4dd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_cc55f524d4dd)
MERGE (person_22a5fbaaf713)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_cc55f524d4dd)
MERGE (person_15c58dce8f26)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_cc55f524d4dd)
MERGE (person_f180a2b2aaf0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric piano'] }]->(perf_a7d56571a164)
MERGE (person_823edc2a7c02)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_a7d56571a164)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a7d56571a164)
MERGE (person_2099544918fe)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric bass guitar'] }]->(perf_a7d56571a164)
MERGE (person_15c58dce8f26)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tambourine'] }]->(perf_a7d56571a164)
MERGE (person_994c0b94aa4d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_a7d56571a164)
MERGE (person_823edc2a7c02)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_f56544069f50)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f56544069f50)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_f56544069f50)
MERGE (person_2099544918fe)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric bass guitar'] }]->(perf_f56544069f50)
MERGE (person_15c58dce8f26)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['cowbell'] }]->(perf_f56544069f50)
MERGE (person_994c0b94aa4d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_f56544069f50)
MERGE (person_41d78c725ce3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a00999496098)
MERGE (person_823edc2a7c02)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_a00999496098)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a00999496098)
MERGE (person_da3f335093a1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric piano'] }]->(perf_a00999496098)
MERGE (person_22a5fbaaf713)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_a00999496098)
MERGE (person_15c58dce8f26)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_a00999496098)
MERGE (person_f180a2b2aaf0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_444c14964ef5)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_444c14964ef5)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_444c14964ef5)
MERGE (person_2099544918fe)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['electric bass guitar'] }]->(perf_444c14964ef5)

