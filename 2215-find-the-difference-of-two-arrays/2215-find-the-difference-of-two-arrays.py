class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        ans1 = [i for i in nums1 if i not in nums2]
        ans2 = [j for j in nums2 if j not in nums1]
        return [set(ans1), set(ans2)]
        