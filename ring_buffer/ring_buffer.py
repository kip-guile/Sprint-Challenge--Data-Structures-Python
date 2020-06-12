from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        # self.size = 0
        self.current = None
        self.capacity = capacity
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head

        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.current.next

        else:
            if not self.current.next:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head

            else:
                self.current.next.delete()
                self.current.insert_after(item)
                self.current = self.current.next

    def get(self):
        list_buffer_contents = []

        def add_to_list(node):
            if not node:
                return
            else:
                list_buffer_contents.append(node.value)
                add_to_list(node.next)

        add_to_list(self.storage.head)

        return list_buffer_contents
