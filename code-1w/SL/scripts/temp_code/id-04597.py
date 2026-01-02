import math

def analyze_sensor_array(raw_readings, baseline):
    # Irrelevant preprocessing - red herring
    normalized = [x * 1.05 for x in raw_readings if x > 0]
    adjusted = [math.log(x) if x > 1 else 0 for x in normalized]

    # Distractor: complex but unused transformation chain
    transformed = list(map(lambda x: (x ** 2 + 1) / (x + 0.5), adjusted))
    derived_metrics = []
    for val in transformed:
        if val > 2.0:
            derived_metrics.append(val * 0.8)
        elif val > 1.0:
            derived_metrics.append(val * 0.9)
        else:
            continue  # early break red herring

    # Actual relevant path begins here
    scaled_readings = [x * baseline for x in raw_readings]
    abs_values = [abs(x) for x in scaled_readings]
    clipped = [min(x, 100) for x in abs_values]  # cap at 100

    # Filtering logic with string-based condition (case conversion distractor)
    mode_flag = 'AdJuSt'  # misleading case variation
    use_strict = mode_flag.lower() == 'adjust'

    if use_strict:
        filtered_data = [x for x in clipped if x > 10]
    else:
        filtered_data = [x for x in clipped if x > 5]

    # Decoy function that's defined but not used
    def deprecated_filter(arr):
        return [x for x in arr if x % 2 == 0]

    # Higher-order function for thresholding
    def threshold_builder(limit):
        return lambda x: x >= limit

    threshold_func = threshold_builder(45)

    # Core processing function nested to increase depth
    def process_readings(data, validator):
        cumulative = 0
        weights = [1.1, 0.9, 1.05, 0.95, 1.0] * (len(data)//5 + 1)
        weighted = [a * b for a, b in zip(data, weights[:len(data)])]
        
        for i, val in enumerate(weighted):
            if i % 3 == 0:
                cumulative += math.sin(val) * 10
            elif i % 3 == 1:
                cumulative -= math.cos(val) * 5
            else:
                cumulative += math.tan(val % (math.pi/3)) * 2
        
        # Final adjustment using bitwise manipulation red herring
        temp = int(abs(cumulative))
        masked = temp & 0xFFFF  # keep lower 16 bits
        shifted = (masked << 1) - (masked >> 1)
        return shifted + (cumulative - int(cumulative))  # preserve fractional part

    # Dead code path - never executed
    if baseline < 0:
        fallback = sum(clipped) / len(clipped)
        final_diagnostic = fallback * 1000
        return final_diagnostic

    final_diagnostic = process_readings(filtered_data, threshold_func)
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulate sensor input and execute
sensor_input = [12.5, -8.3, 15.7, 4.2, 23.1, 18.9, 6.4, 11.0]
baseline_factor = 3.8
result = analyze_sensor_array(sensor_input, baseline_factor)