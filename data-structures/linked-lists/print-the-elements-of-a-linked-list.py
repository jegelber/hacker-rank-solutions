# Problem: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
# Score: 5/5

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.get_next() is not None:
                curr_node = curr_node.get_next()
            curr_node.set_next(new_node)

def printLinkedList(head):
    curr_node = head
    while curr_node is not None:
        print(curr_node.get_data())
        curr_node = curr_node.get_next()
