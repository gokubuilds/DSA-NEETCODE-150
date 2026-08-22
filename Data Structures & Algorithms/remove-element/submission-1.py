class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums:
            if nums[i]==val:
                del nums[i]
                continue
        return nums