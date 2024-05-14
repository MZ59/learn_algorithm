'''
多个区间，将有重叠的区间进行合并
Input: [[1,5],[2,6],[7,12],[17,21]]
Output: [[1,6],[7,12],[17,21]]
解释: 由于[1,5] 和 [2,6] 有重叠区域, 合并为 [1,6].
'''

def soulution(input):
    sinput = sorted(input, key = lambda x:x[0])
    output = list()
    output.append(sinput[0])
    for i in range(1, len(input)):
        if sinput[i][0] <= output[-1][1]:
            left = min(sinput[i][0], output[-1][0])
            right = max(sinput[i][1], output[-1][1])
            output[-1] = [left, right]
        else:
            output.append(sinput[i])
    return output

if __name__ == '__main__':
    input = [[1,8],[2,6],[7,12],[17,21]]
    # import pdb;pdb.set_trace()
    print(soulution(input))




