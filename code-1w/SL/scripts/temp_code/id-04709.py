from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic evaluation
def analyze_sensor_network():
    raw_readings = [
        (101, 23.4, 'temp'), (102, 45.1, 'pressure'), (103, 23.4, 'temp'),
        (104, 18.9, 'humidity'), (105, 45.1, 'pressure'), (106, 23.4, 'temp'),
        (107, 33.2, 'flow'), (108, 18.9, 'humidity'), (109, 45.1, 'pressure')
    ]

    # Irrelevant transformation: map node ids to dummy status codes
    status_lookup = {node: (node * 3) % 7 for node, _, _ in raw_readings}
    
    # Decoy analysis: count by type (not used in final result)
    type_counter = Counter(kind for _, _, kind in raw_readings)
    pressure_count = type_counter['pressure']  # red herring

    # Distractor: complex normalization that isn't used
    normalized = []
    base_ref = sum(val for _, val, _ in raw_readings) / len(raw_readings)
    for node_id, value, kind in raw_readings:
        z_score = (value - base_ref) / (1 + value % 3)
        category = 'A' if z_score > 1 else 'B' if z_score > -1 else 'C'
        normalized.append((node_id, value, kind, round(z_score, 2), category))

    # Actual relevant filtering: extract temperature readings above threshold
    temp_readings = [(val, idx) for idx, val, typ in raw_readings if typ == 'temp']
    avg_temp = sum(v for v, _ in temp_readings) / len(temp_readings)
    filtered_data = [v for v, _ in temp_readings if v > avg_temp]

    # Dead code path: unused recursive function
    def recursive_sum(lst):
        return lst[0] + recursive_sum(lst[1:]) if lst else 0
    
    # Unused list comprehension with bit manipulation
    masked_values = [int(v) ^ 255 for v in filtered_data]  # decoy

    # Create threshold map (used later)
    threshold_map = defaultdict(float)
    threshold_map['temp'] = 23.0
    threshold_map['pressure'] = 40.0
    threshold_map['humidity'] = 20.0
    threshold_map['flow'] = 30.0

    # Another distraction: zip-based pairing with no impact
    indices = list(range(len(filtered_data)))
    shifts = [i << 1 for i in indices]
    paired_offsets = list(zip(filtered_data, shifts))  # never used

    # Real logic begins: process only filtered_data using threshold_map
    def process_readings(data, thresholds):
        excess_total = 0.0
        for value in data:
            # Only temperature threshold matters here
            if value > thresholds['temp']:
                deviation = value - thresholds['temp']
                # Apply diminishing return factor via exponentiation
                contribution = deviation ** 1.5
                excess_total += contribution
        # Final transformation
        result = int(excess_total * 100) / 100  # round to 2 decimal places
        return result

    # Key assignment point
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Multiple distractor assignments after key point
    final_diagnostic += 10.0  # misleading!
    final_diagnostic = abs(final_diagnostic - 5.0)  # another distraction
    final_diagnostic = round(final_diagnostic, 2)
    
    # Reset to correct value (simulates debugging artifact)
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print result for evaluation
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()