import itertools

# Simulate a complex embedded diagnostics system with multiple interference layers
def main():
    # Core state variables
    sensor_readings = [0.87, 0.92, 0.85, 0.78, 0.96, 0.88, 0.73]
    calibration_offset = 0.05
    timing_log = {i: val * (i + 1) for i, val in enumerate(sensor_readings)}
    
    # Irrelevant preprocessing path - red herring
    processed_data = []
    for x in sensor_readings:
        temp_val = x ** 2 + calibration_offset
        if temp_val > 0.8:
            processed_data.append(temp_val * 1.1)
    
    # Decoy function - looks important but unused
    def analyze_pattern(seq):
        return sum(x * i for i, x in enumerate(seq)) % 100
    
    # Unused data structure - distraction
    historical_stats = {
        'peak': max(sensor_readings),
        'trough': min(sensor_readings),
        'variance': (sum((x - sum(sensor_readings)/len(sensor_readings))**2 for x in sensor_readings) / len(sensor_readings)),
        'flags': [i for i, x in enumerate(sensor_readings) if x < 0.8]
    }

    # Real processing begins - deeply nested logic
    system_state = {}
    for i in range(len(sensor_readings)):
        if i % 2 == 0:
            state_code = 1
            if sensor_readings[i] > 0.85:
                state_code += 2
            if i in timing_log and timing_log[i] > 1.0:
                state_code += 4
        else:
            state_code = 0
            if sensor_readings[i] < 0.8:
                state_code = -1
        system_state[f'node_{i}'] = state_code

    # Complex aggregation with slicing and dictionary ops
    active_nodes = [k for k, v in system_state.items() if v > 0]
    node_indices = [int(k.split('_')[1]) for k in active_nodes]
    filtered_readings = sensor_readings[:max(node_indices) + 1] if node_indices else []

    # Misleading intermediate calculation
    phantom_score = sum(itertools.chain(
        [filtered_readings[i] * (i+1) for i in range(0, len(filtered_readings), 2)],
        [0.1 * i for i in range(len(filtered_readings))]
    )) // 1

    # Critical diagnostic function
    def aggregate_metrics(log, states):
        base_sum = sum(log[k] for k in log if k < 5)
        state_bonus = sum(v for v in states.values() if v > 0)
        penalty = 0
        
        # Nested conditional logic with bit manipulation red herring
        for i, reading in enumerate(sensor_readings):
            if reading < 0.8 and i in log:
                penalty += 2
                # Bitwise decoy - looks sophisticated but unused
                mask = (penalty << 2) ^ 0x0F
            
        # Real contribution: combination of arithmetic and counting
        count_high = len([r for r in filtered_readings if r > 0.85])
        return int(base_sum * 10) + state_bonus * 3 - penalty + count_high

    # Unused alternative method - dead code path
    def legacy_aggregate(log_dict):
        values = list(log_dict.values())
        return sum(values[i] for i in range(0, len(values), 3))

    # Execution point of interest
    final_diagnostic = aggregate_metrics(timing_log, system_state)

    # Distractor: additional unrelated computation
    summary_hash = 0
    for char in 'diagnostics_active':
        summary_hash += ord(char) % 7

    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()