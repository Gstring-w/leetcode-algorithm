import json
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """ 解法一
        max = 0
        for i in range(len(prices) - 1):
            j = i + 1
            d = prices[j] - prices[i]
            if d > 0:
                max += d #有利润就卖
        return max
        """
        #   解法二
        # 动态规划的角度来考虑问题
        l = len(prices)
        if l == 0:
            return 0
        dp = [0] * l
        dp[0] = 0
        for i in range(1, l):
            dp[i] = max(dp[i-1], dp[i-1] + prices[i] - prices[i-1])
        return dp[l-1]

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            prices = stringToIntegerList(line)
            
            ret = Solution().maxProfit(prices)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

"""
在控制台执行代码
zp-MACdeMacBook-Pro:List zpmac$ python3 122maxProfit.py
接着输入数组
[7, 1, 5, 3, 6, 4]
7
[1, 2, 3, 4, 5]
4
"""