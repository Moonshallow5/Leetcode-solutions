class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res=[]
        digitstochar={

            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res=[]

        def backtrack(curStr,i):
            if(len(curStr)==len(digits)):
                res.append(curStr)
                return
            for c in digitstochar[digits[i]]:
                backtrack(curStr+c,i+1)
        if(digits):
            backtrack("",0)
        return res
        
        
