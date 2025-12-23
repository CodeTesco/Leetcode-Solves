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

def pairSum(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    maxSum = 0
    first = head
    curr = prev

    while curr:
        sum = curr.val + first.val
        maxSum = max(sum, maxSum)
        curr = curr.next
        first = first.next

    return maxSum

head = arrToLinked([5,4,2,1])
result = pairSum(head)
print(result)