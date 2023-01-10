# Middle of the Linked List
'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''
def middleNode(head):
  """
  :type head: ListNode
  :rtype: ListNode
  """

  isEven = len(head) % 2 == 0
  isOdd = len(head) % 1 == 0
  print(isEven, head)
  print(isOdd, head)

  evenMiddle = round(len(head) / 2)
  oddMiddle = round(len(head) / 2 -.5)

  if isEven:
    return head[evenMiddle : ], evenMiddle
  elif isOdd:
    return head[oddMiddle : ], oddMiddle

  print(evenMiddle)
  print(oddMiddle)

  return head



head1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
head2 = [1, 2, 3, 4, 5, 6]

ex1 =middleNode(head1)
ex2 =middleNode(head2)

print('length', len(ex1))
print('length', len(ex2))
print('head', ex1)
print('head', ex2)