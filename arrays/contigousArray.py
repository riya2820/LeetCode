def contigousArray(nums):
    seen_at = {}
    seen_at[0] = -1
    ans = count = 0
    
    # Time and space complexity is O(N)
    for idx, num in enumerate(nums):
        if num == 1:
            count += 1
        else:
            count = -1
            
        if count in seen_at:
            ans = max(ans, idx-seen_at[count])
        else:
            seen_at[count] = idx # updated the value 
        
    return ans

print(contigousArray([0,1,0]))
