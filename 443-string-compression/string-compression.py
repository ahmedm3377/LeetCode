class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)<=1:
            return len(chars)
        
        p1 = 0
        p2 = 0

        c = chars[0]
        cntr = 1
        while p1<len(chars)-1:
            p1 +=1
            if chars[p1]==c:
                cntr +=1
            else:
                if cntr>1:
                    for i in str(cntr):
                        p2 +=1
                        chars[p2] = i

                cntr = 1
                c = chars[p1]
                p2 +=1
                chars[p2] = c
        
        if cntr>1:
            for i in str(cntr):
                p2 +=1
                chars[p2] = i

        del chars[p2+1:]

        return len(chars)

            


