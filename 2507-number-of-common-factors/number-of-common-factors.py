class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factors = 1
        s = min(a,b)
        for i in range(2,s+1):
            if a%i==0 and b%i==0:
                factors+=1
        return factors
