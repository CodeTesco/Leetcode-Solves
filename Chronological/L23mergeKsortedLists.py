class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    arr = []

    def arrayToLinkedList(arr):
        if (not arr):
            return None
        
        head = ListNode(arr[0])
        current = head

        for el in arr[1:]:
            current.next = ListNode(el)
            current = current.next
        
        return head
    
    arr2d = []

    current = lists
    while current:
        arr.extend(current.val)
        current = current.next
    print(arr)

    # for head in lists:
    #     subArr = []
    #     while head:
    #         subArr.append(head.val)
    #         head = head.next
    #     arr2d.append(subArr)
    
    # for subArr in arr2d:
    #     arr.extend(subArr)
    # print(arr)
    
    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        arr1 = [0] * n1
        arr2 = [0] * n2

        for i in range(n1):
            arr1[i] = arr[left + i]
        for j in range(n2):
            arr2[j] = arr[mid + 1 + j]

        i = 0
        j = 0
        k = left
        while i < n1 and j < n2:
            if (arr1[i] <= arr2[j]):
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = arr1[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = arr2[j]
            j += 1
            k += 1
    
    def mergeSort(arr, left, right):
        if(left < right):
            mid = (left + right) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)
            merge(arr, left, mid, right)
    
    mergeSort(arr, 0, len(arr) - 1)
    linked = arrayToLinkedList(arr)

    return linked


def arrayToLinkedList(arr):
    if (not arr):
        return None
    
    head = ListNode(arr[0])
    current = head

    for el in arr[1:]:
        current.next = ListNode(el)
        current = current.next
    
    return head

head = mergeKLists(arrayToLinkedList([[1,2,3],[4,5,6,7]]))

current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")


# def linkedListToArray(head):
#     subArr = []
#     current = head
#     print(current)
#     while current:
#         subArr.append(current.val)
#         print(subArr)
#         current = current.next
    
#     return subArr