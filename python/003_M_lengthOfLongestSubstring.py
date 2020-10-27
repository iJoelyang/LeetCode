# -*- coding: utf-8 -*-
"""
题目：无重复字符的最长子串
难度: 中等
描述:
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sub = s[0]
        max_len = 1

        for i in range(1, len(s)):
            if s[i] not in sub:
                sub += s[i]
            else:
                index = sub.index(s[i])
                sub = sub[index + 1:] + s[i]

            max_len = len(sub) if len(sub) > max_len else max_len

        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abca"))
