class Node:
    def __init__(self, song: str, artist: str, album: str):
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
        length = 0

        for _ in self:
            length += 1

        return length

    def insert_at_beginning(self, element: Node):
        element.next = self.start

        if self.start is not None:
            self.start.prev = element

        self.start = element

    def insert_at_end(self, element: Node):
        if self.start is None:
            self.start = element
            return

        for node in self:
            last = node

        last.next = element
        element.prev = last

    def insert_after_node(self, element: Node, node_reference: any):
        for node in self:
            if node.data == node_reference:
                element.next = node.next
                element.prev = node

                if node.next is not None:
                    node.next.prev = element

                node.next = element
                return

    def delete_node(self, element_data: any):
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

    def search(self, element_data: any):
        for node in self:
            if node.data == element_data:
                return node

        return None

    def traverse(self):
        for node in self:
            print(node.data)
