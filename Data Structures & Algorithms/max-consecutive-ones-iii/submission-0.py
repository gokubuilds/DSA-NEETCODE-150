class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes=0
        maxcount=0
        start=0
        for i,el in enumerate(nums):
            if el==0:
                zeroes+=1
            while zeroes>k:
                if nums[start]==0:
                    zeroes-=1
                start+=1
            maxcount=max(i-start+1,maxcount)
        return maxcount
        