import math

def analyze_pattern(sequence):
    if not sequence:
        return 0
    squared_total = sum(x ** 2 for x in sequence if x > 0)
    shifted = squared_total >> 2
    return shifted + len(sequence)

# Irrelevant helper function (decoy)
def compute_entropy(data):
    total = 0
    for d in data:
        if d > 0:
            total -= d * math.log(d + 1e-9)
    return round(total, 4)

# Unused but plausible transformation
def mirror_sequence(arr):
    return arr + arr[::-1]

# Core logic disguised among distractors
def filter_critical_events(events, threshold=5):
    result = []
    temp_accum = 0
    for e in events:
        temp_accum += e % 7
        if e % 5 == 0 and temp_accum > threshold:
            result.append(e * 2)
            temp_accum = 0
    # Dead code path (never reached due to logic above)
    if temp_accum < 0:
        result.extend([0] * temp_accum)  
    return result

# Another red herring: string processing with no impact
def extract_codes(tag_string):
    parts = tag_string.split('-')
    codes = [p for p in parts if p.isdigit()]
    return [int(c) for c in codes if c.startswith('1')]

class PerformanceTracker:
    def __init__(self):
        self.buffer = []
        self.max_window = 8

    def update(self, val):
        self.buffer.append(val ^ 3)
        if len(self.buffer) > self.max_window:
            self.buffer.pop(0)

    def get_stability(self):
        if len(self.buffer) < 2:
            return 0.0
        diffs = [abs(self.buffer[i] - self.buffer[i-1]) for i in range(1, len(self.buffer))]
        return round(sum(diffs) / len(diffs), 3)

# Main computation buried in noise
debug_flags = [True, False, True]
config_mask = 0b101010

# Simulated sensor readings (some relevant, some not)
sensor_readings = [4, 6, 10, 15, 25, 30, 45, 50, 75, 100]

# Distractor list comprehension with no downstream use
unused_analysis = [math.sqrt(x) for x in sensor_readings if x % 10 == 0 and x > 20]

# Actual input data
logged_events = [3, 5, 6, 10, 12, 15, 18, 20, 21, 25, 27, 30]

# Decoy data structure
auxiliary_map = {i: logged_events[i] ** 2 for i in range(len(logged_events)) if i % 3 == 0}

# Linear search for a condition that's never used
found_index = -1
for idx, val in enumerate(logged_events):
    if val == 99:  # unreachable
        found_index = idx
        break

# Bit manipulation side calculation (distraction)
bit_accumulator = 0
for n in logged_events[:5]:
    bit_accumulator ^= (n << 1) & 0xFF

tracker = PerformanceTracker()
for val in logged_events:
    tracker.update(val)

# Real processing chain starts here
processed = filter_critical_events(logged_events, threshold=8)

# Secondary transformation with conditional twist
transformed = []
for p in processed:
    if p > 20:
        transformed.append(p - 5)
    else:
        transformed.append(p + 3)

# Mix in list comprehension (required python feature)
adjusted_scores = [x + analyze_pattern([x, x//2]) for x in transformed if x % 4 != 2]

# Final aggregation using multiple concepts
stability_metric = tracker.get_stability()
dynamic_offset = len(processed) * int(stability_metric)
base_sum = sum(adjusted_scores)

# Key line: this is where final_score is set
final_score = aggregate_performance(logged_events)

# Function defined late to obscure relevance
def aggregate_performance(events):
    filtered = [e for e in events if e % 3 == 0]  # divisible by 3
    enhanced = [e * 3 for e in filtered if e % 5 != 0]  # exclude multiples of 5
    bonus = len([e for e in events if e > 20 and e % 7 == 0])
    penalty = analyze_pattern([len(events), len(filtered)])
    raw_total = sum(enhanced) + (bonus ** 2) - penalty
    return raw_total + dynamic_offset

# Print required at end
print(f"Target result: {final_score}")