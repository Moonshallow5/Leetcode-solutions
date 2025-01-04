class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurence={}
        last_occurence={}

        for i,char in enumerate(s):
            if char not in first_occurence:
                first_occurence[char]=i
            last_occurence[char]=i
        print(first_occurence)
        print(last_occurence)

        unique=set()
        for char in first_occurence:
            start=first_occurence[char]
            end=last_occurence[char]

            if(start<end):
                middle_chars=set(s[start+1:end])
                for i in middle_chars:
                    unique.add((s[start+1],i,s[end]))
        print(unique)
        return len(unique)





        
