class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = [i for i in s if i in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']]

        vowels.reverse()

        result = []

        for char in s:
            if char in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
                result.append(vowels.pop(0))
            else:
                result.append(char)

        return "".join(result)