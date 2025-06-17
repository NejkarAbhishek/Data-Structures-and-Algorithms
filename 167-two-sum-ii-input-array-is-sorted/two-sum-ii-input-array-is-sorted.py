class Solution(object):
    def twoSum(self, numbers, target):
        
        L , R =0,len(numbers)-1

        while L < R:
            if numbers[L] + numbers[R]<target:
                L+=1
            elif numbers[L] + numbers[R] >target:
                R-=1
            else:
                return [L+1,R+1]
        
        return [-1,-1]

   