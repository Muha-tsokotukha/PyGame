class Solution:
    def interpret(self, command: str) -> str:
            x = command
            ans = ""
            i = 0
            for i in range(0, len(x)):
                if x[i] == 'G':
                    ans += "G"
                    i +=1
                elif x[i] == '(':
                    if x[i+1] == ')':
                        ans += "o"
                        i = i + 2 
                    else:
                        ans += "al"
                        i = i + 3
            return ans