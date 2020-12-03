'''
    层次遍历
'''

from binary_tree import n1

# print(n1.left.val)
def max_depth(root):
    if root is None:
        return 0
    depth = 0
    nodes = [root]
    while len(nodes) != 0:

        depth += 1
        for i in range(len(nodes)):
            tmp = nodes.pop(0)
            if tmp.left is not None:
                nodes.append(tmp.left)
            if tmp.right is not None:
                nodes.append(tmp.right)
    return depth

def max_depth2(root):

    if root is None:
        return 0
    if root.left is not None:
        left_depth = max_depth2(root.left)
    else:
        left_depth = 0
    if root.right is not None:
        right_depth = max_depth2(root.right)
    else:
        right_depth = 0
    return max(left_depth, right_depth) + 1

print(max_depth2(n1))

