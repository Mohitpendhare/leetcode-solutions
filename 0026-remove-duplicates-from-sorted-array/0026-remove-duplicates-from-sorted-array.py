class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      count = 1

      if not nums:
        return 0
        
      for i in range(1,len(nums)):
        if nums[i-1] != nums[i]:
            nums[count] = nums[i]
            count += 1
      return count



        
        
    

