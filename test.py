from ll import LinkedList, Node

ll = LinkedList()

node_a = Node('Losing It', 'Fisher', 'Losing It')
node_b = Node('Red Light', 'Anyma', 'A Mirror Without Reflection')
node_c = Node('Rapture', 'Anyma & Massano', 'Rapture')

ll.insert_at_end(node_a)
ll.insert_at_end(node_b)
ll.insert_at_end(node_c)

print('Lista:')
print(ll)

print('\nNavegando con prev/next:')
current = ll.start
while current is not None:
    print(f'  -> {current}')
    current = current.next

print('\nNavegando al reves:')
while current is None:
    current = ll.start
    for node in ll:
        last = node

current = last
while current is not None:
    print(f'  -> {current}')
    current = current.prev
