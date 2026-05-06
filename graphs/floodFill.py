class Solution: 
    # (1,1) fill 2
    # 1 1 1     2 2 2
    # 1 1 0 ->  2 2 0
    # 1 0 1     2 0 1
    def floodFill(self, image, r, c, color):
        if not image or not image[0]:
            return 

        row, cols = len(image), len(image[0])
        stack.append(image[r][c])

        while stack:
            stack.pop()
            if image[r][c] == "1":
                image[r][c] = color
     
            if r+1 < len(image):
                stack.append((r+1, c)) # down
            if r > 0:
                stack.append((r-1, c)) # up
            if c+1 < len(image):
                stack.append((r, c+1)) # right
            if c > 0:
                stack.append((r, c-1)) # left
            
        return image

    
