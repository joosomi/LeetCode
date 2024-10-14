class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new = []
        # print(zip(word1, word2))
        for i, j in zip(word1, word2):
            new.append(i)
            new.append(j)
        
        new.append(word1[len(word2):])
        new.append(word2[len(word1):])

        return "".join(new)