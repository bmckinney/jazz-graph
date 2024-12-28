
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_0126620dd0ef:Release{ uuid: '78d73308-5c39-4967-b584-0126620dd0ef' })
SET release_0126620dd0ef.name = 'Osaka Concert, Vol. 2'
SET release_0126620dd0ef.country = 'DK'
SET release_0126620dd0ef.date = '1987'
SET release_0126620dd0ef.format = 'CD'
SET release_0126620dd0ef.discode = 'SCCD-30002'
SET release_0126620dd0ef.discogs = 'https://www.discogs.com/release/11274468'
SET release_0126620dd0ef.musicbrainz = 'http://musicbrainz.org/release/78d73308-5c39-4967-b584-0126620dd0ef'
SET release_0126620dd0ef.source = 'musicbrainz.org'


MERGE (person_6265ca93cbb7:Person{ uuid: 'd0b291c3-256e-42c0-b855-6265ca93cbb7' }) 
SET person_6265ca93cbb7.name = 'Duke Jordan Trio'
SET person_6265ca93cbb7.discogs = 'https://www.discogs.com/artist/1593139'
SET person_6265ca93cbb7.wikidata = 'https://www.wikidata.org/wiki/Q110987590'
SET person_6265ca93cbb7.musicbrainz = 'https://musicbrainz.org/artist/d0b291c3-256e-42c0-b855-6265ca93cbb7'
SET person_6265ca93cbb7.source = 'musicbrainz.org'


MERGE (person_e9a9d7c21236:Person{ uuid: 'f2261901-d6d8-4293-b6a9-e9a9d7c21236' }) 
SET person_e9a9d7c21236.name = 'Nils Winther'
SET person_e9a9d7c21236.gender = 'Male'
SET person_e9a9d7c21236.country = 'DK'
SET person_e9a9d7c21236.discogs = 'https://www.discogs.com/artist/266539'
SET person_e9a9d7c21236.musicbrainz = 'https://musicbrainz.org/artist/f2261901-d6d8-4293-b6a9-e9a9d7c21236'
SET person_e9a9d7c21236.source = 'musicbrainz.org'


MERGE (person_558229fbfdd2:Person{ uuid: '18288a13-0259-4a44-a9dc-558229fbfdd2' }) 
SET person_558229fbfdd2.name = 'Duke Jordan'
SET person_558229fbfdd2.gender = 'Male'
SET person_558229fbfdd2.country = 'DK'
SET person_558229fbfdd2.allmusic = 'https://www.allmusic.com/artist/mn0000147245'
SET person_558229fbfdd2.discogs = 'https://www.discogs.com/artist/272016'
SET person_558229fbfdd2.viaf = 'http://viaf.org/viaf/84969788'
SET person_558229fbfdd2.wikidata = 'https://www.wikidata.org/wiki/Q1264406'
SET person_558229fbfdd2.wikipedia = 'https://en.wikipedia.org/wiki/Duke_Jordan'
SET person_558229fbfdd2.databases = ['http://d-nb.info/gnd/119146096', 'http://id.loc.gov/authorities/names/n83231137', 'https://catalogue.bnf.fr/ark:/12148/cb13895757x', 'http://snaccooperative.org/ark:/99166/w6cv606t', 'https://www.worldcat.org/identities/lccn-n83231137']
SET person_558229fbfdd2.musicbrainz = 'https://musicbrainz.org/artist/18288a13-0259-4a44-a9dc-558229fbfdd2'
SET person_558229fbfdd2.isni_list = ['http://isni.org/isni/0000000078397141']
SET person_558229fbfdd2.source = 'musicbrainz.org'


MERGE (person_ac59cbd82246:Person{ uuid: 'f3edba06-dad2-4916-98da-ac59cbd82246' }) 
SET person_ac59cbd82246.name = 'Wilbur Little'
SET person_ac59cbd82246.gender = 'Male'
SET person_ac59cbd82246.country = 'US'
SET person_ac59cbd82246.allmusic = 'https://www.allmusic.com/artist/mn0000845025'
SET person_ac59cbd82246.discogs = 'https://www.discogs.com/artist/634055'
SET person_ac59cbd82246.viaf = 'http://viaf.org/viaf/76500764'
SET person_ac59cbd82246.wikidata = 'https://www.wikidata.org/wiki/Q950919'
SET person_ac59cbd82246.wikipedia = 'https://en.wikipedia.org/wiki/Wilbur_Little'
SET person_ac59cbd82246.databases = ['http://d-nb.info/gnd/135240395', 'http://id.loc.gov/authorities/names/no99082008', 'https://catalogue.bnf.fr/ark:/12148/cb138967126', 'https://www.worldcat.org/identities/lccn-no99082008']
SET person_ac59cbd82246.musicbrainz = 'https://musicbrainz.org/artist/f3edba06-dad2-4916-98da-ac59cbd82246'
SET person_ac59cbd82246.isni_list = ['http://isni.org/isni/0000000055151835']
SET person_ac59cbd82246.source = 'musicbrainz.org'


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

// labels

MERGE (label_fc139ddfa883:Label{ uuid: 'a04e05cf-189c-4095-9d78-fc139ddfa883' })
SET label_fc139ddfa883.name= 'SteepleChase'

// performances

MERGE (perf_033651fc47a6:Performance{ uuid: '0070e095-b977-4f98-8974-033651fc47a6' })
SET perf_033651fc47a6.name = 'Two Loves'
SET perf_033651fc47a6.duration = '3:25'
SET perf_033651fc47a6.begin_date = '1976-09-20'
SET perf_033651fc47a6.end_date = '1976-09-20'
SET perf_033651fc47a6.source = 'musicbrainz.org'


MERGE (perf_41c32eda1bcd:Performance{ uuid: 'f51c7e71-aac7-49bd-b9c9-41c32eda1bcd' })
SET perf_41c32eda1bcd.name = 'In My Solitude'
SET perf_41c32eda1bcd.duration = '3:40'
SET perf_41c32eda1bcd.begin_date = '1976-09-20'
SET perf_41c32eda1bcd.end_date = '1976-09-20'
SET perf_41c32eda1bcd.source = 'musicbrainz.org'


MERGE (perf_e3f2e88fb9ef:Performance{ uuid: 'f004ccd3-1210-42d1-a733-e3f2e88fb9ef' })
SET perf_e3f2e88fb9ef.name = 'No Problem'
SET perf_e3f2e88fb9ef.duration = '10:48'
SET perf_e3f2e88fb9ef.begin_date = '1976-09-20'
SET perf_e3f2e88fb9ef.end_date = '1976-09-20'
SET perf_e3f2e88fb9ef.source = 'musicbrainz.org'


MERGE (perf_18e3a0f0e8db:Performance{ uuid: 'dbcfe2f6-888f-4d18-b475-18e3a0f0e8db' })
SET perf_18e3a0f0e8db.name = 'There’s a Star for You'
SET perf_18e3a0f0e8db.duration = '7:07'
SET perf_18e3a0f0e8db.begin_date = '1976-09-20'
SET perf_18e3a0f0e8db.end_date = '1976-09-20'
SET perf_18e3a0f0e8db.source = 'musicbrainz.org'


MERGE (perf_9d3ae87c965a:Performance{ uuid: 'fb37747b-0edc-4960-85d5-9d3ae87c965a' })
SET perf_9d3ae87c965a.name = 'Misty Thursday'
SET perf_9d3ae87c965a.duration = '5:03'
SET perf_9d3ae87c965a.begin_date = '1976-09-20'
SET perf_9d3ae87c965a.end_date = '1976-09-20'
SET perf_9d3ae87c965a.source = 'musicbrainz.org'


MERGE (perf_54581849bb9a:Performance{ uuid: '133be159-2a7d-4526-af0d-54581849bb9a' })
SET perf_54581849bb9a.name = 'Cold Bordeaux Blues'
SET perf_54581849bb9a.duration = '6:46'
SET perf_54581849bb9a.begin_date = '1976-09-20'
SET perf_54581849bb9a.end_date = '1976-09-20'
SET perf_54581849bb9a.source = 'musicbrainz.org'


MERGE (perf_4d68cffb9f72:Performance{ uuid: 'f1538795-dd6e-4d21-b87e-4d68cffb9f72' })
SET perf_4d68cffb9f72.name = 'Lady Linda'
SET perf_4d68cffb9f72.duration = '3:39'
SET perf_4d68cffb9f72.begin_date = '1976-09-20'
SET perf_4d68cffb9f72.end_date = '1976-09-20'
SET perf_4d68cffb9f72.source = 'musicbrainz.org'


MERGE (perf_651fe2145f44:Performance{ uuid: 'a8b09b76-c745-4db3-89fd-651fe2145f44' })
SET perf_651fe2145f44.name = 'Forecast'
SET perf_651fe2145f44.duration = '5:24'
SET perf_651fe2145f44.begin_date = '1976-09-20'
SET perf_651fe2145f44.end_date = '1976-09-20'
SET perf_651fe2145f44.source = 'musicbrainz.org'


MERGE (perf_0dee32b97735:Performance{ uuid: '5274faee-c4e6-459d-b15b-0dee32b97735' })
SET perf_0dee32b97735.name = 'Cherokee'
SET perf_0dee32b97735.duration = '11:07'
SET perf_0dee32b97735.begin_date = '1976-09-20'
SET perf_0dee32b97735.end_date = '1976-09-20'
SET perf_0dee32b97735.source = 'musicbrainz.org'


MERGE (perf_e9ba71d106fe:Performance{ uuid: 'd3cb497d-faf3-4e56-b2d2-e9ba71d106fe' })
SET perf_e9ba71d106fe.name = 'Jordu'
SET perf_e9ba71d106fe.duration = '3:26'
SET perf_e9ba71d106fe.begin_date = '1976-09-20'
SET perf_e9ba71d106fe.end_date = '1976-09-20'
SET perf_e9ba71d106fe.source = 'musicbrainz.org'


MERGE (perf_5f8bba5660f7:Performance{ uuid: '54779ca8-cea0-47c9-a576-5f8bba5660f7' })
SET perf_5f8bba5660f7.name = 'Flight to Japan'
SET perf_5f8bba5660f7.duration = '1:03'
SET perf_5f8bba5660f7.begin_date = '1976-09-20'
SET perf_5f8bba5660f7.end_date = '1976-09-20'
SET perf_5f8bba5660f7.source = 'musicbrainz.org'




// labels
MERGE (release_0126620dd0ef)-[:HAS_LABEL]->(label_fc139ddfa883)


// tracks
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_033651fc47a6)
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_41c32eda1bcd)
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_e3f2e88fb9ef)
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_18e3a0f0e8db)
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_9d3ae87c965a)
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_54581849bb9a)
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_4d68cffb9f72)
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_651fe2145f44)
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_0dee32b97735)
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_e9ba71d106fe)
MERGE (release_0126620dd0ef)-[:HAS_TRACK {name: '11', sequence: 11}]->(perf_5f8bba5660f7)

// works

MERGE (person_4e98168f002f:Person{ uuid: '716a01fc-da79-41b8-816c-4e98168f002f' }) 
SET person_4e98168f002f.name = 'Ray Noble'
SET person_4e98168f002f.gender = 'Male'
SET person_4e98168f002f.country = 'GB'
SET person_4e98168f002f.allmusic = 'https://www.allmusic.com/artist/mn0000034769'
SET person_4e98168f002f.discogs = 'https://www.discogs.com/artist/503363'
SET person_4e98168f002f.imdb = 'https://www.imdb.com/name/nm0633656/'
SET person_4e98168f002f.viaf = 'http://viaf.org/viaf/37102927'
SET person_4e98168f002f.wikidata = 'https://www.wikidata.org/wiki/Q953019'
SET person_4e98168f002f.databases = ['http://d-nb.info/gnd/119161761', 'http://id.loc.gov/authorities/names/n80063207', 'https://catalogue.bnf.fr/ark:/12148/cb13897993t', 'http://snaccooperative.org/ark:/99166/w6hb28dc', 'https://nla.gov.au/nla.party-1526110', 'https://rateyourmusic.com/artist/ray_noble', 'https://www.worldcat.org/identities/lccn-n80063207']
SET person_4e98168f002f.musicbrainz = 'https://musicbrainz.org/artist/716a01fc-da79-41b8-816c-4e98168f002f'
SET person_4e98168f002f.isni_list = ['http://isni.org/isni/0000000081161439']
SET person_4e98168f002f.source = 'musicbrainz.org'


MERGE (person_b87fc4c00cc8:Person{ uuid: 'e6def1e6-d9a8-4700-a520-b87fc4c00cc8' }) 
SET person_b87fc4c00cc8.name = 'Eddie DeLange'
SET person_b87fc4c00cc8.gender = 'Male'
SET person_b87fc4c00cc8.country = 'US'
SET person_b87fc4c00cc8.allmusic = 'https://www.allmusic.com/artist/mn0000079849'
SET person_b87fc4c00cc8.discogs = 'https://www.discogs.com/artist/657340'
SET person_b87fc4c00cc8.viaf = 'http://viaf.org/viaf/46970792'
SET person_b87fc4c00cc8.wikidata = 'https://www.wikidata.org/wiki/Q363281'
SET person_b87fc4c00cc8.databases = ['http://d-nb.info/gnd/119385899', 'http://id.loc.gov/authorities/names/n93105687', 'https://catalogue.bnf.fr/ark:/12148/cb14169839j', 'http://snaccooperative.org/ark:/99166/w6p12ppc', 'https://nla.gov.au/nla.party-884996', 'https://rateyourmusic.com/artist/eddie_de_lange', 'https://www.ibdb.com/person.php?id=88729', 'https://www.worldcat.org/identities/lccn-n93105687/']
SET person_b87fc4c00cc8.musicbrainz = 'https://musicbrainz.org/artist/e6def1e6-d9a8-4700-a520-b87fc4c00cc8'
SET person_b87fc4c00cc8.isni_list = ['http://isni.org/isni/0000000107807737']
SET person_b87fc4c00cc8.source = 'musicbrainz.org'


MERGE (person_1ef2fece51ce:Person{ uuid: '2a2bf494-ac80-4ac9-901f-1ef2fece51ce' }) 
SET person_1ef2fece51ce.name = 'Irving Mills'
SET person_1ef2fece51ce.gender = 'Male'
SET person_1ef2fece51ce.country = 'US'
SET person_1ef2fece51ce.allmusic = 'https://www.allmusic.com/artist/mn0000084993'
SET person_1ef2fece51ce.discogs = 'https://www.discogs.com/artist/307446'
SET person_1ef2fece51ce.imdb = 'https://www.imdb.com/name/nm0590030/'
SET person_1ef2fece51ce.viaf = 'http://viaf.org/viaf/76500944'
SET person_1ef2fece51ce.wikidata = 'https://www.wikidata.org/wiki/Q1292110'
SET person_1ef2fece51ce.databases = ['http://d-nb.info/gnd/135465664', 'http://id.loc.gov/authorities/names/n88621778', 'https://catalogue.bnf.fr/ark:/12148/cb13897535j', 'https://ibdb.com/person.php?id=83868', 'http://snaccooperative.org/ark:/99166/w6f50280', 'https://nla.gov.au/nla.party-1528202', 'https://rateyourmusic.com/artist/irving_mills', 'https://www.worldcat.org/identities/lccn-n88621778/']
SET person_1ef2fece51ce.musicbrainz = 'https://musicbrainz.org/artist/2a2bf494-ac80-4ac9-901f-1ef2fece51ce'
SET person_1ef2fece51ce.isni_list = ['http://isni.org/isni/0000000081569522']
SET person_1ef2fece51ce.source = 'musicbrainz.org'


MERGE (person_7eeeb45e411f:Person{ uuid: '3af06bc4-68ad-4cae-bb7a-7eeeb45e411f' }) 
SET person_7eeeb45e411f.name = 'Duke Ellington'
SET person_7eeeb45e411f.gender = 'Male'
SET person_7eeeb45e411f.disambiguation = 'US composer, pianist & jazz bandleader'
SET person_7eeeb45e411f.country = 'US'
SET person_7eeeb45e411f.allmusic = 'https://www.allmusic.com/artist/mn0000120323'
SET person_7eeeb45e411f.bbc = 'https://www.bbc.co.uk/music/artists/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.discogs = 'https://www.discogs.com/artist/145257'
SET person_7eeeb45e411f.imdb = 'https://www.imdb.com/name/nm0254153/'
SET person_7eeeb45e411f.viaf = 'http://viaf.org/viaf/66651610'
SET person_7eeeb45e411f.wikidata = 'https://www.wikidata.org/wiki/Q4030'
SET person_7eeeb45e411f.databases = ['http://d-nb.info/gnd/118529994', 'http://id.loc.gov/authorities/names/n50080187', 'https://catalogue.bnf.fr/ark:/12148/cb13893638w', 'https://ibdb.com/person.php?id=11631', 'http://snaccooperative.org/ark:/99166/w6639nkm', 'https://nla.gov.au/nla.party-815399', 'https://openlibrary.org/works/OL1953949A', 'https://rateyourmusic.com/artist/duke_ellington', 'https://www.worldcat.org/identities/lccn-n50080187/']
SET person_7eeeb45e411f.musicbrainz = 'https://musicbrainz.org/artist/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.isni_list = ['http://isni.org/isni/0000000109110810']
SET person_7eeeb45e411f.source = 'musicbrainz.org'


MERGE (work_deed2cb0ceaa:Work{ uuid: '945070ce-3f47-3c6c-9d2c-deed2cb0ceaa' })
SET work_deed2cb0ceaa.name = 'Cherokee'
SET work_deed2cb0ceaa.iswc = 'T-010.433.944-7'
SET work_deed2cb0ceaa.wikidata = 'https://www.wikidata.org/wiki/Q1070310'
SET work_deed2cb0ceaa.musicbrainz = 'https://musicbrainz.org/work/945070ce-3f47-3c6c-9d2c-deed2cb0ceaa'
SET work_deed2cb0ceaa.source = 'musicbrainz.org'


MERGE (work_7c52134b61a5:Work{ uuid: '54f9a704-dd4e-4018-9e6b-7c52134b61a5' })
SET work_7c52134b61a5.name = 'Jordu'
SET work_7c52134b61a5.iswc = 'T-070.241.379-3'
SET work_7c52134b61a5.type = 'Song'
SET work_7c52134b61a5.wikidata = 'https://www.wikidata.org/wiki/Q6277539'
SET work_7c52134b61a5.musicbrainz = 'https://musicbrainz.org/work/54f9a704-dd4e-4018-9e6b-7c52134b61a5'
SET work_7c52134b61a5.source = 'musicbrainz.org'


MERGE (work_7f14a91d7df2:Work{ uuid: '9069d72a-6c01-3f23-b996-7f14a91d7df2' })
SET work_7f14a91d7df2.name = '(In My) Solitude'
SET work_7f14a91d7df2.iswc = 'T-071.070.380-2'
SET work_7f14a91d7df2.type = 'Song'
SET work_7f14a91d7df2.wikidata = 'https://www.wikidata.org/wiki/Q833563'
SET work_7f14a91d7df2.musicbrainz = 'https://musicbrainz.org/work/9069d72a-6c01-3f23-b996-7f14a91d7df2'
SET work_7f14a91d7df2.source = 'musicbrainz.org'



// performances of
MERGE (perf_0dee32b97735)-[:PERFORMANCE_OF]->(work_deed2cb0ceaa)
MERGE (perf_e9ba71d106fe)-[:PERFORMANCE_OF]->(work_7c52134b61a5)
MERGE (perf_41c32eda1bcd)-[:PERFORMANCE_OF]->(work_7f14a91d7df2)


// composers
MERGE (person_4e98168f002f)-[:COMPOSED]->(work_deed2cb0ceaa)
MERGE (person_4e98168f002f)-[:WROTE_LYRICS]->(work_deed2cb0ceaa)
MERGE (person_558229fbfdd2)-[:COMPOSED]->(work_7c52134b61a5)
MERGE (person_7eeeb45e411f)-[:COMPOSED]->(work_7f14a91d7df2)
MERGE (person_b87fc4c00cc8)-[:WROTE_LYRICS]->(work_7f14a91d7df2)
MERGE (person_1ef2fece51ce)-[:WROTE_LYRICS]->(work_7f14a91d7df2)


// place nodes

MERGE (place_fa09286dc6d5:Place{ uuid: '90be9117-b054-4271-b64c-fa09286dc6d5' })
SET place_fa09286dc6d5.name = 'サンケイホールブリーゼ'
SET place_fa09286dc6d5.source = 'musicbrainz.org'


// place relationships
MERGE (perf_033651fc47a6)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)
MERGE (perf_41c32eda1bcd)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)
MERGE (perf_e3f2e88fb9ef)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)
MERGE (perf_18e3a0f0e8db)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)
MERGE (perf_9d3ae87c965a)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)
MERGE (perf_54581849bb9a)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)
MERGE (perf_4d68cffb9f72)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)
MERGE (perf_651fe2145f44)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)
MERGE (perf_0dee32b97735)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)
MERGE (perf_e9ba71d106fe)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)
MERGE (perf_5f8bba5660f7)-[:HAS_PLACE { type: 'recorded at', begin_date: '1976-09-20', end_date: '1976-09-20' }]->(place_fa09286dc6d5)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_033651fc47a6)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_033651fc47a6)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_033651fc47a6)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_033651fc47a6)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_41c32eda1bcd)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_41c32eda1bcd)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_41c32eda1bcd)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_41c32eda1bcd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e3f2e88fb9ef)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e3f2e88fb9ef)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e3f2e88fb9ef)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e3f2e88fb9ef)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_18e3a0f0e8db)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_18e3a0f0e8db)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_18e3a0f0e8db)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_18e3a0f0e8db)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9d3ae87c965a)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_9d3ae87c965a)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_9d3ae87c965a)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_9d3ae87c965a)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_54581849bb9a)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_54581849bb9a)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_54581849bb9a)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_54581849bb9a)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_4d68cffb9f72)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_4d68cffb9f72)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_4d68cffb9f72)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_4d68cffb9f72)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_651fe2145f44)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_651fe2145f44)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_651fe2145f44)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_651fe2145f44)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_0dee32b97735)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_0dee32b97735)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_0dee32b97735)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_0dee32b97735)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e9ba71d106fe)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e9ba71d106fe)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e9ba71d106fe)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e9ba71d106fe)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_5f8bba5660f7)
MERGE (person_558229fbfdd2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5f8bba5660f7)
MERGE (person_ac59cbd82246)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_5f8bba5660f7)
MERGE (person_e9a9d7c21236)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_5f8bba5660f7)



"""
)