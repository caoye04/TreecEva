from collections import defaultdict, Counter
import math

# Simulate sensor data aggregation from distributed nodes
def collect_sensor_readings():
    raw_streams = [
        [3, 5, 7, 11, 13, 17],
        [2, 4, 8, 16, 32],
        [1, 1, 2, 3, 5, 8, 13, 21],
        [10, 20, 30, 40],
        [1, 4, 9, 16, 25]
    ]
    
    aggregated = []
    for stream in raw_streams:
        processed = []
        for val in stream:
            if val % 2 == 0:
                processed.append(val * 1.5)
            else:
                processed.append(val * 0.8)
        aggregated.extend(processed)
    
    # Irrelevant transformation (dead path)
    temp_result = [x ** 0.5 for x in aggregated if x > 10]
    
    return aggregated

# Misleading auxiliary function (decoy)
def compute_thermal_index(data):
    total = 0
    for x in data:
        if x > 25:
            total += int(math.log(x) * 2)
    return total * 1.7

# Auxiliary state tracker (partially relevant)
class StateTracker:
    def __init__(self):
        self.history = []
        self.counter = defaultdict(int)
    
    def update(self, values):
        for v in values:
            self.counter[int(v // 5)] += 1
        self.history.append(sum(self.counter.values()))

# Heavily distractor-laden analysis core
def analyze_pattern(data, thresholds):
    tracker = StateTracker()
    
    # Distractor: irrelevant frequency analysis
    freq = Counter(data)
    dominant = max(freq, key=freq.get)
    
    # Real processing begins: filter and transform
    filtered = [x for x in data if x > 5]
    transformed = []
    
    for x in filtered:
        if x in thresholds['critical']:
            transformed.append(x * 1.1)
        elif x in thresholds['elevated']:
            transformed.append(x * 0.9)
        else:
            transformed.append(x)
    
    # Nested conditional with misleading intermediate
    adjustment_factor = 1.0
    if len(transformed) > 10:
        avg = sum(transformed) / len(transformed)
        if avg > 15:
            adjustment_factor = 0.95
            # Dead computation branch
            outlier_count = 0
            for t in transformed:
                if abs(t - avg) > 2 * avg ** 0.5:
                    outlier_count += 1
            synthetic_metric = outlier_count * avg / 3.7  # unused
    
    # Key logic hidden among distractions
    base_sum = sum(transformed)
    penalty = 0
    for k, count in tracker.counter.items():
        if k > 3:
            penalty += count * 2
    
    # Actual result formation
    diagnostic_score = int((base_sum - penalty) * adjustment_factor)
    
    # Multiple red herring variables
    normalized_score = diagnostic_score / 100.0
    reliability_index = len([x for x in data if x < 3])
    stability_ratio = math.sin(len(filtered) * 0.1)  # unused
    
    return diagnostic_score

# Misleading setup section
baseline_modes = {'A': 1, 'B': 2, 'C': 4}
reference_grid = set(baseline_modes.values())
reference_grid.add(8)
reference_grid.update([16, 32])  # Unused in logic

# Threshold map actually used in decision
threshold_map = {
    'critical': {16.5, 24.0, 33.0, 48.0},
    'elevated': {9.0, 12.0, 18.0}
}

# Data collection with side effects
collected_data = collect_sensor_readings()

# Tracker used but with obscured relevance
tracker_main = StateTracker()
tracker_main.update(collected_data)

# Decoy function call (no impact on result)
dummy_index = compute_thermal_index(collected_data)

# Critical execution point
final_diagnostic = analyze_pattern(collected_data, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")