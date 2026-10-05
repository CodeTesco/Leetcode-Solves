def deleteNode(root, key):
    def findMin(node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    if root is None:
        return root
    
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        successor = findMin(root.right)
        root.val = successor.val

        root.right = deleteNode(root.right, successor.val)

    return root