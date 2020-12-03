'''
    递归
    平衡二叉树：左子树和右子树高度差小于等于1
'''

from binary_tree import n1

def isBalanced(root):
    if root is None:
        return 0, True

    left_depth, left_ba = isBalanced(root.left)
    right_depth, right_ba = isBalanced(root.right)
    return max(left_depth, right_depth) + 1, abs(left_depth - right_depth) <= 1 and left_ba and right_ba


print(isBalanced(n1))