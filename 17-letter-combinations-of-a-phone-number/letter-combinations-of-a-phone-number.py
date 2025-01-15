class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        

        def dfs(index, path, res):
            if index >= len(digits):
                res.append(path)
                return
            string1 = dic[digits[index]]
            for i in string1:
                dfs(index + 1, path + i, res)
        
        dfs(0, '', res)
        return res