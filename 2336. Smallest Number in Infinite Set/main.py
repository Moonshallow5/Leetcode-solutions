class SmallestInfiniteSet(object):

    def __init__(self):
        self.l=list(range(1,1001))
        self.curr=set(self.l)


        

    def popSmallest(self):
        """
        :rtype: int
        """
        if(self.curr):
            x=min(self.curr)
            self.curr.remove(x)
            return x
        else:
            return  None

        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if(num not in self.curr):
            self.curr.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
