class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    
        res=s.split()
        print(res)
        if len(res)==0:
            return 0
        return len(res[-1])
        
        