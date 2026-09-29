class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        hash={2:"abc",
        3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        ans=[]
        if len(digits)==1:
            for x in hash[int(digits)]:
                ans.append(x)
            return ans
        elif len(digits)==2:
            for i in range(1,len(digits)):
                for y in hash[int(digits[i-1])]:
                    for z in hash[int(digits[i])]:
                        ans.append(y+z)
            return ans
        elif len(digits)==3:
            for i in range(2,len(digits)):
                for y in hash[int(digits[i-2])]:
                    for z in hash[int(digits[i-1])]:
                        for w in hash[int(digits[i])]:
                            ans.append(y+z+w)
            return ans
        else:
            for i in range(3,len(digits)):
                for y in hash[int(digits[i-3])]:
                    for z in hash[int(digits[i-2])]:
                        for w in hash[int(digits[i-1])]:
                            for u in hash[int(digits[i])]:
                                ans.append(y+z+w+u)
            return ans

            
            
