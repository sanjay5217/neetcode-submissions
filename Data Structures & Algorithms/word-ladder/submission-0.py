class Solution:
    def check_word(self, word1: str, word2: str) -> bool:
        difference = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                difference += 1
                if difference > 1:
                    return False
        return difference == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        
        # do beginWord first
        words = list(set(wordList + [beginWord]))

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.check_word(words[i], words[j]):
                    graph[words[i]].append(words[j])
                    graph[words[j]].append(words[i])

        queue = deque()
        visited = set()
        queue.append((beginWord, 1))
        visited.add(beginWord)

        while queue:
            curr, dist = queue.popleft()
            if curr == endWord:
                return dist
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    queue.append((neighbour, dist+1))
                    visited.add(neighbour)
        return 0