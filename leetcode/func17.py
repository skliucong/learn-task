class Solution:
    ll=[]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        ma={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        lis=[]
        for  item in digits:
            ite=int(item)
            lis.append(ma.get(ite))
        self.ll=[]
        self.combin("",lis)
        return self.ll

    def combin(self,pailie,lis):
        if len(lis)==1:
            for item in lis[0]:
                self.ll.append(pailie+item)
        else:
            for item in lis[0]:
                self.combin(pailie+item,lis[1:])





if __name__ == '__main__':
    re=Solution().letterCombinations("23")
    print(re)