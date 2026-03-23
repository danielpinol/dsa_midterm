from playlist import build_playlist, songs


def display(node: 'Node', index: int, total: int):
    print('\n' + '=' * 40)
    print(f'  Now Playing ({index}/{total})')
    print('=' * 40)
    print(f'  Song:   {node.data["song"]}')
    print(f'  Artist: {node.data["artist"]}')
    print(f'  Album:  {node.data["album"]}')
    print('=' * 40)
    print('  [n] Next   [p] Previous   [q] Quit')
    print('=' * 40)


def run():
    playlist = build_playlist(songs)
    total = len(playlist)
    current = playlist.start
    index = 1

    display(current, index, total)

    while True:
        action = input('\n> ').strip().lower()

        if action == 'n':
            if current.next is None:
                print('  Ya termino la playlist')
            else:
                current = current.next
                index += 1
                display(current, index, total)

        elif action == 'p':
            if current.prev is None:
                print('  Already at the first song.')
            else:
                current = current.prev
                index -= 1
                display(current, index, total)

        elif action == 'q':
            print('\n  Adios!')
            break

        else:
            print('  Invalid input. Use n, p, or q.')


run()
