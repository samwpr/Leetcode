def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    #print(intervals)
    for i in range(1, len(intervals)):
        #print(i)
        i1 = intervals[i - 1]
        print("i1", i1)
        i2 = intervals[i]
        print("i2", i2)

        if i1[1] > i2[0]:
            return False
    return True


print(canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
#print(canAttendMeetings([[7, 10], [2, 4]]))

#firstelement = lambda x: x[0]
#print(firstelement([[5, 10], [15, 20], [0, 30]]))