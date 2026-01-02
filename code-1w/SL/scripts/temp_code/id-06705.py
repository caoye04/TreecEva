import itertools

def process_metrics(stream):
    base_multiplier = 1.5
    temp_buffer = []
    cumulative_shift = 0
    efficiency_score = 0
    overflow_flag = False

    for index, chunk in enumerate(stream):
        chunk_value = sum(chunk)
        
        # Irrelevant transformation (distractor)
        transformed = list(map(lambda x: x ** 0.5 + 2, chunk))
        avg_transformed = sum(transformed) / len(transformed)

        if chunk_value > 50:
            adjustment_factor = 2 if index % 2 == 0 else 3
            cumulative_shift += chunk_value * adjustment_factor
            
            # Real logic branch
            if cumulative_shift > 200:
                cumulative_shift = 200 - (cumulative_shift % 37)

        # Dead code path (misleading)
        if chunk_value < 0:
            overflow_flag = True
            temp_buffer.append(chunk_value)

        # Core computation
        weighted_sum = sum(x * (i + 1) for i, x in enumerate(chunk))
        efficiency_score += weighted_sum // (index + 1) if index >= 0 else 0

    # Secondary processing with conditional expression
    final_correction = 10 if efficiency_score > 150 else 5
    efficiency_score -= final_correction

    # Unused helper computation (distractor)
    def auxiliary_diagnostic(val):
        return val * base_multiplier + 7.3
    
    diagnostic_trace = [auxiliary_diagnostic(x) for x in [10, 20, 30]]

    # Key statement
    final_output = efficiency_score
    return final_output

# Data setup
raw_data = [[8, 12, 15], [20, 18, 25], [30, 5, 10], [14, 16, 22]]
data_stream = [list(group) for group in itertools.islice(itertools.cycle(raw_data), 4)]

# Execute
result_var = process_metrics(data_stream)
efficiency_score = result_var
print(f"Result: {efficiency_score}")