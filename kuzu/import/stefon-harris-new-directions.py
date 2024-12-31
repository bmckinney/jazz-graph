
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_74357dc5893c:Release{ uuid: '82bf3e61-824b-4810-8066-74357dc5893c' })
SET release_74357dc5893c.name = 'New Directions'
SET release_74357dc5893c.country = 'XE'
SET release_74357dc5893c.date = '2000'
SET release_74357dc5893c.format = 'CD'
SET release_74357dc5893c.discode = '7243 5 22978 2 5'
SET release_74357dc5893c.discogs = 'https://www.discogs.com/release/3226148'
SET release_74357dc5893c.musicbrainz = 'http://musicbrainz.org/release/82bf3e61-824b-4810-8066-74357dc5893c'
SET release_74357dc5893c.source = 'musicbrainz.org'


MERGE (person_ab71e164ae60:Person{ uuid: 'a60a8aad-3d96-441a-9c3b-ab71e164ae60' }) 
SET person_ab71e164ae60.name = 'Tarus Mateen'
SET person_ab71e164ae60.gender = 'Male'
SET person_ab71e164ae60.country = 'US'
SET person_ab71e164ae60.allmusic = 'https://www.allmusic.com/artist/mn0000011084'
SET person_ab71e164ae60.discogs = 'https://www.discogs.com/artist/187661'
SET person_ab71e164ae60.viaf = 'http://viaf.org/viaf/22332258'
SET person_ab71e164ae60.wikidata = 'https://www.wikidata.org/wiki/Q1481025'
SET person_ab71e164ae60.databases = ['http://id.loc.gov/authorities/names/nr94041571', 'https://catalogue.bnf.fr/ark:/12148/cb13939811s', 'https://d-nb.info/gnd/134742745', 'https://www.worldcat.org/identities/lccn-nr94041571']
SET person_ab71e164ae60.musicbrainz = 'https://musicbrainz.org/artist/a60a8aad-3d96-441a-9c3b-ab71e164ae60'
SET person_ab71e164ae60.isni_list = ['http://isni.org/isni/0000000055164943']
SET person_ab71e164ae60.source = 'musicbrainz.org'


MERGE (person_c65081d12d86:Person{ uuid: '2f97f8ef-1bd6-439e-b725-c65081d12d86' }) 
SET person_c65081d12d86.name = 'Jason Moran'
SET person_c65081d12d86.gender = 'Male'
SET person_c65081d12d86.disambiguation = 'American jazz pianist and composer'
SET person_c65081d12d86.country = 'US'
SET person_c65081d12d86.discogs = 'https://www.discogs.com/artist/96435'
SET person_c65081d12d86.imdb = 'https://www.imdb.com/name/nm1390780/'
SET person_c65081d12d86.viaf = 'http://viaf.org/viaf/49422111'
SET person_c65081d12d86.wikidata = 'https://www.wikidata.org/wiki/Q978467'
SET person_c65081d12d86.databases = ['http://id.loc.gov/authorities/names/no2001053219', 'https://catalogue.bnf.fr/ark:/12148/cb14025774t', 'https://d-nb.info/gnd/13512669X', 'http://www.worldcat.org/wcidentities/lccn-no2001-53219']
SET person_c65081d12d86.musicbrainz = 'https://musicbrainz.org/artist/2f97f8ef-1bd6-439e-b725-c65081d12d86'
SET person_c65081d12d86.isni_list = ['http://isni.org/isni/000000011443588X']
SET person_c65081d12d86.source = 'musicbrainz.org'


MERGE (person_cf15b8735268:Person{ uuid: 'ab3363db-53ac-44c1-abfe-cf15b8735268' }) 
SET person_cf15b8735268.name = 'Nasheet Waits'
SET person_cf15b8735268.gender = 'Male'
SET person_cf15b8735268.country = 'US'
SET person_cf15b8735268.allmusic = 'https://www.allmusic.com/artist/mn0000315826'
SET person_cf15b8735268.discogs = 'https://www.discogs.com/artist/334551'
SET person_cf15b8735268.viaf = 'http://viaf.org/viaf/37128340'
SET person_cf15b8735268.wikidata = 'https://www.wikidata.org/wiki/Q1965729'
SET person_cf15b8735268.databases = ['http://id.loc.gov/authorities/names/no2001000847', 'https://catalogue.bnf.fr/ark:/12148/cb142374501', 'https://d-nb.info/gnd/135043077', 'https://www.worldcat.org/identities/lccn-no2001000847']
SET person_cf15b8735268.musicbrainz = 'https://musicbrainz.org/artist/ab3363db-53ac-44c1-abfe-cf15b8735268'
SET person_cf15b8735268.isni_list = ['http://isni.org/isni/0000000055174105']
SET person_cf15b8735268.source = 'musicbrainz.org'


MERGE (person_08c85d96da39:Person{ uuid: 'bbef05c0-ec64-46df-b7af-08c85d96da39' }) 
SET person_08c85d96da39.name = 'Greg Osby'
SET person_08c85d96da39.gender = 'Male'
SET person_08c85d96da39.disambiguation = 'American jazz saxophonist'
SET person_08c85d96da39.country = 'US'
SET person_08c85d96da39.allmusic = 'https://www.allmusic.com/artist/mn0000156900'
SET person_08c85d96da39.discogs = 'https://www.discogs.com/artist/29993'
SET person_08c85d96da39.viaf = 'http://viaf.org/viaf/39563865'
SET person_08c85d96da39.wikidata = 'https://www.wikidata.org/wiki/Q707969'
SET person_08c85d96da39.wikipedia = 'https://en.wikipedia.org/wiki/Greg_Osby'
SET person_08c85d96da39.databases = ['http://id.loc.gov/authorities/names/nr91024118', 'https://catalogue.bnf.fr/ark:/12148/cb13921997g', 'https://d-nb.info/gnd/134638565', 'https://www.worldcat.org/identities/lccn-nr91024118']
SET person_08c85d96da39.musicbrainz = 'https://musicbrainz.org/artist/bbef05c0-ec64-46df-b7af-08c85d96da39'
SET person_08c85d96da39.isni_list = ['http://isni.org/isni/0000000073654110']
SET person_08c85d96da39.source = 'musicbrainz.org'


MERGE (person_a5bca957bed1:Person{ uuid: '35af8529-aa19-4268-b58d-a5bca957bed1' }) 
SET person_a5bca957bed1.name = 'Seth Presant'
SET person_a5bca957bed1.gender = 'Male'
SET person_a5bca957bed1.discogs = 'https://www.discogs.com/artist/659592'
SET person_a5bca957bed1.musicbrainz = 'https://musicbrainz.org/artist/35af8529-aa19-4268-b58d-a5bca957bed1'
SET person_a5bca957bed1.source = 'musicbrainz.org'


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


MERGE (person_fae4c02a9a1a:Person{ uuid: 'a18b2895-1dbe-4b55-bba0-fae4c02a9a1a' }) 
SET person_fae4c02a9a1a.name = 'Stefon Harris'
SET person_fae4c02a9a1a.gender = 'Male'
SET person_fae4c02a9a1a.country = 'US'
SET person_fae4c02a9a1a.allmusic = 'https://www.allmusic.com/artist/mn0000019334'
SET person_fae4c02a9a1a.allmusic = 'https://www.allmusic.com/artist/mn0003789427'
SET person_fae4c02a9a1a.discogs = 'https://www.discogs.com/artist/312030'
SET person_fae4c02a9a1a.discogs = 'https://www.discogs.com/artist/348693'
SET person_fae4c02a9a1a.imdb = 'https://www.imdb.com/name/nm4395750/'
SET person_fae4c02a9a1a.viaf = 'http://viaf.org/viaf/85807754'
SET person_fae4c02a9a1a.wikidata = 'https://www.wikidata.org/wiki/Q720524'
SET person_fae4c02a9a1a.databases = ['http://id.loc.gov/authorities/names/no98100654', 'https://catalogue.bnf.fr/ark:/12148/cb14028428j', 'https://d-nb.info/gnd/135095557', 'https://rateyourmusic.com/artist/stefon-harris', 'https://www.worldcat.org/identities/lccn-no98100654']
SET person_fae4c02a9a1a.musicbrainz = 'https://musicbrainz.org/artist/a18b2895-1dbe-4b55-bba0-fae4c02a9a1a'
SET person_fae4c02a9a1a.isni_list = ['http://isni.org/isni/0000000114507556', 'http://isni.org/isni/0000000407664715']
SET person_fae4c02a9a1a.source = 'musicbrainz.org'


MERGE (person_af0e1842067e:Person{ uuid: 'b3bc445c-d4f4-4eee-bc9b-af0e1842067e' }) 
SET person_af0e1842067e.name = 'Maureen Sickler'
SET person_af0e1842067e.discogs = 'https://www.discogs.com/artist/879407'
SET person_af0e1842067e.musicbrainz = 'https://musicbrainz.org/artist/b3bc445c-d4f4-4eee-bc9b-af0e1842067e'
SET person_af0e1842067e.source = 'musicbrainz.org'


MERGE (person_daf81c508719:Person{ uuid: '26dfe5ce-be83-46d4-9ae2-daf81c508719' }) 
SET person_daf81c508719.name = 'Mark Shim'
SET person_daf81c508719.gender = 'Male'
SET person_daf81c508719.country = 'JM'
SET person_daf81c508719.allmusic = 'https://www.allmusic.com/artist/mn0000844811'
SET person_daf81c508719.discogs = 'https://www.discogs.com/artist/303165'
SET person_daf81c508719.viaf = 'http://viaf.org/viaf/37128006'
SET person_daf81c508719.wikidata = 'https://www.wikidata.org/wiki/Q1900432'
SET person_daf81c508719.databases = ['http://id.loc.gov/authorities/names/no98103545', 'https://catalogue.bnf.fr/ark:/12148/cb14226939f', 'https://d-nb.info/gnd/135085268', 'https://www.worldcat.org/identities/lccn-no98103545']
SET person_daf81c508719.musicbrainz = 'https://musicbrainz.org/artist/26dfe5ce-be83-46d4-9ae2-daf81c508719'
SET person_daf81c508719.isni_list = ['http://isni.org/isni/0000000055174076']
SET person_daf81c508719.source = 'musicbrainz.org'

// labels

MERGE (label_14e1ddfd5946:Label{ uuid: '713c4a95-6616-442b-9cf6-14e1ddfd5946' })
SET label_14e1ddfd5946.name= 'Blue Note'

// performances

MERGE (perf_79ff62ac1702:Performance{ uuid: 'dc4f45d7-a409-4f5e-a918-79ff62ac1702' })
SET perf_79ff62ac1702.name = 'Theme From Blow Up'
SET perf_79ff62ac1702.duration = '7:58'
SET perf_79ff62ac1702.begin_date = '1999-05-10'
SET perf_79ff62ac1702.end_date = '1999-05-11'
SET perf_79ff62ac1702.source = 'musicbrainz.org'


MERGE (perf_18d192d82bb8:Performance{ uuid: '39ba0721-1289-40a0-b8aa-18d192d82bb8' })
SET perf_18d192d82bb8.name = 'The Sidewinder'
SET perf_18d192d82bb8.duration = '5:01'
SET perf_18d192d82bb8.begin_date = '1999-05-10'
SET perf_18d192d82bb8.end_date = '1999-05-11'
SET perf_18d192d82bb8.source = 'musicbrainz.org'


MERGE (perf_2b466aab58e6:Performance{ uuid: 'c507a947-0700-43da-92ee-2b466aab58e6' })
SET perf_2b466aab58e6.name = 'Ping Pong'
SET perf_2b466aab58e6.duration = '4:52'
SET perf_2b466aab58e6.begin_date = '1999-05-10'
SET perf_2b466aab58e6.end_date = '1999-05-11'
SET perf_2b466aab58e6.source = 'musicbrainz.org'


MERGE (perf_53aeafb147b4:Performance{ uuid: 'b06640c3-f0c0-430a-8b7f-53aeafb147b4' })
SET perf_53aeafb147b4.name = 'Beatrice'
SET perf_53aeafb147b4.duration = '3:59'
SET perf_53aeafb147b4.begin_date = '1999-05-10'
SET perf_53aeafb147b4.end_date = '1999-05-11'
SET perf_53aeafb147b4.source = 'musicbrainz.org'


MERGE (perf_eec94f94c776:Performance{ uuid: '78591e0b-bf1c-43ec-8a89-eec94f94c776' })
SET perf_eec94f94c776.name = 'No Room for Squares'
SET perf_eec94f94c776.duration = '4:54'
SET perf_eec94f94c776.begin_date = '1999-05-10'
SET perf_eec94f94c776.end_date = '1999-05-11'
SET perf_eec94f94c776.source = 'musicbrainz.org'


MERGE (perf_0c8ef440d52a:Performance{ uuid: 'd310fa15-c848-40f1-a1b1-0c8ef440d52a' })
SET perf_0c8ef440d52a.name = 'Song for My Father'
SET perf_0c8ef440d52a.duration = '7:16'
SET perf_0c8ef440d52a.begin_date = '1999-05-10'
SET perf_0c8ef440d52a.end_date = '1999-05-11'
SET perf_0c8ef440d52a.source = 'musicbrainz.org'


MERGE (perf_19d054bd4142:Performance{ uuid: 'b7a31d82-1946-47c1-95c1-19d054bd4142' })
SET perf_19d054bd4142.name = 'Tom Thumb'
SET perf_19d054bd4142.duration = '5:05'
SET perf_19d054bd4142.begin_date = '1999-05-10'
SET perf_19d054bd4142.end_date = '1999-05-11'
SET perf_19d054bd4142.source = 'musicbrainz.org'


MERGE (perf_48334528efa4:Performance{ uuid: '8b38965d-e489-45b2-8fe3-48334528efa4' })
SET perf_48334528efa4.name = 'Commentary on Electrical Switches'
SET perf_48334528efa4.duration = '2:42'
SET perf_48334528efa4.begin_date = '1999-05-10'
SET perf_48334528efa4.end_date = '1999-05-11'
SET perf_48334528efa4.source = 'musicbrainz.org'


MERGE (perf_e1821e97fc07:Performance{ uuid: '1cd6ad02-1817-40a6-a1fa-e1821e97fc07' })
SET perf_e1821e97fc07.name = 'Big Bertha'
SET perf_e1821e97fc07.duration = '4:37'
SET perf_e1821e97fc07.begin_date = '1999-05-10'
SET perf_e1821e97fc07.end_date = '1999-05-11'
SET perf_e1821e97fc07.source = 'musicbrainz.org'


MERGE (perf_a50c9ab756f2:Performance{ uuid: '98eb37a7-c6f0-4b62-9afb-a50c9ab756f2' })
SET perf_a50c9ab756f2.name = 'Recorda Me'
SET perf_a50c9ab756f2.duration = '4:25'
SET perf_a50c9ab756f2.begin_date = '1999-05-10'
SET perf_a50c9ab756f2.end_date = '1999-05-11'
SET perf_a50c9ab756f2.source = 'musicbrainz.org'


MERGE (perf_d49d3ecbbf2c:Performance{ uuid: '9cb7d4a3-7af7-4338-863d-d49d3ecbbf2c' })
SET perf_d49d3ecbbf2c.name = 'Song of the Whispering Banshee'
SET perf_d49d3ecbbf2c.duration = '5:44'
SET perf_d49d3ecbbf2c.begin_date = '1999-05-10'
SET perf_d49d3ecbbf2c.end_date = '1999-05-11'
SET perf_d49d3ecbbf2c.source = 'musicbrainz.org'


MERGE (perf_0d40f0345260:Performance{ uuid: 'd2d39d14-9326-4b12-90de-0d40f0345260' })
SET perf_0d40f0345260.name = 'False Start'
SET perf_0d40f0345260.duration = '0:44'
SET perf_0d40f0345260.begin_date = '1999-05-10'
SET perf_0d40f0345260.end_date = '1999-05-11'
SET perf_0d40f0345260.source = 'musicbrainz.org'


MERGE (perf_b840386fb3f1:Performance{ uuid: 'a4cd729d-d6b8-4e41-ade0-b840386fb3f1' })
SET perf_b840386fb3f1.name = '20 Questions'
SET perf_b840386fb3f1.duration = '4:01'
SET perf_b840386fb3f1.begin_date = '1999-05-10'
SET perf_b840386fb3f1.end_date = '1999-05-11'
SET perf_b840386fb3f1.source = 'musicbrainz.org'




// labels
MERGE (release_74357dc5893c)-[:HAS_LABEL]->(label_14e1ddfd5946)


// tracks
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_79ff62ac1702)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_18d192d82bb8)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_2b466aab58e6)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_53aeafb147b4)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_eec94f94c776)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_0c8ef440d52a)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_19d054bd4142)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_48334528efa4)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_e1821e97fc07)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_a50c9ab756f2)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '11', sequence: 11}]->(perf_d49d3ecbbf2c)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '12', sequence: 12}]->(perf_0d40f0345260)
MERGE (release_74357dc5893c)-[:HAS_TRACK {name: '13', sequence: 13}]->(perf_b840386fb3f1)

// works

MERGE (person_5a55a08701ec:Person{ uuid: 'a1235272-3650-4ed7-9317-5a55a08701ec' }) 
SET person_5a55a08701ec.name = 'Lee Morgan'
SET person_5a55a08701ec.gender = 'Male'
SET person_5a55a08701ec.disambiguation = 'jazz trumpeter / composer'
SET person_5a55a08701ec.country = 'US'
SET person_5a55a08701ec.allmusic = 'https://www.allmusic.com/artist/mn0000226380'
SET person_5a55a08701ec.bbc = 'https://www.bbc.co.uk/music/artists/a1235272-3650-4ed7-9317-5a55a08701ec'
SET person_5a55a08701ec.discogs = 'https://www.discogs.com/artist/29976'
SET person_5a55a08701ec.imdb = 'https://www.imdb.com/name/nm1504323/'
SET person_5a55a08701ec.viaf = 'http://viaf.org/viaf/115064720'
SET person_5a55a08701ec.wikidata = 'https://www.wikidata.org/wiki/Q362564'
SET person_5a55a08701ec.databases = ['http://id.loc.gov/authorities/names/n81058254', 'https://catalogue.bnf.fr/ark:/12148/cb13897709j', 'https://d-nb.info/gnd/132982854', 'http://snaccooperative.org/ark:/99166/w6m92b80', 'https://rateyourmusic.com/artist/lee_morgan', 'https://www.whosampled.com/Lee-Morgan/', 'https://www.worldcat.org/identities/lccn-n81-058254']
SET person_5a55a08701ec.musicbrainz = 'https://musicbrainz.org/artist/a1235272-3650-4ed7-9317-5a55a08701ec'
SET person_5a55a08701ec.isni_list = ['http://isni.org/isni/0000000121484217']
SET person_5a55a08701ec.source = 'musicbrainz.org'


MERGE (person_250bdf3f0b3b:Person{ uuid: 'f86342be-eef7-445b-90c9-250bdf3f0b3b' }) 
SET person_250bdf3f0b3b.name = 'Sam Rivers'
SET person_250bdf3f0b3b.gender = 'Male'
SET person_250bdf3f0b3b.disambiguation = 'saxophone, flute jazz musician'
SET person_250bdf3f0b3b.country = 'US'
SET person_250bdf3f0b3b.allmusic = 'https://www.allmusic.com/artist/mn0000290775'
SET person_250bdf3f0b3b.discogs = 'https://www.discogs.com/artist/244170'
SET person_250bdf3f0b3b.viaf = 'http://viaf.org/viaf/46947488'
SET person_250bdf3f0b3b.wikidata = 'https://www.wikidata.org/wiki/Q722432'
SET person_250bdf3f0b3b.databases = ['http://id.loc.gov/authorities/names/n81035958', 'https://catalogue.bnf.fr/ark:/12148/cb13899041k', 'https://d-nb.info/gnd/134498836', 'https://rateyourmusic.com/artist/sam_rivers', 'https://www.worldcat.org/identities/lccn-n81035958']
SET person_250bdf3f0b3b.musicbrainz = 'https://musicbrainz.org/artist/f86342be-eef7-445b-90c9-250bdf3f0b3b'
SET person_250bdf3f0b3b.isni_list = ['http://isni.org/isni/0000000118332570']
SET person_250bdf3f0b3b.source = 'musicbrainz.org'


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
SET person_9ee947b4ce37.databases = ['http://id.loc.gov/authorities/names/n82164702', 'https://catalogue.bnf.fr/ark:/12148/cb138951291', 'https://d-nb.info/gnd/131961454', 'http://snaccooperative.org/ark:/99166/w6hm8fsd', 'https://nla.gov.au/nla.party-1048452', 'https://openlibrary.org/works/OL5629680A', 'https://rateyourmusic.com/artist/joe_henderson', 'https://www.worldcat.org/identities/lccn-n82164702']
SET person_9ee947b4ce37.musicbrainz = 'https://musicbrainz.org/artist/bcab8301-c7e5-4689-a4ad-9ee947b4ce37'
SET person_9ee947b4ce37.isni_list = ['http://isni.org/isni/0000000081835181']
SET person_9ee947b4ce37.source = 'musicbrainz.org'


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


MERGE (person_7cf3390253ed:Person{ uuid: 'ea39ae7d-5498-4f26-992b-7cf3390253ed' }) 
SET person_7cf3390253ed.name = 'Duke Pearson'
SET person_7cf3390253ed.gender = 'Male'
SET person_7cf3390253ed.country = 'US'
SET person_7cf3390253ed.allmusic = 'https://www.allmusic.com/artist/mn0000148559'
SET person_7cf3390253ed.discogs = 'https://www.discogs.com/artist/29955'
SET person_7cf3390253ed.viaf = 'http://viaf.org/viaf/76501134'
SET person_7cf3390253ed.wikidata = 'https://www.wikidata.org/wiki/Q1184976'
SET person_7cf3390253ed.databases = ['http://id.loc.gov/authorities/names/n88646344', 'https://catalogue.bnf.fr/ark:/12148/cb138983206', 'https://d-nb.info/gnd/134672380', 'https://rateyourmusic.com/artist/duke_pearson', 'https://www.worldcat.org/identities/lccn-n88646344']
SET person_7cf3390253ed.musicbrainz = 'https://musicbrainz.org/artist/ea39ae7d-5498-4f26-992b-7cf3390253ed'
SET person_7cf3390253ed.isni_list = ['http://isni.org/isni/000000005515186X']
SET person_7cf3390253ed.source = 'musicbrainz.org'


MERGE (person_633fafd72002:Person{ uuid: '2379937f-6e0d-46a2-b8ff-633fafd72002' }) 
SET person_633fafd72002.name = 'Wayne Shorter'
SET person_633fafd72002.gender = 'Male'
SET person_633fafd72002.disambiguation = 'US jazz saxophonist and composer'
SET person_633fafd72002.country = 'US'
SET person_633fafd72002.allmusic = 'https://www.allmusic.com/artist/mn0000250435'
SET person_633fafd72002.bbc = 'https://www.bbc.co.uk/music/artists/2379937f-6e0d-46a2-b8ff-633fafd72002'
SET person_633fafd72002.discogs = 'https://www.discogs.com/artist/29979'
SET person_633fafd72002.imdb = 'https://www.imdb.com/name/nm0795147/'
SET person_633fafd72002.viaf = 'http://viaf.org/viaf/86650174'
SET person_633fafd72002.wikidata = 'https://www.wikidata.org/wiki/Q317161'
SET person_633fafd72002.databases = ['http://id.loc.gov/authorities/names/n81014577', 'https://catalogue.bnf.fr/ark:/12148/cb138997525', 'https://d-nb.info/gnd/124938981', 'http://snaccooperative.org/ark:/99166/w63n3pcn', 'https://rateyourmusic.com/artist/wayne-shorter', 'https://www.musik-sammler.de/artist/wayne-shorter/', 'https://www.worldcat.org/identities/lccn-n81014577']
SET person_633fafd72002.musicbrainz = 'https://musicbrainz.org/artist/2379937f-6e0d-46a2-b8ff-633fafd72002'
SET person_633fafd72002.isni_list = ['http://isni.org/isni/0000000121424206']
SET person_633fafd72002.source = 'musicbrainz.org'


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


MERGE (work_54eb594be43d:Work{ uuid: 'a257122e-ac2b-45c5-a5ff-54eb594be43d' })
SET work_54eb594be43d.name = 'Song of the Whispering Banshee'
SET work_54eb594be43d.source = 'musicbrainz.org'


MERGE (work_a30c1fbf5a3c:Work{ uuid: '09343f49-4c0e-3d62-9b4e-a30c1fbf5a3c' })
SET work_a30c1fbf5a3c.name = 'Song for My Father'
SET work_a30c1fbf5a3c.iswc = 'T-070.139.880-2'
SET work_a30c1fbf5a3c.type = 'Song'
SET work_a30c1fbf5a3c.wikidata = 'https://www.wikidata.org/wiki/Q25210847'
SET work_a30c1fbf5a3c.musicbrainz = 'https://musicbrainz.org/work/09343f49-4c0e-3d62-9b4e-a30c1fbf5a3c'
SET work_a30c1fbf5a3c.source = 'musicbrainz.org'


MERGE (work_d0fe7ef7d2a2:Work{ uuid: 'bf577f85-defd-41a2-9057-d0fe7ef7d2a2' })
SET work_d0fe7ef7d2a2.name = 'Tom Thumb'
SET work_d0fe7ef7d2a2.type = 'Song'
SET work_d0fe7ef7d2a2.source = 'musicbrainz.org'


MERGE (work_57fedaf74fdf:Work{ uuid: '080aea74-5d75-4e68-acbb-57fedaf74fdf' })
SET work_57fedaf74fdf.name = 'Big Bertha'
SET work_57fedaf74fdf.source = 'musicbrainz.org'


MERGE (work_50645e17641a:Work{ uuid: 'caf84eae-d516-4855-8915-50645e17641a' })
SET work_50645e17641a.name = '20 Questions'
SET work_50645e17641a.source = 'musicbrainz.org'


MERGE (work_ee9776b45547:Work{ uuid: 'fceca67d-8dcf-36e8-8558-ee9776b45547' })
SET work_ee9776b45547.name = 'Beatrice'
SET work_ee9776b45547.type = 'Song'
SET work_ee9776b45547.source = 'musicbrainz.org'


MERGE (work_484b786fba10:Work{ uuid: '7af52106-7376-38d5-83c4-484b786fba10' })
SET work_484b786fba10.name = 'The Sidewinder'
SET work_484b786fba10.iswc = 'T-910.407.203-9'
SET work_484b786fba10.type = 'Song'
SET work_484b786fba10.wikidata = 'https://www.wikidata.org/wiki/Q17144542'
SET work_484b786fba10.musicbrainz = 'https://musicbrainz.org/work/7af52106-7376-38d5-83c4-484b786fba10'
SET work_484b786fba10.source = 'musicbrainz.org'


MERGE (work_2d4704ecd851:Work{ uuid: 'f9ef25c7-3cc2-324e-9fed-2d4704ecd851' })
SET work_2d4704ecd851.name = 'No Room for Squares'
SET work_2d4704ecd851.type = 'Song'
SET work_2d4704ecd851.source = 'musicbrainz.org'


MERGE (work_d6b590603daf:Work{ uuid: '9472de5e-6dfa-3a7c-b139-d6b590603daf' })
SET work_d6b590603daf.name = 'Ping-Pong'
SET work_d6b590603daf.source = 'musicbrainz.org'


MERGE (work_d01cda007d99:Work{ uuid: '97c692e3-8340-476d-88ac-d01cda007d99' })
SET work_d01cda007d99.name = 'Commentary on Electrical Switches'
SET work_d01cda007d99.source = 'musicbrainz.org'


MERGE (work_f55b56512451:Work{ uuid: '82643c6f-1297-4d13-b2a6-f55b56512451' })
SET work_f55b56512451.name = 'Recorda Me'
SET work_f55b56512451.iswc = 'T-070.243.116-0'
SET work_f55b56512451.type = 'Song'
SET work_f55b56512451.wikidata = 'https://www.wikidata.org/wiki/Q30594358'
SET work_f55b56512451.musicbrainz = 'https://musicbrainz.org/work/82643c6f-1297-4d13-b2a6-f55b56512451'
SET work_f55b56512451.source = 'musicbrainz.org'



// performances of
MERGE (perf_d49d3ecbbf2c)-[:PERFORMANCE_OF]->(work_54eb594be43d)
MERGE (perf_0c8ef440d52a)-[:PERFORMANCE_OF]->(work_a30c1fbf5a3c)
MERGE (perf_19d054bd4142)-[:PERFORMANCE_OF]->(work_d0fe7ef7d2a2)
MERGE (perf_e1821e97fc07)-[:PERFORMANCE_OF]->(work_57fedaf74fdf)
MERGE (perf_b840386fb3f1)-[:PERFORMANCE_OF]->(work_50645e17641a)
MERGE (perf_53aeafb147b4)-[:PERFORMANCE_OF]->(work_ee9776b45547)
MERGE (perf_18d192d82bb8)-[:PERFORMANCE_OF]->(work_484b786fba10)
MERGE (perf_eec94f94c776)-[:PERFORMANCE_OF]->(work_2d4704ecd851)
MERGE (perf_2b466aab58e6)-[:PERFORMANCE_OF]->(work_d6b590603daf)
MERGE (perf_48334528efa4)-[:PERFORMANCE_OF]->(work_d01cda007d99)
MERGE (perf_a50c9ab756f2)-[:PERFORMANCE_OF]->(work_f55b56512451)


// composers
MERGE (person_fae4c02a9a1a)-[:COMPOSED]->(work_54eb594be43d)
MERGE (person_8c848a4765b6)-[:COMPOSED]->(work_a30c1fbf5a3c)
MERGE (person_633fafd72002)-[:COMPOSED]->(work_d0fe7ef7d2a2)
MERGE (person_7cf3390253ed)-[:COMPOSED]->(work_57fedaf74fdf)
MERGE (person_08c85d96da39)-[:COMPOSED]->(work_50645e17641a)
MERGE (person_250bdf3f0b3b)-[:COMPOSED]->(work_ee9776b45547)
MERGE (person_5a55a08701ec)-[:COMPOSED]->(work_484b786fba10)
MERGE (person_107bddae77c2)-[:COMPOSED]->(work_2d4704ecd851)
MERGE (person_633fafd72002)-[:COMPOSED]->(work_d6b590603daf)
MERGE (person_c65081d12d86)-[:COMPOSED]->(work_d01cda007d99)
MERGE (person_9ee947b4ce37)-[:COMPOSED]->(work_f55b56512451)


// place nodes

MERGE (place_569fa8b97644:Place{ uuid: '1165ef7d-371c-4e03-98db-569fa8b97644' })
SET place_569fa8b97644.name = 'Van Gelder Studio'
SET place_569fa8b97644.source = 'musicbrainz.org'


// place relationships
MERGE (perf_79ff62ac1702)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_18d192d82bb8)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_2b466aab58e6)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_53aeafb147b4)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_eec94f94c776)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_0c8ef440d52a)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_19d054bd4142)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_48334528efa4)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_e1821e97fc07)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_a50c9ab756f2)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_d49d3ecbbf2c)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_0d40f0345260)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)
MERGE (perf_b840386fb3f1)-[:HAS_PLACE { type: 'recorded at', begin_date: '1999-05-10', end_date: '1999-05-11' }]->(place_569fa8b97644)

MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_79ff62ac1702)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_79ff62ac1702)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_79ff62ac1702)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_79ff62ac1702)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_79ff62ac1702)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_79ff62ac1702)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_79ff62ac1702)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_18d192d82bb8)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_18d192d82bb8)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_18d192d82bb8)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_18d192d82bb8)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_18d192d82bb8)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_18d192d82bb8)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_18d192d82bb8)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2b466aab58e6)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_2b466aab58e6)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_2b466aab58e6)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_2b466aab58e6)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_2b466aab58e6)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_2b466aab58e6)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_2b466aab58e6)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_53aeafb147b4)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_53aeafb147b4)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_53aeafb147b4)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_53aeafb147b4)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_eec94f94c776)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_eec94f94c776)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_eec94f94c776)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_eec94f94c776)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_eec94f94c776)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_eec94f94c776)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_eec94f94c776)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_0c8ef440d52a)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_0c8ef440d52a)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_0c8ef440d52a)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_0c8ef440d52a)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_0c8ef440d52a)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_0c8ef440d52a)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_0c8ef440d52a)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_19d054bd4142)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_19d054bd4142)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_19d054bd4142)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_19d054bd4142)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_19d054bd4142)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_19d054bd4142)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_19d054bd4142)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_48334528efa4)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_48334528efa4)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_48334528efa4)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_48334528efa4)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_48334528efa4)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_e1821e97fc07)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_e1821e97fc07)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_e1821e97fc07)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e1821e97fc07)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_e1821e97fc07)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_e1821e97fc07)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_e1821e97fc07)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_a50c9ab756f2)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_a50c9ab756f2)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a50c9ab756f2)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a50c9ab756f2)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_a50c9ab756f2)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_a50c9ab756f2)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a50c9ab756f2)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_d49d3ecbbf2c)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_d49d3ecbbf2c)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d49d3ecbbf2c)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_d49d3ecbbf2c)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_d49d3ecbbf2c)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_d49d3ecbbf2c)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_d49d3ecbbf2c)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_0d40f0345260)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_0d40f0345260)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_0d40f0345260)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_0d40f0345260)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_0d40f0345260)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_0d40f0345260)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_0d40f0345260)
MERGE (person_08c85d96da39)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['alto saxophone'] }]->(perf_b840386fb3f1)
MERGE (person_fae4c02a9a1a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['vibraphone'] }]->(perf_b840386fb3f1)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_b840386fb3f1)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b840386fb3f1)
MERGE (person_daf81c508719)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_b840386fb3f1)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_b840386fb3f1)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_b840386fb3f1)



"""
)