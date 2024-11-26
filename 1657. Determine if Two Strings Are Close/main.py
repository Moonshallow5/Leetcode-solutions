class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if(set(word1) !=set(word2)):
            return False
        count1=Counter(word1)
        count2=Counter(word2)
        print(count1.values())
        print(count2.values())
        return sorted(count1.values())==sorted(count2.values())

      
