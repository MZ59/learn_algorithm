from binary_tree import n1, TreeNode

def insert_search_tree(root, val):
    '''
    :param root: 根节点
    :param val: 插入的值
    :return: 新的二叉搜索树
    '''
    node = root
    while node:
        if val > node.val:
            if not node.right:
                node.right = TreeNode(val)
                return root
            else:
                node = node.right
        else:
            if not node.left:
                node.left = TreeNode(val)
                return root
            else:
                node = node.left
    return TreeNode(val)

