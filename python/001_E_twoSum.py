# -*- coding: utf-8 -*-
"""
题目：两数之和
难度: 简单
描述:
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums: list, target: int):
        hash_nums = {}
        for index, num in enumerate(nums):
            another = target - num
            if another in hash_nums.keys():
                return [hash_nums[another], index]
            hash_nums[num] = index


if __name__ == '__main__':
    nums, target = [1, 3, 3, 4, 6], 6
    s = Solution()
    print(s.twoSum(nums=nums, target=target))
