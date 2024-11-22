class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # vowels = [i for i in s if i in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']]

        # vowels.reverse()

        # result = []

        # for char in s:
        #     if char in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
        #         result.append(vowels.pop(0))
        #     else:
        #         result.append(char)

        # return "".join(result)

        # two pointers 

        vowels = set('aAiIoOuUeE')
        s = list(s)
        left, right = 0, len(s)-1

        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
            elif s[left] not in vowels:
                left +=1
                continue
            elif s[right] not in vowels:
                right -= 1
                continue
            left +=1 
            right -=1 

        return "".join(s)
