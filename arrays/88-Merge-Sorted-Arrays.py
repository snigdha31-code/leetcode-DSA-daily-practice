# Title: Merge Sorted Array
# LeetCode: https://leetcode.com/problems/merge-sorted-array/
# ID: 88
# Difficulty: Easy
# Tags: arrays, two-pointers
# Language: Python3
# Date: 2025-10-13
#
# Approach:
# - Start filling nums1 from the end
# - Compare last elements of nums1 and nums2 and place the bigger one at the end
# - Fill leftover nums2 elements if any
# Time Complexity: O(m+n)
# Space Complexity: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #LAST INDEX OF NUMS1
        last = m+n-1

        #MERGE IN REVERSE ORDER
        while m>0 and n>0:    #while elements exists in both arrays
            if nums1[m-1]>nums2[n-1]:
                nums1[last]=nums1[m-1]
                m=m-1
            else:
                nums1[last]=nums2[n-1]
                n=n-1
            last=last-1
        #FILL NUMS1 ARRAY WITH LEFTOVER NUMS2
        while n>0:
            nums1[last]=nums2[n-1]
            n=n-1
            last=last-1
