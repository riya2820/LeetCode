# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
from collections import defaultdict
from tkinter import S

def suggestedProducts(products, searchWord):
    # if > 3, return 3 lexicographically 
    # O(N) time and O(N) space
    s = "" 
    d = defaultdict(list)
    
    # Edge case!
    if len(products) == 1 and searchWord not in products[0]:
        return [products]
        
    i = 0 # "m o u s e"
    while i < len(searchWord):
        for product in products:
            try:
                if searchWord[i] == product[i]:
                    d[i] += [product]
            except IndexError:
                pass
        i += 1

    result = []
    for k, v in d.items():
        v.sort()
        if len(v) > 3:
            result.append(v[:3])
        else:
            result.append(v)
    
    return result 

products = ["havana"]
searchWord = "tatiana"
# ["bags","baggage","banner","box","cloths"]
# ["mobile","mouse","moneypot","monitor","mousepad"]
# searchWord = "bags"
# "mouse"
print(suggestedProducts(products, searchWord))
