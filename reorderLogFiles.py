class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # Order 
        # letter logs (sorted lexicographically by contents then indentifiers), 
        # digit logs (relative ordering)
        
        # "dig1 8 1 5 1" --4
        # "let1 art can" --1
        # "dig2 3 6" --5
        # "let2 own kit dig" --3
        # "let3 art zero" --2
        digitLogs, letterLogs = [], []
        result = []
        
        for log in logs:
            content = log.split(" ")
            if content[1].isdigit():
                digitLogs.append(' '.join(content))
            else:
                letterLogs.append((content[0], ' '.join(content[1:])))
                
        letterLogs.sort(key=lambda x:(x[1], x[0]))
        result = [' '.join(tups) for tups in letterLogs]
        result.extend(digitLogs)
        
        return result
        
