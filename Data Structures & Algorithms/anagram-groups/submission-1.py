class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = {}

        for string in strs:
            map = [0] * 26
            for char in string:
                map[ord(char) - ord("a")]+=1
            
            key = tuple(map)
            if key not in collection:
                collection[key] = [string]
            else:
                collection[key].append(string)
        
        return list(collection.values())