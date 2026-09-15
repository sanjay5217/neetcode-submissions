class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)

        for string in strs:
            _map = [0] * 26
            for char in string:
                _map[ord(char) - ord("a")]+=1
            
            collection[tuple(_map)].append(string)
        
        return list(collection.values())