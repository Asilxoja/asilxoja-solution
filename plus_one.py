import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int(input())
        satr = list(map(str, digits))
        ans = int(''.join(satr))
        ans = ans + 1
        ans = str(ans)
        ls = []
        for key in ans:
            ls += key
        return ls