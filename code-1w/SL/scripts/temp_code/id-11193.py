from collections import defaultdict, Counter
import math

# Simulated sensor data from a chemical plant (irrelevant for final result but looks important)
sensor_readings = [23.4, 24.1, 22.9, 25.6, 26.0, 24.8, 23.9, 25.1]

def analyze_sensor_trends(data):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends.append('up')
        elif data[i] < data[i-1]:
            trends.append('down')
        else:
            trends.append('stable')
    return trends

# Misleading preprocessing function that isn't used in the critical path
def normalize_readings(readings):
    mean_val = sum(readings) / len(readings)
    return [(x - mean_val) / mean_val for x in readings]

# Decoy statistical analysis
mean_sensor = sum(sensor_readings) / len(sensor_readings)
variance = sum((x - mean_sensor) ** 2 for x in sensor_readings) / len(sensor_readings)
std_dev = math.sqrt(variance)

# Real data pipeline starts here — batch reaction parameters
raw_batches = [
    {'id': 'B001', 'temp': 180, 'pressure': 22, 'catalyst': 'X1', 'duration': 45},
    {'id': 'B002', 'temp': 195, 'pressure': 25, 'catalyst': 'X2', 'duration': 50},
    {'id': 'B003', 'temp': 175, 'pressure': 20, 'catalyst': 'X1', 'duration': 40},
    {'id': 'B004', 'temp': 200, 'pressure': 27, 'catalyst': 'X3', 'duration': 55},
    {'id': 'B005', 'temp': 185, 'pressure': 23, 'catalyst': 'X2', 'duration': 48}
]

# Unused transformation — red herring
def augment_batch_data(batches):
    enhanced = []
    for b in batches:
        b_copy = b.copy()
        b_copy['efficiency_score'] = (b['temp'] * b['pressure']) / (b['duration'] + 10)
        enhanced.append(b_copy)
    return enhanced

# Data filtering based on hidden rules (only some conditions matter)
filtered_batches = []
for batch in raw_batches:
    if batch['temp'] >= 180 and batch['pressure'] >= 22:
        filtered_batches.append(batch)

# Extract durations for secondary analysis (distraction)
durations = [b['duration'] for b in filtered_batches]

# Primary processing: extract duration slices and apply transformations
slice_start = 1
slice_end = None
sliced_durations = durations[slice_start:slice_end]  # effectively [50, 48] from B002 and B005

# Simulate intermediate yield estimation (partially relevant)
base_yields = []
for dur in sliced_durations:
    if dur > 45:
        base_yields.append(dur * 1.8)
    else:
        base_yields.append(dur * 1.5)

# Hidden rule: only even-indexed base yields in sorted order contribute
sorted_yields = sorted(base_yields)
even_indexed_yields = [sorted_yields[i] for i in range(len(sorted_yields)) if i % 2 == 0]

# Catalyst grouping (looks important, but only one group is used later)
catalyst_map = defaultdict(list)
for batch in raw_batches:
    catalyst_map[batch['catalyst']].append(batch['duration'])

count_per_catalyst = Counter([b['catalyst'] for b in raw_batches])

# Dummy aggregation
aggregated_stats = {}
for cat, times in catalyst_map.items():
    aggregated_stats[cat] = {
        'avg': sum(times) / len(times),
        'total': sum(times)
    }

# Critical function — depends only on even_indexed_yields and a fixed offset
def calculate_optimal_yield(yield_list):
    total_input = sum(yield_list)
    adjustment_factor = 0.9
    penalty = len(yield_list) * 5.5
    return (total_input * adjustment_factor) - penalty

# Additional distraction: unused recursive function
def recursive_efficiency(n):
    if n <= 1:
        return 1
    return n * 0.95 + recursive_efficiency(n - 1)

# More decoy variables
project_phase = 'validation'
last_audit = '2023-11-05'
compliance_status = True

# Processed data that feeds into the real calculation
processed_data = even_indexed_yields  # This is [90.0] because sorted(base_yields)=[90.0, 86.4], even index=0

# Key assignment statement
final_yield = calculate_optimal_yield(processed_data)

print(f"Target result: {final_yield}")