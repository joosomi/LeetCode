class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        magaz = Counter(magazine)

        for key, cnt in ransom.items():
            if magaz[key] < cnt:
                return False
        return True