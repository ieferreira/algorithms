# basic data structure that is a collection of nodes
# needs data and pointers

class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


class LinkedListVis:
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
        node = self.head
        while node is not None:
            yield node
            node = node.next


l_list = LinkedListVis()

l_list.head = first_node
first_node.next = second_node
second_node.next = third_node

l_list.visualize()

for node in l_list:
    print(node.data)
