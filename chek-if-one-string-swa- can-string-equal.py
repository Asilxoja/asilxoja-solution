class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        differing_chars = []
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                differing_chars.append((s1[i], s2[i]))

        if len(differing_chars) != 2:
            return False

        return differing_chars[0] == differing_chars[1][::-1]