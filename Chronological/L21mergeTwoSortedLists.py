class Node:
    def __init__(self, val):
        self.val = val
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

def linked_to_arr(list):
    cur = list
    arr = []
    while cur:
        arr.append(cur.val)
        cur = cur.next
    
    return arr

def mergeTwoLists(list1, list2):
    list1 = array_to_linked_list(list1)
    list2 = array_to_linked_list(list2)
    n1 = 0
    n2 = 0
    current1 = list1
    current2 = list2
    while current1:
        n1 += 1
        current1 = current1.next
    while current2:
        n2 += 1
        current2 = current2.next

    cur1 = list1
    cur2 = list2
    if (n1 < n2):
        dup = n1
        n1 = n2
        n2 = dup
        cur1 = list2
        cur2 = list1

    if (cur1 and cur2):
        if (cur1.val <= cur2.val):
            sortedList = Node(cur1.val)
            cur1 = cur1.next
        else:
            sortedList = Node(cur2.val)
            cur2 = cur2.next
    else:
        return cur1 if cur1 else cur2
    
    tail = sortedList

    while cur1 and cur2:
        if (cur2.val <= cur1.val):
            tail.next = Node(cur2.val)
            cur2 = cur2.next
        else:
            tail.next = Node(cur1.val)
            cur1 = cur1.next
        tail = tail.next

    tail.next = cur1 if cur1 else cur2
    
    return sortedList
        
head = mergeTwoLists([], [0])
print(head)

current = head
while current:
    print(current.val, end=" -> ")
    current = current.next