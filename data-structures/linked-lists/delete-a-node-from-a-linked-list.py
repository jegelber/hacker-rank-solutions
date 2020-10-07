# Problem: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
# Score: 5/5

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNode(head, position):
    # Empty List
    if head is None:
        return None

    # Head removed
    if position == 0:
        head = head.next
        return head

    # Non-head node
    count = 1
    curr_node = head.next
    prev_node = head

    while count < position:
        prev_node = curr_node
        curr_node = curr_node.next
        count += 1

    prev_node.next = curr_node.next

    return head
