#贪心思想
#局部最优：让abs大的负数变为正数,全局最优：sum最大
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        #先按绝对值大小排序
        nums = sorted(nums,key = abs)[::-1]
        for i in range(len(nums)):
            #當有k时
            if k > 0:
                if nums[i] < 0: #有负数,就将负数改为正数
                    nums[i] = abs(nums[i])
                    k -= 1      #次数减一
        #nums = nums[::-1]
        while k > 0:            #如果k还有
            nums[-1] = -nums[-1] #把k都浪费在最小的那个身上
            k -= 1
        return sum(nums)
