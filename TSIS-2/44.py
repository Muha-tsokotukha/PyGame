class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
            
            mx = 0
            i = 0
            res = 0
            for i in range(0, len(gain)):
                res += gain[i]
                if res > mx:
                    mx = res
                i += 1
            return(mx)