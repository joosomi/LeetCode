class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(set(Counter(arr).values())) != len(set(arr)):
            return False
        return True