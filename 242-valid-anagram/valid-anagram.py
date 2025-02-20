class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        countS,countT={},{}

        for index in range(len(s)):
            countS[s[index]]=1+countS.get(s[index],0)
            countT[t[index]]=1+countT.get(t[index],0)
        
        return countS==countT