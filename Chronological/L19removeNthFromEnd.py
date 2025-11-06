class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def array_to_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head


def removeNthFromEnd(linked, n):
    head = array_to_linked_list(linked)
    print(head)
    length = 0
    current = head

    while current:
        length += 1
        current = current.next

    index = length - n
    count = 0

    cur = head
    while cur and cur.next:
        if (index == 0):
            return head.next
        
        if count + 1 == index:
            cur.next = cur.next.next
            return head
        cur = cur.next
        count += 1

head = removeNthFromEnd([4,5,4], 1)

current = head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
