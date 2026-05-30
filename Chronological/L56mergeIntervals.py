def merge(intervals):
    i = 0
    intervals.sort(key=lambda interval: interval[0])

    while i+1 < len(intervals):
        if intervals[i+1][0] <= intervals[i][1]:
            if intervals[i+1][1] >= intervals[i][1]:
                intervals[i][1] = intervals[i+1][1]
            intervals.pop(i+1)
        else:
            i += 1
    
    return intervals
    

print(merge([[1, 4],[2,3]]))