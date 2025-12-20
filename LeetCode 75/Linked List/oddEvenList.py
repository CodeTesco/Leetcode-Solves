class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def arrToLinked(arr):
    head = ListNode(arr[0])
    current = head

    for el in arr[1:]:
        current.next = ListNode(el)
        current = current.next

    return head

def linkedToArr(head):
    arr = []
    current = head

    while current:
        arr.append(current.val)
        current = current.next

    return arr

def oddEvenList(head):
    current = head.next
    lastOdd = head
    firstEven = current
    lastEven = firstEven
    i = 2

    while current:
        if not i % 2 == 0:
            lastEven.next = current.next
            lastOdd.next = current
            current.next = firstEven
            lastOdd = current
            current = lastEven.next
        else:
            lastEven = current
            current = current.next
        i += 1

    return head

head = arrToLinked([2,1,3,5,6,4,7])
result = oddEvenList(head)
print(linkedToArr(result))