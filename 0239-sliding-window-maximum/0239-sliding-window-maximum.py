from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for i in range(len(nums)):

            # 1. Remove indices outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Start recording answers when window reaches size k
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result