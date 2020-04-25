# This problem was asked by Snapchat.

# Given a list of possibly overlapping intervals, return a new list of intervals where all 
# overlapping intervals have been merged.

# The input list is not necessarily ordered in any way.

# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

def merged_intervals(intervals):
    merged_intervals = intervals

    for interval in intervals:
        interval_min = min(interval)
        interval_max = max(interval)

        for workingInterval in intervals:
            workingInterval_min = min(workingInterval)
            workingInterval_max = max(workingInterval)

            if workingInterval_min < interval_min and workingInterval_max > interval_max:
                intervals.remove(interval)
                break
    
    return merged_intervals

print(merged_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]))