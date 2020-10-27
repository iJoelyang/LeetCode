# -*- coding: utf-8 -*-
"""
题目：两数之和
难度: 中等
描述:
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        def dfs(left, right, carry):
            if not left and not right and not carry:
                return None
            val = (left.val if left else 0) + (right.val if right else 0) + carry
            node = ListNode(s % 10)
            node.next = dfs(left.next if left else None, right.next if right else None, val // 10)
            return node

        return dfs(l1, l2, 0)


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        carry = 0
        # dummy head
        head = curr = ListNode()
        while l1 or l2 or carry > 0:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = val // 10

        return head.next
