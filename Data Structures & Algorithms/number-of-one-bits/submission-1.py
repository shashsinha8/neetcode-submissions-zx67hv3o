class Solution:
    def hammingWeight(self, n: int) -> int:
        

        m = n
        ans = ''
        print(f"m = {m}")
        while m != 0:
            if m == 1: 
                ans = "1" + ans
                break
            d = int(m % 2)
            m = m // 2
            ans = str(d) + ans
        count = ans.count("1")
        return count
