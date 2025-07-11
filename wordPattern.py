def wordPattern(self, pattern: str, s: str) -> bool:
        d1, d2 = defaultdict(list), defaultdict(list)

        for idx, char in enumerate(pattern):
            if char in d1:
                d1[char].append(idx)
            else:
                d1[char] = [idx]

        compare_string = s.split(" ")
        print(compare_string)
        for idx, char in enumerate(compare_string):
            if char in d2:
                d2[char].append(idx)
            else:
                d2[char] = [idx]

        return list(d1.values()) == list(d2.values())
