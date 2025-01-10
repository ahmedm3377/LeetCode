class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        Vowels  = ('a', 'e', 'i', 'o', 'u')

        w = s[0:k]
        c = 0
        for l in w:
            if l in Vowels:
                c +=1
        mx = c
        if len(s)>k:
            for l in s[k:]:
                if w[0] in Vowels:
                    c -=1
                w = w[1:]+l
                if l in Vowels:
                    c += 1
                if c>mx:
                    mx = c

        return mx
