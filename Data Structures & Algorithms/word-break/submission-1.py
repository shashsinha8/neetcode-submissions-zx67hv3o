class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        wordset = set(wordDict)
        memo = {}
        def look(startPos):
            if startPos >= len(s):
                return True
            if startPos in memo:
                return memo[startPos]

            # for loop instead of while loop
            # use for loop to check if the word is in the dictionary
            # for all words in dictionary use recursion
                
            for i in range(startPos + 1, len(s)+1):
                if s[startPos:i] in wordset and look(i):
                    memo[startPos] = True
                    return True
            memo[startPos] = False
            return False
        
        return look(0) 
                    