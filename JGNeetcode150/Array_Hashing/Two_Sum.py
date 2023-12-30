class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
        return None
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         j = i + 1
    #         while j <len(nums):
    #             total = nums[i] + nums[j]
    #             if total == target:
    #                 return [i, j]
    #             else:
    #                 j+=1
    #     return None