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
        curr_node = answer
        carry = 0
        while l1 != None or l2 != None:
            a=0
            b=0
            if l1 !=None:
                a = l1.val
            if l2 !=None:
                b= l2.val
            answer_val = a + b +carry
            print("a is "+str(a))
            print("b is "+ str(b))
            print("carry is "+ str(carry))
            print("answer val is "+str(answer_val))
            if answer_val >= 10:
                carry = 1 
                answer_val = answer_val % 10
            else:
                carry =0
            
            curr_node.val = answer_val
            if  ( (l1 == None and l2 != None and l2.next !=None) or
                    (l2 == None and l1 != None and l1.next !=None) or
                    ((l1 != None and l2 != None) and (l1.next != None or l2.next != None))):
                curr_node.next = ListNode()

            else:
                if carry == 1:
                    curr_node.next = ListNode(1)
                else:
                    curr_node.next=None
                    break
            curr_node= curr_node.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        return answer
            
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