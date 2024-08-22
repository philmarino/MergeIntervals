def merge(intervals):
    output = []
    output.append(intervals[0])
    
    #assumes intervals are in ascending order
    for i in range(1,len(intervals)):
        merge = False
        for j in range(len(output)):
            if intervals[i][0] <= output[j][1]: #they overlap
                output[j][1] = intervals[i][1]
                merge = True
        if not merge:
            output.append(intervals[i])

    return output

# Example 1:
# Input: 
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: 
intervals = [[1,4],[4,5]]
print(merge(intervals))
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
