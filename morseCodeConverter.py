class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code =  [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        c = ""
        result = []

        for word in words:
            for letter in word:
                idx = ord(letter) - (ord("a")) 
                c += code[idx]
                
            result.append(c)
            c = ""
    
        return len(set(result))
