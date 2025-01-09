class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        sorted_val = {}

        for idx, val in enumerate(strs):
            print(sorted(list(val)))

            if "".join(sorted(list(val))) in sorted_val:
                sorted_val["".join(sorted(list(val)))].append(val)
            else:
                sorted_val["".join(sorted(list(val)))] = [val]

        
        return sorted_val.values()

            

  