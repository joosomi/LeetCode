class Solution:
    def countLargestGroup(self, n: int) -> int:
        # return the number of groups - 가장 큰 사이즈 
      
        digit_sum = lambda x: sum(map(int, str(x)))

        freq = defaultdict(int)

        for num in range(1, n+1):
            freq[digit_sum(num)] += 1

        counts=  list(freq.values())
        max_size = max(counts)

        return counts.count(max_size)