# class ChainNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mine_p(matrix):
    #import pdb;pdb.set_trace()
    while len(matrix) > 0:
        col = len(matrix[0])
        if col == 0:
            break
        for i in range(col):
            print(matrix[0][i])
        matrix.pop(0)
        #import pdb;pdb.set_trace()
        if len(matrix) > 0:
            matrix = rotate(matrix)

def rotate(mat):
    row = len(mat)
    col = len(mat[0])
    tmp_mat = []
    for j in range(col):
        tmp_col = []
        for i in range(row):
            tmp_col.append(mat[i][col - j - 1])
        tmp_mat.append(tmp_col)
    return tmp_mat

input = [[1,2,3], [4,5,6], [7,8,9]]
mine_p(input)
