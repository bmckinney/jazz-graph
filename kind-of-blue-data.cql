// ---------------------------------------------------------------------------------
// ----- NODES ---------------------------------------------------------------------
// ---------------------------------------------------------------------------------

// artists
MERGE
(artist_323e6ce46c2a:Artist{
	name: 'Miles Davis',
	gender: 'Male',
	sort_name: 'Davis, Miles',
	disambiguation: 'jazz trumpeter, bandleader, songwriter',
	country: 'US',
	birth_date: '1926-05-26',
	death_date: '1991-09-28',
	aliases: ['Miles Davies', 'Miles Dewey Davis III.', 'Miles Favis'],
	tags: ['bebop', 'cool jazz', 'hard bop', 'jazz', 'jazz fusion', 'modal jazz'],
	wikipedia: 'http://en.wikipedia.org/wiki/Miles_Davis',
	viaf: 'http://viaf.org/viaf/97762193',
	allmusic: 'http://www.allmusic.com/artist/mn0000423829',
	bbc: 'http://www.bbc.co.uk/music/artists/561d854a-6a28-4aa7-8c99-323e6ce46c2a',
	discogs: 'http://www.discogs.com/artist/23755',
	imdb: 'http://www.imdb.com/name/nm0002537/',
	wikidata: 'http://www.wikidata.org/wiki/Q93341',
	discographies: ['http://all-blues.de/music/missing.htm', 'http://en.wikipedia.org/wiki/Miles_Davis_discography', 'http://www.plosin.com/milesahead/'],
	databases: ['http://musicmoz.org/Bands_and_Artists/D/Davis,_Miles/', 'http://rateyourmusic.com/artist/miles_davis'],
	musicbrainz: 'https://musicbrainz.org/artist/561d854a-6a28-4aa7-8c99-323e6ce46c2a',
	isni: 'http://isni.org/isni/000000012144707X',
	uuid: '561d854a-6a28-4aa7-8c99-323e6ce46c2a'
})
MERGE
(artist_2fe1f9f27da8:Artist{
	name: 'Cannonball Adderley',
	gender: 'Male',
	sort_name: 'Adderley, Cannonball',
	country: 'US',
	birth_date: '1928-09-15',
	death_date: '1975-08-08',
	aliases: ['Cannonball Adderly', 'CannonballAdderley', 'Julian "Cannonball" Adderley', 'Julian Adderley', 'Julian Cannonball Adderley', 'Julian Cannonball Adderly'],
	wikipedia: 'http://en.wikipedia.org/wiki/Cannonball_Adderley',
	viaf: 'http://viaf.org/viaf/36906016',
	allmusic: 'http://www.allmusic.com/artist/mn0000548338',
	discogs: 'http://www.discogs.com/artist/61585',
	wikidata: 'http://www.wikidata.org/wiki/Q110477',
	discographies: ['http://jazzdisco.org/adderley/', 'http://www.cannonball-adderley.com/'],
	databases: ['https://rateyourmusic.com/artist/cannonball_adderley'],
	musicbrainz: 'https://musicbrainz.org/artist/a4c73ebe-b2c7-4f13-b99d-2fe1f9f27da8',
	uuid: 'a4c73ebe-b2c7-4f13-b99d-2fe1f9f27da8'
})
MERGE
(artist_72ad46cdb831:Artist{
	name: 'John Coltrane',
	gender: 'Male',
	sort_name: 'Coltrane, John',
	country: 'US',
	birth_date: '1926-09-23',
	death_date: '1967-07-17',
	aliases: ['John Coltraine', 'John William Coltrane', 'Trane'],
	tags: ['american', 'avant-garde jazz', 'free jazz', 'hard bop', 'jazz', 'modal jazz'],
	wikipedia: 'http://en.wikipedia.org/wiki/John_Coltrane',
	viaf: 'http://viaf.org/viaf/61731379',
	allmusic: 'http://www.allmusic.com/artist/mn0000175553',
	bbc: 'http://www.bbc.co.uk/music/artists/b625448e-bf4a-41c3-a421-72ad46cdb831',
	discogs: 'http://www.discogs.com/artist/97545',
	wikidata: 'http://www.wikidata.org/wiki/Q7346',
	discographies: ['http://www.mossiehigh.com/Coltrane/Main.htm'],
	databases: ['http://d-nb.info/gnd/118521667', 'http://rateyourmusic.com/artist/john_coltrane', 'http://www.whosampled.com/John-Coltrane/', 'https://www.musik-sammler.de/artist/john-coltrane/', 'https://www.worldcat.org/identities/lccn-n50-031907'],
	musicbrainz: 'https://musicbrainz.org/artist/b625448e-bf4a-41c3-a421-72ad46cdb831',
	isni: 'http://isni.org/isni/000000012280792X',
	uuid: 'b625448e-bf4a-41c3-a421-72ad46cdb831'
})
MERGE
(artist_13d821490e42:Artist{
	name: 'Wynton Kelly',
	gender: 'Male',
	sort_name: 'Kelly, Wynton',
	country: 'US',
	birth_date: '1931-12-02',
	death_date: '1971-04-12',
	wikipedia: 'http://en.wikipedia.org/wiki/Wynton_Kelly',
	viaf: 'http://viaf.org/viaf/29718356',
	allmusic: 'http://www.allmusic.com/artist/mn0000684253',
	discogs: 'http://www.discogs.com/artist/252308',
	imdb: 'http://www.imdb.com/name/nm4017040/',
	wikidata: 'http://www.wikidata.org/wiki/Q536415',
	musicbrainz: 'https://musicbrainz.org/artist/d3f9352c-18e2-47a0-802c-13d821490e42',
	uuid: 'd3f9352c-18e2-47a0-802c-13d821490e42'
})
MERGE
(artist_6c57b03a4e36:Artist{
	name: 'Bill Evans',
	gender: 'Male',
	sort_name: 'Evans, Bill',
	disambiguation: 'pianist',
	country: 'US',
	birth_date: '1929-08-16',
	death_date: '1980-09-15',
	tags: ['jazz'],
	wikipedia: 'http://en.wikipedia.org/wiki/Bill_Evans',
	viaf: 'http://viaf.org/viaf/29717820',
	allmusic: 'http://www.allmusic.com/artist/mn0000764702',
	bbc: 'http://www.bbc.co.uk/music/artists/8247a3f2-3a8e-4256-b322-6c57b03a4e36',
	discogs: 'http://www.discogs.com/artist/252310',
	imdb: 'http://www.imdb.com/name/nm0262572/',
	wikidata: 'http://www.wikidata.org/wiki/Q208205',
	discographies: ['http://www.jazztet.com/BillEvans/BillEvans-1.htm'],
	databases: ['http://d-nb.info/gnd/137724519', 'http://www.whosampled.com/Bill-Evans/', 'https://rateyourmusic.com/artist/bill_evans', 'https://www.musik-sammler.de/artist/175764/', 'https://www.worldcat.org/identities/lccn-n81-147281'],
	musicbrainz: 'https://musicbrainz.org/artist/8247a3f2-3a8e-4256-b322-6c57b03a4e36',
	isni: 'http://isni.org/isni/0000000121261603',
	uuid: '8247a3f2-3a8e-4256-b322-6c57b03a4e36'
})
MERGE
(artist_7de13124b970:Artist{
	name: 'Paul Chambers',
	gender: 'Male',
	sort_name: 'Chambers, Paul',
	disambiguation: 'US jazz bassist',
	country: 'US',
	birth_date: '1935-04-22',
	death_date: '1969-01-04',
	wikipedia: 'http://en.wikipedia.org/wiki/Paul_Chambers',
	viaf: 'http://viaf.org/viaf/100313280',
	discogs: 'http://www.discogs.com/artist/259778',
	wikidata: 'http://www.wikidata.org/wiki/Q541659',
	musicbrainz: 'https://musicbrainz.org/artist/b6ff4fd0-03ae-41a6-942e-7de13124b970',
	uuid: 'b6ff4fd0-03ae-41a6-942e-7de13124b970'
})
MERGE
(artist_fe2cd264bbd0:Artist{
	name: 'Jimmy Cobb',
	gender: 'Male',
	sort_name: 'Cobb, Jimmy',
	country: 'US',
	birth_date: '1929-01-20',
	aliases: ['James Cobb'],
	wikipedia: 'http://en.wikipedia.org/wiki/Jimmy_Cobb',
	viaf: 'http://viaf.org/viaf/85107638',
	allmusic: 'http://www.allmusic.com/artist/mn0000350892',
	discogs: 'http://www.discogs.com/artist/252311',
	wikidata: 'http://www.wikidata.org/wiki/Q499491',
	musicbrainz: 'https://musicbrainz.org/artist/d0cbf65a-541b-476a-996c-fe2cd264bbd0',
	uuid: 'd0cbf65a-541b-476a-996c-fe2cd264bbd0'
})
MERGE
(artist_c69b63044dd6:Artist{
	name: 'Gil Evans',
	gender: 'Male',
	sort_name: 'Evans, Gil',
	country: 'US',
	birth_date: '1912-05-13',
	death_date: '1988-03-20',
	wikipedia: 'http://en.wikipedia.org/wiki/Gil_Evans',
	viaf: 'http://viaf.org/viaf/7573806',
	allmusic: 'http://www.allmusic.com/artist/mn0000551815',
	bbc: 'http://www.bbc.co.uk/music/artists/83b1d510-c4ae-485b-91bf-c69b63044dd6',
	discogs: 'http://www.discogs.com/artist/255137',
	wikidata: 'http://www.wikidata.org/wiki/Q348477',
	musicbrainz: 'https://musicbrainz.org/artist/83b1d510-c4ae-485b-91bf-c69b63044dd6',
	isni: 'http://isni.org/isni/0000000368575102',
	uuid: '83b1d510-c4ae-485b-91bf-c69b63044dd6'
})
MERGE
(artist_d5fead5a7988:Artist{
	name: 'Teo Macero',
	gender: 'Male',
	sort_name: 'Macero, Teo',
	country: 'US',
	birth_date: '1925-10-30',
	death_date: '2008-02-19',
	wikipedia: 'http://en.wikipedia.org/wiki/Teo_Macero',
	viaf: 'http://viaf.org/viaf/32185295',
	allmusic: 'http://www.allmusic.com/artist/mn0000020762',
	discogs: 'http://www.discogs.com/artist/237977',
	imdb: 'http://www.imdb.com/name/nm0532163/',
	wikidata: 'http://www.wikidata.org/wiki/Q265494',
	musicbrainz: 'https://musicbrainz.org/artist/64e2e449-234c-480d-89d3-d5fead5a7988',
	uuid: '64e2e449-234c-480d-89d3-d5fead5a7988'
})
MERGE
(artist_f35080d12d60:Artist{
	name: 'Irving Townsend',
	gender: 'Male',
	sort_name: 'Townsend, Irving',
	country: 'US',
	birth_date: '1920',
	death_date: '1981',
	discogs: 'http://www.discogs.com/artist/239628',
	wikipedia: 'https://en.wikipedia.org/wiki/Irving_Townsend',
	wikidata: 'https://www.wikidata.org/wiki/Q6074822',
	musicbrainz: 'https://musicbrainz.org/artist/5ca16cfc-f480-4203-93e7-f35080d12d60',
	uuid: '5ca16cfc-f480-4203-93e7-f35080d12d60'
})
MERGE
(artist_084c872be8e5:Artist{
	name: 'Fred Plaut',
	sort_name: 'Plaut, Fred',
	gender: 'Male',
	country: 'DE',
	birth_date: '1907-05-12',
	death_date: '1985-06',
	wikipedia: 'https://en.wikipedia.org/wiki/Fred_Plaut',
	viaf: 'https://viaf.org/viaf/44566177/',
	isni: 'http://isni-url.oclc.nl/isni/0000000114715435',
	uuid: 'febc30e8-5033-4c65-b25c-084c872be8e5'
})

// other
MERGE
(artist_98c032bfe986:Artist{
	uuid:'48d3c6e4-cb6e-48a8-8b3b-98c032bfe986',
	name:'Robert Herridge',
	sort_name: 'Herridge, Robert',
	gender: 'Male',
	country: 'US',
	birth_date: '1914-01-12',
	death_date: '1981-08-14',
	wikipedia: 'https://en.wikipedia.org/wiki/Robert_Herridge',
	imdb: 'http://www.imdb.com/name/nm1055561/',
	viaf: 'http://viaf.org/viaf/97144648487392445628',
	wikidata: 'https://www.wikidata.org/wiki/Q7345465'
})

// works
MERGE
(work_3a7d6599a72e:Work{
	name: 'So What',
	iswc: 'T-900.305.844-4',
	type: 'Song',
	wikidata: 'http://www.wikidata.org/wiki/Q919291',
	musicbrainz: 'https://musicbrainz.org/work/2fafd730-423f-342e-b6c7-3a7d6599a72e',
	uuid: '2fafd730-423f-342e-b6c7-3a7d6599a72e'
})
MERGE
(perf_56f120ba125d:Performance{
	name: 'So What',
	disambiguation: '2013 stereo remix',
	duration: '9:08',
	uuid: '14ff2bb3-d0fd-4a8a-b697-56f120ba125d'
})
MERGE
(perf_9fe886723889:Performance{
	name: 'So What',
	disambiguation: 'first speed-correct stereo remix',
	duration: '9:25',
	uuid: '1930bfe4-0d3b-4b1c-abda-9fe886723889'
})
MERGE
(perf_0396774f77e9:Performance{
	name: 'So What',
	disambiguation: 'original mono studio mix',
	duration: '9:05',
	uuid: '23db7f43-d015-40f2-adb3-0396774f77e9'
})
MERGE
(perf_627ff0588a73:Performance{
	name: 'So What',
	disambiguation: 'studio session, 1959-3-2: Columbia Studios, NY, US',
	duration: '9:23',
	uuid: '272dbf93-1501-4650-bbde-627ff0588a73'
})
MERGE
(perf_374d6a433e46:Performance{
	name: 'So What!',
	duration: '5:32',
	uuid: '286f9582-96a6-4ebe-ae00-374d6a433e46'
})
MERGE
(perf_ea9246336782:Performance{
	name: 'So What',
	duration: '9:47',
	uuid: '2cbda1b8-49e5-45c4-bcb5-ea9246336782'
})
MERGE
(perf_5d9812a293ae:Performance{
	name: 'So What',
	duration: '7:45',
	uuid: '55496add-fada-419e-8036-5d9812a293ae'
})
MERGE
(perf_ab022f027ca5:Performance{
	name: 'So What',
	duration: '2:41',
	uuid: '56619545-5724-4365-b4d5-ab022f027ca5'
})
MERGE
(perf_44a8a638e360:Performance{
	name: 'So What',
	duration: '10:02',
	uuid: '58f1c9a4-c108-4d4f-832e-44a8a638e360'
})
MERGE
(perf_fa7b9a0948e3:Performance{
	name: 'So What',
	duration: '9:23',
	uuid: '5df1af65-b443-4127-a483-fa7b9a0948e3'
})
MERGE
(perf_905334c9a48a:Performance{
	name: 'So What',
	disambiguation: 'original stereo studio master',
	duration: '9:05',
	uuid: '60f750f4-d222-46b7-ad5c-905334c9a48a'
})
MERGE
(perf_e5eb02e4779c:Performance{
	name: 'So What',
	duration: '9:26',
	uuid: '614e2800-f17c-45c3-9449-e5eb02e4779c'
})
MERGE
(perf_890f9dc95d12:Performance{
	name: 'So What',
	duration: '9:19',
	uuid: '693cdb96-e0bc-45e8-ae7b-890f9dc95d12'
})
MERGE
(perf_f377a1549f41:Performance{
	name: 'So What',
	duration: '3:30',
	uuid: '6e75f9ca-dae4-4077-a135-f377a1549f41'
})
MERGE
(perf_75a8471af82d:Performance{
	name: 'So What! (Tuff \'n\' Smooth mix)',
	duration: '5:12',
	uuid: '71e01be7-6082-408f-8b9a-75a8471af82d'
})
MERGE
(perf_e5b27315070a:Performance{
	name: 'So What',
	duration: '6:11',
	uuid: '85ff4115-0940-49c0-ab6b-e5b27315070a'
})
MERGE
(perf_4de574c23bf2:Performance{
	name: 'So What',
	duration: '7:21',
	uuid: '87b26e8a-a5be-4354-8504-4de574c23bf2'
})
MERGE
(perf_a87489f4edfb:Performance{
	name: 'So What!/Teen Town',
	duration: '13:51',
	uuid: '8ba2ea31-557d-48c6-8e25-a87489f4edfb'
})
MERGE
(perf_2e30e1f11898:Performance{
	name: 'So What',
	duration: '8:58',
	uuid: '8cbab19b-d251-41aa-b9a2-2e30e1f11898'
})
MERGE
(perf_550dac9b606f:Performance{
	name: 'So What',
	duration: '5:55',
	uuid: 'a1e84a9e-3769-40d1-ab1e-550dac9b606f'
})
MERGE
(perf_3512576e7867:Performance{
	name: 'So What',
	duration: '9:00',
	uuid: 'a7ba3bc1-3068-4734-8264-3512576e7867'
})
MERGE
(perf_c9fb07026b93:Performance{
	name: 'So What',
	duration: '10:13',
	uuid: 'b4e409f2-1f54-412f-8936-c9fb07026b93'
})
MERGE
(perf_f2e5773f2904:Performance{
	name: 'So What',
	duration: '10:33',
	uuid: 'be1d6f97-9046-4071-a1ff-f2e5773f2904'
})
MERGE
(perf_cb0f58ab49f3:Performance{
	name: 'So What',
	duration: '5:08',
	uuid: 'c4abb56f-151c-4aeb-9833-cb0f58ab49f3'
})
MERGE
(perf_878d54026449:Performance{
	name: 'So what!',
	duration: '10:52',
	uuid: 'c53b410a-d14a-463c-a651-878d54026449'
})
MERGE
(perf_65d639180437:Performance{
	name: 'So What',
	duration: '5:24',
	uuid: 'c63cc74c-b7d3-4500-82b6-65d639180437'
})
MERGE
(perf_666f12d5883e:Performance{
	name: 'So What',
	duration: '7:36',
	uuid: 'd699c3d8-cf6d-48ab-ac5f-666f12d5883e'
})
MERGE
(perf_678f890b4f82:Performance{
	name: 'So What',
	duration: '11:09',
	uuid: 'd97c37ac-503b-471c-9d08-678f890b4f82'
})
MERGE
(perf_ea3680ebf325:Performance{
	name: 'So What',
	duration: '10:23',
	uuid: 'dbc6465c-60a3-4079-ae55-ea3680ebf325'
})
MERGE
(perf_f2314bc256a0:Performance{
	name: 'So What',
	duration: '5:53',
	uuid: 'e559d6a7-10d8-454d-8f2e-f2314bc256a0'
})
MERGE
(perf_2e80ae99583e:Performance{
	name: 'So What',
	disambiguation: '2013 mono remix',
	duration: '9:08',
	uuid: 'e8b51ade-5ff7-4906-8db3-2e80ae99583e'
})
MERGE
(perf_70f195a3a251:Performance{
	name: 'So What',
	disambiguation: 'live, 1960-04-08: Kongresshaus, Zürich, Switzerland',
	duration: '15:24',
	uuid: 'eb90c778-f6ba-4a09-ae3e-70f195a3a251'
})
MERGE
(work_382bacca0923:Work{
	name: 'Freddie Freeloader',
	uuid: '500ecdf1-a82e-3afc-9268-382bacca0923'
})
MERGE
(perf_a06ef88ca8a7:Performance{
	name: 'Freddie Freeloader',
	duration: '5:41',
	uuid: '0160e55d-549e-436a-889a-a06ef88ca8a7'
})
MERGE
(perf_2396a6961083:Performance{
	name: 'Freddie Freeloader',
	disambiguation: 'original mono studio mix',
	duration: '9:35',
	uuid: '0bdecbca-403a-4f0b-9aa2-2396a6961083'
})
MERGE
(perf_77005243e0ae:Performance{
	name: 'Freddie Freeloader',
	duration: '7:37',
	uuid: '1facebf0-e90d-4a0c-b7fb-77005243e0ae'
})
MERGE
(perf_6f43bda625cf:Performance{
	name: 'Freddie Freeloader',
	duration: '9:33',
	uuid: '5d604342-0bdb-4a4e-b52e-6f43bda625cf'
})
MERGE
(perf_117ef9da73f6:Performance{
	name: 'Freddie Freeloader',
	duration: '6:33',
	uuid: '65c793e7-2b21-4b74-8ab2-117ef9da73f6'
})
MERGE
(perf_7b864e366803:Performance{
	name: 'Freddie Freeloader',
	disambiguation: 'first speed-correct stereo remix',
	duration: '9:49',
	uuid: '6ea17013-fa68-4446-a2c7-7b864e366803'
})
MERGE
(perf_86d6e973196f:Performance{
	name: 'Freddie Freeloader',
	disambiguation: 'original stereo studio master',
	duration: '9:35',
	uuid: '852bf62a-29f9-4026-abc5-86d6e973196f'
})
MERGE
(perf_563d9a227e7e:Performance{
	name: 'Freddie Freeloader',
	disambiguation: '2013 mono remix',
	duration: '9:48',
	uuid: '8c25ec38-cc1f-48fc-9142-563d9a227e7e'
})
MERGE
(perf_4fd96a938857:Performance{
	name: 'Freddie Freeloader',
	disambiguation: '2013 stereo remix',
	duration: '9:48',
	uuid: 'b0e9bb7e-53b7-4c6c-b7ba-4fd96a938857'
})
MERGE
(perf_73b11087a1d5:Performance{
	name: 'Freddie Freelader',
	duration: '5:14',
	uuid: 'b5e794f5-0648-4a68-b546-73b11087a1d5'
})
MERGE
(perf_995f83279a4e:Performance{
	name: 'Freddie Freeloader (take 3)',
	duration: '7:48',
	uuid: 'c11d6487-39e0-48ae-a0d9-995f83279a4e'
})
MERGE
(perf_2bbc58c4e013:Performance{
	name: 'Freddie Freeloader',
	duration: '5:38',
	uuid: 'e3c441ff-d6f6-4d9b-9e6b-2bbc58c4e013'
})
MERGE
(perf_df0f1c1b8c5f:Performance{
	name: 'Freddie Freeloader',
	duration: '6:50',
	uuid: 'f57de4d9-35a0-44ce-99ca-df0f1c1b8c5f'
})
MERGE
(perf_6a08b1fc829b:Performance{
	name: 'Freddie Freeloader',
	duration: '8:33',
	uuid: 'f940878d-b471-48fc-8bf2-6a08b1fc829b'
})
MERGE
(perf_5a1a9bb5204f:Performance{
	name: 'Freddie Freeloader',
	duration: '5:51',
	uuid: 'fa8bfd84-9be2-4299-9877-5a1a9bb5204f'
})
MERGE
(work_d7943efb9a03:Work{
	name: 'Blue in Green',
	type: 'Song',
	wikidata: 'http://www.wikidata.org/wiki/Q510852',
	musicbrainz: 'https://musicbrainz.org/work/54d591f2-e928-3263-b963-d7943efb9a03',
	uuid: '54d591f2-e928-3263-b963-d7943efb9a03'
})
MERGE
(perf_e1e3224858d5:Performance{
	name: 'Blue in Green',
	duration: '5:06',
	uuid: '1112349e-a8e5-4509-b282-e1e3224858d5'
})
MERGE
(perf_7d35a60f9894:Performance{
	name: 'Blue in Green',
	disambiguation: '2013 mono remix',
	duration: '5:36',
	uuid: '1180d3de-ae1d-4ef0-a1bf-7d35a60f9894'
})
MERGE
(perf_899641dc3ef4:Performance{
	name: 'Blue in Green',
	duration: '7:27',
	uuid: '19ef80f1-47a1-47e7-a0c5-899641dc3ef4'
})
MERGE
(perf_0a121eface86:Performance{
	name: 'Blue in Green',
	duration: '5:32',
	uuid: '1f50e274-6e0c-461b-afc3-0a121eface86'
})
MERGE
(perf_16c93ebdbe28:Performance{
	name: 'Blue in Green',
	duration: '4:09',
	uuid: '208c6308-6410-4abd-a964-16c93ebdbe28'
})
MERGE
(perf_acab7145713d:Performance{
	name: 'Blue in Green',
	duration: '3:40',
	uuid: '264c15af-736c-4767-8fb9-acab7145713d'
})
MERGE
(perf_f67d6df000a0:Performance{
	name: 'Blue in Green',
	duration: '6:33',
	uuid: '2c0164c5-b54a-42ae-9bcc-f67d6df000a0'
})
MERGE
(perf_1696e1b62128:Performance{
	name: 'Blue in Green',
	duration: '3:30',
	uuid: '372d4657-548f-43df-a0d8-1696e1b62128'
})
MERGE
(perf_ed4ff735a34a:Performance{
	name: 'Blue in Green',
	duration: '5:26',
	uuid: '40b7e9a7-8dba-4d59-afce-ed4ff735a34a'
})
MERGE
(perf_05741c5ebac7:Performance{
	name: 'Blue in Green',
	duration: '5:06',
	uuid: '43ed8289-6c8a-4915-b539-05741c5ebac7'
})
MERGE
(perf_e5526f650010:Performance{
	name: 'Blue in Green',
	duration: '9:16',
	uuid: '5160af15-c281-4665-b954-e5526f650010'
})
MERGE
(perf_9eace7e208f2:Performance{
	name: 'Blue in Green',
	disambiguation: 'studio session, 3-2-1959: Columbia Studio, New York, US',
	duration: '5:28',
	uuid: '67a9794c-153a-4a24-82ec-9eace7e208f2'
})
MERGE
(perf_155daa25751b:Performance{
	name: 'Blue in Green',
	duration: '2:47',
	uuid: '7084d0d2-7921-40c5-b4b2-155daa25751b'
})
MERGE
(perf_95a0ef477189:Performance{
	name: 'Blue In Green',
	duration: '4:11',
	uuid: '77ad7edd-7cd4-40c4-ba24-95a0ef477189'
})
MERGE
(perf_0404f1f15b78:Performance{
	name: 'Blue in Green',
	disambiguation: 'first speed-correct stereo remix',
	duration: '5:37',
	uuid: '8121ce09-135d-477d-aafb-0404f1f15b78'
})
MERGE
(perf_e46312ee1150:Performance{
	name: 'Blue in Green',
	duration: '8:05',
	uuid: '847a2d81-64f1-49d4-8002-e46312ee1150'
})
MERGE
(perf_cf3a1c9376ec:Performance{
	name: 'Blue in Green',
	duration: '5:26',
	uuid: '9a7fffbe-2624-44cc-bcef-cf3a1c9376ec'
})
MERGE
(perf_b82de3cfa632:Performance{
	name: 'Blue in Green',
	duration: '4:39',
	uuid: 'a8946ee3-158e-482e-a37d-b82de3cfa632'
})
MERGE
(perf_af9ff95b97da:Performance{
	name: 'Blue In Green',
	duration: '5:33',
	uuid: 'b82778ad-a0ae-4dfa-84f4-af9ff95b97da'
})
MERGE
(perf_cf671462f29e:Performance{
	name: 'Blue in Green',
	duration: '8:08',
	uuid: 'bcca891b-bc42-4e08-89e0-cf671462f29e'
})
MERGE
(perf_4bb97553ae89:Performance{
	name: 'Blue in Green',
	duration: '4:11',
	uuid: 'bddfbbc8-1be0-4b90-9405-4bb97553ae89'
})
MERGE
(perf_1a1c24d4be26:Performance{
	name: 'Blue in Green',
	uuid: 'cad56c05-c716-4e97-ba8b-1a1c24d4be26'
})
MERGE
(perf_a94415e9d27d:Performance{
	name: 'Blue in Green',
	duration: '2:40',
	uuid: 'd49a06c0-dff0-4e5f-8013-a94415e9d27d'
})
MERGE
(perf_ad1fabaa0670:Performance{
	name: 'Blue in Green',
	duration: '6:13',
	uuid: 'd988a76d-6dd7-428e-886a-ad1fabaa0670'
})
MERGE
(perf_08ed20598107:Performance{
	name: 'Blue in Green',
	disambiguation: '2013 stereo remix',
	duration: '5:36',
	uuid: 'e7355307-97c9-4dd9-9946-08ed20598107'
})
MERGE
(perf_0a208b51d653:Performance{
	name: 'Blue in Green',
	duration: '4:04',
	uuid: 'eca4dd77-37ef-4b5f-bcfe-0a208b51d653'
})
MERGE
(perf_05cce238d31f:Performance{
	name: 'Blue in Green',
	duration: '5:55',
	uuid: 'ed1979cf-d8e7-4099-8f48-05cce238d31f'
})
MERGE
(perf_8a24258962b8:Performance{
	name: 'Blue in Green',
	disambiguation: 'original mono studio mix',
	duration: '5:28',
	uuid: 'edd1de11-e598-4e4a-ae9a-8a24258962b8'
})
MERGE
(work_c46c80a82e1b:Work{
	name: 'Flamenco Sketches',
	type: 'Song',
	wikidata: 'http://www.wikidata.org/wiki/Q1142997',
	musicbrainz: 'https://musicbrainz.org/work/36ff917b-6e10-3ee0-9e42-c46c80a82e1b',
	uuid: '36ff917b-6e10-3ee0-9e42-c46c80a82e1b'
})
MERGE
(perf_5d1a166e0f2f:Performance{
	name: 'Flamenco Sketches',
	disambiguation: 'original stereo studio master',
	duration: '9:24',
	uuid: '250b3f1d-7620-42a9-87b3-5d1a166e0f2f'
})
MERGE
(perf_8c24e42d0d58:Performance{
	name: 'Flamenco Sketches',
	duration: '3:32',
	uuid: '28a04388-0e77-491e-84c8-8c24e42d0d58'
})
MERGE
(perf_71fbf3d1171f:Performance{
	name: 'Flamenco Sketches',
	disambiguation: '2013 stereo remix',
	duration: '9:21',
	uuid: '2b7eda87-9518-4d65-bd67-71fbf3d1171f'
})
MERGE
(perf_17e4e0eddabf:Performance{
	name: 'Flamenco Sketches',
	disambiguation: '2013 mono remix',
	duration: '9:22',
	uuid: '2df62921-e94d-494b-a507-17e4e0eddabf'
})
MERGE
(perf_395b798e54b3:Performance{
	name: 'Flamenco Sketches',
	duration: '16:04',
	uuid: '54e64391-f8a9-40c8-8817-395b798e54b3'
})
MERGE
(perf_0c31dbd4a33d:Performance{
	name: 'Flamenco Sketches',
	duration: '7:10',
	uuid: '6086acbb-f12d-42b4-8697-0c31dbd4a33d'
})
MERGE
(perf_87d5b10e5d5d:Performance{
	name: 'Flamenco Sketches (alternate take)',
	duration: '9:32',
	uuid: 'bc80349a-c5d6-4d35-8d29-87d5b10e5d5d'
})
MERGE
(perf_08eb3c078dff:Performance{
	name: 'Flamenco Sketches',
	disambiguation: 'first speed-correct stereo remix',
	duration: '9:25',
	uuid: 'bd2167ef-4d52-4cde-b723-08eb3c078dff'
})
MERGE
(perf_a7ab0ba678e6:Performance{
	name: 'Flamenco Sketches',
	disambiguation: 'original mono studio mix',
	duration: '9:24',
	uuid: 'fabcab5f-12e1-435d-a66b-a7ab0ba678e6'
})
MERGE
(work_1938072b1375:Work{
	name: 'All Blues',
	iswc: 'T-073.092.719-1',
	type: 'Song',
	wikidata: 'http://www.wikidata.org/wiki/Q2600918',
	musicbrainz: 'https://musicbrainz.org/work/46e6bfc3-5f37-3e6e-a2be-1938072b1375',
	uuid: '46e6bfc3-5f37-3e6e-a2be-1938072b1375'
})
MERGE
(perf_43704088742c:Performance{
	name: 'All Blues',
	duration: '4:57',
	uuid: '0012285d-2166-4424-b411-43704088742c'
})
MERGE
(perf_5e26e59c6336:Performance{
	name: 'All Blues',
	duration: '15:09',
	uuid: '013acfd5-3cea-42a9-9f6d-5e26e59c6336'
})
MERGE
(perf_a217e0560ae5:Performance{
	name: 'All Blues',
	duration: '17:06',
	uuid: '09841c36-02a3-4268-b590-a217e0560ae5'
})
MERGE
(perf_aad57f849549:Performance{
	name: 'All Blues',
	duration: '6:28',
	uuid: '0aadfeab-c2e7-4944-9e6c-aad57f849549'
})
MERGE
(perf_18684fa2f594:Performance{
	name: 'All Blues',
	duration: '3:27',
	uuid: '0fa11e0b-18dd-448a-941b-18684fa2f594'
})
MERGE
(perf_fd025057ee68:Performance{
	name: 'All Blues',
	duration: '12:02',
	uuid: '1043eb64-660d-44d2-85ce-fd025057ee68'
})
MERGE
(perf_8759929f896a:Performance{
	name: 'All Blues',
	duration: '6:26',
	uuid: '329b9eb0-ada4-4f86-86e7-8759929f896a'
})
MERGE
(perf_174c4c2c0b46:Performance{
	name: 'All Blues',
	duration: '12:36',
	uuid: '3a5dde1c-7001-4fdf-b1c8-174c4c2c0b46'
})
MERGE
(perf_be09ff27fbda:Performance{
	name: 'All Blues',
	disambiguation: 'first speed-correct stereo remix',
	duration: '11:35',
	uuid: '3a9345f6-7f1f-4497-93c9-be09ff27fbda'
})
MERGE
(perf_ef1fe85ad46b:Performance{
	name: 'All Blues (cut)',
	duration: '6:07',
	uuid: '3c783b5d-45dc-4c45-a07e-ef1fe85ad46b'
})
MERGE
(perf_83e187970b2d:Performance{
	name: 'All Blues',
	duration: '7:14',
	uuid: '67f7c150-0234-4758-9c2f-83e187970b2d'
})
MERGE
(perf_20b9d803ae10:Performance{
	name: 'All Blues',
	disambiguation: '2013 mono remix',
	duration: '11:33',
	uuid: '727213a4-7932-417c-b91b-20b9d803ae10'
})
MERGE
(perf_aae8ebc09520:Performance{
	name: 'All Blues',
	duration: '7:08',
	uuid: '7281bfdb-1d4b-46e9-bb51-aae8ebc09520'
})
MERGE
(perf_71bb427c4d07:Performance{
	name: 'All Blues',
	duration: '2:26',
	uuid: '87ec7a04-8dd8-4cc7-b623-71bb427c4d07'
})
MERGE
(perf_57ce9a275e11:Performance{
	name: 'All Blues',
	duration: '9:51',
	uuid: '8e628aae-144d-48a9-9507-57ce9a275e11'
})
MERGE
(perf_4bc0f502e5e6:Performance{
	name: 'All Blues',
	duration: '8:57',
	uuid: '8ea67404-ddc2-479a-882f-4bc0f502e5e6'
})
MERGE
(perf_5c800b8d5c88:Performance{
	name: 'All Blues',
	duration: '8:46',
	uuid: '93e80526-9a1c-4882-998f-5c800b8d5c88'
})
MERGE
(perf_00b29f504057:Performance{
	name: 'All Blues',
	disambiguation: 'original mono studio mix',
	duration: '11:33',
	uuid: '9725eef2-8cf7-479d-85d1-00b29f504057'
})
MERGE
(perf_3d0cee232925:Performance{
	name: 'All Blues',
	disambiguation: 'original stereo studio master',
	duration: '11:33',
	uuid: 'b7ebe185-21e9-4400-a17a-3d0cee232925'
})
MERGE
(perf_efee700a2803:Performance{
	name: 'All Blues',
	duration: '5:37',
	uuid: 'c6ea8b4f-13a9-4112-90a3-efee700a2803'
})
MERGE
(perf_d2fe3edc00c2:Performance{
	name: 'All Blues',
	duration: '8:28',
	uuid: 'c9d2c053-0912-4a75-935b-d2fe3edc00c2'
})
MERGE
(perf_76266b6e74b6:Performance{
	name: 'All Blues',
	disambiguation: '2013 stereo remix',
	duration: '11:33',
	uuid: 'd3c678a7-d391-44a4-b6be-76266b6e74b6'
})
MERGE
(perf_0731952204e1:Performance{
	name: 'All Blues',
	duration: '12:56',
	uuid: 'e19f7bcb-5a5b-47be-aef9-0731952204e1'
})
MERGE
(perf_1dbf154f8ff3:Performance{
	name: 'All Blues',
	duration: '7:56',
	uuid: 'e5b90e7e-1880-42b9-af12-1dbf154f8ff3'
})
MERGE
(perf_79e8720259be:Performance{
	name: 'All Blues',
	duration: '6:53',
	uuid: 'ecafd082-0302-4573-846d-79e8720259be'
})
MERGE
(perf_7d39899a5e00:Performance{
	name: 'All Blues',
	duration: '5:03',
	uuid: 'f0def3f2-dd88-4beb-8d47-7d39899a5e00'
})
MERGE
(perf_e0d8385a8da6:Performance{
	name: 'All Blues',
	duration: '7:03',
	uuid: 'fcafad0a-e656-41f5-b94b-e0d8385a8da6'
})
MERGE
(perf_464f58283f6c:Performance{
	name: 'All Blues',
	duration: '12:58',
	uuid: 'fcfe4a7c-b463-4fa8-b4a2-464f58283f6c'
})

// tv performance
MERGE
(perf_9077837a3faa:Performance{
    uuid: '88059b0d-d74d-41b0-a698-9077837a3faa',
    name: 'So What'
})
MERGE (perf_9077837a3faa)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)


// performances of
MERGE (perf_56f120ba125d)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_9fe886723889)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_0396774f77e9)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_627ff0588a73)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_374d6a433e46)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_ea9246336782)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_5d9812a293ae)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_ab022f027ca5)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_44a8a638e360)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_fa7b9a0948e3)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_905334c9a48a)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_e5eb02e4779c)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_890f9dc95d12)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_f377a1549f41)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_75a8471af82d)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_e5b27315070a)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_4de574c23bf2)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_a87489f4edfb)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_2e30e1f11898)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_550dac9b606f)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_3512576e7867)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_c9fb07026b93)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_f2e5773f2904)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_cb0f58ab49f3)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_878d54026449)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_65d639180437)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_666f12d5883e)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_678f890b4f82)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_ea3680ebf325)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_f2314bc256a0)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_2e80ae99583e)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_70f195a3a251)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_a06ef88ca8a7)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_2396a6961083)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_77005243e0ae)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_6f43bda625cf)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_117ef9da73f6)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_7b864e366803)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_86d6e973196f)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_563d9a227e7e)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_4fd96a938857)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_73b11087a1d5)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_995f83279a4e)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_2bbc58c4e013)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_df0f1c1b8c5f)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_6a08b1fc829b)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_5a1a9bb5204f)-[:PERFORMANCE_OF]->(work_382bacca0923)
MERGE (perf_e1e3224858d5)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_7d35a60f9894)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_899641dc3ef4)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_0a121eface86)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_16c93ebdbe28)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_acab7145713d)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_f67d6df000a0)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_1696e1b62128)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_ed4ff735a34a)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_05741c5ebac7)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_e5526f650010)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_9eace7e208f2)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_155daa25751b)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_95a0ef477189)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_0404f1f15b78)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_e46312ee1150)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_cf3a1c9376ec)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_b82de3cfa632)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_af9ff95b97da)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_cf671462f29e)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_4bb97553ae89)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_1a1c24d4be26)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_a94415e9d27d)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_ad1fabaa0670)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_08ed20598107)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_0a208b51d653)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_05cce238d31f)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_8a24258962b8)-[:PERFORMANCE_OF]->(work_d7943efb9a03)
MERGE (perf_5d1a166e0f2f)-[:PERFORMANCE_OF]->(work_c46c80a82e1b)
MERGE (perf_8c24e42d0d58)-[:PERFORMANCE_OF]->(work_c46c80a82e1b)
MERGE (perf_71fbf3d1171f)-[:PERFORMANCE_OF]->(work_c46c80a82e1b)
MERGE (perf_17e4e0eddabf)-[:PERFORMANCE_OF]->(work_c46c80a82e1b)
MERGE (perf_395b798e54b3)-[:PERFORMANCE_OF]->(work_c46c80a82e1b)
MERGE (perf_0c31dbd4a33d)-[:PERFORMANCE_OF]->(work_c46c80a82e1b)
MERGE (perf_87d5b10e5d5d)-[:PERFORMANCE_OF]->(work_c46c80a82e1b)
MERGE (perf_08eb3c078dff)-[:PERFORMANCE_OF]->(work_c46c80a82e1b)
MERGE (perf_a7ab0ba678e6)-[:PERFORMANCE_OF]->(work_c46c80a82e1b)
MERGE (perf_43704088742c)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_5e26e59c6336)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_a217e0560ae5)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_aad57f849549)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_18684fa2f594)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_fd025057ee68)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_8759929f896a)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_174c4c2c0b46)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_be09ff27fbda)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_ef1fe85ad46b)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_83e187970b2d)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_20b9d803ae10)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_aae8ebc09520)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_71bb427c4d07)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_57ce9a275e11)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_4bc0f502e5e6)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_5c800b8d5c88)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_00b29f504057)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_3d0cee232925)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_efee700a2803)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_d2fe3edc00c2)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_76266b6e74b6)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_0731952204e1)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_1dbf154f8ff3)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_79e8720259be)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_7d39899a5e00)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_e0d8385a8da6)-[:PERFORMANCE_OF]->(work_1938072b1375)
MERGE (perf_464f58283f6c)-[:PERFORMANCE_OF]->(work_1938072b1375)

// composers
MERGE (artist_323e6ce46c2a)-[:COMPOSED]->(work_3a7d6599a72e)
MERGE (artist_323e6ce46c2a)-[:COMPOSED]->(work_382bacca0923)
MERGE (artist_323e6ce46c2a)-[:COMPOSED]->(work_d7943efb9a03)
MERGE (artist_6c57b03a4e36)-[:COMPOSED]->(work_d7943efb9a03)
MERGE (artist_323e6ce46c2a)-[:COMPOSED]->(work_c46c80a82e1b)
MERGE (artist_6c57b03a4e36)-[:COMPOSED]->(work_c46c80a82e1b)
MERGE (artist_323e6ce46c2a)-[:COMPOSED]->(work_1938072b1375)

MERGE
(release_947554bc8b3d:Release{
	name: 'Kind of Blue',
	disambiguation: 'mono',
	country: 'US',
	date: '1959-08-17',
	format: '12" Vinyl',
	discode: 'CL 1355',
	discogs: 'http://www.discogs.com/release/2252871',
	musicbrainz: 'http://musicbrainz.org/release/79ed3ff2-1b33-3245-8755-947554bc8b3d',
	uuid: '79ed3ff2-1b33-3245-8755-947554bc8b3d'
})

// labels
MERGE
(label_0400dd45693e:Label{
	name: 'Columbia',
	uuid: '011d1192-6f65-45bd-85c4-0400dd45693e'
})
MERGE (release_947554bc8b3d)-[:HAS_LABEL]->(label_0400dd45693e)

// tracks
MERGE (release_947554bc8b3d)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_0396774f77e9)
MERGE (release_947554bc8b3d)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_2396a6961083)
MERGE (release_947554bc8b3d)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_8a24258962b8)
MERGE (release_947554bc8b3d)-[:HAS_TRACK {name: 'B1', sequence: 4}]->(perf_00b29f504057)
MERGE (release_947554bc8b3d)-[:HAS_TRACK {name: 'B2', sequence: 5}]->(perf_a7ab0ba678e6)

// leaders
MERGE (release_947554bc8b3d)-[:HAS_LEADER]->(artist_323e6ce46c2a)

// release - producers, engineers, liner notes, etc.
MERGE (artist_f35080d12d60)-[:PARTICIPATED_IN {roles:['producer']}]->(release_947554bc8b3d)
MERGE (artist_d5fead5a7988)-[:PARTICIPATED_IN {roles:['producer']}]->(release_947554bc8b3d)
MERGE (artist_c69b63044dd6)-[:PARTICIPATED_IN {roles:['original liner notes']}]->(release_947554bc8b3d)
MERGE (artist_084c872be8e5)-[:PARTICIPATED_IN {roles:['engineer']}]->(release_947554bc8b3d)

// sessions
MERGE
	(session_0f8c3b265704:Session{
		uuid:'10202790-4ffd-4f8a-a3b5-0f8c3b265704',
		name:'Kind of Blue: Miles Davis Sextet',
		date:'1959-03-02',
		lordisco: ['D1596', 'D1597'],
		type:'recording session'})
MERGE
	(session_2f5a658d2f51:Session{
		uuid:'b91a5e28-d4f8-4c83-b9f3-2f5a658d2f51',
		name:'Kind of Blue: Miles Davis Sextet',
		date:'1959-04-22',
		lordisco: ['D1599'],
		type:'recording session'})
MERGE
	(session_793d44668bf0:Session{
		uuid:'cccc57ec-a06b-4566-8414-793d44668bf0',
		name:'Miles Davis at The Robert Herridge Theater - The Sound of Miles Davis Live',
		date:'1959-04-03',
		lordisco: ['D1598'],
		type:'television appearance',
		links: ['http://www.dailymotion.com/video/xmo2xe_miles-davis-the-cool-jazz-sound_shortfilms']})

// locations
MERGE
(loc1:Location{
	name: 'Columbia 30th Street Studios',
	city: 'New York City',
	state: 'NY',
	country: 'USA',
	lat: '40.712784',
	lng: '-74.005941',
	venue: 'Columbia 30th Street Studios',
	links: ['https://en.wikipedia.org/wiki/CBS_30th_Street_Studio']
})
MERGE
(loc2:Location{
	name: 'The Robert Herridge Theater',
	city: 'New York City',
	state: 'NY',
	country: 'USA',
	lat: '40.712784',
	lng: '-74.005941',
	venue: 'CBS Studio 1, The Robert Herridge Theater'
})

// session -> performances

MERGE (session_0f8c3b265704)-[:HAS_PERFORMANCE]->(perf_0396774f77e9)
MERGE (session_0f8c3b265704)-[:HAS_PERFORMANCE]->(perf_2396a6961083)
MERGE (session_0f8c3b265704)-[:HAS_PERFORMANCE]->(perf_8a24258962b8)
MERGE (session_2f5a658d2f51)-[:HAS_PERFORMANCE]->(perf_00b29f504057)
MERGE (session_2f5a658d2f51)-[:HAS_PERFORMANCE]->(perf_a7ab0ba678e6)
MERGE (session_793d44668bf0)-[:HAS_PERFORMANCE]->(perf_9077837a3faa)

// session -> location
MERGE (session_0f8c3b265704)-[:HAS_LOCATION]->(loc1)
MERGE (session_2f5a658d2f51)-[:HAS_LOCATION]->(loc1)
MERGE (session_793d44668bf0)-[:HAS_LOCATION]->(loc2)

// ---------------------------------------------------------------------------------
// ----- ARTIST RELATIONSHIPS ------------------------------------------------------
// ---------------------------------------------------------------------------------

// performances:
// perf_0396774f77e9 = so what
// perf_2396a6961083 = freddie freeloader
// perf_8a24258962b8 = blue in green
// perf_00b29f504057 = all blues
// perf_a7ab0ba678e6 = flamenco sketches
// perf_9077837a3faa = so what (television)

// artist -> performance

// miles davis
MERGE (artist_323e6ce46c2a)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(perf_0396774f77e9)
MERGE (artist_323e6ce46c2a)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(perf_2396a6961083)
MERGE (artist_323e6ce46c2a)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(perf_8a24258962b8)
MERGE (artist_323e6ce46c2a)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(perf_00b29f504057)
MERGE (artist_323e6ce46c2a)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(perf_a7ab0ba678e6)
MERGE (artist_323e6ce46c2a)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(perf_9077837a3faa)

// john coltrane
MERGE (artist_72ad46cdb831)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(perf_0396774f77e9)
MERGE (artist_72ad46cdb831)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(perf_2396a6961083)
MERGE (artist_72ad46cdb831)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(perf_8a24258962b8)
MERGE (artist_72ad46cdb831)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(perf_00b29f504057)
MERGE (artist_72ad46cdb831)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(perf_a7ab0ba678e6)
MERGE (artist_72ad46cdb831)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(perf_9077837a3faa)

// paul chambers
MERGE (artist_7de13124b970)-[:PARTICIPATED_IN {instruments:['double bass']}]->(perf_0396774f77e9)
MERGE (artist_7de13124b970)-[:PARTICIPATED_IN {instruments:['double bass']}]->(perf_2396a6961083)
MERGE (artist_7de13124b970)-[:PARTICIPATED_IN {instruments:['double bass']}]->(perf_8a24258962b8)
MERGE (artist_7de13124b970)-[:PARTICIPATED_IN {instruments:['double bass']}]->(perf_00b29f504057)
MERGE (artist_7de13124b970)-[:PARTICIPATED_IN {instruments:['double bass']}]->(perf_a7ab0ba678e6)
MERGE (artist_7de13124b970)-[:PARTICIPATED_IN {instruments:['double bass']}]->(perf_9077837a3faa)

// jimmy cobb
MERGE (artist_fe2cd264bbd0)-[:PARTICIPATED_IN {instruments:['drums']}]->(perf_0396774f77e9)
MERGE (artist_fe2cd264bbd0)-[:PARTICIPATED_IN {instruments:['drums']}]->(perf_2396a6961083)
MERGE (artist_fe2cd264bbd0)-[:PARTICIPATED_IN {instruments:['drums']}]->(perf_8a24258962b8)
MERGE (artist_fe2cd264bbd0)-[:PARTICIPATED_IN {instruments:['drums']}]->(perf_00b29f504057)
MERGE (artist_fe2cd264bbd0)-[:PARTICIPATED_IN {instruments:['drums']}]->(perf_a7ab0ba678e6)
MERGE (artist_fe2cd264bbd0)-[:PARTICIPATED_IN {instruments:['drums']}]->(perf_9077837a3faa)

// cannonball adderley
MERGE (artist_2fe1f9f27da8)-[:PARTICIPATED_IN {instruments:['alto saxophone']}]->(perf_0396774f77e9)
MERGE (artist_2fe1f9f27da8)-[:PARTICIPATED_IN {instruments:['alto saxophone']}]->(perf_2396a6961083)
MERGE (artist_2fe1f9f27da8)-[:PARTICIPATED_IN {instruments:['alto saxophone']}]->(perf_00b29f504057)
MERGE (artist_2fe1f9f27da8)-[:PARTICIPATED_IN {instruments:['alto saxophone']}]->(perf_a7ab0ba678e6)

// bill evans
MERGE (artist_6c57b03a4e36)-[:PARTICIPATED_IN {instruments:['piano']}]->(perf_0396774f77e9)
MERGE (artist_6c57b03a4e36)-[:PARTICIPATED_IN {instruments:['piano']}]->(perf_8a24258962b8)
MERGE (artist_6c57b03a4e36)-[:PARTICIPATED_IN {instruments:['piano']}]->(perf_00b29f504057)
MERGE (artist_6c57b03a4e36)-[:PARTICIPATED_IN {instruments:['piano']}]->(perf_a7ab0ba678e6)

// Wynton Kelly
MERGE (artist_13d821490e42)-[:PARTICIPATED_IN {instruments:['piano']}]->(perf_2396a6961083)
MERGE (artist_13d821490e42)-[:PARTICIPATED_IN {instruments:['piano']}]->(perf_9077837a3faa)

// gil evans
MERGE (artist_c69b63044dd6)-[:PARTICIPATED_IN {roles:['conductor','arranger']}]->(perf_9077837a3faa)

// robert herridge
MERGE (artist_98c032bfe986)-[:PARTICIPATED_IN {roles:['television producer','television host']}]->(session_793d44668bf0)


