class Solution:
    def romanToInt(self, s: str) -> int:
        Rum_nume = {
         "I": 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000
        }
        string = s
        ans = 0
        for i in range(len(string)):
            if i < len(string) - 1 and Rum_nume[string[i]] < Rum_nume[string[i+1]]:
                ans -= Rum_nume[string[i]]
            else:
                ans += Rum_nume[string[i]]
        return f"{ans}"