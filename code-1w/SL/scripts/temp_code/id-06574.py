from itertools import permutations, cycle
import math

# Simulated sensor data processing with red herrings
def collect_readings():
    raw = [12, 7, 3, 19, 41, 2, 8]
    processed = []
    for val in raw:
        if val % 2 == 0:
            processed.append(val ** 2)
        else:
            processed.append(val + 1)
    return processed

# Irrelevant transformation: scrambles order but unused
def scramble(data):
    return [data[i] for i in range(len(data)-1, -1, -1)]

# Fake filter that looks important but isn't used
def noise_filter(arr):
    threshold = sum(arr) / len(arr)
    return [x for x in arr if x > threshold]

# Real computation path begins here
def compute_base_energy(readings):
    total = 0
    multiplier = 1
    for i, r in enumerate(readings):
        if i % 2 == 0:
            total += r * (multiplier + i)
        else:
            total -= r // (multiplier + 1)
    return total

# Distractor function: appears in call chain but not in actual logic
def adjust_for_timezone(timestamps, zone_offset=3):
    adjusted = []
    for t in timestamps:
        adjusted.append((t + zone_offset) % 24)
    return adjusted

# Unused recursive decoy
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Critical intermediate step disguised among noise
def extract_features(data_stream):
    feature_set = []
    cycler = cycle([1, -1])
    for d in data_stream:
        sign = next(cycler)
        feature_set.append(d * sign)
    return feature_set

# Another red herring: processes strings but irrelevant to final answer
def analyze_labels(tags):
    char_count = {}
    for tag in tags:
        for c in tag.lower():
            char_count[c] = char_count.get(c, 0) + 1
    return sorted(char_count.values(), reverse=True)[0] if char_count else 0

# Core calculation
summation = 0
def finalize(base, offset):
    global summation
    temp = base * 3
    temp -= offset ** 2
    temp += int(math.log(temp + 100, 2))
    summation = temp  # critical assignment point
    return temp

# Dead code path — never invoked
def deprecated_path():
    readings = collect_readings()
    readings = scramble(readings)
    readings = noise_filter(readings)
    return sum(readings)

# Main execution with distractions
if __name__ == '__main__':
    # Initialize with real data
    sensor_data = collect_readings()  # [144, 8, 9, 20, 1681, 4, 64]

    # Irrelevant string analysis
    labels = ['alpha', 'beta', 'gamma', 'delta']
    peak_frequency = analyze_labels(labels)

    # Fake timestamp adjustment
    timestamps = [10, 14, 18, 22]
    adjusted_times = adjust_for_timezone(timestamps)

    # Extract features using signed alternation
    signal = extract_features(sensor_data)

    # Compute base energy from alternating signal
    energy = compute_base_energy(signal)

    # Offset derived from unused fibonacci branch
    offset = fibonacci(7)  # 13, computed but distractor in context

    # ACTUAL KEY STATEMENT
    checksum = finalize(energy, offset)

    # Print result as required
    print(f"Result: {checksum}")