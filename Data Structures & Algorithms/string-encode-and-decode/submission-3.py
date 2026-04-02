class Solution:

    def encode(self, strs: List[str]) -> str:
        
        password = ""
        for s in strs:
            password += f"{len(s)}#{s}"
            # ["neet","code","love","you"]
            # 4#neet4#code4#love3#you
        print(password)
        return password
        


    def decode(self, s: str) -> List[str]:

        # 4#neet4#code4#love3#you
        # 
        ans = []
        num_index = 0
        for i in range(len(s)): 
            if s[i] == '#' and s[i-1].isnumeric():

                print(f"i = {i} num_index = {num_index}")
                length = int(s[num_index:i])
                print(f"Length= {length}")


                ans.append(s[i+1:(i+1+length)])
                
                i += length
                num_index = i+1

        return ans
                

        return



