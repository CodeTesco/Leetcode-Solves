def trap(height):
    if not height: return 0

    water_trapped = 0
    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]

    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            water_trapped += max(0, left_max - height[l])
        else:
            r -= 1
            right_max = max(right_max, height[r])
            water_trapped += max(0, right_max - height[r])

    return water_trapped


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
