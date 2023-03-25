// releases

MERGE (release_966fc4f493a8:Release{ uuid: 'f3ccbf09-08b6-465f-833c-966fc4f493a8' })
SET release_966fc4f493a8.name = 'Thank You Thank You'
SET release_966fc4f493a8.country = 'US'
SET release_966fc4f493a8.date = '1977'
SET release_966fc4f493a8.format = '12" Vinyl'
SET release_966fc4f493a8.discode = 'GXY-5103'
SET release_966fc4f493a8.discogs = 'https://www.discogs.com/release/1350637'
SET release_966fc4f493a8.musicbrainz = 'http://musicbrainz.org/release/f3ccbf09-08b6-465f-833c-966fc4f493a8'
SET release_966fc4f493a8.source = 'musicbrainz.org'
SET release_966fc4f493a8.timestamp = timestamp()

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

MERGE (person_bb48278688a0:Person{ uuid: '6c9ca088-9da0-404f-ae61-bb48278688a0' }) 
SET person_bb48278688a0.name = 'Peter Knapp'
SET person_bb48278688a0.gender = 'Male'
SET person_bb48278688a0.disambiguation = 'bass'
SET person_bb48278688a0.discogs = 'https://www.discogs.com/artist/947179'
SET person_bb48278688a0.musicbrainz = 'https://musicbrainz.org/artist/6c9ca088-9da0-404f-ae61-bb48278688a0'
SET person_bb48278688a0.source = 'musicbrainz.org'
SET person_bb48278688a0.timestamp = timestamp()

MERGE (person_20039cafef7b:Person{ uuid: '56fbc674-7d57-4fc0-b36c-20039cafef7b' }) 
SET person_20039cafef7b.name = 'Ed Michel'
SET person_20039cafef7b.discogs = 'https://www.discogs.com/artist/166631'
SET person_20039cafef7b.imdb = 'https://www.imdb.com/name/nm2123705/'
SET person_20039cafef7b.wikidata = 'https://www.wikidata.org/wiki/Q92309803'
SET person_20039cafef7b.musicbrainz = 'https://musicbrainz.org/artist/56fbc674-7d57-4fc0-b36c-20039cafef7b'
SET person_20039cafef7b.source = 'musicbrainz.org'
SET person_20039cafef7b.timestamp = timestamp()

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

MERGE (person_823edc2a7c02:Person{ uuid: '5ca31148-6257-44eb-bb0d-823edc2a7c02' }) 
SET person_823edc2a7c02.name = 'Marcus Fiorillo'
SET person_823edc2a7c02.gender = 'Male'
SET person_823edc2a7c02.disambiguation = 'Jazz guitarist'
SET person_823edc2a7c02.discogs = 'https://www.discogs.com/artist/1282894'
SET person_823edc2a7c02.musicbrainz = 'https://musicbrainz.org/artist/5ca31148-6257-44eb-bb0d-823edc2a7c02'
SET person_823edc2a7c02.source = 'musicbrainz.org'
SET person_823edc2a7c02.timestamp = timestamp()

MERGE (person_3b8d23ba518a:Person{ uuid: '9a6358be-4223-40f5-a8ee-3b8d23ba518a' }) 
SET person_3b8d23ba518a.name = 'Baxter Fillmore'
SET person_3b8d23ba518a.discogs = 'https://www.discogs.com/artist/1488637'
SET person_3b8d23ba518a.musicbrainz = 'https://musicbrainz.org/artist/9a6358be-4223-40f5-a8ee-3b8d23ba518a'
SET person_3b8d23ba518a.source = 'musicbrainz.org'
SET person_3b8d23ba518a.timestamp = timestamp()

MERGE (person_ba539b0ef93c:Person{ uuid: '7cf86f47-fbb0-44a5-949e-ba539b0ef93c' }) 
SET person_ba539b0ef93c.name = 'Baker Bigsby'
SET person_ba539b0ef93c.gender = 'Male'
SET person_ba539b0ef93c.country = 'US'
SET person_ba539b0ef93c.discogs = 'https://www.discogs.com/artist/363563'
SET person_ba539b0ef93c.musicbrainz = 'https://musicbrainz.org/artist/7cf86f47-fbb0-44a5-949e-ba539b0ef93c'
SET person_ba539b0ef93c.source = 'musicbrainz.org'
SET person_ba539b0ef93c.timestamp = timestamp()

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

MERGE (person_15c58dce8f26:Person{ uuid: 'ba72fa6c-7fbc-42ca-b4a8-15c58dce8f26' }) 
SET person_15c58dce8f26.name = 'Kenneth Nash'
SET person_15c58dce8f26.gender = 'Male'
SET person_15c58dce8f26.discogs = 'https://www.discogs.com/artist/309767'
SET person_15c58dce8f26.musicbrainz = 'https://musicbrainz.org/artist/ba72fa6c-7fbc-42ca-b4a8-15c58dce8f26'
SET person_15c58dce8f26.source = 'musicbrainz.org'
SET person_15c58dce8f26.timestamp = timestamp()

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



// labels
MERGE (release_966fc4f493a8)-[:HAS_LABEL]->(label_b3591da0e289)


// tracks
MERGE (release_966fc4f493a8)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_e33d873d572d)
MERGE (release_966fc4f493a8)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_5ddd932379ef)
MERGE (release_966fc4f493a8)-[:HAS_TRACK {name: 'B1', sequence: 3}]->(perf_0905d963fd04)
MERGE (release_966fc4f493a8)-[:HAS_TRACK {name: 'B2', sequence: 4}]->(perf_fe387b8c3b8f)
MERGE (release_966fc4f493a8)-[:HAS_TRACK {name: 'B3', sequence: 5}]->(perf_3e11ee1cc728)

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

