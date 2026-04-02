class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for s in strs: 
            answer += f"{len(s)}#{s}"
        print(answer)
        return answer

    def decode(self, s: str) -> List[str]:

        # 4#neet4#code4#love3#you
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j + 1 + length
        return ans       


