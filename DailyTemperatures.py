class Solution(object):
    # tc : O(2n) 2n becuase we have to pop up the elements from the stack and update them with the values to so one n to move forward, 1n backwar, 2 does n't matter O(n), sc : O(1)
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # approach : using a stack where if the curr temperature if greater than the temperature at the peek of stack then we will pop out as found the next warmer day, and update that day with  currindex- peek elment index , this value represent the next warmer day 

        stack = []
        stack.append([temperatures[0],0]) # update the intial day temperature and the index
        output = [0]*(len(temperatures))

        for i in range(1,len(temperatures)):
            while stack:
                prev_temperature, index = stack[-1]
                if temperatures[i] > prev_temperature:
                    stack.pop() # pop it up 
                    output[index] = i - index # update with the future warmer day
                else:
                    break
            # if the day was not greater then lets break it 
            # and we need to append this day into out stack to find the futrue warmer day for it
            stack.append([temperatures[i], i])
                
        
        # after the for loop if the stakc was not empty that means they dont have any warmer day and for them its 0 which is alread taken care while intializing the output

        return output
