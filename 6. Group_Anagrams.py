from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        
        for word in strs:
            
            counts = Counter(word)
            
            wordset = frozenset([kv[0] + str(kv[1]) for kv in counts.items()])

            if wordset not in words:
                words[wordset] = []
            words[wordset].append(word)
            
        return [kv[1] for kv in words.items()]
                
