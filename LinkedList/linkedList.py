# %%
# basic data structure that is a collection of nodes
# needs data and pointers

# %%
class LinkedList:
    # Linked List with visualization
    def __init__(self):
        self.head = None

    def visualize(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        print(" -> ".join(nodes))

    def __iter__(self):
        # for iterating inside a for loop
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # inserting node at start
    def insert_first(self, node):
        node.next = self.head
        self.head = node

    def insert_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def insert_after(self, target, new_node):
        if self.head is None:
            raise Exception("Empty list")
        for node in self:
            if node.data == target:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Target not found")

    def remove_node(self, target):
        if self.head is None:
            raise Exception("empty linked list")
        if self.head.data == target:
            self.head = self.head.next
            return
        one_before = self.head
        for node in self:
            if node.data == target:
                one_before.next = node.next
                return
            one_before = node
        raise Exception("target node not found")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# %%


first_node = Node("a")
second_node = Node("b")
third_node = Node("c")

l_list = LinkedList()

l_list.head = first_node
first_node.next = second_node
second_node.next = third_node


string_repr = ""
node = l_list.head

while node is not None:
    string_repr += node.data
    string_repr += " -> "
    node = node.next
string_repr += "None"

print(string_repr)

# %%
# visualization implementation


l_list = LinkedList()

l_list.head = first_node
first_node.next = second_node
second_node.next = third_node

l_list.visualize()

for node in l_list:
    print(node.data)

l_list.insert_first(Node("01"))
l_list.insert_first(Node("00"))


for node in l_list:
    print(node.data)
# %%
print(type(Node("AAA")))

print("Building a linked list")

linked_list = LinkedList()
linked_list.insert_first(Node("D"))
linked_list.insert_first(Node("C"))
linked_list.insert_first(Node("B"))
linked_list.insert_first(Node("A"))

linked_list.visualize()


# %%

# inserting at the end of the line

linked_list.insert_last(Node("E"))
linked_list.insert_last(Node("F"))
linked_list.visualize()

# %%

# inserting a node between two nodes
linked_list.insert_after("B", Node("BB"))
linked_list.insert_after("C", Node("CC"))
linked_list.visualize()
# %%
# * remove a node
linked_list.remove_node("BB")
linked_list.remove_node("CC")
linked_list.visualize()

# %%
# %%

# %%

# %%
