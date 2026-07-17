class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mpp1 = [0]*26
        mpp2 = [0]*26
        for i in range(len(s)):
            mpp1[ord(s[i])-ord('a')] +=1
            mpp2[ord(t[i])-ord('a')] +=1
        for i in range(len(s)):
            if mpp1[ord(s[i])-ord('a')] != mpp2[ord(s[i])-ord('a')]:
                return False
        return True

        
        