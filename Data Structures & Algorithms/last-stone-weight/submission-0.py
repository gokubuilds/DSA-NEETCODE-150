class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stack=[]
        stack.append(stones[0])
        for i in range(1,len(stones)):
            diff= abs(stones[i]-stack.pop())
            stack.append(diff)
        return stack.pop()

        