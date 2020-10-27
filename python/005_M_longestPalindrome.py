# -*- coding: utf-8 -*-
"""
题目：最长回文串
难度: 中等
描述:
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    def isPalindrome(self, s):
        p = 0
        q = len(s) - 1
        while p != q and p < q:
            if s[p] != s[q]:
                return False
            p += 1
            q -= 1

        return True

    def longestPalindrome1(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        max_len = 0
        ret = ""

        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                palindrome = s[i:j]
                if self.isPalindrome(palindrome):
                    length = len(palindrome)
                    if length > max_len:
                        max_len = length
                        ret = palindrome
        return ret

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        n = len(s)
        ret = ""
        dp = [[False] * n for _ in range(n)]

        # 依次增加字符串长度
        for l in range(0, n):
            for i in range(0, n - l):
                j = l + i
                # 先将主对角线初始化, i==j, 单个字符均为回文
                if l == 0:
                    dp[i][j] = True
                # 长度为2的字符串
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                # 长度>=3的字符串
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                # l + 1 = j - i + 1 字符串长度
                if dp[i][j] and l + 1 > len(ret):
                    ret = s[i:j + 1]
        return ret


if __name__ == '__main__':
    p = 'aba'
    p = 'babad'
    s = Solution()
    print(s.longestPalindrome(p))
