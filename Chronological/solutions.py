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

def reverseKGroup(self, head, k: int):
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        # Find the k-th node from group_prev
        kth = self.get_kth_node(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next
        
        # Reverse the group
        before = kth.next
        curr = groupPrev.next
        while curr != groupNext:
            after = curr.next
            curr.next = before
            before = curr
            curr = after

        # Reconnect the reversed group with the rest of the list
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
        
    return dummy.next


def get_kth_node(self, curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr