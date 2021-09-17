def construct_tree(prel, inl): #元素的数据结构为树节点
    root = prel[0]
    inl_index = inl.index(root)
    root.left = construct_tree(prel[1:inl_index +1], inl[0:inl_index])
    root.right = construct_tree(prel[inl_index + 1:], inl[inl_index+1:])
    return root

def back_trav(root):
    if not root:
        return []
    stack = [root]
    res = []
    while len(stack) > 0:
        tmp = stack.pop()
        res.append(tmp)
        if tmp.left:
            res.append(tmp.left)
        if tmp.right:
            res.append(tmp.right)
    return res[::-1]