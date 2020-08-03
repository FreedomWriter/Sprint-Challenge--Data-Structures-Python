class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1 if value is not None else 0

    # Insert the given value into the tree
    def insert(self, value):
        self.size += 1
        if value < self.value:
            # if there is already a value to the left, call insert on self.left
            if self.left:
                return self.left.insert(value)
            else: # there is no value on the left, insert a new node
                self.left = BST(value)
        else: # less than or equal to
            if self.right: # if there is a value on the right, recursively call insert on self.right
                return self.right.insert(value)
            else: # no value on the right, insert a new node
                self.right = BST(value)

    def contains(self, target):
        # if the value is equal to the root value
        if self.value == target:
            return True
        # if the value is greater than the root value and there is a right child - recursively run contains
        elif target > self.value and self.right:
            return self.right.contains(target)
        # if the value is greater than the root value and there is a left child - recursively run contains
        elif target < self.value and self.left:
            return self.left.contains(target)
        # if the value was never found
        return False 

bst = BST('place holder') 

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# ORIGINAL RUNTIME O(N^2)
# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# # NEW RUNTIME O(log N)
# # Replace the nested for loops below with your improvements
# for name in names_1:
#     bst.insert(name)
# for name in names_2:
#     if bst.contains(name):
#         duplicates.append(name)

# STRETCH
# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
