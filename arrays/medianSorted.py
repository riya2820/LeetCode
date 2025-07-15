def funct(nums1, nums2): 
    lst = []
    #lst = sorted(nums1 + nums2) #O(N)!
    l1 = len(nums1)
    l2 = len(nums2)
    i = 0
    j = 0
    
    #O(log(m+n)) time
    while i < l1 and j <l2:
        if nums1[i] < nums2[j]:
            lst.append(nums1[i])
            i+=1
        else:
            lst.append(nums2[j])
            j+=1
    
    while i < l1:
        lst.append(nums1[i])
        i+=1
    while j < l2:
        lst.append(nums2[j])
        j+=1
    
    
    n = len(lst)
    
    if n%2 == 1:
        return lst[n/2]
    else:
        return (lst[n//2]+lst[n//2-1])/2
