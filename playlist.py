from ll import LinkedList, Node


songs = [
    ('Losing It', 'Fisher', 'Losing It'),
    ('Red Light', 'Anyma', 'A Mirror Without Reflection'),
    ('Alive', 'Massano', 'Alive'),
    ('Realm of Consciousness', 'Chris Avantgarde', 'Realm of Consciousness'),
    ('Innerbloom', 'RÜFÜS DU SOL', 'Bloom'),
    ('Glue', 'Bicep', 'Bicep'),
    ('Lady (Hear Me Tonight)', 'Modjo', 'Modjo'),
    ('Music Sounds Better With You', 'Stardust', 'Music Sounds Better With You'),
    ('Latch', 'Disclosure', 'Settle'),
    ('Porcelain', 'Moby', 'Play'),
    ('D.A.N.C.E.', 'Justice', 'Cross'),
    ('One More Time', 'Daft Punk', 'Discovery'),
    ('Nightcall', 'Kavinsky', 'Outrun'),
    ('Voices', 'Russ Yallop', 'Voices'),
    ('Opus', 'Eric Prydz', 'Opus'),
    ('Strobe', 'Deadmau5', 'For Lack of a Better Name'),
    ('Endless', 'Tale Of Us', 'Endless'),
    ('Conjure', 'Maceo Plex', 'Conjure'),
    ('Starry Night', 'Peggy Gou', 'Starry Night'),
    ('Doppler', 'Charlotte de Witte', 'Doppler'),
    ('Exhale', 'Amelie Lens', 'Exhale'),
    ('Subzero', 'Ben Klock', 'Subzero'),
    ('Temptation', 'Solomun', 'Temptation'),
    ('Seeing Through Shadows', 'Dixon', 'Seeing Through Shadows'),
    ('Baby', 'Four Tet', 'Baby'),
    ('LesAlpx', 'Floating Points', 'Elaenia'),
    ('Immunity', 'Jon Hopkins', 'Immunity'),
    ('Space Is Only Noise If You Can See', 'Nicolas Jaar', 'Space Is Only Noise'),
    ("Can't Do Without You", 'Caribou', 'Our Love'),
    ('Loud Places', 'Jamie xx', 'In Colour'),
    ('Delilah (Pull Me Out of This)', 'Fred Again..', 'Actual Life'),
    ('Chances', 'Kaytranada', '99.9%'),
    ('Cherry', 'Mall Grab', 'Cherry'),
    ('Cola', 'CamelPhat', 'Cola'),
    ("Don't You", 'Lane 8', 'Little Bang'),
    ('Knee Deep', 'Hot Since 82', 'Knee Deep'),
    ('Bar A Thym', 'Kerri Chandler', 'Bar A Thym'),
    ('Your Love', 'Frankie Knuckles', 'Your Love'),
    ('Can You Feel It', 'Larry Heard', 'Can You Feel It'),
    ('Move Your Body', 'Marshall Jefferson', 'Move Your Body'),
    ("Keep On Jumpin'", 'Todd Terry', "Keep On Jumpin'"),
    ('Lovelee Dae', 'Blaze', 'Lovelee Dae'),
    ('To Be in Love', 'Masters at Work', 'To Be in Love'),
    ('French Kiss', 'Lil Louis', 'French Kiss'),
    ('Pick Up', 'DJ Koze', 'Knock Knock'),
    ('Rej', 'Âme', 'Rej'),
    ("Geht's Noch", 'Roman Flügel', "Geht's Noch"),
    ('Danube', 'Move D', 'Danube'),
    ('Fleece on Brain', 'Matthew Dear', 'Fleece on Brain'),
    ('Hubble', 'Actress', 'Hubble'),
]


def build_playlist(song_list: list) -> LinkedList:
    playlist = LinkedList()

    for song, artist, album in song_list:
        node = Node(song, artist, album)
        playlist.insert_at_end(node)

    return playlist


playlist = build_playlist(songs)
print(playlist)
