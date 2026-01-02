def simulate_agricultural_cycle():
    # Environmental constants
    base_rainfall = 85.0
    temperature_bias = -2.3
    soil_nutrients = 142

    # Crop parameters
    crop_coefficients = [0.78, 0.91, 1.05, 0.88, 1.12]
    growth_stages = ['seed', 'sprout', 'mature', 'flower', 'fruit']

    # Simulate daily micro-variations in environment (mostly irrelevant)
    daily_fluctuations = []
    temp_accumulator = 0
    for i in range(5):
        adjustment = (base_rainfall * (crop_coefficients[i] + i * 0.1)) % 7
        temp_accumulator += adjustment
        daily_fluctuations.append(temp_accumulator)

    # Distractor: unused function
    def analyze_soil_ph(level):
        return lambda x: x * 0.92 if level > 7 else x * 1.08

    # Real processing begins here
    stage_data = {}
    for idx, stage in enumerate(growth_stages):
        # Core transformation logic
        metric = (soil_nutrients * crop_coefficients[idx]) + (base_rainfall * (idx + 1))
        if temperature_bias < 0:
            metric *= 0.94
        stage_data[stage] = round(metric, 3)

    # Intermediate filtering using lambda (relevant)
    valid_stages = list(filter(lambda x: x[1] > 100, stage_data.items()))

    # Process only high-yield stages
    processed_data = []
    cumulative_factor = 1.0
    for name, value in valid_stages:
        adjusted = value * (cumulative_factor + 0.1)
        cumulative_factor *= 0.95  # decay factor
        processed_data.append(adjusted)

    # Red herring: complex string manipulation with no impact
    status_log = ""
    for s in growth_stages:
        status_log += f"[{s.upper()}]: OK|"
    checksum = sum(ord(c) for c in status_log if c.isalpha()) % 50

    # Core calculation function (depends on processed_data)
    def calculate_harvest(data):
        total = 0
        modifier = 1.1
        for val in data:
            if val > 150:
                total += val * modifier
                modifier *= 0.97
        return int(total)  # deterministic integer output

    # Final computation
    final_yield = calculate_harvest(processed_data)

    # Dead code path (never executed)
    if False:
        fallback = sum(processed_data) / len(processed_data)
        final_yield = int(fallback)

    # Output result as required
    print(f"Result: {final_yield}")
    return final_yield

simulate_agricultural_cycle()