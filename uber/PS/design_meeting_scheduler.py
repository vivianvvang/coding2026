from typing import List, Optional

class MeetingScheduler:
    def __init__(self, roomList: List[str]):
        self.sorted_rooms = sorted(roomList)
        self.recordMap = {room: [] for room in self.sorted_rooms}

    def schedule(self, start: int, end: int) -> str:
        for room in self.sorted_rooms:
            records = self.recordMap[room]
            
            to_insert = self._insert_meeting(records, start)
            
            if to_insert > 0 and records[to_insert - 1][1] > start:
                continue
            if to_insert < len(records) and records[to_insert][0] < end:
                continue
  
            records.insert(to_insert, [start, end])
            return room
        return ""

    def _insert_meeting(self, records, start):

        # consider start time only
        l, r = 0, len(records)
        # while l < r:
        #     mid = (l + r) // 2
        #     if records[mid][0] < start:
        #         l = mid + 1
        #     else:
        #         r = mid
        
        # binary search using master template:
        # looking for the minimal k value satisfying nums[k] >= target
        # find the right postion to insert (which will push rest of elements + 1)
        while l < r:
            mid = (l + r) // 2
            if records[mid][0] >= start:
                r = mid
            else:
                l = mid + 1
        return l

