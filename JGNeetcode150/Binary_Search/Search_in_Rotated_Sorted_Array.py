class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = nums[0]
        right = nums[len(nums) - 1]
        if target == left:
            return 0
        elif target == right:
            return len(nums) - 1
        elif target > left:
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < left:
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        elif target < right:
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l+r)//2
                print(mid)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > right:
                    l = mid +1
                elif nums[mid] < target:
                    l = mid +1
                else:
                    r = mid -1
            return -1
        else:
            return -1