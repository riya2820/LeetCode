def merge(A,first1, last1, first2, last2):
        index1 = first1
        index2 = first2
        tempIndex  = 0
        temp = []
        invCount = 0
        
        while (index1 <= last1) and (index2 <= last2):
            if nums[index1] <= A[index2]:
                temp[tempIndex++] = A[index1++]
            else:
                temp[tempIndex++] = A[index2++]
                invCount += last1 - index1 + 1
            
        while index1 <= last1:
            temp[tempIndex++] = A[index1++]
            
        while index2 <= last2:
            temp[tempIndex++] = A[index2++]
            
        tempIndex = 0
        index = first1
        while index <= last2:
            A[index1++] = temp[tempIndex++]
        return invCount
      
