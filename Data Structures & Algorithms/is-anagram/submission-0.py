class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # s.sorted()
        s_sorted = "".join(sorted(s))
        # t.sorted()
        t_sorted = "".join(sorted(t))
        # print(s_sorted)
        # print(t_sorted)
        for i in range(len(s_sorted)):
            if s_sorted[i] != t_sorted[i]:
                return False
        return True
