
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_45ed43086b8c:Release{ uuid: 'd9fd214c-86e5-400d-b829-45ed43086b8c' })
SET release_45ed43086b8c.name = 'One Night Stand: The Town Hall Concert 1947'
SET release_45ed43086b8c.country = 'US'
SET release_45ed43086b8c.date = '1997'
SET release_45ed43086b8c.format = 'CD'
SET release_45ed43086b8c.discode = 'CDP 532139'
SET release_45ed43086b8c.musicbrainz = 'http://musicbrainz.org/release/d9fd214c-86e5-400d-b829-45ed43086b8c'
SET release_45ed43086b8c.source = 'musicbrainz.org'


MERGE (person_026959d062eb:Person{ uuid: 'b3daf30a-6d84-4fe5-b1aa-026959d062eb' }) 
SET person_026959d062eb.name = 'Sadik Hakim'
SET person_026959d062eb.gender = 'Male'
SET person_026959d062eb.country = 'US'
SET person_026959d062eb.discogs = 'https://www.discogs.com/artist/1772838'
SET person_026959d062eb.discogs = 'https://www.discogs.com/artist/480264'
SET person_026959d062eb.viaf = 'http://viaf.org/viaf/12491503'
SET person_026959d062eb.wikidata = 'https://www.wikidata.org/wiki/Q2211168'
SET person_026959d062eb.wikipedia = 'https://en.wikipedia.org/wiki/Sadik_Hakim'
SET person_026959d062eb.databases = ['http://d-nb.info/gnd/134751892', 'http://id.loc.gov/authorities/names/no98012278', 'https://catalogue.bnf.fr/ark:/12148/cb13894896v', 'http://snaccooperative.org/ark:/99166/w6vn8pcc', 'https://www.worldcat.org/identities/lccn-no98012278']
SET person_026959d062eb.musicbrainz = 'https://musicbrainz.org/artist/b3daf30a-6d84-4fe5-b1aa-026959d062eb'
SET person_026959d062eb.isni_list = ['http://isni.org/isni/000000005513332X']
SET person_026959d062eb.source = 'musicbrainz.org'


MERGE (person_579480f7f7e8:Person{ uuid: 'd613e4ae-093a-49a1-b06a-579480f7f7e8' }) 
SET person_579480f7f7e8.name = 'Lester Young'
SET person_579480f7f7e8.gender = 'Male'
SET person_579480f7f7e8.disambiguation = 'saxophonist'
SET person_579480f7f7e8.country = 'US'
SET person_579480f7f7e8.allmusic = 'https://www.allmusic.com/artist/mn0000259529'
SET person_579480f7f7e8.bbc = 'https://www.bbc.co.uk/music/artists/d613e4ae-093a-49a1-b06a-579480f7f7e8'
SET person_579480f7f7e8.discogs = 'https://www.discogs.com/artist/258433'
SET person_579480f7f7e8.imdb = 'https://www.imdb.com/name/nm0949818/'
SET person_579480f7f7e8.viaf = 'http://viaf.org/viaf/46948203'
SET person_579480f7f7e8.wikidata = 'https://www.wikidata.org/wiki/Q110714'
SET person_579480f7f7e8.databases = ['http://d-nb.info/gnd/118771620', 'http://id.loc.gov/authorities/names/n81023212', 'https://catalogue.bnf.fr/ark:/12148/cb139013455', 'http://snaccooperative.org/ark:/99166/w6gq76mm', 'https://nla.gov.au/nla.party-1038762', 'https://rateyourmusic.com/artist/lester_young', 'https://www.musik-sammler.de/artist/lester-young/', 'https://www.worldcat.org/identities/lccn-n81023212']
SET person_579480f7f7e8.musicbrainz = 'https://musicbrainz.org/artist/d613e4ae-093a-49a1-b06a-579480f7f7e8'
SET person_579480f7f7e8.isni_list = ['http://isni.org/isni/0000000081255822']
SET person_579480f7f7e8.source = 'musicbrainz.org'


MERGE (person_0afaa7773881:Person{ uuid: 'e0ff9119-fdd6-4dda-bae5-0afaa7773881' }) 
SET person_0afaa7773881.name = 'Sammy Benskin'
SET person_0afaa7773881.gender = 'Male'
SET person_0afaa7773881.country = 'US'
SET person_0afaa7773881.discogs = 'https://www.discogs.com/artist/416124'
SET person_0afaa7773881.viaf = 'http://viaf.org/viaf/37107746'
SET person_0afaa7773881.wikidata = 'https://www.wikidata.org/wiki/Q2217477'
SET person_0afaa7773881.databases = ['http://id.loc.gov/authorities/names/no2005024633', 'https://catalogue.bnf.fr/ark:/12148/cb13950605j', 'http://snaccooperative.org/ark:/99166/w60b0gv8', 'https://www.worldcat.org/identities/lccn-no2005024633']
SET person_0afaa7773881.musicbrainz = 'https://musicbrainz.org/artist/e0ff9119-fdd6-4dda-bae5-0afaa7773881'
SET person_0afaa7773881.isni_list = ['http://isni.org/isni/0000000114900593']
SET person_0afaa7773881.source = 'musicbrainz.org'


MERGE (person_cd42f757accd:Person{ uuid: '6c2009bd-6389-4fcf-8fdb-cd42f757accd' }) 
SET person_cd42f757accd.name = 'Fred Lacey'
SET person_cd42f757accd.gender = 'Male'
SET person_cd42f757accd.country = 'US'
SET person_cd42f757accd.discogs = 'https://www.discogs.com/artist/671074'
SET person_cd42f757accd.musicbrainz = 'https://musicbrainz.org/artist/6c2009bd-6389-4fcf-8fdb-cd42f757accd'
SET person_cd42f757accd.source = 'musicbrainz.org'


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


MERGE (person_8dbeec4f6ef7:Person{ uuid: '744692a4-e5bc-4393-9e3d-8dbeec4f6ef7' }) 
SET person_8dbeec4f6ef7.name = 'Shorty McConnell'
SET person_8dbeec4f6ef7.gender = 'Male'
SET person_8dbeec4f6ef7.source = 'musicbrainz.org'


MERGE (person_c85fad20da55:Person{ uuid: '351d8bdf-33a1-45e2-8c04-c85fad20da55' }) 
SET person_c85fad20da55.name = 'Sarah Vaughan'
SET person_c85fad20da55.gender = 'Female'
SET person_c85fad20da55.country = 'US'
SET person_c85fad20da55.allmusic = 'https://www.allmusic.com/artist/mn0000204901'
SET person_c85fad20da55.bbc = 'https://www.bbc.co.uk/music/artists/351d8bdf-33a1-45e2-8c04-c85fad20da55'
SET person_c85fad20da55.discogs = 'https://www.discogs.com/artist/8284'
SET person_c85fad20da55.imdb = 'https://www.imdb.com/name/nm0891098/'
SET person_c85fad20da55.viaf = 'http://viaf.org/viaf/112758178'
SET person_c85fad20da55.wikidata = 'https://www.wikidata.org/wiki/Q229513'
SET person_c85fad20da55.databases = ['http://d-nb.info/gnd/119140047', 'http://id.loc.gov/authorities/names/n82019976', 'http://musicmoz.org/Bands_and_Artists/V/Vaughan,_Sarah/', 'https://catalogue.bnf.fr/ark:/12148/cb13900777n', 'http://snaccooperative.org/ark:/99166/w6cc1ksr', 'https://openlibrary.org/works/OL7220209A', 'https://rateyourmusic.com/artist/sarah_vaughan', 'https://www.musik-sammler.de/artist/sarah-vaughan/', 'https://www.worldcat.org/identities/lccn-n82019976']
SET person_c85fad20da55.musicbrainz = 'https://musicbrainz.org/artist/351d8bdf-33a1-45e2-8c04-c85fad20da55'
SET person_c85fad20da55.isni_list = ['http://isni.org/isni/0000000081802574']
SET person_c85fad20da55.source = 'musicbrainz.org'


MERGE (person_8382db5e9f31:Person{ uuid: '4b97fa95-b518-41dd-a17b-8382db5e9f31' }) 
SET person_8382db5e9f31.name = 'Rodney Richardson'
SET person_8382db5e9f31.gender = 'Male'
SET person_8382db5e9f31.country = 'US'
SET person_8382db5e9f31.allmusic = 'https://www.allmusic.com/artist/mn0000808986'
SET person_8382db5e9f31.discogs = 'https://www.discogs.com/artist/330693'
SET person_8382db5e9f31.viaf = 'http://viaf.org/viaf/7575957'
SET person_8382db5e9f31.wikidata = 'https://www.wikidata.org/wiki/Q2161188'
SET person_8382db5e9f31.databases = ['https://catalogue.bnf.fr/ark:/12148/cb13921537h']
SET person_8382db5e9f31.musicbrainz = 'https://musicbrainz.org/artist/4b97fa95-b518-41dd-a17b-8382db5e9f31'
SET person_8382db5e9f31.isni_list = ['http://isni.org/isni/0000000002767863']
SET person_8382db5e9f31.source = 'musicbrainz.org'

// labels

MERGE (label_14e1ddfd5946:Label{ uuid: '713c4a95-6616-442b-9cf6-14e1ddfd5946' })
SET label_14e1ddfd5946.name= 'Blue Note'

// performances

MERGE (perf_3606c8140558:Performance{ uuid: 'af195496-0fea-4bd0-b89a-3606c8140558' })
SET perf_3606c8140558.name = 'Lester Leaps In'
SET perf_3606c8140558.duration = '3:11'
SET perf_3606c8140558.begin_date = '1947-11-08'
SET perf_3606c8140558.end_date = '1947-11-08'
SET perf_3606c8140558.source = 'musicbrainz.org'


MERGE (perf_9d078916d034:Performance{ uuid: '005bb1f3-2bcb-498a-86d2-9d078916d034' })
SET perf_9d078916d034.name = 'Just You, Just Me'
SET perf_9d078916d034.duration = '5:22'
SET perf_9d078916d034.begin_date = '1947-11-08'
SET perf_9d078916d034.end_date = '1947-11-08'
SET perf_9d078916d034.source = 'musicbrainz.org'


MERGE (perf_6e3a1cb1351b:Performance{ uuid: '45bbcd73-2640-4308-b6e2-6e3a1cb1351b' })
SET perf_6e3a1cb1351b.name = 'Jumpin’ With Symphony Sid'
SET perf_6e3a1cb1351b.duration = '3:50'
SET perf_6e3a1cb1351b.begin_date = '1947-11-08'
SET perf_6e3a1cb1351b.end_date = '1947-11-08'
SET perf_6e3a1cb1351b.source = 'musicbrainz.org'


MERGE (perf_8a17673cc9e2:Performance{ uuid: '64842022-6e62-4135-9672-8a17673cc9e2' })
SET perf_8a17673cc9e2.name = 'Sunday'
SET perf_8a17673cc9e2.duration = '6:20'
SET perf_8a17673cc9e2.begin_date = '1947-11-08'
SET perf_8a17673cc9e2.end_date = '1947-11-08'
SET perf_8a17673cc9e2.source = 'musicbrainz.org'


MERGE (perf_37f0eb9fa0c6:Performance{ uuid: 'c336723d-e8a0-44f6-a7c4-37f0eb9fa0c6' })
SET perf_37f0eb9fa0c6.name = 'Don’t Blame Me'
SET perf_37f0eb9fa0c6.duration = '3:47'
SET perf_37f0eb9fa0c6.begin_date = '1947-11-08'
SET perf_37f0eb9fa0c6.end_date = '1947-11-08'
SET perf_37f0eb9fa0c6.source = 'musicbrainz.org'


MERGE (perf_f176562c0073:Performance{ uuid: 'bcf98a74-a981-43c2-8bf8-f176562c0073' })
SET perf_f176562c0073.name = 'My Kinda Love'
SET perf_f176562c0073.duration = '1:47'
SET perf_f176562c0073.begin_date = '1947-11-08'
SET perf_f176562c0073.end_date = '1947-11-08'
SET perf_f176562c0073.source = 'musicbrainz.org'


MERGE (perf_464e800f8514:Performance{ uuid: '74b6a81d-88e2-4cd2-b90d-464e800f8514' })
SET perf_464e800f8514.name = 'I Cover the Waterfront'
SET perf_464e800f8514.duration = '3:36'
SET perf_464e800f8514.begin_date = '1947-11-08'
SET perf_464e800f8514.end_date = '1947-11-08'
SET perf_464e800f8514.source = 'musicbrainz.org'


MERGE (perf_9abef563a68b:Performance{ uuid: '58ec4b5c-5339-4f96-a461-9abef563a68b' })
SET perf_9abef563a68b.name = 'A Ghost of a Chance'
SET perf_9abef563a68b.duration = '3:55'
SET perf_9abef563a68b.begin_date = '1947-11-08'
SET perf_9abef563a68b.end_date = '1947-11-08'
SET perf_9abef563a68b.source = 'musicbrainz.org'


MERGE (perf_372483a0f6d5:Performance{ uuid: 'b5154c1b-94dc-43c1-ba4a-372483a0f6d5' })
SET perf_372483a0f6d5.name = 'Lester’s Bebop Boogie'
SET perf_372483a0f6d5.duration = '4:53'
SET perf_372483a0f6d5.begin_date = '1947-11-08'
SET perf_372483a0f6d5.end_date = '1947-11-08'
SET perf_372483a0f6d5.source = 'musicbrainz.org'


MERGE (perf_e97beee51432:Performance{ uuid: 'a9562a45-9f93-4b55-b54e-e97beee51432' })
SET perf_e97beee51432.name = 'These Foolish Things'
SET perf_e97beee51432.duration = '4:56'
SET perf_e97beee51432.begin_date = '1947-11-08'
SET perf_e97beee51432.end_date = '1947-11-08'
SET perf_e97beee51432.source = 'musicbrainz.org'


MERGE (perf_a739023a5d20:Performance{ uuid: 'ad630215-4f1c-4ae7-ad13-a739023a5d20' })
SET perf_a739023a5d20.name = 'Movin’ With Lester'
SET perf_a739023a5d20.duration = '5:51'
SET perf_a739023a5d20.begin_date = '1947-11-08'
SET perf_a739023a5d20.end_date = '1947-11-08'
SET perf_a739023a5d20.source = 'musicbrainz.org'


MERGE (perf_931a70e567c3:Performance{ uuid: '554bf08b-8f72-4820-badb-931a70e567c3' })
SET perf_931a70e567c3.name = 'The Man I Love'
SET perf_931a70e567c3.duration = '3:33'
SET perf_931a70e567c3.begin_date = '1947-11-08'
SET perf_931a70e567c3.end_date = '1947-11-08'
SET perf_931a70e567c3.source = 'musicbrainz.org'


MERGE (perf_abfa2ed60305:Performance{ uuid: '6363cc58-7cc2-46f2-8839-abfa2ed60305' })
SET perf_abfa2ed60305.name = 'Time After Time'
SET perf_abfa2ed60305.duration = '2:52'
SET perf_abfa2ed60305.begin_date = '1947-11-08'
SET perf_abfa2ed60305.end_date = '1947-11-08'
SET perf_abfa2ed60305.source = 'musicbrainz.org'


MERGE (perf_7de25aef7438:Performance{ uuid: 'cd2c739b-1a37-4a90-b294-7de25aef7438' })
SET perf_7de25aef7438.name = 'Mean to Me'
SET perf_7de25aef7438.duration = '2:40'
SET perf_7de25aef7438.begin_date = '1947-11-08'
SET perf_7de25aef7438.end_date = '1947-11-08'
SET perf_7de25aef7438.source = 'musicbrainz.org'


MERGE (perf_a37dead6af85:Performance{ uuid: '5e1e02d7-48b5-411e-8209-a37dead6af85' })
SET perf_a37dead6af85.name = 'Body and Soul'
SET perf_a37dead6af85.duration = '4:05'
SET perf_a37dead6af85.begin_date = '1947-11-08'
SET perf_a37dead6af85.end_date = '1947-11-08'
SET perf_a37dead6af85.source = 'musicbrainz.org'


MERGE (perf_b971e0964a2c:Performance{ uuid: 'c3bf8cf2-73c7-4a98-ae75-b971e0964a2c' })
SET perf_b971e0964a2c.name = 'I Cried for You'
SET perf_b971e0964a2c.duration = '3:46'
SET perf_b971e0964a2c.begin_date = '1947-11-08'
SET perf_b971e0964a2c.end_date = '1947-11-08'
SET perf_b971e0964a2c.source = 'musicbrainz.org'




// labels
MERGE (release_45ed43086b8c)-[:HAS_LABEL]->(label_14e1ddfd5946)


// tracks
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_3606c8140558)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_9d078916d034)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_6e3a1cb1351b)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_8a17673cc9e2)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_37f0eb9fa0c6)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_f176562c0073)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_464e800f8514)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_9abef563a68b)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_372483a0f6d5)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_e97beee51432)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '11', sequence: 11}]->(perf_a739023a5d20)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '12', sequence: 12}]->(perf_931a70e567c3)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '13', sequence: 13}]->(perf_abfa2ed60305)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '14', sequence: 14}]->(perf_7de25aef7438)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '15', sequence: 15}]->(perf_a37dead6af85)
MERGE (release_45ed43086b8c)-[:HAS_TRACK {name: '16', sequence: 16}]->(perf_b971e0964a2c)

// works

MERGE (person_3fbbe73d09b4:Person{ uuid: '1b3a1e49-2494-441c-9818-3fbbe73d09b4' }) 
SET person_3fbbe73d09b4.name = 'Jule Styne'
SET person_3fbbe73d09b4.gender = 'Male'
SET person_3fbbe73d09b4.country = 'GB'
SET person_3fbbe73d09b4.allmusic = 'https://www.allmusic.com/artist/mn0000304458'
SET person_3fbbe73d09b4.discogs = 'https://www.discogs.com/artist/341663'
SET person_3fbbe73d09b4.imdb = 'https://www.imdb.com/name/nm0006312/'
SET person_3fbbe73d09b4.viaf = 'http://viaf.org/viaf/94213715'
SET person_3fbbe73d09b4.wikidata = 'https://www.wikidata.org/wiki/Q587741'
SET person_3fbbe73d09b4.databases = ['http://d-nb.info/gnd/121819604', 'http://id.loc.gov/authorities/names/n81120322', 'https://catalogue.bnf.fr/ark:/12148/cb13900158q', 'https://ibdb.com/person.php?id=12466', 'http://snaccooperative.org/ark:/99166/w6gb25xj', 'https://nla.gov.au/nla.party-1196551', 'https://openlibrary.org/works/OL575686A', 'https://rateyourmusic.com/artist/jule_styne', 'https://www.worldcat.org/identities/lccn-n81120322/']
SET person_3fbbe73d09b4.musicbrainz = 'https://musicbrainz.org/artist/1b3a1e49-2494-441c-9818-3fbbe73d09b4'
SET person_3fbbe73d09b4.isni_list = ['http://isni.org/isni/0000000114778217']
SET person_3fbbe73d09b4.source = 'musicbrainz.org'


MERGE (person_322e34240ffc:Person{ uuid: '509086c2-9cc8-4e77-89e9-322e34240ffc' }) 
SET person_322e34240ffc.name = 'Ira Gershwin'
SET person_322e34240ffc.gender = 'Male'
SET person_322e34240ffc.country = 'US'
SET person_322e34240ffc.allmusic = 'https://www.allmusic.com/artist/mn0000200301'
SET person_322e34240ffc.discogs = 'https://www.discogs.com/artist/264105'
SET person_322e34240ffc.imdb = 'https://www.imdb.com/name/nm0314857/'
SET person_322e34240ffc.viaf = 'http://viaf.org/viaf/39519496'
SET person_322e34240ffc.wikidata = 'https://www.wikidata.org/wiki/Q61059'
SET person_322e34240ffc.databases = ['http://d-nb.info/gnd/119500027', 'http://id.loc.gov/authorities/names/n50076010', 'https://catalogue.bnf.fr/ark:/12148/cb13194929s', 'https://ibdb.com/person.php?id=6435', 'http://snaccooperative.org/ark:/99166/w60w94tm', 'https://nla.gov.au/nla.party-965252', 'https://openlibrary.org/works/OL233692A', 'https://rateyourmusic.com/artist/ira_gershwin', 'https://www.worldcat.org/identities/lccn-n50076010/']
SET person_322e34240ffc.musicbrainz = 'https://musicbrainz.org/artist/509086c2-9cc8-4e77-89e9-322e34240ffc'
SET person_322e34240ffc.isni_list = ['http://isni.org/isni/0000000108901469']
SET person_322e34240ffc.source = 'musicbrainz.org'


MERGE (person_afa0632abd19:Person{ uuid: '7c0e243d-30e5-472f-b5db-afa0632abd19' }) 
SET person_afa0632abd19.name = 'Harry Link'
SET person_afa0632abd19.gender = 'Male'
SET person_afa0632abd19.disambiguation = 'US vaudeville actor & songwriter'
SET person_afa0632abd19.country = 'US'
SET person_afa0632abd19.allmusic = 'https://www.allmusic.com/artist/mn0000664719'
SET person_afa0632abd19.discogs = 'https://www.discogs.com/artist/669135'
SET person_afa0632abd19.viaf = 'http://viaf.org/viaf/4610991'
SET person_afa0632abd19.wikidata = 'https://www.wikidata.org/wiki/Q5670641'
SET person_afa0632abd19.databases = ['http://id.loc.gov/authorities/names/no2003007529', 'https://nla.gov.au/nla.party-1528905', 'https://www.ibdb.com/person.php?id=75589', 'https://www.worldcat.org/identities/lccn-no2003007529/']
SET person_afa0632abd19.musicbrainz = 'https://musicbrainz.org/artist/7c0e243d-30e5-472f-b5db-afa0632abd19'
SET person_afa0632abd19.isni_list = ['http://isni.org/isni/0000000109502857']
SET person_afa0632abd19.source = 'musicbrainz.org'


MERGE (person_5bf00afc3eaf:Person{ uuid: 'a13ede92-5e64-43ac-a5a6-5bf00afc3eaf' }) 
SET person_5bf00afc3eaf.name = 'Eric Maschwitz'
SET person_5bf00afc3eaf.gender = 'Male'
SET person_5bf00afc3eaf.country = 'GB'
SET person_5bf00afc3eaf.allmusic = 'https://www.allmusic.com/artist/mn0000824948'
SET person_5bf00afc3eaf.discogs = 'https://www.discogs.com/artist/669134'
SET person_5bf00afc3eaf.discogs = 'https://www.discogs.com/artist/693833'
SET person_5bf00afc3eaf.imdb = 'https://www.imdb.com/name/nm0556178/'
SET person_5bf00afc3eaf.viaf = 'http://viaf.org/viaf/23153688'
SET person_5bf00afc3eaf.wikidata = 'https://www.wikidata.org/wiki/Q1351469'
SET person_5bf00afc3eaf.databases = ['http://d-nb.info/gnd/12715051X', 'http://id.loc.gov/authorities/names/n85151644', 'https://catalogue.bnf.fr/ark:/12148/cb14768955v', 'http://snaccooperative.org/ark:/99166/w6f4812k', 'https://nla.gov.au/nla.party-1201885', 'https://openlibrary.org/works/OL2300851A', 'https://www.ibdb.com/person.php?id=86572', 'https://www.worldcat.org/identities/lccn-n85151644/']
SET person_5bf00afc3eaf.musicbrainz = 'https://musicbrainz.org/artist/a13ede92-5e64-43ac-a5a6-5bf00afc3eaf'
SET person_5bf00afc3eaf.isni_list = ['http://isni.org/isni/0000000108790113', 'http://isni.org/isni/0000000109502208']
SET person_5bf00afc3eaf.source = 'musicbrainz.org'


MERGE (person_0229920db798:Person{ uuid: '15e3114e-19f8-4222-a585-0229920db798' }) 
SET person_0229920db798.name = 'Fred Ahlert'
SET person_0229920db798.gender = 'Male'
SET person_0229920db798.country = 'US'
SET person_0229920db798.discogs = 'https://www.discogs.com/artist/699210'
SET person_0229920db798.imdb = 'https://www.imdb.com/name/nm0013997/'
SET person_0229920db798.viaf = 'http://viaf.org/viaf/29716449'
SET person_0229920db798.wikidata = 'https://www.wikidata.org/wiki/Q4347908'
SET person_0229920db798.databases = ['http://id.loc.gov/authorities/names/no93031859', 'https://catalogue.bnf.fr/ark:/12148/cb13786784p', 'http://snaccooperative.org/ark:/99166/w6n31c31', 'https://nla.gov.au/nla.party-1497118', 'https://www.ibdb.com/person.php?id=11295', 'https://www.worldcat.org/identities/lccn-no93031859/']
SET person_0229920db798.musicbrainz = 'https://musicbrainz.org/artist/15e3114e-19f8-4222-a585-0229920db798'
SET person_0229920db798.isni_list = ['http://isni.org/isni/0000000073574495']
SET person_0229920db798.source = 'musicbrainz.org'


MERGE (person_36cedde0ce66:Person{ uuid: '80cb9ce6-e1c7-4211-91fa-36cedde0ce66' }) 
SET person_36cedde0ce66.name = 'Arthur Freed'
SET person_36cedde0ce66.gender = 'Male'
SET person_36cedde0ce66.country = 'US'
SET person_36cedde0ce66.allmusic = 'https://www.allmusic.com/artist/mn0000604999'
SET person_36cedde0ce66.discogs = 'https://www.discogs.com/artist/555147'
SET person_36cedde0ce66.imdb = 'https://www.imdb.com/name/nm0006085/'
SET person_36cedde0ce66.viaf = 'http://viaf.org/viaf/94212060'
SET person_36cedde0ce66.wikidata = 'https://www.wikidata.org/wiki/Q709413'
SET person_36cedde0ce66.databases = ['http://d-nb.info/gnd/124876900', 'http://id.loc.gov/authorities/names/n84163297', 'https://catalogue.bnf.fr/ark:/12148/cb13939239h', 'http://snaccooperative.org/ark:/99166/w6d51fg9', 'https://rateyourmusic.com/artist/arthur-freed', 'https://www.ibdb.com/person.php?id=11694', 'https://www.worldcat.org/identities/lccn-n84163297/']
SET person_36cedde0ce66.musicbrainz = 'https://musicbrainz.org/artist/80cb9ce6-e1c7-4211-91fa-36cedde0ce66'
SET person_36cedde0ce66.isni_list = ['http://isni.org/isni/0000000046248838', 'http://isni.org/isni/0000000116886801']
SET person_36cedde0ce66.source = 'musicbrainz.org'


MERGE (person_f0917b4fc06d:Person{ uuid: '30305a68-ba45-42b6-8f25-f0917b4fc06d' }) 
SET person_f0917b4fc06d.name = 'Roy Turk'
SET person_f0917b4fc06d.gender = 'Male'
SET person_f0917b4fc06d.country = 'US'
SET person_f0917b4fc06d.allmusic = 'https://www.allmusic.com/artist/mn0000354663'
SET person_f0917b4fc06d.discogs = 'https://www.discogs.com/artist/642080'
SET person_f0917b4fc06d.imdb = 'https://www.imdb.com/name/nm0877172/'
SET person_f0917b4fc06d.viaf = 'http://viaf.org/viaf/27332876'
SET person_f0917b4fc06d.wikidata = 'https://www.wikidata.org/wiki/Q984231'
SET person_f0917b4fc06d.databases = ['http://d-nb.info/gnd/141387807', 'http://id.loc.gov/authorities/names/no89009291', 'https://catalogue.bnf.fr/ark:/12148/cb14838832g', 'http://snaccooperative.org/ark:/99166/w6vx1x7k', 'https://nla.gov.au/nla.party-1510092', 'https://www.ibdb.com/person.php?id=13381', 'https://www.worldcat.org/identities/lccn-no89009291/']
SET person_f0917b4fc06d.musicbrainz = 'https://musicbrainz.org/artist/30305a68-ba45-42b6-8f25-f0917b4fc06d'
SET person_f0917b4fc06d.isni_list = ['http://isni.org/isni/0000000078279663']
SET person_f0917b4fc06d.source = 'musicbrainz.org'


MERGE (person_1bfdeb0d8097:Person{ uuid: '3ffb3594-ac72-4ed6-ae66-1bfdeb0d8097' }) 
SET person_1bfdeb0d8097.name = 'Jo Trent'
SET person_1bfdeb0d8097.gender = 'Male'
SET person_1bfdeb0d8097.country = 'US'
SET person_1bfdeb0d8097.discogs = 'https://www.discogs.com/artist/643489'
SET person_1bfdeb0d8097.imdb = 'https://www.imdb.com/name/nm0872151/'
SET person_1bfdeb0d8097.musicbrainz = 'https://musicbrainz.org/artist/3ffb3594-ac72-4ed6-ae66-1bfdeb0d8097'
SET person_1bfdeb0d8097.source = 'musicbrainz.org'


MERGE (person_b693a808a158:Person{ uuid: '65744963-191a-44ef-a3c7-b693a808a158' }) 
SET person_b693a808a158.name = 'George Gershwin'
SET person_b693a808a158.gender = 'Male'
SET person_b693a808a158.disambiguation = 'composer'
SET person_b693a808a158.country = 'US'
SET person_b693a808a158.allmusic = 'https://www.allmusic.com/artist/mn0000197918'
SET person_b693a808a158.bbc = 'https://www.bbc.co.uk/music/artists/65744963-191a-44ef-a3c7-b693a808a158'
SET person_b693a808a158.discogs = 'https://www.discogs.com/artist/261293'
SET person_b693a808a158.imdb = 'https://www.imdb.com/name/nm0006097/'
SET person_b693a808a158.viaf = 'http://viaf.org/viaf/61554329'
SET person_b693a808a158.wikidata = 'https://www.wikidata.org/wiki/Q123829'
SET person_b693a808a158.databases = ['http://d-nb.info/gnd/118639226', 'http://id.loc.gov/authorities/names/n79077265', 'https://catalogue.bnf.fr/ark:/12148/cb119493251', 'https://ibdb.com/person.php?id=5813', 'http://snaccooperative.org/ark:/99166/w6x065dx', 'https://nla.gov.au/nla.party-832382', 'https://openlibrary.org/works/OL67761A', 'http://soundtrackcollector.com/composer/33/', 'https://rateyourmusic.com/artist/george_gershwin', 'https://www.worldcat.org/identities/lccn-n79077265']
SET person_b693a808a158.musicbrainz = 'https://musicbrainz.org/artist/65744963-191a-44ef-a3c7-b693a808a158'
SET person_b693a808a158.isni_list = ['http://isni.org/isni/0000000121355968']
SET person_b693a808a158.source = 'musicbrainz.org'


MERGE (person_0cdf22c48565:Person{ uuid: '338f9d5d-9327-4f01-bb99-0cdf22c48565' }) 
SET person_0cdf22c48565.name = 'Victor Young'
SET person_0cdf22c48565.gender = 'Male'
SET person_0cdf22c48565.disambiguation = 'American composer, arranger, violinist & conductor'
SET person_0cdf22c48565.country = 'US'
SET person_0cdf22c48565.allmusic = 'https://www.allmusic.com/artist/mn0000959775'
SET person_0cdf22c48565.discogs = 'https://www.discogs.com/artist/370725'
SET person_0cdf22c48565.imdb = 'https://www.imdb.com/name/nm0000082/'
SET person_0cdf22c48565.viaf = 'http://viaf.org/viaf/100232829'
SET person_0cdf22c48565.wikidata = 'https://www.wikidata.org/wiki/Q365199'
SET person_0cdf22c48565.databases = ['http://d-nb.info/gnd/133160297', 'http://id.loc.gov/authorities/names/n87911854', 'https://catalogue.bnf.fr/ark:/12148/cb139013544', 'https://ibdb.com/person.php?id=12609', 'http://snaccooperative.org/ark:/99166/w6862fdw', 'https://nla.gov.au/nla.party-1140987', 'https://openlibrary.org/works/OL7177117A', 'http://soundtrackcollector.com/composer/47/', 'https://rateyourmusic.com/artist/victor_young', 'https://www.45worlds.com/78rpm/artist/victor-young', 'https://www.worldcat.org/identities/lccn-n87911854/']
SET person_0cdf22c48565.musicbrainz = 'https://musicbrainz.org/artist/338f9d5d-9327-4f01-bb99-0cdf22c48565'
SET person_0cdf22c48565.isni_list = ['http://isni.org/isni/0000000116917487']
SET person_0cdf22c48565.source = 'musicbrainz.org'


MERGE (person_e5f1cc0ea99b:Person{ uuid: 'a216236e-fc6f-4d48-ab57-e5f1cc0ea99b' }) 
SET person_e5f1cc0ea99b.name = 'Jesse Greer'
SET person_e5f1cc0ea99b.gender = 'Male'
SET person_e5f1cc0ea99b.country = 'US'
SET person_e5f1cc0ea99b.discogs = 'https://www.discogs.com/artist/830473'
SET person_e5f1cc0ea99b.imdb = 'https://www.imdb.com/name/nm0339455/'
SET person_e5f1cc0ea99b.viaf = 'http://viaf.org/viaf/104152701'
SET person_e5f1cc0ea99b.wikidata = 'https://www.wikidata.org/wiki/Q16006764'
SET person_e5f1cc0ea99b.databases = ['http://id.loc.gov/authorities/names/no96063299', 'https://catalogue.bnf.fr/ark:/12148/cb13797386q', 'https://nla.gov.au/nla.party-1529396', 'https://www.ibdb.com/person.php?id=11791', 'https://www.worldcat.org/identities/lccn-no96063299/']
SET person_e5f1cc0ea99b.musicbrainz = 'https://musicbrainz.org/artist/a216236e-fc6f-4d48-ab57-e5f1cc0ea99b'
SET person_e5f1cc0ea99b.isni_list = ['http://isni.org/isni/0000000078233358']
SET person_e5f1cc0ea99b.source = 'musicbrainz.org'


MERGE (person_2a20254ed520:Person{ uuid: 'c414371b-3377-43b5-9dc2-2a20254ed520' }) 
SET person_2a20254ed520.name = 'Jimmy McHugh'
SET person_2a20254ed520.gender = 'Male'
SET person_2a20254ed520.disambiguation = 'songwriter'
SET person_2a20254ed520.country = 'US'
SET person_2a20254ed520.discogs = 'https://www.discogs.com/artist/556382'
SET person_2a20254ed520.imdb = 'https://www.imdb.com/name/nm0006192/'
SET person_2a20254ed520.viaf = 'http://viaf.org/viaf/22334801'
SET person_2a20254ed520.wikidata = 'https://www.wikidata.org/wiki/Q1283031'
SET person_2a20254ed520.databases = ['http://d-nb.info/gnd/134679156', 'http://id.loc.gov/authorities/names/n81024655', 'https://catalogue.bnf.fr/ark:/12148/cb13962828f', 'http://snaccooperative.org/ark:/99166/w6v98r52', 'https://nla.gov.au/nla.party-906683', 'https://openlibrary.org/works/OL1257660A', 'https://www.ibdb.com/person.php?id=12130', 'https://www.worldcat.org/identities/lccn-n81024655/']
SET person_2a20254ed520.musicbrainz = 'https://musicbrainz.org/artist/c414371b-3377-43b5-9dc2-2a20254ed520'
SET person_2a20254ed520.isni_list = ['http://isni.org/isni/0000000115621158']
SET person_2a20254ed520.source = 'musicbrainz.org'


MERGE (person_ed56a0d6c7fc:Person{ uuid: 'c24c5333-1e31-4971-b786-ed56a0d6c7fc' }) 
SET person_ed56a0d6c7fc.name = 'Gus Arnheim'
SET person_ed56a0d6c7fc.gender = 'Male'
SET person_ed56a0d6c7fc.country = 'US'
SET person_ed56a0d6c7fc.discogs = 'https://www.discogs.com/artist/675269'
SET person_ed56a0d6c7fc.imdb = 'https://www.imdb.com/name/nm0036280/'
SET person_ed56a0d6c7fc.wikidata = 'https://www.wikidata.org/wiki/Q135420'
SET person_ed56a0d6c7fc.wikipedia = 'https://en.wikipedia.org/wiki/Gus_Arnheim'
SET person_ed56a0d6c7fc.musicbrainz = 'https://musicbrainz.org/artist/c24c5333-1e31-4971-b786-ed56a0d6c7fc'
SET person_ed56a0d6c7fc.source = 'musicbrainz.org'


MERGE (person_cae1b1c6362f:Person{ uuid: '9a775c6e-9346-4b16-a611-cae1b1c6362f' }) 
SET person_cae1b1c6362f.name = 'Dorothy Fields'
SET person_cae1b1c6362f.gender = 'Female'
SET person_cae1b1c6362f.disambiguation = 'US Tin Pan Alley librettist and lyricist'
SET person_cae1b1c6362f.country = 'US'
SET person_cae1b1c6362f.discogs = 'https://www.discogs.com/artist/301992'
SET person_cae1b1c6362f.imdb = 'https://www.imdb.com/name/nm0276227/'
SET person_cae1b1c6362f.viaf = 'http://viaf.org/viaf/59268144'
SET person_cae1b1c6362f.wikidata = 'https://www.wikidata.org/wiki/Q435241'
SET person_cae1b1c6362f.databases = ['http://d-nb.info/gnd/120891735', 'http://id.loc.gov/authorities/names/n81023046', 'https://catalogue.bnf.fr/ark:/12148/cb137951840', 'http://snaccooperative.org/ark:/99166/w6hf8jtc', 'https://nla.gov.au/nla.party-956142', 'https://openlibrary.org/works/OL2263030A', 'https://www.ibdb.com/person.php?id=5113', 'https://www.worldcat.org/identities/lccn-n81023046/']
SET person_cae1b1c6362f.musicbrainz = 'https://musicbrainz.org/artist/9a775c6e-9346-4b16-a611-cae1b1c6362f'
SET person_cae1b1c6362f.isni_list = ['http://isni.org/isni/0000000081386224']
SET person_cae1b1c6362f.source = 'musicbrainz.org'


MERGE (person_e9385c4e43f8:Person{ uuid: 'f84eb94a-1953-4955-94bc-e9385c4e43f8' }) 
SET person_e9385c4e43f8.name = 'Johnny Green'
SET person_e9385c4e43f8.gender = 'Male'
SET person_e9385c4e43f8.disambiguation = 'composer and conductor, often credited as John Green'
SET person_e9385c4e43f8.country = 'US'
SET person_e9385c4e43f8.allmusic = 'https://www.allmusic.com/artist/mn0000820706'
SET person_e9385c4e43f8.discogs = 'https://www.discogs.com/artist/299701'
SET person_e9385c4e43f8.discogs = 'https://www.discogs.com/artist/834272'
SET person_e9385c4e43f8.imdb = 'https://www.imdb.com/name/nm0338004/'
SET person_e9385c4e43f8.viaf = 'http://viaf.org/viaf/76502811'
SET person_e9385c4e43f8.wikidata = 'https://www.wikidata.org/wiki/Q664592'
SET person_e9385c4e43f8.databases = ['http://d-nb.info/gnd/134265823', 'http://id.loc.gov/authorities/names/n81072979', 'https://catalogue.bnf.fr/ark:/12148/cb138267582', 'http://snaccooperative.org/ark:/99166/w63x93pp', 'https://nla.gov.au/nla.party-1079558', 'https://rateyourmusic.com/artist/johnny_green', 'https://www.ibdb.com/person.php?id=11785', 'https://www.worldcat.org/identities/lccn-n81072979/']
SET person_e9385c4e43f8.musicbrainz = 'https://musicbrainz.org/artist/f84eb94a-1953-4955-94bc-e9385c4e43f8'
SET person_e9385c4e43f8.isni_list = ['http://isni.org/isni/0000000116755641']
SET person_e9385c4e43f8.source = 'musicbrainz.org'


MERGE (person_22ada2e4e284:Person{ uuid: '7f56e48d-50d8-441d-a346-22ada2e4e284' }) 
SET person_22ada2e4e284.name = 'Robert Sour'
SET person_22ada2e4e284.country = 'US'
SET person_22ada2e4e284.discogs = 'https://www.discogs.com/artist/629470'
SET person_22ada2e4e284.imdb = 'https://www.imdb.com/name/nm0815916/'
SET person_22ada2e4e284.viaf = 'http://viaf.org/viaf/87836313'
SET person_22ada2e4e284.wikidata = 'https://www.wikidata.org/wiki/Q6184411'
SET person_22ada2e4e284.wikipedia = 'https://en.wikipedia.org/wiki/Robert_Sour'
SET person_22ada2e4e284.musicbrainz = 'https://musicbrainz.org/artist/7f56e48d-50d8-441d-a346-22ada2e4e284'
SET person_22ada2e4e284.source = 'musicbrainz.org'


MERGE (person_d65a9f32875b:Person{ uuid: '7c68a2be-951e-4b9a-807f-d65a9f32875b' }) 
SET person_d65a9f32875b.name = 'Raymond Klages'
SET person_d65a9f32875b.gender = 'Male'
SET person_d65a9f32875b.country = 'US'
SET person_d65a9f32875b.discogs = 'https://www.discogs.com/artist/830470'
SET person_d65a9f32875b.imdb = 'https://www.imdb.com/name/nm0458176/'
SET person_d65a9f32875b.musicbrainz = 'https://musicbrainz.org/artist/7c68a2be-951e-4b9a-807f-d65a9f32875b'
SET person_d65a9f32875b.source = 'musicbrainz.org'


MERGE (person_4508a4b0db32:Person{ uuid: '2d4bc2de-8c9b-4006-945b-4508a4b0db32' }) 
SET person_4508a4b0db32.name = 'Frank Eyton'
SET person_4508a4b0db32.country = 'GB'
SET person_4508a4b0db32.discogs = 'https://www.discogs.com/artist/629475'
SET person_4508a4b0db32.viaf = 'http://viaf.org/viaf/6860143'
SET person_4508a4b0db32.wikidata = 'https://www.wikidata.org/wiki/Q5486519'
SET person_4508a4b0db32.wikipedia = 'https://en.wikipedia.org/wiki/Frank_Eyton'
SET person_4508a4b0db32.musicbrainz = 'https://musicbrainz.org/artist/2d4bc2de-8c9b-4006-945b-4508a4b0db32'
SET person_4508a4b0db32.source = 'musicbrainz.org'


MERGE (person_91000e35bc46:Person{ uuid: '8ba56dd4-a9e1-410f-9b1e-91000e35bc46' }) 
SET person_91000e35bc46.name = 'Edward Heyman'
SET person_91000e35bc46.gender = 'Male'
SET person_91000e35bc46.country = 'US'
SET person_91000e35bc46.allmusic = 'https://www.allmusic.com/artist/mn0000795422'
SET person_91000e35bc46.discogs = 'https://www.discogs.com/artist/607246'
SET person_91000e35bc46.imdb = 'https://www.imdb.com/name/nm0382269/'
SET person_91000e35bc46.viaf = 'http://viaf.org/viaf/118204894'
SET person_91000e35bc46.wikidata = 'https://www.wikidata.org/wiki/Q4355574'
SET person_91000e35bc46.databases = ['http://d-nb.info/gnd/139673237', 'http://id.loc.gov/authorities/names/n86140056', 'https://catalogue.bnf.fr/ark:/12148/cb14838432c', 'http://snaccooperative.org/ark:/99166/w6m91467', 'https://nla.gov.au/nla.party-844812', 'https://rateyourmusic.com/artist/edward_heyman', 'https://www.ibdb.com/person.php?id=11852', 'https://www.worldcat.org/identities/lccn-n86140056/']
SET person_91000e35bc46.musicbrainz = 'https://musicbrainz.org/artist/8ba56dd4-a9e1-410f-9b1e-91000e35bc46'
SET person_91000e35bc46.isni_list = ['http://isni.org/isni/000000012148820X']
SET person_91000e35bc46.source = 'musicbrainz.org'


MERGE (person_b90d9d7fcf8f:Person{ uuid: '2437980f-513a-44fc-80f1-b90d9d7fcf8f' }) 
SET person_b90d9d7fcf8f.name = 'Bing Crosby'
SET person_b90d9d7fcf8f.gender = 'Male'
SET person_b90d9d7fcf8f.country = 'US'
SET person_b90d9d7fcf8f.allmusic = 'https://www.allmusic.com/artist/mn0000094252'
SET person_b90d9d7fcf8f.bbc = 'https://www.bbc.co.uk/music/artists/2437980f-513a-44fc-80f1-b90d9d7fcf8f'
SET person_b90d9d7fcf8f.discogs = 'https://www.discogs.com/artist/164571'
SET person_b90d9d7fcf8f.discogs = 'https://www.discogs.com/artist/4363198'
SET person_b90d9d7fcf8f.imdb = 'https://www.imdb.com/name/nm0001078/'
SET person_b90d9d7fcf8f.viaf = 'http://viaf.org/viaf/12394764'
SET person_b90d9d7fcf8f.wikidata = 'https://www.wikidata.org/wiki/Q72984'
SET person_b90d9d7fcf8f.databases = ['http://d-nb.info/gnd/118677411', 'http://id.loc.gov/authorities/names/n50018853', 'https://catalogue.bnf.fr/ark:/12148/cb124083942', 'https://ibdb.com/person.php?id=89150', 'http://snaccooperative.org/ark:/99166/w6k361xx', 'https://nla.gov.au/nla.party-1159314', 'https://openlibrary.org/works/OL840188A', 'https://rateyourmusic.com/artist/bing_crosby', 'https://www.worldcat.org/identities/lccn-n50018853']
SET person_b90d9d7fcf8f.musicbrainz = 'https://musicbrainz.org/artist/2437980f-513a-44fc-80f1-b90d9d7fcf8f'
SET person_b90d9d7fcf8f.isni_list = ['http://isni.org/isni/0000000108706364']
SET person_b90d9d7fcf8f.source = 'musicbrainz.org'


MERGE (person_9ecd8b2daa0d:Person{ uuid: '0fb41597-d1a0-480c-93f3-9ecd8b2daa0d' }) 
SET person_9ecd8b2daa0d.name = 'Ned Washington'
SET person_9ecd8b2daa0d.gender = 'Male'
SET person_9ecd8b2daa0d.country = 'US'
SET person_9ecd8b2daa0d.allmusic = 'https://www.allmusic.com/artist/mn0000324645'
SET person_9ecd8b2daa0d.discogs = 'https://www.discogs.com/artist/299280'
SET person_9ecd8b2daa0d.imdb = 'https://www.imdb.com/name/nm0913513/'
SET person_9ecd8b2daa0d.viaf = 'http://viaf.org/viaf/69121638'
SET person_9ecd8b2daa0d.wikidata = 'https://www.wikidata.org/wiki/Q1973924'
SET person_9ecd8b2daa0d.databases = ['http://d-nb.info/gnd/130173606', 'http://id.loc.gov/authorities/names/no89006651', 'https://catalogue.bnf.fr/ark:/12148/cb13952962p', 'http://snaccooperative.org/ark:/99166/w6g73q46', 'https://nla.gov.au/nla.party-1494135', 'https://openlibrary.org/works/OL363737A', 'https://rateyourmusic.com/artist/ned_washington', 'https://www.ibdb.com/person.php?id=12550', 'https://www.worldcat.org/identities/lccn-no89006651/']
SET person_9ecd8b2daa0d.musicbrainz = 'https://musicbrainz.org/artist/0fb41597-d1a0-480c-93f3-9ecd8b2daa0d'
SET person_9ecd8b2daa0d.isni_list = ['http://isni.org/isni/0000000081490873']
SET person_9ecd8b2daa0d.source = 'musicbrainz.org'


MERGE (person_4fa2a31227f1:Person{ uuid: '684348fd-551d-4c45-a1da-4fa2a31227f1' }) 
SET person_4fa2a31227f1.name = 'Abe Lyman'
SET person_4fa2a31227f1.gender = 'Male'
SET person_4fa2a31227f1.country = 'US'
SET person_4fa2a31227f1.allmusic = 'https://www.allmusic.com/artist/mn0000588065'
SET person_4fa2a31227f1.discogs = 'https://www.discogs.com/artist/688773'
SET person_4fa2a31227f1.imdb = 'https://www.imdb.com/name/nm0528139/'
SET person_4fa2a31227f1.viaf = 'http://viaf.org/viaf/24787825'
SET person_4fa2a31227f1.wikidata = 'https://www.wikidata.org/wiki/Q318176'
SET person_4fa2a31227f1.databases = ['http://d-nb.info/gnd/120558998', 'http://id.loc.gov/authorities/names/n83196093', 'https://catalogue.bnf.fr/ark:/12148/cb13896885p', 'http://snaccooperative.org/ark:/99166/w6bg5ppw', 'https://nla.gov.au/nla.party-1135147', 'https://rateyourmusic.com/artist/abe_lyman', 'https://www.worldcat.org/identities/lccn-n83196093/']
SET person_4fa2a31227f1.musicbrainz = 'https://musicbrainz.org/artist/684348fd-551d-4c45-a1da-4fa2a31227f1'
SET person_4fa2a31227f1.isni_list = ['http://isni.org/isni/0000000063036183']
SET person_4fa2a31227f1.source = 'musicbrainz.org'


MERGE (person_d5ce334cef0a:Person{ uuid: '1c8a91b9-5e5d-472a-bbc0-d5ce334cef0a' }) 
SET person_d5ce334cef0a.name = 'Jack Strachey'
SET person_d5ce334cef0a.gender = 'Male'
SET person_d5ce334cef0a.country = 'GB'
SET person_d5ce334cef0a.allmusic = 'https://www.allmusic.com/artist/mn0000104686'
SET person_d5ce334cef0a.discogs = 'https://www.discogs.com/artist/669136'
SET person_d5ce334cef0a.imdb = 'https://www.imdb.com/name/nm0663839/'
SET person_d5ce334cef0a.viaf = 'http://viaf.org/viaf/7654506'
SET person_d5ce334cef0a.wikidata = 'https://www.wikidata.org/wiki/Q6115366'
SET person_d5ce334cef0a.databases = ['http://id.loc.gov/authorities/names/nr2006006683', 'https://catalogue.bnf.fr/ark:/12148/cb14843343r', 'http://snaccooperative.org/ark:/99166/w6mj0kg7', 'https://nla.gov.au/nla.party-1493762', 'https://rateyourmusic.com/artist/jack_strachey', 'https://www.ibdb.com/person.php?id=86570', 'https://www.worldcat.org/identities/lccn-nr2006006683/']
SET person_d5ce334cef0a.musicbrainz = 'https://musicbrainz.org/artist/1c8a91b9-5e5d-472a-bbc0-d5ce334cef0a'
SET person_d5ce334cef0a.isni_list = ['http://isni.org/isni/0000000080871906']
SET person_d5ce334cef0a.source = 'musicbrainz.org'


MERGE (person_86ffc831c030:Person{ uuid: '493ed796-94db-403f-a7f1-86ffc831c030' }) 
SET person_86ffc831c030.name = 'Louis Alter'
SET person_86ffc831c030.gender = 'Male'
SET person_86ffc831c030.country = 'US'
SET person_86ffc831c030.discogs = 'https://www.discogs.com/artist/643488'
SET person_86ffc831c030.imdb = 'https://www.imdb.com/name/nm0022746/'
SET person_86ffc831c030.viaf = 'http://viaf.org/viaf/73408257'
SET person_86ffc831c030.wikidata = 'https://www.wikidata.org/wiki/Q2773125'
SET person_86ffc831c030.databases = ['http://d-nb.info/gnd/1057990051', 'http://id.loc.gov/authorities/names/no89005081', 'http://snaccooperative.org/ark:/99166/w6xw4m4x', 'https://nla.gov.au/nla.party-877504', 'https://openlibrary.org/works/OL7515315A', 'https://www.ibdb.com/person.php?id=11308', 'https://www.worldcat.org/identities/lccn-no89005081/']
SET person_86ffc831c030.musicbrainz = 'https://musicbrainz.org/artist/493ed796-94db-403f-a7f1-86ffc831c030'
SET person_86ffc831c030.isni_list = ['http://isni.org/isni/0000000081531719']
SET person_86ffc831c030.source = 'musicbrainz.org'


MERGE (person_8a3b4f0f3f79:Person{ uuid: '5fd5aa4f-02b0-4747-ad4c-8a3b4f0f3f79' }) 
SET person_8a3b4f0f3f79.name = 'Sammy Cahn'
SET person_8a3b4f0f3f79.gender = 'Male'
SET person_8a3b4f0f3f79.country = 'US'
SET person_8a3b4f0f3f79.allmusic = 'https://www.allmusic.com/artist/mn0000987625'
SET person_8a3b4f0f3f79.discogs = 'https://www.discogs.com/artist/255312'
SET person_8a3b4f0f3f79.imdb = 'https://www.imdb.com/name/nm0005991/'
SET person_8a3b4f0f3f79.viaf = 'http://viaf.org/viaf/209945'
SET person_8a3b4f0f3f79.wikidata = 'https://www.wikidata.org/wiki/Q470040'
SET person_8a3b4f0f3f79.databases = ['http://d-nb.info/gnd/124800823', 'http://id.loc.gov/authorities/names/n82096094', 'https://catalogue.bnf.fr/ark:/12148/cb14025723x', 'http://snaccooperative.org/ark:/99166/w6zs2v3w', 'https://rateyourmusic.com/artist/sammy_cahn', 'https://www.ibdb.com/person.php?id=11268', 'https://www.worldcat.org/identities/lccn-n82096094/']
SET person_8a3b4f0f3f79.musicbrainz = 'https://musicbrainz.org/artist/5fd5aa4f-02b0-4747-ad4c-8a3b4f0f3f79'
SET person_8a3b4f0f3f79.isni_list = ['http://isni.org/isni/0000000080796256']
SET person_8a3b4f0f3f79.source = 'musicbrainz.org'


MERGE (work_2ec936d0c7b2:Work{ uuid: '033b8ca8-e7a3-3b51-a3be-2ec936d0c7b2' })
SET work_2ec936d0c7b2.name = 'I Cried for You'
SET work_2ec936d0c7b2.iswc = 'T-070.902.589-7'
SET work_2ec936d0c7b2.type = 'Song'
SET work_2ec936d0c7b2.wikidata = 'https://www.wikidata.org/wiki/Q2059920'
SET work_2ec936d0c7b2.musicbrainz = 'https://musicbrainz.org/work/033b8ca8-e7a3-3b51-a3be-2ec936d0c7b2'
SET work_2ec936d0c7b2.source = 'musicbrainz.org'


MERGE (work_1bf5a6c0e888:Work{ uuid: '90ca4cb5-4590-384a-b6f1-1bf5a6c0e888' })
SET work_1bf5a6c0e888.name = 'Don’t Blame Me'
SET work_1bf5a6c0e888.iswc = 'T-070.045.769-7'
SET work_1bf5a6c0e888.type = 'Song'
SET work_1bf5a6c0e888.tags = ['instrumental', 'jazz']
SET work_1bf5a6c0e888.wikidata = 'https://www.wikidata.org/wiki/Q5291466'
SET work_1bf5a6c0e888.musicbrainz = 'https://musicbrainz.org/work/90ca4cb5-4590-384a-b6f1-1bf5a6c0e888'
SET work_1bf5a6c0e888.source = 'musicbrainz.org'


MERGE (work_f977bcd57451:Work{ uuid: '6261d6d4-caa9-31f0-8ab4-f977bcd57451' })
SET work_f977bcd57451.name = 'These Foolish Things (Remind Me of You)'
SET work_f977bcd57451.iswc = 'T-900.163.042-8'
SET work_f977bcd57451.type = 'Song'
SET work_f977bcd57451.wikidata = 'https://www.wikidata.org/wiki/Q780019'
SET work_f977bcd57451.musicbrainz = 'https://musicbrainz.org/work/6261d6d4-caa9-31f0-8ab4-f977bcd57451'
SET work_f977bcd57451.source = 'musicbrainz.org'


MERGE (work_c45bdf15b57a:Work{ uuid: '86954cd6-9019-3bb4-bcaf-c45bdf15b57a' })
SET work_c45bdf15b57a.name = 'Mean to Me'
SET work_c45bdf15b57a.iswc = 'T-070.108.794-6'
SET work_c45bdf15b57a.type = 'Song'
SET work_c45bdf15b57a.wikidata = 'https://www.wikidata.org/wiki/Q1915467'
SET work_c45bdf15b57a.musicbrainz = 'https://musicbrainz.org/work/86954cd6-9019-3bb4-bcaf-c45bdf15b57a'
SET work_c45bdf15b57a.source = 'musicbrainz.org'


MERGE (work_9703b0ebd3ee:Work{ uuid: 'd711b1f9-2e77-44da-abbc-9703b0ebd3ee' })
SET work_9703b0ebd3ee.name = 'My Kinda Love'
SET work_9703b0ebd3ee.iswc = 'T-070.111.062-4'
SET work_9703b0ebd3ee.type = 'Song'
SET work_9703b0ebd3ee.musicbrainz = 'https://musicbrainz.org/work/d711b1f9-2e77-44da-abbc-9703b0ebd3ee'
SET work_9703b0ebd3ee.source = 'musicbrainz.org'


MERGE (work_6631d39deea7:Work{ uuid: 'ade9c30c-faf5-3219-aa4a-6631d39deea7' })
SET work_6631d39deea7.name = '(I Don’t Stand) A Ghost of a Chance'
SET work_6631d39deea7.iswc = 'T-071.183.771-6'
SET work_6631d39deea7.type = 'Song'
SET work_6631d39deea7.wikidata = 'https://www.wikidata.org/wiki/Q5976963'
SET work_6631d39deea7.musicbrainz = 'https://musicbrainz.org/work/ade9c30c-faf5-3219-aa4a-6631d39deea7'
SET work_6631d39deea7.source = 'musicbrainz.org'


MERGE (work_73eb2148d143:Work{ uuid: 'a0170c8e-e072-38a8-a2c6-73eb2148d143' })
SET work_73eb2148d143.name = 'Jumpin’ With Symphony Sid'
SET work_73eb2148d143.type = 'Song'
SET work_73eb2148d143.source = 'musicbrainz.org'


MERGE (work_1a522eb16d4f:Work{ uuid: '8f440c9c-13a1-3560-82cb-1a522eb16d4f' })
SET work_1a522eb16d4f.name = 'Time After Time'
SET work_1a522eb16d4f.iswc = 'T-070.180.256-3'
SET work_1a522eb16d4f.type = 'Song'
SET work_1a522eb16d4f.wikidata = 'https://www.wikidata.org/wiki/Q3970756'
SET work_1a522eb16d4f.musicbrainz = 'https://musicbrainz.org/work/8f440c9c-13a1-3560-82cb-1a522eb16d4f'
SET work_1a522eb16d4f.source = 'musicbrainz.org'


MERGE (work_c3f561ae4a1e:Work{ uuid: 'e10256bd-40c6-3ebf-847e-c3f561ae4a1e' })
SET work_c3f561ae4a1e.name = 'The Man I Love'
SET work_c3f561ae4a1e.iswc = 'T-011.191.232-3'
SET work_c3f561ae4a1e.type = 'Song'
SET work_c3f561ae4a1e.wikidata = 'https://www.wikidata.org/wiki/Q1828805'
SET work_c3f561ae4a1e.musicbrainz = 'https://musicbrainz.org/work/e10256bd-40c6-3ebf-847e-c3f561ae4a1e'
SET work_c3f561ae4a1e.source = 'musicbrainz.org'


MERGE (work_cdc262bbd884:Work{ uuid: '755f81d2-007a-49cf-9e54-cdc262bbd884' })
SET work_cdc262bbd884.name = 'Lester Leaps In'
SET work_cdc262bbd884.type = 'Song'
SET work_cdc262bbd884.wikidata = 'https://www.wikidata.org/wiki/Q14932274'
SET work_cdc262bbd884.musicbrainz = 'https://musicbrainz.org/work/755f81d2-007a-49cf-9e54-cdc262bbd884'
SET work_cdc262bbd884.source = 'musicbrainz.org'


MERGE (work_73266fedbec8:Work{ uuid: '98fb7d1f-12f5-3878-9fad-73266fedbec8' })
SET work_73266fedbec8.name = 'Body and Soul'
SET work_73266fedbec8.iswc = 'T-070.012.014-4'
SET work_73266fedbec8.type = 'Song'
SET work_73266fedbec8.wikidata = 'https://www.wikidata.org/wiki/Q890080'
SET work_73266fedbec8.musicbrainz = 'https://musicbrainz.org/work/98fb7d1f-12f5-3878-9fad-73266fedbec8'
SET work_73266fedbec8.source = 'musicbrainz.org'


MERGE (work_3d536de4e0c5:Work{ uuid: '0b393552-2b45-3c27-a3d4-3d536de4e0c5' })
SET work_3d536de4e0c5.name = 'I Cover the Waterfront'
SET work_3d536de4e0c5.iswc = 'T-070.902.587-5'
SET work_3d536de4e0c5.musicbrainz = 'https://musicbrainz.org/work/0b393552-2b45-3c27-a3d4-3d536de4e0c5'
SET work_3d536de4e0c5.source = 'musicbrainz.org'


MERGE (work_348b554a512e:Work{ uuid: 'e4e2860a-5d1c-3f92-84aa-348b554a512e' })
SET work_348b554a512e.name = 'Just You, Just Me'
SET work_348b554a512e.iswc = 'T-070.089.165-1'
SET work_348b554a512e.type = 'Song'
SET work_348b554a512e.wikidata = 'https://www.wikidata.org/wiki/Q6316474'
SET work_348b554a512e.musicbrainz = 'https://musicbrainz.org/work/e4e2860a-5d1c-3f92-84aa-348b554a512e'
SET work_348b554a512e.source = 'musicbrainz.org'



// performances of
MERGE (perf_b971e0964a2c)-[:PERFORMANCE_OF]->(work_2ec936d0c7b2)
MERGE (perf_37f0eb9fa0c6)-[:PERFORMANCE_OF]->(work_1bf5a6c0e888)
MERGE (perf_e97beee51432)-[:PERFORMANCE_OF]->(work_f977bcd57451)
MERGE (perf_7de25aef7438)-[:PERFORMANCE_OF]->(work_c45bdf15b57a)
MERGE (perf_f176562c0073)-[:PERFORMANCE_OF]->(work_9703b0ebd3ee)
MERGE (perf_9abef563a68b)-[:PERFORMANCE_OF]->(work_6631d39deea7)
MERGE (perf_6e3a1cb1351b)-[:PERFORMANCE_OF]->(work_73eb2148d143)
MERGE (perf_abfa2ed60305)-[:PERFORMANCE_OF]->(work_1a522eb16d4f)
MERGE (perf_931a70e567c3)-[:PERFORMANCE_OF]->(work_c3f561ae4a1e)
MERGE (perf_3606c8140558)-[:PERFORMANCE_OF]->(work_cdc262bbd884)
MERGE (perf_a37dead6af85)-[:PERFORMANCE_OF]->(work_73266fedbec8)
MERGE (perf_464e800f8514)-[:PERFORMANCE_OF]->(work_3d536de4e0c5)
MERGE (perf_9d078916d034)-[:PERFORMANCE_OF]->(work_348b554a512e)


// composers
MERGE (person_ed56a0d6c7fc)-[:COMPOSED]->(work_2ec936d0c7b2)
MERGE (person_4fa2a31227f1)-[:COMPOSED]->(work_2ec936d0c7b2)
MERGE (person_36cedde0ce66)-[:WROTE_LYRICS]->(work_2ec936d0c7b2)
MERGE (person_2a20254ed520)-[:COMPOSED]->(work_1bf5a6c0e888)
MERGE (person_cae1b1c6362f)-[:WROTE_LYRICS]->(work_1bf5a6c0e888)
MERGE (person_d5ce334cef0a)-[:COMPOSED]->(work_f977bcd57451)
MERGE (person_afa0632abd19)-[:COMPOSED]->(work_f977bcd57451)
MERGE (person_5bf00afc3eaf)-[:WROTE_LYRICS]->(work_f977bcd57451)
MERGE (person_0229920db798)-[:COMPOSED]->(work_c45bdf15b57a)
MERGE (person_f0917b4fc06d)-[:COMPOSED]->(work_c45bdf15b57a)
MERGE (person_0229920db798)-[:WROTE_LYRICS]->(work_c45bdf15b57a)
MERGE (person_f0917b4fc06d)-[:WROTE_LYRICS]->(work_c45bdf15b57a)
MERGE (person_86ffc831c030)-[:COMPOSED]->(work_9703b0ebd3ee)
MERGE (person_1bfdeb0d8097)-[:WROTE_LYRICS]->(work_9703b0ebd3ee)
MERGE (person_0cdf22c48565)-[:COMPOSED]->(work_6631d39deea7)
MERGE (person_b90d9d7fcf8f)-[:WROTE_LYRICS]->(work_6631d39deea7)
MERGE (person_9ecd8b2daa0d)-[:WROTE_LYRICS]->(work_6631d39deea7)
MERGE (person_579480f7f7e8)-[:COMPOSED]->(work_73eb2148d143)
MERGE (person_3fbbe73d09b4)-[:COMPOSED]->(work_1a522eb16d4f)
MERGE (person_8a3b4f0f3f79)-[:WROTE_LYRICS]->(work_1a522eb16d4f)
MERGE (person_b693a808a158)-[:COMPOSED]->(work_c3f561ae4a1e)
MERGE (person_322e34240ffc)-[:WROTE_LYRICS]->(work_c3f561ae4a1e)
MERGE (person_579480f7f7e8)-[:COMPOSED]->(work_cdc262bbd884)
MERGE (person_e9385c4e43f8)-[:COMPOSED]->(work_73266fedbec8)
MERGE (person_4508a4b0db32)-[:WROTE_LYRICS]->(work_73266fedbec8)
MERGE (person_91000e35bc46)-[:WROTE_LYRICS]->(work_73266fedbec8)
MERGE (person_22ada2e4e284)-[:WROTE_LYRICS]->(work_73266fedbec8)
MERGE (person_e9385c4e43f8)-[:COMPOSED]->(work_3d536de4e0c5)
MERGE (person_91000e35bc46)-[:COMPOSED]->(work_3d536de4e0c5)
MERGE (person_91000e35bc46)-[:WROTE_LYRICS]->(work_3d536de4e0c5)
MERGE (person_e5f1cc0ea99b)-[:COMPOSED]->(work_348b554a512e)
MERGE (person_d65a9f32875b)-[:WROTE_LYRICS]->(work_348b554a512e)


// place nodes

MERGE (place_fc04889e8ba1:Place{ uuid: '59ae8dbd-2563-4825-a811-fc04889e8ba1' })
SET place_fc04889e8ba1.name = 'The Town Hall'
SET place_fc04889e8ba1.source = 'musicbrainz.org'


// place relationships
MERGE (perf_3606c8140558)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_9d078916d034)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_6e3a1cb1351b)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_8a17673cc9e2)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_37f0eb9fa0c6)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_f176562c0073)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_464e800f8514)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_9abef563a68b)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_372483a0f6d5)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_e97beee51432)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_a739023a5d20)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_931a70e567c3)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_abfa2ed60305)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_7de25aef7438)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_a37dead6af85)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)
MERGE (perf_b971e0964a2c)-[:HAS_PLACE { type: 'recorded at', begin_date: '1947-11-08', end_date: '1947-11-08' }]->(place_fc04889e8ba1)

MERGE (person_026959d062eb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_3606c8140558)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_3606c8140558)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_3606c8140558)
MERGE (person_8dbeec4f6ef7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_3606c8140558)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_3606c8140558)
MERGE (person_579480f7f7e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_3606c8140558)
MERGE (person_026959d062eb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_9d078916d034)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9d078916d034)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_9d078916d034)
MERGE (person_8dbeec4f6ef7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_9d078916d034)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_9d078916d034)
MERGE (person_579480f7f7e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9d078916d034)
MERGE (person_026959d062eb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6e3a1cb1351b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6e3a1cb1351b)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_6e3a1cb1351b)
MERGE (person_8dbeec4f6ef7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_6e3a1cb1351b)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_6e3a1cb1351b)
MERGE (person_579480f7f7e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_6e3a1cb1351b)
MERGE (person_026959d062eb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8a17673cc9e2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_8a17673cc9e2)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_8a17673cc9e2)
MERGE (person_8dbeec4f6ef7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_8a17673cc9e2)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_8a17673cc9e2)
MERGE (person_579480f7f7e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_8a17673cc9e2)
MERGE (person_0afaa7773881)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_37f0eb9fa0c6)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_37f0eb9fa0c6)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_37f0eb9fa0c6)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_37f0eb9fa0c6)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_37f0eb9fa0c6)
MERGE (person_0afaa7773881)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f176562c0073)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f176562c0073)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_f176562c0073)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_f176562c0073)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_f176562c0073)
MERGE (person_0afaa7773881)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_464e800f8514)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_464e800f8514)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_464e800f8514)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_464e800f8514)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_464e800f8514)
MERGE (person_0afaa7773881)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_9abef563a68b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9abef563a68b)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_9abef563a68b)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_9abef563a68b)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_9abef563a68b)
MERGE (person_026959d062eb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_372483a0f6d5)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_372483a0f6d5)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_372483a0f6d5)
MERGE (person_8dbeec4f6ef7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_372483a0f6d5)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_372483a0f6d5)
MERGE (person_579480f7f7e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_372483a0f6d5)
MERGE (person_026959d062eb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e97beee51432)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e97beee51432)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_e97beee51432)
MERGE (person_8dbeec4f6ef7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_e97beee51432)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e97beee51432)
MERGE (person_579480f7f7e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_e97beee51432)
MERGE (person_026959d062eb)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a739023a5d20)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a739023a5d20)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_a739023a5d20)
MERGE (person_8dbeec4f6ef7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_a739023a5d20)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_a739023a5d20)
MERGE (person_579480f7f7e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_a739023a5d20)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_931a70e567c3)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_931a70e567c3)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_931a70e567c3)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_931a70e567c3)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_abfa2ed60305)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_abfa2ed60305)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_abfa2ed60305)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_abfa2ed60305)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_7de25aef7438)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_7de25aef7438)
MERGE (person_8dbeec4f6ef7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_7de25aef7438)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_7de25aef7438)
MERGE (person_579480f7f7e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_7de25aef7438)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_7de25aef7438)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a37dead6af85)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_a37dead6af85)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_a37dead6af85)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_a37dead6af85)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_b971e0964a2c)
MERGE (person_cd42f757accd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_b971e0964a2c)
MERGE (person_8dbeec4f6ef7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_b971e0964a2c)
MERGE (person_8382db5e9f31)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_b971e0964a2c)
MERGE (person_579480f7f7e8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_b971e0964a2c)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_b971e0964a2c)



"""
)