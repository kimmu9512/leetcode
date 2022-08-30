#this is my attempt of the two sum problem after looking at the solution.
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        answer =''
        if self.next is None:
            answer = str(self.val)
        else:
            answer= str(self.next)+'-'+ str(self.val)
        return answer
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        currNode = answer
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            currNodeVal= (a+b+carry) %10
            carry = 1 if (a+b+carry) >= 10 else 0
            newNode = ListNode(currNodeVal)
            currNode.next = newNode
            currNode=currNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return answer.next



            
a = ListNode(2, ListNode(4, ListNode(3)))
b = ListNode(5, ListNode(6, ListNode(4)))
print(a)
print(b) 
s= Solution()           
c= s.addTwoNumbers(a,b)
print(c)
a = ListNode(0)
b = ListNode(0)
print(a)
print(b) 
s= Solution()           
c= s.addTwoNumbers(a,b)
print(c)
a = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
b = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
print(a)
print(b) 
s= Solution()           
c= s.addTwoNumbers(a,b)
print(c)
a = ListNode(1, ListNode(8))
b = ListNode(0)
print(a)
print(b) 
s= Solution()           
c= s.addTwoNumbers(a,b)
print(c)