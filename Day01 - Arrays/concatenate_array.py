class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
    
sol = Solution()
print(sol.getConcatenation([1,2,3]))
print(sol.getConcatenation([1,3,2,1]))