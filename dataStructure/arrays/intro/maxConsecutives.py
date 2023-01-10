# Max Consecutive One's
'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
def findMaxConsecutiveOnes(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  length = len(nums)
  print('len', length)
  
  countNums = 0

  consecutiveNum = 0
  
  for num in nums:

    # Check if num is 1
    if num == 1:
      print('ok', num)
      # Update count to zero
      countNums += 1
      # Update consecutive nums
      consecutiveNum = max(consecutiveNum, countNums)
    else:
      # Count resets to zero
      countNums = 0

    print(consecutiveNum)

  return consecutiveNum


nums1 = [1, 1, 0, 1, 1, 1]
nums2 = [1, 0, 1, 1, 0, 1]

ex1 = findMaxConsecutiveOnes(nums1)
# ex2 = findMaxConsecutiveOnes(nums2)

print(ex1)