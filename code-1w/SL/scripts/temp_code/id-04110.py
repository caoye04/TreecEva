from collections import defaultdict
import math

def analyze_events(event_list, sensitivity):
    event_count = defaultdict(int)
    transient_buffer = []
    total_magnitude = 0.0
    noise_floor = 0.1 * sensitivity

    for event in event_list:
        magnitude = event['value'] ** 2
        category = event['type']
        event_count[category] += 1
        total_magnitude += magnitude

        if magnitude > noise_floor:
            transient_buffer.append(magnitude * 0.9)

    filtered_energy = sum([x for x in transient_buffer if x > noise_floor])
    return total_magnitude, event_count, filtered_energy

def calculate_stability_index(readings):
    if len(readings) < 2:
        return 0.0
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return round(math.sqrt(variance), 4)

def evaluate_performance(log_data, threshold):
    base_score = 0
    penalty_pool = 0
    debug_trace = []
    temp_accumulator = 0

    stability_readings = [entry['signal'] for entry in log_data if 'signal' in entry]
    stability_index = calculate_stability_index(stability_readings)

    high_priority_events = [e for e in log_data if e.get('priority') == 'high']
    normal_events = [e for e in log_data if e.get('priority') == 'normal']

    # Irrelevant computation - simulates diagnostic trace
    for i, event in enumerate(high_priority_events):
        cycle_marker = (i + 1) * 0.01
        temp_accumulator += math.sin(cycle_marker)
        debug_trace.append(f"Cycle {i}: {cycle_marker:.3f}")

    # Core logic begins
    total_high_events = len(high_priority_events)
    total_normal_events = len(normal_events)

    base_score += total_high_events * 7
    base_score += total_normal_events * 2

    if stability_index < threshold:
        base_score += 15
    else:
        penalty_pool += 8

    # Secondary analysis with distractor variables
    energy_snapshot = 0
    dummy_factor = 0
    for entry in log_data:
        if 'energy' in entry:
            adjusted_energy = entry['energy'] * 0.85
            energy_snapshot += adjusted_energy
            dummy_factor += abs(adjusted_energy - 10)  # unused beyond here

    # Decision point with early break
    for level in [1, 2, 3]:
        if energy_snapshot > 50 * level:
            base_score += 3
        else:
            break

    # Bitwise integrity check (semi-relevant)
    integrity_key = 0b1010
    flag_mask = 0b1100
    if (total_high_events & integrity_key) == 2:
        base_score += 5

    final_score = base_score - penalty_pool
    return final_score

# Simulated input data
base_threshold = 4.5
data_log = [
    {'value': 3.2, 'type': 'sensor', 'priority': 'high', 'signal': 12},
    {'value': 1.1, 'type': 'status', 'priority': 'normal', 'signal': 14},
    {'value': 4.0, 'type': 'sensor', 'priority': 'high', 'signal': 13},
    {'value': 0.9, 'type': 'status', 'priority': 'normal', 'energy': 20},
    {'value': 2.8, 'type': 'sensor', 'priority': 'high', 'signal': 11},
    {'value': 1.5, 'type': 'diagnostic', 'priority': 'normal', 'energy': 15}
]

# Execution point
final_score = evaluate_performance(data_log, base_threshold)
print(f"Result: {final_score}")