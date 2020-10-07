# Problem: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
# Score: 5/5

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def insertNodeAtTail(head, item):
    new_node = SinglyLinkedListNode(item)
    if head is None:
        head = new_node
    else:
        curr_node = head
        while curr_node.get_next() is not None:
            curr_node = curr_node.get_next()
        curr_node.set_next(new_node)
    return head
