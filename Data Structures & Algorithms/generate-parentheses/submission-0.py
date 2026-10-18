class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(opened, closed, current):
            if opened == closed == n:
                res.append(current)
                return
            
            if opened < n:
                backtrack(opened + 1, closed, current + "(")

            if closed < opened:
                backtrack(opened, closed + 1, current + ")")
    
        backtrack(0, 0, "")
        return res