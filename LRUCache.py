from ListNode import Node


class LRUCache:
    def __init__(self, capacity: int):
        """
        A cache that evicts the least recently used element when its capacity is full
        :param capacity: the capacity of the cache.
        """
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}
        self.size = 0

    def __move_to_tail(self, node):
        """
        Move the given element to the end of the doubly linked list.
        :param node: The node to be moved.
        """
        prev = node.prev
        nxt = node.nxt
        # If prev is None, this node is the head.
        if prev is None:
            self.head = nxt
            if nxt:
                nxt.prev = None
        else:
            prev.nxt = nxt
            if nxt:
                nxt.prev = prev
        self.tail.nxt = node
        node.prev = self.tail
        self.tail = node

    def get(self, key: int) -> int:
        """
        Get the value of the given key from cache.

        :param key: The key to be looked up from the cache.
        :return: The corresponding value. -1 if key on not found.
        """
        # If key is not present in cache, return -1
        if key not in self.cache:
            return -1
        # Key is found, move it to the tail.
        node = self.cache[key]
        self.__move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Put a key, value pair into the cache.

        :param key: The key property of the cache entry.
        :param value: The value property of the cache entry.
        :return: None
        """
        node = Node(key, value)
        # The list is empty, add the node to cache and point head and tail to it.
        if self.head is None:
            self.head = node
            self.tail = node
            self.cache[key] = node
            self.size += 1
            return
        # If key is already present in cache, update its value and move it to tail.
        if key in self.cache:
            self.cache[key].value = value
            self.__move_to_tail(self.cache[key])
            return
        # If the cache exceeds capacity, evict the head node from the cache.
        if self.size >= self.capacity:
            del self.cache[self.head.key]
            self.head = self.head.nxt
            if self.head:
                self.head.prev = None
            self.size -= 1
        # Add the new element to the tail of the list and into cache.
        self.tail.nxt = node
        node.prev = self.tail
        self.tail = node
        self.cache[key] = node
        self.size += 1
