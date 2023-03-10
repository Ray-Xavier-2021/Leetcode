#  Find Numbers with Even Number of Digits
'''
Given an array nums of integers, return how many of them contain an even number of digits.

 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 105
'''
def findNumbers(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  isEvenNums = 0
  length = len(nums)
  print('length', length)

  digits = []
  # Count digits
  test = [digits.append(list(str(num))) for num in nums]
  print('digits', digits)
  for pair in digits:
    # print(len(pair))
    # Check if even numbers
    if len(pair) % 2 == 0:
      isEvenNums += 1

      print(isEvenNums) 
      print(pair)



  return isEvenNums





nums1 = [12,345,2,6,7896]
nums2 = [555,901,482,1771]

ex1 = findNumbers(nums1)

print(ex1)