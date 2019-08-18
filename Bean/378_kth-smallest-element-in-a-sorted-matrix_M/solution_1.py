class Solution(object):
    """
    Runtime: 2352 ms, faster than 5.03% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
    Bad solution, it takes too much time, keep looking for a better solution...
    """
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        N = len(matrix)
        indexes = [0] * N
        min_idx = -1

        while k > 0:
            min_idx = -1
            for i in range(0, N):
                if indexes[i] < N and (min_idx < 0 or matrix[i][indexes[i]] < matrix[min_idx][indexes[min_idx]]):
                    min_idx = i
            # print(matrix[min_idx][indexes[min_idx]])
            indexes[min_idx] += 1
            k -= 1

        if indexes[min_idx] > 0:
            return matrix[min_idx][indexes[min_idx]-1]
        else:
            return matrix[min_idx][indexes[min_idx]]


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
