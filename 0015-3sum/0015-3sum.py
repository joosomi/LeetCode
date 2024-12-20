class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # 중복값 건너뛰기
                continue

            num = nums[i]
            left, right = i+1, len(nums)-1

            while left < right: 
                total = num + nums[left] + nums[right]
                if total ==0 :
                    triplets = [nums[i], nums[left], nums[right]]
                    if triplets not in ans:
                        ans.append(triplets)

                    left += 1
                    right -=1

                elif total < 0:
                    left +=1 
                elif total > 0:
                    right -= 1 

        return ans