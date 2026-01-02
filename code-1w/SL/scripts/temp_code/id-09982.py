def sensor_network_analysis():
    # Simulated environmental sensor readings (temperature in Celsius)
    raw_readings = [23.5, 19.1, 24.3, 27.8, 30.2, 26.4, 22.7, 18.9, 25.1, 28.6]

    # Irrelevant auxiliary data (distractor: humidity levels not used in final logic)
    humidity_levels = [45, 50, 52, 60, 65, 58, 54, 48, 56, 62]
    elevation_map = {'sector_a': 120, 'sector_b': 180, 'sector_c': 95}
    calibration_offsets = [-0.3, 0.1, -0.2, 0.4, 0.0]

    # Initial preprocessing with distractor transformation
    adjusted_readings = [round(r + 0.1, 1) for r in raw_readings]  # Minor adjustment, some irrelevant

    # Decoy function – looks important but unused in critical path
    def analyze_trend(data):
        return sum(1 for i in range(1, len(data)) if data[i] > data[i-1])

    trend_score = analyze_trend(raw_readings)  # Dead-end computation

    # Key filtering operation (relevant)
    baseline_ref = 25.0
    high_temp_indices = [i for i, val in enumerate(adjusted_readings) if val >= baseline_ref]

    # Extracting filtered data based on threshold (key relevant data)
    filtered_data = [raw_readings[i] for i in high_temp_indices]

    # Red herring: complex bit manipulation on unrelated metric
    checksum = 0
    for val in humidity_levels:
        checksum ^= int(val * 1.5) & 0xFF
    checksum = (checksum << 2) | (checksum >> 6)  # Obfuscation, not used later

    # Decoy data structure transformation
    paired_readings = list(zip(raw_readings, adjusted_readings))
    deviation_pairs = [(a, b, abs(a - b)) for a, b in paired_readings]

    # Higher-order function definition – appears significant
    apply_correction = lambda f, offset: [f(x, offset) for x in filtered_data]
    dummy_correction = apply_correction(lambda x, c: x + c, -0.5)  # Unused result

    # Critical threshold logic (core reasoning path)
    def generate_threshold(bias=1.2):
        avg = sum(filtered_data) / len(filtered_data)
        return avg * bias if avg < 28.0 else avg * 1.1

    dynamic_limit = generate_threshold()  # Intermediate calculation

    # Core decision function (used in final call)
    threshold_func = lambda x: x > dynamic_limit

    # Real processing function with nested logic and comprehension
    def process_readings(data, predicate):
        if not data:
            return 0.0
        
        # Transform via enumeration and filtering
        indexed_scores = []
        for idx, temp in enumerate(data):
            score = 0
            if temp > 26.0:
                score += 3
            if idx % 2 == 1:
                score += 1
            if predicate(temp):
                score += 5
            indexed_scores.append(score * 1.5)
        
        # Final aggregation using comprehension
        weighted_sum = sum([s ** 0.5 for s in indexed_scores if s > 3.0])
        count = len([s for s in indexed_scores if s >= 4.5])
        
        return round(weighted_sum / (count + 1), 6) if count > 0 else sum(indexed_scores)

    # Additional distraction: recursive countdown (no side effects)
    def purge_buffer(n):
        if n <= 0:
            return 'cleared'
        return purge_buffer(n - 1)
    
    purge_buffer(3)  # No impact on state

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_func)

    # Output requirement
    print(f"Result: {final_diagnostic}")

sensor_network_analysis()