
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_c184a79d9c78:Release{ uuid: '7fdf1f13-d8a3-41ff-a1ab-c184a79d9c78' })
SET release_c184a79d9c78.name = 'Bird at St. Nick\\'s, Volume 1'
SET release_c184a79d9c78.country = 'DK'
SET release_c184a79d9c78.date = '1957'
SET release_c184a79d9c78.format = '7" Vinyl'
SET release_c184a79d9c78.discode = 'DEP 35'
SET release_c184a79d9c78.discogs = 'https://www.discogs.com/release/2414702'
SET release_c184a79d9c78.musicbrainz = 'http://musicbrainz.org/release/7fdf1f13-d8a3-41ff-a1ab-c184a79d9c78'
SET release_c184a79d9c78.source = 'musicbrainz.org'


MERGE (person_c73775716312:Person{ uuid: 'c7356af9-9ea6-4a78-a55b-c73775716312' }) 
SET person_c73775716312.name = 'Charlie Parker'
SET person_c73775716312.gender = 'Male'
SET person_c73775716312.disambiguation = 'a.k.a. “Bird”, jazz alto saxophonist'
SET person_c73775716312.country = 'US'
SET person_c73775716312.allmusic = 'https://www.allmusic.com/artist/mn0000211758'
SET person_c73775716312.bbc = 'https://www.bbc.co.uk/music/artists/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.discogs = 'https://www.discogs.com/artist/1424206'
SET person_c73775716312.discogs = 'https://www.discogs.com/artist/753336'
SET person_c73775716312.discogs = 'https://www.discogs.com/artist/75617'
SET person_c73775716312.imdb = 'https://www.imdb.com/name/nm0662127/'
SET person_c73775716312.viaf = 'http://viaf.org/viaf/10034216'
SET person_c73775716312.wikidata = 'https://www.wikidata.org/wiki/Q103767'
SET person_c73775716312.databases = ['http://id.loc.gov/authorities/names/n50050327', 'https://adp.library.ucsb.edu/names/336464', 'https://catalogue.bnf.fr/ark:/12148/cb13898247z', 'https://d-nb.info/gnd/118739328', 'http://snaccooperative.org/ark:/99166/w67086vq', 'https://nla.gov.au/nla.party-911160', 'https://openlibrary.org/works/OL4918032A', 'https://rateyourmusic.com/artist/charlie_parker', 'https://www.musik-sammler.de/artist/charlie-parker/', 'https://www.worldcat.org/identities/lccn-n50050327']
SET person_c73775716312.musicbrainz = 'https://musicbrainz.org/artist/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.isni_list = ['http://isni.org/isni/0000000120955806', 'http://isni.org/isni/0000000368633974']
SET person_c73775716312.source = 'musicbrainz.org'


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


MERGE (person_181f6039f3dc:Person{ uuid: '0d18da0d-49ab-4ca0-ac52-181f6039f3dc' }) 
SET person_181f6039f3dc.name = 'Red Rodney'
SET person_181f6039f3dc.gender = 'Male'
SET person_181f6039f3dc.country = 'US'
SET person_181f6039f3dc.allmusic = 'https://www.allmusic.com/artist/mn0000883694'
SET person_181f6039f3dc.discogs = 'https://www.discogs.com/artist/312519'
SET person_181f6039f3dc.imdb = 'https://www.imdb.com/name/nm1012058/'
SET person_181f6039f3dc.viaf = 'http://viaf.org/viaf/5118818'
SET person_181f6039f3dc.wikidata = 'https://www.wikidata.org/wiki/Q350931'
SET person_181f6039f3dc.wikipedia = 'https://en.wikipedia.org/wiki/Red_Rodney'
SET person_181f6039f3dc.databases = ['http://id.loc.gov/authorities/names/n82078482', 'https://adp.library.ucsb.edu/names/340628', 'https://catalogue.bnf.fr/ark:/12148/cb13899101m', 'https://d-nb.info/gnd/134754204', 'http://snaccooperative.org/ark:/99166/w6kr2pkb', 'https://www.worldcat.org/identities/lccn-n82078482']
SET person_181f6039f3dc.musicbrainz = 'https://musicbrainz.org/artist/0d18da0d-49ab-4ca0-ac52-181f6039f3dc'
SET person_181f6039f3dc.isni_list = ['http://isni.org/isni/0000000063084978']
SET person_181f6039f3dc.source = 'musicbrainz.org'


MERGE (person_37e57681a3cf:Person{ uuid: '7d606f44-a90c-4c1e-909d-37e57681a3cf' }) 
SET person_37e57681a3cf.name = 'Tommy Potter'
SET person_37e57681a3cf.gender = 'Male'
SET person_37e57681a3cf.country = 'US'
SET person_37e57681a3cf.allmusic = 'https://www.allmusic.com/artist/mn0000521303'
SET person_37e57681a3cf.discogs = 'https://www.discogs.com/artist/251780'
SET person_37e57681a3cf.viaf = 'http://viaf.org/viaf/27252849'
SET person_37e57681a3cf.wikidata = 'https://www.wikidata.org/wiki/Q1369941'
SET person_37e57681a3cf.wikipedia = 'https://en.wikipedia.org/wiki/Tommy_Potter'
SET person_37e57681a3cf.databases = ['http://id.loc.gov/authorities/names/n82003125', 'https://adp.library.ucsb.edu/names/338247', 'https://catalogue.bnf.fr/ark:/12148/cb13898624d', 'https://d-nb.info/gnd/134487702', 'http://snaccooperative.org/ark:/99166/w6fn2p47', 'https://www.worldcat.org/identities/lccn-n82003125']
SET person_37e57681a3cf.musicbrainz = 'https://musicbrainz.org/artist/7d606f44-a90c-4c1e-909d-37e57681a3cf'
SET person_37e57681a3cf.isni_list = ['http://isni.org/isni/000000011611270X']
SET person_37e57681a3cf.source = 'musicbrainz.org'


MERGE (person_596d83c907e5:Person{ uuid: '3f95b7c3-deba-4698-b12d-596d83c907e5' }) 
SET person_596d83c907e5.name = 'Al Haig'
SET person_596d83c907e5.gender = 'Male'
SET person_596d83c907e5.country = 'US'
SET person_596d83c907e5.allmusic = 'https://www.allmusic.com/artist/mn0000604469'
SET person_596d83c907e5.discogs = 'https://www.discogs.com/artist/259078'
SET person_596d83c907e5.viaf = 'http://viaf.org/viaf/34643332'
SET person_596d83c907e5.wikidata = 'https://www.wikidata.org/wiki/Q174161'
SET person_596d83c907e5.databases = ['http://id.loc.gov/authorities/names/n82165264', 'https://adp.library.ucsb.edu/names/319570', 'https://catalogue.bnf.fr/ark:/12148/cb138948887', 'https://d-nb.info/gnd/134395689', 'http://snaccooperative.org/ark:/99166/w6mg7wk8', 'https://www.worldcat.org/identities/lccn-n82165264']
SET person_596d83c907e5.musicbrainz = 'https://musicbrainz.org/artist/3f95b7c3-deba-4698-b12d-596d83c907e5'
SET person_596d83c907e5.isni_list = ['http://isni.org/isni/0000000055140001']
SET person_596d83c907e5.source = 'musicbrainz.org'

// labels

MERGE (label_0c68608d7321:Label{ uuid: '4fbbecbf-56e9-49db-a3bd-0c68608d7321' })
SET label_0c68608d7321.name= 'Debut'

// performances

MERGE (perf_134006931977:Performance{ uuid: '2f10934a-ac67-48d0-b10d-134006931977' })
SET perf_134006931977.name = 'I Didn\\'t Know What Time It Was'
SET perf_134006931977.duration = '2:37'
SET perf_134006931977.source = 'musicbrainz.org'


MERGE (perf_71572ced856d:Performance{ uuid: '3c1fdb97-380e-4f0c-a90f-71572ced856d' })
SET perf_71572ced856d.name = 'Ornithology'
SET perf_71572ced856d.duration = '3:29'
SET perf_71572ced856d.source = 'musicbrainz.org'


MERGE (perf_2180903ad5a2:Performance{ uuid: '294da0cf-0470-43f5-a006-2180903ad5a2' })
SET perf_2180903ad5a2.name = 'Scrapple From the Apple'
SET perf_2180903ad5a2.duration = '4:39'
SET perf_2180903ad5a2.source = 'musicbrainz.org'


MERGE (perf_8b40413c9e75:Performance{ uuid: 'b7df287f-6aad-4326-9834-8b40413c9e75' })
SET perf_8b40413c9e75.name = 'Embraceable You'
SET perf_8b40413c9e75.duration = '2:19'
SET perf_8b40413c9e75.source = 'musicbrainz.org'




// labels
MERGE (release_c184a79d9c78)-[:HAS_LABEL]->(label_0c68608d7321)


// tracks
MERGE (release_c184a79d9c78)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_134006931977)
MERGE (release_c184a79d9c78)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_71572ced856d)
MERGE (release_c184a79d9c78)-[:HAS_TRACK {name: 'B1', sequence: 3}]->(perf_2180903ad5a2)
MERGE (release_c184a79d9c78)-[:HAS_TRACK {name: 'B2', sequence: 4}]->(perf_8b40413c9e75)

// works

MERGE (person_322e34240ffc:Person{ uuid: '509086c2-9cc8-4e77-89e9-322e34240ffc' }) 
SET person_322e34240ffc.name = 'Ira Gershwin'
SET person_322e34240ffc.gender = 'Male'
SET person_322e34240ffc.country = 'US'
SET person_322e34240ffc.allmusic = 'https://www.allmusic.com/artist/mn0000200301'
SET person_322e34240ffc.discogs = 'https://www.discogs.com/artist/264105'
SET person_322e34240ffc.imdb = 'https://www.imdb.com/name/nm0314857/'
SET person_322e34240ffc.viaf = 'http://viaf.org/viaf/39519496'
SET person_322e34240ffc.wikidata = 'https://www.wikidata.org/wiki/Q61059'
SET person_322e34240ffc.databases = ['http://id.loc.gov/authorities/names/n50076010', 'https://adp.library.ucsb.edu/names/102148', 'https://catalogue.bnf.fr/ark:/12148/cb13194929s', 'https://d-nb.info/gnd/119500027', 'https://ibdb.com/person.php?id=6435', 'http://snaccooperative.org/ark:/99166/w60w94tm', 'https://nla.gov.au/nla.party-965252', 'https://openlibrary.org/works/OL233692A', 'https://rateyourmusic.com/artist/ira_gershwin', 'https://www.worldcat.org/identities/lccn-n50076010/']
SET person_322e34240ffc.musicbrainz = 'https://musicbrainz.org/artist/509086c2-9cc8-4e77-89e9-322e34240ffc'
SET person_322e34240ffc.isni_list = ['http://isni.org/isni/0000000108901469']
SET person_322e34240ffc.source = 'musicbrainz.org'


MERGE (person_acc0205f7513:Person{ uuid: '346448f5-25a0-4f78-bbd6-acc0205f7513' }) 
SET person_acc0205f7513.name = 'Richard Rodgers'
SET person_acc0205f7513.gender = 'Male'
SET person_acc0205f7513.disambiguation = 'composer'
SET person_acc0205f7513.country = 'US'
SET person_acc0205f7513.allmusic = 'https://www.allmusic.com/artist/mn0000820913'
SET person_acc0205f7513.bbc = 'https://www.bbc.co.uk/music/artists/346448f5-25a0-4f78-bbd6-acc0205f7513'
SET person_acc0205f7513.discogs = 'https://www.discogs.com/artist/255801'
SET person_acc0205f7513.imdb = 'https://www.imdb.com/name/nm0006256/'
SET person_acc0205f7513.viaf = 'http://viaf.org/viaf/113475079'
SET person_acc0205f7513.wikidata = 'https://www.wikidata.org/wiki/Q269094'
SET person_acc0205f7513.databases = ['http://id.loc.gov/authorities/names/n50048058', 'https://adp.library.ucsb.edu/names/102086', 'https://catalogue.bnf.fr/ark:/12148/cb13899099w', 'https://d-nb.info/gnd/118790862', 'https://ibdb.com/person.php?id=8323', 'http://snaccooperative.org/ark:/99166/w69h6cvt', 'https://nla.gov.au/nla.party-1015762', 'https://openlibrary.org/works/OL35365A', 'https://rateyourmusic.com/artist/richard_rodgers', 'https://www.worldcat.org/identities/lccn-n50048058/']
SET person_acc0205f7513.musicbrainz = 'https://musicbrainz.org/artist/346448f5-25a0-4f78-bbd6-acc0205f7513'
SET person_acc0205f7513.isni_list = ['http://isni.org/isni/0000000121482043']
SET person_acc0205f7513.source = 'musicbrainz.org'


MERGE (person_1904aa4268f4:Person{ uuid: '3fb75d97-5dfd-4e72-9aee-1904aa4268f4' }) 
SET person_1904aa4268f4.name = 'Lorenz Hart'
SET person_1904aa4268f4.gender = 'Male'
SET person_1904aa4268f4.country = 'US'
SET person_1904aa4268f4.allmusic = 'https://www.allmusic.com/artist/mn0000209620'
SET person_1904aa4268f4.discogs = 'https://www.discogs.com/artist/255800'
SET person_1904aa4268f4.imdb = 'https://www.imdb.com/name/nm0366414/'
SET person_1904aa4268f4.viaf = 'http://viaf.org/viaf/5122279'
SET person_1904aa4268f4.wikidata = 'https://www.wikidata.org/wiki/Q725828'
SET person_1904aa4268f4.databases = ['http://id.loc.gov/authorities/names/n81097890', 'https://adp.library.ucsb.edu/names/103285', 'https://catalogue.bnf.fr/ark:/12148/cb13939224g', 'https://d-nb.info/gnd/118720538', 'https://ibdb.com/Person/View/11244', 'http://snaccooperative.org/ark:/99166/w6x34z1s', 'https://nla.gov.au/nla.party-1266476', 'https://openlibrary.org/works/OL446542A', 'https://rateyourmusic.com/artist/lorenz_hart', 'https://www.worldcat.org/identities/lccn-n81097890/', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Lorenz&last=Hart&middle=']
SET person_1904aa4268f4.musicbrainz = 'https://musicbrainz.org/artist/3fb75d97-5dfd-4e72-9aee-1904aa4268f4'
SET person_1904aa4268f4.isni_list = ['http://isni.org/isni/0000000083526307']
SET person_1904aa4268f4.source = 'musicbrainz.org'


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
SET person_b693a808a158.databases = ['http://id.loc.gov/authorities/names/n79077265', 'https://adp.library.ucsb.edu/names/102427', 'https://catalogue.bnf.fr/ark:/12148/cb119493251', 'https://d-nb.info/gnd/118639226', 'https://ibdb.com/person.php?id=5813', 'http://snaccooperative.org/ark:/99166/w6x065dx', 'https://nla.gov.au/nla.party-832382', 'https://openlibrary.org/works/OL67761A', 'http://soundtrackcollector.com/composer/33/', 'https://rateyourmusic.com/artist/george_gershwin', 'https://www.worldcat.org/identities/lccn-n79077265']
SET person_b693a808a158.musicbrainz = 'https://musicbrainz.org/artist/65744963-191a-44ef-a3c7-b693a808a158'
SET person_b693a808a158.isni_list = ['http://isni.org/isni/0000000121355968']
SET person_b693a808a158.source = 'musicbrainz.org'


MERGE (person_a4cb6fbe4434:Person{ uuid: '57e1817c-4ff5-4079-9381-a4cb6fbe4434' }) 
SET person_a4cb6fbe4434.name = 'Benny Harris'
SET person_a4cb6fbe4434.gender = 'Male'
SET person_a4cb6fbe4434.country = 'US'
SET person_a4cb6fbe4434.allmusic = 'https://www.allmusic.com/artist/mn0000792654'
SET person_a4cb6fbe4434.discogs = 'https://www.discogs.com/artist/415785'
SET person_a4cb6fbe4434.viaf = 'http://viaf.org/viaf/56799353'
SET person_a4cb6fbe4434.wikidata = 'https://www.wikidata.org/wiki/Q818056'
SET person_a4cb6fbe4434.wikipedia = 'https://en.wikipedia.org/wiki/Benny_Harris'
SET person_a4cb6fbe4434.databases = ['http://id.loc.gov/authorities/names/no00031677', 'https://adp.library.ucsb.edu/names/320137', 'https://catalogue.bnf.fr/ark:/12148/cb13931543n', 'http://snaccooperative.org/ark:/99166/w65f1g1g', 'https://www.worldcat.org/identities/lccn-no00031677']
SET person_a4cb6fbe4434.musicbrainz = 'https://musicbrainz.org/artist/57e1817c-4ff5-4079-9381-a4cb6fbe4434'
SET person_a4cb6fbe4434.isni_list = ['http://isni.org/isni/0000000038894792']
SET person_a4cb6fbe4434.source = 'musicbrainz.org'


MERGE (work_0b9056143743:Work{ uuid: '17ffdc13-e578-38d6-8cc7-0b9056143743' })
SET work_0b9056143743.name = 'I Didn’t Know What Time It Was'
SET work_0b9056143743.iswc = 'T-070.902.666-3'
SET work_0b9056143743.type = 'Song'
SET work_0b9056143743.wikidata = 'https://www.wikidata.org/wiki/Q1606678'
SET work_0b9056143743.musicbrainz = 'https://musicbrainz.org/work/17ffdc13-e578-38d6-8cc7-0b9056143743'
SET work_0b9056143743.source = 'musicbrainz.org'


MERGE (work_a364c904a125:Work{ uuid: '858ebb4b-edd7-39ee-9120-a364c904a125' })
SET work_a364c904a125.name = 'Scrapple From the Apple'
SET work_a364c904a125.iswc = 'T-070.243.398-4'
SET work_a364c904a125.type = 'Song'
SET work_a364c904a125.source = 'musicbrainz.org'


MERGE (work_bc5765ec131f:Work{ uuid: '6c3b2860-0c5f-38fc-9e92-bc5765ec131f' })
SET work_bc5765ec131f.name = 'Ornithology'
SET work_bc5765ec131f.iswc = 'T-070.242.790-4'
SET work_bc5765ec131f.type = 'Song'
SET work_bc5765ec131f.musicbrainz = 'https://musicbrainz.org/work/6c3b2860-0c5f-38fc-9e92-bc5765ec131f'
SET work_bc5765ec131f.source = 'musicbrainz.org'


MERGE (work_7c0d2793d8d9:Work{ uuid: '13869248-f36a-3fe0-a8bd-7c0d2793d8d9' })
SET work_7c0d2793d8d9.name = 'Embraceable You'
SET work_7c0d2793d8d9.iswc = 'T-010.433.969-6'
SET work_7c0d2793d8d9.type = 'Song'
SET work_7c0d2793d8d9.tags = ['hard bop']
SET work_7c0d2793d8d9.wikidata = 'https://www.wikidata.org/wiki/Q753607'
SET work_7c0d2793d8d9.musicbrainz = 'https://musicbrainz.org/work/13869248-f36a-3fe0-a8bd-7c0d2793d8d9'
SET work_7c0d2793d8d9.source = 'musicbrainz.org'



// performances of
MERGE (perf_134006931977)-[:PERFORMANCE_OF]->(work_0b9056143743)
MERGE (perf_2180903ad5a2)-[:PERFORMANCE_OF]->(work_a364c904a125)
MERGE (perf_71572ced856d)-[:PERFORMANCE_OF]->(work_bc5765ec131f)
MERGE (perf_8b40413c9e75)-[:PERFORMANCE_OF]->(work_7c0d2793d8d9)


// composers
MERGE (person_acc0205f7513)-[:COMPOSED]->(work_0b9056143743)
MERGE (person_1904aa4268f4)-[:WROTE_LYRICS]->(work_0b9056143743)
MERGE (person_c73775716312)-[:COMPOSED]->(work_a364c904a125)
MERGE (person_a4cb6fbe4434)-[:COMPOSED]->(work_bc5765ec131f)
MERGE (person_c73775716312)-[:COMPOSED]->(work_bc5765ec131f)
MERGE (person_b693a808a158)-[:COMPOSED]->(work_7c0d2793d8d9)
MERGE (person_322e34240ffc)-[:WROTE_LYRICS]->(work_7c0d2793d8d9)

MERGE (person_596d83c907e5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_134006931977)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_134006931977)
MERGE (person_c73775716312)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_134006931977)
MERGE (person_37e57681a3cf)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_134006931977)
MERGE (person_181f6039f3dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_134006931977)
MERGE (person_596d83c907e5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_71572ced856d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_71572ced856d)
MERGE (person_c73775716312)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_71572ced856d)
MERGE (person_37e57681a3cf)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_71572ced856d)
MERGE (person_181f6039f3dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_71572ced856d)



"""
)