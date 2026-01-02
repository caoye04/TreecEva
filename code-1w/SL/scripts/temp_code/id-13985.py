def process_metrics(stream):
    temp_buffer = []
    cumulative_sum = 0
    weight_factor = 1.5
    adjustment = 0.85
    efficiency_score = 0
    outlier_count = 0

    for index, (value, flag) in enumerate(zip(stream['values'], stream['flags'])):
        if flag and value > 0:
            transformed = value ** 0.5 * weight_factor
            temp_buffer.append(transformed)
            cumulative_sum += transformed

            if value > 50:
                outlier_count += 1
                backup_adjustment = value // 10
        else:
            cumulative_sum -= 1

    avg_temp = cumulative_sum / len(temp_buffer) if temp_buffer else 0

    # Irrelevant computation block (distractor)
    hypothetical_gains = []
    for i in range(3):
        hypothetical_gains.append((avg_temp * 1.1) ** i)
    projected_yield = sum(hypothetical_gains) * adjustment  # Not used later

    # Core logic continues
    modifier = len([x for x in stream['values'] if x % 2 == 0])
    scaling_lambda = lambda m, s: (s * m) / (m + 1) if m > 0 else s
    efficiency_score = scaling_lambda(modifier, avg_temp)

    # Dead code path (misleading)
    if outlier_count < 0:  # Never executed
        efficiency_score *= 0.5

    final_output = efficiency_score * 1.0
    return final_output

# Input data
input_stream = {
    'values': [16, 25, 36, 49, 64, 81],
    'flags': [True, True, False, True, True, False]
}

data_stream = input_stream
result = process_metrics(data_stream)
efficiency_score = result
print(f"Result: {efficiency_score}")