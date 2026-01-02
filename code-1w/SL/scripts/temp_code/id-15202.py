def calculate_efficiency(data, limit):
    filtered_data = [x for x in data if x > limit // 2]
    temp_buffer = [x * 1.5 for x in filtered_data]
    scaling_factor = 0
    if len(temp_buffer) > 3:
        scaling_factor += 2
    else:
        scaling_factor += 1
    
    # Irrelevant accumulation (distractor)
    accumulator = 0
    for i in range(len(temp_buffer)):
        accumulator += temp_buffer[i] % 7

    # Misleading transformation (not used later)
    transformed = [int(x // 2) for x in temp_buffer if x > 4]
    size_check = len(transformed) >= 2

    # Core logic with slicing and conditional update
    segment = temp_buffer[1:-1] if len(temp_buffer) > 2 else temp_buffer
    base_score = sum(segment)

    adjustment = 0
    for val in segment:
        if val > limit:
            adjustment += 1.5
        elif val == limit:
            adjustment += 0.5
    
    final_score = base_score + adjustment * scaling_factor

    # Dead code path (never reached due to logic)
    if False and len(data) == 0:
        final_score = -999

    return int(final_score)

# Simulation parameters
temperature_readings = [12, 8, 15, 20, 6, 18]
threshold = 10

# Auxiliary computation (semi-relevant but not part of answer)
baseline_energy = sum([t ** 2 for t in temperature_readings]) / 100

profile_data = temperature_readings[::2]  # Slice: [12, 15, 6]

# Key computational step
thermal_capacity = calculate_efficiency(profile_data, threshold)

print(f"Result: {thermal_capacity}")