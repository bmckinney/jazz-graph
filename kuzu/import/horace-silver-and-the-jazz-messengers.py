
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_8bb1c6ce5d28:Release{ uuid: '41f3eb80-e632-4e1e-8c21-8bb1c6ce5d28' })
SET release_8bb1c6ce5d28.name = 'Horace Silver and the Jazz Messengers'
SET release_8bb1c6ce5d28.country = 'US'
SET release_8bb1c6ce5d28.date = '1955'
SET release_8bb1c6ce5d28.format = '12" Vinyl'
SET release_8bb1c6ce5d28.discode = 'BLP 1518'
SET release_8bb1c6ce5d28.discogs = 'https://www.discogs.com/release/2301336'
SET release_8bb1c6ce5d28.musicbrainz = 'http://musicbrainz.org/release/41f3eb80-e632-4e1e-8c21-8bb1c6ce5d28'
SET release_8bb1c6ce5d28.source = 'musicbrainz.org'


MERGE (person_8c848a4765b6:Person{ uuid: 'd185d986-ee96-4fd3-bd61-8c848a4765b6' }) 
SET person_8c848a4765b6.name = 'Horace Silver'
SET person_8c848a4765b6.gender = 'Male'
SET person_8c848a4765b6.country = 'US'
SET person_8c848a4765b6.allmusic = 'https://www.allmusic.com/artist/mn0000267354'
SET person_8c848a4765b6.discogs = 'https://www.discogs.com/artist/29973'
SET person_8c848a4765b6.imdb = 'https://www.imdb.com/name/nm0798701/'
SET person_8c848a4765b6.viaf = 'http://viaf.org/viaf/8537804'
SET person_8c848a4765b6.wikidata = 'https://www.wikidata.org/wiki/Q365560'
SET person_8c848a4765b6.databases = ['http://id.loc.gov/authorities/names/n82003124', 'https://adp.library.ucsb.edu/names/343818', 'https://catalogue.bnf.fr/ark:/12148/cb13899777h', 'https://d-nb.info/gnd/132099594', 'http://snaccooperative.org/ark:/99166/w6p015gr', 'https://rateyourmusic.com/artist/horace_silver', 'https://www.45cat.com/artist/horace-silver', 'https://www.45worlds.com/cdalbum/artist/horace-silver', 'https://www.45worlds.com/vinyl/artist/horace-silver', 'https://www.musik-sammler.de/artist/horace-silver/', 'https://www.worldcat.org/identities/lccn-n82003124']
SET person_8c848a4765b6.musicbrainz = 'https://musicbrainz.org/artist/d185d986-ee96-4fd3-bd61-8c848a4765b6'
SET person_8c848a4765b6.isni_list = ['http://isni.org/isni/0000000108681996']
SET person_8c848a4765b6.source = 'musicbrainz.org'


MERGE (person_7d625f52fd07:Person{ uuid: 'ebd504b0-7644-4887-9e4e-7d625f52fd07' }) 
SET person_7d625f52fd07.name = 'Doug Watkins'
SET person_7d625f52fd07.gender = 'Male'
SET person_7d625f52fd07.country = 'US'
SET person_7d625f52fd07.allmusic = 'https://www.allmusic.com/artist/mn0000199677'
SET person_7d625f52fd07.discogs = 'https://www.discogs.com/artist/254176'
SET person_7d625f52fd07.viaf = 'http://viaf.org/viaf/71585781'
SET person_7d625f52fd07.wikidata = 'https://www.wikidata.org/wiki/Q1251883'
SET person_7d625f52fd07.wikipedia = 'https://en.wikipedia.org/wiki/Doug_Watkins'
SET person_7d625f52fd07.databases = ['http://id.loc.gov/authorities/names/n81055687', 'https://adp.library.ucsb.edu/names/350140', 'https://catalogue.bnf.fr/ark:/12148/cb139736259', 'https://d-nb.info/gnd/134551419', 'http://snaccooperative.org/ark:/99166/w6t01p8h', 'https://www.worldcat.org/identities/lccn-n81055687']
SET person_7d625f52fd07.musicbrainz = 'https://musicbrainz.org/artist/ebd504b0-7644-4887-9e4e-7d625f52fd07'
SET person_7d625f52fd07.isni_list = ['http://isni.org/isni/000000005519400X']
SET person_7d625f52fd07.source = 'musicbrainz.org'


MERGE (person_ffd770b7e04a:Person{ uuid: '601e7466-eaf5-4a91-9909-ffd770b7e04a' }) 
SET person_ffd770b7e04a.name = 'Art Blakey'
SET person_ffd770b7e04a.gender = 'Male'
SET person_ffd770b7e04a.country = 'US'
SET person_ffd770b7e04a.allmusic = 'https://www.allmusic.com/artist/mn0000928942'
SET person_ffd770b7e04a.bbc = 'https://www.bbc.co.uk/music/artists/601e7466-eaf5-4a91-9909-ffd770b7e04a'
SET person_ffd770b7e04a.discogs = 'https://www.discogs.com/artist/29977'
SET person_ffd770b7e04a.imdb = 'https://www.imdb.com/name/nm0086845/'
SET person_ffd770b7e04a.viaf = 'http://viaf.org/viaf/10032579'
SET person_ffd770b7e04a.wikidata = 'https://www.wikidata.org/wiki/Q311715'
SET person_ffd770b7e04a.databases = ['http://id.loc.gov/authorities/names/n81023040', 'https://adp.library.ucsb.edu/names/304620', 'https://catalogue.bnf.fr/ark:/12148/cb13891566c', 'https://d-nb.info/gnd/119053462', 'http://snaccooperative.org/ark:/99166/w6474h5f', 'https://nla.gov.au/nla.party-1067262', 'https://rateyourmusic.com/artist/art-blakey', 'https://www.worldcat.org/identities/lccn-n81-023040']
SET person_ffd770b7e04a.musicbrainz = 'https://musicbrainz.org/artist/601e7466-eaf5-4a91-9909-ffd770b7e04a'
SET person_ffd770b7e04a.isni_list = ['http://isni.org/isni/000000010869405X', 'http://isni.org/isni/0000000368545392']
SET person_ffd770b7e04a.source = 'musicbrainz.org'


MERGE (person_107bddae77c2:Person{ uuid: '026b096e-e024-42ab-82f3-107bddae77c2' }) 
SET person_107bddae77c2.name = 'Hank Mobley'
SET person_107bddae77c2.gender = 'Male'
SET person_107bddae77c2.disambiguation = 'US jazz tenor saxophonist'
SET person_107bddae77c2.country = 'US'
SET person_107bddae77c2.allmusic = 'https://www.allmusic.com/artist/mn0000951384'
SET person_107bddae77c2.discogs = 'https://www.discogs.com/artist/135872'
SET person_107bddae77c2.viaf = 'http://viaf.org/viaf/56797059'
SET person_107bddae77c2.wikidata = 'https://www.wikidata.org/wiki/Q534842'
SET person_107bddae77c2.databases = ['http://id.loc.gov/authorities/names/n81026539', 'https://catalogue.bnf.fr/ark:/12148/cb13897581q', 'https://d-nb.info/gnd/134464311', 'http://snaccooperative.org/ark:/99166/w6vt4g4z', 'https://rateyourmusic.com/artist/hank_mobley', 'https://www.worldcat.org/identities/lccn-n81026539']
SET person_107bddae77c2.musicbrainz = 'https://musicbrainz.org/artist/026b096e-e024-42ab-82f3-107bddae77c2'
SET person_107bddae77c2.isni_list = ['http://isni.org/isni/0000000073662276']
SET person_107bddae77c2.source = 'musicbrainz.org'


MERGE (person_07c90b6fa661:Person{ uuid: '4476453a-d37e-4c52-b60d-07c90b6fa661' }) 
SET person_07c90b6fa661.name = 'Kenny Dorham'
SET person_07c90b6fa661.gender = 'Male'
SET person_07c90b6fa661.disambiguation = 'US jazz trumpeter, singer, and composer'
SET person_07c90b6fa661.country = 'US'
SET person_07c90b6fa661.allmusic = 'https://www.allmusic.com/artist/mn0000768027'
SET person_07c90b6fa661.discogs = 'https://www.discogs.com/artist/254945'
SET person_07c90b6fa661.viaf = 'http://viaf.org/viaf/76403361'
SET person_07c90b6fa661.wikidata = 'https://www.wikidata.org/wiki/Q498729'
SET person_07c90b6fa661.databases = ['http://id.loc.gov/authorities/names/n83056867', 'https://adp.library.ucsb.edu/names/312661', 'https://catalogue.bnf.fr/ark:/12148/cb12407498g', 'https://d-nb.info/gnd/134361253', 'http://snaccooperative.org/ark:/99166/w6q263n2', 'https://rateyourmusic.com/artist/kenny_dorham', 'https://www.worldcat.org/identities/lccn-n83056867']
SET person_07c90b6fa661.musicbrainz = 'https://musicbrainz.org/artist/4476453a-d37e-4c52-b60d-07c90b6fa661'
SET person_07c90b6fa661.isni_list = ['http://isni.org/isni/0000000083954272']
SET person_07c90b6fa661.source = 'musicbrainz.org'


MERGE (person_6f4c0409d2ee:Person{ uuid: '209ddf15-ee0a-41a1-a1f5-6f4c0409d2ee' }) 
SET person_6f4c0409d2ee.name = 'Art Blakey & The Jazz Messengers'
SET person_6f4c0409d2ee.country = 'US'
SET person_6f4c0409d2ee.allmusic = 'https://www.allmusic.com/artist/mn0000597266'
SET person_6f4c0409d2ee.discogs = 'https://www.discogs.com/artist/262128'
SET person_6f4c0409d2ee.wikidata = 'https://www.wikidata.org/wiki/Q1684482'
SET person_6f4c0409d2ee.databases = ['https://rateyourmusic.com/artist/the_jazz_messengers']
SET person_6f4c0409d2ee.musicbrainz = 'https://musicbrainz.org/artist/209ddf15-ee0a-41a1-a1f5-6f4c0409d2ee'
SET person_6f4c0409d2ee.source = 'musicbrainz.org'

// labels

MERGE (label_14e1ddfd5946:Label{ uuid: '713c4a95-6616-442b-9cf6-14e1ddfd5946' })
SET label_14e1ddfd5946.name= 'Blue Note'

// performances

MERGE (perf_ab5d4f3b8b52:Performance{ uuid: 'a2bf3851-8d42-4e95-8fe8-ab5d4f3b8b52' })
SET perf_ab5d4f3b8b52.name = 'Room 608'
SET perf_ab5d4f3b8b52.duration = '5:21'
SET perf_ab5d4f3b8b52.source = 'musicbrainz.org'


MERGE (perf_7016faa3f7d8:Performance{ uuid: '7df9661f-3d06-4f57-bbed-7016faa3f7d8' })
SET perf_7016faa3f7d8.name = 'Creepin’ In'
SET perf_7016faa3f7d8.duration = '7:25'
SET perf_7016faa3f7d8.source = 'musicbrainz.org'


MERGE (perf_1a5483a72303:Performance{ uuid: 'd4c4e11c-dd76-4b39-9761-1a5483a72303' })
SET perf_1a5483a72303.name = 'Stop Time'
SET perf_1a5483a72303.duration = '4:06'
SET perf_1a5483a72303.source = 'musicbrainz.org'


MERGE (perf_65df9e59bd91:Performance{ uuid: '4a4ba5f4-4d0f-432c-aebb-65df9e59bd91' })
SET perf_65df9e59bd91.name = 'To Whom It May Concern'
SET perf_65df9e59bd91.duration = '5:10'
SET perf_65df9e59bd91.source = 'musicbrainz.org'


MERGE (perf_f1d44e18233e:Performance{ uuid: '3164504a-3c15-46e2-9f99-f1d44e18233e' })
SET perf_f1d44e18233e.name = 'Hippy'
SET perf_f1d44e18233e.duration = '5:23'
SET perf_f1d44e18233e.source = 'musicbrainz.org'


MERGE (perf_a935f9290f1c:Performance{ uuid: 'c7ff468d-f263-41a4-b644-a935f9290f1c' })
SET perf_a935f9290f1c.name = 'The Preacher'
SET perf_a935f9290f1c.duration = '4:18'
SET perf_a935f9290f1c.source = 'musicbrainz.org'


MERGE (perf_652f0955630c:Performance{ uuid: '6af088d3-356d-4d68-be4b-652f0955630c' })
SET perf_652f0955630c.name = 'Hankerin’'
SET perf_652f0955630c.duration = '5:17'
SET perf_652f0955630c.source = 'musicbrainz.org'


MERGE (perf_05a0c90f7b3c:Performance{ uuid: '80ad46ad-ba1a-47d5-9d03-05a0c90f7b3c' })
SET perf_05a0c90f7b3c.name = 'Doodlin’'
SET perf_05a0c90f7b3c.duration = '6:45'
SET perf_05a0c90f7b3c.source = 'musicbrainz.org'




// labels
MERGE (release_8bb1c6ce5d28)-[:HAS_LABEL]->(label_14e1ddfd5946)


// tracks
MERGE (release_8bb1c6ce5d28)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_ab5d4f3b8b52)
MERGE (release_8bb1c6ce5d28)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_7016faa3f7d8)
MERGE (release_8bb1c6ce5d28)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_1a5483a72303)
MERGE (release_8bb1c6ce5d28)-[:HAS_TRACK {name: 'A4', sequence: 4}]->(perf_65df9e59bd91)
MERGE (release_8bb1c6ce5d28)-[:HAS_TRACK {name: 'B1', sequence: 5}]->(perf_f1d44e18233e)
MERGE (release_8bb1c6ce5d28)-[:HAS_TRACK {name: 'B2', sequence: 6}]->(perf_a935f9290f1c)
MERGE (release_8bb1c6ce5d28)-[:HAS_TRACK {name: 'B3', sequence: 7}]->(perf_652f0955630c)
MERGE (release_8bb1c6ce5d28)-[:HAS_TRACK {name: 'B4', sequence: 8}]->(perf_05a0c90f7b3c)

// works

MERGE (person_02b6ad8e7135:Person{ uuid: '3b451321-9cd1-470f-8e41-02b6ad8e7135' }) 
SET person_02b6ad8e7135.name = 'Babs Gonzales'
SET person_02b6ad8e7135.gender = 'Male'
SET person_02b6ad8e7135.country = 'US'
SET person_02b6ad8e7135.allmusic = 'https://www.allmusic.com/artist/mn0000072091'
SET person_02b6ad8e7135.discogs = 'https://www.discogs.com/artist/321467'
SET person_02b6ad8e7135.viaf = 'http://viaf.org/viaf/196227'
SET person_02b6ad8e7135.wikidata = 'https://www.wikidata.org/wiki/Q797766'
SET person_02b6ad8e7135.wikipedia = 'https://en.wikipedia.org/wiki/Babs_Gonzales'
SET person_02b6ad8e7135.databases = ['http://id.loc.gov/authorities/names/n87144467', 'https://adp.library.ucsb.edu/names/359915', 'https://catalogue.bnf.fr/ark:/12148/cb138945992', 'http://snaccooperative.org/ark:/99166/w65t4j51', 'https://www.worldcat.org/identities/lccn-n87144467']
SET person_02b6ad8e7135.musicbrainz = 'https://musicbrainz.org/artist/3b451321-9cd1-470f-8e41-02b6ad8e7135'
SET person_02b6ad8e7135.isni_list = ['http://isni.org/isni/0000000059403243']
SET person_02b6ad8e7135.source = 'musicbrainz.org'


MERGE (work_986f23608057:Work{ uuid: '8b1f53a6-2e87-3c47-897e-986f23608057' })
SET work_986f23608057.name = 'Creepin\\' In'
SET work_986f23608057.source = 'musicbrainz.org'


MERGE (work_18286ac18d47:Work{ uuid: 'd72a1623-fd5e-3e38-bf78-18286ac18d47' })
SET work_18286ac18d47.name = 'Hippy'
SET work_18286ac18d47.type = 'Song'
SET work_18286ac18d47.source = 'musicbrainz.org'


MERGE (work_29f983ef7e54:Work{ uuid: 'a2c39680-f1d9-3e52-8f0f-29f983ef7e54' })
SET work_29f983ef7e54.name = 'Doodlin’'
SET work_29f983ef7e54.iswc = 'T-070.039.822-6'
SET work_29f983ef7e54.type = 'Song'
SET work_29f983ef7e54.wikidata = 'https://www.wikidata.org/wiki/Q21998467'
SET work_29f983ef7e54.musicbrainz = 'https://musicbrainz.org/work/a2c39680-f1d9-3e52-8f0f-29f983ef7e54'
SET work_29f983ef7e54.source = 'musicbrainz.org'


MERGE (work_178270584d23:Work{ uuid: '5dbea680-ae2f-30ad-bcb0-178270584d23' })
SET work_178270584d23.name = 'The Preacher'
SET work_178270584d23.iswc = 'T-901.295.250-0'
SET work_178270584d23.type = 'Song'
SET work_178270584d23.source = 'musicbrainz.org'


MERGE (work_8cd06c9c81b7:Work{ uuid: '40ec300a-9b41-31d4-bd46-8cd06c9c81b7' })
SET work_8cd06c9c81b7.name = 'Stop Time'
SET work_8cd06c9c81b7.iswc = 'T-070.140.802-7'
SET work_8cd06c9c81b7.type = 'Song'
SET work_8cd06c9c81b7.source = 'musicbrainz.org'


MERGE (work_7915654e1e7f:Work{ uuid: '254e8ea3-8389-3308-807a-7915654e1e7f' })
SET work_7915654e1e7f.name = 'To Whom It May Concern'
SET work_7915654e1e7f.source = 'musicbrainz.org'


MERGE (work_ba4e4b7b9133:Work{ uuid: 'e96c9f50-1fb6-38d9-9e4a-ba4e4b7b9133' })
SET work_ba4e4b7b9133.name = 'Hankerin\\''
SET work_ba4e4b7b9133.source = 'musicbrainz.org'


MERGE (work_30bed8635286:Work{ uuid: '5a43bf1e-3848-34ac-8626-30bed8635286' })
SET work_30bed8635286.name = 'Room 608'
SET work_30bed8635286.type = 'Song'
SET work_30bed8635286.source = 'musicbrainz.org'



// performances of
MERGE (perf_7016faa3f7d8)-[:PERFORMANCE_OF]->(work_986f23608057)
MERGE (perf_f1d44e18233e)-[:PERFORMANCE_OF]->(work_18286ac18d47)
MERGE (perf_05a0c90f7b3c)-[:PERFORMANCE_OF]->(work_29f983ef7e54)
MERGE (perf_a935f9290f1c)-[:PERFORMANCE_OF]->(work_178270584d23)
MERGE (perf_1a5483a72303)-[:PERFORMANCE_OF]->(work_8cd06c9c81b7)
MERGE (perf_65df9e59bd91)-[:PERFORMANCE_OF]->(work_7915654e1e7f)
MERGE (perf_652f0955630c)-[:PERFORMANCE_OF]->(work_ba4e4b7b9133)
MERGE (perf_ab5d4f3b8b52)-[:PERFORMANCE_OF]->(work_30bed8635286)


// composers
MERGE (person_8c848a4765b6)-[:COMPOSED]->(work_986f23608057)
MERGE (person_8c848a4765b6)-[:COMPOSED]->(work_18286ac18d47)
MERGE (person_8c848a4765b6)-[:COMPOSED]->(work_29f983ef7e54)
MERGE (person_8c848a4765b6)-[:COMPOSED]->(work_178270584d23)
MERGE (person_02b6ad8e7135)-[:WROTE_LYRICS]->(work_178270584d23)
MERGE (person_8c848a4765b6)-[:COMPOSED]->(work_8cd06c9c81b7)
MERGE (person_8c848a4765b6)-[:COMPOSED]->(work_7915654e1e7f)
MERGE (person_107bddae77c2)-[:COMPOSED]->(work_ba4e4b7b9133)
MERGE (person_8c848a4765b6)-[:COMPOSED]->(work_30bed8635286)

MERGE (person_ffd770b7e04a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_ab5d4f3b8b52)
MERGE (person_07c90b6fa661)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_ab5d4f3b8b52)
MERGE (person_107bddae77c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_ab5d4f3b8b52)
MERGE (person_8c848a4765b6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ab5d4f3b8b52)
MERGE (person_7d625f52fd07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_ab5d4f3b8b52)
MERGE (person_ffd770b7e04a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_7016faa3f7d8)
MERGE (person_07c90b6fa661)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_7016faa3f7d8)
MERGE (person_107bddae77c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_7016faa3f7d8)
MERGE (person_8c848a4765b6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_7016faa3f7d8)
MERGE (person_7d625f52fd07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_7016faa3f7d8)
MERGE (person_ffd770b7e04a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_1a5483a72303)
MERGE (person_07c90b6fa661)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_1a5483a72303)
MERGE (person_107bddae77c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_1a5483a72303)
MERGE (person_8c848a4765b6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_1a5483a72303)
MERGE (person_7d625f52fd07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_1a5483a72303)
MERGE (person_ffd770b7e04a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_65df9e59bd91)
MERGE (person_07c90b6fa661)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_65df9e59bd91)
MERGE (person_107bddae77c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_65df9e59bd91)
MERGE (person_8c848a4765b6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_65df9e59bd91)
MERGE (person_7d625f52fd07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_65df9e59bd91)
MERGE (person_ffd770b7e04a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f1d44e18233e)
MERGE (person_07c90b6fa661)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_f1d44e18233e)
MERGE (person_107bddae77c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_f1d44e18233e)
MERGE (person_8c848a4765b6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f1d44e18233e)
MERGE (person_7d625f52fd07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_f1d44e18233e)
MERGE (person_ffd770b7e04a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a935f9290f1c)
MERGE (person_07c90b6fa661)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_a935f9290f1c)
MERGE (person_107bddae77c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_a935f9290f1c)
MERGE (person_8c848a4765b6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a935f9290f1c)
MERGE (person_7d625f52fd07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_a935f9290f1c)
MERGE (person_ffd770b7e04a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_652f0955630c)
MERGE (person_07c90b6fa661)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_652f0955630c)
MERGE (person_107bddae77c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_652f0955630c)
MERGE (person_8c848a4765b6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_652f0955630c)
MERGE (person_7d625f52fd07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_652f0955630c)
MERGE (person_ffd770b7e04a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_05a0c90f7b3c)
MERGE (person_07c90b6fa661)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_05a0c90f7b3c)
MERGE (person_107bddae77c2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_05a0c90f7b3c)
MERGE (person_8c848a4765b6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_05a0c90f7b3c)
MERGE (person_7d625f52fd07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_05a0c90f7b3c)



"""
)