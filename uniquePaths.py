def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    # Logic -> keep adding bottom and right value 
    row = [1]*n

    for i in range(m-1):
        newRow = [1]*n # row above current row
        for j in range(n-2, -1, -1): # every col except rightmost col; since it is always 1
            # traversing L <- R 
            newRow[j] = newRow[j+1] + row[j]
        row = newRow
    return row[0] # start cell which has the total no of paths

if __name__ == "__main__":
    m = 3
    n = 7
    print(uniquePaths(m,n))
