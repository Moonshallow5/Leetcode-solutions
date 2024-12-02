class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s=sentence.split()
        print(s)
        for i,val in enumerate(s):
            if(val.startswith(searchWord)):
                return i+1
        return -1
