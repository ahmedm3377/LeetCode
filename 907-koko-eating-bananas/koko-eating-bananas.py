class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)

        def calculate(x):
            c = 0
            for p in piles:
                c += math.ceil(p/x)
            return c

        mn = 1
        mx = max(piles)


        while mn<mx:
            middle = (mn+mx)//2
            calcH = calculate(middle)

            if (calcH>h):
                mn=middle+1
            if (calcH <= h):
                mx = middle
        return mx



        