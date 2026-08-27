class Solution:
    from typing import List
    def sortedSquares(self, nums: List[int]) -> List[int]:
        siz = len(nums)
        neg = []
        pos = []
        #seperate negative and positive numbers
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        #1 if there is no negative   
        if len(neg) == 0:
                return[x * x for x in pos]
        #2 if there is no positive
        if len(pos) == 0:
                res = [x * x for x in neg]      # res = result
                res.reverse()
                return res
        #3 if both exist 
        neg = [x * x for x in neg][::-1]
        pos = [x * x for x in pos]
        n, m = len(neg), len(pos)
        res = []

        i = 0 
        j = 0
        while i < n and j < m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1    
            else:
                res.append(pos[j])
                j += 1
# while loop khatam hogaya
        while i < n:
            res.append(neg[i])
            i += 1
            
        while j < m:
            res.append(pos[j])
            j += 1
            
        return res


