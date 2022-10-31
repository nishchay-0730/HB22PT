class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l,stack=0,[-1]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    l=max(l,i-stack[-1])
        return l;
