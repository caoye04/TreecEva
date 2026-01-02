def calculate_performance_metric():
    base_value = 42
    modifier = 17
    temp_offset = 3

    # Simulate sensor readings with noise filtering
    raw_readings = [98, 102, 97, 105, 110, 95, 100]
    filtered = [x for x in raw_readings if abs(x - 100) <= 10]
    avg_reading = sum(filtered) / len(filtered) if filtered else 100

    # Secondary calculation: system health check (distractor)
    health_flags = 0b1101
    error_count = bin(health_flags).count('1')
    critical_error = bool(health_flags & 0b1000)

    # Irrelevant transformation chain
    dummy_accumulator = 0
    for i in range(3):
        dummy_accumulator += (modifier >> i) ^ (base_value << (i % 2))

    # Key processing with conditional expression
    adjustment_factor = 1.5 if avg_reading > 99 else 0.8
    intermediate = int((avg_reading - 90) * adjustment_factor)

    # Bitwise state encoding (partially relevant)
    encoded_state = (intermediate << 2) | (modifier & 0b11)

    # Misleading complex-looking but unused computation
    shadow_value = (base_value * 2 + modifier) // temp_offset
    shadow_value = shadow_value if shadow_value < 100 else shadow_value // 2

    # Final score derivation through nested logic
    if encoded_state > 100:
        final_score = encoded_state - 60
    else:
        final_score = encoded_state + 20

    return final_score

# Execute and print result
target_result = calculate_performance_metric()
print(f"Target result: {target_result}")