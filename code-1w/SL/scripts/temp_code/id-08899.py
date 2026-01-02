from collections import defaultdict, Counter

# Simulated sensor data stream (real-world context: environmental monitoring)
sensor_data = [
    {'node': 'A', 'temp': 23.5, 'humidity': 45, 'status': 'active'},
    {'node': 'B', 'temp': -19.2, 'humidity': 60, 'status': 'active'},
    {'node': 'C', 'temp': 31.8, 'humidity': 33, 'status': 'inactive'},
    {'node': 'A', 'temp': 25.1, 'humidity': 47, 'status': 'active'},
    {'node': 'B', 'temp': -18.7, 'humidity': 62, 'status': 'active'},
    {'node': 'D', 'temp': 19.3, 'humidity': 55, 'status': 'active'}
]

# Irrelevant statistical tracking (distractor)
extreme_temp_count = 0
stable_humidity_count = 0
status_log = []

# Data structures for aggregation (relevant and distractor)
temperature_readings = []
humidity_readings = []
node_activity = defaultdict(int)
health_flags = Counter()

# Processing loop with mixed relevance
for entry in sensor_data:
    temp = entry['temp']
    humidity = entry['humidity']
    node = entry['node']
    status = entry['status']

    # Relevant data collection
    temperature_readings.append(temp)
    humidity_readings.append(humidity)
    node_activity[node] += 1

    # Distractor logic: flag extremes that aren't used later
    if temp < -10 or temp > 30:
        health_flags['extreme_temp'] += 1
        extreme_temp_count += 1  # unused variable
    
    if 40 < humidity < 60:
        stable_humidity_count += 1  # dead-end counter

    # Red herring: logging inactive nodes (but all calcs use active)
    if status == 'inactive':
        status_log.append(node)

# Secondary transformation (partially irrelevant)
normalized_temps = [round(t ** 2 / 10, 1) for t in temperature_readings if t > 0]  # only positive temps
inverted_humidity = [(100 - h) ** 0.5 for h in humidity_readings]  # not used

# Decoy function: looks important but unused
def calculate_stability_index(readings):
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    return round(variance, 2)

# Conditional expression with misleading branch (only one arm matters)
baseline_offset = 5 if len(node_activity) > 3 else -10  # depends on number of nodes

# Core calculation setup (key path)
valid_readings = [t for t in temperature_readings if t >= -20 and t <= 40]  # filter valid range
adjusted_avg_temp = sum(valid_readings) / len(valid_readings)

# Bit manipulation red herring (unrelated to final result)
bitmask = 0
for i, t in enumerate(valid_readings):
    bitmask ^= int(t) & 7  # XOR with low bits

# Another decoy: complex sorting with no downstream use
sorted_pairs = sorted(zip(temperature_readings, humidity_readings), key=lambda x: (x[0] > 0, -x[1]))
ranked_nodes = sorted(node_activity.items(), key=lambda x: x[1], reverse=True)

# Control flow distraction: short-circuit evaluation pattern
system_ready = len(status_log) == 0 and (node_activity.get('A', 0) > 0 or node_activity.get('B', 0) > 0)

# Real computation begins: health score based on average temperature deviation
ideal_temp = 22.0
temp_deviation = abs(adjusted_avg_temp - ideal_temp)
aggregate_health_score = 100 - (temp_deviation * 5)

# Correction factors with conditional expression (relevant)
correction_factor = 1.2 if len(set(entry['node'] for entry in sensor_data)) >= 3 else 0.8
system_bias = -8

# Key statement: combines relevant variables amid noise
final_diagnostic = aggregate_health_score + system_bias * correction_factor

# Final distractor: unrelated combinatorics
possible_node_pairs = 0
nodes = list(node_activity.keys())
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        possible_node_pairs += 1  # computed but unused

print(f"Result: {final_diagnostic}")