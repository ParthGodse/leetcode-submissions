class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        words = set(bank)

        valid = 'ACGT'
        count = 0
        q = deque([startGene])
        visit = set()
        visit.add(startGene)
        
        while q:
            size = len(q)

            for i in range(size):
                word = q.popleft()

                if word == endGene:
                    return count

                for j in range(8):
                    for char in valid:
                        new_word = word[:j] + char + word[j + 1:]
                        if new_word in words and new_word not in visit:
                            q.append(new_word)
                            visit.add(new_word)
            count += 1

        return -1            