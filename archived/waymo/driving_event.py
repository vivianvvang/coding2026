from enum import Enum
class Status(Enum):
    OPEN = 1
    CLOSE = 2

class Event:
    def __init__(self, type, status, time):
        self.type = type
        self.status = status
        self.time = time

class Solution:
    def drive_time(self, events):
        tmap = {}
        for event in events:
            if event.status == Status.OPEN:
                if event.type in tmap:
                    return "invalid"
                tmap[event.type] = event.time
            elif event.status == Status.CLOSE:
                if event.type not in tmap:
                    return "invalid"
                del tmap[event.type]
        if len(tmap) == 0:
            return "ready"
        return "not_ready"
    
    def second_q(self, events, start, end):
        ts = set()
        avaliable = 0 
        total = 0
        for event in events:
            if event.status == Status.OPEN:
                if event.type in ts:
                    return -1
                if len(ts) == 0 and event.time >= start:
                    total += min(end, event.time) - max(avaliable, start)
                    avaliable = 0
                ts.add(event.type)
            elif event.status == Status.CLOSE:
                if event.type not in ts:
                    return -1
                ts.remove(event.type)
                if len(ts) == 0:
                    avaliable = event.time
        if end > avaliable:
            total += end - avaliable
        return total

s = Solution()
events = [
    Event('oil', Status.OPEN, 10), 
    Event('oil', Status.CLOSE, 15)
]
print(s.drive_time(events))
events_two = [
    Event('oil', Status.OPEN, 10), 
    Event('oil', Status.CLOSE, 15),
    Event('docs', Status.OPEN, 20),
    Event('docs', Status.CLOSE, 30)
]
print(s.second_q(events_two, 0, 40))
print(s.second_q(events_two, 15, 30))