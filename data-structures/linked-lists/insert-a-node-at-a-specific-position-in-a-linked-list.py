# Problem: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
# Score: 5/5
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)

    if position == 0 or head is None:
        new_node.next = head
        return new_node

    count = 1
    prev_node = head
    curr_node = head.next

    while count < position:
        prev_node = curr_node
        curr_node = curr_node.next
        count += 1

    prev_node.next = new_node
    new_node.next = curr_node

    return head
