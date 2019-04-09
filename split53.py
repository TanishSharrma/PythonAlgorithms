'''

QUESTION :

Given an array of ints, is it possible to divide the ints into two groups, so that the sum of the two groups
 is the same, with these constraints: all the values that are multiple of 5 must be in one group, and all the
 values that are a multiple of 3 (and not a multiple of 5) must be in the other. (No loops needed.)

split53([1, 1]) → true
split53([1, 1, 1]) → false
split53([2, 4, 2]) → true

'''

def sumArray(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

def split53(nums):
    five = []
    numsX = []
    three = []
    if len(nums)<2:
        return False
    for i in range(len(nums)):
        if nums[i]%5==0:
            five.append(nums[i])
        elif nums[i]%3==0:
            three.append(nums[i])
        else:
            numsX.append(nums[i])
    fsum = sumArray(five)
    tsum = sumArray(three)
    if len(numsX)==0:
        return (fsum==tsum)
    elif len(numsX)==1:
        return (numsX[0]+fsum==tsum or numsX[0]+tsum==fsum)
    else:
        p = abs(tsum-fsum)
        m = sumArray(numsX)-p
        if m%2==1:
            return False
        else:
            m = m/2
            return groupSum(numsX,m)

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

# Test Cases :

print(split53([1, 1]))
print(split53([1, 1, 1]))
print(split53([2, 4, 2]))
print(split53([2, 2, 2, 1]))
print(split53([3, 3, 5, 1]))
print(split53([3, 5, 8]))
print(split53([2, 4, 6]))
print(split53([3, 5, 6, 10, 3, 3]))


