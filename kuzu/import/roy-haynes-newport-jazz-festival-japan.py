
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_0db3bdcc2b3d:Release{ uuid: '84a848b8-d2ec-4ec8-bb09-0db3bdcc2b3d' })
SET release_0db3bdcc2b3d.name = 'Newport Jazz Festival Japan'
SET release_0db3bdcc2b3d.country = 'JP'
SET release_0db3bdcc2b3d.date = '1974-07-10'
SET release_0db3bdcc2b3d.format = '12" Vinyl'
SET release_0db3bdcc2b3d.discode = 'KV-201'
SET release_0db3bdcc2b3d.discogs = 'https://www.discogs.com/release/8176647'
SET release_0db3bdcc2b3d.musicbrainz = 'http://musicbrainz.org/release/84a848b8-d2ec-4ec8-bb09-0db3bdcc2b3d'
SET release_0db3bdcc2b3d.source = 'musicbrainz.org'


MERGE (person_e9753d5ae693:Person{ uuid: '4f8a0d9b-5777-40da-b29a-e9753d5ae693' }) 
SET person_e9753d5ae693.name = 'Jimmy Smith'
SET person_e9753d5ae693.gender = 'Male'
SET person_e9753d5ae693.disambiguation = 'US jazz organist'
SET person_e9753d5ae693.country = 'US'
SET person_e9753d5ae693.allmusic = 'https://www.allmusic.com/artist/mn0000781172'
SET person_e9753d5ae693.bbc = 'https://www.bbc.co.uk/music/artists/4f8a0d9b-5777-40da-b29a-e9753d5ae693'
SET person_e9753d5ae693.discogs = 'https://www.discogs.com/artist/29981'
SET person_e9753d5ae693.imdb = 'https://www.imdb.com/name/nm0808732/'
SET person_e9753d5ae693.viaf = 'http://viaf.org/viaf/70675920'
SET person_e9753d5ae693.wikidata = 'https://www.wikidata.org/wiki/Q318948'
SET person_e9753d5ae693.databases = ['http://id.loc.gov/authorities/names/n87137943', 'https://catalogue.bnf.fr/ark:/12148/cb138998695', 'https://d-nb.info/gnd/134524543', 'http://snaccooperative.org/ark:/99166/w66h5463', 'https://rateyourmusic.com/artist/jimmy_smith', 'https://www.musik-sammler.de/artist/jimmy-smith/', 'https://www.worldcat.org/identities/lccn-n87137943']
SET person_e9753d5ae693.musicbrainz = 'https://musicbrainz.org/artist/4f8a0d9b-5777-40da-b29a-e9753d5ae693'
SET person_e9753d5ae693.isni_list = ['http://isni.org/isni/0000000034293818', 'http://isni.org/isni/0000000115776694']
SET person_e9753d5ae693.source = 'musicbrainz.org'


MERGE (person_e5f45e8d25d7:Person{ uuid: 'ee40fc76-9cbf-4862-bd00-e5f45e8d25d7' }) 
SET person_e5f45e8d25d7.name = 'Art Farmer'
SET person_e5f45e8d25d7.gender = 'Male'
SET person_e5f45e8d25d7.country = 'US'
SET person_e5f45e8d25d7.allmusic = 'https://www.allmusic.com/artist/mn0000502199'
SET person_e5f45e8d25d7.discogs = 'https://www.discogs.com/artist/179055'
SET person_e5f45e8d25d7.viaf = 'http://viaf.org/viaf/24787012'
SET person_e5f45e8d25d7.wikidata = 'https://www.wikidata.org/wiki/Q500464'
SET person_e5f45e8d25d7.databases = ['http://id.loc.gov/authorities/names/n83160891', 'https://adp.library.ucsb.edu/names/314819', 'https://catalogue.bnf.fr/ark:/12148/cb13893797p', 'https://d-nb.info/gnd/134026357', 'http://snaccooperative.org/ark:/99166/w6642tfk', 'https://rateyourmusic.com/artist/art_farmer', 'https://www.worldcat.org/identities/lccn-n83160891']
SET person_e5f45e8d25d7.musicbrainz = 'https://musicbrainz.org/artist/ee40fc76-9cbf-4862-bd00-e5f45e8d25d7'
SET person_e5f45e8d25d7.isni_list = ['http://isni.org/isni/0000000059479563']
SET person_e5f45e8d25d7.source = 'musicbrainz.org'


MERGE (person_8be01f64b4ea:Person{ uuid: '9d7283cd-a00c-469d-99f6-8be01f64b4ea' }) 
SET person_8be01f64b4ea.name = 'Jack Six'
SET person_8be01f64b4ea.gender = 'Male'
SET person_8be01f64b4ea.country = 'US'
SET person_8be01f64b4ea.allmusic = 'https://www.allmusic.com/artist/mn0000688926'
SET person_8be01f64b4ea.discogs = 'https://www.discogs.com/artist/251690'
SET person_8be01f64b4ea.wikidata = 'https://www.wikidata.org/wiki/Q19624438'
SET person_8be01f64b4ea.databases = ['https://adp.library.ucsb.edu/names/344053']
SET person_8be01f64b4ea.musicbrainz = 'https://musicbrainz.org/artist/9d7283cd-a00c-469d-99f6-8be01f64b4ea'
SET person_8be01f64b4ea.source = 'musicbrainz.org'


MERGE (person_983ca8e60b14:Person{ uuid: 'cb8c8b87-a52d-4a7e-b168-983ca8e60b14' }) 
SET person_983ca8e60b14.name = 'James Moody'
SET person_983ca8e60b14.gender = 'Male'
SET person_983ca8e60b14.disambiguation = 'jazz saxophonist'
SET person_983ca8e60b14.country = 'US'
SET person_983ca8e60b14.allmusic = 'https://www.allmusic.com/artist/mn0000786080'
SET person_983ca8e60b14.discogs = 'https://www.discogs.com/artist/120620'
SET person_983ca8e60b14.discogs = 'https://www.discogs.com/artist/346168'
SET person_983ca8e60b14.imdb = 'https://www.imdb.com/name/nm1792642/'
SET person_983ca8e60b14.viaf = 'http://viaf.org/viaf/79634074'
SET person_983ca8e60b14.wikidata = 'https://www.wikidata.org/wiki/Q962310'
SET person_983ca8e60b14.databases = ['http://id.loc.gov/authorities/names/n85244180', 'https://catalogue.bnf.fr/ark:/12148/cb13897661c', 'https://d-nb.info/gnd/134465784', 'https://ibdb.com/person.php?id=497175', 'http://snaccooperative.org/ark:/99166/w66n14c6', 'https://www.worldcat.org/identities/lccn-n85244180']
SET person_983ca8e60b14.musicbrainz = 'https://musicbrainz.org/artist/cb8c8b87-a52d-4a7e-b168-983ca8e60b14'
SET person_983ca8e60b14.isni_list = ['http://isni.org/isni/0000000114494505']
SET person_983ca8e60b14.source = 'musicbrainz.org'


MERGE (person_b7acdad1459c:Person{ uuid: '15ab8bb8-7348-4377-ab73-b7acdad1459c' }) 
SET person_b7acdad1459c.name = 'Illinois Jacquet'
SET person_b7acdad1459c.gender = 'Male'
SET person_b7acdad1459c.country = 'US'
SET person_b7acdad1459c.allmusic = 'https://www.allmusic.com/artist/mn0000770629'
SET person_b7acdad1459c.discogs = 'https://www.discogs.com/artist/257114'
SET person_b7acdad1459c.discogs = 'https://www.discogs.com/artist/320618'
SET person_b7acdad1459c.imdb = 'https://www.imdb.com/name/nm0415203/'
SET person_b7acdad1459c.viaf = 'http://viaf.org/viaf/37102134'
SET person_b7acdad1459c.wikidata = 'https://www.wikidata.org/wiki/Q1658835'
SET person_b7acdad1459c.databases = ['http://id.loc.gov/authorities/names/n83021444', 'https://adp.library.ucsb.edu/names/323040', 'https://catalogue.bnf.fr/ark:/12148/cb13895542b', 'https://d-nb.info/gnd/118989375', 'http://snaccooperative.org/ark:/99166/w6j23m4v', 'https://rateyourmusic.com/artist/illinois_jacquet', 'http://www.worldcat.org/wcidentities/lccn-n83-21444']
SET person_b7acdad1459c.musicbrainz = 'https://musicbrainz.org/artist/15ab8bb8-7348-4377-ab73-b7acdad1459c'
SET person_b7acdad1459c.isni_list = ['http://isni.org/isni/0000000059487571']
SET person_b7acdad1459c.source = 'musicbrainz.org'


MERGE (person_71aaf0f6b267:Person{ uuid: '68f19808-1f7b-46d4-bd1d-71aaf0f6b267' }) 
SET person_71aaf0f6b267.name = 'Gerry Mulligan'
SET person_71aaf0f6b267.gender = 'Male'
SET person_71aaf0f6b267.country = 'US'
SET person_71aaf0f6b267.allmusic = 'https://www.allmusic.com/artist/mn0000542549'
SET person_71aaf0f6b267.bbc = 'https://www.bbc.co.uk/music/artists/68f19808-1f7b-46d4-bd1d-71aaf0f6b267'
SET person_71aaf0f6b267.discogs = 'https://www.discogs.com/artist/37733'
SET person_71aaf0f6b267.imdb = 'https://www.imdb.com/name/nm0612302/'
SET person_71aaf0f6b267.viaf = 'http://viaf.org/viaf/22328253'
SET person_71aaf0f6b267.wikidata = 'https://www.wikidata.org/wiki/Q156535'
SET person_71aaf0f6b267.databases = ['http://id.loc.gov/authorities/names/n82153045', 'https://adp.library.ucsb.edu/names/332937', 'https://catalogue.bnf.fr/ark:/12148/cb138977969', 'https://d-nb.info/gnd/134469100', 'https://ibdb.com/person.php?id=107163', 'http://snaccooperative.org/ark:/99166/w66m3d6p', 'https://nla.gov.au/nla.party-910559', 'https://rateyourmusic.com/artist/gerry_mulligan', 'https://www.musik-sammler.de/artist/gerry-mulligan/', 'https://www.worldcat.org/identities/lccn-n82153045']
SET person_71aaf0f6b267.musicbrainz = 'https://musicbrainz.org/artist/68f19808-1f7b-46d4-bd1d-71aaf0f6b267'
SET person_71aaf0f6b267.isni_list = ['http://isni.org/isni/0000000081014850']
SET person_71aaf0f6b267.source = 'musicbrainz.org'


MERGE (person_16456d4d592b:Person{ uuid: 'ed9070ec-f1d2-405f-a386-16456d4d592b' }) 
SET person_16456d4d592b.name = 'Joe Newman'
SET person_16456d4d592b.gender = 'Male'
SET person_16456d4d592b.disambiguation = 'US jazz trumpeter'
SET person_16456d4d592b.country = 'US'
SET person_16456d4d592b.allmusic = 'https://www.allmusic.com/artist/mn0000208035'
SET person_16456d4d592b.discogs = 'https://www.discogs.com/artist/309874'
SET person_16456d4d592b.viaf = 'http://viaf.org/viaf/48256229'
SET person_16456d4d592b.wikidata = 'https://www.wikidata.org/wiki/Q356176'
SET person_16456d4d592b.wikipedia = 'https://en.wikipedia.org/wiki/Joe_Newman_(trumpeter)'
SET person_16456d4d592b.databases = ['http://id.loc.gov/authorities/names/n86145240', 'https://adp.library.ucsb.edu/names/207262', 'https://catalogue.bnf.fr/ark:/12148/cb13897933z', 'https://d-nb.info/gnd/134472675', 'http://snaccooperative.org/ark:/99166/w6xk9xmq', 'https://www.worldcat.org/identities/lccn-n86145240']
SET person_16456d4d592b.musicbrainz = 'https://musicbrainz.org/artist/ed9070ec-f1d2-405f-a386-16456d4d592b'
SET person_16456d4d592b.isni_list = ['http://isni.org/isni/0000000083804266']
SET person_16456d4d592b.source = 'musicbrainz.org'


MERGE (person_d585b8a14ce1:Person{ uuid: 'a85b66d2-34df-4d5a-8c0d-d585b8a14ce1' }) 
SET person_d585b8a14ce1.name = 'Kenny Burrell'
SET person_d585b8a14ce1.gender = 'Male'
SET person_d585b8a14ce1.country = 'US'
SET person_d585b8a14ce1.allmusic = 'https://www.allmusic.com/artist/mn0000068780'
SET person_d585b8a14ce1.discogs = 'https://www.discogs.com/artist/30184'
SET person_d585b8a14ce1.viaf = 'http://viaf.org/viaf/42024720'
SET person_d585b8a14ce1.wikidata = 'https://www.wikidata.org/wiki/Q255355'
SET person_d585b8a14ce1.databases = ['http://id.loc.gov/authorities/names/n81071440', 'https://adp.library.ucsb.edu/names/306302', 'https://catalogue.bnf.fr/ark:/12148/cb13891997r', 'https://d-nb.info/gnd/134340965', 'http://snaccooperative.org/ark:/99166/w60g4rc6', 'https://rateyourmusic.com/artist/kenny_burrell', 'https://www.musik-sammler.de/artist/kenny-burrell/', 'https://www.worldcat.org/identities/lccn-n81071440']
SET person_d585b8a14ce1.musicbrainz = 'https://musicbrainz.org/artist/a85b66d2-34df-4d5a-8c0d-d585b8a14ce1'
SET person_d585b8a14ce1.isni_list = ['http://isni.org/isni/0000000114426449']
SET person_d585b8a14ce1.source = 'musicbrainz.org'


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


// performances

MERGE (perf_e7339f336c20:Performance{ uuid: 'deae0885-6848-429b-a2c5-e7339f336c20' })
SET perf_e7339f336c20.name = 'Birthday for Jacquet'
SET perf_e7339f336c20.duration = '13:01'
SET perf_e7339f336c20.begin_date = '1972-10-06'
SET perf_e7339f336c20.end_date = '1972-10-06'
SET perf_e7339f336c20.source = 'musicbrainz.org'


MERGE (perf_db05b55b8ded:Performance{ uuid: 'b6928d3a-be74-48ae-b6d4-db05b55b8ded' })
SET perf_db05b55b8ded.name = 'Polka Dots and Moonbeams'
SET perf_db05b55b8ded.duration = '5:48'
SET perf_db05b55b8ded.begin_date = '1972-10-06'
SET perf_db05b55b8ded.end_date = '1972-10-06'
SET perf_db05b55b8ded.source = 'musicbrainz.org'


MERGE (perf_ea9bd12f7015:Performance{ uuid: 'ef8bb1dc-9987-4521-8b4c-ea9bd12f7015' })
SET perf_ea9bd12f7015.name = 'Blues for Kenny'
SET perf_ea9bd12f7015.duration = '10:35'
SET perf_ea9bd12f7015.begin_date = '1972-10-06'
SET perf_ea9bd12f7015.end_date = '1972-10-06'
SET perf_ea9bd12f7015.source = 'musicbrainz.org'


MERGE (perf_505a0bdf9b48:Performance{ uuid: '710a1a5a-001e-4a99-bb69-505a0bdf9b48' })
SET perf_505a0bdf9b48.name = 'Robbin\\'s Nest'
SET perf_505a0bdf9b48.duration = '9:25'
SET perf_505a0bdf9b48.begin_date = '1972-10-06'
SET perf_505a0bdf9b48.end_date = '1972-10-06'
SET perf_505a0bdf9b48.source = 'musicbrainz.org'


MERGE (perf_109d45a52204:Performance{ uuid: 'cc026ad2-8a75-43b3-9237-109d45a52204' })
SET perf_109d45a52204.name = 'Blues From Louisiana'
SET perf_109d45a52204.duration = '18:05'
SET perf_109d45a52204.begin_date = '1972-10-06'
SET perf_109d45a52204.end_date = '1972-10-06'
SET perf_109d45a52204.source = 'musicbrainz.org'



// tracks
MERGE (release_0db3bdcc2b3d)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_e7339f336c20)
MERGE (release_0db3bdcc2b3d)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_db05b55b8ded)
MERGE (release_0db3bdcc2b3d)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_ea9bd12f7015)
MERGE (release_0db3bdcc2b3d)-[:HAS_TRACK {name: 'B1', sequence: 4}]->(perf_505a0bdf9b48)
MERGE (release_0db3bdcc2b3d)-[:HAS_TRACK {name: 'B2', sequence: 5}]->(perf_109d45a52204)

// works

MERGE (person_14002aa8d5f5:Person{ uuid: '15972619-2cb8-4187-8581-14002aa8d5f5' }) 
SET person_14002aa8d5f5.name = 'Sir Charles Thompson'
SET person_14002aa8d5f5.gender = 'Male'
SET person_14002aa8d5f5.disambiguation = 'jazz'
SET person_14002aa8d5f5.country = 'US'
SET person_14002aa8d5f5.allmusic = 'https://www.allmusic.com/artist/mn0000747654'
SET person_14002aa8d5f5.discogs = 'https://www.discogs.com/artist/310293'
SET person_14002aa8d5f5.viaf = 'http://viaf.org/viaf/10034935'
SET person_14002aa8d5f5.wikidata = 'https://www.wikidata.org/wiki/Q725415'
SET person_14002aa8d5f5.wikipedia = 'https://en.wikipedia.org/wiki/Charles_Thompson_(jazz)'
SET person_14002aa8d5f5.databases = ['http://id.loc.gov/authorities/names/n85244979', 'https://adp.library.ucsb.edu/names/210152', 'https://catalogue.bnf.fr/ark:/12148/cb13900419n', 'https://d-nb.info/gnd/134539354', 'http://snaccooperative.org/ark:/99166/w6k6716x', 'https://www.worldcat.org/identities/lccn-n85244979']
SET person_14002aa8d5f5.musicbrainz = 'https://musicbrainz.org/artist/15972619-2cb8-4187-8581-14002aa8d5f5'
SET person_14002aa8d5f5.isni_list = ['http://isni.org/isni/0000000073641125']
SET person_14002aa8d5f5.source = 'musicbrainz.org'


MERGE (person_8825529afd5d:Person{ uuid: 'c9b9ec99-b592-4556-aa0b-8825529afd5d' }) 
SET person_8825529afd5d.name = 'Johnny Burke'
SET person_8825529afd5d.gender = 'Male'
SET person_8825529afd5d.disambiguation = 'American lyricist, 1908-1964'
SET person_8825529afd5d.country = 'US'
SET person_8825529afd5d.allmusic = 'https://www.allmusic.com/artist/mn0001053846'
SET person_8825529afd5d.discogs = 'https://www.discogs.com/artist/301993'
SET person_8825529afd5d.imdb = 'https://www.imdb.com/name/nm0121741/'
SET person_8825529afd5d.viaf = 'http://viaf.org/viaf/76583294'
SET person_8825529afd5d.wikidata = 'https://www.wikidata.org/wiki/Q743229'
SET person_8825529afd5d.databases = ['http://id.loc.gov/authorities/names/no89004670', 'https://adp.library.ucsb.edu/names/108757', 'https://catalogue.bnf.fr/ark:/12148/cb148427966', 'https://d-nb.info/gnd/102085412X', 'http://snaccooperative.org/ark:/99166/w6z61w7v', 'https://nla.gov.au/nla.party-887950', 'https://rateyourmusic.com/artist/johnny_burke_f1', 'https://www.ibdb.com/person.php?id=11462', 'https://www.worldcat.org/identities/lccn-no89004670/']
SET person_8825529afd5d.musicbrainz = 'https://musicbrainz.org/artist/c9b9ec99-b592-4556-aa0b-8825529afd5d'
SET person_8825529afd5d.isni_list = ['http://isni.org/isni/0000000071400010']
SET person_8825529afd5d.source = 'musicbrainz.org'


MERGE (person_4bb27485ceca:Person{ uuid: '6c355895-7b21-488a-9147-4bb27485ceca' }) 
SET person_4bb27485ceca.name = 'Bob Russell'
SET person_4bb27485ceca.gender = 'Male'
SET person_4bb27485ceca.disambiguation = 'US songwriter/lyricist Sidney Keith “Bob” Russell'
SET person_4bb27485ceca.country = 'US'
SET person_4bb27485ceca.discogs = 'https://www.discogs.com/artist/449216'
SET person_4bb27485ceca.discogs = 'https://www.discogs.com/artist/725888'
SET person_4bb27485ceca.imdb = 'https://www.imdb.com/name/nm0751035/'
SET person_4bb27485ceca.viaf = 'http://viaf.org/viaf/66733637'
SET person_4bb27485ceca.wikidata = 'https://www.wikidata.org/wiki/Q888226'
SET person_4bb27485ceca.databases = ['http://id.loc.gov/authorities/names/n87860169', 'https://adp.library.ucsb.edu/names/105700', 'https://catalogue.bnf.fr/ark:/12148/cb148431316', 'https://d-nb.info/gnd/134797981', 'https://nla.gov.au/nla.party-1526172', 'https://www.worldcat.org/identities/lccn-n87860169/']
SET person_4bb27485ceca.musicbrainz = 'https://musicbrainz.org/artist/6c355895-7b21-488a-9147-4bb27485ceca'
SET person_4bb27485ceca.isni_list = ['http://isni.org/isni/0000000107844378']
SET person_4bb27485ceca.source = 'musicbrainz.org'


MERGE (person_a6d92136636f:Person{ uuid: '8d3f8b43-0d28-4500-900e-a6d92136636f' }) 
SET person_a6d92136636f.name = 'Jimmy Van Heusen'
SET person_a6d92136636f.gender = 'Male'
SET person_a6d92136636f.country = 'US'
SET person_a6d92136636f.allmusic = 'https://www.allmusic.com/artist/mn0000309464'
SET person_a6d92136636f.allmusic = 'https://www.allmusic.com/artist/mn0003168282'
SET person_a6d92136636f.discogs = 'https://www.discogs.com/artist/255313'
SET person_a6d92136636f.imdb = 'https://www.imdb.com/name/nm0006329/'
SET person_a6d92136636f.viaf = 'http://viaf.org/viaf/54338466'
SET person_a6d92136636f.wikidata = 'https://www.wikidata.org/wiki/Q33124'
SET person_a6d92136636f.databases = ['http://id.loc.gov/authorities/names/n87146380', 'https://adp.library.ucsb.edu/names/105592', 'https://catalogue.bnf.fr/ark:/12148/cb13952105n', 'https://d-nb.info/gnd/134545370', 'https://ibdb.com/person.php?id=12521', 'http://snaccooperative.org/ark:/99166/w6zc82bn', 'https://nla.gov.au/nla.party-887953', 'https://rateyourmusic.com/artist/jimmy_van_heusen', 'https://www.worldcat.org/identities/lccn-n87146380/']
SET person_a6d92136636f.musicbrainz = 'https://musicbrainz.org/artist/8d3f8b43-0d28-4500-900e-a6d92136636f'
SET person_a6d92136636f.isni_list = ['http://isni.org/isni/0000000081333253']
SET person_a6d92136636f.source = 'musicbrainz.org'


MERGE (work_bd8f035e170e:Work{ uuid: '90fe9bba-988d-4fc4-aff7-bd8f035e170e' })
SET work_bd8f035e170e.name = 'Blues for Gerry'
SET work_bd8f035e170e.source = 'musicbrainz.org'


MERGE (work_265084ca0934:Work{ uuid: 'd0392e86-d8c3-4278-b0b2-265084ca0934' })
SET work_265084ca0934.name = 'Robbins’ Nest'
SET work_265084ca0934.iswc = 'T-070.243.205-0'
SET work_265084ca0934.type = 'Song'
SET work_265084ca0934.musicbrainz = 'https://musicbrainz.org/work/d0392e86-d8c3-4278-b0b2-265084ca0934'
SET work_265084ca0934.source = 'musicbrainz.org'


MERGE (work_fef963759bfa:Work{ uuid: 'f32a8ad2-1196-3e41-85dd-fef963759bfa' })
SET work_fef963759bfa.name = 'Polka Dots and Moonbeams'
SET work_fef963759bfa.iswc = 'T-070.166.193-9'
SET work_fef963759bfa.type = 'Song'
SET work_fef963759bfa.wikidata = 'https://www.wikidata.org/wiki/Q3366103'
SET work_fef963759bfa.musicbrainz = 'https://musicbrainz.org/work/f32a8ad2-1196-3e41-85dd-fef963759bfa'
SET work_fef963759bfa.source = 'musicbrainz.org'



// performances of
MERGE (perf_ea9bd12f7015)-[:PERFORMANCE_OF]->(work_bd8f035e170e)
MERGE (perf_505a0bdf9b48)-[:PERFORMANCE_OF]->(work_265084ca0934)
MERGE (perf_db05b55b8ded)-[:PERFORMANCE_OF]->(work_fef963759bfa)


// composers
MERGE (person_b7acdad1459c)-[:COMPOSED]->(work_265084ca0934)
MERGE (person_14002aa8d5f5)-[:COMPOSED]->(work_265084ca0934)
MERGE (person_4bb27485ceca)-[:WROTE_LYRICS]->(work_265084ca0934)
MERGE (person_a6d92136636f)-[:COMPOSED]->(work_fef963759bfa)
MERGE (person_8825529afd5d)-[:WROTE_LYRICS]->(work_fef963759bfa)


// place nodes

MERGE (place_344332e41f0a:Place{ uuid: '80b1ef04-44ea-4270-ae6a-344332e41f0a' })
SET place_344332e41f0a.name = 'Teichiku Studio'
SET place_344332e41f0a.source = 'musicbrainz.org'


// place relationships
MERGE (perf_e7339f336c20)-[:HAS_PLACE { type: 'recorded at', begin_date: '1972-10-06', end_date: '1972-10-06' }]->(place_344332e41f0a)
MERGE (perf_db05b55b8ded)-[:HAS_PLACE { type: 'recorded at', begin_date: '1972-10-06', end_date: '1972-10-06' }]->(place_344332e41f0a)
MERGE (perf_ea9bd12f7015)-[:HAS_PLACE { type: 'recorded at', begin_date: '1972-10-06', end_date: '1972-10-06' }]->(place_344332e41f0a)
MERGE (perf_505a0bdf9b48)-[:HAS_PLACE { type: 'recorded at', begin_date: '1972-10-06', end_date: '1972-10-06' }]->(place_344332e41f0a)
MERGE (perf_109d45a52204)-[:HAS_PLACE { type: 'recorded at', begin_date: '1972-10-06', end_date: '1972-10-06' }]->(place_344332e41f0a)

MERGE (person_d585b8a14ce1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_e7339f336c20)
MERGE (person_e5f45e8d25d7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flugelhorn'] }]->(perf_e7339f336c20)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e7339f336c20)
MERGE (person_b7acdad1459c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_e7339f336c20)
MERGE (person_983ca8e60b14)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_e7339f336c20)
MERGE (person_71aaf0f6b267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_e7339f336c20)
MERGE (person_16456d4d592b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_e7339f336c20)
MERGE (person_8be01f64b4ea)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_e7339f336c20)
MERGE (person_e9753d5ae693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['keyboard'] }]->(perf_e7339f336c20)
MERGE (person_d585b8a14ce1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_db05b55b8ded)
MERGE (person_e5f45e8d25d7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flugelhorn'] }]->(perf_db05b55b8ded)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_db05b55b8ded)
MERGE (person_b7acdad1459c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_db05b55b8ded)
MERGE (person_983ca8e60b14)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_db05b55b8ded)
MERGE (person_71aaf0f6b267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_db05b55b8ded)
MERGE (person_16456d4d592b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_db05b55b8ded)
MERGE (person_8be01f64b4ea)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_db05b55b8ded)
MERGE (person_e9753d5ae693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['keyboard'] }]->(perf_db05b55b8ded)
MERGE (person_d585b8a14ce1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_ea9bd12f7015)
MERGE (person_e5f45e8d25d7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flugelhorn'] }]->(perf_ea9bd12f7015)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_ea9bd12f7015)
MERGE (person_b7acdad1459c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_ea9bd12f7015)
MERGE (person_983ca8e60b14)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_ea9bd12f7015)
MERGE (person_71aaf0f6b267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_ea9bd12f7015)
MERGE (person_16456d4d592b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_ea9bd12f7015)
MERGE (person_8be01f64b4ea)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_ea9bd12f7015)
MERGE (person_e9753d5ae693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['keyboard'] }]->(perf_ea9bd12f7015)
MERGE (person_d585b8a14ce1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_505a0bdf9b48)
MERGE (person_e5f45e8d25d7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flugelhorn'] }]->(perf_505a0bdf9b48)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_505a0bdf9b48)
MERGE (person_b7acdad1459c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_505a0bdf9b48)
MERGE (person_983ca8e60b14)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_505a0bdf9b48)
MERGE (person_71aaf0f6b267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_505a0bdf9b48)
MERGE (person_16456d4d592b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_505a0bdf9b48)
MERGE (person_8be01f64b4ea)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_505a0bdf9b48)
MERGE (person_e9753d5ae693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['keyboard'] }]->(perf_505a0bdf9b48)
MERGE (person_d585b8a14ce1)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_109d45a52204)
MERGE (person_e5f45e8d25d7)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flugelhorn'] }]->(perf_109d45a52204)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_109d45a52204)
MERGE (person_b7acdad1459c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_109d45a52204)
MERGE (person_983ca8e60b14)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_109d45a52204)
MERGE (person_71aaf0f6b267)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_109d45a52204)
MERGE (person_16456d4d592b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_109d45a52204)
MERGE (person_8be01f64b4ea)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_109d45a52204)
MERGE (person_e9753d5ae693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['keyboard'] }]->(perf_109d45a52204)



"""
)