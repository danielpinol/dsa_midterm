from playlist import build_playlist, songs


def display(node, i, total):
    print('\n' + '=' * 40)
    print(f'  Now Playing ({i}/{total})')
    print('=' * 40)
    print(f'  Song:   {node.data["song"]}')
    print(f'  Artist: {node.data["artist"]}')
    print(f'  Album:  {node.data["album"]}')
    print('=' * 40)
    print('  [n] Next   [p] Previous   [q] Quit')
    print('=' * 40)


def run():
    pl = build_playlist(songs)
    total = len(pl)
    current = pl.start
    i = 1

    display(current, i, total)

    while True:
        action = input('\n> ').strip().lower()

        if action == 'n':
            if current.next is None:
                print('  Ya termino la playlist.')
            else:
                current = current.next
                i += 1
                display(current, i, total)

        elif action == 'p':
            if current.prev is None:
                print('  Already at the first song.')
            else:
                current = current.prev
                i -= 1
                display(current, i, total)

        elif action == 'q':
            print('\n  Adios!')
            break

        else:
            print('  Invalid input. Use n, p, or q.')


run()