class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        count_s = Counter(s)
        count_t = Counter(t)
        if count_s == count_t:
            return True
        else:
            return False