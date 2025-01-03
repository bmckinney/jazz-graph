// releases

MERGE (release_9c1d47c44167:Release{ uuid: '1f1db260-b8a2-4b95-9b5d-9c1d47c44167' })
SET release_9c1d47c44167.name = 'My Shining Hour'
SET release_9c1d47c44167.country = 'XW'
SET release_9c1d47c44167.date = '2020-02-05'
SET release_9c1d47c44167.format = 'Digital Media'
SET release_9c1d47c44167.musicbrainz = 'http://musicbrainz.org/release/1f1db260-b8a2-4b95-9b5d-9c1d47c44167'
SET release_9c1d47c44167.source = 'musicbrainz.org'
SET release_9c1d47c44167.timestamp = timestamp()

MERGE (person_c77a0041911d:Person{ uuid: '2bb8f4bc-d6e2-4a67-bdc9-c77a0041911d' }) 
SET person_c77a0041911d.name = 'Thomas Clausen'
SET person_c77a0041911d.gender = 'Male'
SET person_c77a0041911d.disambiguation = 'Danish jazz pianist'
SET person_c77a0041911d.country = 'DK'
SET person_c77a0041911d.allmusic = 'https://www.allmusic.com/artist/mn0000592059'
SET person_c77a0041911d.discogs = 'https://www.discogs.com/artist/315696'
SET person_c77a0041911d.imdb = 'https://www.imdb.com/name/nm2188680/'
SET person_c77a0041911d.viaf = 'http://viaf.org/viaf/27223529'
SET person_c77a0041911d.wikidata = 'https://www.wikidata.org/wiki/Q2423043'
SET person_c77a0041911d.databases = ['http://id.loc.gov/authorities/names/no2014043690', 'https://d-nb.info/gnd/13465563X', 'https://rateyourmusic.com/artist/thomas_clausen', 'https://www.worldcat.org/identities/lccn-no2014043690']
SET person_c77a0041911d.musicbrainz = 'https://musicbrainz.org/artist/2bb8f4bc-d6e2-4a67-bdc9-c77a0041911d'
SET person_c77a0041911d.isni_list = ['http://isni.org/isni/0000000072479947']
SET person_c77a0041911d.source = 'musicbrainz.org'
SET person_c77a0041911d.timestamp = timestamp()

MERGE (person_c816a5f43bda:Person{ uuid: '3a3cec56-8514-49a0-b676-c816a5f43bda' }) 
SET person_c816a5f43bda.name = 'Niels-Henning Ørsted Pedersen'
SET person_c816a5f43bda.gender = 'Male'
SET person_c816a5f43bda.disambiguation = 'Danish jazz upright bassist'
SET person_c816a5f43bda.country = 'DK'
SET person_c816a5f43bda.allmusic = 'https://www.allmusic.com/artist/mn0000404907'
SET person_c816a5f43bda.discogs = 'https://www.discogs.com/artist/285231'
SET person_c816a5f43bda.imdb = 'https://www.imdb.com/name/nm0669934/'
SET person_c816a5f43bda.viaf = 'http://viaf.org/viaf/114610990'
SET person_c816a5f43bda.wikidata = 'https://www.wikidata.org/wiki/Q520796'
SET person_c816a5f43bda.databases = ['http://id.loc.gov/authorities/names/n81024656', 'https://catalogue.bnf.fr/ark:/12148/cb138981210', 'https://d-nb.info/gnd/129965510', 'https://nla.gov.au/nla.party-1038474', 'https://www.musik-sammler.de/artist/niels-henning-oersted-pedersen/', 'https://www.worldcat.org/identities/lccn-n81024656']
SET person_c816a5f43bda.musicbrainz = 'https://musicbrainz.org/artist/3a3cec56-8514-49a0-b676-c816a5f43bda'
SET person_c816a5f43bda.isni_list = ['http://isni.org/isni/0000000084117257']
SET person_c816a5f43bda.source = 'musicbrainz.org'
SET person_c816a5f43bda.timestamp = timestamp()

MERGE (person_076b7ee0e707:Person{ uuid: 'a21f52c0-ad9e-49aa-bf1c-076b7ee0e707' }) 
SET person_076b7ee0e707.name = 'Tomas Franck'
SET person_076b7ee0e707.gender = 'Male'
SET person_076b7ee0e707.disambiguation = 'saxophone'
SET person_076b7ee0e707.country = 'SE'
SET person_076b7ee0e707.allmusic = 'https://www.allmusic.com/artist/mn0000511996'
SET person_076b7ee0e707.discogs = 'https://www.discogs.com/artist/1063390'
SET person_076b7ee0e707.viaf = 'http://viaf.org/viaf/53818859'
SET person_076b7ee0e707.wikidata = 'https://www.wikidata.org/wiki/Q2440389'
SET person_076b7ee0e707.databases = ['http://id.loc.gov/authorities/names/n2002054780', 'http://id.loc.gov/authorities/names/no2002054780', 'https://d-nb.info/gnd/134677412', 'https://www.worldcat.org/identities/lccn-n2002054780', 'https://www.worldcat.org/identities/lccn-no2002054780/']
SET person_076b7ee0e707.musicbrainz = 'https://musicbrainz.org/artist/a21f52c0-ad9e-49aa-bf1c-076b7ee0e707'
SET person_076b7ee0e707.isni_list = ['http://isni.org/isni/0000000041510251']
SET person_076b7ee0e707.source = 'musicbrainz.org'
SET person_076b7ee0e707.timestamp = timestamp()

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
SET person_6f0a331cc1ca.timestamp = timestamp()

// performances

MERGE (perf_16f97a365e51:Performance{ uuid: 'ff1b11e9-3215-463b-b0c4-16f97a365e51' })
SET perf_16f97a365e51.name = 'My Shining Hour'
SET perf_16f97a365e51.duration = '10:25'
SET perf_16f97a365e51.source = 'musicbrainz.org'
SET perf_16f97a365e51.timestamp = timestamp()

MERGE (perf_8c69306a0638:Performance{ uuid: '278a307e-d2e4-4354-83ef-8c69306a0638' })
SET perf_8c69306a0638.name = 'I Fall in Love Too Easily'
SET perf_8c69306a0638.duration = '6:21'
SET perf_8c69306a0638.source = 'musicbrainz.org'
SET perf_8c69306a0638.timestamp = timestamp()

MERGE (perf_a7ea4dced64f:Performance{ uuid: '2df5ce78-bfe2-43d6-9763-a7ea4dced64f' })
SET perf_a7ea4dced64f.name = 'Bessie\'s Blues'
SET perf_a7ea4dced64f.duration = '8:21'
SET perf_a7ea4dced64f.source = 'musicbrainz.org'
SET perf_a7ea4dced64f.timestamp = timestamp()

MERGE (perf_bc1ba22d76f3:Performance{ uuid: 'c8390cd9-7548-44f0-b10d-bc1ba22d76f3' })
SET perf_bc1ba22d76f3.name = 'All Blues'
SET perf_bc1ba22d76f3.duration = '10:52'
SET perf_bc1ba22d76f3.source = 'musicbrainz.org'
SET perf_bc1ba22d76f3.timestamp = timestamp()

MERGE (perf_67c2ec2d68d5:Performance{ uuid: '3d95db66-3007-4a71-8f2d-67c2ec2d68d5' })
SET perf_67c2ec2d68d5.name = 'Skylark'
SET perf_67c2ec2d68d5.duration = '8:42'
SET perf_67c2ec2d68d5.source = 'musicbrainz.org'
SET perf_67c2ec2d68d5.timestamp = timestamp()

MERGE (perf_81fe66a8cbcf:Performance{ uuid: '2ef8f50a-c18b-43a2-9c47-81fe66a8cbcf' })
SET perf_81fe66a8cbcf.name = 'Rhythm-A-Ning'
SET perf_81fe66a8cbcf.duration = '8:27'
SET perf_81fe66a8cbcf.source = 'musicbrainz.org'
SET perf_81fe66a8cbcf.timestamp = timestamp()

MERGE (perf_64f30ae3c684:Performance{ uuid: '4251155a-0bbe-4f95-8990-64f30ae3c684' })
SET perf_64f30ae3c684.name = 'A La Blues'
SET perf_64f30ae3c684.duration = '6:30'
SET perf_64f30ae3c684.source = 'musicbrainz.org'
SET perf_64f30ae3c684.timestamp = timestamp()

MERGE (perf_5012fbe30038:Performance{ uuid: '6abdbe02-59b8-43ad-95ba-5012fbe30038' })
SET perf_5012fbe30038.name = 'Bright/Roy Haynes\'s Statement of Aknowledgement'
SET perf_5012fbe30038.duration = '8:32'
SET perf_5012fbe30038.source = 'musicbrainz.org'
SET perf_5012fbe30038.timestamp = timestamp()


// tracks
MERGE (release_9c1d47c44167)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_16f97a365e51)
MERGE (release_9c1d47c44167)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_8c69306a0638)
MERGE (release_9c1d47c44167)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_a7ea4dced64f)
MERGE (release_9c1d47c44167)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_bc1ba22d76f3)
MERGE (release_9c1d47c44167)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_67c2ec2d68d5)
MERGE (release_9c1d47c44167)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_81fe66a8cbcf)
MERGE (release_9c1d47c44167)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_64f30ae3c684)
MERGE (release_9c1d47c44167)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_5012fbe30038)

// works

MERGE (person_2b3e7beaf00a:Person{ uuid: 'b342d50e-401c-4c77-b7e4-2b3e7beaf00a' }) 
SET person_2b3e7beaf00a.name = 'Johnny Mercer'
SET person_2b3e7beaf00a.gender = 'Male'
SET person_2b3e7beaf00a.country = 'US'
SET person_2b3e7beaf00a.allmusic = 'https://www.allmusic.com/artist/mn0000244406'
SET person_2b3e7beaf00a.bbc = 'https://www.bbc.co.uk/music/artists/b342d50e-401c-4c77-b7e4-2b3e7beaf00a'
SET person_2b3e7beaf00a.discogs = 'https://www.discogs.com/artist/164574'
SET person_2b3e7beaf00a.imdb = 'https://www.imdb.com/name/nm0006197/'
SET person_2b3e7beaf00a.viaf = 'http://viaf.org/viaf/79167222'
SET person_2b3e7beaf00a.wikidata = 'https://www.wikidata.org/wiki/Q363698'
SET person_2b3e7beaf00a.databases = ['http://id.loc.gov/authorities/names/n82078485', 'https://adp.library.ucsb.edu/names/103688', 'https://catalogue.bnf.fr/ark:/12148/cb138974071', 'https://d-nb.info/gnd/118801031', 'http://snaccooperative.org/ark:/99166/w65140xb', 'https://nla.gov.au/nla.party-1213050', 'http://soundtrackcollector.com/composer/3036/', 'https://rateyourmusic.com/artist/johnny_mercer', 'https://www.ibdb.com/person.php?id=12137', 'https://www.worldcat.org/identities/lccn-n82078485/']
SET person_2b3e7beaf00a.musicbrainz = 'https://musicbrainz.org/artist/b342d50e-401c-4c77-b7e4-2b3e7beaf00a'
SET person_2b3e7beaf00a.isni_list = ['http://isni.org/isni/0000000120183877']
SET person_2b3e7beaf00a.source = 'musicbrainz.org'
SET person_2b3e7beaf00a.timestamp = timestamp()

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
SET person_323e6ce46c2a.timestamp = timestamp()

MERGE (person_e6a00ac37491:Person{ uuid: '75f6fe4b-8a7a-4f3c-9232-e6a00ac37491' }) 
SET person_e6a00ac37491.name = 'Hoagy Carmichael'
SET person_e6a00ac37491.gender = 'Male'
SET person_e6a00ac37491.country = 'US'
SET person_e6a00ac37491.allmusic = 'https://www.allmusic.com/artist/mn0000708613'
SET person_e6a00ac37491.discogs = 'https://www.discogs.com/artist/301368'
SET person_e6a00ac37491.imdb = 'https://www.imdb.com/name/nm0005994/'
SET person_e6a00ac37491.viaf = 'http://viaf.org/viaf/116045429'
SET person_e6a00ac37491.wikidata = 'https://www.wikidata.org/wiki/Q460662'
SET person_e6a00ac37491.databases = ['http://id.loc.gov/authorities/names/n50032462', 'https://adp.library.ucsb.edu/names/102001', 'https://catalogue.bnf.fr/ark:/12148/cb13892178h', 'https://d-nb.info/gnd/124217184', 'https://ibdb.com/person.php?id=11490', 'http://snaccooperative.org/ark:/99166/w6sx6mkm', 'https://nla.gov.au/nla.party-1060823', 'https://openlibrary.org/works/OL239165A', 'https://rateyourmusic.com/artist/hoagy_carmichael', 'https://www.worldcat.org/identities/lccn-n50032462']
SET person_e6a00ac37491.musicbrainz = 'https://musicbrainz.org/artist/75f6fe4b-8a7a-4f3c-9232-e6a00ac37491'
SET person_e6a00ac37491.isni_list = ['http://isni.org/isni/0000000081847887']
SET person_e6a00ac37491.source = 'musicbrainz.org'
SET person_e6a00ac37491.timestamp = timestamp()

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
SET person_72ad46cdb831.timestamp = timestamp()

MERGE (work_fdfbe022ae91:Work{ uuid: '40123b58-fcfb-39ab-884a-fdfbe022ae91' })
SET work_fdfbe022ae91.name = 'Skylark'
SET work_fdfbe022ae91.iswc = 'T-070.135.891-9'
SET work_fdfbe022ae91.type = 'Song'
SET work_fdfbe022ae91.wikidata = 'https://www.wikidata.org/wiki/Q7537823'
SET work_fdfbe022ae91.musicbrainz = 'https://musicbrainz.org/work/40123b58-fcfb-39ab-884a-fdfbe022ae91'
SET work_fdfbe022ae91.source = 'musicbrainz.org'
SET work_fdfbe022ae91.timestamp = timestamp()

MERGE (work_16aafec65e2d:Work{ uuid: '57a7cb80-55cd-352a-b5ed-16aafec65e2d' })
SET work_16aafec65e2d.name = 'Bessie\'s Blues'
SET work_16aafec65e2d.iswc = 'T-070.232.974-5'
SET work_16aafec65e2d.type = 'Song'
SET work_16aafec65e2d.allmusic = 'https://www.allmusic.com/song/mt0009518223'
SET work_16aafec65e2d.musicbrainz = 'https://musicbrainz.org/work/57a7cb80-55cd-352a-b5ed-16aafec65e2d'
SET work_16aafec65e2d.source = 'musicbrainz.org'
SET work_16aafec65e2d.timestamp = timestamp()

MERGE (work_1938072b1375:Work{ uuid: '46e6bfc3-5f37-3e6e-a2be-1938072b1375' })
SET work_1938072b1375.name = 'All Blues'
SET work_1938072b1375.iswc = 'T-039.266.451-5'
SET work_1938072b1375.type = 'Song'
SET work_1938072b1375.wikidata = 'https://www.wikidata.org/wiki/Q2600918'
SET work_1938072b1375.musicbrainz = 'https://musicbrainz.org/work/46e6bfc3-5f37-3e6e-a2be-1938072b1375'
SET work_1938072b1375.source = 'musicbrainz.org'
SET work_1938072b1375.timestamp = timestamp()


// performances of
MERGE (perf_67c2ec2d68d5)-[:PERFORMANCE_OF]->(work_fdfbe022ae91)
MERGE (perf_a7ea4dced64f)-[:PERFORMANCE_OF]->(work_16aafec65e2d)
MERGE (perf_bc1ba22d76f3)-[:PERFORMANCE_OF]->(work_1938072b1375)


// composers
MERGE (person_e6a00ac37491)-[:COMPOSED]->(work_fdfbe022ae91)
MERGE (person_2b3e7beaf00a)-[:WROTE_LYRICS]->(work_fdfbe022ae91)
MERGE (person_72ad46cdb831)-[:COMPOSED]->(work_16aafec65e2d)
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_1938072b1375)

MERGE (person_c77a0041911d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_16f97a365e51)
MERGE (person_076b7ee0e707)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_16f97a365e51)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_16f97a365e51)
MERGE (person_c816a5f43bda)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_16f97a365e51)
MERGE (person_c77a0041911d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8c69306a0638)
MERGE (person_076b7ee0e707)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_8c69306a0638)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_8c69306a0638)
MERGE (person_c816a5f43bda)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_8c69306a0638)
MERGE (person_c77a0041911d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a7ea4dced64f)
MERGE (person_076b7ee0e707)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_a7ea4dced64f)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_a7ea4dced64f)
MERGE (person_c816a5f43bda)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_a7ea4dced64f)
MERGE (person_c77a0041911d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bc1ba22d76f3)
MERGE (person_076b7ee0e707)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_bc1ba22d76f3)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_bc1ba22d76f3)
MERGE (person_c816a5f43bda)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_bc1ba22d76f3)
MERGE (person_c77a0041911d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_67c2ec2d68d5)
MERGE (person_076b7ee0e707)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_67c2ec2d68d5)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_67c2ec2d68d5)
MERGE (person_c816a5f43bda)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_67c2ec2d68d5)
MERGE (person_c77a0041911d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_81fe66a8cbcf)
MERGE (person_076b7ee0e707)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_81fe66a8cbcf)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_81fe66a8cbcf)
MERGE (person_c816a5f43bda)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_81fe66a8cbcf)
MERGE (person_c77a0041911d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_64f30ae3c684)
MERGE (person_076b7ee0e707)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_64f30ae3c684)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_64f30ae3c684)
MERGE (person_c816a5f43bda)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_64f30ae3c684)
MERGE (person_c77a0041911d)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5012fbe30038)
MERGE (person_076b7ee0e707)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_5012fbe30038)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_5012fbe30038)
MERGE (person_c816a5f43bda)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_5012fbe30038)

