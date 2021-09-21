test = [1, 2, 3, 4, 5]
n = len(test)
print(n)
print("###########")
for i in range(0, n, 1): # 从0开始，一直+1， 共加n-0次
    print(test[i])
print("###########")
for j in range(n-1, -1, -1): # 从n-1开始，一直-1， 共减（n-1）-（-1）次
    print(test[j])