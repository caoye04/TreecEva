from collections import defaultdict, Counter
import math

# Simulated sensor network diagnostic system
def collect_diagnostics():
    raw_readings = [
        (101, 45.6, 'TEMP'), (102, 30.2, 'PRESS'), (103, 45.6, 'TEMP'),
        (104, 128, 'VIBR'), (105, 75.8, 'TEMP'), (106, 30.2, 'PRESS'),
        (107, 204, 'VIBR'), (108, 45.6, 'TEMP'), (109, 128, 'VIBR')
    ]

    # Irrelevant transformation - distractor
    encoded_logs = []
    for rid, val, typ in raw_readings:
        encoded_logs.append(f'{rid:x}-{val:.1f}-{typ[::-1]}')

    # Decoy analysis path - never used
    def analyze_trend(data, mode='basic'):
        return sum(v for _, v, _ in data) / len(data)

    trend_proxy = analyze_trend(raw_readings)  # Red herring

    # Real processing begins: filter valid TEMP and VIBR readings above baseline
    temp_data = [(rid, val) for rid, val, typ in raw_readings if typ == 'TEMP' and val > 40.0]
    vibr_data = [(rid, val) for rid, val, typ in raw_readings if typ == 'VIBR' and val > 100]

    # Combine relevant readings
    filtered_data = temp_data + vibr_data

    # Build threshold map with multiple unused entries - distraction
    threshold_map = defaultdict(lambda: float('inf'))
    threshold_map['TEMP'] = 44.0
    threshold_map['PRESS'] = 28.5
    threshold_map['VIBR'] = 110.0
    threshold_map['HUM'] = 60.0
    threshold_map['FLOW'] = 200.0

    # Distractor: unused counters
    type_counter = Counter(typ for _, _, typ in raw_readings)
    spike_count = sum(1 for _, v, _ in raw_readings if v > 100)

    # Destructuring with irrelevant variables
    avg_temp = sum(val for _, val in temp_data) / len(temp_data)
    max_vibr = max(val for _, val in vibr_data)
    median_vibr = sorted(v for _, v in vibr_data)[len(vibr_data)//2]

    # Dead code path - misleading function
    def calibrate_sensor(reading):
        if reading < 50:
            return reading * 1.1
        else:
            return reading * 0.9  # Never actually applied

    # Key processing function
    def process_readings(data, thresholds):
        diagnostics = []
        temp_ids = set()
        vibr_levels = []

        for sensor_id, value in data:
            hex_id = hex(sensor_id)[2:]
            first_digit = int(hex_id[0], 16)
            
            # Conditional logic with short-circuiting red herring
            if first_digit % 2 == 0 and (value * 2) > 1000:  # Always false
                continue

            if sensor_id < 105:
                category = 'PRIMARY'
            else:
                category = 'SECONDARY'

            # Real logic branch
            if 'TEMP' in [t for _, _, t in raw_readings if t == 'TEMP']:
                adjusted = value - 40.0
                normalized = math.log(adjusted) if adjusted > 0 else 0
                diagnostics.append(normalized * 10)

            # Accumulate only TEMP IDs for later use
            if sensor_id in [r[0] for r in temp_data]:
                temp_ids.add(sensor_id % 10)

            # Vibrations contribute to a separate metric
            if sensor_id in [r[0] for r in vibr_data]:
                vibr_levels.append(value // 10)

        # Complex aggregation with decoy operations
        base_score = sum(diagnostics)
        id_entropy = sum(i * i for i in temp_ids)
        vibr_metric = sum(set(vibr_levels))  # Remove duplicates then sum

        # Final computation - only this matters
        final_diagnostic = int(base_score + id_entropy - vibr_metric)

        # Unused transformations - distractions
        binary_rep = ''.join(format(ord(c), 'b') for c in f'SCORE:{final_diagnostic}')
        checksum = sum(int(b) for b in binary_rep[:32]) ^ 0xAA

        return final_diagnostic

    # Execution point of interest
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Irrelevant cleanup
    del threshold_map['HUM'], threshold_map['FLOW']

    return final_diagnostic

# Run simulation
collect_diagnostics()