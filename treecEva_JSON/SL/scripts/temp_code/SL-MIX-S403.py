import math

def process_matrix(data):
    transformed = []
    for row in data:
        new_row = []
        for val in row:
            if val > 0:
                new_row.append(math.log(val) if val != 1 else 0)
            else:
                new_row.append(0)
        transformed.append(new_row)
    return transformed

def aggregate_stats(matrix):
    total_sum = 0
    count = 0
    for row in matrix:
        for val in row:
            if val != 0:
                total_sum += val
                count += 1
    return total_sum / count if count > 0 else 0

data = [
    [math.exp(1), math.exp(2), 0, math.exp(3)],
    [1, math.exp(1), math.exp(2), 0],
    [0, 1, math.exp(3), math.exp(1)]
]

processed = process_matrix(data)
avg_value = aggregate_stats(processed)

# Create a dictionary with calculated values
results_dict = {
    'processed_data': processed,
    'average': avg_value,
    'sum_of_averages': avg_value * len(processed),
    'rounded_sum': round(avg_value * len(processed))
}

# Perform bit operations on the rounded sum
bitwise_result = results_dict['rounded_sum']
bitwise_result = (bitwise_result << 2) ^ 0xF  # Shift left by 2 and XOR with 15

# Final calculation
final_result = int(math.floor(bitwise_result / 3.0))

print(f"Result: {final_result}")