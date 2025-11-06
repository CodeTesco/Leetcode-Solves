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

def linkedListToArray(linkedList):
    arr = []
    current = linkedList

    while current:
        arr.append(current.val)
        current = current.next

    return arr

def swapPairs(head):
    cur = head
    prev = None
    
    while cur and cur.next:
        Node1 = cur
        Node2 = cur.next
        Node1.next = Node2.next
        Node2.next = Node1
        if (prev == None):
            head = Node2
        else:
            prev.next = Node2
        prev = Node1
        cur = Node1.next
    
    # print(linkedListToArray(head))
    return head

# [3, 2, 1, 4]
# [1,2,3,4,5,6,7,8]
linkedList = arrayToLinkedList([1,2,3])
print(swapPairs(linkedList))
# print(linkedListToArray(head))