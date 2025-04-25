class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # interesting subarrays
        # nums[i] % modulo == k

        ans = 0

        count = [0]
        for i in range(len(nums)):
            prev = count[-1]

            if nums[i] % modulo == k:
                count.append(prev+1)
            else:
                count.append(prev)

        freq = defaultdict(int)
        freq[0] = 1

        for c in count[1:]:
            target = (c + modulo - k) % modulo
            ans += freq[target]
            freq[c % modulo] +=1 

        return ans