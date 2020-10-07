# Problem: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
# Score: 5/5

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtHead(head, data):
    new_node = SinglyLinkedListNode(data)
    new_node.head = head
    return new_node
