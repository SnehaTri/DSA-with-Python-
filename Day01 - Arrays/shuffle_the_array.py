class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i+n]

        j = 2*n - 1
        for i in range(n-1, -1, -1):
            y = nums[i] & (2**10 - 1)
            x = nums[i] >> 10
            nums[j] = y
            nums[j-1] = x
            j -= 2
        return nums
    
sol = Solution()
print(sol.shuffle([2,5,1,3,4,7], 3))
print(sol.shuffle([1,2,3,4,4,3,2,1], 4))
print(sol.shuffle([1,1,2,2], 2))