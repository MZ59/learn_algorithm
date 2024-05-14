def removeElement(nums, val):
    p1 = 0
    p2 = 1
    m = len(nums)
    while p2 < m:
        if nums[p1] == val:
            if nums[p2] != val:
                nums[p1] = nums[p2]
                nums[p2] = val
                p1+=1
                p2+=1
            else:
                p2 += 1
    return p1

if __name__ == '__main__':
    import pdb;pdb.set_trace()
    removeElement([0,1,2,2,3,0,4,2], 2)