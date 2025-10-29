class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # have to check circular way 
        # using stack and loop it over 2n times, and if the curr value is greater thne the peek element in the stack we got the higest valeu for it, but if not then we hae to check in a circular way thats' why iterate over 2 n times
        # and in the circular way if we are about to insert the same index into our stack that means we haven't found the higheest elemetn for this index to the right side of the arr of in teh circualr way the left of it either 
        # then we break it and leave the valeu for them s -1

        output = [-1]*len(nums)
        stack = [] 
        stack = [[nums[0], 0]] # intially append the first element and its index
        n = len(nums)
        
    
        for i in range(1,2*n):
            i = i%n # to move to the circular way wil take the mod of the index
            
            while stack and nums[i] > stack[-1][0]:
                index = stack[-1][1]
                stack.pop()
                output[index] = nums[i]
            stack.append([nums[i],i])
        
        return output