from collections import deque
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

class TunnelScheduler:
    def __init__(self):
        self.entry_queue = deque()
        self.max_wait_time = 0
    
    def add_vehicle(self, arrival_time, processing_time):
        self.entry_queue.append((arrival_time, processing_time))
    
    def process_vehicles(self):
        current_time = 0
        while self.entry_queue:
            arrival_time, processing_time = self.entry_queue.popleft()
            if arrival_time > current_time:
                current_time = arrival_time
            wait_time = current_time - arrival_time
            if wait_time > self.max_wait_time:
                self.max_wait_time = wait_time
            current_time += processing_time
        return self.max_wait_time

scheduler = TunnelScheduler()
# Vehicle arrivals: (arrival_time, processing_time)
scheduler.add_vehicle(0, 3)
scheduler.add_vehicle(1, 2)
scheduler.add_vehicle(3, 1)
scheduler.add_vehicle(4, 2)
scheduler.add_vehicle(6, 1)

# Calculate LCM of first two processing times for synchronization
sync_interval = lcm(3, 2)

max_wait_time = scheduler.process_vehicles() + sync_interval
print(f"Result: {max_wait_time}")