from itertools import combinations

def analyze_bandwidth(segments):
    total_load = 0
    peak_moment = 0
    temp_buffer = []

    for segment in segments:
        raw_data = segment['data'] * segment['redundancy_factor']
        transmission_delay = raw_data / segment['bandwidth']
        if transmission_delay > peak_moment:
            peak_moment = transmission_delay
        total_load += raw_data
        temp_buffer.append(transmission_delay)

    avg_delay = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    return total_load, avg_delay, peak_moment

def validate_segment_integrity(segments):
    errors = 0
    for s in segments:
        checksum = str(s['data']) + str(s['bandwidth'])
        if '9' in checksum:
            errors += 1
    return errors == 0

def calculate_utilization(segments):
    capacity = 0
    efficiency_log = []
    dummy_counter = 0

    for i, pair in enumerate(combinations(segments, 2)):
        seg1, seg2 = pair
        link_strength = (seg1['bandwidth'] + seg2['bandwidth']) / 2
        load_ratio = abs(seg1['data'] - seg2['data']) / max(seg1['data'], seg2['data'], 1)
        if link_strength > 50 and load_ratio < 0.8:
            capacity += int(link_strength * (1 - load_ratio))
            efficiency_log.append(link_strength * (1 - load_ratio))
        dummy_counter += 1  

    if len(efficiency_log) > 3:
        smoothed = sum(efficiency_log[-3:]) / 3
        capacity -= int(smoothed / 4)

    redundant_check = [s['redundancy_factor'] for s in segments if s['redundancy_factor'] > 1]
    if redundant_check:
        capacity += len(redundant_check) * 5

    return capacity

# System configuration
network_segments = [
    {'data': 120, 'bandwidth': 80, 'redundancy_factor': 2},
    {'data': 90, 'bandwidth': 60, 'redundancy_factor': 1},
    {'data': 150, 'bandwidth': 100, 'redundancy_factor': 3},
    {'data': 60, 'bandwidth': 40, 'redundancy_factor': 1},
    {'data': 200, 'bandwidth': 120, 'redundancy_factor': 2}
]

# Preliminary analysis (distraction)
total_load, avg_delay, peak = analyze_bandwidth(network_segments)
integrity = validate_segment_integrity(network_segments)

# Core computation with interference
dummy_list = [x for x in range(len(network_segments) * 3)]
useless_sum = sum([len(str(x)) for x in dummy_list if x % 7 == 0])
efficiency_flags = {i: False for i in range(10)}

for idx, seg in enumerate(network_segments):
    if seg['data'] > 100:
        efficiency_flags[idx] = True

# Critical assignment
final_capacity = calculate_utilization(network_segments)

print(f"Result: {final_capacity}")