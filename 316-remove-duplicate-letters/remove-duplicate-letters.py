class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_seen = {}
        for i in range(len(s)):
            last_seen[s[i]] = i
 
        stack = []
        used = set()
 
        for i in range(len(s)):
            ch = s[i]
            if ch in used:
                continue
 
            while stack and stack[-1] > ch and last_seen[stack[-1]] > i:
                used.remove(stack.pop())
 
            stack.append(ch)
            used.add(ch)
 
        return "".join(stack)