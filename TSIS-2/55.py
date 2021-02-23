class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prod = 1
        symma = 0
        while n > 0:
            prod *= n%10
            symma += n%10
            n //= 10
        return( (prod - symma) )