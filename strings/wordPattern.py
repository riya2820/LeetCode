def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        # edge case
        if len(pattern) != len(words):
            return False 

        char_to_word = defaultdict(str)
        words_used = set() 

        for char, word in zip(pattern, words):
            # print(char, word)
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                if char_to_word[char] in words_used:
                    return False
                else:
                    char_to_word[char] = word
                    words_used.add(char)         
        return True
