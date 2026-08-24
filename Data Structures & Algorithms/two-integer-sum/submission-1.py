class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        li = []
        for i in range(round(n)):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    li.append(i)
                    li.append(j)
                    return li
