from operator import indexOf


def simpleCipher(encrypted, k):
    alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L",
    "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    decrypted = ""
    
    # constraint
    k %= 26

    for letter in encrypted:   
        i = alphabets.index(letter) 
        # takes O(N) space; instead
        # val = ord(letter) - ord('A') -k
        decrypted += alphabets[i-k] 
        # val += ord('A')
        # decrypted += chr(val)

    return decrypted


print(simpleCipher("VTAOG", 2))
