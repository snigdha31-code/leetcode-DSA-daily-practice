# Title: Two Sum
# LeetCode: https://leetcode.com/problems/two-sum/
# ID: 1
# Difficulty: Easy
# Tags: array, hash-table
# Language: Python3
# Date: 2025-10-13
#
# Approach:
# - Use a hash map (dictionary) to store each number's index as we iterate.
# - For each number, calculate its difference (target - num).
# - If the difference exists in the hash map, return both indices.
# - Otherwise, store the current number and its index in the hash map.
#
# Time Complexity: O(n)  -> Each lookup and insert in the hash map is O(1) on average.
# Space Complexity: O(n) -> In the worst case, we store all elements in the hash map.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {} #empty hashmap
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_map:
                return [hash_map[diff],i]
            else:
                hash_map[nums[i]]= i
        return
