
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_4864fdb8cb44:Release{ uuid: 'ed1dab2b-f80a-451d-a9f3-4864fdb8cb44' })
SET release_4864fdb8cb44.name = 'Te-Vou!'
SET release_4864fdb8cb44.country = 'US'
SET release_4864fdb8cb44.date = '1997'
SET release_4864fdb8cb44.format = 'CD'
SET release_4864fdb8cb44.musicbrainz = 'http://musicbrainz.org/release/ed1dab2b-f80a-451d-a9f3-4864fdb8cb44'
SET release_4864fdb8cb44.source = 'musicbrainz.org'


MERGE (person_541154610960:Person{ uuid: 'a404273a-4327-43d4-90ec-541154610960' }) 
SET person_541154610960.name = 'Tom Swift'
SET person_541154610960.gender = 'Male'
SET person_541154610960.disambiguation = 'engineer'
SET person_541154610960.country = 'US'
SET person_541154610960.discogs = 'https://www.discogs.com/artist/388234'
SET person_541154610960.databases = ['https://rateyourmusic.com/artist/tom_swift']
SET person_541154610960.musicbrainz = 'https://musicbrainz.org/artist/a404273a-4327-43d4-90ec-541154610960'
SET person_541154610960.source = 'musicbrainz.org'


MERGE (person_19962a7eb4fd:Person{ uuid: '80d049f2-8d05-47e1-ac46-19962a7eb4fd' }) 
SET person_19962a7eb4fd.name = 'Donald Harrison'
SET person_19962a7eb4fd.gender = 'Male'
SET person_19962a7eb4fd.country = 'US'
SET person_19962a7eb4fd.allmusic = 'https://www.allmusic.com/artist/mn0000184406'
SET person_19962a7eb4fd.discogs = 'https://www.discogs.com/artist/65744'
SET person_19962a7eb4fd.viaf = 'http://viaf.org/viaf/32183394'
SET person_19962a7eb4fd.wikidata = 'https://www.wikidata.org/wiki/Q723508'
SET person_19962a7eb4fd.databases = ['http://id.loc.gov/authorities/names/no2006025251', 'https://catalogue.bnf.fr/ark:/12148/cb13894989v', 'https://d-nb.info/gnd/134398548', 'https://www.worldcat.org/identities/lccn-no2006025251']
SET person_19962a7eb4fd.musicbrainz = 'https://musicbrainz.org/artist/80d049f2-8d05-47e1-ac46-19962a7eb4fd'
SET person_19962a7eb4fd.isni_list = ['http://isni.org/isni/000000006309544X']
SET person_19962a7eb4fd.source = 'musicbrainz.org'


MERGE (person_a7572c34e806:Person{ uuid: '6035000d-b53b-4b01-b5a0-a7572c34e806' }) 
SET person_a7572c34e806.name = 'Christian McBride'
SET person_a7572c34e806.gender = 'Male'
SET person_a7572c34e806.disambiguation = 'American jazz bassist'
SET person_a7572c34e806.country = 'US'
SET person_a7572c34e806.allmusic = 'https://www.allmusic.com/artist/mn0000103600'
SET person_a7572c34e806.discogs = 'https://www.discogs.com/artist/44565'
SET person_a7572c34e806.viaf = 'http://viaf.org/viaf/85464720'
SET person_a7572c34e806.wikidata = 'https://www.wikidata.org/wiki/Q732319'
SET person_a7572c34e806.databases = ['http://id.loc.gov/authorities/names/n92023967', 'https://catalogue.bnf.fr/ark:/12148/cb139401069', 'https://d-nb.info/gnd/134732650', 'https://www.worldcat.org/identities/lccn-n92023967']
SET person_a7572c34e806.musicbrainz = 'https://musicbrainz.org/artist/6035000d-b53b-4b01-b5a0-a7572c34e806'
SET person_a7572c34e806.isni_list = ['http://isni.org/isni/0000000114765651']
SET person_a7572c34e806.source = 'musicbrainz.org'


MERGE (person_f8091d98cf25:Person{ uuid: '7daac7f9-8fcc-485f-a14f-f8091d98cf25' }) 
SET person_f8091d98cf25.name = 'Pat Metheny'
SET person_f8091d98cf25.gender = 'Male'
SET person_f8091d98cf25.country = 'US'
SET person_f8091d98cf25.allmusic = 'https://www.allmusic.com/artist/mn0000179698'
SET person_f8091d98cf25.bbc = 'https://www.bbc.co.uk/music/artists/7daac7f9-8fcc-485f-a14f-f8091d98cf25'
SET person_f8091d98cf25.discogs = 'https://www.discogs.com/artist/20185'
SET person_f8091d98cf25.imdb = 'https://www.imdb.com/name/nm0582533/'
SET person_f8091d98cf25.viaf = 'http://viaf.org/viaf/22188874'
SET person_f8091d98cf25.wikidata = 'https://www.wikidata.org/wiki/Q213887'
SET person_f8091d98cf25.databases = ['http://id.loc.gov/authorities/names/n78096789', 'https://catalogue.bnf.fr/ark:/12148/cb122016747', 'https://d-nb.info/gnd/118946803', 'http://snaccooperative.org/ark:/99166/w6gj10fw', 'https://rateyourmusic.com/artist/pat-metheny', 'https://www.musik-sammler.de/artist/pat-metheny/', 'https://www.progarchives.com/artist.asp?id=2445', 'https://www.worldcat.org/identities/lccn-n78096789']
SET person_f8091d98cf25.musicbrainz = 'https://musicbrainz.org/artist/7daac7f9-8fcc-485f-a14f-f8091d98cf25'
SET person_f8091d98cf25.isni_list = ['http://isni.org/isni/0000000121236985']
SET person_f8091d98cf25.source = 'musicbrainz.org'


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


MERGE (person_b84e43378390:Person{ uuid: '30b01f7e-2af1-4293-a52c-b84e43378390' }) 
SET person_b84e43378390.name = 'David Kikoski'
SET person_b84e43378390.gender = 'Male'
SET person_b84e43378390.country = 'US'
SET person_b84e43378390.allmusic = 'https://www.allmusic.com/artist/mn0000811141'
SET person_b84e43378390.discogs = 'https://www.discogs.com/artist/486649'
SET person_b84e43378390.viaf = 'http://viaf.org/viaf/233486283'
SET person_b84e43378390.wikidata = 'https://www.wikidata.org/wiki/Q1174978'
SET person_b84e43378390.wikipedia = 'https://en.wikipedia.org/wiki/David_Kikoski'
SET person_b84e43378390.databases = ['http://id.loc.gov/authorities/names/n87142774', 'https://catalogue.bnf.fr/ark:/12148/cb139775835', 'https://d-nb.info/gnd/134644328', 'https://www.worldcat.org/identities/lccn-n87142774']
SET person_b84e43378390.musicbrainz = 'https://musicbrainz.org/artist/30b01f7e-2af1-4293-a52c-b84e43378390'
SET person_b84e43378390.isni_list = ['http://isni.org/isni/0000000367948974']
SET person_b84e43378390.source = 'musicbrainz.org'

// labels

MERGE (label_3425c147f535:Label{ uuid: '9e846f54-7799-471c-9a47-3425c147f535' })
SET label_3425c147f535.name= 'Disques Dreyfus'

// performances

MERGE (perf_088ebd9907cd:Performance{ uuid: 'ce62e615-849f-4035-85ec-088ebd9907cd' })
SET perf_088ebd9907cd.name = 'Like This'
SET perf_088ebd9907cd.duration = '5:27'
SET perf_088ebd9907cd.source = 'musicbrainz.org'


MERGE (perf_1f1547070a68:Performance{ uuid: '44687bc1-7d4c-4c8a-af98-1f1547070a68' })
SET perf_1f1547070a68.name = 'John McKee'
SET perf_1f1547070a68.duration = '6:25'
SET perf_1f1547070a68.source = 'musicbrainz.org'


MERGE (perf_f00bddb4f860:Performance{ uuid: '797789f6-7436-4143-9e76-f00bddb4f860' })
SET perf_f00bddb4f860.name = 'James'
SET perf_f00bddb4f860.duration = '4:35'
SET perf_f00bddb4f860.source = 'musicbrainz.org'


MERGE (perf_8896f6b85219:Performance{ uuid: '68d40877-b389-4609-a453-8896f6b85219' })
SET perf_8896f6b85219.name = 'If I Could'
SET perf_8896f6b85219.duration = '8:12'
SET perf_8896f6b85219.source = 'musicbrainz.org'


MERGE (perf_d961e5e8ea65:Performance{ uuid: '96808097-252c-4400-93e5-d961e5e8ea65' })
SET perf_d961e5e8ea65.name = 'Blues M45'
SET perf_d961e5e8ea65.duration = '7:07'
SET perf_d961e5e8ea65.source = 'musicbrainz.org'


MERGE (perf_7e045e06cc6b:Performance{ uuid: '685873a9-fa36-403f-850a-7e045e06cc6b' })
SET perf_7e045e06cc6b.name = 'Trinkle Twinkle'
SET perf_7e045e06cc6b.duration = '6:22'
SET perf_7e045e06cc6b.source = 'musicbrainz.org'


MERGE (perf_7da559a41e12:Performance{ uuid: 'bd1fccdb-19f6-464d-a850-7da559a41e12' })
SET perf_7da559a41e12.name = 'Trigonometry'
SET perf_7da559a41e12.duration = '7:15'
SET perf_7da559a41e12.source = 'musicbrainz.org'


MERGE (perf_a8533a6e337f:Performance{ uuid: '4079baa7-c708-4691-81ed-a8533a6e337f' })
SET perf_a8533a6e337f.name = 'Good for the Soul'
SET perf_a8533a6e337f.duration = '6:44'
SET perf_a8533a6e337f.source = 'musicbrainz.org'




// labels
MERGE (release_4864fdb8cb44)-[:HAS_LABEL]->(label_3425c147f535)


// tracks
MERGE (release_4864fdb8cb44)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_088ebd9907cd)
MERGE (release_4864fdb8cb44)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_1f1547070a68)
MERGE (release_4864fdb8cb44)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_f00bddb4f860)
MERGE (release_4864fdb8cb44)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_8896f6b85219)
MERGE (release_4864fdb8cb44)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_d961e5e8ea65)
MERGE (release_4864fdb8cb44)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_7e045e06cc6b)
MERGE (release_4864fdb8cb44)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_7da559a41e12)
MERGE (release_4864fdb8cb44)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_a8533a6e337f)

// works

MERGE (person_0ad7756dd538:Person{ uuid: '210b51ef-bece-44c6-aa94-0ad7756dd538' }) 
SET person_0ad7756dd538.name = 'Lyle Mays'
SET person_0ad7756dd538.gender = 'Male'
SET person_0ad7756dd538.country = 'US'
SET person_0ad7756dd538.allmusic = 'https://www.allmusic.com/artist/mn0000171015'
SET person_0ad7756dd538.discogs = 'https://www.discogs.com/artist/222583'
SET person_0ad7756dd538.imdb = 'https://www.imdb.com/name/nm0563077/'
SET person_0ad7756dd538.viaf = 'http://viaf.org/viaf/39562612'
SET person_0ad7756dd538.wikidata = 'https://www.wikidata.org/wiki/Q963426'
SET person_0ad7756dd538.databases = ['http://id.loc.gov/authorities/names/n78096790', 'https://catalogue.bnf.fr/ark:/12148/cb13897265n', 'https://d-nb.info/gnd/134458974', 'https://rateyourmusic.com/artist/lyle_mays', 'https://www.worldcat.org/identities/lccn-n78096790']
SET person_0ad7756dd538.musicbrainz = 'https://musicbrainz.org/artist/210b51ef-bece-44c6-aa94-0ad7756dd538'
SET person_0ad7756dd538.isni_list = ['http://isni.org/isni/000000012278596X']
SET person_0ad7756dd538.source = 'musicbrainz.org'


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


MERGE (person_829aa7b39205:Person{ uuid: '169c0d1b-fcb8-4a43-9097-829aa7b39205' }) 
SET person_829aa7b39205.name = 'Ornette Coleman'
SET person_829aa7b39205.gender = 'Male'
SET person_829aa7b39205.disambiguation = 'US jazz saxophonist, trumpeter, violinist, and composer'
SET person_829aa7b39205.country = 'US'
SET person_829aa7b39205.allmusic = 'https://www.allmusic.com/artist/mn0000484396'
SET person_829aa7b39205.bbc = 'https://www.bbc.co.uk/music/artists/169c0d1b-fcb8-4a43-9097-829aa7b39205'
SET person_829aa7b39205.discogs = 'https://www.discogs.com/artist/224506'
SET person_829aa7b39205.imdb = 'https://www.imdb.com/name/nm0171170/'
SET person_829aa7b39205.viaf = 'http://viaf.org/viaf/79166373'
SET person_829aa7b39205.wikidata = 'https://www.wikidata.org/wiki/Q208797'
SET person_829aa7b39205.databases = ['http://id.loc.gov/authorities/names/n83071536', 'https://catalogue.bnf.fr/ark:/12148/cb13892628b', 'https://d-nb.info/gnd/118890964', 'http://snaccooperative.org/ark:/99166/w6rz0q2w', 'https://nla.gov.au/nla.party-941985', 'https://rateyourmusic.com/artist/ornette-coleman', 'https://www.jazzmusicarchives.com/artist/ornette-coleman', 'https://www.musik-sammler.de/artist/ornette-coleman/', 'https://www.themoviedb.org/person/998600-ornette-coleman', 'https://www.whosampled.com/Ornette-Coleman/', 'https://www.worldcat.org/oclc/935032488']
SET person_829aa7b39205.musicbrainz = 'https://musicbrainz.org/artist/169c0d1b-fcb8-4a43-9097-829aa7b39205'
SET person_829aa7b39205.isni_list = ['http://isni.org/isni/0000000117719685']
SET person_829aa7b39205.source = 'musicbrainz.org'


MERGE (work_0495ba1449c3:Work{ uuid: 'b94a1718-1873-42d1-b34a-0495ba1449c3' })
SET work_0495ba1449c3.name = 'If I Could'
SET work_0495ba1449c3.type = 'Song'
SET work_0495ba1449c3.source = 'musicbrainz.org'


MERGE (work_f67c8f133de2:Work{ uuid: '3dec3df7-bc56-401e-8636-f67c8f133de2' })
SET work_f67c8f133de2.name = 'John McKee'
SET work_f67c8f133de2.type = 'Song'
SET work_f67c8f133de2.source = 'musicbrainz.org'


MERGE (work_567b5ea2c2bf:Work{ uuid: 'de481d05-d2a8-369d-b1dc-567b5ea2c2bf' })
SET work_567b5ea2c2bf.name = 'James'
SET work_567b5ea2c2bf.iswc = 'T-070.241.328-2'
SET work_567b5ea2c2bf.source = 'musicbrainz.org'


MERGE (work_a000d9687baa:Work{ uuid: 'aa857bc2-3922-4e8d-b9b4-a000d9687baa' })
SET work_a000d9687baa.name = 'Trigonometry'
SET work_a000d9687baa.type = 'Song'
SET work_a000d9687baa.source = 'musicbrainz.org'


MERGE (work_1003e9b588f3:Work{ uuid: '067eccc9-5533-34b9-a676-1003e9b588f3' })
SET work_1003e9b588f3.name = 'Trinkle Tinkle'
SET work_1003e9b588f3.iswc = 'T-070.247.478-9'
SET work_1003e9b588f3.type = 'Song'
SET work_1003e9b588f3.source = 'musicbrainz.org'



// performances of
MERGE (perf_8896f6b85219)-[:PERFORMANCE_OF]->(work_0495ba1449c3)
MERGE (perf_1f1547070a68)-[:PERFORMANCE_OF]->(work_f67c8f133de2)
MERGE (perf_f00bddb4f860)-[:PERFORMANCE_OF]->(work_567b5ea2c2bf)
MERGE (perf_7da559a41e12)-[:PERFORMANCE_OF]->(work_a000d9687baa)
MERGE (perf_7e045e06cc6b)-[:PERFORMANCE_OF]->(work_1003e9b588f3)


// composers
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_0495ba1449c3)
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_f67c8f133de2)
MERGE (person_0ad7756dd538)-[:COMPOSED]->(work_567b5ea2c2bf)
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_567b5ea2c2bf)
MERGE (person_829aa7b39205)-[:COMPOSED]->(work_a000d9687baa)
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_a000d9687baa)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_1003e9b588f3)


// place nodes

MERGE (place_91e209c23453:Place{ uuid: '6b67cf30-282a-44ba-82e0-91e209c23453' })
SET place_91e209c23453.name = 'EastSide Sound'
SET place_91e209c23453.source = 'musicbrainz.org'

MERGE (place_75b565e0e8ff:Place{ uuid: 'c3d28ac3-74d7-4577-983f-75b565e0e8ff' })
SET place_75b565e0e8ff.name = 'Master Sound Astoria'
SET place_75b565e0e8ff.source = 'musicbrainz.org'


// place relationships
MERGE (perf_088ebd9907cd)-[:HAS_PLACE { type: 'mixed at' }]->(place_91e209c23453)
MERGE (perf_088ebd9907cd)-[:HAS_PLACE { type: 'recorded at' }]->(place_75b565e0e8ff)
MERGE (perf_1f1547070a68)-[:HAS_PLACE { type: 'mixed at' }]->(place_91e209c23453)
MERGE (perf_1f1547070a68)-[:HAS_PLACE { type: 'recorded at' }]->(place_75b565e0e8ff)
MERGE (perf_f00bddb4f860)-[:HAS_PLACE { type: 'mixed at' }]->(place_91e209c23453)
MERGE (perf_f00bddb4f860)-[:HAS_PLACE { type: 'recorded at' }]->(place_75b565e0e8ff)
MERGE (perf_8896f6b85219)-[:HAS_PLACE { type: 'mixed at' }]->(place_91e209c23453)
MERGE (perf_8896f6b85219)-[:HAS_PLACE { type: 'recorded at' }]->(place_75b565e0e8ff)
MERGE (perf_d961e5e8ea65)-[:HAS_PLACE { type: 'mixed at' }]->(place_91e209c23453)
MERGE (perf_d961e5e8ea65)-[:HAS_PLACE { type: 'recorded at' }]->(place_75b565e0e8ff)
MERGE (perf_7e045e06cc6b)-[:HAS_PLACE { type: 'mixed at' }]->(place_91e209c23453)
MERGE (perf_7e045e06cc6b)-[:HAS_PLACE { type: 'recorded at' }]->(place_75b565e0e8ff)
MERGE (perf_7da559a41e12)-[:HAS_PLACE { type: 'mixed at' }]->(place_91e209c23453)
MERGE (perf_7da559a41e12)-[:HAS_PLACE { type: 'recorded at' }]->(place_75b565e0e8ff)
MERGE (perf_a8533a6e337f)-[:HAS_PLACE { type: 'mixed at' }]->(place_91e209c23453)
MERGE (perf_a8533a6e337f)-[:HAS_PLACE { type: 'recorded at' }]->(place_75b565e0e8ff)

MERGE (person_19962a7eb4fd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_088ebd9907cd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_088ebd9907cd)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_088ebd9907cd)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_088ebd9907cd)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_088ebd9907cd)
MERGE (person_19962a7eb4fd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_1f1547070a68)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_1f1547070a68)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_1f1547070a68)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_1f1547070a68)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_1f1547070a68)
MERGE (person_19962a7eb4fd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_f00bddb4f860)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_f00bddb4f860)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f00bddb4f860)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_f00bddb4f860)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_f00bddb4f860)
MERGE (person_19962a7eb4fd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_8896f6b85219)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_8896f6b85219)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8896f6b85219)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_8896f6b85219)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_8896f6b85219)
MERGE (person_19962a7eb4fd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_d961e5e8ea65)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_d961e5e8ea65)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d961e5e8ea65)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_d961e5e8ea65)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_d961e5e8ea65)
MERGE (person_19962a7eb4fd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_7e045e06cc6b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_7e045e06cc6b)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_7e045e06cc6b)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_7e045e06cc6b)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_7e045e06cc6b)
MERGE (person_19962a7eb4fd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_7da559a41e12)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_7da559a41e12)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_7da559a41e12)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_7da559a41e12)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_7da559a41e12)
MERGE (person_19962a7eb4fd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_a8533a6e337f)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_a8533a6e337f)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a8533a6e337f)
MERGE (person_a7572c34e806)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a8533a6e337f)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_a8533a6e337f)



"""
)