class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start=0
        end=k-1
        res=[]
        while end<len(nums) :
            res.append(max(nums[start:end+1]))
            start+=1
            end+=1
        return res

        