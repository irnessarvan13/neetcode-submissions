class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()  #Create a set

        for num in nums:   #Go through each number in nums
            if num in seen:  #If the number is in seen
                return True  #Return True
            seen.add(num)    #If its not in seen, then add it to seen
        
        return False         #Else return False