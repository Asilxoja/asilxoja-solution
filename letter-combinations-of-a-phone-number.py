class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }        
        if len(digits) == 0:
            return []
        
        try1 = ['']
        for digit in digits:
            if digit not in dic:
                continue
            letters = dic[digit]
            new_try = []
            for combination in try1:
                for letter in letters:
                    new_try.append(combination + letter)
            try1 = new_try
        
        return try1