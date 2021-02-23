class Solution:
    def defangIPaddr(self, address: str) -> str:
        x = 0
        ans = str("")
        for x in range(0, len(address)):
            if address[x]==".":
                ans = ans + "[" + address[x] + "]"
            else: ans += address[x]
            x += 1 
        return ans