class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hash={}
        for i in range(n):
            co=target-nums[i]
            if co in hash:
                return hash[co],i
            hash[nums[i]]=i
        return []
                

