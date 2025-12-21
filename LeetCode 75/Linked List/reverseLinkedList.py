class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linkedToArr(head):
    arr = []
    current = head

    while current:
        arr.append(current.val)
        current = current.next

    return arr

def arrToLinked(arr):
    head = ListNode(arr[0])
    current = head

    for el in arr[1:]:
        current.next = ListNode(el)
        current = current.next
    
    return head

def reverseList(head):
    if head is None or head.next is None:
        return head
    
    rest = reverseList(head.next)

    head.next.next = head
    head.next = None

    return rest

linked = arrToLinked([1,2,3,4,5])
revList = reverseList(linked)
print(linkedToArr(revList))