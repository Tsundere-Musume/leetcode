#!/usr/bin/env python

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1) :
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        half = (n1 + n2) // 2

        # 0..=n1
        l, r = 0, n1
        x = 0
        while l <= r:
            m = l + (r - l) // 2
            left_1, right_1 = nums1[: m] , nums1[m: ]
            left_2, right_2 = nums2[: (half - m)] , nums2[(half - m): ]

            if (not left_1 or left_1[-1] <= right_2[0]) and (not right_1 or left_2[-1] <= right_1[0]):
                x = m
                break

            if left_1 and left_1[-1] > right_2[0]:
                r = m - 1
            else:
                l = m + 1


        part_1, part_2 = nums1[x:], nums2[(half-x) :]
        l1, l2 = nums1[:x], nums2[:(half - x)]
        if (n1 + n2) % 2 == 0:
            return (max([*l1[-1:], *l2[-1:]]) + min([*part_1[:1], *part_2[:1]])) /2
        else:
            return min([*part_1[:1], *part_2[:1]])
