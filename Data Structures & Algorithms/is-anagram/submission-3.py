class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for i in s:
            count_s[i] = count_s.get(i,0)+1
        for j in t:
            count_t[j] = count_t.get(j,0)+1
        if count_s != count_t:
            return False
        else:
            return True