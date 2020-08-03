# class Node:
#     def __init__(self, value=None, next_node=None):
#         self.value = value
#         self.next_node = next_node
        
# class LinkedList:
#     def __init__(self):
#         self.head = None  # Stores a node, that corresponds to our first node in the list
#         self.tail = None  # stores a node tht is the end of the list
#         self.size = 0

#         # return all values for the is a -> b -> c -> d -> None
#     def __str__(self):
#         output = list()
#         # create a tracker variable
#         current_node = self.head

#         # loop until None
#         while current_node is not None:
#             output.append(current_node.value)
#             # update tracker to next node
#             current_node = current_node.next_node

#         return str(output)
    
#     def __len__(self):
#         self.size

#     def add_to_head(self, value):

#         # create a node to add
#         new_node = Node(value)
#         # check if list is empty
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # new_node should point to current head
#             new_node.next_node = self.head
#             # move head to new_node
#             self.head = new_node
#         self.size+=1
#     def remove_head(self):
#         # if list is empty do nothing
#         if not self.head:
#             return None
#         # if list only has one element set head and tail to None
#         if self.head.next_node is None:
#             head_value = self.head.value
#             self.head = None
#             self.tail = None
#             return head_value
#         # otherwise we have more elements in the list
#         else:
#             head_value = self.head.value
#             self.head = self.head.next_node
#             return head_value

#     def add_to_tail(self, value):
#         # create a node to add
#         new_node = Node(value)
#         # check if list is empty
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # point thendoe at the current tail, to the new node
#             self.tail.next_node = new_node
#             self.tail = new_node
#         self.size+=1

#     # def remove_tail(self):
#     #     if self.head is None and self.tail is None:
#     #         return None
#     #     elif self.head == self.tail:
#     #         self.head = None
#     #         self.tail = None
#     #         self.size -= 1
            
#     #     else:
#     #         cur_node = self.head
#     #         while cur_node.next_node is not self.tail:
#     #             cur_node = cur_node.next_node
#     #         cur_node.next_node = None
#     #         self.size -= 1
            

# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.buffer = LinkedList()
#         self.head = None
#         self.tail = None
#         self.size = 0

#     def append(self, item):

#         # full buffer
#         if self.size == self.capacity:
#             # self.buffer.remove_head()
#             self.buffer.add_to_tail(item)
#         # not full buffer
#         if self.size < self.capacity:
#             self.size += 1
#             self.buffer.add_to_tail(item)



    

#     def get(self):
#         return self.buffer




# buffer = RingBuffer(5)
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# buffer.append('e')
# buffer.append('f')
# buffer.append('g')
# buffer.append('h')
# buffer.append('i')
# print(buffer.buffer)
# print(buffer.size)
# print(buffer.get())


# Works below, will come back to above if there's time

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = list()
        self.capicity_tracker = capacity

 
    def append(self, item):
        if self.capacity > 0:
            self.buffer.append(item)
            self.capacity -= 1
        
        # empty buffer
        elif self.capacity == 0:
            self.capacity = self.capicity_tracker * -1
            self.buffer[self.capacity] = item
            self.capacity += 1
        # full buffer
        elif self.capacity < 0:
            self.buffer[self.capacity] = item
            self.capacity += 1
        # return self.buffer   


    

    def get(self):
        return self.buffer



ring_buffer = RingBuffer(5)
ring_buffer.append('a')
ring_buffer.append('b')
ring_buffer.append('c')
ring_buffer.append('d')
ring_buffer.append('e')
ring_buffer.append('f')
ring_buffer.append('g')
ring_buffer.append('h')
ring_buffer.append('i')
print(ring_buffer.buffer)
print(ring_buffer.get())
