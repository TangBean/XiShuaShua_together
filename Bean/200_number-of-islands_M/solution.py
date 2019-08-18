class Solution(object):
    """
    Runtime: 124 ms, faster than 80.47% of Python online submissions for Number of Islands.
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        M = len(grid)
        N = len(grid[0])
        visited = []
        count = 0
        for i in range(M):
            visited.append([False]*N)

        stack = []
        for i in range(M):
            for j in range(N):
                if not visited[i][j] and grid[i][j] == '1':
                    stack.append((i, j))
                    while stack:
                        m, n = stack.pop()
                        if 0 <= m < M and 0 <= n < N and not visited[m][n] and grid[m][n] == '1':
                            visited[m][n] = True
                            stack.append((m-1, n))
                            stack.append((m+1, n))
                            stack.append((m, n-1))
                            stack.append((m, n+1))
                    count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    res = solution.numIslands(grid)
    print(res)
