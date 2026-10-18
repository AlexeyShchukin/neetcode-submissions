class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if c != hashmap[stack.pop()]:
                        return False
        return not stack
