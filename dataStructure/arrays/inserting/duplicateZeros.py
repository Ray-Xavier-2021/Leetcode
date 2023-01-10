# Duplicate Zeros
'''
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
'''
def duplicateZeros(arr):
  """
  :type arr: List[int]
  :rtype: None Do not return anything, modify arr in-place instead.
  """
  length = len(arr)
  print(length)

  for i in arr:
    # print('nia', i)
    if i == 0:
      arr[i] + 1  == 0
      # print('zero', i)
      # print(i, arr[i])


  # return arr

arr1 = [1,0,2,3,0,4,5,0]
arr2 = [1,2,3]

ex1 = duplicateZeros(arr1)
ex1
# ex2 = duplicateZeros(arr2)

# print(ex1)
# print(ex2)