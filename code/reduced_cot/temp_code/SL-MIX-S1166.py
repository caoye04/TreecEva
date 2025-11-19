import math
from functools import wraps

def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

class ResourceSimulator:
    def __init__(self, resource_limit):
        self.resource_limit = resource_limit
        self.allocated = 0
    
    def __enter__(self):
        self.allocated = min(self.resource_limit, 100)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.allocated = 0

@call_counter
def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

@call_counter
def lcm_of_primes_in_range(start, end):
    primes = []
    for num in range(max(2, start), end + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    if len(primes) < 2:
        return 0
    
    result_lcm = primes[0]
    for i in range(1, len(primes)):
        result_lcm = abs(result_lcm * primes[i]) // gcd_extended(result_lcm, primes[i])[0]
    return result_lcm

with ResourceSimulator(150) as rs:
    signal_base_freq = 120
    modulation_factor = 7
    prime_lcm_result = lcm_of_primes_in_range(10, 30)
    if prime_lcm_result > 1000:
        modulation_factor *= 2
    else:
        modulation_factor *= 3
    
    final_modulation_index = (signal_base_freq * modulation_factor) % rs.allocated
    if final_modulation_index < 50:
        final_modulation_index += 25
    elif final_modulation_index > 100:
        final_modulation_index -= 15
    
    # Execution point Y
    print(f"Result: {final_modulation_index}")