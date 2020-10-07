# Problem: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
# Score: 5/5

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def reversePrint(head):
    head_reversed = reverseList(head)
    curr_node = head_reversed
    while curr_node is not None:
        print(curr_node.data)
        curr_node = curr_node.next

def reverseList(head):
    prev_node = None
    curr_node = head

    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node
