class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        
        nums.sort()
        print(nums)

        for idx, val in enumerate(nums):

            if idx>0 and nums[idx]==nums[idx-1]:
                continue 

            remained = -val
            
            left, right = idx+1, len(nums)-1

            while left < right:
                
                if nums[left]+nums[right] ==remained:
                    ans.append([nums[left], nums[right], val])

                    while left <right and nums[left] == nums[left+1]:
                        left+=1 
                    while left < right and nums[right]==nums[right-1]:
                        right-=1 
                    left +=1 
                    right -=1

                elif nums[left]+nums[right]< remained:
                    left +=1 
                elif nums[left]+nums[right]>remained:
                    right-=1

        return ans

    