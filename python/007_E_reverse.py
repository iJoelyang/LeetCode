# -*- coding: utf-8 -*-
"""
题目：整数反转
难度: 中等
描述:
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def __reverse(self, x):
        flag = True if x > 0 else False
        boundary = (1 << 31) - 1 if flag else (1 << 31)
        val, x = 0, abs(x)
        while x:
            val = val * 10 + x % 10
            x = x // 10
            if val > boundary:
                return 0
        return val if flag > 0 else -val

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            return self.__reverse(x)

    def reverse2(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            x = int('-' + s[1:][::-1])
        else:
            x = int(s[::-1])
        return x if -2147483648 < x < 2147483647 else 0


if __name__ == '__main__':
    num = 120
    s = Solution()
    print(s.reverse(num))
