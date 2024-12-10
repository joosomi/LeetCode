class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0 
        
        if len(nums) == 1:
            return 1 

        nums.sort()
        seq = []
        
        in_seq = 1

        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                in_seq += 1
            elif nums[i] == nums[i+1]:
                i += 1 
            else: 
                seq.append(in_seq)
                i += 1
                in_seq = 1 
            seq.append(in_seq)
        print(seq)
        return max(seq)