class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        # 用循环处理连续的偶数除以2
        while num > 1 and num % 2 == 0:
            num = num // 2
            steps += 1
        # 递归处理奇数或最后一步
        if num == 0:
            return steps
        elif num == 1:
            return steps + 1
        else:
            # 奇数减1后，递归继续处理
            return self.numberOfSteps(num - 1) + 1
