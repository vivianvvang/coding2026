import bisect
"""
Core Problem: Meeting SchedulerAPI: boolean book(int start, int end)Input / Output Example:book(10, 20) -> 
Returns true (Successfully booked)book(15, 25) -> Returns false (Conflict with 10-20, fails)book(20, 30) -> 
Returns true (Successfully booked, adjacent intervals usually don't conflict)What it tests: 

Optimizing from an $O(N)$ linear scan to an $O(\log N)$ search. The interviewer expects you to use a balanced binary search tree (like a TreeMap)
 or an Interval Tree to efficiently find and insert non-overlapping time slots.
 
 
Follow-up 1: Add a method to return the last N meetingsAPI:
List<Meeting> getLastN(int n)Input / Output Example:(Assuming [10, 20] and [20, 30] were successfully booked in that order)getLastN(2) -> 
Returns [[20, 30], [10, 20]] (Ordered by the chronological order of the booking actions, with the most recently booked meeting first)What it tests: 
Data structure composition. A TreeMap naturally sorts by the meeting's start time, not the order in which they were created.
    You need to introduce a Doubly Linked List. Every time a meeting is successfully booked, you append it as a new node to the head of this list.

Follow-up 2: Add a method to cancel a meeting, updating the last N meetingsAPI: boolean cancel(int meetingId)
(Assuming each meeting is assigned a unique ID)Input / Output Example:cancel(1) -> Returns true (Assuming ID 1 is the [10, 20] meeting,
 it is canceled)getLastN(2) -> Returns [[20, 30]] (The [10, 20] meeting is removed from the history list)
What it tests: Synchronizing and maintaining consistency across multiple complex data structures. 
 To remove a node from the middle of a doubly linked list in $O(1)$ time, you must introduce a HashMap<MeetingId, Node>
to map IDs directly to their linked list nodes. This turns the problem into a variation of the classic LRU Cache.
           
Follow-up 3: Handling Concurrent RequestsWhat it tests: Backend system design and multi-threading fundamentals.
           The Question: What happens if 1,000 users call book() at the exact same millisecond?Your initial answer:
            Add a Global Lock to ensure that only one thread can modify the tree and the linked list at a time,
            preventing race conditions.The Interviewer's Goal: A global lock bottlenecks performance. 
            They want to hear how you would improve system throughput.The Improvement: Room-level locks (fine-grained locking). 
            Real scheduling systems have multiple rooms. You can use a structure like ConcurrentHashMap<RoomId, ReentrantLock>.
            When a user books Room A, you only lock Room A's resources.
            This doesn't block users trying to book Room B, drastically increasing concurrency and performance.
"""
from sortedcontainers import SortedDict
class MeetingScheduler:
    def __init__(self):
        # Stores tuples of (start, end)
        # key: start_time, value: end_time
        self.calendar = SortedDict()
        self.meeting_counter = 0 # To assign unique IDs later

    def book(self, start: int, end: int) -> bool:
        if start >= end:
            return False
            
        # bisect_right 会返回第一个 key 大于 start 的索引 (即下一个可能冲突的会议)
        # 时间复杂度 O(log N)
        idx = self.calendar.bisect_right(start) # log(n)
        
        # 1. 检查跟前一个会议是否冲突
        if idx > 0:
            # 获取前一个会议的 start_time (key)
            prev_start = self.calendar.keys()[idx - 1]
            prev_end = self.calendar[prev_start]
            if prev_end > start:
                return False
                
        # 2. 检查跟后一个会议是否冲突
        if idx < len(self.calendar):
            # 获取后一个会议的 start_time (key)
            next_start = self.calendar.keys()[idx]
            if next_start < end:
                return False
                
        # 3. 没有任何冲突，插入新会议
        # 这一步在 SortedDict 中是 O(log N) 的时间复杂度
        self.calendar[start] = end
        return True

scheduler = MeetingScheduler()
scheduler.book(1, 10) # true
scheduler.book(2, 12) # false
scheduler.book(11, 20) # true
scheduler.book(21, 30) # true

import bisect

class MeetingSchedulerFU1:
    def __init__(self):
        self.calendar = []
        self.history = [] # Tracks the order of booked meetings

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_right(self.calendar, (start, end))
        
        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False
            
        self.calendar.insert(idx, (start, end))
        # Record the successful booking in our history
        self.history.append((start, end))
        return True

    def get_last_n(self, n: int) -> list:
        # Return the last N meetings, most recent first
        return self.history[-n:][::-1] if n <= len(self.history) else self.history[::-1]
    
import bisect

class Node:
    def __init__(self, meeting_id, start, end):
        self.meeting_id = meeting_id
        self.start = start
        self.end = end
        self.prev = None
        self.next = None

class MeetingSchedulerFU2:
    def __init__(self):
        self.calendar = []  # Still stores (start, end, meeting_id) for sorting
        self.node_map = {}  # Map: meeting_id -> Node
        self.meeting_id_counter = 0
        
        # Doubly Linked List dummy head and tail
        self.head = Node(-1, -1, -1)
        self.tail = Node(-1, -1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node: Node):
        """Adds a node right after the dummy head (most recent)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        """Removes a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def book(self, start: int, end: int) -> int:
        """Returns meeting_id if successful, -1 if failed."""
        idx = bisect.bisect_right(self.calendar, (start, end, -1))
        
        if idx > 0 and self.calendar[idx - 1][1] > start:
            return -1
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return -1
            
        self.meeting_id_counter += 1
        m_id = self.meeting_id_counter
        
        self.calendar.insert(idx, (start, end, m_id))
        
        # Add to history (Doubly Linked List & Map)
        new_node = Node(m_id, start, end)
        self._add_to_head(new_node)
        self.node_map[m_id] = new_node
        
        return m_id

    def cancel(self, meeting_id: int) -> bool:
        if meeting_id not in self.node_map:
            return False
            
        node_to_cancel = self.node_map[meeting_id]
        
        # 1. Remove from calendar array (O(N) in Python list, O(log N) in balanced BST)
        self.calendar.remove((node_to_cancel.start, node_to_cancel.end, meeting_id))
        
        # 2. Remove from history (O(1) operations)
        self._remove_node(node_to_cancel)
        del self.node_map[meeting_id]
        
        return True

    def get_last_n(self, n: int) -> list:
        result = []
        curr = self.head.next
        while curr != self.tail and len(result) < n:
            result.append((curr.start, curr.end))
            curr = curr.next
        return result
    

import bisect
import threading
from collections import defaultdict

class ConcurrentMeetingScheduler:
    def __init__(self):
        # Dictionary mapping room_id to its specific calendar list
        self.room_calendars = defaultdict(list)
        # Dictionary mapping room_id to its specific thread lock
        self.room_locks = defaultdict(threading.Lock)

    def book(self, room_id: str, start: int, end: int) -> bool:
        if start >= end:
            return False
            
        # Acquire the lock ONLY for the specific room being requested
        with self.room_locks[room_id]:
            calendar = self.room_calendars[room_id]
            
            idx = bisect.bisect_right(calendar, (start, end))
            
            if idx > 0 and calendar[idx - 1][1] > start:
                return False
            if idx < len(calendar) and calendar[idx][0] < end:
                return False
                
            calendar.insert(idx, (start, end))
            return True
            
    # Note: If you needed to implement cancel() or getLastN() here, 
    # you would also wrap their critical sections in the same room lock.