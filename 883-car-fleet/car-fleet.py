class Solution(object):
    def carFleet(self, target, position, speed):
        pair = sorted(zip(position, speed), reverse=True)

        stack = []
        for p, s in pair:
            time = (target - p) / float(s)  
            if stack and time <= stack[-1]:
                continue 
            stack.append(time)  

        return len(stack)  
