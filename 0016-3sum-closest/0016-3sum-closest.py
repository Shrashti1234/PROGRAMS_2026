class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # Update closest
                if abs(total - target) < abs(closest - target):
                    closest = total

                # Exact match
                if total == target:
                    return total

                # Need a bigger sum
                elif total < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return closest