class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_splited = [*s]
#         t_splited = [*t]
#         for c in t_splited:
#             if c in s_splited:
#                 s_splited.remove(c)
#             else:
#                 return False
#         if len(s_splited) == 0:
#             return True
#         else:
#             return False