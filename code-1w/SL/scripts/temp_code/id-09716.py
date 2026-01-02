def process_data(data, threshold):
    temp_cache = []
    cumulative_shift = 0
    overflow_flag = False
    activation_log = []

    for index in range(len(data)):
        raw_value = data[index]
        normalized = raw_value - (index * 0.1)
        
        # Irrelevant transformation chain
        shadow_copy = normalized * 1.05
        if shadow_copy > 20:
            temp_cache.append(shadow_copy)

        # Core logic disguised among noise
        if normalized > threshold:
            adjusted = int(normalized ** 0.5)
            cumulative_shift += adjusted
            activation_log.append(adjusted)
            
            # Red herring: complex but unused calculation
            secondary_effect = sum([x % (adjusted + 1) for x in activation_log if x > 1])
            if secondary_effect > 100:
                overflow_flag = True

    # Distractor: semi-relevant post-processing
    if temp_cache:
        average_temp = sum(temp_cache) / len(temp_cache)
        smoothing_factor = average_temp * 0.01
        cumulative_shift = int(cumulative_shift + smoothing_factor)

    # Key computation with lambda obfuscation
    transform = lambda x: x + (x // 3) if x > 0 else x
    final_shift = transform(cumulative_shift)

    # Linear search for fallback (never triggered due to data)
    fallback_value = 0
    for val in activation_log:
        if val == 999:
            fallback_value = -1
            break

    # Final assignment
    final_output = final_shift + fallback_value
    return final_output

# Input setup
stream_buffer = [25, 16, 36, 49, 81, 100, 144, 121]
activation_threshold = 30

# Execution point
final_output = process_data(stream_buffer, activation_threshold)
print(f"Result: {final_output}")