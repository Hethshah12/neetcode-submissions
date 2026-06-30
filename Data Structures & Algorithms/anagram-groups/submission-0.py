class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict=defaultdict(list)
        for s in strs:
            count= [0]*26
            for ch in s:
                count[ord(ch)-ord('a')] +=1

            key=tuple(count)
            anagram_dict[key].append(s)
        
        return list(anagram_dict.values())