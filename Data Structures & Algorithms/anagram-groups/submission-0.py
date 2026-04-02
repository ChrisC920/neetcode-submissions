class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # create an empty dictionary
                                # with default value as an empty list
        for s in strs:
            count = [0] * 26    # empty list with 26 0's
            for c in s:
                count[ord(c) - ord('a')] += 1 # count no. of each char
            res[tuple(count)].append(s) # convert to tuple so it can be a key
        return list(res.values())