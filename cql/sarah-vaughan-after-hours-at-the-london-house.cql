// releases

MERGE (release_d694234072ba:Release{ uuid: '3a3cf7a8-c54c-309b-9372-d694234072ba' })
SET release_d694234072ba.name = 'After Hours at the London House'
SET release_d694234072ba.country = 'US'
SET release_d694234072ba.date = '1959'
SET release_d694234072ba.format = '12" Vinyl'
SET release_d694234072ba.discode = 'MG-20383'
SET release_d694234072ba.discogs = 'https://www.discogs.com/release/8971421'
SET release_d694234072ba.musicbrainz = 'http://musicbrainz.org/release/3a3cf7a8-c54c-309b-9372-d694234072ba'
SET release_d694234072ba.source = 'musicbrainz.org'
SET release_d694234072ba.timestamp = timestamp()

MERGE (person_ff9017878cdd:Person{ uuid: 'b59843a1-bb97-45f0-84b9-ff9017878cdd' }) 
SET person_ff9017878cdd.name = 'Richard Davis'
SET person_ff9017878cdd.gender = 'Male'
SET person_ff9017878cdd.disambiguation = 'American jazz bassist'
SET person_ff9017878cdd.country = 'US'
SET person_ff9017878cdd.allmusic = 'https://www.allmusic.com/artist/mn0000851653'
SET person_ff9017878cdd.discogs = 'https://www.discogs.com/artist/263441'
SET person_ff9017878cdd.viaf = 'http://viaf.org/viaf/120739764'
SET person_ff9017878cdd.wikidata = 'https://www.wikidata.org/wiki/Q716851'
SET person_ff9017878cdd.databases = ['http://d-nb.info/gnd/134355792', 'http://id.loc.gov/authorities/names/n81015291', 'https://catalogue.bnf.fr/ark:/12148/cb13893033h', 'http://snaccooperative.org/ark:/99166/w66d6dj7', 'https://rateyourmusic.com/artist/richard_davis', 'https://www.worldcat.org/identities/lccn-n81015291']
SET person_ff9017878cdd.musicbrainz = 'https://musicbrainz.org/artist/b59843a1-bb97-45f0-84b9-ff9017878cdd'
SET person_ff9017878cdd.isni_list = ['http://isni.org/isni/0000000079564079']
SET person_ff9017878cdd.source = 'musicbrainz.org'
SET person_ff9017878cdd.timestamp = timestamp()

MERGE (person_49233b3ea8cc:Person{ uuid: 'cffb356e-97ea-4566-9852-49233b3ea8cc' }) 
SET person_49233b3ea8cc.name = 'Ronnell Bright'
SET person_49233b3ea8cc.gender = 'Male'
SET person_49233b3ea8cc.country = 'US'
SET person_49233b3ea8cc.allmusic = 'https://www.allmusic.com/artist/mn0000283754'
SET person_49233b3ea8cc.discogs = 'https://www.discogs.com/artist/678784'
SET person_49233b3ea8cc.imdb = 'https://www.imdb.com/name/nm1388629/'
SET person_49233b3ea8cc.viaf = 'http://viaf.org/viaf/34642667'
SET person_49233b3ea8cc.wikidata = 'https://www.wikidata.org/wiki/Q2165975'
SET person_49233b3ea8cc.wikipedia = 'https://en.wikipedia.org/wiki/Ronnell_Bright'
SET person_49233b3ea8cc.databases = ['http://d-nb.info/gnd/134592328', 'http://id.loc.gov/authorities/names/n91108009', 'https://catalogue.bnf.fr/ark:/12148/cb138918546', 'http://snaccooperative.org/ark:/99166/w6gx4z85', 'https://www.worldcat.org/identities/lccn-n91108009']
SET person_49233b3ea8cc.musicbrainz = 'https://musicbrainz.org/artist/cffb356e-97ea-4566-9852-49233b3ea8cc'
SET person_49233b3ea8cc.isni_list = ['http://isni.org/isni/0000000055139932']
SET person_49233b3ea8cc.source = 'musicbrainz.org'
SET person_49233b3ea8cc.timestamp = timestamp()

MERGE (person_1b6313c126ca:Person{ uuid: '2676ce19-1319-48af-93dd-1b6313c126ca' }) 
SET person_1b6313c126ca.name = 'Thad Jones'
SET person_1b6313c126ca.gender = 'Male'
SET person_1b6313c126ca.country = 'US'
SET person_1b6313c126ca.allmusic = 'https://www.allmusic.com/artist/mn0000133119'
SET person_1b6313c126ca.discogs = 'https://www.discogs.com/artist/271154'
SET person_1b6313c126ca.imdb = 'https://www.imdb.com/name/nm1238001/'
SET person_1b6313c126ca.viaf = 'http://viaf.org/viaf/100314084'
SET person_1b6313c126ca.wikidata = 'https://www.wikidata.org/wiki/Q539883'
SET person_1b6313c126ca.databases = ['http://d-nb.info/gnd/133125777', 'http://id.loc.gov/authorities/names/n83043758', 'https://catalogue.bnf.fr/ark:/12148/cb138957468', 'http://snaccooperative.org/ark:/99166/w6gf112b', 'https://nla.gov.au/nla.party-896370', 'https://rateyourmusic.com/artist/thad_jones', 'https://www.worldcat.org/identities/lccn-n83043758']
SET person_1b6313c126ca.musicbrainz = 'https://musicbrainz.org/artist/2676ce19-1319-48af-93dd-1b6313c126ca'
SET person_1b6313c126ca.isni_list = ['http://isni.org/isni/0000000109289144']
SET person_1b6313c126ca.source = 'musicbrainz.org'
SET person_1b6313c126ca.timestamp = timestamp()

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
SET person_c85fad20da55.timestamp = timestamp()

MERGE (person_6b794cb69f8c:Person{ uuid: '0029973f-f57e-43d1-9f6e-6b794cb69f8c' }) 
SET person_6b794cb69f8c.name = 'Wendell Culley'
SET person_6b794cb69f8c.gender = 'Male'
SET person_6b794cb69f8c.country = 'US'
SET person_6b794cb69f8c.allmusic = 'https://www.allmusic.com/artist/mn0000194415'
SET person_6b794cb69f8c.discogs = 'https://www.discogs.com/artist/339273'
SET person_6b794cb69f8c.viaf = 'http://viaf.org/viaf/22331912'
SET person_6b794cb69f8c.wikidata = 'https://www.wikidata.org/wiki/Q664655'
SET person_6b794cb69f8c.databases = ['http://d-nb.info/gnd/134622545', 'http://id.loc.gov/authorities/names/n95101844', 'https://catalogue.bnf.fr/ark:/12148/cb13937672z', 'http://snaccooperative.org/ark:/99166/w68j2v55', 'https://www.worldcat.org/identities/lccn-n95101844']
SET person_6b794cb69f8c.musicbrainz = 'https://musicbrainz.org/artist/0029973f-f57e-43d1-9f6e-6b794cb69f8c'
SET person_6b794cb69f8c.isni_list = ['http://isni.org/isni/000000005516488X']
SET person_6b794cb69f8c.source = 'musicbrainz.org'
SET person_6b794cb69f8c.timestamp = timestamp()

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

MERGE (person_18bed4c8a3b8:Person{ uuid: '3d58bb59-5837-4805-a779-18bed4c8a3b8' }) 
SET person_18bed4c8a3b8.name = 'Henry Coker'
SET person_18bed4c8a3b8.gender = 'Male'
SET person_18bed4c8a3b8.country = 'US'
SET person_18bed4c8a3b8.allmusic = 'https://www.allmusic.com/artist/mn0000672596'
SET person_18bed4c8a3b8.discogs = 'https://www.discogs.com/artist/321922'
SET person_18bed4c8a3b8.viaf = 'http://viaf.org/viaf/37101334'
SET person_18bed4c8a3b8.wikidata = 'https://www.wikidata.org/wiki/Q1606614'
SET person_18bed4c8a3b8.wikipedia = 'https://en.wikipedia.org/wiki/Henry_Coker'
SET person_18bed4c8a3b8.databases = ['http://d-nb.info/gnd/134622537', 'http://id.loc.gov/authorities/names/no92003397', 'https://catalogue.bnf.fr/ark:/12148/cb13892621x', 'http://snaccooperative.org/ark:/99166/w6h5220s', 'https://www.worldcat.org/identities/lccn-no92003397']
SET person_18bed4c8a3b8.musicbrainz = 'https://musicbrainz.org/artist/3d58bb59-5837-4805-a779-18bed4c8a3b8'
SET person_18bed4c8a3b8.isni_list = ['http://isni.org/isni/0000000055140618']
SET person_18bed4c8a3b8.source = 'musicbrainz.org'
SET person_18bed4c8a3b8.timestamp = timestamp()

MERGE (person_cdc2599bcba6:Person{ uuid: '8a271ade-5c59-4223-9b29-cdc2599bcba6' }) 
SET person_cdc2599bcba6.name = 'Frank Wess'
SET person_cdc2599bcba6.gender = 'Male'
SET person_cdc2599bcba6.country = 'US'
SET person_cdc2599bcba6.allmusic = 'https://www.allmusic.com/artist/mn0000138635'
SET person_cdc2599bcba6.discogs = 'https://www.discogs.com/artist/10096'
SET person_cdc2599bcba6.imdb = 'https://www.imdb.com/name/nm0921785/'
SET person_cdc2599bcba6.viaf = 'http://viaf.org/viaf/119858348'
SET person_cdc2599bcba6.wikidata = 'https://www.wikidata.org/wiki/Q182792'
SET person_cdc2599bcba6.wikipedia = 'https://en.wikipedia.org/wiki/Frank_Wess'
SET person_cdc2599bcba6.databases = ['http://d-nb.info/gnd/134554922', 'http://id.loc.gov/authorities/names/n83045066', 'https://catalogue.bnf.fr/ark:/12148/cb13901108d', 'http://snaccooperative.org/ark:/99166/w6j99s0t', 'https://www.worldcat.org/identities/lccn-n83045066']
SET person_cdc2599bcba6.musicbrainz = 'https://musicbrainz.org/artist/8a271ade-5c59-4223-9b29-cdc2599bcba6'
SET person_cdc2599bcba6.isni_list = ['http://isni.org/isni/000000008188846X']
SET person_cdc2599bcba6.source = 'musicbrainz.org'
SET person_cdc2599bcba6.timestamp = timestamp()
// labels

MERGE (label_5a7a0ece8ad6:Label{ uuid: '995428e7-81b6-41dd-bd38-5a7a0ece8ad6' })
SET label_5a7a0ece8ad6.name= 'Mercury Records'

// performances

MERGE (perf_22e504b1a7cd:Performance{ uuid: '6c04ccac-2df8-453b-a824-22e504b1a7cd' })
SET perf_22e504b1a7cd.name = 'Like Someone in Love'
SET perf_22e504b1a7cd.duration = '3:37'
SET perf_22e504b1a7cd.begin = '1958-03-07'
SET perf_22e504b1a7cd.end = '1958-03-07'
SET perf_22e504b1a7cd.source = 'musicbrainz.org'
SET perf_22e504b1a7cd.timestamp = timestamp()

MERGE (perf_e60d2a08f1d7:Performance{ uuid: 'f11c967b-bfac-4b1b-94bc-e60d2a08f1d7' })
SET perf_e60d2a08f1d7.name = 'Detour Ahead'
SET perf_e60d2a08f1d7.duration = '5:28'
SET perf_e60d2a08f1d7.begin = '1958-03-07'
SET perf_e60d2a08f1d7.end = '1958-03-07'
SET perf_e60d2a08f1d7.source = 'musicbrainz.org'
SET perf_e60d2a08f1d7.timestamp = timestamp()

MERGE (perf_a14739f64633:Performance{ uuid: 'ca3a6c50-572f-4f5a-bb86-a14739f64633' })
SET perf_a14739f64633.name = 'Three Little Words'
SET perf_a14739f64633.duration = '3:40'
SET perf_a14739f64633.begin = '1958-03-07'
SET perf_a14739f64633.end = '1958-03-07'
SET perf_a14739f64633.source = 'musicbrainz.org'
SET perf_a14739f64633.timestamp = timestamp()

MERGE (perf_8e8bee805798:Performance{ uuid: 'd7a0319e-741c-4364-bf50-8e8bee805798' })
SET perf_8e8bee805798.name = 'I’ll String Along With You'
SET perf_8e8bee805798.duration = '5:15'
SET perf_8e8bee805798.begin = '1958-03-07'
SET perf_8e8bee805798.end = '1958-03-07'
SET perf_8e8bee805798.source = 'musicbrainz.org'
SET perf_8e8bee805798.timestamp = timestamp()

MERGE (perf_1e3a191a1b14:Performance{ uuid: '31a7084e-77ec-478f-9d25-1e3a191a1b14' })
SET perf_1e3a191a1b14.name = 'You’d Be So Nice to Come Home To'
SET perf_1e3a191a1b14.duration = '4:00'
SET perf_1e3a191a1b14.begin = '1958-03-07'
SET perf_1e3a191a1b14.end = '1958-03-07'
SET perf_1e3a191a1b14.source = 'musicbrainz.org'
SET perf_1e3a191a1b14.timestamp = timestamp()

MERGE (perf_6908b587ec84:Performance{ uuid: 'd47aa0e5-1486-465f-95d7-6908b587ec84' })
SET perf_6908b587ec84.name = 'Speak Low'
SET perf_6908b587ec84.duration = '4:51'
SET perf_6908b587ec84.begin = '1958-03-07'
SET perf_6908b587ec84.end = '1958-03-07'
SET perf_6908b587ec84.source = 'musicbrainz.org'
SET perf_6908b587ec84.timestamp = timestamp()

MERGE (perf_3250d56e0dea:Performance{ uuid: '6a2ec4bf-253b-45d3-aa4c-3250d56e0dea' })
SET perf_3250d56e0dea.name = 'All of You'
SET perf_3250d56e0dea.duration = '4:15'
SET perf_3250d56e0dea.begin = '1958-03-07'
SET perf_3250d56e0dea.end = '1958-03-07'
SET perf_3250d56e0dea.source = 'musicbrainz.org'
SET perf_3250d56e0dea.timestamp = timestamp()

MERGE (perf_78084253f0dd:Performance{ uuid: 'ba5c379c-4281-4507-b5cb-78084253f0dd' })
SET perf_78084253f0dd.name = 'Thanks for the Memory'
SET perf_78084253f0dd.duration = '6:58'
SET perf_78084253f0dd.begin = '1958-03-07'
SET perf_78084253f0dd.end = '1958-03-07'
SET perf_78084253f0dd.source = 'musicbrainz.org'
SET perf_78084253f0dd.timestamp = timestamp()



// labels
MERGE (release_d694234072ba)-[:HAS_LABEL]->(label_5a7a0ece8ad6)


// tracks
MERGE (release_d694234072ba)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_22e504b1a7cd)
MERGE (release_d694234072ba)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_e60d2a08f1d7)
MERGE (release_d694234072ba)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_a14739f64633)
MERGE (release_d694234072ba)-[:HAS_TRACK {name: 'A4', sequence: 4}]->(perf_8e8bee805798)
MERGE (release_d694234072ba)-[:HAS_TRACK {name: 'B1', sequence: 5}]->(perf_1e3a191a1b14)
MERGE (release_d694234072ba)-[:HAS_TRACK {name: 'B2', sequence: 6}]->(perf_6908b587ec84)
MERGE (release_d694234072ba)-[:HAS_TRACK {name: 'B3', sequence: 7}]->(perf_3250d56e0dea)
MERGE (release_d694234072ba)-[:HAS_TRACK {name: 'B4', sequence: 8}]->(perf_78084253f0dd)

// works

MERGE (person_668e586793d9:Person{ uuid: '46d8708e-e8f7-4a1b-ad13-668e586793d9' }) 
SET person_668e586793d9.name = 'Johnny Frigo'
SET person_668e586793d9.gender = 'Male'
SET person_668e586793d9.disambiguation = 'US jazz musician'
SET person_668e586793d9.country = 'US'
SET person_668e586793d9.allmusic = 'https://www.allmusic.com/artist/mn0000821026'
SET person_668e586793d9.discogs = 'https://www.discogs.com/artist/274253'
SET person_668e586793d9.imdb = 'https://www.imdb.com/name/nm3011081/'
SET person_668e586793d9.viaf = 'http://viaf.org/viaf/46949353'
SET person_668e586793d9.wikidata = 'https://www.wikidata.org/wiki/Q1702324'
SET person_668e586793d9.databases = ['http://d-nb.info/gnd/13461089X', 'http://id.loc.gov/authorities/names/n91115192', 'https://catalogue.bnf.fr/ark:/12148/cb13931747k', 'https://www.worldcat.org/identities/lccn-n91115192']
SET person_668e586793d9.musicbrainz = 'https://musicbrainz.org/artist/46d8708e-e8f7-4a1b-ad13-668e586793d9'
SET person_668e586793d9.isni_list = ['http://isni.org/isni/0000000059374104']
SET person_668e586793d9.source = 'musicbrainz.org'
SET person_668e586793d9.timestamp = timestamp()

MERGE (person_8eb400d9bcdc:Person{ uuid: '0c233822-7d98-4746-8dc7-8eb400d9bcdc' }) 
SET person_8eb400d9bcdc.name = 'Harry Ruby'
SET person_8eb400d9bcdc.gender = 'Male'
SET person_8eb400d9bcdc.country = 'US'
SET person_8eb400d9bcdc.allmusic = 'https://www.allmusic.com/artist/mn0000683640'
SET person_8eb400d9bcdc.discogs = 'https://www.discogs.com/artist/622064'
SET person_8eb400d9bcdc.imdb = 'https://www.imdb.com/name/nm0748438/'
SET person_8eb400d9bcdc.viaf = 'http://viaf.org/viaf/100234716'
SET person_8eb400d9bcdc.wikidata = 'https://www.wikidata.org/wiki/Q507947'
SET person_8eb400d9bcdc.databases = ['http://d-nb.info/gnd/134503635', 'http://id.loc.gov/authorities/names/n85106023', 'https://catalogue.bnf.fr/ark:/12148/cb139401901', 'http://snaccooperative.org/ark:/99166/w6tq7cms', 'https://rateyourmusic.com/artist/harry_ruby', 'https://www.ibdb.com/person.php?id=6141', 'https://www.worldcat.org/identities/lccn-n85106023/']
SET person_8eb400d9bcdc.musicbrainz = 'https://musicbrainz.org/artist/0c233822-7d98-4746-8dc7-8eb400d9bcdc'
SET person_8eb400d9bcdc.isni_list = ['http://isni.org/isni/0000000118801592']
SET person_8eb400d9bcdc.source = 'musicbrainz.org'
SET person_8eb400d9bcdc.timestamp = timestamp()

MERGE (person_955faa96931d:Person{ uuid: '213f938b-35d6-406c-aae5-955faa96931d' }) 
SET person_955faa96931d.name = 'Bert Kalmar'
SET person_955faa96931d.gender = 'Male'
SET person_955faa96931d.country = 'US'
SET person_955faa96931d.allmusic = 'https://www.allmusic.com/artist/mn0000749456'
SET person_955faa96931d.discogs = 'https://www.discogs.com/artist/679003'
SET person_955faa96931d.imdb = 'https://www.imdb.com/name/nm0436095/'
SET person_955faa96931d.viaf = 'http://viaf.org/viaf/46957275'
SET person_955faa96931d.wikidata = 'https://www.wikidata.org/wiki/Q655221'
SET person_955faa96931d.databases = ['http://d-nb.info/gnd/129591513', 'http://id.loc.gov/authorities/names/n85106022', 'https://catalogue.bnf.fr/ark:/12148/cb140034387', 'https://ibdb.com/person.php?id=4504', 'http://snaccooperative.org/ark:/99166/w6d802ws', 'https://nla.gov.au/nla.party-978642', 'https://rateyourmusic.com/artist/bert_kalmar', 'https://www.worldcat.org/identities/lccn-n85106022/']
SET person_955faa96931d.musicbrainz = 'https://musicbrainz.org/artist/213f938b-35d6-406c-aae5-955faa96931d'
SET person_955faa96931d.isni_list = ['http://isni.org/isni/0000000083797510']
SET person_955faa96931d.source = 'musicbrainz.org'
SET person_955faa96931d.timestamp = timestamp()

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
SET person_8825529afd5d.databases = ['http://d-nb.info/gnd/102085412X', 'http://id.loc.gov/authorities/names/no89004670', 'https://catalogue.bnf.fr/ark:/12148/cb148427966', 'http://snaccooperative.org/ark:/99166/w6z61w7v', 'https://nla.gov.au/nla.party-887950', 'https://rateyourmusic.com/artist/johnny_burke_f1', 'https://www.ibdb.com/person.php?id=11462', 'https://www.worldcat.org/identities/lccn-no89004670/']
SET person_8825529afd5d.musicbrainz = 'https://musicbrainz.org/artist/c9b9ec99-b592-4556-aa0b-8825529afd5d'
SET person_8825529afd5d.isni_list = ['http://isni.org/isni/0000000071400010']
SET person_8825529afd5d.source = 'musicbrainz.org'
SET person_8825529afd5d.timestamp = timestamp()

MERGE (person_5c6090f7ea1b:Person{ uuid: 'ab4ee924-e126-4835-8433-5c6090f7ea1b' }) 
SET person_5c6090f7ea1b.name = 'Al Dubin'
SET person_5c6090f7ea1b.gender = 'Male'
SET person_5c6090f7ea1b.country = 'CH'
SET person_5c6090f7ea1b.allmusic = 'https://www.allmusic.com/artist/mn0000770368'
SET person_5c6090f7ea1b.discogs = 'https://www.discogs.com/artist/628267'
SET person_5c6090f7ea1b.imdb = 'https://www.imdb.com/name/nm0006048/'
SET person_5c6090f7ea1b.viaf = 'http://viaf.org/viaf/71582796'
SET person_5c6090f7ea1b.wikidata = 'https://www.wikidata.org/wiki/Q180899'
SET person_5c6090f7ea1b.databases = ['http://d-nb.info/gnd/103976604', 'http://id.loc.gov/authorities/names/n80151128', 'https://adp.library.ucsb.edu/names/102968', 'https://catalogue.bnf.fr/ark:/12148/cb139430418', 'http://snaccooperative.org/ark:/99166/w6b39wqj', 'https://nla.gov.au/nla.party-919241', 'https://rateyourmusic.com/artist/al_dubin', 'https://www.ibdb.com/person.php?id=12855', 'https://www.worldcat.org/identities/lccn-n80151128/']
SET person_5c6090f7ea1b.musicbrainz = 'https://musicbrainz.org/artist/ab4ee924-e126-4835-8433-5c6090f7ea1b'
SET person_5c6090f7ea1b.isni_list = ['http://isni.org/isni/0000000081517132']
SET person_5c6090f7ea1b.source = 'musicbrainz.org'
SET person_5c6090f7ea1b.timestamp = timestamp()

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
SET person_a6d92136636f.databases = ['http://d-nb.info/gnd/134545370', 'http://id.loc.gov/authorities/names/n87146380', 'https://catalogue.bnf.fr/ark:/12148/cb13952105n', 'https://ibdb.com/person.php?id=12521', 'http://snaccooperative.org/ark:/99166/w6zc82bn', 'https://nla.gov.au/nla.party-887953', 'https://rateyourmusic.com/artist/jimmy_van_heusen', 'https://www.worldcat.org/identities/lccn-n87146380/']
SET person_a6d92136636f.musicbrainz = 'https://musicbrainz.org/artist/8d3f8b43-0d28-4500-900e-a6d92136636f'
SET person_a6d92136636f.isni_list = ['http://isni.org/isni/0000000081333253']
SET person_a6d92136636f.source = 'musicbrainz.org'
SET person_a6d92136636f.timestamp = timestamp()

MERGE (person_7fd09c8ae291:Person{ uuid: '7a9390eb-76ea-4d3a-a786-7fd09c8ae291' }) 
SET person_7fd09c8ae291.name = 'Harry Warren'
SET person_7fd09c8ae291.gender = 'Male'
SET person_7fd09c8ae291.disambiguation = 'US composer and lyricist'
SET person_7fd09c8ae291.country = 'US'
SET person_7fd09c8ae291.allmusic = 'https://www.allmusic.com/artist/mn0000961299'
SET person_7fd09c8ae291.discogs = 'https://www.discogs.com/artist/601710'
SET person_7fd09c8ae291.imdb = 'https://www.imdb.com/name/nm0912851/'
SET person_7fd09c8ae291.viaf = 'http://viaf.org/viaf/79169269'
SET person_7fd09c8ae291.wikidata = 'https://www.wikidata.org/wiki/Q938810'
SET person_7fd09c8ae291.databases = ['http://d-nb.info/gnd/134551028', 'http://id.loc.gov/authorities/names/n81048007', 'https://catalogue.bnf.fr/ark:/12148/cb139392354', 'http://snaccooperative.org/ark:/99166/w6ff3r5t', 'https://nla.gov.au/nla.party-979287', 'https://rateyourmusic.com/artist/harry_warren', 'https://www.ibdb.com/person.php?id=12549', 'https://www.worldcat.org/identities/lccn-n81048007/']
SET person_7fd09c8ae291.musicbrainz = 'https://musicbrainz.org/artist/7a9390eb-76ea-4d3a-a786-7fd09c8ae291'
SET person_7fd09c8ae291.isni_list = ['http://isni.org/isni/0000000083969407']
SET person_7fd09c8ae291.source = 'musicbrainz.org'
SET person_7fd09c8ae291.timestamp = timestamp()

MERGE (person_4f7500861060:Person{ uuid: '0e738f68-783c-4a6a-80ae-4f7500861060' }) 
SET person_4f7500861060.name = 'Kurt Weill'
SET person_4f7500861060.gender = 'Male'
SET person_4f7500861060.disambiguation = 'composer'
SET person_4f7500861060.country = 'DE'
SET person_4f7500861060.allmusic = 'https://www.allmusic.com/artist/mn0000683446'
SET person_4f7500861060.discogs = 'https://www.discogs.com/artist/407111'
SET person_4f7500861060.imdb = 'https://www.imdb.com/name/nm0918044/'
SET person_4f7500861060.viaf = 'http://viaf.org/viaf/76501825'
SET person_4f7500861060.wikidata = 'https://www.wikidata.org/wiki/Q55004'
SET person_4f7500861060.databases = ['http://d-nb.info/gnd/118630202', 'http://id.loc.gov/authorities/names/n50022735', 'https://catalogue.bnf.fr/ark:/12148/cb13901071w', 'https://ibdb.com/person.php?id=7112', 'http://snaccooperative.org/ark:/99166/w6rr1x51', 'https://nla.gov.au/nla.party-1009171', 'https://openlibrary.org/works/OL452842A', 'https://rateyourmusic.com/artist/kurt_weill', 'https://www.worldcat.org/identities/lccn-n50022735']
SET person_4f7500861060.musicbrainz = 'https://musicbrainz.org/artist/0e738f68-783c-4a6a-80ae-4f7500861060'
SET person_4f7500861060.isni_list = ['http://isni.org/isni/0000000114753562']
SET person_4f7500861060.source = 'musicbrainz.org'
SET person_4f7500861060.timestamp = timestamp()

MERGE (person_14f95e6ce86d:Person{ uuid: 'e8006a80-7c18-4b1c-a10f-14f95e6ce86d' }) 
SET person_14f95e6ce86d.name = 'Leo Robin'
SET person_14f95e6ce86d.gender = 'Male'
SET person_14f95e6ce86d.disambiguation = 'US composer, lyricist & songwriter'
SET person_14f95e6ce86d.country = 'US'
SET person_14f95e6ce86d.allmusic = 'https://www.allmusic.com/artist/mn0000821040'
SET person_14f95e6ce86d.discogs = 'https://www.discogs.com/artist/531605'
SET person_14f95e6ce86d.imdb = 'https://www.imdb.com/name/nm0732209/'
SET person_14f95e6ce86d.viaf = 'http://viaf.org/viaf/28536574'
SET person_14f95e6ce86d.wikidata = 'https://www.wikidata.org/wiki/Q364124'
SET person_14f95e6ce86d.databases = ['http://d-nb.info/gnd/13477535X', 'http://id.loc.gov/authorities/names/n85378850', 'https://catalogue.bnf.fr/ark:/12148/cb13948729j', 'https://ibdb.com/person.php?id=13232', 'http://snaccooperative.org/ark:/99166/w6jj6cx7', 'https://nla.gov.au/nla.party-1072860', 'https://rateyourmusic.com/artist/leo_robin', 'https://www.worldcat.org/identities/lccn-n85378850/']
SET person_14f95e6ce86d.musicbrainz = 'https://musicbrainz.org/artist/e8006a80-7c18-4b1c-a10f-14f95e6ce86d'
SET person_14f95e6ce86d.isni_list = ['http://isni.org/isni/0000000110233164']
SET person_14f95e6ce86d.source = 'musicbrainz.org'
SET person_14f95e6ce86d.timestamp = timestamp()

MERGE (person_180c3283d2f9:Person{ uuid: '33ddc4a0-2d48-4da5-91f4-180c3283d2f9' }) 
SET person_180c3283d2f9.name = 'Herb Ellis'
SET person_180c3283d2f9.gender = 'Male'
SET person_180c3283d2f9.disambiguation = 'jazz guitarist'
SET person_180c3283d2f9.country = 'US'
SET person_180c3283d2f9.allmusic = 'https://www.allmusic.com/artist/mn0000674310'
SET person_180c3283d2f9.discogs = 'https://www.discogs.com/artist/256065'
SET person_180c3283d2f9.imdb = 'https://www.imdb.com/name/nm0254869/'
SET person_180c3283d2f9.viaf = 'http://viaf.org/viaf/85720646'
SET person_180c3283d2f9.wikidata = 'https://www.wikidata.org/wiki/Q499662'
SET person_180c3283d2f9.databases = ['http://d-nb.info/gnd/134366794', 'http://id.loc.gov/authorities/names/n81026541', 'https://catalogue.bnf.fr/ark:/12148/cb13893644t', 'http://snaccooperative.org/ark:/99166/w6bp3jjr', 'https://rateyourmusic.com/artist/herb-ellis', 'https://www.worldcat.org/identities/lccn-n81026541']
SET person_180c3283d2f9.musicbrainz = 'https://musicbrainz.org/artist/33ddc4a0-2d48-4da5-91f4-180c3283d2f9'
SET person_180c3283d2f9.isni_list = ['http://isni.org/isni/0000000114766996']
SET person_180c3283d2f9.source = 'musicbrainz.org'
SET person_180c3283d2f9.timestamp = timestamp()

MERGE (person_f6e8c16c7467:Person{ uuid: 'df603a62-0f5e-4ed9-b494-f6e8c16c7467' }) 
SET person_f6e8c16c7467.name = 'Ogden Nash'
SET person_f6e8c16c7467.gender = 'Male'
SET person_f6e8c16c7467.country = 'US'
SET person_f6e8c16c7467.allmusic = 'https://www.allmusic.com/artist/mn0000046126'
SET person_f6e8c16c7467.discogs = 'https://www.discogs.com/artist/598013'
SET person_f6e8c16c7467.viaf = 'http://viaf.org/viaf/14812297'
SET person_f6e8c16c7467.wikidata = 'https://www.wikidata.org/wiki/Q719228'
SET person_f6e8c16c7467.wikipedia = 'https://en.wikipedia.org/wiki/Ogden_Nash'
SET person_f6e8c16c7467.databases = ['https://rateyourmusic.com/artist/ogden_nash']
SET person_f6e8c16c7467.musicbrainz = 'https://musicbrainz.org/artist/df603a62-0f5e-4ed9-b494-f6e8c16c7467'
SET person_f6e8c16c7467.isni_list = ['http://isni.org/isni/0000000110406088']
SET person_f6e8c16c7467.source = 'musicbrainz.org'
SET person_f6e8c16c7467.timestamp = timestamp()

MERGE (person_6565dc36a994:Person{ uuid: '890022a1-6d43-4fd8-94a8-6565dc36a994' }) 
SET person_6565dc36a994.name = 'Ralph Rainger'
SET person_6565dc36a994.gender = 'Male'
SET person_6565dc36a994.country = 'US'
SET person_6565dc36a994.allmusic = 'https://www.allmusic.com/artist/mn0000387462'
SET person_6565dc36a994.discogs = 'https://www.discogs.com/artist/531602'
SET person_6565dc36a994.imdb = 'https://www.imdb.com/name/nm0006247/'
SET person_6565dc36a994.viaf = 'http://viaf.org/viaf/76505949'
SET person_6565dc36a994.wikidata = 'https://www.wikidata.org/wiki/Q364163'
SET person_6565dc36a994.databases = ['http://d-nb.info/gnd/1036356884', 'http://id.loc.gov/authorities/names/no93028475', 'https://catalogue.bnf.fr/ark:/12148/cb13948556w', 'http://snaccooperative.org/ark:/99166/w6r79vps', 'https://nla.gov.au/nla.party-953360', 'https://www.ibdb.com/person.php?id=78637', 'https://www.worldcat.org/identities/lccn-no93028475/']
SET person_6565dc36a994.musicbrainz = 'https://musicbrainz.org/artist/890022a1-6d43-4fd8-94a8-6565dc36a994'
SET person_6565dc36a994.isni_list = ['http://isni.org/isni/0000000083956745']
SET person_6565dc36a994.source = 'musicbrainz.org'
SET person_6565dc36a994.timestamp = timestamp()

MERGE (person_75474f6dae9f:Person{ uuid: '9102865f-0037-4c60-947f-75474f6dae9f' }) 
SET person_75474f6dae9f.name = 'Lou Carter'
SET person_75474f6dae9f.gender = 'Male'
SET person_75474f6dae9f.country = 'US'
SET person_75474f6dae9f.discogs = 'https://www.discogs.com/artist/708476'
SET person_75474f6dae9f.viaf = 'http://viaf.org/viaf/41046149'
SET person_75474f6dae9f.wikidata = 'https://www.wikidata.org/wiki/Q1650207'
SET person_75474f6dae9f.databases = ['http://id.loc.gov/authorities/names/n93009541', 'https://www.worldcat.org/identities/lccn-n93009541']
SET person_75474f6dae9f.musicbrainz = 'https://musicbrainz.org/artist/9102865f-0037-4c60-947f-75474f6dae9f'
SET person_75474f6dae9f.source = 'musicbrainz.org'
SET person_75474f6dae9f.timestamp = timestamp()

MERGE (person_a37897b950ce:Person{ uuid: '4a94a6cb-e70a-418b-bb53-a37897b950ce' }) 
SET person_a37897b950ce.name = 'Cole Porter'
SET person_a37897b950ce.gender = 'Male'
SET person_a37897b950ce.disambiguation = 'composer'
SET person_a37897b950ce.country = 'US'
SET person_a37897b950ce.allmusic = 'https://www.allmusic.com/artist/mn0000109607'
SET person_a37897b950ce.discogs = 'https://www.discogs.com/artist/264026'
SET person_a37897b950ce.imdb = 'https://www.imdb.com/name/nm0006234/'
SET person_a37897b950ce.viaf = 'http://viaf.org/viaf/5118684'
SET person_a37897b950ce.wikidata = 'https://www.wikidata.org/wiki/Q215120'
SET person_a37897b950ce.databases = ['http://d-nb.info/gnd/11879292X', 'http://id.loc.gov/authorities/names/n80017862', 'https://catalogue.bnf.fr/ark:/12148/cb13898618g', 'https://ibdb.com/person.php?id=12257', 'http://snaccooperative.org/ark:/99166/w6j38s5m', 'https://nla.gov.au/nla.party-949524', 'https://openlibrary.org/works/OL709416A', 'http://soundtrackcollector.com/composer/166/', 'https://rateyourmusic.com/artist/cole_porter', 'https://www.worldcat.org/identities/lccn-n80017862', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Cole&last=Porter&middle=']
SET person_a37897b950ce.musicbrainz = 'https://musicbrainz.org/artist/4a94a6cb-e70a-418b-bb53-a37897b950ce'
SET person_a37897b950ce.isni_list = ['http://isni.org/isni/0000000108653610']
SET person_a37897b950ce.source = 'musicbrainz.org'
SET person_a37897b950ce.timestamp = timestamp()

MERGE (work_8748f890dd88:Work{ uuid: 'b863dcdb-556c-3f82-94c2-8748f890dd88' })
SET work_8748f890dd88.name = 'Detour Ahead'
SET work_8748f890dd88.iswc = 'T-071.181.436-6'
SET work_8748f890dd88.type = 'Song'
SET work_8748f890dd88.wikidata = 'https://www.wikidata.org/wiki/Q5265789'
SET work_8748f890dd88.musicbrainz = 'https://musicbrainz.org/work/b863dcdb-556c-3f82-94c2-8748f890dd88'
SET work_8748f890dd88.source = 'musicbrainz.org'
SET work_8748f890dd88.timestamp = timestamp()

MERGE (work_13a3125d3c19:Work{ uuid: '9721f999-fdb5-3331-94da-13a3125d3c19' })
SET work_13a3125d3c19.name = 'Speak Low'
SET work_13a3125d3c19.iswc = 'T-070.137.239-5'
SET work_13a3125d3c19.type = 'Song'
SET work_13a3125d3c19.wikidata = 'https://www.wikidata.org/wiki/Q1799926'
SET work_13a3125d3c19.musicbrainz = 'https://musicbrainz.org/work/9721f999-fdb5-3331-94da-13a3125d3c19'
SET work_13a3125d3c19.source = 'musicbrainz.org'
SET work_13a3125d3c19.timestamp = timestamp()

MERGE (work_0eeaedc04aac:Work{ uuid: 'f62a25f0-30c1-31c3-818f-0eeaedc04aac' })
SET work_0eeaedc04aac.name = 'I’ll String Along With You'
SET work_0eeaedc04aac.iswc = 'T-070.210.739-8'
SET work_0eeaedc04aac.type = 'Song'
SET work_0eeaedc04aac.wikidata = 'https://www.wikidata.org/wiki/Q16386212'
SET work_0eeaedc04aac.musicbrainz = 'https://musicbrainz.org/work/f62a25f0-30c1-31c3-818f-0eeaedc04aac'
SET work_0eeaedc04aac.source = 'musicbrainz.org'
SET work_0eeaedc04aac.timestamp = timestamp()

MERGE (work_1a76a8a20304:Work{ uuid: '37b27e98-26a4-3411-abf2-1a76a8a20304' })
SET work_1a76a8a20304.name = 'Thanks for the Memory'
SET work_1a76a8a20304.iswc = 'T-070.178.583-2'
SET work_1a76a8a20304.type = 'Song'
SET work_1a76a8a20304.wikidata = 'https://www.wikidata.org/wiki/Q3816112'
SET work_1a76a8a20304.musicbrainz = 'https://musicbrainz.org/work/37b27e98-26a4-3411-abf2-1a76a8a20304'
SET work_1a76a8a20304.source = 'musicbrainz.org'
SET work_1a76a8a20304.timestamp = timestamp()

MERGE (work_6126d682fab2:Work{ uuid: 'dca3d1eb-0365-37fd-97de-6126d682fab2' })
SET work_6126d682fab2.name = 'You’d Be So Nice to Come Home To'
SET work_6126d682fab2.iswc = 'T-070.211.122-5'
SET work_6126d682fab2.type = 'Song'
SET work_6126d682fab2.wikidata = 'https://www.wikidata.org/wiki/Q2601445'
SET work_6126d682fab2.wikipedia = 'https://en.wikipedia.org/wiki/You%27d_Be_So_Nice_to_Come_Home_To'
SET work_6126d682fab2.musicbrainz = 'https://musicbrainz.org/work/dca3d1eb-0365-37fd-97de-6126d682fab2'
SET work_6126d682fab2.source = 'musicbrainz.org'
SET work_6126d682fab2.timestamp = timestamp()

MERGE (work_aae7fa5e1564:Work{ uuid: '25da9e17-9428-39d0-9e4d-aae7fa5e1564' })
SET work_aae7fa5e1564.name = 'Three Little Words'
SET work_aae7fa5e1564.iswc = 'T-070.180.019-2'
SET work_aae7fa5e1564.type = 'Song'
SET work_aae7fa5e1564.wikidata = 'https://www.wikidata.org/wiki/Q7797594'
SET work_aae7fa5e1564.musicbrainz = 'https://musicbrainz.org/work/25da9e17-9428-39d0-9e4d-aae7fa5e1564'
SET work_aae7fa5e1564.source = 'musicbrainz.org'
SET work_aae7fa5e1564.timestamp = timestamp()

MERGE (work_370654cda985:Work{ uuid: 'c9a51eb1-c80a-33e9-b015-370654cda985' })
SET work_370654cda985.name = 'All of You'
SET work_370654cda985.iswc = 'T-072.103.950-4'
SET work_370654cda985.type = 'Song'
SET work_370654cda985.wikidata = 'https://www.wikidata.org/wiki/Q4730061'
SET work_370654cda985.databases = ['https://castalbums.org/songs/All-of-You/10645/']
SET work_370654cda985.musicbrainz = 'https://musicbrainz.org/work/c9a51eb1-c80a-33e9-b015-370654cda985'
SET work_370654cda985.source = 'musicbrainz.org'
SET work_370654cda985.timestamp = timestamp()

MERGE (work_ad4a192fd542:Work{ uuid: '5894be54-19fa-3668-bb08-ad4a192fd542' })
SET work_ad4a192fd542.name = 'Like Someone in Love'
SET work_ad4a192fd542.iswc = 'T-070.095.943-8'
SET work_ad4a192fd542.type = 'Song'
SET work_ad4a192fd542.wikidata = 'https://www.wikidata.org/wiki/Q6547136'
SET work_ad4a192fd542.musicbrainz = 'https://musicbrainz.org/work/5894be54-19fa-3668-bb08-ad4a192fd542'
SET work_ad4a192fd542.source = 'musicbrainz.org'
SET work_ad4a192fd542.timestamp = timestamp()


// performances of
MERGE (perf_e60d2a08f1d7)-[:PERFORMANCE_OF]->(work_8748f890dd88)
MERGE (perf_6908b587ec84)-[:PERFORMANCE_OF]->(work_13a3125d3c19)
MERGE (perf_8e8bee805798)-[:PERFORMANCE_OF]->(work_0eeaedc04aac)
MERGE (perf_8e8bee805798)-[:PERFORMANCE_OF]->(work_0eeaedc04aac)
MERGE (perf_78084253f0dd)-[:PERFORMANCE_OF]->(work_1a76a8a20304)
MERGE (perf_1e3a191a1b14)-[:PERFORMANCE_OF]->(work_6126d682fab2)
MERGE (perf_a14739f64633)-[:PERFORMANCE_OF]->(work_aae7fa5e1564)
MERGE (perf_3250d56e0dea)-[:PERFORMANCE_OF]->(work_370654cda985)
MERGE (perf_22e504b1a7cd)-[:PERFORMANCE_OF]->(work_ad4a192fd542)


// composers
MERGE (person_75474f6dae9f)-[:COMPOSED]->(work_8748f890dd88)
MERGE (person_180c3283d2f9)-[:COMPOSED]->(work_8748f890dd88)
MERGE (person_668e586793d9)-[:COMPOSED]->(work_8748f890dd88)
MERGE (person_4f7500861060)-[:COMPOSED]->(work_13a3125d3c19)
MERGE (person_f6e8c16c7467)-[:WROTE_LYRICS]->(work_13a3125d3c19)
MERGE (person_7fd09c8ae291)-[:COMPOSED]->(work_0eeaedc04aac)
MERGE (person_5c6090f7ea1b)-[:WROTE_LYRICS]->(work_0eeaedc04aac)
MERGE (person_6565dc36a994)-[:COMPOSED]->(work_1a76a8a20304)
MERGE (person_14f95e6ce86d)-[:WROTE_LYRICS]->(work_1a76a8a20304)
MERGE (person_a37897b950ce)-[:COMPOSED]->(work_6126d682fab2)
MERGE (person_a37897b950ce)-[:WROTE_LYRICS]->(work_6126d682fab2)
MERGE (person_8eb400d9bcdc)-[:COMPOSED]->(work_aae7fa5e1564)
MERGE (person_955faa96931d)-[:WROTE_LYRICS]->(work_aae7fa5e1564)
MERGE (person_a37897b950ce)-[:COMPOSED]->(work_370654cda985)
MERGE (person_a37897b950ce)-[:WROTE_LYRICS]->(work_370654cda985)
MERGE (person_a6d92136636f)-[:COMPOSED]->(work_ad4a192fd542)
MERGE (person_8825529afd5d)-[:WROTE_LYRICS]->(work_ad4a192fd542)


// place nodes

MERGE (place_307a6414aae1:Place{ uuid: '8b641480-07b0-4234-9a6f-307a6414aae1' })
SET place_307a6414aae1.name = 'London House'
SET place_307a6414aae1.source = 'musicbrainz.org'


// place relationships
MERGE (perf_22e504b1a7cd)-[:HAS_PLACE { type: 'recorded at', begin: '1958-03-07', end: '1958-03-07' }]->(place_307a6414aae1)
MERGE (perf_e60d2a08f1d7)-[:HAS_PLACE { type: 'recorded at', begin: '1958-03-07', end: '1958-03-07' }]->(place_307a6414aae1)
MERGE (perf_a14739f64633)-[:HAS_PLACE { type: 'recorded at', begin: '1958-03-07', end: '1958-03-07' }]->(place_307a6414aae1)
MERGE (perf_8e8bee805798)-[:HAS_PLACE { type: 'recorded at', begin: '1958-03-07', end: '1958-03-07' }]->(place_307a6414aae1)
MERGE (perf_1e3a191a1b14)-[:HAS_PLACE { type: 'recorded at', begin: '1958-03-07', end: '1958-03-07' }]->(place_307a6414aae1)
MERGE (perf_6908b587ec84)-[:HAS_PLACE { type: 'recorded at', begin: '1958-03-07', end: '1958-03-07' }]->(place_307a6414aae1)
MERGE (perf_3250d56e0dea)-[:HAS_PLACE { type: 'recorded at', begin: '1958-03-07', end: '1958-03-07' }]->(place_307a6414aae1)
MERGE (perf_78084253f0dd)-[:HAS_PLACE { type: 'recorded at', begin: '1958-03-07', end: '1958-03-07' }]->(place_307a6414aae1)

MERGE (person_49233b3ea8cc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_22e504b1a7cd)
MERGE (person_18bed4c8a3b8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_22e504b1a7cd)
MERGE (person_6b794cb69f8c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_22e504b1a7cd)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_22e504b1a7cd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_22e504b1a7cd)
MERGE (person_1b6313c126ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_22e504b1a7cd)
MERGE (person_cdc2599bcba6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_22e504b1a7cd)
MERGE (person_49233b3ea8cc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e60d2a08f1d7)
MERGE (person_18bed4c8a3b8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_e60d2a08f1d7)
MERGE (person_6b794cb69f8c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_e60d2a08f1d7)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e60d2a08f1d7)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e60d2a08f1d7)
MERGE (person_1b6313c126ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_e60d2a08f1d7)
MERGE (person_cdc2599bcba6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_e60d2a08f1d7)
MERGE (person_49233b3ea8cc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a14739f64633)
MERGE (person_18bed4c8a3b8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_a14739f64633)
MERGE (person_6b794cb69f8c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_a14739f64633)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_a14739f64633)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a14739f64633)
MERGE (person_1b6313c126ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_a14739f64633)
MERGE (person_cdc2599bcba6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_a14739f64633)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_a14739f64633)
MERGE (person_49233b3ea8cc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8e8bee805798)
MERGE (person_18bed4c8a3b8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_8e8bee805798)
MERGE (person_6b794cb69f8c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_8e8bee805798)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_8e8bee805798)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_8e8bee805798)
MERGE (person_1b6313c126ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_8e8bee805798)
MERGE (person_cdc2599bcba6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_8e8bee805798)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_8e8bee805798)
MERGE (person_49233b3ea8cc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_1e3a191a1b14)
MERGE (person_18bed4c8a3b8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_1e3a191a1b14)
MERGE (person_6b794cb69f8c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_1e3a191a1b14)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_1e3a191a1b14)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_1e3a191a1b14)
MERGE (person_1b6313c126ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_1e3a191a1b14)
MERGE (person_cdc2599bcba6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_1e3a191a1b14)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_1e3a191a1b14)
MERGE (person_49233b3ea8cc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6908b587ec84)
MERGE (person_18bed4c8a3b8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_6908b587ec84)
MERGE (person_6b794cb69f8c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_6908b587ec84)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_6908b587ec84)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6908b587ec84)
MERGE (person_1b6313c126ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_6908b587ec84)
MERGE (person_cdc2599bcba6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_6908b587ec84)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_6908b587ec84)
MERGE (person_49233b3ea8cc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_3250d56e0dea)
MERGE (person_18bed4c8a3b8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_3250d56e0dea)
MERGE (person_6b794cb69f8c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_3250d56e0dea)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_3250d56e0dea)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_3250d56e0dea)
MERGE (person_1b6313c126ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_3250d56e0dea)
MERGE (person_cdc2599bcba6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_3250d56e0dea)
MERGE (person_49233b3ea8cc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_78084253f0dd)
MERGE (person_18bed4c8a3b8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_78084253f0dd)
MERGE (person_6b794cb69f8c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_78084253f0dd)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_78084253f0dd)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_78084253f0dd)
MERGE (person_1b6313c126ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_78084253f0dd)
MERGE (person_cdc2599bcba6)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_78084253f0dd)

