// releases

MERGE (release_0c1837fda612:Release{ uuid: 'b9ae21ad-f3c7-4f29-8c2e-0c1837fda612' })
SET release_0c1837fda612.name = 'Praise'
SET release_0c1837fda612.country = 'DE'
SET release_0c1837fda612.date = '2007-02-01'
SET release_0c1837fda612.format = 'Digital Media'
SET release_0c1837fda612.musicbrainz = 'http://musicbrainz.org/release/b9ae21ad-f3c7-4f29-8c2e-0c1837fda612'
SET release_0c1837fda612.source = 'musicbrainz.org'
SET release_0c1837fda612.timestamp = timestamp()

MERGE (person_c27e8aedbc62:Person{ uuid: '3ec80d72-073a-4985-9a91-c27e8aedbc62' }) 
SET person_c27e8aedbc62.name = 'Dwayne Burno'
SET person_c27e8aedbc62.gender = 'Male'
SET person_c27e8aedbc62.country = 'US'
SET person_c27e8aedbc62.allmusic = 'https://www.allmusic.com/artist/mn0000160529'
SET person_c27e8aedbc62.discogs = 'https://www.discogs.com/artist/346618'
SET person_c27e8aedbc62.imdb = 'https://www.imdb.com/name/nm0122550/'
SET person_c27e8aedbc62.viaf = 'http://viaf.org/viaf/12502212'
SET person_c27e8aedbc62.wikidata = 'https://www.wikidata.org/wiki/Q1268435'
SET person_c27e8aedbc62.databases = ['http://d-nb.info/gnd/134772865', 'http://id.loc.gov/authorities/names/no97068569', 'https://catalogue.bnf.fr/ark:/12148/cb14002491f', 'https://www.worldcat.org/identities/lccn-no97068569']
SET person_c27e8aedbc62.musicbrainz = 'https://musicbrainz.org/artist/3ec80d72-073a-4985-9a91-c27e8aedbc62'
SET person_c27e8aedbc62.isni_list = ['http://isni.org/isni/0000000083576144']
SET person_c27e8aedbc62.source = 'musicbrainz.org'
SET person_c27e8aedbc62.timestamp = timestamp()

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
SET person_6f0a331cc1ca.timestamp = timestamp()

MERGE (person_b84e43378390:Person{ uuid: '30b01f7e-2af1-4293-a52c-b84e43378390' }) 
SET person_b84e43378390.name = 'David Kikoski'
SET person_b84e43378390.gender = 'Male'
SET person_b84e43378390.country = 'US'
SET person_b84e43378390.allmusic = 'https://www.allmusic.com/artist/mn0000811141'
SET person_b84e43378390.discogs = 'https://www.discogs.com/artist/486649'
SET person_b84e43378390.viaf = 'http://viaf.org/viaf/233486283'
SET person_b84e43378390.wikidata = 'https://www.wikidata.org/wiki/Q1174978'
SET person_b84e43378390.wikipedia = 'https://en.wikipedia.org/wiki/David_Kikoski'
SET person_b84e43378390.databases = ['http://d-nb.info/gnd/134644328', 'http://id.loc.gov/authorities/names/n87142774', 'https://catalogue.bnf.fr/ark:/12148/cb139775835', 'https://www.worldcat.org/identities/lccn-n87142774']
SET person_b84e43378390.musicbrainz = 'https://musicbrainz.org/artist/30b01f7e-2af1-4293-a52c-b84e43378390'
SET person_b84e43378390.isni_list = ['http://isni.org/isni/0000000367948974']
SET person_b84e43378390.source = 'musicbrainz.org'
SET person_b84e43378390.timestamp = timestamp()

MERGE (person_786008422061:Person{ uuid: 'd72e6ce3-641f-46a4-b5a7-786008422061' }) 
SET person_786008422061.name = 'Kenny Garrett'
SET person_786008422061.gender = 'Male'
SET person_786008422061.country = 'US'
SET person_786008422061.allmusic = 'https://www.allmusic.com/artist/mn0000767404'
SET person_786008422061.discogs = 'https://www.discogs.com/artist/55729'
SET person_786008422061.viaf = 'http://viaf.org/viaf/24791747'
SET person_786008422061.wikidata = 'https://www.wikidata.org/wiki/Q711059'
SET person_786008422061.databases = ['http://d-nb.info/gnd/134717678', 'http://id.loc.gov/authorities/names/nr91029864', 'https://catalogue.bnf.fr/ark:/12148/cb139411981', 'https://www.worldcat.org/identities/lccn-nr91029864']
SET person_786008422061.musicbrainz = 'https://musicbrainz.org/artist/d72e6ce3-641f-46a4-b5a7-786008422061'
SET person_786008422061.isni_list = ['http://isni.org/isni/0000000081038051']
SET person_786008422061.source = 'musicbrainz.org'
SET person_786008422061.timestamp = timestamp()

MERGE (person_57b0d1da571e:Person{ uuid: 'e49fec41-3e7a-4447-8f78-57b0d1da571e' }) 
SET person_57b0d1da571e.name = 'A.T. Michael MacDonald'
SET person_57b0d1da571e.gender = 'Male'
SET person_57b0d1da571e.disambiguation = 'engineer'
SET person_57b0d1da571e.country = 'US'
SET person_57b0d1da571e.discogs = 'https://www.discogs.com/artist/889143'
SET person_57b0d1da571e.musicbrainz = 'https://musicbrainz.org/artist/e49fec41-3e7a-4447-8f78-57b0d1da571e'
SET person_57b0d1da571e.source = 'musicbrainz.org'
SET person_57b0d1da571e.timestamp = timestamp()

MERGE (person_ae8744b4801f:Person{ uuid: 'e75fbff2-9418-43bc-a958-ae8744b4801f' }) 
SET person_ae8744b4801f.name = 'François Zalacain'
SET person_ae8744b4801f.allmusic = 'https://www.allmusic.com/artist/mn0000185821'
SET person_ae8744b4801f.discogs = 'https://www.discogs.com/artist/1035067'
SET person_ae8744b4801f.wikidata = 'https://www.wikidata.org/wiki/Q3086076'
SET person_ae8744b4801f.wikipedia = 'https://en.wikipedia.org/wiki/Fran%C3%A7ois_Zalacain'
SET person_ae8744b4801f.musicbrainz = 'https://musicbrainz.org/artist/e75fbff2-9418-43bc-a958-ae8744b4801f'
SET person_ae8744b4801f.source = 'musicbrainz.org'
SET person_ae8744b4801f.timestamp = timestamp()

MERGE (person_688a5f4b38c5:Person{ uuid: 'ee616317-01ad-411b-964f-688a5f4b38c5' }) 
SET person_688a5f4b38c5.name = 'Graham Haynes'
SET person_688a5f4b38c5.gender = 'Male'
SET person_688a5f4b38c5.disambiguation = 'American cornetist, trumpeter and composer'
SET person_688a5f4b38c5.country = 'US'
SET person_688a5f4b38c5.allmusic = 'https://www.allmusic.com/artist/mn0000182288'
SET person_688a5f4b38c5.discogs = 'https://www.discogs.com/artist/70870'
SET person_688a5f4b38c5.viaf = 'http://viaf.org/viaf/69120491'
SET person_688a5f4b38c5.wikidata = 'https://www.wikidata.org/wiki/Q1541931'
SET person_688a5f4b38c5.wikipedia = 'https://en.wikipedia.org/wiki/Graham_Haynes'
SET person_688a5f4b38c5.databases = ['http://d-nb.info/gnd/134833651', 'http://id.loc.gov/authorities/names/n92070639', 'https://catalogue.bnf.fr/ark:/12148/cb13942842k', 'https://www.worldcat.org/identities/lccn-n92070639']
SET person_688a5f4b38c5.musicbrainz = 'https://musicbrainz.org/artist/ee616317-01ad-411b-964f-688a5f4b38c5'
SET person_688a5f4b38c5.isni_list = ['http://isni.org/isni/0000000083916479']
SET person_688a5f4b38c5.source = 'musicbrainz.org'
SET person_688a5f4b38c5.timestamp = timestamp()
// labels

MERGE (label_45a4aac43b37:Label{ uuid: 'd3698a68-ef9f-431e-93a0-45a4aac43b37' })
SET label_45a4aac43b37.name= 'Dreyfus Jazz'

// performances

MERGE (perf_ac49c44ff5ca:Performance{ uuid: '9b969b86-cf83-453e-acd5-ac49c44ff5ca' })
SET perf_ac49c44ff5ca.name = 'Mirror Mirror'
SET perf_ac49c44ff5ca.duration = '6:24'
SET perf_ac49c44ff5ca.begin = '1998-05-03'
SET perf_ac49c44ff5ca.end = '1998-05-05'
SET perf_ac49c44ff5ca.source = 'musicbrainz.org'
SET perf_ac49c44ff5ca.timestamp = timestamp()

MERGE (perf_df70063ef588:Performance{ uuid: '2aabb613-a577-4db8-a8dc-df70063ef588' })
SET perf_df70063ef588.name = 'After Sunrise'
SET perf_df70063ef588.duration = '7:19'
SET perf_df70063ef588.begin = '1998-05-03'
SET perf_df70063ef588.end = '1998-05-05'
SET perf_df70063ef588.source = 'musicbrainz.org'
SET perf_df70063ef588.timestamp = timestamp()

MERGE (perf_572d69872833:Performance{ uuid: '28e2109a-e408-435a-b63d-572d69872833' })
SET perf_572d69872833.name = 'Israel'
SET perf_572d69872833.duration = '5:41'
SET perf_572d69872833.begin = '1998-05-03'
SET perf_572d69872833.end = '1998-05-05'
SET perf_572d69872833.source = 'musicbrainz.org'
SET perf_572d69872833.timestamp = timestamp()

MERGE (perf_c98adb330be2:Performance{ uuid: 'c54b605e-281c-4310-8afb-c98adb330be2' })
SET perf_c98adb330be2.name = 'My Little Suede Shoes'
SET perf_c98adb330be2.duration = '5:46'
SET perf_c98adb330be2.begin = '1998-05-03'
SET perf_c98adb330be2.end = '1998-05-05'
SET perf_c98adb330be2.source = 'musicbrainz.org'
SET perf_c98adb330be2.timestamp = timestamp()

MERGE (perf_fa8674c89e2a:Performance{ uuid: 'cd81b731-b6a9-4732-837c-fa8674c89e2a' })
SET perf_fa8674c89e2a.name = 'The Touch of Your Lips'
SET perf_fa8674c89e2a.duration = '7:10'
SET perf_fa8674c89e2a.begin = '1998-05-03'
SET perf_fa8674c89e2a.end = '1998-05-05'
SET perf_fa8674c89e2a.source = 'musicbrainz.org'
SET perf_fa8674c89e2a.timestamp = timestamp()

MERGE (perf_39af0017ecf4:Performance{ uuid: '4224a8af-b734-47b2-98a3-39af0017ecf4' })
SET perf_39af0017ecf4.name = 'Inner Trust'
SET perf_39af0017ecf4.duration = '7:43'
SET perf_39af0017ecf4.begin = '1998-05-03'
SET perf_39af0017ecf4.end = '1998-05-05'
SET perf_39af0017ecf4.source = 'musicbrainz.org'
SET perf_39af0017ecf4.timestamp = timestamp()

MERGE (perf_41248edb681a:Performance{ uuid: '77a2e8bc-57f8-4ea1-be5d-41248edb681a' })
SET perf_41248edb681a.name = 'Morning Has Broken'
SET perf_41248edb681a.duration = '7:13'
SET perf_41248edb681a.begin = '1998-05-03'
SET perf_41248edb681a.end = '1998-05-05'
SET perf_41248edb681a.source = 'musicbrainz.org'
SET perf_41248edb681a.timestamp = timestamp()

MERGE (perf_d9e9f246af5f:Performance{ uuid: 'bda7c464-c085-40a0-bb19-d9e9f246af5f' })
SET perf_d9e9f246af5f.name = 'Blues on the Corner'
SET perf_d9e9f246af5f.duration = '8:36'
SET perf_d9e9f246af5f.begin = '1998-05-03'
SET perf_d9e9f246af5f.end = '1998-05-05'
SET perf_d9e9f246af5f.source = 'musicbrainz.org'
SET perf_d9e9f246af5f.timestamp = timestamp()

MERGE (perf_ad2f4078eea3:Performance{ uuid: '54324542-3486-4f28-9209-ad2f4078eea3' })
SET perf_ad2f4078eea3.name = 'Shades of Senegal'
SET perf_ad2f4078eea3.duration = '6:09'
SET perf_ad2f4078eea3.begin = '1998-05-03'
SET perf_ad2f4078eea3.end = '1998-05-05'
SET perf_ad2f4078eea3.source = 'musicbrainz.org'
SET perf_ad2f4078eea3.timestamp = timestamp()



// labels
MERGE (release_0c1837fda612)-[:HAS_LABEL]->(label_45a4aac43b37)


// tracks
MERGE (release_0c1837fda612)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_ac49c44ff5ca)
MERGE (release_0c1837fda612)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_df70063ef588)
MERGE (release_0c1837fda612)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_572d69872833)
MERGE (release_0c1837fda612)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_c98adb330be2)
MERGE (release_0c1837fda612)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_fa8674c89e2a)
MERGE (release_0c1837fda612)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_39af0017ecf4)
MERGE (release_0c1837fda612)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_41248edb681a)
MERGE (release_0c1837fda612)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_d9e9f246af5f)
MERGE (release_0c1837fda612)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_ad2f4078eea3)

// works

MERGE (person_e533299730a4:Person{ uuid: '01c28079-d190-4de1-bf82-e533299730a4' }) 
SET person_e533299730a4.name = 'John Carisi'
SET person_e533299730a4.gender = 'Male'
SET person_e533299730a4.country = 'US'
SET person_e533299730a4.allmusic = 'https://www.allmusic.com/artist/mn0000186708'
SET person_e533299730a4.discogs = 'https://www.discogs.com/artist/271036'
SET person_e533299730a4.viaf = 'http://viaf.org/viaf/24786635'
SET person_e533299730a4.wikidata = 'https://www.wikidata.org/wiki/Q1699545'
SET person_e533299730a4.wikipedia = 'https://en.wikipedia.org/wiki/John_Carisi'
SET person_e533299730a4.databases = ['http://d-nb.info/gnd/135399076', 'http://id.loc.gov/authorities/names/n91042369', 'https://catalogue.bnf.fr/ark:/12148/cb13892161s', 'http://snaccooperative.org/ark:/99166/w62z4cbn', 'https://www.worldcat.org/identities/lccn-n91042369']
SET person_e533299730a4.musicbrainz = 'https://musicbrainz.org/artist/01c28079-d190-4de1-bf82-e533299730a4'
SET person_e533299730a4.isni_list = ['http://isni.org/isni/0000000083655184']
SET person_e533299730a4.source = 'musicbrainz.org'
SET person_e533299730a4.timestamp = timestamp()

MERGE (person_c73775716312:Person{ uuid: 'c7356af9-9ea6-4a78-a55b-c73775716312' }) 
SET person_c73775716312.name = 'Charlie Parker'
SET person_c73775716312.gender = 'Male'
SET person_c73775716312.disambiguation = 'a.k.a. “Bird”, jazz alto saxophonist'
SET person_c73775716312.country = 'US'
SET person_c73775716312.allmusic = 'https://www.allmusic.com/artist/mn0000211758'
SET person_c73775716312.bbc = 'https://www.bbc.co.uk/music/artists/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.discogs = 'https://www.discogs.com/artist/75617'
SET person_c73775716312.imdb = 'https://www.imdb.com/name/nm0662127/'
SET person_c73775716312.viaf = 'http://viaf.org/viaf/10034216'
SET person_c73775716312.wikidata = 'https://www.wikidata.org/wiki/Q103767'
SET person_c73775716312.databases = ['http://d-nb.info/gnd/118739328', 'http://id.loc.gov/authorities/names/n50050327', 'https://catalogue.bnf.fr/ark:/12148/cb13898247z', 'http://snaccooperative.org/ark:/99166/w67086vq', 'https://nla.gov.au/nla.party-911160', 'https://openlibrary.org/works/OL4918032A', 'https://rateyourmusic.com/artist/charlie_parker', 'https://www.musik-sammler.de/artist/charlie-parker/', 'https://www.worldcat.org/identities/lccn-n50050327']
SET person_c73775716312.musicbrainz = 'https://musicbrainz.org/artist/c7356af9-9ea6-4a78-a55b-c73775716312'
SET person_c73775716312.isni_list = ['http://isni.org/isni/0000000120955806', 'http://isni.org/isni/0000000368633974']
SET person_c73775716312.source = 'musicbrainz.org'
SET person_c73775716312.timestamp = timestamp()

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
SET person_4e98168f002f.timestamp = timestamp()

MERGE (person_5a269b32b4c2:Person{ uuid: '8446fcca-109e-4c6d-a2ff-5a269b32b4c2' }) 
SET person_5a269b32b4c2.name = 'Chick Corea'
SET person_5a269b32b4c2.gender = 'Male'
SET person_5a269b32b4c2.disambiguation = 'jazz pianist'
SET person_5a269b32b4c2.country = 'US'
SET person_5a269b32b4c2.allmusic = 'https://www.allmusic.com/artist/mn0000110541'
SET person_5a269b32b4c2.discogs = 'https://www.discogs.com/artist/37731'
SET person_5a269b32b4c2.imdb = 'https://www.imdb.com/name/nm0179706/'
SET person_5a269b32b4c2.viaf = 'http://viaf.org/viaf/37337806'
SET person_5a269b32b4c2.wikidata = 'https://www.wikidata.org/wiki/Q192465'
SET person_5a269b32b4c2.databases = ['http://d-nb.info/gnd/119238489', 'http://id.loc.gov/authorities/names/n81080890', 'https://catalogue.bnf.fr/ark:/12148/cb13892744v', 'https://rateyourmusic.com/artist/chick_corea', 'https://www.worldcat.org/identities/lccn-n81080890']
SET person_5a269b32b4c2.musicbrainz = 'https://musicbrainz.org/artist/8446fcca-109e-4c6d-a2ff-5a269b32b4c2'
SET person_5a269b32b4c2.isni_list = ['http://isni.org/isni/0000000121285074']
SET person_5a269b32b4c2.source = 'musicbrainz.org'
SET person_5a269b32b4c2.timestamp = timestamp()

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
SET person_8971e7a2912e.databases = ['http://d-nb.info/gnd/134543734', 'http://id.loc.gov/authorities/names/n81058256', 'https://catalogue.bnf.fr/ark:/12148/cb139006254', 'http://snaccooperative.org/ark:/99166/w6183cz4', 'https://www.worldcat.org/identities/lccn-n81-058256']
SET person_8971e7a2912e.musicbrainz = 'https://musicbrainz.org/artist/22fe7b6f-af38-458e-87bd-8971e7a2912e'
SET person_8971e7a2912e.isni_list = ['http://isni.org/isni/0000000120184511']
SET person_8971e7a2912e.source = 'musicbrainz.org'
SET person_8971e7a2912e.timestamp = timestamp()

MERGE (person_1d2a7a1721c9:Person{ uuid: '86f1037c-4771-499b-80dc-1d2a7a1721c9' }) 
SET person_1d2a7a1721c9.name = 'Eleanor Farjeon'
SET person_1d2a7a1721c9.gender = 'Female'
SET person_1d2a7a1721c9.country = 'GB'
SET person_1d2a7a1721c9.discogs = 'https://www.discogs.com/artist/605772'
SET person_1d2a7a1721c9.imdb = 'https://www.imdb.com/name/nm1626467/'
SET person_1d2a7a1721c9.viaf = 'http://viaf.org/viaf/44768621'
SET person_1d2a7a1721c9.wikidata = 'https://www.wikidata.org/wiki/Q258669'
SET person_1d2a7a1721c9.databases = ['http://d-nb.info/gnd/105528773', 'https://catalogue.bnf.fr/ark:/12148/cb13082977s', 'https://openlibrary.org/works/OL32773A']
SET person_1d2a7a1721c9.musicbrainz = 'https://musicbrainz.org/artist/86f1037c-4771-499b-80dc-1d2a7a1721c9'
SET person_1d2a7a1721c9.isni_list = ['http://isni.org/isni/0000000107805336']
SET person_1d2a7a1721c9.source = 'musicbrainz.org'
SET person_1d2a7a1721c9.timestamp = timestamp()

MERGE (person_8d40b5dcbc41:Person{ uuid: '9be7f096-97ec-4615-8957-8d40b5dcbc41' }) 
SET person_8d40b5dcbc41.name = '[traditional]'
SET person_8d40b5dcbc41.gender = 'Not applicable'
SET person_8d40b5dcbc41.disambiguation = 'Special Purpose Artist'
SET person_8d40b5dcbc41.country = 'XW'
SET person_8d40b5dcbc41.allmusic = 'https://www.allmusic.com/artist/mn0000022266'
SET person_8d40b5dcbc41.discogs = 'https://www.discogs.com/artist/151641'
SET person_8d40b5dcbc41.discogs = 'https://www.discogs.com/artist/320156'
SET person_8d40b5dcbc41.wikidata = 'https://www.wikidata.org/wiki/Q235858'
SET person_8d40b5dcbc41.databases = ['https://rateyourmusic.com/artist/traditional', 'https://www.whosampled.com/Traditional-Folk/']
SET person_8d40b5dcbc41.musicbrainz = 'https://musicbrainz.org/artist/9be7f096-97ec-4615-8957-8d40b5dcbc41'
SET person_8d40b5dcbc41.source = 'musicbrainz.org'
SET person_8d40b5dcbc41.timestamp = timestamp()

MERGE (work_db56cfbc63ce:Work{ uuid: '89967e58-40f3-3580-a912-db56cfbc63ce' })
SET work_db56cfbc63ce.name = 'Israel'
SET work_db56cfbc63ce.iswc = 'T-070.241.208-5'
SET work_db56cfbc63ce.type = 'Song'
SET work_db56cfbc63ce.wikidata = 'https://www.wikidata.org/wiki/Q30601570'
SET work_db56cfbc63ce.musicbrainz = 'https://musicbrainz.org/work/89967e58-40f3-3580-a912-db56cfbc63ce'
SET work_db56cfbc63ce.source = 'musicbrainz.org'
SET work_db56cfbc63ce.timestamp = timestamp()

MERGE (work_e6867964d6dd:Work{ uuid: '0c7363b4-97f4-37b3-981c-e6867964d6dd' })
SET work_e6867964d6dd.name = 'The Touch of Your Lips'
SET work_e6867964d6dd.iswc = 'T-010.433.970-9'
SET work_e6867964d6dd.type = 'Song'
SET work_e6867964d6dd.musicbrainz = 'https://musicbrainz.org/work/0c7363b4-97f4-37b3-981c-e6867964d6dd'
SET work_e6867964d6dd.source = 'musicbrainz.org'
SET work_e6867964d6dd.timestamp = timestamp()

MERGE (work_d7565be7f6ff:Work{ uuid: '56ff47de-1cb3-3417-b663-d7565be7f6ff' })
SET work_d7565be7f6ff.name = 'My Little Suede Shoes'
SET work_d7565be7f6ff.iswc = 'T-070.241.759-1'
SET work_d7565be7f6ff.type = 'Song'
SET work_d7565be7f6ff.source = 'musicbrainz.org'
SET work_d7565be7f6ff.timestamp = timestamp()

MERGE (work_82ac673cb60b:Work{ uuid: '0ccc7a8f-cd57-4792-a7aa-82ac673cb60b' })
SET work_82ac673cb60b.name = 'Mirror, Mirror'
SET work_82ac673cb60b.type = 'Song'
SET work_82ac673cb60b.source = 'musicbrainz.org'
SET work_82ac673cb60b.timestamp = timestamp()

MERGE (work_16a8bde9d64b:Work{ uuid: '993aff2b-235f-36d9-94ed-16a8bde9d64b' })
SET work_16a8bde9d64b.name = 'Morning Has Broken'
SET work_16a8bde9d64b.iswc = 'T-011.231.892-9'
SET work_16a8bde9d64b.type = 'Song'
SET work_16a8bde9d64b.wikidata = 'https://www.wikidata.org/wiki/Q1948304'
SET work_16a8bde9d64b.databases = ['https://www.whosampled.com/Cat-Stevens/Morning-Has-Broken']
SET work_16a8bde9d64b.musicbrainz = 'https://musicbrainz.org/work/993aff2b-235f-36d9-94ed-16a8bde9d64b'
SET work_16a8bde9d64b.source = 'musicbrainz.org'
SET work_16a8bde9d64b.timestamp = timestamp()

MERGE (work_31d339ec564f:Work{ uuid: 'b3e92b2a-bcd5-4218-af68-31d339ec564f' })
SET work_31d339ec564f.name = 'Blues on the Corner'
SET work_31d339ec564f.type = 'Song'
SET work_31d339ec564f.source = 'musicbrainz.org'
SET work_31d339ec564f.timestamp = timestamp()


// performances of
MERGE (perf_572d69872833)-[:PERFORMANCE_OF]->(work_db56cfbc63ce)
MERGE (perf_fa8674c89e2a)-[:PERFORMANCE_OF]->(work_e6867964d6dd)
MERGE (perf_c98adb330be2)-[:PERFORMANCE_OF]->(work_d7565be7f6ff)
MERGE (perf_ac49c44ff5ca)-[:PERFORMANCE_OF]->(work_82ac673cb60b)
MERGE (perf_41248edb681a)-[:PERFORMANCE_OF]->(work_16a8bde9d64b)
MERGE (perf_d9e9f246af5f)-[:PERFORMANCE_OF]->(work_31d339ec564f)


// composers
MERGE (person_e533299730a4)-[:COMPOSED]->(work_db56cfbc63ce)
MERGE (person_4e98168f002f)-[:COMPOSED]->(work_e6867964d6dd)
MERGE (person_4e98168f002f)-[:WROTE_LYRICS]->(work_e6867964d6dd)
MERGE (person_c73775716312)-[:COMPOSED]->(work_d7565be7f6ff)
MERGE (person_5a269b32b4c2)-[:COMPOSED]->(work_82ac673cb60b)
MERGE (person_8d40b5dcbc41)-[:COMPOSED]->(work_16a8bde9d64b)
MERGE (person_1d2a7a1721c9)-[:WROTE_LYRICS]->(work_16a8bde9d64b)
MERGE (person_8971e7a2912e)-[:COMPOSED]->(work_31d339ec564f)


// place nodes

MERGE (place_70b236d3aa47:Place{ uuid: 'f1526c4b-b38e-42e5-897e-70b236d3aa47' })
SET place_70b236d3aa47.name = 'Systems Two Recording Studio'
SET place_70b236d3aa47.source = 'musicbrainz.org'


// place relationships
MERGE (perf_ac49c44ff5ca)-[:HAS_PLACE { type: 'recorded at', begin: '1998-05-03', end: '1998-05-05' }]->(place_70b236d3aa47)
MERGE (perf_df70063ef588)-[:HAS_PLACE { type: 'recorded at', begin: '1998-05-03', end: '1998-05-05' }]->(place_70b236d3aa47)
MERGE (perf_572d69872833)-[:HAS_PLACE { type: 'recorded at', begin: '1998-05-03', end: '1998-05-05' }]->(place_70b236d3aa47)
MERGE (perf_c98adb330be2)-[:HAS_PLACE { type: 'recorded at', begin: '1998-05-03', end: '1998-05-05' }]->(place_70b236d3aa47)
MERGE (perf_fa8674c89e2a)-[:HAS_PLACE { type: 'recorded at', begin: '1998-05-03', end: '1998-05-05' }]->(place_70b236d3aa47)
MERGE (perf_39af0017ecf4)-[:HAS_PLACE { type: 'recorded at', begin: '1998-05-03', end: '1998-05-05' }]->(place_70b236d3aa47)
MERGE (perf_41248edb681a)-[:HAS_PLACE { type: 'recorded at', begin: '1998-05-03', end: '1998-05-05' }]->(place_70b236d3aa47)
MERGE (perf_d9e9f246af5f)-[:HAS_PLACE { type: 'recorded at', begin: '1998-05-03', end: '1998-05-05' }]->(place_70b236d3aa47)
MERGE (perf_ad2f4078eea3)-[:HAS_PLACE { type: 'recorded at', begin: '1998-05-03', end: '1998-05-05' }]->(place_70b236d3aa47)

MERGE (person_c27e8aedbc62)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_ac49c44ff5ca)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_ac49c44ff5ca)
MERGE (person_688a5f4b38c5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_ac49c44ff5ca)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_ac49c44ff5ca)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ac49c44ff5ca)
MERGE (person_ae8744b4801f)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_ac49c44ff5ca)
MERGE (person_c27e8aedbc62)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_df70063ef588)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_df70063ef588)
MERGE (person_688a5f4b38c5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_df70063ef588)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_df70063ef588)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_df70063ef588)
MERGE (person_ae8744b4801f)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_df70063ef588)
MERGE (person_c27e8aedbc62)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_572d69872833)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_572d69872833)
MERGE (person_688a5f4b38c5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_572d69872833)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_572d69872833)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_572d69872833)
MERGE (person_ae8744b4801f)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_572d69872833)
MERGE (person_c27e8aedbc62)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_c98adb330be2)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_c98adb330be2)
MERGE (person_688a5f4b38c5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_c98adb330be2)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_c98adb330be2)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_c98adb330be2)
MERGE (person_ae8744b4801f)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_c98adb330be2)
MERGE (person_c27e8aedbc62)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_fa8674c89e2a)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_fa8674c89e2a)
MERGE (person_688a5f4b38c5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_fa8674c89e2a)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_fa8674c89e2a)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_fa8674c89e2a)
MERGE (person_ae8744b4801f)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_fa8674c89e2a)
MERGE (person_c27e8aedbc62)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_39af0017ecf4)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_39af0017ecf4)
MERGE (person_688a5f4b38c5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_39af0017ecf4)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_39af0017ecf4)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_39af0017ecf4)
MERGE (person_ae8744b4801f)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_39af0017ecf4)
MERGE (person_c27e8aedbc62)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_41248edb681a)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_41248edb681a)
MERGE (person_688a5f4b38c5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_41248edb681a)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_41248edb681a)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_41248edb681a)
MERGE (person_ae8744b4801f)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_41248edb681a)
MERGE (person_c27e8aedbc62)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_d9e9f246af5f)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_d9e9f246af5f)
MERGE (person_688a5f4b38c5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_d9e9f246af5f)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_d9e9f246af5f)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d9e9f246af5f)
MERGE (person_ae8744b4801f)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_d9e9f246af5f)
MERGE (person_c27e8aedbc62)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_ad2f4078eea3)
MERGE (person_786008422061)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_ad2f4078eea3)
MERGE (person_688a5f4b38c5)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['brass'] }]->(perf_ad2f4078eea3)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_ad2f4078eea3)
MERGE (person_b84e43378390)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ad2f4078eea3)
MERGE (person_ae8744b4801f)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_ad2f4078eea3)

