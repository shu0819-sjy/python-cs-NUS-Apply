# LeetCode 1480. 一维数组的动态和
class Solution:
    def runningSum(self, nums):
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        return nums

# 测试用例
if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    print("动态和数组：", sol.runningSum(nums))  # 输出: [1,3,6,10]
