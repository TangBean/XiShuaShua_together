class Solution(object):
    """
    RuntimeError: maximum recursion depth exceeded, recur method is not work for python, use stack. [cite ./solution_1.py]
    """
    def __init__(self):
        self.count = 0
        self.visited = None
        self.grid = None
        self.M = 0
        self.N = 0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        self.M = len(grid)
        self.N = len(grid[0])
        self.visited = []
        self.grid = grid
        for i in range(self.M):
            self.visited.append([False]*self.N)

        for m in range(self.M):
            for n in range(self.N):
                if not self.visited[m][n] and grid[m][n]:

                    self.num_islands_helper(m, n)
                    self.count += 1
        return self.count

    def num_islands_helper(self, m, n):
        if m < 0 or m >= self.M or n < 0 or n >= self.N or self.visited[m][n] or not self.grid[m][n]:
            return
        self.visited[m][n] = True
        self.num_islands_helper(m-1, n)
        self.num_islands_helper(m+1, n)
        self.num_islands_helper(m, n-1)
        self.num_islands_helper(m, n+1)


if __name__ == '__main__':
    solution = Solution()
    # grid = [
    #     [1, 1, 0, 0, 0],
    #     [1, 1, 0, 0, 0],
    #     [0, 0, 1, 0, 0],
    #     [0, 0, 0, 1, 1]
    # ]
    grid = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    count = solution.numIslands(grid)
    print(count)
