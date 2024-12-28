
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""


MERGE (release_5dcd68fba746:Release{ uuid: 'f8239dcf-a9d5-4a65-ac69-5dcd68fba746' })
SET release_5dcd68fba746.name = 'The Great Kai & J.J.'
SET release_5dcd68fba746.country = 'US'
SET release_5dcd68fba746.date = '1961'
SET release_5dcd68fba746.format = '12" Vinyl'
SET release_5dcd68fba746.discode = 'A 1'
SET release_5dcd68fba746.discogs = 'http://www.discogs.com/release/744522'
SET release_5dcd68fba746.musicbrainz = 'http://musicbrainz.org/release/f8239dcf-a9d5-4a65-ac69-5dcd68fba746'
SET release_5dcd68fba746.source = 'musicbrainz.org'


MERGE (person_bb92bb970e3e:Person{ uuid: '35a92228-a559-4235-99ee-bb92bb970e3e' })
SET person_bb92bb970e3e.name = 'Art Taylor'
SET person_bb92bb970e3e.gender = 'Male'
SET person_bb92bb970e3e.country = 'US'
SET person_bb92bb970e3e.wikipedia = 'http://en.wikipedia.org/wiki/Art_Taylor'
SET person_bb92bb970e3e.allmusic = 'http://www.allmusic.com/artist/mn0000505154'
SET person_bb92bb970e3e.discogs = 'http://www.discogs.com/artist/261196'
SET person_bb92bb970e3e.wikidata = 'http://www.wikidata.org/wiki/Q705751'
SET person_bb92bb970e3e.musicbrainz = 'https://musicbrainz.org/artist/35a92228-a559-4235-99ee-bb92bb970e3e'
SET person_bb92bb970e3e.source = 'musicbrainz.org'


MERGE (person_735169d82ebc:Person{ uuid: '45113025-9222-437f-9c57-735169d82ebc' })
SET person_735169d82ebc.name = 'Tommy Williams'
SET person_735169d82ebc.gender = 'Male'
SET person_735169d82ebc.disambiguation = 'jazz bassist'
SET person_735169d82ebc.discogs = 'http://www.discogs.com/artist/461502'
SET person_735169d82ebc.musicbrainz = 'https://musicbrainz.org/artist/45113025-9222-437f-9c57-735169d82ebc'
SET person_735169d82ebc.source = 'musicbrainz.org'


MERGE (person_f42ad7cebf1e:Person{ uuid: 'd9566c72-7ad1-410f-9f26-f42ad7cebf1e' })
SET person_f42ad7cebf1e.name = 'Kai Winding'
SET person_f42ad7cebf1e.gender = 'Male'
SET person_f42ad7cebf1e.country = 'US'
SET person_f42ad7cebf1e.wikipedia = 'http://en.wikipedia.org/wiki/Kai_Winding'
SET person_f42ad7cebf1e.viaf = 'http://viaf.org/viaf/50436655'
SET person_f42ad7cebf1e.allmusic = 'http://www.allmusic.com/artist/mn0000352164'
SET person_f42ad7cebf1e.discogs = 'http://www.discogs.com/artist/267186'
SET person_f42ad7cebf1e.imdb = 'http://www.imdb.com/name/nm0934718/'
SET person_f42ad7cebf1e.wikidata = 'http://www.wikidata.org/wiki/Q494976'
SET person_f42ad7cebf1e.databases = ['https://rateyourmusic.com/artist/kai_winding']
SET person_f42ad7cebf1e.musicbrainz = 'https://musicbrainz.org/artist/d9566c72-7ad1-410f-9f26-f42ad7cebf1e'
SET person_f42ad7cebf1e.isni_list = ['http://isni.org/isni/0000000080159265']
SET person_f42ad7cebf1e.source = 'musicbrainz.org'


MERGE (person_6c57b03a4e36:Person{ uuid: '8247a3f2-3a8e-4256-b322-6c57b03a4e36' })
SET person_6c57b03a4e36.name = 'Bill Evans'
SET person_6c57b03a4e36.gender = 'Male'
SET person_6c57b03a4e36.disambiguation = 'pianist'
SET person_6c57b03a4e36.country = 'US'
SET person_6c57b03a4e36.wikipedia = 'http://en.wikipedia.org/wiki/Bill_Evans'
SET person_6c57b03a4e36.viaf = 'http://viaf.org/viaf/29717820'
SET person_6c57b03a4e36.allmusic = 'http://www.allmusic.com/artist/mn0000764702'
SET person_6c57b03a4e36.bbc = 'http://www.bbc.co.uk/music/artists/8247a3f2-3a8e-4256-b322-6c57b03a4e36'
SET person_6c57b03a4e36.discogs = 'http://www.discogs.com/artist/252310'
SET person_6c57b03a4e36.imdb = 'http://www.imdb.com/name/nm0262572/'
SET person_6c57b03a4e36.wikidata = 'http://www.wikidata.org/wiki/Q208205'
SET person_6c57b03a4e36.discographies = ['http://www.jazztet.com/BillEvans/BillEvans-1.htm']
SET person_6c57b03a4e36.databases = ['http://d-nb.info/gnd/137724519', 'http://www.whosampled.com/Bill-Evans/', 'https://rateyourmusic.com/artist/bill_evans', 'https://www.musik-sammler.de/artist/175764/', 'https://www.worldcat.org/identities/lccn-n81-147281']
SET person_6c57b03a4e36.musicbrainz = 'https://musicbrainz.org/artist/8247a3f2-3a8e-4256-b322-6c57b03a4e36'
SET person_6c57b03a4e36.isni_list = ['http://isni.org/isni/0000000121261603']
SET person_6c57b03a4e36.source = 'musicbrainz.org'


MERGE (person_644bd536ec07:Person{ uuid: '33e50556-d4be-421b-a5d1-644bd536ec07' })
SET person_644bd536ec07.name = 'J. J. Johnson'
SET person_644bd536ec07.gender = 'Male'
SET person_644bd536ec07.disambiguation = 'Jazz/bop trombonist/session leader'
SET person_644bd536ec07.country = 'US'
SET person_644bd536ec07.wikipedia = 'http://en.wikipedia.org/wiki/J._J._Johnson'
SET person_644bd536ec07.allmusic = 'http://www.allmusic.com/artist/mn0000119111'
SET person_644bd536ec07.discogs = 'http://www.discogs.com/artist/251778'
SET person_644bd536ec07.wikidata = 'http://www.wikidata.org/wiki/Q504915'
SET person_644bd536ec07.musicbrainz = 'https://musicbrainz.org/artist/33e50556-d4be-421b-a5d1-644bd536ec07'
SET person_644bd536ec07.source = 'musicbrainz.org'


MERGE (person_6f0a331cc1ca:Person{ uuid: '2c090b57-5e9d-49c5-9b71-6f0a331cc1ca' })
SET person_6f0a331cc1ca.name = 'Roy Haynes'
SET person_6f0a331cc1ca.gender = 'Male'
SET person_6f0a331cc1ca.country = 'US'
SET person_6f0a331cc1ca.wikipedia = 'http://en.wikipedia.org/wiki/Roy_Haynes'
SET person_6f0a331cc1ca.viaf = 'http://viaf.org/viaf/84975999'
SET person_6f0a331cc1ca.allmusic = 'http://www.allmusic.com/artist/mn0000290464'
SET person_6f0a331cc1ca.bbc = 'http://www.bbc.co.uk/music/artists/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.discogs = 'http://www.discogs.com/artist/255556'
SET person_6f0a331cc1ca.imdb = 'http://www.imdb.com/name/nm0371542/'
SET person_6f0a331cc1ca.wikidata = 'http://www.wikidata.org/wiki/Q448235'
SET person_6f0a331cc1ca.musicbrainz = 'https://musicbrainz.org/artist/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.source = 'musicbrainz.org'


MERGE (person_7de13124b970:Person{ uuid: 'b6ff4fd0-03ae-41a6-942e-7de13124b970' })
SET person_7de13124b970.name = 'Paul Chambers'
SET person_7de13124b970.gender = 'Male'
SET person_7de13124b970.disambiguation = 'US jazz bassist'
SET person_7de13124b970.country = 'US'
SET person_7de13124b970.wikipedia = 'http://en.wikipedia.org/wiki/Paul_Chambers'
SET person_7de13124b970.viaf = 'http://viaf.org/viaf/100313280'
SET person_7de13124b970.discogs = 'http://www.discogs.com/artist/259778'
SET person_7de13124b970.wikidata = 'http://www.wikidata.org/wiki/Q541659'
SET person_7de13124b970.musicbrainz = 'https://musicbrainz.org/artist/b6ff4fd0-03ae-41a6-942e-7de13124b970'
SET person_7de13124b970.source = 'musicbrainz.org'

// labels

MERGE (label_8fb76f3e6ca9:Label{ uuid: '93c3b044-2b4e-4239-a73b-8fb76f3e6ca9' })
SET label_8fb76f3e6ca9.name= 'impulse!'

// performances

MERGE (perf_bf0c6229d51b:Performance{ uuid: 'b54dfcaa-8fc4-4ddf-b9f0-bf0c6229d51b' })
SET perf_bf0c6229d51b.name = 'This Could Be the Start of Something Big'
SET perf_bf0c6229d51b.duration = '3:13'
SET perf_bf0c6229d51b.begin_date = '1960-10-03'
SET perf_bf0c6229d51b.end_date = '1960-10-03'
SET perf_bf0c6229d51b.source = 'musicbrainz.org'


MERGE (perf_555dc983fc5b:Performance{ uuid: 'd7a6695d-4c20-4cf8-86d2-555dc983fc5b' })
SET perf_555dc983fc5b.name = 'Georgia on My Mind'
SET perf_555dc983fc5b.duration = '3:52'
SET perf_555dc983fc5b.source = 'musicbrainz.org'


MERGE (perf_89c7ecb707e1:Performance{ uuid: 'b824ec97-27b3-4de3-b568-89c7ecb707e1' })
SET perf_89c7ecb707e1.name = 'Blue Monk'
SET perf_89c7ecb707e1.duration = '4:32'
SET perf_89c7ecb707e1.begin_date = '1960-11-02'
SET perf_89c7ecb707e1.end_date = '1960-11-02'
SET perf_89c7ecb707e1.source = 'musicbrainz.org'


MERGE (perf_f3b3af904705:Performance{ uuid: 'c30a9aa1-f784-40e0-9c07-f3b3af904705' })
SET perf_f3b3af904705.name = 'Judy'
SET perf_f3b3af904705.duration = '4:06'
SET perf_f3b3af904705.source = 'musicbrainz.org'


MERGE (perf_d4cd60fa05f4:Performance{ uuid: 'cc5501c4-74c0-4abb-a13f-d4cd60fa05f4' })
SET perf_d4cd60fa05f4.name = 'Alone Together'
SET perf_d4cd60fa05f4.duration = '3:36'
SET perf_d4cd60fa05f4.source = 'musicbrainz.org'


MERGE (perf_87361584043c:Performance{ uuid: '3a132d78-def0-4af8-ad0b-87361584043c' })
SET perf_87361584043c.name = 'Side by Side'
SET perf_87361584043c.duration = '3:06'
SET perf_87361584043c.begin_date = '1960-11-02'
SET perf_87361584043c.end_date = '1960-11-02'
SET perf_87361584043c.source = 'musicbrainz.org'


MERGE (perf_be64f42ca793:Performance{ uuid: '25d04c4a-6038-434d-a317-be64f42ca793' })
SET perf_be64f42ca793.name = 'I Concentrate on You'
SET perf_be64f42ca793.duration = '4:04'
SET perf_be64f42ca793.begin_date = '1960-11-02'
SET perf_be64f42ca793.end_date = '1960-11-02'
SET perf_be64f42ca793.source = 'musicbrainz.org'


MERGE (perf_3714735deb41:Performance{ uuid: '447102fb-0c2b-4fe7-a3f9-3714735deb41' })
SET perf_3714735deb41.name = 'Theme From Picnic'
SET perf_3714735deb41.duration = '4:05'
SET perf_3714735deb41.source = 'musicbrainz.org'


MERGE (perf_5d03207d0665:Performance{ uuid: '6e5bf862-4e79-404c-9354-5d03207d0665' })
SET perf_5d03207d0665.name = 'Trixie'
SET perf_5d03207d0665.duration = '5:10'
SET perf_5d03207d0665.source = 'musicbrainz.org'


MERGE (perf_74acebd63633:Performance{ uuid: 'f3780a84-da2f-46cb-beee-74acebd63633' })
SET perf_74acebd63633.name = 'Going, Going, Gong!'
SET perf_74acebd63633.duration = '3:11'
SET perf_74acebd63633.source = 'musicbrainz.org'


MERGE (perf_d89c6ca47820:Performance{ uuid: '8ddca02f-d0af-4f7a-8abd-d89c6ca47820' })
SET perf_d89c6ca47820.name = 'Just for a Thrill'
SET perf_d89c6ca47820.duration = '3:18'
SET perf_d89c6ca47820.source = 'musicbrainz.org'




// labels
MERGE (release_5dcd68fba746)-[:HAS_LABEL]->(label_8fb76f3e6ca9)


// tracks
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_bf0c6229d51b)
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_555dc983fc5b)
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_89c7ecb707e1)
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'A4', sequence: 4}]->(perf_f3b3af904705)
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'A5', sequence: 5}]->(perf_d4cd60fa05f4)
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'A6', sequence: 6}]->(perf_87361584043c)
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'B1', sequence: 7}]->(perf_be64f42ca793)
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'B2', sequence: 8}]->(perf_3714735deb41)
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'B3', sequence: 9}]->(perf_5d03207d0665)
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'B4', sequence: 10}]->(perf_74acebd63633)
MERGE (release_5dcd68fba746)-[:HAS_TRACK {name: 'B5', sequence: 11}]->(perf_d89c6ca47820)

// works

MERGE (person_cd78a223724c:Person{ uuid: '765d18ec-8a76-4f6e-9c6e-cd78a223724c' })
SET person_cd78a223724c.name = 'Harry M. Woods'
SET person_cd78a223724c.gender = 'Male'
SET person_cd78a223724c.country = 'US'
SET person_cd78a223724c.wikipedia = 'http://en.wikipedia.org/wiki/Harry_M._Woods'
SET person_cd78a223724c.discogs = 'http://www.discogs.com/artist/632766'
SET person_cd78a223724c.wikidata = 'http://www.wikidata.org/wiki/Q1566366'
SET person_cd78a223724c.musicbrainz = 'https://musicbrainz.org/artist/765d18ec-8a76-4f6e-9c6e-cd78a223724c'
SET person_cd78a223724c.source = 'musicbrainz.org'


MERGE (person_e6a00ac37491:Person{ uuid: '75f6fe4b-8a7a-4f3c-9232-e6a00ac37491' })
SET person_e6a00ac37491.name = 'Hoagy Carmichael'
SET person_e6a00ac37491.gender = 'Male'
SET person_e6a00ac37491.country = 'US'
SET person_e6a00ac37491.wikipedia = 'http://en.wikipedia.org/wiki/Hoagy_Carmichael'
SET person_e6a00ac37491.viaf = 'http://viaf.org/viaf/116045429'
SET person_e6a00ac37491.allmusic = 'http://www.allmusic.com/artist/mn0000708613'
SET person_e6a00ac37491.discogs = 'http://www.discogs.com/artist/301368'
SET person_e6a00ac37491.imdb = 'http://www.imdb.com/name/nm0005994/'
SET person_e6a00ac37491.wikidata = 'http://www.wikidata.org/wiki/Q460662'
SET person_e6a00ac37491.databases = ['http://ibdb.com/person.php?id=11490', 'https://rateyourmusic.com/artist/hoagy_carmichael']
SET person_e6a00ac37491.musicbrainz = 'https://musicbrainz.org/artist/75f6fe4b-8a7a-4f3c-9232-e6a00ac37491'
SET person_e6a00ac37491.isni_list = ['http://isni.org/isni/0000000081847887']
SET person_e6a00ac37491.source = 'musicbrainz.org'


MERGE (person_5260b4274ed4:Person{ uuid: '8e8c7417-c905-46b1-b42a-5260b4274ed4' })
SET person_5260b4274ed4.name = 'Thelonious Monk'
SET person_5260b4274ed4.gender = 'Male'
SET person_5260b4274ed4.country = 'US'
SET person_5260b4274ed4.wikipedia = 'http://en.wikipedia.org/wiki/Thelonious_Monk'
SET person_5260b4274ed4.viaf = 'http://viaf.org/viaf/44485892'
SET person_5260b4274ed4.allmusic = 'http://www.allmusic.com/artist/mn0000490416'
SET person_5260b4274ed4.bbc = 'http://www.bbc.co.uk/music/artists/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.discogs = 'http://www.discogs.com/artist/145256'
SET person_5260b4274ed4.imdb = 'http://www.imdb.com/name/nm0598243/'
SET person_5260b4274ed4.wikidata = 'http://www.wikidata.org/wiki/Q109612'
SET person_5260b4274ed4.discographies = ['http://www.howardm.net/tsmonk/tsmonk.php', 'http://www.jazzdisco.org/monk/']
SET person_5260b4274ed4.databases = ['http://rateyourmusic.com/artist/thelonious_monk']
SET person_5260b4274ed4.musicbrainz = 'https://musicbrainz.org/artist/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.isni_list = ['http://isni.org/isni/0000000120249127']
SET person_5260b4274ed4.source = 'musicbrainz.org'


MERGE (person_01d7f963cfad:Person{ uuid: 'a29bbbcb-46d8-4760-93fa-01d7f963cfad' })
SET person_01d7f963cfad.name = 'Steve Allen'
SET person_01d7f963cfad.gender = 'Male'
SET person_01d7f963cfad.disambiguation = 'US actor, musician & comedian'
SET person_01d7f963cfad.country = 'US'
SET person_01d7f963cfad.wikipedia = 'http://en.wikipedia.org/wiki/Steve_Allen'
SET person_01d7f963cfad.viaf = 'http://viaf.org/viaf/110897594'
SET person_01d7f963cfad.discogs = 'http://www.discogs.com/artist/344996'
SET person_01d7f963cfad.imdb = 'http://www.imdb.com/name/nm0006752/'
SET person_01d7f963cfad.wikidata = 'http://www.wikidata.org/wiki/Q553276'
SET person_01d7f963cfad.musicbrainz = 'https://musicbrainz.org/artist/a29bbbcb-46d8-4760-93fa-01d7f963cfad'
SET person_01d7f963cfad.source = 'musicbrainz.org'


MERGE (person_23cd34f4e33b:Person{ uuid: '318ea4ad-6319-41a0-8382-23cd34f4e33b' })
SET person_23cd34f4e33b.name = 'Arthur Schwartz'
SET person_23cd34f4e33b.gender = 'Male'
SET person_23cd34f4e33b.country = 'US'
SET person_23cd34f4e33b.wikipedia = 'http://en.wikipedia.org/wiki/Arthur_Schwartz'
SET person_23cd34f4e33b.viaf = 'http://viaf.org/viaf/22332262'
SET person_23cd34f4e33b.discogs = 'http://www.discogs.com/artist/616853'
SET person_23cd34f4e33b.wikidata = 'http://www.wikidata.org/wiki/Q711473'
SET person_23cd34f4e33b.musicbrainz = 'https://musicbrainz.org/artist/318ea4ad-6319-41a0-8382-23cd34f4e33b'
SET person_23cd34f4e33b.source = 'musicbrainz.org'


MERGE (work_e289714bce83:Work{ uuid: '71f7b9a9-e51e-45dd-b9fe-e289714bce83' })
SET work_e289714bce83.name = 'This Could Be the Start of Something Big'
SET work_e289714bce83.iswc = 'T-070.179.669-1'
SET work_e289714bce83.type = 'Song'
SET work_e289714bce83.wikidata = 'http://www.wikidata.org/wiki/Q17032435'
SET work_e289714bce83.musicbrainz = 'https://musicbrainz.org/work/71f7b9a9-e51e-45dd-b9fe-e289714bce83'
SET work_e289714bce83.source = 'musicbrainz.org'


MERGE (work_172724b21666:Work{ uuid: '1140ca2b-ba16-375c-a09d-172724b21666' })
SET work_172724b21666.name = 'Georgia on My Mind'
SET work_172724b21666.iswc = 'T-801.813.912-4'
SET work_172724b21666.type = 'Song'
SET work_172724b21666.wikidata = 'http://www.wikidata.org/wiki/Q1420007'
SET work_172724b21666.musicbrainz = 'https://musicbrainz.org/work/1140ca2b-ba16-375c-a09d-172724b21666'
SET work_172724b21666.source = 'musicbrainz.org'


MERGE (work_744a53e360ba:Work{ uuid: '3e519d37-02f5-3fe4-b1ff-744a53e360ba' })
SET work_744a53e360ba.name = 'Blue Monk'
SET work_744a53e360ba.type = 'Song'
SET work_744a53e360ba.wikidata = 'http://www.wikidata.org/wiki/Q2905615'
SET work_744a53e360ba.musicbrainz = 'https://musicbrainz.org/work/3e519d37-02f5-3fe4-b1ff-744a53e360ba'
SET work_744a53e360ba.source = 'musicbrainz.org'


MERGE (work_c0498f21cc55:Work{ uuid: '0e2b553a-d9e0-4585-9f17-c0498f21cc55' })
SET work_c0498f21cc55.name = 'Judy'
SET work_c0498f21cc55.iswc = 'T-700.033.083-8'
SET work_c0498f21cc55.source = 'musicbrainz.org'


MERGE (work_4241b57b56e0:Work{ uuid: '2eeec569-6ada-3f76-8d65-4241b57b56e0' })
SET work_4241b57b56e0.name = 'Alone Together'
SET work_4241b57b56e0.iswc = 'T-070.000.952-4'
SET work_4241b57b56e0.type = 'Song'
SET work_4241b57b56e0.wikidata = 'http://www.wikidata.org/wiki/Q4734404'
SET work_4241b57b56e0.musicbrainz = 'https://musicbrainz.org/work/2eeec569-6ada-3f76-8d65-4241b57b56e0'
SET work_4241b57b56e0.source = 'musicbrainz.org'


MERGE (work_f04b6dd2030b:Work{ uuid: '1ab9a6d9-48d8-40af-a18b-f04b6dd2030b' })
SET work_f04b6dd2030b.name = 'Side by Side'
SET work_f04b6dd2030b.iswc = 'T-070.135.404-2'
SET work_f04b6dd2030b.type = 'Song'
SET work_f04b6dd2030b.wikidata = 'http://www.wikidata.org/wiki/Q7508310'
SET work_f04b6dd2030b.musicbrainz = 'https://musicbrainz.org/work/1ab9a6d9-48d8-40af-a18b-f04b6dd2030b'
SET work_f04b6dd2030b.source = 'musicbrainz.org'



// performances of
MERGE (perf_bf0c6229d51b)-[:PERFORMANCE_OF]->(work_e289714bce83)
MERGE (perf_555dc983fc5b)-[:PERFORMANCE_OF]->(work_172724b21666)
MERGE (perf_89c7ecb707e1)-[:PERFORMANCE_OF]->(work_744a53e360ba)
MERGE (perf_f3b3af904705)-[:PERFORMANCE_OF]->(work_c0498f21cc55)
MERGE (perf_d4cd60fa05f4)-[:PERFORMANCE_OF]->(work_4241b57b56e0)
MERGE (perf_87361584043c)-[:PERFORMANCE_OF]->(work_f04b6dd2030b)


// composers
MERGE (person_01d7f963cfad)-[:COMPOSED]->(work_e289714bce83)
MERGE (person_e6a00ac37491)-[:COMPOSED]->(work_172724b21666)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_744a53e360ba)
MERGE (person_644bd536ec07)-[:COMPOSED]->(work_c0498f21cc55)
MERGE (person_23cd34f4e33b)-[:COMPOSED]->(work_4241b57b56e0)
MERGE (person_cd78a223724c)-[:COMPOSED]->(work_f04b6dd2030b)


// place nodes

MERGE (place_decbb365c07f:Place{ uuid: '74e50e58-5deb-4b99-93a2-decbb365c07f' })
SET place_decbb365c07f.name = 'New York'
SET place_decbb365c07f.source = 'musicbrainz.org'


// place relationships
MERGE (perf_bf0c6229d51b)-[:HAS_PLACE { type: 'recorded in', begin_date: '1960-10-03', end_date: '1960-10-03' }]->(place_decbb365c07f)
MERGE (perf_89c7ecb707e1)-[:HAS_PLACE { type: 'recorded in', begin_date: '1960-11-02', end_date: '1960-11-02' }]->(place_decbb365c07f)
MERGE (perf_87361584043c)-[:HAS_PLACE { type: 'recorded in', begin_date: '1960-11-02', end_date: '1960-11-02' }]->(place_decbb365c07f)
MERGE (perf_be64f42ca793)-[:HAS_PLACE { type: 'recorded in', begin_date: '1960-11-02', end_date: '1960-11-02' }]->(place_decbb365c07f)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_bf0c6229d51b)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_bf0c6229d51b)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bf0c6229d51b)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_bf0c6229d51b)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_bf0c6229d51b)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_555dc983fc5b)
MERGE (person_bb92bb970e3e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_555dc983fc5b)
MERGE (person_735169d82ebc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_555dc983fc5b)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_555dc983fc5b)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_555dc983fc5b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_89c7ecb707e1)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_89c7ecb707e1)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_89c7ecb707e1)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_89c7ecb707e1)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_89c7ecb707e1)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_f3b3af904705)
MERGE (person_bb92bb970e3e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_f3b3af904705)
MERGE (person_735169d82ebc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_f3b3af904705)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f3b3af904705)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_f3b3af904705)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_d4cd60fa05f4)
MERGE (person_bb92bb970e3e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_d4cd60fa05f4)
MERGE (person_735169d82ebc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_d4cd60fa05f4)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d4cd60fa05f4)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_d4cd60fa05f4)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_87361584043c)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_87361584043c)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_87361584043c)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_87361584043c)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_87361584043c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_be64f42ca793)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_be64f42ca793)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_be64f42ca793)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_be64f42ca793)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_be64f42ca793)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_3714735deb41)
MERGE (person_bb92bb970e3e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_3714735deb41)
MERGE (person_735169d82ebc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_3714735deb41)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_3714735deb41)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_3714735deb41)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_5d03207d0665)
MERGE (person_bb92bb970e3e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_5d03207d0665)
MERGE (person_735169d82ebc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_5d03207d0665)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5d03207d0665)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_5d03207d0665)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_74acebd63633)
MERGE (person_bb92bb970e3e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_74acebd63633)
MERGE (person_735169d82ebc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_74acebd63633)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_74acebd63633)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_74acebd63633)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_d89c6ca47820)
MERGE (person_bb92bb970e3e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums'] }]->(perf_d89c6ca47820)
MERGE (person_735169d82ebc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_d89c6ca47820)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d89c6ca47820)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_d89c6ca47820)


"""
)