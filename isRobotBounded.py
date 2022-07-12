class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y = 0, 0
        dx, dy = 0, 1

        for i in instructions:
            if i == 'L':  
                dx, dy = -dy, dx # Turn left 
                print("Left: ",dx,dy)

            elif i == 'R' :  
                dx, dy = dy, -dx # Turn right 
                print("Right: ",dx,dy)

            elif i == 'G': 
                x += dx
                y += dy
                print("Straight: ",x,y)

        if (x, y) == (0, 0): # Case 1: Robot returns to rigin
            return True

        if (dx, dy) != (0, 1): # Case 2: Robot does not face north 
            return True

        return False
