class Solution:
    def stripString(self, s: str):
        newstr = ''
        for c in s: 
            if c.isalnum() and c != ' ':
                newstr += c.lower()
        return newstr
    def isPalindrome(self, s: str):
        '''
        Given:  s -> str
        Task: return True if s is palindrome
        '''
        strippedString = self.stripString(s)
        print(strippedString)
        return strippedString == strippedString[::-1]
