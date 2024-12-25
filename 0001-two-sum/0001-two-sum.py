class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
       # 시간을 줄이기 위해 -> 해쉬맵(딕셔너리)를 사용한다! 
        ans = {}

        for idx, val in enumerate(nums):
            remained_value = target - val
            if remained_value in ans:
                return [ans[remained_value], idx]
            
            ans[val] = idx
            
            