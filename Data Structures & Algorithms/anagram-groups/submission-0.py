class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_anagrams = {}

        for string in strs:
            canonical = ''.join(sorted(string))

            if canonical in group_anagrams:
                group_anagrams[canonical].append(string)
            else:
               group_anagrams[canonical] = [string]
        return list(group_anagrams.values())

        