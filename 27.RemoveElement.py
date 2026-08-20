class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        y=[]
        i=0
        l=len(nums)
        while i<l:
            if nums[i]==val:
                nums.pop(i)
                l-=1
            else:
                i+=1
        return len(nums)
                

        return len(nums)
