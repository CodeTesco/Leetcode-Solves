def jump(nums):
    n = len(nums)
    if n <= 1:
        return 0

    i = 0
    jumps = 0
    max_jump = 0 
    current_end = 0 

    while i < n - 1:
        max_jump = max(max_jump, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = max_jump
            
        i += 1

    return jumps

print(jump([10,9,8,7,6,5,4,3,2,1,1,0]))

# [2,3,1,1,4]