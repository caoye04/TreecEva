import math
from contextlib import contextmanager

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

@contextmanager
def temperature_monitor():
    state = 'NORMAL'
    yield state
    print("Temperature monitoring session ended.")

# Simulated temperature deviation data (in Celsius)
temperature_readings = [0.3, 1.2, 2.5, -0.5, 3.1, 1.8, 0.9, 2.2, -1.0, 4.5, 0.7, 3.3, 2.8]

# State machine classifications
classifications = []
threshold = 2.0

with temperature_monitor() as current_state:
    for reading in temperature_readings:
        if current_state == 'NORMAL' and reading >= threshold:
            current_state = 'WARNING'
            classifications.append('WARMING')
        elif current_state == 'WARNING' and reading < threshold:
            current_state = 'NORMAL'
            classifications.append('COOLING')
        else:
            classifications.append('STABLE')

# Greedy detection of significant warming events
significant_events = []
i = 0
while i < len(classifications):
    if classifications[i] == 'WARMING':
        magnitude = 0
        start_i = i
        # Continue while temperatures are high
        while i < len(temperature_readings) and temperature_readings[i] >= threshold:
            magnitude += temperature_readings[i]
            i += 1
        # Only count if duration is prime number of readings
        duration = i - start_i
        if is_prime(duration):
            significant_events.append(magnitude)
    else:
        i += 1

# Divide and conquer function to calculate mean
def calculate_mean(values, start, end):
    if start == end:
        return values[start]
    if start + 1 == end:
        return (values[start] + values[end]) / 2
    mid = (start + end) // 2
    left_mean = calculate_mean(values, start, mid)
    right_mean = calculate_mean(values, mid+1, end)
    left_count = mid - start + 1
    right_count = end - mid
    return (left_mean * left_count + right_mean * right_count) / (left_count + right_count)

# Calculate average using divide and conquer if we have significant events
if significant_events:
    significant_warming_average = calculate_mean(significant_events, 0, len(significant_events)-1)
else:
    significant_warming_average = 0

print(f"Result: {significant_warming_average}")