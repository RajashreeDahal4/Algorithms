"""
Date: February 10, 2024
Name: Rajashree Dahal
Problem: Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(val=0)
        dummy.next=head
        first=dummy
        second=dummy
        for _ in range(n+1):
            first=first.next
        
        while first is not None:
            first=first.next
            second=second.next
        second.next=second.next.next
        return dummy.next