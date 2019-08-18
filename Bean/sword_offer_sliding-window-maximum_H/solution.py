class Solution:
    """
    运行时间：30ms
    占用内存：5756k
    """
    def maxInWindows(self, num, size):
        if not size:
            return []

        deque = []
        res = []
        for i in range(len(num)):
            while deque and num[i] > deque[-1]:
                deque.pop()
            deque.append(num[i])
            if i >= size - 1:
                res.append(deque[0])
                if num[i-size+1] == deque[0]:
                    deque.pop(0)
        return res


if __name__ == '__main__':
    solution = Solution()
    num = [2, 3, 4, 2, 6, 2, 5, 1]
    size = len(num)
    res = solution.maxInWindows(num, 3)
    print(res)
