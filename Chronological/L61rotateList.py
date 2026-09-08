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

def rotateRight(head, k):
    count = 0
    current = head
    if current is None or current.next is None:
        return head

    while current is not None:
        count += 1
        current = current.next
    
    k = k % count
    for _ in range(k):
        curr = head
        prev = None

        while curr.next:
            prev = curr
            curr = curr.next

        curr.next = head
        prev.next = None
        head = curr

    return head


head = arrToLinked([1,2,3,4,5])
result = rotateRight(head, 2)
print(linkedToArr(result))
