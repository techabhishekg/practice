class Node:
    def __init__(self):
        self.next= None
        self.data= 0


def push(head_ref, newdata):
    newnode = Node()
    newnode.data = newdata
    if head_ref is None:
        head_ref = newnode
    else:
        cur = head_ref
        while cur.next:
            cur = cur.next

        cur.next = newnode

    return head_ref


def printList(head_ref):
    while head_ref != None:
        print head_ref.data
        head_ref = head_ref.next


head = None
head = push(head, 1)
head = push(head, 2)
head = push(head, 3)
head = push(head, 4)
head = push(head, 5)
head = push(head, 6)
head = push(head, 7)
head = push(head, 8)


print('head is on ', head.data)



print('printing the linked list')
printList(head)

print('This program is for detect a loop in linked list, so create a LL which have loop')
print(head.next.next.next.next.next.data, head.next.next.data)
head.next.next.next.next.next = head.next.next


def detectAndremoveLoop(head):
    slow_p = fast_p = head
    while (slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        if slow_p == fast_p:
            print('loop node found',head.data, slow_p.data)
            removeloop(head, slow_p)
            return 1

    return 0


def detectLoop(head):
    slow_p = fast_p = head
    while (slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        if slow_p == fast_p:
            return 1

    return 0

def removeloop(head, loopnode):
    # detect the number of node in loop k
    # set the ptr2 at k node after head
    # iterate until ptr1 , ptr 2 same
    # now iterate ptr2, until it point ptr1, then set ptr2.next = None

    ptr1 = loopnode
    ptr2 = loopnode
    count = 1
    while ptr2.next != ptr1:
        ptr2 = ptr2.next
        count +=1

    print(count)

    ptr1 = head
    ptr2 = head
    for i in range(count):
        ptr2 = ptr2.next

    print(ptr1.data, ptr2.data)

    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    while ptr2.next != ptr1:
        ptr2 = ptr2.next

    ptr2.next = None

print('now check loop in LL')
print(detectLoop(head))


print('now dtect and remove loop  LL')
print(detectAndremoveLoop(head))


print('again detect loop')
print(detectLoop(head))



