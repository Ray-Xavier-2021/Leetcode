# Fizz Buzz Loop
'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
'''
def fizzBuzz(n):
  """
  :type n: int
  :rtype: List[str]
  """
  results = [num for num in range(1, n + 1)]

  # for num in results:
  #   if num % 3 == 0 and num % 5 == 0:
  #     results.append('FizzBuzz')
  #   elif num % 3 == 0:
  #     results.append('Fizz')
  #   elif num % 5 == 0:
  #     results.append('Buzz')
  #   else:
  #     results.append(str(num))


  # for num in range(1, n + 1):
  #   if num % 3 == 0 and num % 5 == 0:
  #     results.append('FizzBuzz')
  #   elif num % 5 == 0:
  #     results.append('Buzz')
  #   elif num % 3 == 0:
  #     results.append('Fizz')
  #   else:
  #     results.append(str(num))
    # print(num)


  print(results)

  # print(results[0] % 3)
  # print(results[1] % 3)
  # print(results[2] % 3)

  return results

ex1 = fizzBuzz(15)
# ex2 = fizzBuzz(5)
# ex3 = fizzBuzz(15)

print(ex1)
# print(ex2)
# print(ex3)