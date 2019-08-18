class Solution(object):
    """
    Your runtime beats 93.79 % of python submissions.
    """
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        while n != 0:
            num += n & 1
            n >>= 1
        return num


if __name__ == '__main__':
    solution = Solution()
    n = '00000000000000000000000010000000'
    n = int(n, 2)
    res = solution.hammingWeight(n)
    print(res)
