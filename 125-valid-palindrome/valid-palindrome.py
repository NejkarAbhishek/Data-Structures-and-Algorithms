class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L, R=0,len(s)-1
        while L<R:
            if not s[L].isalnum():
                L+=1
                continue
            elif not s[R].isalnum():
                R-=1
                continue
            else:
                if s[L].lower()!=s[R].lower():
                    return False
            L+=1
            R-=1
        return True