"""
Date: February 29, 2024
Name: Rajashree Dahal
Project:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first_list=dummy=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
               first_list.next=list1
               list1=list1.next
            else: 
                first_list.next=list2
                list2=list2.next
            first_list=first_list.next
        if list1 or list2:
            first_list.next=list1 if list1 else list2 
        return dummy.next

