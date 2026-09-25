class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(index, current):
            # We have considered all elements
            if index == len(nums):
                result.append(current.copy())
                return

            # Choice 1: Include nums[index]
            current.append(nums[index])
            backtrack(index + 1, current)

            # Undo the choice
            current.pop()

            # Choice 2: Don't include nums[index]
            backtrack(index + 1, current)

        backtrack(0, [])

        return result