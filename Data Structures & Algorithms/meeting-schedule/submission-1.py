"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        schedule = [] #always valid, in order

        for inter in intervals:
            if len(schedule) == 0:
                schedule.append(inter)
                continue

            i = 0
            for s in schedule:
                if (s.start > inter.start):
                    break
                i += 1
            #inter belongs in i

            #can you schedule meeting?
            if i > 0:
                if schedule[i-1].end > inter.start:
                    return False
            if i < len(schedule):
                if schedule[i].start < inter.end:
                    return False
            schedule.insert(i + 1, inter)
        return True