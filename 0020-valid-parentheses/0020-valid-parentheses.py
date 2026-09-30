class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash={"(":")","[":"]","{":"}"}
        for i in s:
            if i in hash:
                stack.append(i)
            else:
                if not stack or hash[stack[-1]]!=i:
                    return False
                stack.pop()
        return not stack
                


            
            

