def transform_signal(raw):
    # Irrelevant signal processing transformation (dead path)
    return [x * 1.05 for x in raw if x > 0]

import math

def calculate_entropy(data):
    # Distractor function: calculates entropy but not used in final result
    total = sum(data)
    entropy = 0
    for x in data:
        p = x / total if total else 0
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

# Simulated sensor readings over time
raw_readings = [12, 15, 10, 8, 23, 25, 20, 18, 30, 35, 28, 22]

# Misleading intermediate transformation (not used in final path)
cleaned_signal = transform_signal([x - 5 for x in raw_readings])

# Key data structure: stores processed diagnostic values
processed_data = []
buffer = []

# Auxiliary counters (some irrelevant)
event_count = 0
warning_level = 0
stable_period = 0

threshold = 20
hysteresis = 3

# Primary processing loop with nested logic
for reading in raw_readings:
    # Complex conditional masking (some branches are dead ends)
    if reading > threshold + hysteresis:
        status_flag = 1
        event_count += 1
        buffer.append(reading * 0.9)
        if reading % 2 == 0:
            warning_level += 2
        else:
            warning_level += 1
    elif reading < threshold - hysteresis:
        status_flag = -1
        stable_period += 1
        buffer.clear()
    else:
        status_flag = 0
        warning_level = max(0, warning_level - 1)

    # Accumulate only high-confidence anomalies
    if status_flag == 1 and reading in [23, 25, 30, 35]:  # Specific observed anomalies
        processed_data.append(reading - 17)  # Normalize base

    # Decoy accumulation (never used)
    cumulative = sum(buffer) if buffer else 0
    if cumulative > 100:
        break  # Unreachable due to small buffer size

# Secondary validation using string-based tagging (uses string method)
diagnostic_tags = []
for val in processed_data:
    tag = ''
    if val < 5:
        tag = 'LOW'
    elif val < 8:
        tag = 'MEDIUM'
    else:
        tag = 'HIGH'
    diagnostic_tags.append(tag.strip().lower() + '_alert')

def analyze_readings(readings, limit):
    # Core analysis function: computes weighted impact
    base_score = 0
    multiplier = 1
    for i, val in enumerate(readings):
        if i % 2 == 0:
            base_score += val * 1.5
        else:
            base_score += val * 0.8
        if val > 6:
            multiplier += 0.2
    return int(base_score * multiplier)

# Dead code: unused alternative algorithm
def legacy_analysis(seq):
    return sum(x**2 for x in seq) // (len(seq) or 1)

# Final computation point
final_diagnostic = analyze_readings(processed_data, threshold)

# Output requirement
print(f"Result: {final_diagnostic}")