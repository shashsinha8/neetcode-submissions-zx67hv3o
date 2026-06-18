class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1: 
            return 0
        
        sieve = [False] * n
        sieve[0] = sieve[1] = True
        res = 0

        for num in range(2, n):
            if not sieve[num]:
                res += 1
                for i in range(num+num, n, num):
                    sieve[i] = True
                            
        return (res)
