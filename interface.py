from playlist import build_playlist, songs


def mostrar(nodo, i, total, shuffle):
    estado = 'ON' if shuffle else 'OFF'
    print('\n' + '=' * 40)
    print(f'  Now Playing ({i}/{total})')
    print('=' * 40)
    print(f'  Song:   {nodo.data["song"]}')
    print(f'  Artist: {nodo.data["artist"]}')
    print(f'  Album:  {nodo.data["album"]}')
    print('=' * 40)
    print(f'  [n] Next   [p] Previous   [s] Shuffle ({estado})   [q] Quit')
    print('=' * 40)


def buscar_indice(lista, objetivo):
    i = 1
    nodo = lista.start
    while nodo is not objetivo:
        nodo = nodo.next
        i += 1
    return i


def run():
    lista = build_playlist(songs)
    total = len(lista)
    actual = lista.start
    i = 1

    mostrar(actual, i, total, lista.shuffle)

    while True:
        accion = input('\n> ').strip().lower()

        if accion == 'n':
            siguiente = lista.next_node(actual)
            if siguiente is None:
                print('  Ya termino la playlist.')
            else:
                actual = siguiente
                i = buscar_indice(lista, actual)
                mostrar(actual, i, total, lista.shuffle)

        elif accion == 'p':
            anterior = lista.prev_node(actual)
            if anterior is None:
                print('  Already at the first song.')
            else:
                actual = anterior
                i = buscar_indice(lista, actual)
                mostrar(actual, i, total, lista.shuffle)

        elif accion == 's':
            lista.toggle_shuffle()
            print(f'\n  Shuffle {"ON" if lista.shuffle else "OFF"}.')
            mostrar(actual, i, total, lista.shuffle)

        elif accion == 'q':
            print('\n  Adios!')
            break

        else:
            print('  Invalid input. Use n, p, s, or q.')


run()