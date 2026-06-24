class BankSystem:
    def __init__(self):
        self.record = {} # user -> {"time_stamp": [], prefix_sum: [], balence: int}

    def _create_account_if_not_exist(self, id):
        if id not in self.record:
            self.record[id] = {
                "timestamp": [],
                "balence": 0,
                "prefix_sum": []
            }
    def deposit(self, id, timestamp, amount):
        self._create_account_if_not_exist(id)
        ur = self.record[id]
        ur["timestamp"].append(timestamp)
        ur["balence"] += amount
        ur["prefix_sum"].append(ur["balence"])
        return ur["balence"]

    def withdraw(self, id, timestamp, amount):
        self._create_account_if_not_exist(id)
        ur = self.record[id]
        if ur["balence"] < amount:
            return -1
        self.deposit(id, timestamp, -amount)
        return ur["balence"]

    def check(self, id):
        if id not in self.record:
            return -1
        return self.record[id]["balence"]

    def _find_upper_bound(self, target, user_record): # find first ts where ts > start
        l, r = 0, len(user_record)
        while l < r:
            mid = l + (r - l) // 2
            if user_record["timestamp"][mid] > target:
                r = mid
            else:
                l = mid + 1
        return l

    def balance(self, id, startTime, endTime): # O(logN)
        if id not in self.record:
            return -1
        ur = self.record[id]
        # balence btwn (startTime, endTime]: prefix_sum[startTime - 1, endTime]
        # first ts > startTime [upperbound]
        start_idx = self._find_upper_bound(startTime, ur)
        # last ts <= endTime -> (first ts > endTime) - 1 [upperbound]
        end_idx = self._find_upper_bound(endTime, ur) - 1
        if start_idx > end_idx:
            return 0    
        end_sum = ur["prefix_sum"][end_idx]
        start_sum = ur["prefix_sum"][start_idx - 1] if start_idx > 0 else 0
        return end_sum - start_sum
    

bank = BankSystem()
print(bank.deposit(1, 0, 100))  # ID 1 deposits 100 at t=0
print(bank.deposit(1, 10, 50))  # ID 1 deposits 50 at t=10
print(bank.withdraw(1, 20, 20)) # ID 1 withdraws 20 at t=20. Returns True.
print(bank.check(1))            # Returns 130 (100 + 50 - 20)
print(bank.balance(1, 0, 20))   # Range is (0, 20]. Valid timestamps: 10, 20.
