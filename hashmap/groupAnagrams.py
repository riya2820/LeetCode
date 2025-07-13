class Solution(object):
    def groupAnagrams(self, strs):
      
        s = [''.join(sorted(x)) for x in strs]
        
        dictionary = {}
        #since enumerate format is count, elem in enumerate(s)
        for val, key in enumerate(s):
            if key not in dictionary:
                dictionary[key] = [strs[val]]
  
            else:
                dictionary[key].append(strs[val])
    
        return list(dictionary.values())
