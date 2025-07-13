# 1. Initialization (Constructor)
# Step 1.1: Create a class named LinkedList

# Step 1.2: Inside it, define a variable head and set it to None

# This means the list is empty

# 2. Insert at End
# When you want to insert a value into the list:

# Step 2.1: Create a new Node with the given value
# This node has .value = value and .next = None

# Step 2.2: Check if head is None
# If yes:
# → This is the first node, so set head = new_node

# If no:
# → Start from head
# → Move forward using .next until you find the last node (where next = None)
# → Set last_node.next = new_node

# 3. Print List
# To print all values in the list:

# Step 3.1: Start at head
# Step 3.2: While the current node is not None:
# Print its .value

# Move to current.next

# Optional: Summary in Plain English
# Start with nothing (head = None)

# To add a new value:

# If the list is empty, make it the first item

# If not, go to the end and attach the new item

# To print, start from the beginning and follow the arrows, printing values one by one

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def inseert_at_end(self,value):
#         newNode = Node(value)

#         if self.head is None:
#             self.head = newNode
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = newNode
#     def print(self):
#         current = self.head
#         while current:
#             print(current.value)
#             current = current.next


# li = LinkedList()
# li.inseert_at_end(3)
# li.inseert_at_end(4)
# li.inseert_at_end(6)
# li.inseert_at_end(2)
# li.inseert_at_end(7)

# li.print()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def set_at_end(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head

            while current.next:
                current = current.next
            current.next = newNode

    def set_at_beginning(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

li = LinkedList()
li.set_at_end(2)
li.set_at_end(1)
li.set_at_beginning(10)
li.set_at_end(3)
li.set_at_end(4)
li.set_at_end(2)

li.print()