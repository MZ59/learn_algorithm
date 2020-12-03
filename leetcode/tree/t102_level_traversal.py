from binary_tree import n1

def binary_traversal(root):
    if not root:
        return []
    tmp = [root]
    result = []
    hight = 0
    while len(tmp) != 0:
        hight += 1
        r_tmp = []
        for i in range(len(tmp)):
            node = tmp.pop(0)
            r_tmp.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        if hight % 2 == 0:
            r_tmp.reverse()
        result.append(r_tmp)
    return result#[::-1]

print(binary_traversal(n1))
