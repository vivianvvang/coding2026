import bisect

class Driver:
    def __init__(self, id: str, hourly_rate_usd: int):
        self.id = id
        self.rate_per_second = (hourly_rate_usd * 100) / 3600
        self.intervals = []
        self.last_paid_time = 0
    
    def add_interval(self, start, end):
        self.intervals.append([start, end])
        self.intervals.sort() # O(NlogN)

        merged = []
        l = 0
        for current_interval in self.intervals:
            if not merged or current_interval[0] > merged[-1][1]:
                merged.append(current_interval)
            else:
                merged[-1][1] = max(merged[-1][1], current_interval[1])  
        self.intervals = merged
    
    # part II
    def calculate_cost_by(self, end_time):
        total_secs = 0
        for s, e in self.intervals:
            if s >= end_time:
                break
            end = min(e, end_time)
            total_secs += (end - s)
        return int(total_secs * self.rate_per_second)

    # part III

    def get_intervals_in_window(self, s, e):
        valid_intervals = []
        for ts, te in self.intervals:
            if s >= te:
                break
            if ts < e and te > s:
                valid_intervals.append([ts, te])
        return valid_intervals

    def get_intervals_in_window_binary_search(self, s, e):
        if not self.intervals:
            return []

        idx = bisect.bisect_right([interval[1] for interval in self.intervals], s)
        valid_intervals = []
        for i in range(idx, len(self.intervals)):
            s, e = self.intervals[i]
            if s >= e:
                break # 超出时间窗，提前结束
            valid_intervals.append([s, e])
            
        return valid_intervals

class PayrollService:
    def __init__(self):
        self.drivers = {} # driver_id -> hourly pay rate
        self.sys_paid_until = {} # driver_id -> last paid time
    
    def add_driver(self, driver_id, hourly_rate):
        if driver_id not in self.drivers:
            self.drivers[driver_id] = Driver(driver_id, hourly_rate)
            self.sys_paid_until[driver_id] = 0

    def record_delivery(self, driver_id, s, e):
        if driver_id in self.drivers:
            self.drivers[driver_id].add_interval(s, e)

    def get_total_cost(self) -> int:
        total = 0
        for driver in self.drivers.values():
            if driver.intervals:
                max_time = driver.intervals[-1][1]
                total += driver.calculate_cost_by(max_time)
        return total
    
    # part II
    def pay_up_to(self, pay_time):
        total = 0
        for d_id, driver in self.drivers.items():
            paid_time = driver.calculate_cost_by(self.sys_paid_until[d_id])
            new_paid_time = driver.calculate_cost_by(pay_time)

            total += (new_paid_time - paid_time)
            self.sys_paid_until[d_id] = paid_time
        return total    
    
    def total_unpaid(self):
        total_to_pay = self.get_total_cost()
        total_paid = 0
        for d_id, driver in self.drivers.items():
            total_paid += driver.calculate_cost_by(self.sys_paid_until[d_id])
        return total_to_pay - total_paid
    
    def max_simultaneous_driver_intervals_past_24_hours(self, now):
        start  = now - 86400
        end = now
        events = []
        for driver in self.drivers.values():
            valid_intervals = driver.get_intervals_in_window(start, end)
            for s, e in valid_intervals:
                es = max(s, start)
                ee = min(e, end)

                if es < ee:
                    events.append((es, 1))
                    events.append((ee, -1))
        
        # x[0]: time，x[1] status
        events.sort(key=lambda x: (x[0], x[1]))

        max_concurrent = 0
        for time, status in events:
            current_concurrent += status
            if current_concurrent > max_concurrent:
                max_concurrent = current_concurrent
        return max_concurrent

if __name__ == "__main__":
    system = PayrollService()
    print("--- 1. Initialization ---")
    system.add_driver("Alice", 36)
    system.record_delivery("Alice", 100, 200) 
    system.record_delivery("Alice", 150, 250) 
    system.record_delivery("Alice", 400, 500)
    print("\n--- 2. Financial Checks ---")
    total_cost = system.get_total_cost()
    print(f"Get_Total_Cost(): {total_cost} cents (${total_cost/100:.2f})")


    # 4. Partial Payment (Pay up to timestamp 200)
    print("\n--- 4. Processing Payment ---")
    # Cuts the [100, 250] interval in half. Pays for 100 to 200 (100s = 100 cents).
    paid_batch_1 = system.pay_up_to(200)
    print(f"Pay_Up_To(200): Paid out {paid_batch_1} cents (${paid_batch_1/100:.2f})")

    # 5. Check Unpaid Balance
    print("\n--- 5. Total Unpaid ---")
    unpaid = system.total_unpaid()
    # Total (250) - Paid (100) = 150
    print(f"Total_Cost_Unpaid(): {unpaid} cents (${unpaid/100:.2f})")

    # 6. Final Payout (Pay up to end of time)
    print("\n--- 6. Final Payment ---")
    paid_batch_2 = system.pay_up_to(1000)
    print(f"Pay_Up_To(1000): Paid out {paid_batch_2} cents (${paid_batch_2/100:.2f})")
    print(f"Final Unpaid Balance: {system.total_unpaid()} cents")