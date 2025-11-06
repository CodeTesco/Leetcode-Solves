class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def arrayToLinkedList(arr):
    if (not arr):
        return None
    
    linkedList = ListNode(arr[0])
    current = linkedList

    for el in arr[1:]:
        current.next = ListNode(el)
        current = current.next

    return linkedList

def linkedListToArray(head):
    arr = []
    current = head

    while current:
        arr.append(current.val)
        current = current.next

    return arr

def reverseKGroup(head, k):
    current = head
    l = head
    r = head
    lCount = 0
    rCount = k - 1
    prevL = None
    prevR = head
    count = k - 1

    while count > 0:
        r = r.next
        count -= 1

    def reversePairs(l, r, prevL, prevR, lCount, rCount, k):
        nonlocal head
        current = head
        for i in range(rCount):
            prevR = current
            current = current.next

        if (lCount >= rCount):
            return
        
        if (k == 2):
            l.next = r.next
            r.next = l
        elif (k > 2):
            lNext = l.next
            prevR.next = l
            l.next= r.next
            r.next = lNext
        if (prevL == None):
            head = r
        else:
            prevL.next = r

        lCount += 1
        rCount -= 1
        k -= 2
        reversePairs(r.next, prevR, r, prevR, lCount, rCount, k)
    
    length = 0
    while current:
        length += 1
        current = current.next
    current = head
    div = length // k
    left = 0
    right = left + k - 1
    mult = k

    for i in range(div):
        reversePairs(l, r, prevL, prevR, lCount, rCount, mult)

        if (i == div - 1):
            break
        left = right + 1
        right = left + k - 1
        lCount = left
        rCount = right
        l = head
        r = head

        for i in range(lCount):
            prevL = l
            l = l.next
        for i in range(rCount):
            prevR = r
            r = r.next

    return head

linkedList = arrayToLinkedList([1,2,3,4,5,6])
head = reverseKGroup(linkedList, 2)
print(linkedListToArray(head))

# [4,2,3,1,5,6]
# print(l.val)
# print(l.next.val)
# print(prevL.val if not (prevL == None) else None)
# print(f"lcount = {lCount}")
# print(r.val)
# print(r.next.val)
# print(prevR.val)
# print(f"rcount = {rCount}")
# print(head.val)
# print(head.next.val)
# print(head.next.next.val)
# print(linkedListToArray(head))
# print("")