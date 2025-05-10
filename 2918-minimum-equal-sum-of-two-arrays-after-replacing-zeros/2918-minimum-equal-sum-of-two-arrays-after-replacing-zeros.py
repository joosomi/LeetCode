class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1 = nums1.count(0)
        cnt2 = nums2.count(0)


        sum1 = sum(1 if x == 0 else x for x in nums1)
        sum2 = sum(1 if x == 0 else x for x in nums2)

        if sum1 == sum2:
            return sum1

        if sum1 > sum2:
            diff = sum1 - sum2 

            if cnt2 == 0:
                return -1
    
            return diff + sum2
        else:
            diff = sum2 - sum1
            if cnt1 == 0:
                return -1
            
            return diff + sum1