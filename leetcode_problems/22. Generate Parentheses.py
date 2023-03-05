class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1.open == close return
        2. open> close: add )
        3. open<n add (
        """
        stack=[]
        res=[]
        def backrecursion(openN,closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN <n:
                stack.append("(")
                backrecursion(openN+1,closeN)
                stack.pop()
            if openN> closeN:
                stack.append(")")
                backrecursion(openN,closeN+1)
                stack.pop()
        backrecursion(0,0)
        return res
