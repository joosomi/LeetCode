class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)

        cnt1, cnt2= nums1.count(0), nums2.count(0)

        min_sum1, min_sum2 = sum1 + cnt1, sum2 + cnt2

        if min_sum1 > min_sum2 and cnt2 == 0:
            return -1 
        if min_sum2 > min_sum1 and cnt1 == 0:
            return -1 


        return max(min_sum1, min_sum2)