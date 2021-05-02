

class Node:
    def __init__(self):
        self.data = 0
        self.next = None

#insert at start of linked list (left)
# def push(head_ref, new_data):
#     new_node = Node()
#     new_node.data = new_data
#
#     new_node.next = head_ref
#
#     head_ref = new_node
#
#     return head_ref

# insert at end
def push(head_ref, new_data):
    new_node = Node()
    new_node.data = new_data
    if head_ref is None:
        head_ref = new_node
    else:
        cur = head_ref
        while (cur.next):
            cur = cur.next

        cur.next = new_node


    return head_ref


def reverse(head, k):
    if (head == None):
        return head

    # Create deque to store the address
    # of the nodes of the linked list
    q = []

    # Store head pointer in current to
    # traverse the linked list
    current = head
    i = 0

    # Iterate through the entire linked
    # list by moving the current
    while (current != None):
        #import pdb; pdb.set_trace()
        i = 1

        # Store addresses of the k
        # nodes in the deque
        while (i <= k):
            if (current == None):
                break
            q.append(current)
            current = current.next
            i = i + 1

        # pop first and the last value from
        # the deque and swap the data values at
        # those addresses
        # Do this till there exist an address in
        # the deque or deque is not empty
        while (len(q) > 0):
            front = q[-1]
            last = q[0]

            temp = front.data
            front.data = last.data
            last.data = temp

            # pop from the front if
            # the deque is not empty
            if (len(q) > 0):
                q.pop()

                # pop from the back if
            # the deque is not empty
            if (len(q)):
                q.pop(0)

    return head




def printList(head):
    while (head != None):
        print(head.data)
        head = head.next



head = None

head = push(head, 10)
head = push(head, 9)
head = push(head, 8)
head = push(head, 7)
head = push(head, 6)
head = push(head, 5)
head = push(head, 4)
head = push(head, 3)
head = push(head, 2)
head = push(head, 1)


printList(head)

k = 4


print('after reversing the linked list')
# Get the new head after reversing the
# linked list in groups of size k
head = reverse(head, k)
printList(head)