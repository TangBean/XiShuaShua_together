import heapq


class MedianFinder(object):
    """
    Runtime: 260 ms, faster than 71.44% of Python online submissions for Find Median from Data Stream.
    """
    def __init__(self):
        self.left = []
        self.right = []
        self.size = 0

    def addNum(self, num):
        if self.size & 1:
            if num >= -self.left[0]:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.right, -heapq.heappop(self.left))
                heapq.heappush(self.left, -num)
        else:
            if self.size == 0 or num <= self.right[0]:
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.left, -heapq.heappop(self.right))
                heapq.heappush(self.right, num)
        self.size += 1

    def findMedian(self):
        if self.size & 1:
            return -self.left[0]
        else:
            return (float(self.right[0]) - float(self.left[0])) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
