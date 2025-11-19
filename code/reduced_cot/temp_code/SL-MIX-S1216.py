import heapq
from math import gcd

def prime_filter(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            return False
        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                return False
        return True
    return wrapper

@prime_filter
def process_frequency(freq):
    return freq

class SignalBatcher:
    def __init__(self):
        self.batch_sum = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def add_signal(self, sig):
        self.batch_sum += sig

# Reference parameters
reference_freq = 42
alpha_cal = 6
beta_cal = 14
lcm_calibration = (alpha_cal * beta_cal) // gcd(alpha_cal, beta_cal)  # LCM(6,14) = 42

cosmic_observations = [17, 29, 42, 51, 73, 89, 97, 103]
signal_heap = []

for obs in cosmic_observations:
    heapq.heappush(signal_heap, obs)

primary_accumulator = 0

while signal_heap:
    current_signal = heapq.heappop(signal_heap)
    if process_frequency(current_signal):
        if gcd(current_signal, reference_freq) == lcm_calibration:
            with SignalBatcher() as batcher:
                batcher.add_signal(current_signal)
                primary_accumulator += batcher.batch_sum

print(f"Result: {primary_accumulator}")