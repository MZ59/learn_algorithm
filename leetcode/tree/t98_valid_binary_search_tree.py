'''
    二叉搜索树：左节点比根节点小，有节点比根节点大
'''

from binary_tree import n1

def is_Valid(root, low=float("-inf"), high=float("inf")):
    if not root:
        return True
    val = root.val
    if not low < val or not high > val:
        return False
    if not is_Valid(root.left, low, val):
        return False
    if not is_Valid(root.right, val, high):
        return False
    return True

def isValidBST(root):
    return is_Valid(root)
print(isValidBST(n1))

