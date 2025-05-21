class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        stack = []
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        for i, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i < last[stack[-1]]:
                    # stack.pop()
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)

        return "".join(stack)
