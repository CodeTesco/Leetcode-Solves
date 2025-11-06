def maxArea(height):
    left = 0
    right = len(height) - 1
    maxWater = 0

    while(left < right):
        smallerWall = min(height[left], height[right])
        area = smallerWall * (right - left)
        if (area > maxWater):
            maxWater = area
        
        if(height[left] == smallerWall):
            left += 1
        else:
            right -= 1

        continue

    return maxWater

print(maxArea([1,1]))