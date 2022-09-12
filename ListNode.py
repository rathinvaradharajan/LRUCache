class Node:
    def __init__(self, key: int, value: int, prev=None, nxt=None):
        """
        A doubly linked list node which has a key and value as content.
        :param key: The key property of the node.
        :param value: The value property of the node.
        :param prev: This node's previous node in the doubly linked list.
        :param nxt: This node's next node in the doubly linked list.
        """
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt
        