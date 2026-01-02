def process_data(data, threshold):
    # Irrelevant preprocessing step (distractor)
    normalized = [x / max(data) for x in data]
    weighted_sum = sum(x * 0.9 for x in normalized)

    # Core logic begins here
    filtered = list(filter(lambda x: x > threshold, data))
    
    # Secondary processing with intermediate transformations
    squared_values = [x ** 2 for x in filtered]
    modded_values = [val % 7 for val in squared_values]  # Modular arithmetic

    # State tracking variables (some irrelevant)
    cumulative = 0
    peak_value = 0
    count_above_50 = 0

    for val in squared_values:
        cumulative += val
        if val > peak_value:
            peak_value = val
        if val > 50:
            count_above_50 += 1

    # Another distractor computation (not used later)
    average_sq = cumulative / len(squared_values) if squared_values else 0
    dummy_score = (peak_value * 0.3) + (cumulative * 0.01)

    # Actual result depends only on modded values and count
    adjustment_factor = len(modded_values) if sum(modded_values) % 2 == 0 else 1
    temp_result = sum(modded_values) * adjustment_factor

    # Final transformation
    final_adjustment = (temp_result + 3) // 4
    return final_adjustment

# Simulated sensor data stream
stream_buffer = [12, 15, 3, 8, 20, 5, 18, 2]
activation_threshold = 10

# Dead code path (misleading)
if len(stream_buffer) > 20:
    activation_threshold *= 2
elif any(x < 0 for x in stream_buffer):
    activation_threshold -= 1

# Key computation
final_output = process_data(stream_buffer, activation_threshold)

# Print result as required
print(f"Target result: {final_output}")