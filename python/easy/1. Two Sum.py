class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Iterate over all possible pairs of indices in nums
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the sum of the two elements at indices i and j is equal to target
                if nums[i] + nums[j] == target:
                    # Return the indices if the sum is equal to target
                    return [i, j]

        # Return an empty list if no pair of indices was found that sums to target
        return []


# Create an object of the class
a = Solution()

# Call the twoSum function and print the result
print(a.twoSum([3, 2, 4], 6))
