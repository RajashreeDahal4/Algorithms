"""
Date: February 14, 2024
Name: Rajashree Dahal
Problem: Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy
        while curr.next and curr.next.next:
            first=curr.next
            second=curr.next.next
            curr.next=second
            first.next=second.next
            second.next=first
            curr=curr.next.next
        return dummy.next
