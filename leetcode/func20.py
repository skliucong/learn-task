class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s==' ' or s=='' or s==None:
            return True
        stack=[]
        for item in s:
            if item=='(' or item=='{' or item=='[':
                stack.append(item)
            elif len(stack)!=0 and (item==')' or item=='}' or item==']') :
                ite=stack.pop()
                if item==')' and ite=='(':
                    continue
                elif item=='}' and ite=='{':
                    continue
                elif item==']' and ite=='[':
                    continue
                else:
                    return False
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False





if __name__ == '__main__':
    print(Solution().isValid("["))