class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_items = 0
        self.head = None
        self.tail = None
        self.items = {}
    
    def is_head(self, node):
        return node == self.head
    
    def is_tail(self, node):
        return node == self.tail
    
    def set_head(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.num_items += 1
        return node
    
    def remove_tail(self):
        node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.num_items -= 1
        return node
    
    def remove_node(self, node):
        if self.is_tail(node):
            self.remove_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = node.prev = None
            self.num_items -= 1
            return node
        
    def put(self, number, value):
        """O(1) time"""
        if number in self.items:
            node = self.items[number]['node']
            if node != self.head:
                self.remove_node(node)
            self.items[number]['val'] = value
        else:
            node = LinkedListNode(number)
            self.items[number] = {'node': node, 'val': value}
        if node != self.head:
            self.set_head(node)
        
        if self.num_items > self.capacity:
            node = self.remove_tail()
            del self.items[node.val]
            
    def get(self, number):
        """O(1) time"""
        if number in self.items:
            node = self.items[number]['node']
            if node != self.head:
                self.remove_node(node)
                self.set_head(node)
            return self.items[number]['val']
        else:
            return -1
