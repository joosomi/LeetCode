class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        #bucket sort 

        cnt = Counter(nums)
        print(cnt.items())

        buckets = [[] for _ in range(len(nums) + 1)]

        for val, freq in cnt.items():
            buckets[freq].append(val)

        ans = []
        
        for bucket in reversed(buckets):
            for val in bucket:
                ans.append(val)
                k -= 1
                if k == 0:
                    return ans