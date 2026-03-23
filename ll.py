import random


class Node:
    def __init__(self, song, artist, album):
        self.data = {
            'song': song,
            'artist': artist,
            'album': album
        }
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'( {self.data["song"]} - {self.data["artist"]} )'


class LinkedList:
    def __init__(self):
        self.start = None
        self.shuffle = False

    def __repr__(self):
        nodes = ['START']
        for node in self:
            nodes.append(str(node.data['song']))
        nodes.append('NIL')
        return '\n' + ' --> '.join(nodes)

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        n = 0
        for _ in self:
            n += 1
        return n

    def insert_at_beginning(self, element):
        element.next = self.start
        if self.start is not None:
            self.start.prev = element
        self.start = element

    def insert_at_end(self, element):
        if self.start is None:
            self.start = element
            return
        for node in self:
            last = node
        last.next = element
        element.prev = last

    def insert_after_node(self, element, node_reference):
        for node in self:
            if node.data == node_reference:
                element.next = node.next
                element.prev = node
                if node.next is not None:
                    node.next.prev = element
                node.next = element
                return

    def delete_node(self, element_data):
        if self.start is None:
            return
        if self.start.data == element_data:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            return
        for node in self:
            if node.data == element_data:
                if node.next is not None:
                    node.next.prev = node.prev
                node.prev.next = node.next
                return

    def search(self, element_data):
        for node in self:
            if node.data == element_data:
                return node
        return None

    def traverse(self):
        for node in self:
            print(node.data)

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle
        return self.shuffle

    def next_node(self, current):
        if self.shuffle:
            steps = random.randint(1, len(self) - 1)
            node = current
            for _ in range(steps):
                node = node.next if node.next is not None else self.start
            return node
        return current.next

    def prev_node(self, current):
        if self.shuffle:
            steps = random.randint(1, len(self) - 1)
            node = current
            for _ in range(steps):
                if node.prev is not None:
                    node = node.prev
                else:
                    for n in self:
                        last = n
                    node = last
            return node
        return current.prev