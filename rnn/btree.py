class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

def search(value, node):
    if node is None or node.value == value:
        return node

    elif value < node.value:
        return search(value, node.leftChild)


    else:
        return search(value, node.rightChild)
