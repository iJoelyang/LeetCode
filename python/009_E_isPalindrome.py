# -*- coding: utf-8 -*-
"""
题目：回文数
难度: 简单
描述:
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        p, q = 0, len(s) - 1
        while p != q and p < q:
            if s[p] != s[q]:
                return False
            p += 1
            q -= 1

        return True


if __name__ == '__main__':
    num = 121
    s = Solution()
    print(s.isPalindrome(num))
