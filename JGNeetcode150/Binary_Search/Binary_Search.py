import math
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums)-1
        while begin <= end:
            mid = math.floor((begin + end)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                begin = mid + 1
            else:
                end = mid - 1
        return -1