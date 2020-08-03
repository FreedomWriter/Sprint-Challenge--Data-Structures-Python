# passes all tests

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


# # THIS IMPLEMENTATION WORKS, BUT WILL NOT PASS TESTS - (DUE TO THE WAY THE TESTS EXPECT .GET() TO BEHAVE)
# class Node:
#     def __init__(self, value=None, next_node=None):
#         self.value = value
#         self.next_node = next_node
        
# class LinkedList:
#     def __init__(self):
#         self.head = None  
#         self.tail = None  
#         self.size = 0

#     def __str__(self):
#         output = list()
#         current_node = self.head

#         while current_node is not None:
#             output.append(current_node.value)
#             current_node = current_node.next_node

#         return str(output)
    
#     def __len__(self):
#         self.size

#     def add_to_head(self, value):
#         new_node = Node(value)
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next_node = self.head
#             self.head = new_node
#         self.size+=1
#     def remove_head(self):
#         if not self.head:
#             return None
#         if self.head.next_node is None:
#             head_value = self.head.value
#             self.head = None
#             self.tail = None
#             return head_value
#         else:
#             head_value = self.head.value
#             self.head = self.head.next_node
#             return head_value

#     def add_to_tail(self, value):
#         new_node = Node(value)
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next_node = new_node
#             self.tail = new_node
#         self.size+=1

            

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
#             self.buffer.remove_head()
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

# # for i in range(50):
# #     buffer.append(i)
# print(buffer.buffer)
# print(buffer.size)
# print(buffer.get())


