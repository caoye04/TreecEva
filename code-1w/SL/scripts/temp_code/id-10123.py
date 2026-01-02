def sensor_network_analysis():
    raw_readings = [145, 273, 98, 412, 68, 305, 221, 176, 89, 314]
    calibration_offset = 17
    baseline_correction = sum([r % 13 for r in raw_readings[:5]])
    adjusted_readings = [r + calibration_offset for r in raw_readings]

    # Irrelevant processing: dead path based on impossible condition
    legacy_mode = False
    if len(adjusted_readings) > 20 and not legacy_mode:
        adjusted_readings = [r * 2 for r in adjusted_readings]

    outlier_threshold = 350
    valid_range = (50, 400)
    
    # Filtering logic with distractor variables
    high_alerts = []
    medium_flags = []
    temp_snapshot = {i: val for i, val in enumerate(adjusted_readings) if val > 300}
    debug_stats = {
        'peak': max(adjusted_readings),
        'truncated_sum': sum(adjusted_readings[::3]),
        'ignored_average': sum(temp_snapshot.values()) / len(temp_snapshot) if temp_snapshot else 0
    }

    # Real filtering used later
    filtered_data = [val for val in adjusted_readings if valid_range[0] <= val <= valid_range[1]]

    # Decoy statistical computation (unused)
    entropy_approx = 0.0
    for x in raw_readings:
        if x > 0:
            entropy_approx += x * math.log(x, 2)

    # Set operations (required feature)
    critical_set = {145, 273, 412, 305}
    threshold_set = {x for x in filtered_data if x > outlier_threshold}
    auxiliary_set = {x + 10 for x in critical_set}
    unused_intersection = critical_set & auxiliary_set

    # Conditional expression (required feature)
    mode_flag = 'aggressive' if len(threshold_set) > 2 else 'conservative'

    # Simulated processing function
    def process_readings(data, thresholds):
        base_score = sum(data)
        penalty = 0
        
        # Nested conditional logic with early returns
        if not data:
            return -1
        
        for d in data:
            if d in thresholds:
                if d % 2 == 0:
                    penalty += 5
                else:
                    penalty += 3
            elif d < 100:
                penalty += 1

        adjustment_factor = 0.9 if 'aggressive' in {mode_flag} else 1.1
        intermediate = base_score - penalty
        
        # Multiple abstraction layers
        def apply_decay(val, steps=2):
            for _ in range(steps):
                val = int(val ** 0.5) * 5
            return val
        
        if intermediate > 1000:
            intermediate = apply_decay(intermediate)

        return intermediate + len(thresholds) * 7

    # Unused recursive red herring
    def recursive_weight(n):
        if n <= 1:
            return 1
        return n + recursive_weight(n // 2)
    
    dummy_weight = recursive_weight(10)  # Dead-end computation

    # Key execution point
    final_diagnostic = process_readings(filtered_data, threshold_set)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

# Required import
import math
sensor_network_analysis()