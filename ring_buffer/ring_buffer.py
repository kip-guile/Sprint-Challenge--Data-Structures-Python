from singly_linked_list import LinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.storage = []

    def append(self, item):
        if self.size == self.capacity:
            self.cur = 0
            self.storage[self.cur] = x
            self.cur = (self.cur + 1) % self.capacity
        self.storage.append(item)

    def get(self):
        return self.storage[self.cur:]+self.storage[:self.cur]
