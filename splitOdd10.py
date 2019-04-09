'''
QUESTION :

Given an array of ints, is it possible to divide the ints into two groups, so that the sum of one group is a multiple
of 10, and the sum of the other group is odd. Every int must be in one group or the other. Write a recursive helper
 method that takes whatever arguments you like, and make the initial call to your recursive helper from splitOdd10().
 (No loops needed.)

splitOdd10([5, 5, 5]) → true
splitOdd10([5, 5, 6]) → false
splitOdd10([5, 5, 6, 1]) → true

'''

def find10(nums, target):
    if nums[0]>target:
        if len(nums)>1:
            return find10(nums[1:],target)
        else:
            return [-1]
    else:
        tt = target-nums[0]
        if tt == 0:
            return [nums[0]]
        if len(nums)<2:
            return [-1]
        else:
            q = find10(nums[1:],tt)
            if q[0] != -1:
                q.append(nums[0])
                return q
            else:
                return find10(nums[1:],target)

 # This function (find10) finds and returns array of numbers whose sum equals to the target. If no
 # such group is found, an array is returned with -1

def make10(nums):
    if len(nums)==0:
        return [-1]
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    target = int((sum-(sum%10))/10)
    for x in range(1, target+1):
        a = find10(nums,x*10)
        if a[0] != -1:
            break
    if a[0]!=-1:
        for p in range(len(a)):
            id = nums.index(a[p])
            if id+1<len(nums):
                nums = nums[0:id] + nums[id+1:]
            else:
                nums = nums[0:id]
        return nums
    else:
        return [-1]

# This function (make10) first sums the array and then takes the Highest multiple of 10 (Hx) which is less than
# the sum of the array. It then loops the array x no of times by setting target as 10 and its multiples
# till the highest multiple (Hx). if a match is found at the lowest level, the numbers returned in the array
# from find10 are then removed and this new array is returned. The find10 numbers can also be added in the resultant
# array by adding return [nums,a]

def sumArray(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

def splitOdd10(nums):
    if sumArray(nums)<10:
        if sumArray(nums)%2==1:
            return True
        else:
            return False
    arr = make10(nums)
    if arr[0] == -1:
        return False
    else :
        a = sumArray(arr)
        if a%2==1:
            return True
        else:
            return False

# Test Cases :

print (splitOdd10([5, 5, 5]))               # Returns True
print (splitOdd10([5,5,6]))                 # Returns False
print (splitOdd10([5, 5, 6, 1]))            # Returns True
print (splitOdd10([6, 5, 5, 1]))            # Returns True
print (splitOdd10([6, 5, 5, 1, 10]))        # Returns True
print (splitOdd10([6, 5, 5, 5, 1]))         # Returns False
print (splitOdd10([1]))                     # Returns True
print (splitOdd10([]))                      # Returns False
print (splitOdd10([10, 7, 5, 5]))           # Returns True
print (splitOdd10([10, 0, 5, 5]))           # Returns False
print (splitOdd10([10, 7, 5, 5, 2]))        # Returns True
print (splitOdd10([10, 7, 5, 5, 1]))        # Returns False

