class Solution:
    def isValid(self, s):
        return self.isValid_Solution2(s)

    def isValid_Soltion1(self, s):
        # Initialization
        parentheses = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in range(len(s)):
            if s[i] in parentheses:
                value = stack.pop() if len(stack) > 0 else '#'
                if(parentheses[s[i]] != value):
                    return False
            else:
                stack.append(s[i])
        return len(stack) == 0

    def isValid_Solution2(self, s):
        # Initialization
        parentheses = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in range(len(s)):
            if s[i] in parentheses:
                stack.append(s[i])
            else:
                value = stack.pop() if len(stack) > 0 else '#'
                if not(value in parentheses) or (parentheses[value] != s[i]):
                    return False
        return len(stack) == 0


    # Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "){"
print(Solution().isValid(s))
