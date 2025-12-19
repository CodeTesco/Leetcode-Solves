import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def arrToLinked(arr):
    linkedList = ListNode(arr[0])
    current = linkedList

    for el in arr[1:]:
        current.next = ListNode(el)
        current = current.next
    
    return linkedList

def linkedToArr(linkedList):
    arr = []
    current = linkedList

    while current:
        arr.append(current.val)
        current = current.next

    return arr

def deleteMiddleNode(head):
    n = 0
    current = head

    while current:
        n += 1
        current = current.next

    mid = math.floor(n/2)
    count = 0
    current = head

    while current:
        if count == mid - 1:
            current.next = current.next.next
        current = current.next
        count += 1
    return head

head = arrToLinked([2])
edited = deleteMiddleNode(head)
print(linkedToArr(edited))