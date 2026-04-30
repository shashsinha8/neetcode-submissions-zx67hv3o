class Solution:

    def encode(self, strs: List[str]) -> str:
        message = ""
        for s in strs: 
            message += f"#{len(s)}#{s}"
        return message


    def decode(self, s: str) -> List[str]:
        #5#Hello#5#World
        ans = []
        L, R = 0, 0
        i = 0
        while i < (len(s) - 1):
            
            if s[i] == "#":
                i = i + 1
                lenl = i
                while s[i] != "#":
                    i+= 1
                lenr = i

                #5#Hello#5#World
                word_len = int(s[lenl:lenr])
                word = s[lenr+1:lenr+1+word_len]
                ans.append(word)
                i = i + word_len + 1

        return ans
                



                
                



