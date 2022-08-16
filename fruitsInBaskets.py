from collections import defaultdict

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        result = 0
        basket = defaultdict(int)
        l = r = 0

        while r < len(fruits):
            if len(basket) < 2:
                basket[fruits[r]] += 1
                r += 1
            elif len(basket) == 2 and fruits[r] in basket:
                basket[fruits[r]] += 1
                r += 1
            elif len(basket) == 2 and fruits[r] not in basket:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            result = max(result, r-l)

        return result
        
