from collections import defaultdict

def solution(arr):
    d = defaultdict(int) # can index default dict (int)
    
    for s in arr:
        if s[0] != "!":
            d[s] += 1   
        
        elif s[0] == "!":
            n = int(s[1:])
            d[arr[n-1]] += 1 # update count 

    # Return number of times each command gets executed
    # as [cp count, ls count, mv count].

  
    return [d["cp"]] + [d["ls"]] + [d["mv"]] # adding lists to be one big list [] + [] = [_, _]

arr = ["ls","cp","mv", "dir", "!3", "!1", "!2", "!3", "!4"]   
print(solution(arr))
