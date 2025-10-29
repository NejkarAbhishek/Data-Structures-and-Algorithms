class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False


        countS, countT = {},{}

        for a,b in zip(s,t):
            countS[a]= 1 + countS.get(a, 0)
            countT[b]= 1 + countT.get(b, 0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True
        