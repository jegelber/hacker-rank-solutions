# Problem: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
# Score: 5/5

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    prev_node = None
    curr_node = head

    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node
