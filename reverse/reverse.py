class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    
    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # empty
        if self.head is None:
            return 
        # one item
        if self.head.get_next() is None:
            return self.head

        prev_node = prev
        cur_node = node
        
        # More than one item
        while cur_node is not None:
            next_node = cur_node.next_node
            cur_node.next_node = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def print_list(self):
        cur_val = self.head
        print(self.head.value)
        while cur_val is not None:
            print(cur_val.value)
            cur_val= cur_val.next_node




