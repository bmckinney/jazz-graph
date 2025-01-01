
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_becd58186f0a:Release{ uuid: 'b3ea624f-fea0-4aeb-a5df-becd58186f0a' })
SET release_becd58186f0a.name = 'Dear Old Stockholm'
SET release_becd58186f0a.country = 'US'
SET release_becd58186f0a.date = '1993-02-16'
SET release_becd58186f0a.format = 'CD'
SET release_becd58186f0a.discode = 'GRD120'
SET release_becd58186f0a.discogs = 'https://www.discogs.com/release/1468656'
SET release_becd58186f0a.musicbrainz = 'http://musicbrainz.org/release/b3ea624f-fea0-4aeb-a5df-becd58186f0a'
SET release_becd58186f0a.source = 'musicbrainz.org'


MERGE (person_72ad46cdb831:Person{ uuid: 'b625448e-bf4a-41c3-a421-72ad46cdb831' }) 
SET person_72ad46cdb831.name = 'John Coltrane'
SET person_72ad46cdb831.gender = 'Male'
SET person_72ad46cdb831.country = 'US'
SET person_72ad46cdb831.allmusic = 'https://www.allmusic.com/artist/mn0000175553'
SET person_72ad46cdb831.bbc = 'https://www.bbc.co.uk/music/artists/b625448e-bf4a-41c3-a421-72ad46cdb831'
SET person_72ad46cdb831.discogs = 'https://www.discogs.com/artist/97545'
SET person_72ad46cdb831.imdb = 'https://www.imdb.com/name/nm0173328/'
SET person_72ad46cdb831.viaf = 'http://viaf.org/viaf/61731379'
SET person_72ad46cdb831.wikidata = 'https://www.wikidata.org/wiki/Q7346'
SET person_72ad46cdb831.databases = ['http://id.loc.gov/authorities/names/n50031907', 'https://adp.library.ucsb.edu/names/309224', 'https://catalogue.bnf.fr/ark:/12148/cb138926615', 'https://d-nb.info/gnd/118521667', 'https://ibdb.com/person.php?id=485239', 'http://snaccooperative.org/ark:/99166/w6x92hns', 'https://nla.gov.au/nla.party-1006213', 'https://openlibrary.org/works/OL7513936A', 'https://rateyourmusic.com/artist/john_coltrane', 'https://www.45cat.com/artist/john-coltrane', 'https://www.45worlds.com/cdalbum/artist/john-coltrane', 'https://www.45worlds.com/tape/artist/john-coltrane', 'https://www.45worlds.com/vinyl/artist/john-coltrane', 'https://www.musik-sammler.de/artist/john-coltrane/', 'https://www.whosampled.com/John-Coltrane/', 'https://www.worldcat.org/identities/lccn-n50-031907']
SET person_72ad46cdb831.musicbrainz = 'https://musicbrainz.org/artist/b625448e-bf4a-41c3-a421-72ad46cdb831'
SET person_72ad46cdb831.isni_list = ['http://isni.org/isni/000000012280792X']
SET person_72ad46cdb831.source = 'musicbrainz.org'


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


MERGE (person_ea3dca37315e:Person{ uuid: '5af83c93-103f-433b-b759-ea3dca37315e' }) 
SET person_ea3dca37315e.name = 'Jimmy Garrison'
SET person_ea3dca37315e.gender = 'Male'
SET person_ea3dca37315e.country = 'US'
SET person_ea3dca37315e.allmusic = 'https://www.allmusic.com/artist/mn0000853359'
SET person_ea3dca37315e.discogs = 'https://www.discogs.com/artist/254065'
SET person_ea3dca37315e.viaf = 'http://viaf.org/viaf/85775382'
SET person_ea3dca37315e.wikidata = 'https://www.wikidata.org/wiki/Q727702'
SET person_ea3dca37315e.databases = ['http://id.loc.gov/authorities/names/n82020003', 'https://catalogue.bnf.fr/ark:/12148/cb138943191', 'https://d-nb.info/gnd/134381858', 'https://www.worldcat.org/identities/lccn-n82020003']
SET person_ea3dca37315e.musicbrainz = 'https://musicbrainz.org/artist/5af83c93-103f-433b-b759-ea3dca37315e'
SET person_ea3dca37315e.isni_list = ['http://isni.org/isni/000000011576719X']
SET person_ea3dca37315e.source = 'musicbrainz.org'


MERGE (person_97fbbd83c619:Person{ uuid: '14955018-4a03-430c-9d99-97fbbd83c619' }) 
SET person_97fbbd83c619.name = 'Bob Thiele'
SET person_97fbbd83c619.gender = 'Male'
SET person_97fbbd83c619.disambiguation = 'producer & songwriter'
SET person_97fbbd83c619.country = 'US'
SET person_97fbbd83c619.allmusic = 'https://www.allmusic.com/artist/mn0000076822'
SET person_97fbbd83c619.discogs = 'https://www.discogs.com/artist/253353'
SET person_97fbbd83c619.discogs = 'https://www.discogs.com/artist/629474'
SET person_97fbbd83c619.imdb = 'https://www.imdb.com/name/nm1176718/'
SET person_97fbbd83c619.viaf = 'http://viaf.org/viaf/79167866'
SET person_97fbbd83c619.wikidata = 'https://www.wikidata.org/wiki/Q888287'
SET person_97fbbd83c619.databases = ['http://id.loc.gov/authorities/names/n92017297', 'https://catalogue.bnf.fr/ark:/12148/cb13900392f', 'https://d-nb.info/gnd/119376989', 'https://rateyourmusic.com/artist/bob_thiele', 'https://www.worldcat.org/identities/lccn-n92017297']
SET person_97fbbd83c619.musicbrainz = 'https://musicbrainz.org/artist/14955018-4a03-430c-9d99-97fbbd83c619'
SET person_97fbbd83c619.isni_list = ['http://isni.org/isni/0000000114491726']
SET person_97fbbd83c619.source = 'musicbrainz.org'


MERGE (person_8971e7a2912e:Person{ uuid: '22fe7b6f-af38-458e-87bd-8971e7a2912e' }) 
SET person_8971e7a2912e.name = 'McCoy Tyner'
SET person_8971e7a2912e.gender = 'Male'
SET person_8971e7a2912e.disambiguation = 'jazz pianist'
SET person_8971e7a2912e.country = 'US'
SET person_8971e7a2912e.allmusic = 'https://www.allmusic.com/artist/mn0000868092'
SET person_8971e7a2912e.bbc = 'https://www.bbc.co.uk/music/artists/22fe7b6f-af38-458e-87bd-8971e7a2912e'
SET person_8971e7a2912e.discogs = 'https://www.discogs.com/artist/10620'
SET person_8971e7a2912e.imdb = 'https://www.imdb.com/name/nm1743784/'
SET person_8971e7a2912e.viaf = 'http://viaf.org/viaf/84970893'
SET person_8971e7a2912e.wikidata = 'https://www.wikidata.org/wiki/Q318619'
SET person_8971e7a2912e.databases = ['http://id.loc.gov/authorities/names/n81058256', 'https://catalogue.bnf.fr/ark:/12148/cb139006254', 'https://d-nb.info/gnd/134543734', 'http://snaccooperative.org/ark:/99166/w6183cz4', 'https://www.worldcat.org/identities/lccn-n81-058256']
SET person_8971e7a2912e.musicbrainz = 'https://musicbrainz.org/artist/22fe7b6f-af38-458e-87bd-8971e7a2912e'
SET person_8971e7a2912e.isni_list = ['http://isni.org/isni/0000000120184511']
SET person_8971e7a2912e.source = 'musicbrainz.org'


MERGE (person_05d508e09a73:Person{ uuid: 'f0707f1d-55e1-46b6-8a9c-05d508e09a73' }) 
SET person_05d508e09a73.name = 'Rudy van Gelder'
SET person_05d508e09a73.gender = 'Male'
SET person_05d508e09a73.country = 'US'
SET person_05d508e09a73.allmusic = 'https://www.allmusic.com/artist/mn0000305301'
SET person_05d508e09a73.discogs = 'https://www.discogs.com/artist/252966'
SET person_05d508e09a73.viaf = 'http://viaf.org/viaf/33997197'
SET person_05d508e09a73.wikidata = 'https://www.wikidata.org/wiki/Q945681'
SET person_05d508e09a73.databases = ['http://id.loc.gov/authorities/names/no00020144', 'https://d-nb.info/gnd/133648508', 'https://rateyourmusic.com/artist/rudy_van_gelder', 'https://www.worldcat.org/identities/lccn-no00020144']
SET person_05d508e09a73.musicbrainz = 'https://musicbrainz.org/artist/f0707f1d-55e1-46b6-8a9c-05d508e09a73'
SET person_05d508e09a73.isni_list = ['http://isni.org/isni/0000000019691076']
SET person_05d508e09a73.source = 'musicbrainz.org'


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
SET person_6f0a331cc1ca.databases = ['http://id.loc.gov/authorities/names/n81140108', 'https://adp.library.ucsb.edu/names/320530', 'https://catalogue.bnf.fr/ark:/12148/cb13895060w', 'https://d-nb.info/gnd/134400623', 'http://snaccooperative.org/ark:/99166/w6fj33d4', 'https://www.worldcat.org/identities/lccn-n81140108']
SET person_6f0a331cc1ca.musicbrainz = 'https://musicbrainz.org/artist/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.isni_list = ['http://isni.org/isni/0000000078266176']
SET person_6f0a331cc1ca.source = 'musicbrainz.org'

// labels

MERGE (label_8fb76f3e6ca9:Label{ uuid: '93c3b044-2b4e-4239-a73b-8fb76f3e6ca9' })
SET label_8fb76f3e6ca9.name= 'impulse!'

// performances

MERGE (perf_f86092af2ab1:Performance{ uuid: '568f3cf4-0986-49c6-ac52-f86092af2ab1' })
SET perf_f86092af2ab1.name = 'Dear Old Stockholm'
SET perf_f86092af2ab1.duration = '10:35'
SET perf_f86092af2ab1.begin_date = '1963-04-29'
SET perf_f86092af2ab1.end_date = '1963-04-29'
SET perf_f86092af2ab1.source = 'musicbrainz.org'


MERGE (perf_ed2841c444f8:Performance{ uuid: '1cddceed-13e7-4491-b093-ed2841c444f8' })
SET perf_ed2841c444f8.name = 'After the Rain'
SET perf_ed2841c444f8.disambiguation = 'studio, 1963-04-29'
SET perf_ed2841c444f8.duration = '4:10'
SET perf_ed2841c444f8.begin_date = '1963-04-29'
SET perf_ed2841c444f8.end_date = '1963-04-29'
SET perf_ed2841c444f8.source = 'musicbrainz.org'


MERGE (perf_daf1c45b6cc1:Performance{ uuid: 'ee15cb99-edad-4498-835d-daf1c45b6cc1' })
SET perf_daf1c45b6cc1.name = 'One Down, One Up'
SET perf_daf1c45b6cc1.disambiguation = 'studio, 1965-05-26: Van Gelder Studio, Englewood Cliffs, NJ'
SET perf_daf1c45b6cc1.duration = '15:25'
SET perf_daf1c45b6cc1.begin_date = '1965-05-26'
SET perf_daf1c45b6cc1.end_date = '1965-05-26'
SET perf_daf1c45b6cc1.source = 'musicbrainz.org'


MERGE (perf_390b90edb966:Performance{ uuid: 'aea8e156-509e-4873-9064-390b90edb966' })
SET perf_390b90edb966.name = 'After the Crescent'
SET perf_390b90edb966.duration = '13:34'
SET perf_390b90edb966.begin_date = '1965-05-26'
SET perf_390b90edb966.end_date = '1965-05-26'
SET perf_390b90edb966.source = 'musicbrainz.org'


MERGE (perf_aee6a481f20b:Performance{ uuid: '673f8ef8-9be8-4e6a-b463-aee6a481f20b' })
SET perf_aee6a481f20b.name = 'Dear Lord'
SET perf_aee6a481f20b.duration = '5:35'
SET perf_aee6a481f20b.begin_date = '1965-05-26'
SET perf_aee6a481f20b.end_date = '1965-05-26'
SET perf_aee6a481f20b.source = 'musicbrainz.org'




// labels
MERGE (release_becd58186f0a)-[:HAS_LABEL]->(label_8fb76f3e6ca9)


// tracks
MERGE (release_becd58186f0a)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_f86092af2ab1)
MERGE (release_becd58186f0a)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_ed2841c444f8)
MERGE (release_becd58186f0a)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_daf1c45b6cc1)
MERGE (release_becd58186f0a)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_390b90edb966)
MERGE (release_becd58186f0a)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_aee6a481f20b)

// works

MERGE (person_8d40b5dcbc41:Person{ uuid: '9be7f096-97ec-4615-8957-8d40b5dcbc41' }) 
SET person_8d40b5dcbc41.name = '[traditional]'
SET person_8d40b5dcbc41.gender = 'Not applicable'
SET person_8d40b5dcbc41.disambiguation = 'special purpose artist'
SET person_8d40b5dcbc41.country = 'XW'
SET person_8d40b5dcbc41.allmusic = 'https://www.allmusic.com/artist/mn0000022266'
SET person_8d40b5dcbc41.discogs = 'https://www.discogs.com/artist/151641'
SET person_8d40b5dcbc41.discogs = 'https://www.discogs.com/artist/320156'
SET person_8d40b5dcbc41.wikidata = 'https://www.wikidata.org/wiki/Q235858'
SET person_8d40b5dcbc41.databases = ['https://rateyourmusic.com/artist/traditional', 'https://www.whosampled.com/Traditional-Folk/']
SET person_8d40b5dcbc41.musicbrainz = 'https://musicbrainz.org/artist/9be7f096-97ec-4615-8957-8d40b5dcbc41'
SET person_8d40b5dcbc41.source = 'musicbrainz.org'


MERGE (work_f2d20567d331:Work{ uuid: 'e5cf173e-12c2-3842-955a-f2d20567d331' })
SET work_f2d20567d331.name = 'After the Crescent'
SET work_f2d20567d331.iswc = 'T-070.221.972-4'
SET work_f2d20567d331.type = 'Song'
SET work_f2d20567d331.allmusic = 'https://www.allmusic.com/song/mt0044895753'
SET work_f2d20567d331.musicbrainz = 'https://musicbrainz.org/work/e5cf173e-12c2-3842-955a-f2d20567d331'
SET work_f2d20567d331.source = 'musicbrainz.org'


MERGE (work_faef6a0b8e7e:Work{ uuid: 'd7165326-52d4-3073-a3bb-faef6a0b8e7e' })
SET work_faef6a0b8e7e.name = 'One Down, One Up'
SET work_faef6a0b8e7e.iswc = 'T-700.050.692-5'
SET work_faef6a0b8e7e.type = 'Song'
SET work_faef6a0b8e7e.source = 'musicbrainz.org'


MERGE (work_b1286766ae1b:Work{ uuid: '7691eb8b-7a8b-335e-9421-b1286766ae1b' })
SET work_b1286766ae1b.name = 'Dear Lord'
SET work_b1286766ae1b.iswc = 'T-700.008.831-5'
SET work_b1286766ae1b.type = 'Song'
SET work_b1286766ae1b.allmusic = 'https://www.allmusic.com/song/mt0007612629'
SET work_b1286766ae1b.musicbrainz = 'https://musicbrainz.org/work/7691eb8b-7a8b-335e-9421-b1286766ae1b'
SET work_b1286766ae1b.source = 'musicbrainz.org'


MERGE (work_529eba30435c:Work{ uuid: '0e29de59-030d-4e0f-b30f-529eba30435c' })
SET work_529eba30435c.name = 'Dear Old Stockholm'
SET work_529eba30435c.iswc = 'T-900.312.305-5'
SET work_529eba30435c.type = 'Song'
SET work_529eba30435c.wikidata = 'https://www.wikidata.org/wiki/Q404991'
SET work_529eba30435c.musicbrainz = 'https://musicbrainz.org/work/0e29de59-030d-4e0f-b30f-529eba30435c'
SET work_529eba30435c.source = 'musicbrainz.org'


MERGE (work_45b938686d41:Work{ uuid: '469120aa-8a5b-30bf-8608-45b938686d41' })
SET work_45b938686d41.name = 'After the Rain'
SET work_45b938686d41.iswc = 'T-070.231.851-1'
SET work_45b938686d41.type = 'Song'
SET work_45b938686d41.allmusic = 'https://www.allmusic.com/song/mt0027042159'
SET work_45b938686d41.musicbrainz = 'https://musicbrainz.org/work/469120aa-8a5b-30bf-8608-45b938686d41'
SET work_45b938686d41.source = 'musicbrainz.org'



// performances of
MERGE (perf_390b90edb966)-[:PERFORMANCE_OF]->(work_f2d20567d331)
MERGE (perf_daf1c45b6cc1)-[:PERFORMANCE_OF]->(work_faef6a0b8e7e)
MERGE (perf_aee6a481f20b)-[:PERFORMANCE_OF]->(work_b1286766ae1b)
MERGE (perf_f86092af2ab1)-[:PERFORMANCE_OF]->(work_529eba30435c)
MERGE (perf_ed2841c444f8)-[:PERFORMANCE_OF]->(work_45b938686d41)


// composers
MERGE (person_72ad46cdb831)-[:COMPOSED]->(work_f2d20567d331)
MERGE (person_72ad46cdb831)-[:COMPOSED]->(work_faef6a0b8e7e)
MERGE (person_72ad46cdb831)-[:COMPOSED]->(work_b1286766ae1b)
MERGE (person_8d40b5dcbc41)-[:COMPOSED]->(work_529eba30435c)
MERGE (person_72ad46cdb831)-[:COMPOSED]->(work_45b938686d41)


// place nodes

MERGE (place_569fa8b97644:Place{ uuid: '1165ef7d-371c-4e03-98db-569fa8b97644' })
SET place_569fa8b97644.name = 'Van Gelder Studio'
SET place_569fa8b97644.source = 'musicbrainz.org'


// place relationships
MERGE (perf_f86092af2ab1)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-04-29', end_date: '1963-04-29' }]->(place_569fa8b97644)
MERGE (perf_ed2841c444f8)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-04-29', end_date: '1963-04-29' }]->(place_569fa8b97644)
MERGE (perf_daf1c45b6cc1)-[:HAS_PLACE { type: 'recorded at', begin_date: '1965-05-26', end_date: '1965-05-26' }]->(place_569fa8b97644)
MERGE (perf_390b90edb966)-[:HAS_PLACE { type: 'recorded at', begin_date: '1965-05-26', end_date: '1965-05-26' }]->(place_569fa8b97644)
MERGE (perf_aee6a481f20b)-[:HAS_PLACE { type: 'recorded at', begin_date: '1965-05-26', end_date: '1965-05-26' }]->(place_569fa8b97644)

MERGE (person_72ad46cdb831)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_f86092af2ab1)
MERGE (person_ea3dca37315e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass', 'double bass'] }]->(perf_f86092af2ab1)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f86092af2ab1)
MERGE (person_8971e7a2912e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f86092af2ab1)
MERGE (person_97fbbd83c619)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_f86092af2ab1)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_f86092af2ab1)
MERGE (person_72ad46cdb831)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_ed2841c444f8)
MERGE (person_ea3dca37315e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_ed2841c444f8)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_ed2841c444f8)
MERGE (person_8971e7a2912e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ed2841c444f8)
MERGE (person_97fbbd83c619)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_ed2841c444f8)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_ed2841c444f8)
MERGE (person_72ad46cdb831)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_daf1c45b6cc1)
MERGE (person_ea3dca37315e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_daf1c45b6cc1)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_daf1c45b6cc1)
MERGE (person_8971e7a2912e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_daf1c45b6cc1)
MERGE (person_97fbbd83c619)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_daf1c45b6cc1)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_daf1c45b6cc1)
MERGE (person_72ad46cdb831)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_390b90edb966)
MERGE (person_ea3dca37315e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass', 'double bass'] }]->(perf_390b90edb966)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_390b90edb966)
MERGE (person_8971e7a2912e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_390b90edb966)
MERGE (person_97fbbd83c619)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_390b90edb966)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_390b90edb966)
MERGE (person_72ad46cdb831)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_aee6a481f20b)
MERGE (person_ea3dca37315e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_aee6a481f20b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_aee6a481f20b)
MERGE (person_bed4063208e7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_aee6a481f20b)
MERGE (person_8971e7a2912e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_aee6a481f20b)
MERGE (person_97fbbd83c619)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_aee6a481f20b)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_aee6a481f20b)



"""
)