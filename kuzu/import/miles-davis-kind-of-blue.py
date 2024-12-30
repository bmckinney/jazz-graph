
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_6455e87ba60b:Release{ uuid: 'bee5e0cd-1767-4a8e-9578-6455e87ba60b' })
SET release_6455e87ba60b.name = 'Kind of Blue'
SET release_6455e87ba60b.disambiguation = 'stereo'
SET release_6455e87ba60b.country = 'US'
SET release_6455e87ba60b.date = '1959-08-17'
SET release_6455e87ba60b.format = '12" Vinyl'
SET release_6455e87ba60b.discode = 'CS 8163'
SET release_6455e87ba60b.discogs = 'https://www.discogs.com/release/1353040'
SET release_6455e87ba60b.musicbrainz = 'http://musicbrainz.org/release/bee5e0cd-1767-4a8e-9578-6455e87ba60b'
SET release_6455e87ba60b.source = 'musicbrainz.org'


MERGE (person_13d821490e42:Person{ uuid: 'd3f9352c-18e2-47a0-802c-13d821490e42' }) 
SET person_13d821490e42.name = 'Wynton Kelly'
SET person_13d821490e42.gender = 'Male'
SET person_13d821490e42.country = 'US'
SET person_13d821490e42.allmusic = 'https://www.allmusic.com/artist/mn0000684253'
SET person_13d821490e42.discogs = 'https://www.discogs.com/artist/252308'
SET person_13d821490e42.imdb = 'https://www.imdb.com/name/nm4017040/'
SET person_13d821490e42.viaf = 'http://viaf.org/viaf/29718356'
SET person_13d821490e42.wikidata = 'https://www.wikidata.org/wiki/Q536415'
SET person_13d821490e42.databases = ['http://id.loc.gov/authorities/names/n84148411', 'https://catalogue.bnf.fr/ark:/12148/cb13895927j', 'https://d-nb.info/gnd/134424549', 'https://rateyourmusic.com/artist/wynton_kelly', 'https://www.worldcat.org/identities/lccn-n84148411']
SET person_13d821490e42.musicbrainz = 'https://musicbrainz.org/artist/d3f9352c-18e2-47a0-802c-13d821490e42'
SET person_13d821490e42.isni_list = ['http://isni.org/isni/0000000109624133']
SET person_13d821490e42.source = 'musicbrainz.org'


MERGE (person_6c57b03a4e36:Person{ uuid: '8247a3f2-3a8e-4256-b322-6c57b03a4e36' }) 
SET person_6c57b03a4e36.name = 'Bill Evans'
SET person_6c57b03a4e36.gender = 'Male'
SET person_6c57b03a4e36.disambiguation = 'pianist'
SET person_6c57b03a4e36.country = 'US'
SET person_6c57b03a4e36.allmusic = 'https://www.allmusic.com/artist/mn0000764702'
SET person_6c57b03a4e36.bbc = 'https://www.bbc.co.uk/music/artists/8247a3f2-3a8e-4256-b322-6c57b03a4e36'
SET person_6c57b03a4e36.discogs = 'https://www.discogs.com/artist/252310'
SET person_6c57b03a4e36.imdb = 'https://www.imdb.com/name/nm0262572/'
SET person_6c57b03a4e36.viaf = 'http://viaf.org/viaf/29717820'
SET person_6c57b03a4e36.wikidata = 'https://www.wikidata.org/wiki/Q208205'
SET person_6c57b03a4e36.databases = ['http://id.loc.gov/authorities/names/n81147281', 'https://adp.library.ucsb.edu/names/203037', 'https://castalbums.org/people/Bill-Evans-1/11965', 'https://catalogue.bnf.fr/ark:/12148/cb13893736g', 'https://d-nb.info/gnd/137724519', 'https://id.oclc.org/worldcat/entity/E39PBJf8xcCTxHr9htXyQxwpyd', 'https://musicmoz.org/Bands_and_Artists/E/Evans,_Bill/', 'http://snaccooperative.org/ark:/99166/w6v411q5', 'https://openlibrary.org/authors/OL6591650A', 'https://openlibrary.org/authors/OL7514955A', 'https://operabase.com/a2242729', 'https://rateyourmusic.com/artist/bill_evans', 'https://www.dramonline.org/composers/evans-bill', 'https://www.librarything.com/author/evansbill-1-5203912', 'https://www.musik-sammler.de/artist/175764/', 'https://www.muziekweb.nl/Link/M00000255981/POPULAR/', 'https://www.themoviedb.org/person/137953', 'https://www.whosampled.com/Bill-Evans/', 'https://www.worldcat.org/identities/lccn-n81-147281', 'http://www.maniadb.com/artist/117793']
SET person_6c57b03a4e36.musicbrainz = 'https://musicbrainz.org/artist/8247a3f2-3a8e-4256-b322-6c57b03a4e36'
SET person_6c57b03a4e36.isni_list = ['http://isni.org/isni/0000000121261603']
SET person_6c57b03a4e36.source = 'musicbrainz.org'


MERGE (person_f35080d12d60:Person{ uuid: '5ca16cfc-f480-4203-93e7-f35080d12d60' }) 
SET person_f35080d12d60.name = 'Irving Townsend'
SET person_f35080d12d60.gender = 'Male'
SET person_f35080d12d60.country = 'US'
SET person_f35080d12d60.discogs = 'https://www.discogs.com/artist/239628'
SET person_f35080d12d60.wikidata = 'https://www.wikidata.org/wiki/Q6074822'
SET person_f35080d12d60.musicbrainz = 'https://musicbrainz.org/artist/5ca16cfc-f480-4203-93e7-f35080d12d60'
SET person_f35080d12d60.source = 'musicbrainz.org'


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


MERGE (person_084c872be8e5:Person{ uuid: 'febc30e8-5033-4c65-b25c-084c872be8e5' }) 
SET person_084c872be8e5.name = 'Fred Plaut'
SET person_084c872be8e5.gender = 'Male'
SET person_084c872be8e5.country = 'US'
SET person_084c872be8e5.viaf = 'http://viaf.org/viaf/44566177'
SET person_084c872be8e5.wikidata = 'https://www.wikidata.org/wiki/Q5496081'
SET person_084c872be8e5.databases = ['http://id.loc.gov/authorities/names/nr2002014455', 'https://catalogue.bnf.fr/ark:/12148/cb148051802', 'https://d-nb.info/gnd/119157691', 'http://snaccooperative.org/ark:/99166/w6z32k3p', 'https://www.worldcat.org/identities/containsVIAFID/44566177']
SET person_084c872be8e5.musicbrainz = 'https://musicbrainz.org/artist/febc30e8-5033-4c65-b25c-084c872be8e5'
SET person_084c872be8e5.isni_list = ['http://isni.org/isni/0000000114715435']
SET person_084c872be8e5.source = 'musicbrainz.org'


MERGE (person_7de13124b970:Person{ uuid: 'b6ff4fd0-03ae-41a6-942e-7de13124b970' }) 
SET person_7de13124b970.name = 'Paul Chambers'
SET person_7de13124b970.gender = 'Male'
SET person_7de13124b970.disambiguation = 'US jazz bassist'
SET person_7de13124b970.country = 'US'
SET person_7de13124b970.allmusic = 'https://www.allmusic.com/artist/mn0000747984'
SET person_7de13124b970.discogs = 'https://www.discogs.com/artist/259778'
SET person_7de13124b970.imdb = 'https://www.imdb.com/name/nm2424848/'
SET person_7de13124b970.viaf = 'http://viaf.org/viaf/100313280'
SET person_7de13124b970.wikidata = 'https://www.wikidata.org/wiki/Q541659'
SET person_7de13124b970.databases = ['http://id.loc.gov/authorities/names/n84148412', 'https://adp.library.ucsb.edu/names/308013', 'https://catalogue.bnf.fr/ark:/12148/cb138923573', 'https://d-nb.info/gnd/134345797', 'http://snaccooperative.org/ark:/99166/w6ht3khn', 'https://www.worldcat.org/identities/lccn-n84148412']
SET person_7de13124b970.musicbrainz = 'https://musicbrainz.org/artist/b6ff4fd0-03ae-41a6-942e-7de13124b970'
SET person_7de13124b970.isni_list = ['http://isni.org/isni/0000000109289128']
SET person_7de13124b970.source = 'musicbrainz.org'


MERGE (person_323e6ce46c2a:Person{ uuid: '561d854a-6a28-4aa7-8c99-323e6ce46c2a' }) 
SET person_323e6ce46c2a.name = 'Miles Davis'
SET person_323e6ce46c2a.gender = 'Male'
SET person_323e6ce46c2a.disambiguation = 'jazz trumpeter, bandleader, songwriter'
SET person_323e6ce46c2a.country = 'US'
SET person_323e6ce46c2a.allmusic = 'https://www.allmusic.com/artist/mn0000423829'
SET person_323e6ce46c2a.bbc = 'https://www.bbc.co.uk/music/artists/561d854a-6a28-4aa7-8c99-323e6ce46c2a'
SET person_323e6ce46c2a.discogs = 'https://www.discogs.com/artist/23755'
SET person_323e6ce46c2a.imdb = 'https://www.imdb.com/name/nm0002537/'
SET person_323e6ce46c2a.viaf = 'http://viaf.org/viaf/97762193'
SET person_323e6ce46c2a.wikidata = 'https://www.wikidata.org/wiki/Q93341'
SET person_323e6ce46c2a.databases = ['http://id.loc.gov/authorities/names/n50035608', 'http://musicmoz.org/Bands_and_Artists/D/Davis,_Miles/', 'https://catalogue.bnf.fr/ark:/12148/cb13893030g', 'https://d-nb.info/gnd/118524046', 'http://snaccooperative.org/ark:/99166/w68k7wq0', 'https://openlibrary.org/works/OL4359245A', 'https://rateyourmusic.com/artist/miles_davis', 'https://www.45cat.com/artist/miles-davis', 'https://www.45worlds.com/78rpm/artist/miles-davis', 'https://www.45worlds.com/cdalbum/artist/miles-davis', 'https://www.45worlds.com/live/artist/miles-davis', 'https://www.45worlds.com/tape/artist/miles-davis', 'https://www.45worlds.com/vinyl/artist/miles-davis', 'https://www.muziekweb.nl/Link/M00000286446/', 'https://www.worldcat.org/identities/lccn-n50035608']
SET person_323e6ce46c2a.musicbrainz = 'https://musicbrainz.org/artist/561d854a-6a28-4aa7-8c99-323e6ce46c2a'
SET person_323e6ce46c2a.isni_list = ['http://isni.org/isni/000000012144707X']
SET person_323e6ce46c2a.source = 'musicbrainz.org'


MERGE (person_2fe1f9f27da8:Person{ uuid: 'a4c73ebe-b2c7-4f13-b99d-2fe1f9f27da8' }) 
SET person_2fe1f9f27da8.name = 'Cannonball Adderley'
SET person_2fe1f9f27da8.gender = 'Male'
SET person_2fe1f9f27da8.country = 'US'
SET person_2fe1f9f27da8.allmusic = 'https://www.allmusic.com/artist/mn0000548338'
SET person_2fe1f9f27da8.discogs = 'https://www.discogs.com/artist/61585'
SET person_2fe1f9f27da8.imdb = 'https://www.imdb.com/name/nm0011645/'
SET person_2fe1f9f27da8.viaf = 'http://viaf.org/viaf/36906016'
SET person_2fe1f9f27da8.wikidata = 'https://www.wikidata.org/wiki/Q110477'
SET person_2fe1f9f27da8.databases = ['http://id.loc.gov/authorities/names/n84163049', 'https://catalogue.bnf.fr/ark:/12148/cb138905900', 'https://d-nb.info/gnd/122466616', 'http://snaccooperative.org/ark:/99166/w65q52jh', 'https://rateyourmusic.com/artist/cannonball_adderley', 'https://www.worldcat.org/identities/lccn-n84163049']
SET person_2fe1f9f27da8.musicbrainz = 'https://musicbrainz.org/artist/a4c73ebe-b2c7-4f13-b99d-2fe1f9f27da8'
SET person_2fe1f9f27da8.isni_list = ['http://isni.org/isni/000000011566991X']
SET person_2fe1f9f27da8.source = 'musicbrainz.org'


MERGE (person_fe2cd264bbd0:Person{ uuid: 'd0cbf65a-541b-476a-996c-fe2cd264bbd0' }) 
SET person_fe2cd264bbd0.name = 'Jimmy Cobb'
SET person_fe2cd264bbd0.gender = 'Male'
SET person_fe2cd264bbd0.disambiguation = 'US jazz drummer'
SET person_fe2cd264bbd0.country = 'US'
SET person_fe2cd264bbd0.allmusic = 'https://www.allmusic.com/artist/mn0000350892'
SET person_fe2cd264bbd0.discogs = 'https://www.discogs.com/artist/252311'
SET person_fe2cd264bbd0.imdb = 'https://www.imdb.com/name/nm0167780/'
SET person_fe2cd264bbd0.viaf = 'http://viaf.org/viaf/85107638'
SET person_fe2cd264bbd0.wikidata = 'https://www.wikidata.org/wiki/Q499491'
SET person_fe2cd264bbd0.databases = ['http://id.loc.gov/authorities/names/n86857266', 'https://adp.library.ucsb.edu/names/105463', 'https://catalogue.bnf.fr/ark:/12148/cb13892597w', 'https://d-nb.info/gnd/134566394', 'https://www.worldcat.org/identities/lccn-n86857266']
SET person_fe2cd264bbd0.musicbrainz = 'https://musicbrainz.org/artist/d0cbf65a-541b-476a-996c-fe2cd264bbd0'
SET person_fe2cd264bbd0.isni_list = ['http://isni.org/isni/0000000114945249']
SET person_fe2cd264bbd0.source = 'musicbrainz.org'

// labels

MERGE (label_0400dd45693e:Label{ uuid: '011d1192-6f65-45bd-85c4-0400dd45693e' })
SET label_0400dd45693e.name= 'Columbia'

// performances

MERGE (perf_905334c9a48a:Performance{ uuid: '60f750f4-d222-46b7-ad5c-905334c9a48a' })
SET perf_905334c9a48a.name = 'So What'
SET perf_905334c9a48a.disambiguation = 'stereo'
SET perf_905334c9a48a.duration = '9:05'
SET perf_905334c9a48a.begin_date = '1959-03-02'
SET perf_905334c9a48a.end_date = '1959-03-02'
SET perf_905334c9a48a.source = 'musicbrainz.org'


MERGE (perf_86d6e973196f:Performance{ uuid: '852bf62a-29f9-4026-abc5-86d6e973196f' })
SET perf_86d6e973196f.name = 'Freddie Freeloader'
SET perf_86d6e973196f.disambiguation = 'stereo'
SET perf_86d6e973196f.duration = '9:35'
SET perf_86d6e973196f.begin_date = '1959-03-02'
SET perf_86d6e973196f.end_date = '1959-03-02'
SET perf_86d6e973196f.source = 'musicbrainz.org'


MERGE (perf_9eace7e208f2:Performance{ uuid: '67a9794c-153a-4a24-82ec-9eace7e208f2' })
SET perf_9eace7e208f2.name = 'Blue in Green'
SET perf_9eace7e208f2.disambiguation = 'stereo'
SET perf_9eace7e208f2.duration = '5:28'
SET perf_9eace7e208f2.source = 'musicbrainz.org'


MERGE (perf_3d0cee232925:Performance{ uuid: 'b7ebe185-21e9-4400-a17a-3d0cee232925' })
SET perf_3d0cee232925.name = 'All Blues'
SET perf_3d0cee232925.disambiguation = 'stereo'
SET perf_3d0cee232925.duration = '11:33'
SET perf_3d0cee232925.begin_date = '1959-04-22'
SET perf_3d0cee232925.end_date = '1959-04-22'
SET perf_3d0cee232925.source = 'musicbrainz.org'


MERGE (perf_5d1a166e0f2f:Performance{ uuid: '250b3f1d-7620-42a9-87b3-5d1a166e0f2f' })
SET perf_5d1a166e0f2f.name = 'Flamenco Sketches'
SET perf_5d1a166e0f2f.disambiguation = 'stereo'
SET perf_5d1a166e0f2f.duration = '9:24'
SET perf_5d1a166e0f2f.begin_date = '1959-04-22'
SET perf_5d1a166e0f2f.end_date = '1959-04-22'
SET perf_5d1a166e0f2f.source = 'musicbrainz.org'




// labels
MERGE (release_6455e87ba60b)-[:HAS_LABEL]->(label_0400dd45693e)


// tracks
MERGE (release_6455e87ba60b)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_905334c9a48a)
MERGE (release_6455e87ba60b)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_86d6e973196f)
MERGE (release_6455e87ba60b)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_9eace7e208f2)
MERGE (release_6455e87ba60b)-[:HAS_TRACK {name: 'B1', sequence: 4}]->(perf_3d0cee232925)
MERGE (release_6455e87ba60b)-[:HAS_TRACK {name: 'B2', sequence: 5}]->(perf_5d1a166e0f2f)

// works

MERGE (work_d7943efb9a03:Work{ uuid: '54d591f2-e928-3263-b963-d7943efb9a03' })
SET work_d7943efb9a03.name = 'Blue in Green'
SET work_d7943efb9a03.iswc = 'T-073.092.724-8'
SET work_d7943efb9a03.type = 'Song'
SET work_d7943efb9a03.wikidata = 'https://www.wikidata.org/wiki/Q510852'
SET work_d7943efb9a03.musicbrainz = 'https://musicbrainz.org/work/54d591f2-e928-3263-b963-d7943efb9a03'
SET work_d7943efb9a03.source = 'musicbrainz.org'


MERGE (work_c46c80a82e1b:Work{ uuid: '36ff917b-6e10-3ee0-9e42-c46c80a82e1b' })
SET work_c46c80a82e1b.name = 'Flamenco Sketches'
SET work_c46c80a82e1b.type = 'Song'
SET work_c46c80a82e1b.wikidata = 'https://www.wikidata.org/wiki/Q1142997'
SET work_c46c80a82e1b.musicbrainz = 'https://musicbrainz.org/work/36ff917b-6e10-3ee0-9e42-c46c80a82e1b'
SET work_c46c80a82e1b.source = 'musicbrainz.org'


MERGE (work_382bacca0923:Work{ uuid: '500ecdf1-a82e-3afc-9268-382bacca0923' })
SET work_382bacca0923.name = 'Freddie Freeloader'
SET work_382bacca0923.iswc = 'T-073.092.747-5'
SET work_382bacca0923.wikidata = 'https://www.wikidata.org/wiki/Q1452600'
SET work_382bacca0923.musicbrainz = 'https://musicbrainz.org/work/500ecdf1-a82e-3afc-9268-382bacca0923'
SET work_382bacca0923.source = 'musicbrainz.org'


MERGE (work_1938072b1375:Work{ uuid: '46e6bfc3-5f37-3e6e-a2be-1938072b1375' })
SET work_1938072b1375.name = 'All Blues'
SET work_1938072b1375.iswc = 'T-039.266.451-5'
SET work_1938072b1375.type = 'Song'
SET work_1938072b1375.wikidata = 'https://www.wikidata.org/wiki/Q2600918'
SET work_1938072b1375.musicbrainz = 'https://musicbrainz.org/work/46e6bfc3-5f37-3e6e-a2be-1938072b1375'
SET work_1938072b1375.source = 'musicbrainz.org'


MERGE (work_3a7d6599a72e:Work{ uuid: '2fafd730-423f-342e-b6c7-3a7d6599a72e' })
SET work_3a7d6599a72e.name = 'So What'
SET work_3a7d6599a72e.iswc = 'T-073.092.797-5'
SET work_3a7d6599a72e.type = 'Song'
SET work_3a7d6599a72e.wikidata = 'https://www.wikidata.org/wiki/Q919291'
SET work_3a7d6599a72e.musicbrainz = 'https://musicbrainz.org/work/2fafd730-423f-342e-b6c7-3a7d6599a72e'
SET work_3a7d6599a72e.source = 'musicbrainz.org'



// performances of
MERGE (perf_9eace7e208f2)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_5d1a166e0f2f)-[:PERFORMANCE_OF]->(work_c46c80a82e1b)
MERGE (perf_86d6e973196f)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_3d0cee232925)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_905334c9a48a)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)


// composers
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_d7943efb9a03)
MERGE (person_6c57b03a4e36)-[:COMPOSED]->(work_d7943efb9a03)
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_c46c80a82e1b)
MERGE (person_6c57b03a4e36)-[:COMPOSED]->(work_c46c80a82e1b)
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_382bacca0923)
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_1938072b1375)
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_3a7d6599a72e)


// place nodes

MERGE (place_2f7f416fbd01:Place{ uuid: '3fb38491-3081-442a-9d4b-2f7f416fbd01' })
SET place_2f7f416fbd01.name = 'CBS 30th Street Studio'
SET place_2f7f416fbd01.source = 'musicbrainz.org'

MERGE (place_decbb365c07f:Place{ uuid: '74e50e58-5deb-4b99-93a2-decbb365c07f' })
SET place_decbb365c07f.name = 'New York'
SET place_decbb365c07f.source = 'musicbrainz.org'


// place relationships
MERGE (perf_905334c9a48a)-[:HAS_PLACE { type: 'recorded at', begin_date: '1959-03-02', end_date: '1959-03-02' }]->(place_2f7f416fbd01)
MERGE (perf_86d6e973196f)-[:HAS_PLACE { type: 'recorded at', begin_date: '1959-03-02', end_date: '1959-03-02' }]->(place_2f7f416fbd01)
MERGE (perf_3d0cee232925)-[:HAS_PLACE { type: 'recorded at', begin_date: '1959-04-22', end_date: '1959-04-22' }]->(place_2f7f416fbd01)
MERGE (perf_3d0cee232925)-[:HAS_PLACE { type: 'recorded in', begin_date: '1959-04-22', end_date: '1959-04-22' }]->(place_decbb365c07f)
MERGE (perf_5d1a166e0f2f)-[:HAS_PLACE { type: 'recorded at', begin_date: '1959-04-22', end_date: '1959-04-22' }]->(place_2f7f416fbd01)

MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_905334c9a48a)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_905334c9a48a)
MERGE (person_fe2cd264bbd0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_905334c9a48a)
MERGE (person_72ad46cdb831)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_905334c9a48a)
MERGE (person_323e6ce46c2a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_905334c9a48a)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_905334c9a48a)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_86d6e973196f)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_86d6e973196f)
MERGE (person_fe2cd264bbd0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_86d6e973196f)
MERGE (person_72ad46cdb831)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_86d6e973196f)
MERGE (person_323e6ce46c2a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_86d6e973196f)
MERGE (person_13d821490e42)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_86d6e973196f)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_9eace7e208f2)
MERGE (person_fe2cd264bbd0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9eace7e208f2)
MERGE (person_72ad46cdb831)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_9eace7e208f2)
MERGE (person_323e6ce46c2a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_9eace7e208f2)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_9eace7e208f2)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_3d0cee232925)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_3d0cee232925)
MERGE (person_fe2cd264bbd0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_3d0cee232925)
MERGE (person_72ad46cdb831)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_3d0cee232925)
MERGE (person_323e6ce46c2a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_3d0cee232925)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_3d0cee232925)
MERGE (person_f35080d12d60)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_3d0cee232925)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_5d1a166e0f2f)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_5d1a166e0f2f)
MERGE (person_fe2cd264bbd0)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_5d1a166e0f2f)
MERGE (person_72ad46cdb831)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_5d1a166e0f2f)
MERGE (person_323e6ce46c2a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_5d1a166e0f2f)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5d1a166e0f2f)
MERGE (person_f35080d12d60)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_5d1a166e0f2f)
MERGE (person_084c872be8e5)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_5d1a166e0f2f)



"""
)