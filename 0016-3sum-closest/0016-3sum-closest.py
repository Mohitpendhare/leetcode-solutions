class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        max_diff = float('inf')
        res = []

        for i in range(0,n-2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                d = abs(total - target)

                if max_diff > d:
                    max_diff = d
                    res = total

                if total == target:
                    return res 
                
                if total < target:
                    left += 1
                
                else:
                    right -= 1
        
        return res
