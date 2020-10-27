# -*- coding: utf-8 -*-
"""
题目：盛最多水的容器
难度: 中等
描述:
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为(i, ai)
和(i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
"""


class Solution:
    def maxArea(self, height):
        p, q = 0, len(height) - 1
        max_area = (q - p) * min(height[p], height[q])
        while p < q:
            if height[p] <= height[q]:
                p = p + 1
            else:
                q = q - 1

            area = (q - p) * min(height[p], height[q])
            if area > max_area:
                max_area = area
        return max_area


if __name__ == '__main__':
    nums = [2, 3, 4, 5, 18, 17, 6]
    s = Solution()
    print(s.maxArea(nums))
