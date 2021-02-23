class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        i = 0
        for i in range(0, len(nums)):
            j = i
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    cnt+=1
                j += 1
            i += 1
        return cnt
        