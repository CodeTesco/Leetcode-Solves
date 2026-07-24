def insert(intervals, newInterval):
    if not intervals:
        return [newInterval]

    if intervals[-1][1] < newInterval[0]:
        intervals.append(newInterval)
        return intervals
    if intervals[0][0] > newInterval[1]:
        intervals.insert(0, newInterval)
        return intervals
    
    res = []

    for i, interval in enumerate(intervals):
        new_array = [0, 0]
        if interval[1] >= newInterval[0]:
            new_array[0] = interval[0] if interval[0] < newInterval[0] else newInterval[0]
            new_array[1] = newInterval[1] if newInterval[1] > interval[1] else interval[1]

            if newInterval[1] < interval[0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                break
            i += 1

            if i < len(intervals):
                while intervals[i][0] <= newInterval[1]:
                    if intervals[i][1] >= newInterval[1]:
                        new_array[1] = intervals[i][1]
                        i += 1
                        break
                    if i + 1 < len(intervals):
                        i += 1
                    else:
                        i += 1
                        break

            res.append(new_array)
            res.extend(intervals[i:])
            break
        res.append(interval)

    return res

print(insert([[1,5]], [0,3]))