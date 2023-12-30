class Solution:
    def isValid(self, s: str) -> bool:
        store = []
        for c in range(len(s)):
            if s[c] == '(' or s[c] == '[' or s[c] == '{':
                store.append(s[c])
            else:
                if len(store) == 0:
                    return False
                else:
                    if s[c] == ')':
                        p = store.pop()
                        if p != '(':
                            return False
                    elif s[c] == ']':
                        p = store.pop()
                        if p != '[':
                            return False
                    elif s[c] == '}':
                        p = store.pop()
                        if p != '{':
                            return False
                    else:
                        return False
        if len(store) == 0:
            return True
        else:
            return False