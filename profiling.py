import time
from memory_profiler import profile
from playlist import build_playlist, songs


start = time.perf_counter()
pl = build_playlist(songs)
end = time.perf_counter()

print(f'build_playlist() took: {(end - start) * 1000:.4f} ms')
print(f'Songs loaded: {len(pl)}')


@profile
def run(data):
    from ll import LinkedList, Node
    pl = LinkedList()
    for song, artist, album in data:
        node = Node(song, artist, album)
        pl.insert_at_end(node)
    return pl


run(songs)