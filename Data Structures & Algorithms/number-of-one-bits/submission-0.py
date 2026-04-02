class Solution:
    def hammingWeight(self, n: int) -> int:
        


        b = format(n, '032b')
        print(n)
        print(b)
        counter = 0
        for c in str(b):
            if c == "1":
                counter += 1

        print(f"counter = {counter}")

        return counter