# 1. flatten nested array
# 分别用递归和非递归写

class NestedArray:
	def __init__(self, is_nested, arr):
		self.arr = arr
		self.is_nested = is_nested

# [[1, 2, [3], 4], 5, [6, 7]]
nested_arr = NestedArray(
	True,
	[
		NestedArray(True, [NestedArray(False, 1), NestedArray(False, 2), NestedArray(True, [NestedArray(False, 3)]), NestedArray(False, 4)]),
		NestedArray(False, 5),
		NestedArray(True, [NestedArray(False, 6), NestedArray(False, 7)])
	]
)

class NestedArrayTuple:
	def __init__(self, nested_array, depth):
		self.nested_array = nested_array
		self.depth = depth

def unnested_array(nested_array, depth):
	if not depth or not nested_array.is_nested:
		return nested_array

	stack = []
	result = []

	for array in reversed(nested_array.arr):
		stack.append(NestedArrayTuple(array, depth - 1))

	while stack:
		top_arr_tuple = stack.pop()
		if top_arr_tuple.depth > 0 and top_arr_tuple.nested_array.is_nested:
			for array in reversed(top_arr_tuple.nested_array.arr):
				stack.append(NestedArrayTuple(array, top_arr_tuple.depth - 1))
		else:
			result.append(top_arr_tuple.nested_array.arr)

	return result


print(unnested_array(nested_arr, 2))


# 1.coding1: 一个亚裔小哥，问给一个log数组，给一个n代表每一页log capacity，给一个i代表page的index，让返回一个数组，
# 数组里每一个数代表这个cursor开头的log id。
# 写完以后发现还有第二题，现在给多个log数组，同样给每一页可以放多少log的n和page index，
# 让你反回同样的结果。但是是所有log数组的合并结果。这个题有点类似于离叩珥霰。

# mergeKlist

# Time complexity: lists size N, average list length K
# O(knlgN)
from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNodeTuple:
    def __init__(self, val, node):
        self.val = val
        self.node = node
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        priority_queue = PriorityQueue()
        dummy_head = ListNode()
        mover = dummy_head

        for linked_list_head in lists:
            if linked_list_head:
                priority_queue.put(ListNodeTuple(linked_list_head.val, linked_list_head))
        
        while not priority_queue.empty():

            cur_node = priority_queue.get().node
            mover.next = cur_node
            mover = cur_node

            if cur_node.next:
                priority_queue.put(ListNodeTuple(cur_node.next.val, cur_node.next))
        

        return dummy_head.next

        



# 地里经典，是给一些log让你实时返回这个event是不是有效的。要求是每个用户只能在一段时间内发出定量的event。有点类似于叁柳饵。

# 面试小哥是个国人，题目是地里的那个log timestamp的高频题，follow up我是用的map 存每个timestamp 的entry，val 就是一个list，
# 因为需要记录所有信息。follow up 之后，又发散性的问了在分布式的情况下怎么处理。

# 從log裡檢查ip是否為bot. 會給你input string, 每一行是timestamp及ip. 從給定的threshold輸出哪些ip是bot就行.
# follow-up是給你list of timestamp及ip, 每次輸入timestamp及ip時判斷這個ip是否為bot.

# 同一题的两问：
# part 1. 给 时间 和 IP， 看在提供的input里面如果ip 超出了一个threshold，判断为机器人，output 机器人的ip

# input: following string, and threshold


# 1, ip1
# 1, ip2
# 1, ip1
# 4, ip1
# 4, ip2
# 5, ip3

# isBot(String input, 3) -> ip1
# isBot(String input, 2) -> ip1, ip2

# isBot(String input, 1) -> ip1, ip2, ip3

# part 2. 给 时间 和 IP, 但是有需要看 sliding time window 里面的 ip 数量 超出了一个 threshold，output true/false

# # class CheckBot {
# #     public CheckBot(int threshold, int windowSize) {

# #     }


# #     public boolean isBot(int timestamp, String ip) {

# #     }

# # }

# # example:
# # Checkbot cb = new CheckBot(threshold = 3, sliding time size = 3);

# # isBot(0, ip1) -> false

# # isBot(1, ip1) -> false
# # isBot(1, ip1) -> true // reached threshold 3 within the time window of 3
# # isBot(4, ip2) -> false
# # isBot(5, ip1) -> false

from collections import defaultdict, deque

# use a map where key is the ip and value is a queue of timestamp
# when checking an ip, first pop out the old timestamp exceed timewindow
# then check if queue size (frequency) exceed the threshold
class CheckBot:
	def __init__(self, threshold, window_size):
		self.threshold = threshold
		self.window_size = window_size
		self.ip_to_timestamp_map = defaultdict(deque)

	def is_bot(self, time_stamp, ip_address):
		if ip_address in self.ip_to_timestamp_map:
			time_stamps = self.ip_to_timestamp_map[ip_address]

			while time_stamps and time_stamps[0] < time_stamp - self.window_size:
				time_stamps.popleft()

		self.ip_to_timestamp_map[ip_address].append(time_stamp)

		return len(self.ip_to_timestamp_map[ip_address]) >= self.threshold


cb = CheckBot(threshold=3, window_size=3)

print(cb.is_bot(0, "ip1"))  # False
print(cb.is_bot(1, "ip1"))  # False
print(cb.is_bot(1, "ip1"))  # True (3 requests at time 0, 1, 1)
print(cb.is_bot(4, "ip2"))  # False
print(cb.is_bot(5, "ip1"))  # False (timestamps at 1, 1, 5 => only 1 in last 3s)


# 好像没在店里看到这题, 
# input如下, ->代表function call, <- 代表function return, 
# output是frequency最高的call stack,
# 这个例子里就是"main->eventClick->eventClickAction". frequency是2， 1, 2, 3行是第一次出现, 1, 2, 5行是第二次出现 （3, 4行可以看作是offset了，我的理解）求加米！！！
# traces=[
# "-> main",
# "-> eventClick",

# "-> eventClickAction",
# "<- eventClickAction",
# "-> eventClickAction",
# "<- eventClickAction",
# "<- eventClick",
# "<- main",
# ]

# 然后约tech screen，问的是给日志，怎么判断
# 哪个function被call的最多，如果一样多的return第一个。日志的格式是有开始结束marker，像
# > main
# > a
# > b
# < b
# > b
# < b
# < a
# > a
# < a
# < main
# 没有recursive call。要过test case

# mostFrequentStack
# time complexity: worst case O(N^2)

from collections import defaultdict

def find_most_frequenct_stack(logs):
	frequency_map = defaultdict(int)
	cur_highest_frequency = 0
	cur_highest_frequency_stack = ''

	call_stacks = []

	for log in logs:
		action, call = log.split(' ')
		if action == '>':
			call_stacks.append(call)
			call_stacks_str = '<'.join(call_stacks)
			frequency_map[call_stacks_str] += 1

			if frequency_map[call_stacks_str] > cur_highest_frequency:
				cur_highest_frequency = frequency_map[call_stacks_str]
				cur_highest_frequency_stack = call_stacks_str
		else:
			call_stacks.pop()

	return cur_highest_frequency_stack

logs = [
    '> main',
    '> a',
    '> b',
    '< b',
    '> b',
    '< b',
    '< a',
    '> a',
    '< a',
    '< main'
]

print(find_most_frequenct_stack(logs))

# coding，把寺旧。不过要print座位。写了解法，一开始有bug，改了会。
# for each empty seats group between 2 occupied seats, 
# if the length is k [number of empty seats], then the maximum distance is (k + 1) / 2

# MaxDistance
def maxDistToClosest(seats) -> int:
	seats_length = len(seats)
	distance_group = 0
	max_distance = 0
	seat_index = -1

	for i in range(0, seats_length):
		if seats[i]:
			distance_group = 0
		else:
			distance_group += 1 
			if (distance_group + 1) / 2 > max_distance:
				seat_index = i
				max_distance = (distance_group + 1) / 2

	for i in range(0, seats_length):
		if seats[i]:
			if i > max_distance:
				max_distance = i
				seat_index = i - 1
			break

	for i in range(seats_length - 1, -1, -1):
		if seats[i]:
			if seats_length - i - 1 > max_distance:
				max_distance = seats_length - i - 1
				seat_index = i + 1
			break

	new_seats = seats.copy()
	new_seats[int(seat_index)] = 1

	print(seat_index, max_distance)

	return new_seats

seats = [1,0,0,0,1,0,1]

print(maxDistToClosest(seats))


# 7. 一道dfs，player根据当前cell值（J, W）可以跳格子或走格子，问能不能到终点。
# follow-up是最短路径。

# boardJump
walk_movements = [
	(0, 1),
	(0, -1),
	(1, 0),
	(-1, 0),
]
jump_movements = [
	(0, 2),
	(0, -2),
	(2, 0),
	(-2, 0)
]

def can_reach_destination(player, board, destination):
	return move(player, board, set(), destination)

def move(cur_cell, board, visited, destination):
	if destination == cur_cell:
		return True

	reach_destination = False
	if board[cur_cell[0]][cur_cell[1]] == 'W':
		movements = walk_movements
	else:
		movements = jump_movements

	for movement in movements:
		next_cell = (cur_cell[0] + movement[0], cur_cell[1] + movement[1])
		if next_cell[0] < 0 or next_cell[0] >= len(board) or next_cell[1] < 0 or next_cell[1] >= len(board[0]):
			continue
		if next_cell in visited:
			continue

		visited.add(next_cell)

		reach_destination = reach_destination or move(next_cell, board, visited, destination)

	return reach_destination


def reach_destination_shortest(player, board, destination):
	visited_to_destination = {
		player: 2*31,
		destination: 0
	}

	result = move_shortest(player, board, visited_to_destination, destination)

	print(visited_to_destination)
	return result

def move_shortest(cur_cell, board, visited_to_destination, destination):
	if destination == cur_cell:
		return 0

	reach_destination_steps = 2**31

	if board[cur_cell[0]][cur_cell[1]] == 'W':
		movements = walk_movements
	else:
		movements = jump_movements

	for movement in movements:
		next_cell = (cur_cell[0] + movement[0], cur_cell[1] + movement[1])
		if next_cell[0] < 0 or next_cell[0] >= len(board) or next_cell[1] < 0 or next_cell[1] >= len(board[0]):
			continue

		if next_cell in visited_to_destination and visited_to_destination[next_cell] == 2**31:
			continue

		if next_cell in visited_to_destination:
			reach_destination_steps = min(reach_destination_steps, visited_to_destination[next_cell] + 1)
			continue

		visited_to_destination[next_cell] = 2**31

		reach_destination_steps = min(reach_destination_steps, move_shortest(next_cell, board, visited_to_destination, destination) + 1)

	visited_to_destination[cur_cell] = reach_destination_steps

	return reach_destination_steps

board = [
	['J', 'W', 'W'],
	['W', 'J', 'W'],
	['J', 'W', 'J'],
]



#code轮是prefix题，具体的在另外一个回复了。
# remove string that is prefix of other string in an array. The ordering needs to be the same as the input
# 电面 就是地里常见的给list of strings 删除其他string的prefix的string。 follow up：删除其他string的substring

# ["a","abc","abc hello","bc"]
# string array，如果里面有string是另一个string prefix，remove prefix, and keep remaining string order same
# answer: ["abc hello","bc"]

# Remove prefix strings in a list of string.
# 比如 {"a", "ab", "abc"}， output: {"abc"}.
# {"a", "bc", "ab", "abc hello"} ， output: {"bc", "abc hello"}.
# 要求output array 要保持string 在input 里的顺序

# Remove prefix strings in a list of string.


# Example 1: input  {"a", "ab", "abc"} -> output: {"abc"}.
# Example 2: input {"a", "bc", "ab", "abc hello"} --> output: {"bc", "abc hello"}.

# 要求： output array 要保持String 在input 里的顺序。比如第二个例子: {"abc hello", "bc"} 顺序就不对了。。。

# 写了最简单的遍历方法。分了一下时间复杂度。提了一下 trie 的解法。没时间写。不管结果怎么样。小哥人挺nice。全程帮忙改typo. experience 不错。

# removePrefix

# 2 pass of the words list
# when check if prefix, go through trie tree for this word, in the end, if the node still has children, then it is a prefix
# time complexity O(kn) - k=average length of word n=number of word
# 
# if checking is substring, when insert word, also insert word's suffixs.
# for abcde, also insert bcde, cde, de, e. 
# while checking if substring from another word, go through trie tree, if the end node has children or is a suffix, 
# then it is a substring
class TrieNode:
	def __init__(self, word=None):
		self.word = word
		self.children = {}


def remove_prefix_words(words):
	result = []

	trie_tree = TrieTree()

	for word in words:
		trie_tree.insert_word(word)

	for word in words:
		if not trie_tree.check_is_prefix(word):
			result.append(word)

	return result

class TrieTree:
	def __init__(self):
		self.root = TrieNode()

	def insert_word(self, word):
		mover = self.root

		for ch in word:
			if ch not in mover.children:
				mover.children[ch] = TrieNode()

			mover = mover.children[ch]

		mover.word = word

	def check_is_prefix(self, word):
		mover = self.root

		for ch in word:
			mover = mover.children[ch]

		return bool(mover.children)


words = ["a","abc","abc hello", "bcd", "bc"]

print(remove_prefix_words(words))


# 五轮，四轮利口 + 模型设计讨论/project deep dive，一轮HM BQ

# 四轮利口分别是 奇异伞，五六零变形，物流+一道bucket sort忘记题目，七九 follow up 二一二

# subarray product
# Given an array of integers nums and an integer k, 
# return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0
class Solution:
	# greedy
    # 2 pointer left, right
    # calculate nums[left] times till nums[right]
    # when the product >= k, discard the nums[left], then left++
    # b/c we need continguous subarray, we need to keep discarding until product < k
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k and left <= right:
                product = product / nums[left]
                left += 1
            
            result += right - left + 1
        
        return result


# subarray sum
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2


class Solution:
    # if we have accumulated sum in array sums[]
    # if we found sums[i] - sums[j] = k
    # meaning sums of subarray i to j is k
    
    # since subarray's sum can show up multiple times - [-1, 1, -1] => 0 twice
    # calculate the accumulated sums of nums
    # and store them into a map of frequency
    # if we found accumulated_sum - k in the map, meaning previously there are
    # frequency[accumulated_sum - k] times the sum = accumulated_sum - k shown up till
    # current index we are visiting
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_frequency_map = defaultdict(int)
        result = 0

        sum_frequency_map[0] = 1
        cur_sum = 0

        for num in nums:
            cur_sum += num
            if cur_sum - k in sum_frequency_map:
                result += sum_frequency_map[cur_sum - k]

            sum_frequency_map[cur_sum] += 1
        return result
        


# 14. 剩20min考一道经典老题 利口 贰佰



# 15. 然后一道地里利口老题·一把伞丝

# CPUThread

# single thread cpu
# use priority queue to sort the tasks based on processing time and index
# use a cur_time to record the current time
# everytime in the loop, if not task in pq to take 
# update cur_time to next task in task pool
# insert all task from pool into pq where their enqueue time <= cur_time
# take the top task from pq to process, update cur_time += task.process_time

# time complexity - O(NlgN)
from queue import PriorityQueue

class TaskToken:
    def __init__(self, enqueue_time, process_time, index):
        self.enqueue_time = enqueue_time
        self.process_time = process_time
        self.index = index

    def __lt__(self, other):
        if self.process_time == other.process_time:
            return self.index < other.index
        return self.process_time < other.process_time
    
    def __eq__(self, other):
        return self.process_time == other.process_time and self.index == other.index

    def __str__(self):
        return f'enqueue_time {self.enqueue_time} | process_time {self.process_time} | index {self.index}'


class Solution:
    # [[1,2],[2,4],[3,2],[4,1]]
    # pq: [[2, 4, 1]]
    # cur_task: [4, 1, 3]
    # index: 4
    # cur_time: 5
    # order: [1, 2, ]
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_pq = PriorityQueue()

        cur_time = 0
        executed_order = []
        task_index = 0

        sorted_task = [TaskToken(task[0], task[1], index) for index, task in enumerate(tasks)]
        sorted_task.sort(key=lambda x: x.enqueue_time)

        while task_index < len(sorted_task):
            if task_pq.empty() and cur_time <= sorted_task[task_index].enqueue_time:
                cur_time = sorted_task[task_index].enqueue_time
            
            while task_index < len(tasks) and sorted_task[task_index].enqueue_time <= cur_time:
                task_pq.put(sorted_task[task_index])
                task_index += 1
            
            execute_task = task_pq.get()
            executed_order.append(execute_task.index)
            cur_time += execute_task.process_time
        
        # after iterate through all tasks, there might be tasks left in pq
        while not task_pq.empty():
            execute_task = task_pq.get()
            executed_order.append(execute_task.index)
        
        return executed_order



# 19. 1- 45分钟 题库里面的 Coding: experience Scheduler
# 利口原题 621
# 其实之前写过，但是写的时候还是还是有点紧张，写了一个heap解法，忘记了有linear 解法，虽然linear的口里描述出来，但是没有implement完

# TaskScheduler
from collections import defaultdict

class Solution:
    # to arrange tasks, we use greedy solution
    # we allocate the task in this way
    # first put the most frequent task and between each of them
    # are idle slots, then there must be (most_frequency - 1) * n slots
    # then go through remaining tasks' frequency, fill the idle slot
    # but for each task, we can allocate at most (most_frequency - 1) number of tasks
    # eventually, after go through all tasks' freqneucy, if there are
    # idle slots, +task number as final total count
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies_map = defaultdict(int)

        for task in tasks:
            frequencies_map[task] += 1

        freq = sorted(list(frequencies_map.values()))
        gaps = freq[-1] - 1
        idle_slots = gaps * n

        # start from next highest frequency
        for i in range(len(freq) - 2, -1, -1):
            idle_slots -= min(gaps, freq[i])

        # all idle slots are filled
        if idle_slots < 0:
            return len(tasks)
        
        return idle_slots + len(tasks)

        


# 给了一道sliding window rate limiter，第一问是对request rate limit，第二问每个request有userId和userexperience，要对这两个分别rate limit

# RateLimiter
class Logger:

    def __init__(self):
        self.recorder = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        should_print = True

        if message in self.recorder:
            last_time = self.recorder[message]
        else:
            last_time = timestamp - 10

        if last_time > timestamp - 10:
            should_print = False
        
        if should_print:
            self.recorder[message] = timestamp
        
        return should_print




# 20. 第一问
# 写一道判断func是不是输入完成的函数叫isFuncComplete，比如
# print( -> false
# print() -> true
# 输入一个string，返回bool，不需要判断太复杂的逻辑，面试官其实只需要判断括号是不是对齐了


# 第二问
# 括号种类升级到了（【{，需要进行上面的类似判断


# 第三问
# 额外增加了引号，判断是否输入完成

# parenthese
def is_func_complete(func_str):
	parenthese = set(['(', ')', '[', ']', '{', '}'])

	parenth_pair = {
		')': '(',
		']': '[',
		'}': '{'
	}
	stack = []
	in_quote = False

	for c in func_str:
		if c == '\'':
			in_quote = not in_quote

		if in_quote:
			continue

		if c not in parenthese:
			continue

		if c not in parenth_pair:
			stack.append(c)
		elif stack and stack[-1] == parenth_pair[c]:
			stack.pop()
		else:
			return False

	return not bool(stack)


print(is_func_complete('print(this([{[]}\'avsedad[{(\'[]]))'))



# FindSublists
# Coding:
# given a integer list, a target index and a window size n, return all sublist with size n that contain target index (easy).
# Followup: among all sublists from last question, find the one that contain most # of target number, 
# (if equal, return the smaller index one). 这题用prefix sum+sliding window做。

# sliding window sublists
# use 2 pointer as sliding window, a counter counts current target number
# as long as counter > 0, put current sublist to result
def find_sublists(target, window_size, nums):
	left = 0
	right = 0
	counter = 0
	result = []

	while right < min(window_size, len(nums)):
		if nums[right] == target:
			counter += 1
		right += 1

	if counter > 0:
		result.append(nums[left:right])

	while right < len(nums):
		if nums[right] == target:
			counter += 1

		if nums[left] == target:
			counter -= 1

		right += 1
		left += 1

		if counter > 0:
			result.append(nums[left:right])

	return result

nums = [1, 2, 1, 3, 4, 2, 1, 9, 0, 2, 1]
nums2 = [2]

print(find_sublists(1, 3, nums))


# followup, 
def find_sublists(target, window_size, nums):
	left = 0
	right = 0
	cur_counter = 0
	max_count = 0
	best_start = 0

	while right < min(window_size, len(nums)):
		if nums[right] == target:
			cur_counter += 1
		right += 1

	max_count = cur_counter

	while right < len(nums):
		if nums[right] == target:
			cur_counter += 1

		if nums[left] == target:
			cur_counter -= 1

		right += 1
		left += 1

		if cur_counter > max_count:
			max_count = cur_counter
			best_start = left

	return nums[best_start:best_start + window_size]

nums = [1, 1, 1, 1, 4, 2, 1, 9, 1, 1, 1]
nums2 = [2]

# print(find_sublists(1, 5, nums))

# 21. An offline music player has a playlist of songs and the following two modes：
# Random – at each step, picks the next song uniformly at random from the entire playlist (with “replacement,” so the same song can appear back-to-back).
# Shuffle – often interpreted iPod‐style:
# The player randomly permutes the entire playlist (each song appears exactly once in that permutation).
# It then plays through that permutation in order.
# Once all songs have been played, it (optionally) picks a new random permutation and starts again.

# You start listening in the middle of whatever the player is doing. You hear a short sequence of songs, then you stop. 
# 问题：“Could the sequence I heard come from ‘shuffle’ mode?”
# 然后给了一些example:
# ["A", "A", "A"]
# → labeled # shuffle

# ["A", "B", "C"]
# → labeled # random

# ["A", "A", "C", "A"]
# → ???

# ["A", "C", "A", "B", "A", "C", "B", "G"]
# → ???

#  https://www.1point3acres.com/bbs/thread-1122435-1-1.html

# a valid shuffle always falls in this pattern
# a prefix as part of a loop, several full loop, then a suffix as part of loop
# prefix is all unique songs same as suffix and size smaller than total count of unique songs (as U)
# To check if a sequence is valid shuffle, we can have a fix window (size = U) moving from left to right
# if the window's songs are unique, meaning it is a loop, and if window's left - 1 is also a valid loop end and goes on,
# then from 0 to this window's right, is a sequence of valid shuffle

# so to do this, we need an array to record if current slot is a valid shuffle's end
# 1. check prefix, before encounter any duplicate songs, the subsequence should consider prefix
# 2. same for suffix
# maintain a map to tract song's count
# maintain a fixed size window moving forward, if window is a loop and if is_valid[window_left - 1] = True, 
# meaning we can append cur window to a shuffle sequence
# We can also check if is_valid[window_right + 1] = True, meaning we meet the suffix and now whole sequence is a shuffle

# time complexity: O(U)
from collections import defaultdict

def is_shuffle(songs):
	is_valid = [None] * len(songs)
	unique_songs_count = len(set(songs))


	# check prefix
	seen = set()
	for i in range(0, len(songs)):
		if songs[i] in seen:
			break
		seen.add(songs[i])
		is_valid[i] = True

	# check suffix
	seen = set()
	for i in range(len(songs) - 1, -1, -1):
		if songs[i] in seen or is_valid[i] is not None:
			break
		seen.add(songs[i])
		is_valid[i] = True	

	cur_window = defaultdict(int)

	# init window
	for i in range(0, unique_songs_count):
		cur_window[songs[i]] += 1

	if len(cur_window) == unique_songs_count:
		is_valid[unique_songs_count - 1] = True

	# move it to current window right side
	idx_right = unique_songs_count
	idx_left = 1

	while idx_right < len(songs):
		previous_end = idx_left - 1
		# refresh window
		cur_window[songs[idx_right]] += 1
		cur_window[songs[previous_end]] -= 1

		if cur_window[songs[previous_end]] == 0:
			del cur_window[songs[previous_end]]

		if len(cur_window) == unique_songs_count and is_valid[previous_end]:
			is_valid[idx_right] = True
		else:
			is_valid[idx_right] = False

		# meet suffix
		if is_valid[idx_right] and idx_right + 1 < len(songs) and is_valid[idx_right + 1]:
			return True

		# move index
		idx_right += 1
		idx_left += 1


	return is_valid[len(songs) - 1]


print(is_shuffle(["A", "B", "C", "D", "E", "F", "A", "B", "C", "D", "E", "E", "E"]))

# 22. input:
# list of int : [1,2,3,4,5,6,7,4,23,1]

# int: amount of segment
# output: random 的 output input list 里的 int 到 segment里
# example
# input: [1,2,3,4,5,6] segment number 2
# output: [[2,5,6], [1,3,4]]

# https://www.1point3acres.com/bbs/thread-1122032-1-1.html

import random

# SegmentShuffle
def shuffle_segments(nums, segment_count):
	shuffle_nums = nums.copy()

	segments = []
	for i in range(0, segment_count):
		segments.append([])

	pool_size = len(nums) - 1
	segment_index = 0

	while pool_size >= 0:
		shuffle_index = random.randint(0, pool_size)

		# assign number into segments
		segments[segment_index].append(shuffle_nums[shuffle_index])
		segment_index = (segment_index + 1) % segment_count

		# swap the number to keep it out of random int pool
		tmp = shuffle_nums[pool_size]
		shuffle_nums[pool_size] = shuffle_nums[shuffle_index]
		shuffle_nums[shuffle_index] = tmp

		pool_size -= 1


	return segments

nums = [1,2,3,4,5,6,7]
print(shuffle_segments(nums, 6))




# ID manager管理[1, MaxLong]的id。实现两个api：
# acquire(): 返回pool中最小的id。
# release(id):把id返回到pool。
# https://www.1point3acres.com/bbs/thread-1118352-1-1.html

# 让实现一个ID pool，ID的range是1到max long。有俩API acquire（）和release（），前者返回一个最小的空闲的id，后者收回一个正在使用的ID，把它重新放回池子。
# 我用了一个min heap来存available的IDs，一开始先只把1放进去。只有当heap空了的时候，放入下一个available的ID。在release的时候再把ID放回heap。
# 再用一个set来存放正在使用的ID。大家有更优解，请不吝赐教。
# 这道题，我分析可能挂在复杂度分析，我说这两个function的时间都是O(logn)，n是max long，但具体说acquire的时候我记成heap poll（）的复杂度是O（1）了，应该是O（logn）的。估计挂这里了。但我代码能跑，用各种edge cases也测过了。
# 但是感觉面试官follow我的思路有点疑惑，也许这不是她期待的解法。欢迎大家讨论。
# https://www.1point3acres.com/bbs/thread-1102457-1-1.html

from queue import PriorityQueue

MAX_VALUE = 2**63 - 1


class IDManager:
	def __init__(self):
		self.released_ids = PriorityQueue()
		self.water_mark = 1

	def acquire(self):
		if self.released_ids.empty():
			if self.water_mark < 0:
				raise Exception('No avaiable ids')

			acquire_id = self.water_mark
			if self.water_mark == MAX_VALUE:
				self.water_mark = -1
			else:
				self.water_mark += 1
		else:
			acquire_id = self.released_ids.get()

		return acquire_id

	def release(self, id):
		self.released_ids.put(id)


manager = IDManager()

print(manager.acquire())
print(manager.acquire())
print(manager.acquire())
print(manager.release(3))
print(manager.release(2))
print(manager.acquire())






# You're running a pool of servers where the servers are numbered sequentially starting from 1.


# Over time, any given server might explode, in which case its server number is made available for reuse. 
# When a new server is launched, it should be given the lowest available number.  


# Write a function which, given the list of currently allocated server numbers, returns the number of the next server to allocate. 
# In addition, you should demonstrate your approach to testing that your function is correct.


# You may choose to use an existing testing library for your language if you choose, or you may write your own process if you prefer.  


# For example, your function should behave something like the following:  
#   >> next_server_number([5, 3, 1])
#   2
#   >> next_server_number([5, 4, 1, 2])
#   3
#   >> next_server_number([3, 2, 1])
#   4
#   >> next_server_number([2, 3])
#   1
#   >> next_server_number([]) #   1
#   >> next_server_number([1,1.5,2,2.5,3,3.5,4,5,5.5])
#   6
#   >> next_server_number([2.5])

# https://www.1point3acres.com/bbs/thread-1098941-1-1.html





44. 读一个 csv 文件，文件里有10k+ rows，每一行有三个element，game id， game score， quality （good/bad）


有个threshold（比如 65%），题目要求选一个score，所有大于这个score 的 game 里面 bad game 比例不低于 threshold

output 最小的game score，game score 不一定是input 里面的score。
比如，game 1， 20， good； game 2， 30， good； game3， 40， bad ； game4，40， bad； game5 50 bad。 
答案是21，因为大于21 的score 有4个游戏，三个是bad，一个是good，所以[21, 30] 都满足theshold 要求，选择最小的。
# https://www.1point3acres.com/bbs/thread-1092327-1-1.html

# games = [
# 	['game1', '20', 'good'],
# 	['game5', '50', 'bad'],
# 	['game3', '40', 'bad'],
# 	['game2', '30', 'good'],
# 	['game4', '40', 'bad'],
# ]

"""
score_to_game_quality
{
	20 - [good-1, bad-0]
	50 - [good-0, bad-1]
	40 - [good-0, bad-2]
	30 - [good-1, bad-0]
}

max score - 50


"""

# use a map record good/bad count per score
# and max_score,
# then go from max_score to 0 and check bad/total ratio
# once threshold match, the next time threshold not match, last score 
# is the minimal score for question

from collections import defaultdict

class GameQuality:
	def __init__(self):
		self.good_count = 0
		self.bad_count = 0

def find_minimal_score(games, threshold):
	score_to_game_quality = defaultdict(GameQuality)
	max_score = 0

	for game in games:
		if game[2] == 'good':
			score_to_game_quality[game[1]].good_count += 1
		else:
			score_to_game_quality[game[1]].bad_count += 1

		if game[1] >= max_score:
			max_score = game[1]


	cur_total = 0
	cur_bad_total = 0
	requirement_matched = False

	score = max_score

	while score >= 0:
		if score in score_to_game_quality:
			game_quality = score_to_game_quality[score]
			
			cur_total += game_quality.good_count + game_quality.bad_count
			cur_bad_total += game_quality.bad_count

		cur_threshold = float(cur_bad_total) / float(cur_total)

		if cur_threshold >= threshold:
			requirement_matched = True
		elif requirement_matched:
			return score + 1

		score -= 1

	if requirement_matched:
		return 0

	# no score found
	return None




games = [
	['game1', 20, 'good'],
	['game5', 50, 'good'],
	['game6', 60, 'bad'],
	['game3', 40, 'good'],
	['game2', 30, 'good'],
	['game4', 40, 'good'],
]


print(find_minimal_score(games, 0.65))






45. 面试官是白人小哥，人挺好的，题目是地里出现过的generate email的题，情景是给三个input，然后output是email body string

第一个input是一个list of detected key words，比如 “hack”，比如“heroin”
第二个input我记不清了，好像是list of string，每个string是keyword to category的mapping，e.g.：["heroin,Drug"]

第三个input是一个list of strings，每一个string是category到instrction的mapping，e.g.：["drug,    Please be aware of drug dealing in the game, report to police if necessary"]
然后输出的email body就是告诉用户，游戏里有XXX类型的关键词被检测到了，你可以按照XXX instructions做。

题不难，主要就是一点字符串处理(大小写，split，join之类的)，我还google了怎么删除strings里的leading spaces，感觉并不影响通过。

这题做完之后还有一个followup，是问如果下游组近期收到的email是之前的三倍，看你会怎么investigate，你可以提问题，面试官会回答，最后找到原因。不知道这个占面试考察多大比例。

# https://www.1point3acres.com/bbs/thread-1091842-1-1.html



Phone Screen: phase1 一个m*n的grid，每个grid里面是一个0-9的数，收集所有横向/纵向3个或3个以上相连的数并记录在结果数组里，记录格式是[位置，长度]，
有上到下/左到右的记录顺序要求 phase2 现在把所有这些相连的数都remove掉让上方的数字往下掉，空的位置填0补充，输出这样操作后的grid

datasize很小所以难度不是很大，但是工程细节比较多，感觉R家所有题都是这样
# 感觉是723变形? 多謝樓主分享
# https://www.1point3acres.com/bbs/thread-1138132-1-1.html

# candy
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        crushed_set = self.find(board)

        while crushed_set:
            self.crush(board, crushed_set)
            self.drop(board)

            crushed_set = self.find(board)

        return board


    def find(self, board):
        height = len(board)
        width = len(board[0])

        crushed_set = set()

        # check vertically
        for c in range(0, width):
            for i in range(1, height - 1):
                if board[i][c] == 0:
                    continue
                
                if board[i - 1][c] == board[i][c] and board[i][c] == board[i + 1][c]:
                    crushed_set.add((i - 1, c))
                    crushed_set.add((i, c))
                    crushed_set.add((i + 1, c))

        # check horizontally
        for c in range(1, width - 1):
            for r in range(0, height):
                if board[r][c] == 0:
                    continue
                
                if board[r][c - 1] == board[r][c] and board[r][c] == board[r][c + 1]:
                    crushed_set.add((r, c))
                    crushed_set.add((r, c - 1))
                    crushed_set.add((r, c + 1))

        return crushed_set
    
    def crush(self, board, crushed_set):
        for (r, c) in crushed_set:
            board[r][c] = 0

    def drop(self, board):
        for c in range(0, len(board[0])):
            lowest_zero_index = -1

            for r in range(len(board) - 1, -1, -1):
                if board[r][c] == 0:
                    lowest_zero_index = max(lowest_zero_index, r)
                elif lowest_zero_index >= 0:
                    temp = board[r][c]
                    board[r][c] = board[lowest_zero_index][c]
                    board[lowest_zero_index][c] = temp

                    lowest_zero_index -= 1
        

# =====================================

# robloxCandy

def find_connected(board):
	vertical_connected = []
	horizontal_connected = []

	# check horizontally
	for r in range(0, len(board)):
		left_idx = 0
		right_idx = 1

		while right_idx < len(board[0]):
			while right_idx < len(board[0]) and board[r][left_idx] == board[r][right_idx]:
				right_idx += 1

			if right_idx - left_idx >= 3:
				horizontal_connected.append(((r, left_idx), right_idx - left_idx))

			left_idx = right_idx

	# check vertically
	for c in range(0, len(board[0])):
		left_idx = 0
		right_idx = 1

		while right_idx < len(board):
			while right_idx < len(board) and board[left_idx][c] == board[right_idx][c]:
				right_idx += 1

			if right_idx - left_idx >= 3:
				vertical_connected.append(((left_idx, c), right_idx - left_idx))

			left_idx = right_idx

	return (vertical_connected, horizontal_connected)

def crush(board, vertical_connected, horizontal_connected):
	for bar in vertical_connected:
		start_idx = bar[0][0]
		c = bar[0][1]
		for r in range(start_idx, start_idx + bar[1]):
			board[r][c] = 0

	for bar in horizontal_connected:
		start_idx = bar[0][1]
		r = bar[0][0]
		for c in range(start_idx, start_idx + bar[1]):
			board[r][c] = 0


# process drop for each column vertically
# maintain a pointer at lowest 0's index
# when meeting a non-zero slot, swap and move the point up 
# by 1 to next lowest zero index
def drop(board):
	for c in range(0, len(board[0])):
		lowest_zero = -1

		for r in range(len(board) - 1, -1, -1):
			if board[r][c] == 0:
				lowest_zero = max(lowest_zero, r)
			elif lowest_zero >= 0:
				temp = board[r][c]
				board[r][c] = board[lowest_zero][c]
				board[lowest_zero][c] = temp

				lowest_zero -= 1


board = [
	[110,  5,112,113,114],
	[210,211,  5,213,214],
	[310,311,  3,313,314],
	[410,411,412,  5,414],
	[  5,  1,512,  3,  3],
	[610,  4,  1,613,614],
	[710,  1,  2,713,714],
	[810,  1,  2,  1,  1],
	[  1,  1,  2,  2,  2],
	[  4,  1,  4,  4,101]
]

board2 = [
	[1, 1, 1, 1]
]

def print_board(board):
	for r in board:
		print(r)

vert_con, hori_con = find_connected(board)
crush(board, vert_con, hori_con)
print_board(board)
print('=================')

drop(board)
print_board(board)



# rain water
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left = 0
        left_max = 0
        right = len(height) - 1
        right_max = 0
        
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water


# 国人小哥， 课程安排2的变种，三个关键点：一是从int变成了string。2是输入不再是pair而是2d array，arr[i][0] depends on arr[i][1...j]。
# 3是如果两个string的order相同，那么要按照他们出现的顺序输出。

# 我把topo写了，研究了这个order，但是面试官说了topo里有个小错误，但是没时间改了。
from collections import deque, defaultdict


def find_order(courses, prerequisites):
	indegree = defaultdict(int)
	downstreams = defaultdict(list)
	course_to_index = {course: index for index, course in enumerate(courses)}

	for dependencies in prerequisites:
		course = dependencies[0]
		
		for i in range(1, len(dependencies)):
			dependency = dependencies[i]
			
			indegree[course] += 1
			downstreams[dependency].append(course)

	queue = deque()
	results = []

	temp = []
	for course in courses:
		if course not in indegree or not indegree[course]:
			temp.append(course)

	temp.sort(key=lambda x: course_to_index[x])

	for c in temp:
		queue.append(c)

	while queue:
		cur_course = queue.popleft()
		results.append(cur_course)

		if cur_course not in downstreams:
			continue

		temp_queue = []
		for downstream in downstreams[cur_course]:
			indegree[downstream] -= 1

			if not indegree[downstream]:
				temp_queue.append(downstream)

		temp_queue.sort(key=lambda x: course_to_index[x])
		for course in temp_queue:
			queue.append(course)


	if len(results) != len(courses):
		return []

	return results


courses = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
prerequisites = [
	['B', 'C', 'D'],
	['C', 'F'],
	['D', 'E'],
	['E', 'G', 'A']
]




print(find_order(courses, prerequisites))






