class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        nums = sorted(nums, key=lambda x: nums.count(x), reverse = True)
        
        ans = []
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
 
        
        return ans[:k]

