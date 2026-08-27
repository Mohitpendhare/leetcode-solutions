class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        a = 0
        b = len(numbers) - 1
        while a < b : 
            sum = numbers[a] + numbers[b]
            if sum == target :  
                return [a+1, b+1]
            elif sum < target :  
                a +=1 
            else : 
                b -=1
        
        