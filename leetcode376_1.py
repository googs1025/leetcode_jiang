# 解题思路：贪心
# 如果nums小于2长度 直接返回
# 设置curdiff为现阶段两数组的差 prediff为前一次两数组的差
# 遍历nums,如果 curdiff大于0 and prediff 小于等于0时 result++ 把curdiff 赋值為為prediff

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        curdiff = 0
        prediff = 0
        result = 1

        for i in range(len(nums)-1):
            curdiff = nums[i+1] - nums[i]

            if (curdiff > 0 and prediff <= 0) or (curdiff < 0 and prediff >= 0):
                result += 1
                prediff = curdiff

        return result