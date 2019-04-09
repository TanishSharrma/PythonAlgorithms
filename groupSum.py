def groupSum (nums, target):
    if target==0:
        return True
    if len(nums)<1:
        return False
    arraysum = 0
    for i in range(0,len(nums)):
        arraysum += nums[i]
    if arraysum < target :
        return False
    if arraysum == target or nums[0] == target:
        return True
    if len(nums) == 1 and nums[0] != target:
        return False
    if nums[0]<target:
        tt = target-nums[0]
        if tt == 0:
            return True
        else :
            a = groupSum(nums[1:], tt)
            if a == False:
                return groupSum(nums[1:], target)
            else :
                return True
    else :
        return groupSum(nums[1:], target)


print (groupSum([2, 4, 8], 10))
print (groupSum([2, 4, 8], 14))
print (groupSum([2, 4, 8], 9))
print (groupSum([2, 4, 8], 8))
print (groupSum([2, 4, 8], 8))
print (groupSum([2, 4, 8], 2))
print (groupSum([1], 1))
print (groupSum([9], 1))
print (groupSum([9], 0))
print (groupSum([], 0))
print (groupSum([10, 2, 2, 5], 17))
print (groupSum([10, 2, 2, 5], 15))
print (groupSum([10, 2, 2, 5], 9))



'''

Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums 
to the given target? This is a classic backtracking recursion problem. Once you understand the recursive 
backtracking strategy in this problem, you can use the same pattern for many problems to search a space 
of choices. Rather than looking at the whole array, our convention is to consider the part of the array 
starting at index start and continuing to the end of the array. The caller can specify the whole array 
simply by passing start as 0. No loops are needed -- the recursive calls progress down the array.

groupSum(0, [2, 4, 8], 10) → true
groupSum(0, [2, 4, 8], 14) → true
groupSum(0, [2, 4, 8], 9) → false

'''