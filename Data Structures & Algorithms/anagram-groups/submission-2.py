class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)

        for string in strs:
            map = [0] * 26
            for char in string:
                map[ord(char) - ord("a")]+=1
            
            collection[tuple(map)].append(string)
        
        return list(collection.values())