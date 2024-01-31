"""
Date: January 31, 2024
Name: Rajashree Dahal
Problem: You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=[]
        while l1:
            num1.append(l1.val)
            l1=l1.next
        num2=[]
        while l2:
            num2.append(l2.val)
            l2=l2.next
        
        num1.reverse()
        num2.reverse()
        num1=[str(i) for i in num1]
        num2=[str(i) for i in num2]
        num1="".join(num1)
        num2="".join(num2)
        result=int(num1)+int(num2)
        result=str(result)
        result=[int(i) for i in result]
        dummy = ListNode()
        current = dummy
        result.reverse()
        for digit in result:
            current.next = ListNode(int(digit))
            current = current.next
        return dummy.next



        