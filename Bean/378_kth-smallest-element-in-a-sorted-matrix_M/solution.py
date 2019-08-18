import heapq


class Solution(object):
    """
    Runtime: 368 ms, faster than 8.40% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
    Still a bad solution, try Binary Search Algorithm tomorrow...
    """
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        nums = []
        for row in matrix:
            for ele in row:
                nums.append(ele)

        if k > len(nums):
            return -1

        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k -= 1
        return heapq.heappop(nums)


if __name__ == '__main__':
    solution = Solution()
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    k = 4
    res = solution.kthSmallest(matrix, k)
    print(res)
