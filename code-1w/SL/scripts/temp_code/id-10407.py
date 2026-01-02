def analyze_sensor(stream, config):
    # Irrelevant preprocessing step (dead code path)
    normalized = [x * 1.05 for x in stream if x > 0]
    adjusted = []
    for val in normalized:
        if val > config.get('noise_floor', 10):
            adjusted.append(val - 2.5)

    # Distractor: complex but unused transformation
    transformed = list(map(lambda x: (x ** 0.5) * 1.75, [v for v in stream if v % 2 == 0]))
    stats = {"mean": sum(stream) / len(stream), "peak": max(stream)}

    # Actual relevant filtering
    filtered_data = [x for x in stream if 15 <= x <= 85]

    # Bitwise masking for sensor error flags (irrelevant to final result)
    error_flags = 0
    for val in stream:
        if val < 5:
            error_flags |= 1 << 1
        elif val > 95:
            error_flags |= 1 << 2

    # Decoy dictionary with misleading diagnostics
    decoy_diagnostics = {
        "status": "unstable",
        "readings_analyzed": len(transformed),
        "risk_level": "high" if error_flags else "low"
    }

    # Real logic begins: threshold mapping using config
    base_threshold = config.get('base_threshold', 40)
    threshold_map = {}
    for i, val in enumerate(filtered_data):
        key = f"sensor_{i % 4}"
        if val > base_threshold:
            threshold_map[key] = threshold_map.get(key, 0) + (val // 5)

    # Another red herring: unused recursive function
    def recurse_check(n):
        if n <= 1:
            return 1
        return recurse_check(n - 2) + (n % 3)

    dummy_calc = recurse_check(7)  # Computation has no effect

    # Conditional branch that looks important but is bypassed
    if config.get("enable_enhanced", False):
        processed = [x * 1.1 for x in filtered_data]
        final_value = sum(processed) / len(processed)
        return int(final_value)

    # Core processing function (depends only on filtered_data and threshold_map)
    def process_readings(data, thresholds):
        accumulation = 0
        for idx, reading in enumerate(data):
            shift = thresholds.get(f"sensor_{idx % 4}", 1)
            # Use bitwise XOR and integer division to obscure logic
            encoded = (reading ^ idx) // 3
n            accumulation += encoded * (shift % 4)
        return accumulation + len(thresholds)

    final_diagnostic = process_readings(filtered_data, threshold_map)
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution entry point
sensor_stream = [20, 30, 5, 80, 70, 90, 25, 60, 85, 10, 40, 75]
settings = {
    "noise_floor": 8,
    "base_threshold": 35,
    "enable_enhanced": False
}
analyze_sensor(sensor_stream, settings)