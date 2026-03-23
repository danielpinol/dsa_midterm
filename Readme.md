dsa_midterm
Playlist de musica implementada con una lista doblemente linkedada no-circular.

Como clonar y ejecutar
git clone https://github.com/danielpinol/dsa_midterm.git
cd dsa_midterm
pip install memory_profiler
python interface.py
```

Controles: `n` siguiente, `p` anterior, `s` shuffle ON/OFF, `q` salir.

---

## Profiling

Se midio el tiempo y memoria de `build_playlist()` al cargar las 100 canciones.

Tiempo con `time.perf_counter()`:
```
build_playlist() took: 0.2170 ms
Songs loaded: 100
```

Memoria con `@profile` de `memory_profiler`:
```
Line #    Mem usage    Increment   Occurrences   Line Contents
=============================================================
    15     28.6 MiB     28.6 MiB           1   @profile
    16                                         def run(data):
    17     28.6 MiB      0.0 MiB           1       from ll import LinkedList, Node
    18     28.6 MiB      0.0 MiB           1       pl = LinkedList()
    19     28.7 MiB      0.0 MiB         102       for song, artist, album in data:
    20     28.7 MiB      0.0 MiB         101           node = Node(song, artist, album)
    21     28.7 MiB      0.0 MiB         101           pl.insert_at_end(node)
    22     28.7 MiB      0.0 MiB           1       return pl
(ver captura en documentation/profiling.png)
Cargar 100 canciones solo subio la memoria 0.1 MiB, de 28.6 a 28.7. Bastante eficiente.

Shuffle
El shuffle esta dentro de LinkedList. Cuando esta activo, en lugar de moverse al nodo siguiente o anterior, recorre un numero random de pasos por los punteros next y prev de la lista. Se activa y desactiva con s en cualquier momento.
Con shuffle OFF moverse es O(1) porque solo sigue un puntero. Con shuffle ON es O(n) porque puede recorrer hasta n-1 nodos.