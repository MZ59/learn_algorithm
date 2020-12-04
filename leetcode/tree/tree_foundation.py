#coding=utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
            a:1
       b:2         c:3
    d:4   e:5   f:6     g:7
        
'''

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

#前序遍历，递归 1245367
def preOrderTraverse_recurs(node):
    if not node:
        return None
    print(node.val)
    preOrderTraverse_recurs(node.left)
    preOrderTraverse_recurs(node.right)


# 前序遍历，非递归
def preOrderTraverse(node):
    stack = [node]
    while len(stack) > 0:
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node = stack.pop(-1)




# 中序遍历，递归
def inOrderTraverse_convers(node):
    if not node:
        return None
    inOrderTraverse_convers(node.left)
    print(node.val)
    inOrderTraverse_convers(node.right)

# 中序遍历，非递归
def inOrderTraverse(node):

    stack = []
    pos = node
    while pos or len(stack) > 0:
        if pos:
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop(-1)
            print(pos.val)
            pos = pos.right

# 后序遍历，递归
def postOrderTraverse_convers(node):
    if not node:
        return None
    postOrderTraverse_convers(node.left)
    postOrderTraverse_convers(node.right)
    print(node.val)

# 后序遍历，非递归
def postOrderTraverse(node):
    stack1 = [node]
    stack2 = []
    while len(stack1) > 0:
        node = stack1.pop(-1)
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while len(stack2) > 0:
        print(stack2.pop(-1).val)

#层次遍历
def levelTraverse(node):
    queue = [node]
    while len(queue) > 0:
        tmp = queue.pop(0)
        print(tmp.val)
        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.right)

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []
        high = 1
        while len(queue) > 0:
            level_result = []

            level_len = len(queue)

            for i in range(level_len):
                tmp = queue.pop(0)
                level_result.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            if high % 2 != 0:
                result.append(level_result)
            else:
                result.append(level_result[::-1])
            high += 1
        return result




if __name__ == "__main__":
    # preOrderTraverse_convers(a)
    # preOrderTraverse(a)

    # inOrderTraverse_convers(a)
    # inOrderTraverse_2(a)

    postOrderTraverse_convers(a)
    postOrderTraverse(a)

    levelTraverse(a)


