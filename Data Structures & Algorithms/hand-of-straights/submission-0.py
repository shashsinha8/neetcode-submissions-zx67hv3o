class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        count = {}
        for n in hand: 
            count[n] = 1 + count.get(n, 0)
        
        print(count)

        for i in sorted(count):
            while count[i] > 0:
                for card in range(i, i + groupSize):
                    if count.get(card, 0) == 0:
                        return False
                    count[card] -= 1

        return True
