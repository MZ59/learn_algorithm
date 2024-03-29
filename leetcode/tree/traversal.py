from binary_tree import n1

def front_trav(root):
    if not root:
        return []
    ll = [root]
    result = []
    while len(ll) > 0:
        tmp = ll.pop()
        result.append(tmp.val)
        if tmp.right:
            ll.append(tmp.right)
        if tmp.left:
            ll.append(tmp.left)
    return result

def mid_trav(root):
    if not root:
        return []
    ll = []
    result = []
    node = root
    while len(ll) != 0 or node:
        # node = ll.pop()
        if node:
            ll.append(node)
            node = node.left
        else:
            node = ll.pop()
            result.append(node.val)
            node = node.right
            # ll.append(node.right)
    return result

def back_trav(root):
    if not root:
        return []
    stack = [root]
    result = []
    while len(stack) > 0:
        tmp = stack.pop()
        result.append(tmp.val)
        if tmp.left:
            stack.append(tmp.left)
        if tmp.right:
            stack.append(tmp.right)
    return result[::-1]

def mid_trav_2(root):
    if not root:
        return []
    ll = []
    node = root
    result = []
    while len(ll) > 0 or node:
        if node:
            ll.append(node)
            node = node.left
        else:
            node = ll.pop()
            result.append(node.val)
            node = node.right
    return result



print(front_trav(n1))
print(mid_trav(n1))
print(mid_trav_2(n1))
print(back_trav(n1))

def front_trav_tmp(root):
    if not root:
        return []
    ll = [root]
    res = list()
    while len(ll) > 0:
        tmp = ll.pop()
        res.append(tmp.val)
        if tmp.right:
            ll.append(tmp.right)
        if tmp.left:
            ll.append(tmp.left)
    return res
print(front_trav_tmp(n1))

def mid_trav_tmp(root):
    if not root:
        return []
    node = root
    ll = []
    res = list()
    while len(ll) != 0 or node:
        if node:
            ll.append(node)
            node = node.left
        else:
            tmp = ll.pop()
            res.append(tmp.val)
            node = tmp.right
    return res
print(mid_trav_tmp(n1))


def back_trav_tmp(root):
    if not root:
        return []
    stack = [root]
    res = []
    while len(stack) > 0:
        tmp = stack.pop(0)
        res.append(tmp.val)
        if tmp.left:
            stack.append(tmp.left)
        if tmp.right:
            stack.append(tmp.right)
    return res[::-1]
print(back_trav_tmp(n1))
