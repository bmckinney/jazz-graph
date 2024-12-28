
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_d61113ae5e78:Release{ uuid: 'd0b0bb40-521f-4aac-8c1b-d61113ae5e78' })
SET release_d61113ae5e78.name = 'In the Land of Hi-Fi'
SET release_d61113ae5e78.country = 'US'
SET release_d61113ae5e78.date = '1955'
SET release_d61113ae5e78.format = '12" Vinyl'
SET release_d61113ae5e78.discode = 'MG 36058'
SET release_d61113ae5e78.discogs = 'https://www.discogs.com/release/3643471'
SET release_d61113ae5e78.musicbrainz = 'http://musicbrainz.org/release/d0b0bb40-521f-4aac-8c1b-d61113ae5e78'
SET release_d61113ae5e78.source = 'musicbrainz.org'


MERGE (person_8bc88dfd8774:Person{ uuid: '19eea818-34bd-4250-ba77-8bc88dfd8774' }) 
SET person_8bc88dfd8774.name = 'Sam Marowitz'
SET person_8bc88dfd8774.gender = 'Male'
SET person_8bc88dfd8774.disambiguation = 'saxophonist and clarinetist'
SET person_8bc88dfd8774.country = 'US'
SET person_8bc88dfd8774.discogs = 'https://www.discogs.com/artist/312540'
SET person_8bc88dfd8774.wikidata = 'https://www.wikidata.org/wiki/Q42148151'
SET person_8bc88dfd8774.musicbrainz = 'https://musicbrainz.org/artist/19eea818-34bd-4250-ba77-8bc88dfd8774'
SET person_8bc88dfd8774.source = 'musicbrainz.org'


MERGE (person_beee70c5e271:Person{ uuid: 'd0fd2d09-eda7-45e2-b7da-beee70c5e271' }) 
SET person_beee70c5e271.name = 'Jimmy Jones'
SET person_beee70c5e271.gender = 'Male'
SET person_beee70c5e271.disambiguation = 'jazz pianist, active years 1936-1975'
SET person_beee70c5e271.country = 'US'
SET person_beee70c5e271.discogs = 'https://www.discogs.com/artist/307373'
SET person_beee70c5e271.viaf = 'http://viaf.org/viaf/100229577'
SET person_beee70c5e271.wikidata = 'https://www.wikidata.org/wiki/Q122966'
SET person_beee70c5e271.wikipedia = 'https://en.wikipedia.org/wiki/Jimmy_Jones_(pianist)'
SET person_beee70c5e271.databases = ['http://d-nb.info/gnd/135370728', 'http://id.loc.gov/authorities/names/n91084904', 'https://catalogue.bnf.fr/ark:/12148/cb13895730w', 'http://snaccooperative.org/ark:/99166/w60k29ks', 'https://www.worldcat.org/identities/lccn-n91084904']
SET person_beee70c5e271.musicbrainz = 'https://musicbrainz.org/artist/d0fd2d09-eda7-45e2-b7da-beee70c5e271'
SET person_beee70c5e271.isni_list = ['http://isni.org/isni/0000000115574603']
SET person_beee70c5e271.source = 'musicbrainz.org'


MERGE (person_07569e15f3fa:Person{ uuid: '15c1d7c1-32e3-4356-8f44-07569e15f3fa' }) 
SET person_07569e15f3fa.name = 'Ernie Wilkins'
SET person_07569e15f3fa.gender = 'Male'
SET person_07569e15f3fa.country = 'US'
SET person_07569e15f3fa.allmusic = 'https://www.allmusic.com/artist/mn0000205130'
SET person_07569e15f3fa.discogs = 'https://www.discogs.com/artist/282003'
SET person_07569e15f3fa.viaf = 'http://viaf.org/viaf/100232872'
SET person_07569e15f3fa.wikidata = 'https://www.wikidata.org/wiki/Q326634'
SET person_07569e15f3fa.databases = ['http://d-nb.info/gnd/134580621', 'http://id.loc.gov/authorities/names/n88629938', 'https://catalogue.bnf.fr/ark:/12148/cb13901164w', 'http://snaccooperative.org/ark:/99166/w6x37289', 'https://www.worldcat.org/identities/lccn-n88629938']
SET person_07569e15f3fa.musicbrainz = 'https://musicbrainz.org/artist/15c1d7c1-32e3-4356-8f44-07569e15f3fa'
SET person_07569e15f3fa.isni_list = ['http://isni.org/isni/0000000116917495']
SET person_07569e15f3fa.source = 'musicbrainz.org'


MERGE (person_644bd536ec07:Person{ uuid: '33e50556-d4be-421b-a5d1-644bd536ec07' }) 
SET person_644bd536ec07.name = 'J.J. Johnson'
SET person_644bd536ec07.gender = 'Male'
SET person_644bd536ec07.disambiguation = 'Jazz/bop trombonist/session leader'
SET person_644bd536ec07.country = 'US'
SET person_644bd536ec07.allmusic = 'https://www.allmusic.com/artist/mn0000119111'
SET person_644bd536ec07.discogs = 'https://www.discogs.com/artist/251778'
SET person_644bd536ec07.imdb = 'https://www.imdb.com/name/nm0425266/'
SET person_644bd536ec07.viaf = 'http://viaf.org/viaf/9137149296258380670007'
SET person_644bd536ec07.wikidata = 'https://www.wikidata.org/wiki/Q504915'
SET person_644bd536ec07.databases = ['http://d-nb.info/gnd/122060989', 'http://id.loc.gov/authorities/names/n84011598', 'https://catalogue.bnf.fr/ark:/12148/cb138956805', 'http://snaccooperative.org/ark:/99166/w6m332cb', 'https://www.worldcat.org/identities/lccn-n84011598']
SET person_644bd536ec07.musicbrainz = 'https://musicbrainz.org/artist/33e50556-d4be-421b-a5d1-644bd536ec07'
SET person_644bd536ec07.isni_list = ['http://isni.org/isni/0000000458907318']
SET person_644bd536ec07.source = 'musicbrainz.org'


MERGE (person_0933d6c60091:Person{ uuid: '87749622-f3b7-42f6-99f3-0933d6c60091' }) 
SET person_0933d6c60091.name = 'Bernie Glow'
SET person_0933d6c60091.gender = 'Male'
SET person_0933d6c60091.country = 'US'
SET person_0933d6c60091.allmusic = 'https://www.allmusic.com/artist/mn0000759837'
SET person_0933d6c60091.discogs = 'https://www.discogs.com/artist/271022'
SET person_0933d6c60091.viaf = 'http://viaf.org/viaf/34645081'
SET person_0933d6c60091.wikidata = 'https://www.wikidata.org/wiki/Q826556'
SET person_0933d6c60091.databases = ['http://d-nb.info/gnd/134759346', 'http://id.loc.gov/authorities/names/n92048616', 'https://catalogue.bnf.fr/ark:/12148/cb13921711c', 'http://snaccooperative.org/ark:/99166/w6zf1wx7', 'https://rateyourmusic.com/artist/bernie_glow', 'https://www.worldcat.org/identities/lccn-n92048616']
SET person_0933d6c60091.musicbrainz = 'https://musicbrainz.org/artist/87749622-f3b7-42f6-99f3-0933d6c60091'
SET person_0933d6c60091.isni_list = ['http://isni.org/isni/0000000055140167']
SET person_0933d6c60091.source = 'musicbrainz.org'


MERGE (person_43ac1e7a092c:Person{ uuid: '17e2ae06-6200-476c-b904-43ac1e7a092c' }) 
SET person_43ac1e7a092c.name = 'Jerome Richardson'
SET person_43ac1e7a092c.gender = 'Male'
SET person_43ac1e7a092c.country = 'US'
SET person_43ac1e7a092c.allmusic = 'https://www.allmusic.com/artist/mn0000273205'
SET person_43ac1e7a092c.discogs = 'https://www.discogs.com/artist/72480'
SET person_43ac1e7a092c.viaf = 'http://viaf.org/viaf/42026472'
SET person_43ac1e7a092c.wikidata = 'https://www.wikidata.org/wiki/Q720693'
SET person_43ac1e7a092c.wikipedia = 'https://en.wikipedia.org/wiki/Jerome_Richardson'
SET person_43ac1e7a092c.databases = ['http://d-nb.info/gnd/134496787', 'http://id.loc.gov/authorities/names/n83189459', 'https://catalogue.bnf.fr/ark:/12148/cb13898983r', 'https://www.worldcat.org/identities/lccn-n83189459']
SET person_43ac1e7a092c.musicbrainz = 'https://musicbrainz.org/artist/17e2ae06-6200-476c-b904-43ac1e7a092c'
SET person_43ac1e7a092c.isni_list = ['http://isni.org/isni/0000000063021168']
SET person_43ac1e7a092c.source = 'musicbrainz.org'


MERGE (person_2fe1f9f27da8:Person{ uuid: 'a4c73ebe-b2c7-4f13-b99d-2fe1f9f27da8' }) 
SET person_2fe1f9f27da8.name = 'Cannonball Adderley'
SET person_2fe1f9f27da8.gender = 'Male'
SET person_2fe1f9f27da8.country = 'US'
SET person_2fe1f9f27da8.allmusic = 'https://www.allmusic.com/artist/mn0000548338'
SET person_2fe1f9f27da8.discogs = 'https://www.discogs.com/artist/61585'
SET person_2fe1f9f27da8.imdb = 'https://www.imdb.com/name/nm0011645/'
SET person_2fe1f9f27da8.viaf = 'http://viaf.org/viaf/36906016'
SET person_2fe1f9f27da8.wikidata = 'https://www.wikidata.org/wiki/Q110477'
SET person_2fe1f9f27da8.databases = ['http://d-nb.info/gnd/122466616', 'http://id.loc.gov/authorities/names/n84163049', 'https://catalogue.bnf.fr/ark:/12148/cb138905900', 'http://snaccooperative.org/ark:/99166/w65q52jh', 'https://rateyourmusic.com/artist/cannonball_adderley', 'https://www.worldcat.org/identities/lccn-n84163049']
SET person_2fe1f9f27da8.musicbrainz = 'https://musicbrainz.org/artist/a4c73ebe-b2c7-4f13-b99d-2fe1f9f27da8'
SET person_2fe1f9f27da8.isni_list = ['http://isni.org/isni/000000011566991X']
SET person_2fe1f9f27da8.source = 'musicbrainz.org'


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


MERGE (person_8f221f658ef3:Person{ uuid: '7ec27748-5886-464d-8e65-8f221f658ef3' }) 
SET person_8f221f658ef3.name = 'Joe Benjamin'
SET person_8f221f658ef3.gender = 'Male'
SET person_8f221f658ef3.disambiguation = 'US jazz bassist'
SET person_8f221f658ef3.country = 'US'
SET person_8f221f658ef3.allmusic = 'https://www.allmusic.com/artist/mn0000140366'
SET person_8f221f658ef3.discogs = 'https://www.discogs.com/artist/254975'
SET person_8f221f658ef3.viaf = 'http://viaf.org/viaf/85790625'
SET person_8f221f658ef3.wikidata = 'https://www.wikidata.org/wiki/Q39016'
SET person_8f221f658ef3.databases = ['http://d-nb.info/gnd/134326059', 'http://id.loc.gov/authorities/names/n80144178', 'https://catalogue.bnf.fr/ark:/12148/cb138913497', 'https://www.worldcat.org/identities/lccn-n80144178']
SET person_8f221f658ef3.musicbrainz = 'https://musicbrainz.org/artist/7ec27748-5886-464d-8e65-8f221f658ef3'
SET person_8f221f658ef3.isni_list = ['http://isni.org/isni/0000000076900778']
SET person_8f221f658ef3.source = 'musicbrainz.org'


MERGE (person_db21a63f19d9:Person{ uuid: 'e3443955-8d71-4b63-b886-db21a63f19d9' }) 
SET person_db21a63f19d9.name = 'Turk Van Lake'
SET person_db21a63f19d9.gender = 'Male'
SET person_db21a63f19d9.country = 'US'
SET person_db21a63f19d9.allmusic = 'https://www.allmusic.com/artist/mn0000205891'
SET person_db21a63f19d9.discogs = 'https://www.discogs.com/artist/616575'
SET person_db21a63f19d9.viaf = 'http://viaf.org/viaf/73400417'
SET person_db21a63f19d9.wikidata = 'https://www.wikidata.org/wiki/Q1420294'
SET person_db21a63f19d9.databases = ['http://id.loc.gov/authorities/names/no00065693', 'https://catalogue.bnf.fr/ark:/12148/cb139403610', 'http://snaccooperative.org/ark:/99166/w6fp3wtd', 'https://www.worldcat.org/identities/lccn-no00065693']
SET person_db21a63f19d9.musicbrainz = 'https://musicbrainz.org/artist/e3443955-8d71-4b63-b886-db21a63f19d9'
SET person_db21a63f19d9.isni_list = ['http://isni.org/isni/0000000373987099']
SET person_db21a63f19d9.source = 'musicbrainz.org'


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


MERGE (person_6be25a4576a2:Person{ uuid: '479df49c-0a3e-4f61-a726-6be25a4576a2' }) 
SET person_6be25a4576a2.name = 'Ernie Royal'
SET person_6be25a4576a2.gender = 'Male'
SET person_6be25a4576a2.country = 'US'
SET person_6be25a4576a2.allmusic = 'https://www.allmusic.com/artist/mn0000805560'
SET person_6be25a4576a2.discogs = 'https://www.discogs.com/artist/271027'
SET person_6be25a4576a2.viaf = 'http://viaf.org/viaf/54333694'
SET person_6be25a4576a2.wikidata = 'https://www.wikidata.org/wiki/Q491422'
SET person_6be25a4576a2.databases = ['http://d-nb.info/gnd/134503406', 'http://id.loc.gov/authorities/names/n80097147', 'https://catalogue.bnf.fr/ark:/12148/cb138992476', 'http://snaccooperative.org/ark:/99166/w6892p1w', 'https://www.worldcat.org/identities/lccn-n80097147']
SET person_6be25a4576a2.musicbrainz = 'https://musicbrainz.org/artist/479df49c-0a3e-4f61-a726-6be25a4576a2'
SET person_6be25a4576a2.isni_list = ['http://isni.org/isni/0000000059444598']
SET person_6be25a4576a2.source = 'musicbrainz.org'


MERGE (person_f42ad7cebf1e:Person{ uuid: 'd9566c72-7ad1-410f-9f26-f42ad7cebf1e' }) 
SET person_f42ad7cebf1e.name = 'Kai Winding'
SET person_f42ad7cebf1e.gender = 'Male'
SET person_f42ad7cebf1e.country = 'US'
SET person_f42ad7cebf1e.allmusic = 'https://www.allmusic.com/artist/mn0000352164'
SET person_f42ad7cebf1e.discogs = 'https://www.discogs.com/artist/267186'
SET person_f42ad7cebf1e.imdb = 'https://www.imdb.com/name/nm0934718/'
SET person_f42ad7cebf1e.viaf = 'http://viaf.org/viaf/50436655'
SET person_f42ad7cebf1e.wikidata = 'https://www.wikidata.org/wiki/Q494976'
SET person_f42ad7cebf1e.databases = ['http://d-nb.info/gnd/13417237X', 'http://id.loc.gov/authorities/names/n84132592', 'https://catalogue.bnf.fr/ark:/12148/cb13901236x', 'http://snaccooperative.org/ark:/99166/w6gb29dg', 'https://rateyourmusic.com/artist/kai_winding', 'https://www.worldcat.org/identities/lccn-n84132592']
SET person_f42ad7cebf1e.musicbrainz = 'https://musicbrainz.org/artist/d9566c72-7ad1-410f-9f26-f42ad7cebf1e'
SET person_f42ad7cebf1e.isni_list = ['http://isni.org/isni/0000000080159265']
SET person_f42ad7cebf1e.source = 'musicbrainz.org'

// labels

MERGE (label_42366b3be8c9:Label{ uuid: 'e023c53a-7e9b-4f7d-99ff-42366b3be8c9' })
SET label_42366b3be8c9.name= 'EmArcy'

// performances

MERGE (perf_f8b570a1808d:Performance{ uuid: 'fc0ad9a5-fe86-4934-ac5f-f8b570a1808d' })
SET perf_f8b570a1808d.name = 'Over the Rainbow'
SET perf_f8b570a1808d.disambiguation = 'original LP mono mix'
SET perf_f8b570a1808d.duration = '3:30'
SET perf_f8b570a1808d.begin_date = '1955-10-27'
SET perf_f8b570a1808d.end_date = '1955-10-27'
SET perf_f8b570a1808d.source = 'musicbrainz.org'


MERGE (perf_f6a38101a1a9:Performance{ uuid: '03e5a9f4-9da9-4ab9-a6f6-f6a38101a1a9' })
SET perf_f6a38101a1a9.name = 'Soon'
SET perf_f6a38101a1a9.disambiguation = 'original LP mono mix'
SET perf_f6a38101a1a9.duration = '2:36'
SET perf_f6a38101a1a9.begin_date = '1955-10-26'
SET perf_f6a38101a1a9.end_date = '1955-10-26'
SET perf_f6a38101a1a9.source = 'musicbrainz.org'


MERGE (perf_39236758e7f6:Performance{ uuid: 'e7887cb9-3758-4b42-9d53-39236758e7f6' })
SET perf_39236758e7f6.name = 'Cherokee'
SET perf_39236758e7f6.disambiguation = 'original LP mono mix'
SET perf_39236758e7f6.duration = '2:32'
SET perf_39236758e7f6.begin_date = '1955-10-26'
SET perf_39236758e7f6.end_date = '1955-10-26'
SET perf_39236758e7f6.source = 'musicbrainz.org'


MERGE (perf_ee1a4ca8b456:Performance{ uuid: '4df2bac8-d537-4fc3-a78e-ee1a4ca8b456' })
SET perf_ee1a4ca8b456.name = 'I’ll Never Smile Again'
SET perf_ee1a4ca8b456.disambiguation = 'original LP mono mix'
SET perf_ee1a4ca8b456.duration = '2:35'
SET perf_ee1a4ca8b456.begin_date = '1955-10-25'
SET perf_ee1a4ca8b456.end_date = '1955-10-25'
SET perf_ee1a4ca8b456.source = 'musicbrainz.org'


MERGE (perf_26f94da10eb4:Performance{ uuid: '6f073c03-f1f1-49b9-8fcb-26f94da10eb4' })
SET perf_26f94da10eb4.name = 'Don’t Be on the Outside'
SET perf_26f94da10eb4.disambiguation = 'original LP mono mix'
SET perf_26f94da10eb4.duration = '3:01'
SET perf_26f94da10eb4.begin_date = '1955-10-25'
SET perf_26f94da10eb4.end_date = '1955-10-25'
SET perf_26f94da10eb4.source = 'musicbrainz.org'


MERGE (perf_2c9607075f35:Performance{ uuid: '944bede1-e003-4b32-b100-2c9607075f35' })
SET perf_2c9607075f35.name = 'How High the Moon'
SET perf_2c9607075f35.disambiguation = 'original LP mono mix'
SET perf_2c9607075f35.duration = '2:37'
SET perf_2c9607075f35.begin_date = '1955-10-27'
SET perf_2c9607075f35.end_date = '1955-10-27'
SET perf_2c9607075f35.source = 'musicbrainz.org'


MERGE (perf_8ba4ce1e86af:Performance{ uuid: '566f61b6-a2ed-4979-8b8b-8ba4ce1e86af' })
SET perf_8ba4ce1e86af.name = 'It Shouldn’t Happen to a Dream'
SET perf_8ba4ce1e86af.disambiguation = 'original LP mono mix'
SET perf_8ba4ce1e86af.duration = '3:20'
SET perf_8ba4ce1e86af.begin_date = '1955-10-25'
SET perf_8ba4ce1e86af.end_date = '1955-10-25'
SET perf_8ba4ce1e86af.source = 'musicbrainz.org'


MERGE (perf_8cf574bd4653:Performance{ uuid: '514c5843-7673-466b-a06a-8cf574bd4653' })
SET perf_8cf574bd4653.name = 'Sometimes I’m Happy'
SET perf_8cf574bd4653.disambiguation = 'original LP mono mix'
SET perf_8cf574bd4653.duration = '2:56'
SET perf_8cf574bd4653.begin_date = '1955-10-25'
SET perf_8cf574bd4653.end_date = '1955-10-25'
SET perf_8cf574bd4653.source = 'musicbrainz.org'


MERGE (perf_514225818c11:Performance{ uuid: '36c8b970-a060-4bd2-a467-514225818c11' })
SET perf_514225818c11.name = 'Maybe'
SET perf_514225818c11.disambiguation = 'original LP mono mix'
SET perf_514225818c11.duration = '2:34'
SET perf_514225818c11.begin_date = '1955-10-26'
SET perf_514225818c11.end_date = '1955-10-26'
SET perf_514225818c11.source = 'musicbrainz.org'


MERGE (perf_128d0f309697:Performance{ uuid: '1dfa0d8e-caf5-4761-ad4a-128d0f309697' })
SET perf_128d0f309697.name = 'An Occasional Man'
SET perf_128d0f309697.disambiguation = 'original LP mono mix'
SET perf_128d0f309697.duration = '2:32'
SET perf_128d0f309697.begin_date = '1955-10-26'
SET perf_128d0f309697.end_date = '1955-10-26'
SET perf_128d0f309697.source = 'musicbrainz.org'


MERGE (perf_55009670ee42:Performance{ uuid: 'a03fcfa7-6d92-4145-bd5e-55009670ee42' })
SET perf_55009670ee42.name = 'Why Can’t I'
SET perf_55009670ee42.disambiguation = 'original LP mono mix'
SET perf_55009670ee42.duration = '2:55'
SET perf_55009670ee42.begin_date = '1955-10-27'
SET perf_55009670ee42.end_date = '1955-10-27'
SET perf_55009670ee42.source = 'musicbrainz.org'


MERGE (perf_979a4e65ca30:Performance{ uuid: '466caff5-7152-4ac2-8678-979a4e65ca30' })
SET perf_979a4e65ca30.name = 'Oh My'
SET perf_979a4e65ca30.disambiguation = 'original LP mono mix'
SET perf_979a4e65ca30.duration = '2:21'
SET perf_979a4e65ca30.begin_date = '1955-10-27'
SET perf_979a4e65ca30.end_date = '1955-10-27'
SET perf_979a4e65ca30.source = 'musicbrainz.org'




// labels
MERGE (release_d61113ae5e78)-[:HAS_LABEL]->(label_42366b3be8c9)


// tracks
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_f8b570a1808d)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_f6a38101a1a9)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_39236758e7f6)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'A4', sequence: 4}]->(perf_ee1a4ca8b456)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'A5', sequence: 5}]->(perf_26f94da10eb4)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'A6', sequence: 6}]->(perf_2c9607075f35)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'B1', sequence: 7}]->(perf_8ba4ce1e86af)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'B2', sequence: 8}]->(perf_8cf574bd4653)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'B3', sequence: 9}]->(perf_514225818c11)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'B4', sequence: 10}]->(perf_128d0f309697)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'B5', sequence: 11}]->(perf_55009670ee42)
MERGE (release_d61113ae5e78)-[:HAS_TRACK {name: 'B6', sequence: 12}]->(perf_979a4e65ca30)

// works

MERGE (person_1904aa4268f4:Person{ uuid: '3fb75d97-5dfd-4e72-9aee-1904aa4268f4' }) 
SET person_1904aa4268f4.name = 'Lorenz Hart'
SET person_1904aa4268f4.gender = 'Male'
SET person_1904aa4268f4.country = 'US'
SET person_1904aa4268f4.allmusic = 'https://www.allmusic.com/artist/mn0000209620'
SET person_1904aa4268f4.discogs = 'https://www.discogs.com/artist/255800'
SET person_1904aa4268f4.imdb = 'https://www.imdb.com/name/nm0366414/'
SET person_1904aa4268f4.viaf = 'http://viaf.org/viaf/5122279'
SET person_1904aa4268f4.wikidata = 'https://www.wikidata.org/wiki/Q725828'
SET person_1904aa4268f4.databases = ['http://d-nb.info/gnd/118720538', 'http://id.loc.gov/authorities/names/n81097890', 'https://catalogue.bnf.fr/ark:/12148/cb13939224g', 'https://ibdb.com/Person/View/11244', 'http://snaccooperative.org/ark:/99166/w6x34z1s', 'https://nla.gov.au/nla.party-1266476', 'https://openlibrary.org/works/OL446542A', 'https://rateyourmusic.com/artist/lorenz_hart', 'https://www.worldcat.org/identities/lccn-n81097890/', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Lorenz&last=Hart&middle=']
SET person_1904aa4268f4.musicbrainz = 'https://musicbrainz.org/artist/3fb75d97-5dfd-4e72-9aee-1904aa4268f4'
SET person_1904aa4268f4.isni_list = ['http://isni.org/isni/0000000083526307']
SET person_1904aa4268f4.source = 'musicbrainz.org'


MERGE (person_376736bb6cde:Person{ uuid: '3508f3fd-3b18-493c-a362-376736bb6cde' }) 
SET person_376736bb6cde.name = 'Harold Arlen'
SET person_376736bb6cde.gender = 'Male'
SET person_376736bb6cde.country = 'US'
SET person_376736bb6cde.allmusic = 'https://www.allmusic.com/artist/mn0000060306'
SET person_376736bb6cde.discogs = 'https://www.discogs.com/artist/301975'
SET person_376736bb6cde.imdb = 'https://www.imdb.com/name/nm0002182/'
SET person_376736bb6cde.viaf = 'http://viaf.org/viaf/59268723'
SET person_376736bb6cde.wikidata = 'https://www.wikidata.org/wiki/Q448644'
SET person_376736bb6cde.databases = ['http://d-nb.info/gnd/119401193', 'http://id.loc.gov/authorities/names/n82155108', 'https://catalogue.bnf.fr/ark:/12148/cb13890872w', 'https://ibdb.com/person.php?id=11319', 'https://id.ndl.go.jp/auth/ndlna/001155326', 'http://snaccooperative.org/ark:/99166/w6z899sq', 'https://nla.gov.au/anbd.aut-an35107300', 'https://openlibrary.org/works/OL342313A', 'https://rateyourmusic.com/artist/harold_arlen', 'https://www.worldcat.org/identities/containsVIAFID/59268723']
SET person_376736bb6cde.musicbrainz = 'https://musicbrainz.org/artist/3508f3fd-3b18-493c-a362-376736bb6cde'
SET person_376736bb6cde.isni_list = ['http://isni.org/isni/0000000083863098', 'http://isni.org/isni/0000000368517543']
SET person_376736bb6cde.source = 'musicbrainz.org'


MERGE (person_7dc242502568:Person{ uuid: '0e860245-4ae3-423b-9a6f-7dc242502568' }) 
SET person_7dc242502568.name = 'Don George'
SET person_7dc242502568.gender = 'Male'
SET person_7dc242502568.disambiguation = 'US songwriter/composer, 1909–1987'
SET person_7dc242502568.country = 'US'
SET person_7dc242502568.discogs = 'https://www.discogs.com/artist/556378'
SET person_7dc242502568.imdb = 'https://www.imdb.com/name/nm0313405/'
SET person_7dc242502568.viaf = 'http://viaf.org/viaf/26551824'
SET person_7dc242502568.wikidata = 'https://www.wikidata.org/wiki/Q5292664'
SET person_7dc242502568.databases = ['http://id.loc.gov/authorities/names/nb90073419', 'https://catalogue.bnf.fr/ark:/12148/cb17052396b', 'https://www.ibdb.com/person.php?id=89869', 'https://www.worldcat.org/identities/lccn-nb90073419']
SET person_7dc242502568.musicbrainz = 'https://musicbrainz.org/artist/0e860245-4ae3-423b-9a6f-7dc242502568'
SET person_7dc242502568.isni_list = ['http://isni.org/isni/0000000116105120']
SET person_7dc242502568.source = 'musicbrainz.org'


MERGE (person_a47048af9239:Person{ uuid: 'c30f7f08-60d0-4211-88ac-a47048af9239' }) 
SET person_a47048af9239.name = 'Frank Madden'
SET person_a47048af9239.gender = 'Male'
SET person_a47048af9239.disambiguation = 'US songwriter'
SET person_a47048af9239.allmusic = 'https://www.allmusic.com/artist/mn0000145134'
SET person_a47048af9239.discogs = 'https://www.discogs.com/artist/941923'
SET person_a47048af9239.wikidata = 'https://www.wikidata.org/wiki/Q105415267'
SET person_a47048af9239.musicbrainz = 'https://musicbrainz.org/artist/c30f7f08-60d0-4211-88ac-a47048af9239'
SET person_a47048af9239.source = 'musicbrainz.org'


MERGE (person_ddfb2ac7ea1a:Person{ uuid: 'ff28a56b-3b04-420d-bf66-ddfb2ac7ea1a' }) 
SET person_ddfb2ac7ea1a.name = 'Mayme Watts'
SET person_ddfb2ac7ea1a.gender = 'Female'
SET person_ddfb2ac7ea1a.country = 'US'
SET person_ddfb2ac7ea1a.musicbrainz = 'https://musicbrainz.org/artist/ff28a56b-3b04-420d-bf66-ddfb2ac7ea1a'
SET person_ddfb2ac7ea1a.source = 'musicbrainz.org'


MERGE (person_307524b9919b:Person{ uuid: '49e0ff4d-5d7b-419b-8b93-307524b9919b' }) 
SET person_307524b9919b.name = 'Morgan Lewis'
SET person_307524b9919b.gender = 'Male'
SET person_307524b9919b.country = 'US'
SET person_307524b9919b.allmusic = 'https://www.allmusic.com/artist/mn0000501474'
SET person_307524b9919b.discogs = 'https://www.discogs.com/artist/714002'
SET person_307524b9919b.imdb = 'https://www.imdb.com/name/nm1200498/'
SET person_307524b9919b.viaf = 'http://viaf.org/viaf/60319107'
SET person_307524b9919b.wikidata = 'https://www.wikidata.org/wiki/Q6911746'
SET person_307524b9919b.databases = ['http://d-nb.info/gnd/1135507198', 'http://id.loc.gov/authorities/names/n00114900', 'https://catalogue.bnf.fr/ark:/12148/cb138023170', 'http://snaccooperative.org/ark:/99166/w69m52b1', 'https://www.ibdb.com/person.php?id=12061', 'https://www.worldcat.org/identities/lccn-n00114900/']
SET person_307524b9919b.musicbrainz = 'https://musicbrainz.org/artist/49e0ff4d-5d7b-419b-8b93-307524b9919b'
SET person_307524b9919b.isni_list = ['http://isni.org/isni/000000008139913X']
SET person_307524b9919b.source = 'musicbrainz.org'


MERGE (person_191ca24ad661:Person{ uuid: '7e43f216-d19c-4668-a939-191ca24ad661' }) 
SET person_191ca24ad661.name = 'Vincent Youmans'
SET person_191ca24ad661.gender = 'Male'
SET person_191ca24ad661.country = 'US'
SET person_191ca24ad661.discogs = 'https://www.discogs.com/artist/301996'
SET person_191ca24ad661.imdb = 'https://www.imdb.com/name/nm0949207/'
SET person_191ca24ad661.viaf = 'http://viaf.org/viaf/74039292'
SET person_191ca24ad661.wikidata = 'https://www.wikidata.org/wiki/Q746951'
SET person_191ca24ad661.databases = ['http://d-nb.info/gnd/11880815X', 'http://id.loc.gov/authorities/names/n80107199', 'https://catalogue.bnf.fr/ark:/12148/cb13901338w', 'https://ibdb.com/person.php?id=12607', 'http://snaccooperative.org/ark:/99166/w66t1fkb', 'https://nla.gov.au/nla.party-1227269', 'https://openlibrary.org/works/OL7514377A', 'https://www.worldcat.org/identities/lccn-n80107199/']
SET person_191ca24ad661.musicbrainz = 'https://musicbrainz.org/artist/7e43f216-d19c-4668-a939-191ca24ad661'
SET person_191ca24ad661.isni_list = ['http://isni.org/isni/0000000081543066']
SET person_191ca24ad661.source = 'musicbrainz.org'


MERGE (person_623899894a6c:Person{ uuid: 'e10cab5c-c6d3-472e-9df6-623899894a6c' }) 
SET person_623899894a6c.name = 'Ruth Lowe'
SET person_623899894a6c.gender = 'Female'
SET person_623899894a6c.country = 'CA'
SET person_623899894a6c.allmusic = 'https://www.allmusic.com/artist/mn0000806996'
SET person_623899894a6c.discogs = 'https://www.discogs.com/artist/675388'
SET person_623899894a6c.imdb = 'https://www.imdb.com/name/nm1283648/'
SET person_623899894a6c.wikidata = 'https://www.wikidata.org/wiki/Q7383090'
SET person_623899894a6c.wikipedia = 'https://en.wikipedia.org/wiki/Ruth_Lowe'
SET person_623899894a6c.musicbrainz = 'https://musicbrainz.org/artist/e10cab5c-c6d3-472e-9df6-623899894a6c'
SET person_623899894a6c.isni_list = ['http://isni.org/isni/000000007969982X']
SET person_623899894a6c.source = 'musicbrainz.org'


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


MERGE (person_98b47fc19825:Person{ uuid: 'f31022a9-f702-430d-9315-98b47fc19825' }) 
SET person_98b47fc19825.name = 'Irving Caesar'
SET person_98b47fc19825.gender = 'Male'
SET person_98b47fc19825.country = 'US'
SET person_98b47fc19825.allmusic = 'https://www.allmusic.com/artist/mn0000773150'
SET person_98b47fc19825.discogs = 'https://www.discogs.com/artist/301994'
SET person_98b47fc19825.imdb = 'https://www.imdb.com/name/nm0128371/'
SET person_98b47fc19825.viaf = 'http://viaf.org/viaf/54415815'
SET person_98b47fc19825.wikidata = 'https://www.wikidata.org/wiki/Q1284219'
SET person_98b47fc19825.databases = ['http://d-nb.info/gnd/135139783', 'http://id.loc.gov/authorities/names/no90027480', 'https://catalogue.bnf.fr/ark:/12148/cb14849329n', 'https://ibdb.com/person.php?id=6455', 'http://snaccooperative.org/ark:/99166/w6jd5b8j', 'https://nla.gov.au/nla.party-1203672', 'https://rateyourmusic.com/artist/irving_caesar', 'https://www.worldcat.org/identities/lccn-no90027480/']
SET person_98b47fc19825.musicbrainz = 'https://musicbrainz.org/artist/f31022a9-f702-430d-9315-98b47fc19825'
SET person_98b47fc19825.isni_list = ['http://isni.org/isni/0000000121337209']
SET person_98b47fc19825.source = 'musicbrainz.org'


MERGE (person_392d39d08ce3:Person{ uuid: 'e4c00cfe-8393-416b-90da-392d39d08ce3' }) 
SET person_392d39d08ce3.name = 'Nancy Hamilton'
SET person_392d39d08ce3.gender = 'Female'
SET person_392d39d08ce3.country = 'US'
SET person_392d39d08ce3.allmusic = 'https://www.allmusic.com/artist/mn0000366325'
SET person_392d39d08ce3.discogs = 'https://www.discogs.com/artist/714004'
SET person_392d39d08ce3.imdb = 'https://www.imdb.com/name/nm0358071/'
SET person_392d39d08ce3.viaf = 'http://viaf.org/viaf/67703673'
SET person_392d39d08ce3.wikidata = 'https://www.wikidata.org/wiki/Q13560398'
SET person_392d39d08ce3.databases = ['http://d-nb.info/gnd/1135507333', 'http://id.loc.gov/authorities/names/n00114903', 'http://snaccooperative.org/ark:/99166/w6tq65bb', 'https://rateyourmusic.com/artist/nancy_hamilton', 'https://www.ibdb.com/person.php?id=7862', 'https://www.worldcat.org/identities/lccn-n00114903/']
SET person_392d39d08ce3.musicbrainz = 'https://musicbrainz.org/artist/e4c00cfe-8393-416b-90da-392d39d08ce3'
SET person_392d39d08ce3.isni_list = ['http://isni.org/isni/000000005939149X']
SET person_392d39d08ce3.source = 'musicbrainz.org'


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
SET person_acc0205f7513.databases = ['http://d-nb.info/gnd/118790862', 'http://id.loc.gov/authorities/names/n50048058', 'https://catalogue.bnf.fr/ark:/12148/cb13899099w', 'https://ibdb.com/person.php?id=8323', 'http://snaccooperative.org/ark:/99166/w69h6cvt', 'https://nla.gov.au/nla.party-1015762', 'https://openlibrary.org/works/OL35365A', 'https://rateyourmusic.com/artist/richard_rodgers', 'https://www.worldcat.org/identities/lccn-n50048058/']
SET person_acc0205f7513.musicbrainz = 'https://musicbrainz.org/artist/346448f5-25a0-4f78-bbd6-acc0205f7513'
SET person_acc0205f7513.isni_list = ['http://isni.org/isni/0000000121482043']
SET person_acc0205f7513.source = 'musicbrainz.org'


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


MERGE (person_fd8f2bb1c7bf:Person{ uuid: '46f29ffe-7479-4365-bfd0-fd8f2bb1c7bf' }) 
SET person_fd8f2bb1c7bf.name = 'Hugh Martin'
SET person_fd8f2bb1c7bf.gender = 'Male'
SET person_fd8f2bb1c7bf.country = 'US'
SET person_fd8f2bb1c7bf.allmusic = 'https://www.allmusic.com/artist/mn0000045373'
SET person_fd8f2bb1c7bf.discogs = 'https://www.discogs.com/artist/615544'
SET person_fd8f2bb1c7bf.imdb = 'https://www.imdb.com/name/nm0552399/'
SET person_fd8f2bb1c7bf.viaf = 'http://viaf.org/viaf/63011164'
SET person_fd8f2bb1c7bf.wikidata = 'https://www.wikidata.org/wiki/Q5931668'
SET person_fd8f2bb1c7bf.databases = ['http://d-nb.info/gnd/134966139', 'http://id.loc.gov/authorities/names/n85378878', 'https://catalogue.bnf.fr/ark:/12148/cb147688218', 'https://ibdb.com/person.php?id=13678', 'http://snaccooperative.org/ark:/99166/w63x9krc', 'https://nla.gov.au/nla.party-1449274', 'https://rateyourmusic.com/artist/hugh_martin', 'https://www.worldcat.org/identities/lccn-n85378878/', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Hugh&last=Martin&middle=']
SET person_fd8f2bb1c7bf.musicbrainz = 'https://musicbrainz.org/artist/46f29ffe-7479-4365-bfd0-fd8f2bb1c7bf'
SET person_fd8f2bb1c7bf.isni_list = ['http://isni.org/isni/0000000081425561']
SET person_fd8f2bb1c7bf.source = 'musicbrainz.org'


MERGE (person_7eeeb45e411f:Person{ uuid: '3af06bc4-68ad-4cae-bb7a-7eeeb45e411f' }) 
SET person_7eeeb45e411f.name = 'Duke Ellington'
SET person_7eeeb45e411f.gender = 'Male'
SET person_7eeeb45e411f.disambiguation = 'US composer, pianist & jazz bandleader'
SET person_7eeeb45e411f.country = 'US'
SET person_7eeeb45e411f.allmusic = 'https://www.allmusic.com/artist/mn0000120323'
SET person_7eeeb45e411f.bbc = 'https://www.bbc.co.uk/music/artists/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.discogs = 'https://www.discogs.com/artist/145257'
SET person_7eeeb45e411f.imdb = 'https://www.imdb.com/name/nm0254153/'
SET person_7eeeb45e411f.viaf = 'http://viaf.org/viaf/66651610'
SET person_7eeeb45e411f.wikidata = 'https://www.wikidata.org/wiki/Q4030'
SET person_7eeeb45e411f.databases = ['http://d-nb.info/gnd/118529994', 'http://id.loc.gov/authorities/names/n50080187', 'https://catalogue.bnf.fr/ark:/12148/cb13893638w', 'https://ibdb.com/person.php?id=11631', 'http://snaccooperative.org/ark:/99166/w6639nkm', 'https://nla.gov.au/nla.party-815399', 'https://openlibrary.org/works/OL1953949A', 'https://rateyourmusic.com/artist/duke_ellington', 'https://www.worldcat.org/identities/lccn-n50080187/']
SET person_7eeeb45e411f.musicbrainz = 'https://musicbrainz.org/artist/3af06bc4-68ad-4cae-bb7a-7eeeb45e411f'
SET person_7eeeb45e411f.isni_list = ['http://isni.org/isni/0000000109110810']
SET person_7eeeb45e411f.source = 'musicbrainz.org'


MERGE (person_882436aa0554:Person{ uuid: '2a5c8f7a-558d-48b4-97ad-882436aa0554' }) 
SET person_882436aa0554.name = 'Sid Wyche'
SET person_882436aa0554.gender = 'Male'
SET person_882436aa0554.country = 'US'
SET person_882436aa0554.allmusic = 'https://www.allmusic.com/artist/mn0003199291'
SET person_882436aa0554.discogs = 'https://www.discogs.com/artist/622062'
SET person_882436aa0554.wikidata = 'https://www.wikidata.org/wiki/Q108545704'
SET person_882436aa0554.databases = ['http://id.loc.gov/authorities/names/n96106337', 'https://www.worldcat.org/identities/lccn-n96106337/']
SET person_882436aa0554.musicbrainz = 'https://musicbrainz.org/artist/2a5c8f7a-558d-48b4-97ad-882436aa0554'
SET person_882436aa0554.isni_list = ['http://isni.org/isni/0000000030335347']
SET person_882436aa0554.source = 'musicbrainz.org'


MERGE (person_a2befbae0ef2:Person{ uuid: 'ba5d193e-bc1f-49c9-a9b0-a2befbae0ef2' }) 
SET person_a2befbae0ef2.name = 'Joe Greene'
SET person_a2befbae0ef2.gender = 'Male'
SET person_a2befbae0ef2.disambiguation = 'US songwriter Joseph Perkins Greene, 1915-1986'
SET person_a2befbae0ef2.country = 'US'
SET person_a2befbae0ef2.discogs = 'https://www.discogs.com/artist/793483'
SET person_a2befbae0ef2.wikidata = 'https://www.wikidata.org/wiki/Q21604710'
SET person_a2befbae0ef2.wikipedia = 'https://en.wikipedia.org/wiki/Joe_Greene_(American_songwriter)'
SET person_a2befbae0ef2.musicbrainz = 'https://musicbrainz.org/artist/ba5d193e-bc1f-49c9-a9b0-a2befbae0ef2'
SET person_a2befbae0ef2.source = 'musicbrainz.org'


MERGE (person_4a9883a11628:Person{ uuid: '935cf315-1187-4436-bda1-4a9883a11628' }) 
SET person_4a9883a11628.name = 'Allan Flynn'
SET person_4a9883a11628.gender = 'Male'
SET person_4a9883a11628.musicbrainz = 'https://musicbrainz.org/artist/935cf315-1187-4436-bda1-4a9883a11628'
SET person_4a9883a11628.source = 'musicbrainz.org'


MERGE (person_dbde156f6907:Person{ uuid: '881d33d8-e86f-42e8-b571-dbde156f6907' }) 
SET person_dbde156f6907.name = 'Johnny Hodges'
SET person_dbde156f6907.gender = 'Male'
SET person_dbde156f6907.country = 'US'
SET person_dbde156f6907.allmusic = 'https://www.allmusic.com/artist/mn0000526407'
SET person_dbde156f6907.discogs = 'https://www.discogs.com/artist/258460'
SET person_dbde156f6907.imdb = 'https://www.imdb.com/name/nm0388178/'
SET person_dbde156f6907.viaf = 'http://viaf.org/viaf/71578250'
SET person_dbde156f6907.wikidata = 'https://www.wikidata.org/wiki/Q455176'
SET person_dbde156f6907.databases = ['http://d-nb.info/gnd/134407482', 'http://id.loc.gov/authorities/names/n81071360', 'https://catalogue.bnf.fr/ark:/12148/cb13895251g', 'https://ibdb.com/person.php?id=89879', 'http://snaccooperative.org/ark:/99166/w6bz6sr7', 'https://nla.gov.au/nla.party-1069233', 'https://rateyourmusic.com/artist/johnny-hodges', 'https://www.musik-sammler.de/artist/johnny-hodges/', 'https://www.worldcat.org/identities/lccn-n81071360']
SET person_dbde156f6907.musicbrainz = 'https://musicbrainz.org/artist/881d33d8-e86f-42e8-b571-dbde156f6907'
SET person_dbde156f6907.isni_list = ['http://isni.org/isni/0000000083930254']
SET person_dbde156f6907.source = 'musicbrainz.org'


MERGE (person_07e86cebef89:Person{ uuid: '82507ca3-189b-4fbe-a943-07e86cebef89' }) 
SET person_07e86cebef89.name = 'George Kelly'
SET person_07e86cebef89.gender = 'Male'
SET person_07e86cebef89.disambiguation = 'US jazz tenor saxophonist, vocalist and arranger'
SET person_07e86cebef89.country = 'US'
SET person_07e86cebef89.allmusic = 'https://www.allmusic.com/artist/mn0000944845'
SET person_07e86cebef89.discogs = 'https://www.discogs.com/artist/1452486'
SET person_07e86cebef89.viaf = 'http://viaf.org/viaf/17409440'
SET person_07e86cebef89.wikidata = 'https://www.wikidata.org/wiki/Q1507698'
SET person_07e86cebef89.wikipedia = 'https://en.wikipedia.org/wiki/George_Kelly_(musician)'
SET person_07e86cebef89.databases = ['http://id.loc.gov/authorities/names/n88643369', 'https://catalogue.bnf.fr/ark:/12148/cb139214675', 'https://www.worldcat.org/identities/lccn-n88643369']
SET person_07e86cebef89.musicbrainz = 'https://musicbrainz.org/artist/82507ca3-189b-4fbe-a943-07e86cebef89'
SET person_07e86cebef89.isni_list = ['http://isni.org/isni/000000007690957X']
SET person_07e86cebef89.source = 'musicbrainz.org'


MERGE (person_cabff6fab531:Person{ uuid: '42e52c03-27bb-4545-8924-cabff6fab531' }) 
SET person_cabff6fab531.name = 'Yip Harburg'
SET person_cabff6fab531.gender = 'Male'
SET person_cabff6fab531.country = 'US'
SET person_cabff6fab531.allmusic = 'https://www.allmusic.com/artist/mn0000806535'
SET person_cabff6fab531.discogs = 'https://www.discogs.com/artist/573556'
SET person_cabff6fab531.imdb = 'https://www.imdb.com/name/nm0361971/'
SET person_cabff6fab531.viaf = 'http://viaf.org/viaf/120709724'
SET person_cabff6fab531.wikidata = 'https://www.wikidata.org/wiki/Q1273621'
SET person_cabff6fab531.databases = ['http://d-nb.info/gnd/11919158X', 'http://id.loc.gov/authorities/names/n85342788', 'https://catalogue.bnf.fr/ark:/12148/cb13798046w', 'https://ibdb.com/person.php?id=5177', 'http://snaccooperative.org/ark:/99166/w6q9253m', 'https://nla.gov.au/nla.party-877568', 'https://openlibrary.org/works/OL6933834A', 'https://rateyourmusic.com/artist/e_y__yip_harburg', 'https://www.worldcat.org/identities/lccn-n85342788/']
SET person_cabff6fab531.musicbrainz = 'https://musicbrainz.org/artist/42e52c03-27bb-4545-8924-cabff6fab531'
SET person_cabff6fab531.isni_list = ['http://isni.org/isni/0000000117013279', 'http://isni.org/isni/0000000372914779']
SET person_cabff6fab531.source = 'musicbrainz.org'


MERGE (person_11b76336ae41:Person{ uuid: '23eb93f3-52b5-470a-aee1-11b76336ae41' }) 
SET person_11b76336ae41.name = 'Ralph Blane'
SET person_11b76336ae41.gender = 'Male'
SET person_11b76336ae41.country = 'US'
SET person_11b76336ae41.allmusic = 'https://www.allmusic.com/artist/mn0000868113'
SET person_11b76336ae41.discogs = 'https://www.discogs.com/artist/615542'
SET person_11b76336ae41.imdb = 'https://www.imdb.com/name/nm0087433/'
SET person_11b76336ae41.viaf = 'http://viaf.org/viaf/64274186'
SET person_11b76336ae41.wikidata = 'https://www.wikidata.org/wiki/Q7287254'
SET person_11b76336ae41.databases = ['http://d-nb.info/gnd/1035691000', 'http://id.loc.gov/authorities/names/n84040775', 'https://catalogue.bnf.fr/ark:/12148/cb14842656p', 'https://ibdb.com/person.php?id=11399', 'https://nla.gov.au/nla.party-1495653', 'https://rateyourmusic.com/artist/ralph_blane', 'https://www.worldcat.org/identities/lccn-n84040775/']
SET person_11b76336ae41.musicbrainz = 'https://musicbrainz.org/artist/23eb93f3-52b5-470a-aee1-11b76336ae41'
SET person_11b76336ae41.isni_list = ['http://isni.org/isni/0000000081440163']
SET person_11b76336ae41.source = 'musicbrainz.org'


MERGE (work_baf8c30ef7c2:Work{ uuid: '23db04e2-7940-4f42-8a6f-baf8c30ef7c2' })
SET work_baf8c30ef7c2.name = 'An Occasional Man'
SET work_baf8c30ef7c2.iswc = 'T-070.158.148-7'
SET work_baf8c30ef7c2.type = 'Song'
SET work_baf8c30ef7c2.musicbrainz = 'https://musicbrainz.org/work/23db04e2-7940-4f42-8a6f-baf8c30ef7c2'
SET work_baf8c30ef7c2.source = 'musicbrainz.org'


MERGE (work_6f97d42f9f5d:Work{ uuid: 'bbb45de0-50f9-3065-b712-6f97d42f9f5d' })
SET work_6f97d42f9f5d.name = 'How High the Moon'
SET work_6f97d42f9f5d.iswc = 'T-070.074.622-0'
SET work_6f97d42f9f5d.type = 'Song'
SET work_6f97d42f9f5d.wikidata = 'https://www.wikidata.org/wiki/Q1631676'
SET work_6f97d42f9f5d.musicbrainz = 'https://musicbrainz.org/work/bbb45de0-50f9-3065-b712-6f97d42f9f5d'
SET work_6f97d42f9f5d.source = 'musicbrainz.org'


MERGE (work_3b8d2792ace7:Work{ uuid: '12aca556-80d8-375b-904d-3b8d2792ace7' })
SET work_3b8d2792ace7.name = 'Why Can\\'t I?'
SET work_3b8d2792ace7.source = 'musicbrainz.org'


MERGE (work_0181088890d8:Work{ uuid: 'ecc823ea-4616-3b5e-92d3-0181088890d8' })
SET work_0181088890d8.name = 'I’ll Never Smile Again'
SET work_0181088890d8.iswc = 'T-070.266.459-2'
SET work_0181088890d8.type = 'Song'
SET work_0181088890d8.wikidata = 'https://www.wikidata.org/wiki/Q1123494'
SET work_0181088890d8.musicbrainz = 'https://musicbrainz.org/work/ecc823ea-4616-3b5e-92d3-0181088890d8'
SET work_0181088890d8.source = 'musicbrainz.org'


MERGE (work_702c61180860:Work{ uuid: 'ddf678a6-a75f-3235-bf12-702c61180860' })
SET work_702c61180860.name = 'Soon'
SET work_702c61180860.iswc = 'T-070.137.026-4'
SET work_702c61180860.type = 'Song'
SET work_702c61180860.wikidata = 'https://www.wikidata.org/wiki/Q7562677'
SET work_702c61180860.musicbrainz = 'https://musicbrainz.org/work/ddf678a6-a75f-3235-bf12-702c61180860'
SET work_702c61180860.source = 'musicbrainz.org'


MERGE (work_96764204a6e1:Work{ uuid: '6722fcb9-c885-424a-8068-96764204a6e1' })
SET work_96764204a6e1.name = 'It Shouldn’t Happen to a Dream'
SET work_96764204a6e1.iswc = 'T-070.907.473-6'
SET work_96764204a6e1.type = 'Song'
SET work_96764204a6e1.musicbrainz = 'https://musicbrainz.org/work/6722fcb9-c885-424a-8068-96764204a6e1'
SET work_96764204a6e1.source = 'musicbrainz.org'


MERGE (work_cf9c9f34fbc6:Work{ uuid: '567d44ec-87ce-3a82-9aed-cf9c9f34fbc6' })
SET work_cf9c9f34fbc6.name = 'Sometimes I’m Happy'
SET work_cf9c9f34fbc6.iswc = 'T-070.136.738-5'
SET work_cf9c9f34fbc6.type = 'Song'
SET work_cf9c9f34fbc6.wikidata = 'https://www.wikidata.org/wiki/Q7560299'
SET work_cf9c9f34fbc6.musicbrainz = 'https://musicbrainz.org/work/567d44ec-87ce-3a82-9aed-cf9c9f34fbc6'
SET work_cf9c9f34fbc6.source = 'musicbrainz.org'


MERGE (work_82979e3785ee:Work{ uuid: 'f8217125-b460-3902-8903-82979e3785ee' })
SET work_82979e3785ee.name = 'Over the Rainbow'
SET work_82979e3785ee.iswc = 'T-070.159.949-6'
SET work_82979e3785ee.type = 'Song'
SET work_82979e3785ee.wikidata = 'https://www.wikidata.org/wiki/Q161402'
SET work_82979e3785ee.musicbrainz = 'https://musicbrainz.org/work/f8217125-b460-3902-8903-82979e3785ee'
SET work_82979e3785ee.source = 'musicbrainz.org'


MERGE (work_deed2cb0ceaa:Work{ uuid: '945070ce-3f47-3c6c-9d2c-deed2cb0ceaa' })
SET work_deed2cb0ceaa.name = 'Cherokee'
SET work_deed2cb0ceaa.iswc = 'T-010.433.944-7'
SET work_deed2cb0ceaa.wikidata = 'https://www.wikidata.org/wiki/Q1070310'
SET work_deed2cb0ceaa.musicbrainz = 'https://musicbrainz.org/work/945070ce-3f47-3c6c-9d2c-deed2cb0ceaa'
SET work_deed2cb0ceaa.source = 'musicbrainz.org'


MERGE (work_9a75a3159cf7:Work{ uuid: 'c39a40cc-c801-36a2-89fe-9a75a3159cf7' })
SET work_9a75a3159cf7.name = 'Maybe'
SET work_9a75a3159cf7.iswc = 'T-070.108.692-1'
SET work_9a75a3159cf7.type = 'Song'
SET work_9a75a3159cf7.wikidata = 'https://www.wikidata.org/wiki/Q6796902'
SET work_9a75a3159cf7.musicbrainz = 'https://musicbrainz.org/work/c39a40cc-c801-36a2-89fe-9a75a3159cf7'
SET work_9a75a3159cf7.source = 'musicbrainz.org'


MERGE (work_c880c1051b5f:Work{ uuid: '578402df-44a3-4022-9adf-c880c1051b5f' })
SET work_c880c1051b5f.name = 'Oh My'
SET work_c880c1051b5f.type = 'Song'
SET work_c880c1051b5f.source = 'musicbrainz.org'


MERGE (work_fda7ab922548:Work{ uuid: 'ac4e38a0-a65d-471e-86df-fda7ab922548' })
SET work_fda7ab922548.name = 'Don’t Be on the Outside'
SET work_fda7ab922548.iswc = 'T-903.928.420-3'
SET work_fda7ab922548.type = 'Song'
SET work_fda7ab922548.source = 'musicbrainz.org'



// performances of
MERGE (perf_128d0f309697)-[:PERFORMANCE_OF]->(work_baf8c30ef7c2)
MERGE (perf_2c9607075f35)-[:PERFORMANCE_OF]->(work_6f97d42f9f5d)
MERGE (perf_55009670ee42)-[:PERFORMANCE_OF]->(work_3b8d2792ace7)
MERGE (perf_ee1a4ca8b456)-[:PERFORMANCE_OF]->(work_0181088890d8)
MERGE (perf_f6a38101a1a9)-[:PERFORMANCE_OF]->(work_702c61180860)
MERGE (perf_8ba4ce1e86af)-[:PERFORMANCE_OF]->(work_96764204a6e1)
MERGE (perf_8cf574bd4653)-[:PERFORMANCE_OF]->(work_cf9c9f34fbc6)
MERGE (perf_f8b570a1808d)-[:PERFORMANCE_OF]->(work_82979e3785ee)
MERGE (perf_39236758e7f6)-[:PERFORMANCE_OF]->(work_deed2cb0ceaa)
MERGE (perf_514225818c11)-[:PERFORMANCE_OF]->(work_9a75a3159cf7)
MERGE (perf_979a4e65ca30)-[:PERFORMANCE_OF]->(work_c880c1051b5f)
MERGE (perf_26f94da10eb4)-[:PERFORMANCE_OF]->(work_fda7ab922548)


// composers
MERGE (person_11b76336ae41)-[:COMPOSED]->(work_baf8c30ef7c2)
MERGE (person_fd8f2bb1c7bf)-[:COMPOSED]->(work_baf8c30ef7c2)
MERGE (person_307524b9919b)-[:COMPOSED]->(work_6f97d42f9f5d)
MERGE (person_392d39d08ce3)-[:WROTE_LYRICS]->(work_6f97d42f9f5d)
MERGE (person_acc0205f7513)-[:COMPOSED]->(work_3b8d2792ace7)
MERGE (person_1904aa4268f4)-[:WROTE_LYRICS]->(work_3b8d2792ace7)
MERGE (person_623899894a6c)-[:COMPOSED]->(work_0181088890d8)
MERGE (person_623899894a6c)-[:WROTE_LYRICS]->(work_0181088890d8)
MERGE (person_b693a808a158)-[:COMPOSED]->(work_702c61180860)
MERGE (person_322e34240ffc)-[:WROTE_LYRICS]->(work_702c61180860)
MERGE (person_7eeeb45e411f)-[:COMPOSED]->(work_96764204a6e1)
MERGE (person_7dc242502568)-[:COMPOSED]->(work_96764204a6e1)
MERGE (person_dbde156f6907)-[:COMPOSED]->(work_96764204a6e1)
MERGE (person_98b47fc19825)-[:COMPOSED]->(work_cf9c9f34fbc6)
MERGE (person_191ca24ad661)-[:WROTE_LYRICS]->(work_cf9c9f34fbc6)
MERGE (person_376736bb6cde)-[:COMPOSED]->(work_82979e3785ee)
MERGE (person_cabff6fab531)-[:WROTE_LYRICS]->(work_82979e3785ee)
MERGE (person_4e98168f002f)-[:COMPOSED]->(work_deed2cb0ceaa)
MERGE (person_4e98168f002f)-[:WROTE_LYRICS]->(work_deed2cb0ceaa)
MERGE (person_4a9883a11628)-[:COMPOSED]->(work_9a75a3159cf7)
MERGE (person_a47048af9239)-[:COMPOSED]->(work_9a75a3159cf7)
MERGE (person_a2befbae0ef2)-[:COMPOSED]->(work_c880c1051b5f)
MERGE (person_a2befbae0ef2)-[:WROTE_LYRICS]->(work_c880c1051b5f)
MERGE (person_07e86cebef89)-[:COMPOSED]->(work_fda7ab922548)
MERGE (person_ddfb2ac7ea1a)-[:COMPOSED]->(work_fda7ab922548)
MERGE (person_882436aa0554)-[:COMPOSED]->(work_fda7ab922548)


// place nodes

MERGE (place_decbb365c07f:Place{ uuid: '74e50e58-5deb-4b99-93a2-decbb365c07f' })
SET place_decbb365c07f.name = 'New York'
SET place_decbb365c07f.source = 'musicbrainz.org'


// place relationships
MERGE (perf_f8b570a1808d)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-27', end_date: '1955-10-27' }]->(place_decbb365c07f)
MERGE (perf_f6a38101a1a9)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-26', end_date: '1955-10-26' }]->(place_decbb365c07f)
MERGE (perf_39236758e7f6)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-26', end_date: '1955-10-26' }]->(place_decbb365c07f)
MERGE (perf_ee1a4ca8b456)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-25', end_date: '1955-10-25' }]->(place_decbb365c07f)
MERGE (perf_26f94da10eb4)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-25', end_date: '1955-10-25' }]->(place_decbb365c07f)
MERGE (perf_2c9607075f35)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-27', end_date: '1955-10-27' }]->(place_decbb365c07f)
MERGE (perf_8ba4ce1e86af)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-25', end_date: '1955-10-25' }]->(place_decbb365c07f)
MERGE (perf_8cf574bd4653)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-25', end_date: '1955-10-25' }]->(place_decbb365c07f)
MERGE (perf_514225818c11)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-26', end_date: '1955-10-26' }]->(place_decbb365c07f)
MERGE (perf_128d0f309697)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-26', end_date: '1955-10-26' }]->(place_decbb365c07f)
MERGE (perf_55009670ee42)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-27', end_date: '1955-10-27' }]->(place_decbb365c07f)
MERGE (perf_979a4e65ca30)-[:HAS_PLACE { type: 'recorded in', begin_date: '1955-10-27', end_date: '1955-10-27' }]->(place_decbb365c07f)

MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_f8b570a1808d)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_f8b570a1808d)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_f8b570a1808d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f8b570a1808d)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_f8b570a1808d)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f8b570a1808d)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_f8b570a1808d)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_f8b570a1808d)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_f8b570a1808d)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_f8b570a1808d)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_f8b570a1808d)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_f8b570a1808d)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_f6a38101a1a9)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_f6a38101a1a9)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_f6a38101a1a9)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f6a38101a1a9)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_f6a38101a1a9)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f6a38101a1a9)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_f6a38101a1a9)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_f6a38101a1a9)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_f6a38101a1a9)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_f6a38101a1a9)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_f6a38101a1a9)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_f6a38101a1a9)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_39236758e7f6)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_39236758e7f6)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_39236758e7f6)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_39236758e7f6)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_39236758e7f6)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_39236758e7f6)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_39236758e7f6)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_39236758e7f6)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_39236758e7f6)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_39236758e7f6)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_39236758e7f6)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_39236758e7f6)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_ee1a4ca8b456)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_ee1a4ca8b456)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_ee1a4ca8b456)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_ee1a4ca8b456)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_ee1a4ca8b456)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ee1a4ca8b456)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_ee1a4ca8b456)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_ee1a4ca8b456)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_ee1a4ca8b456)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_ee1a4ca8b456)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_ee1a4ca8b456)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_ee1a4ca8b456)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_26f94da10eb4)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_26f94da10eb4)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_26f94da10eb4)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_26f94da10eb4)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_26f94da10eb4)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_26f94da10eb4)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_26f94da10eb4)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_26f94da10eb4)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_26f94da10eb4)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_26f94da10eb4)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_26f94da10eb4)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_26f94da10eb4)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_2c9607075f35)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_2c9607075f35)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_2c9607075f35)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_2c9607075f35)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_2c9607075f35)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2c9607075f35)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_2c9607075f35)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_2c9607075f35)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone', 'flute'] }]->(perf_2c9607075f35)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_2c9607075f35)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_2c9607075f35)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_2c9607075f35)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_8ba4ce1e86af)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_8ba4ce1e86af)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_8ba4ce1e86af)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_8ba4ce1e86af)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_8ba4ce1e86af)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8ba4ce1e86af)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_8ba4ce1e86af)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_8ba4ce1e86af)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_8ba4ce1e86af)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_8ba4ce1e86af)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_8ba4ce1e86af)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_8ba4ce1e86af)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_8cf574bd4653)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_8cf574bd4653)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_8cf574bd4653)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_8cf574bd4653)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_8cf574bd4653)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8cf574bd4653)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_8cf574bd4653)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_8cf574bd4653)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_8cf574bd4653)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_8cf574bd4653)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_8cf574bd4653)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_8cf574bd4653)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_514225818c11)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_514225818c11)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_514225818c11)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_514225818c11)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_514225818c11)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_514225818c11)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_514225818c11)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_514225818c11)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_514225818c11)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_514225818c11)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_514225818c11)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_514225818c11)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_128d0f309697)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_128d0f309697)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_128d0f309697)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_128d0f309697)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_128d0f309697)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_128d0f309697)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_128d0f309697)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_128d0f309697)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_128d0f309697)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_128d0f309697)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_128d0f309697)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_128d0f309697)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_55009670ee42)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_55009670ee42)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_55009670ee42)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_55009670ee42)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_55009670ee42)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_55009670ee42)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_55009670ee42)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_55009670ee42)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_55009670ee42)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_55009670ee42)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_55009670ee42)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_55009670ee42)
MERGE (person_2fe1f9f27da8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_979a4e65ca30)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_979a4e65ca30)
MERGE (person_0933d6c60091)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_979a4e65ca30)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_979a4e65ca30)
MERGE (person_644bd536ec07)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_979a4e65ca30)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_979a4e65ca30)
MERGE (person_db21a63f19d9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_979a4e65ca30)
MERGE (person_8bc88dfd8774)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone'] }]->(perf_979a4e65ca30)
MERGE (person_43ac1e7a092c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute', 'tenor saxophone'] }]->(perf_979a4e65ca30)
MERGE (person_6be25a4576a2)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_979a4e65ca30)
MERGE (person_f42ad7cebf1e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_979a4e65ca30)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_979a4e65ca30)



"""
)