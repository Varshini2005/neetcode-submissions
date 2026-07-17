class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        mpp = {}
        for i in range(n):
            mpp[nums[i]] = mpp.get(nums[i],0) +1
            if mpp[nums[i]]>1:
                return True
        return False
        
        