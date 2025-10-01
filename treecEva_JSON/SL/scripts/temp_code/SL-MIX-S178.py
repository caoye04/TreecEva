import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate_metrics(matrix):
    metrics = {
        'sums': [],
        'products': [],
        'geometric_means': []
    }
    
    for row in matrix:
        metrics['sums'].append(sum(row))
        prod = 1
        for item in row:
            prod *= item if item != 0 else 1
        metrics['products'].append(prod)
        
        nonzero = [x for x in row if x > 0]
        if nonzero:
            gm = math.pow(math.prod(nonzero), 1/len(nonzero))
            metrics['geometric_means'].append(gm)
        else:
            metrics['geometric_means'].append(0)
            
    return metrics

data_series = [
    [2, -4, 3, -1, 5],
    [1, 0, 2, 4],
    [3, 3, 3, 3, 3, 3]
]

# Process 1: Transform each series
processed_data = [complex_transform(series) for series in data_series]

# Process 2: Calculate metrics
metrics = aggregate_metrics(processed_data)

# Process 3: Weighted combination
weights = [0.5, 0.3, 0.2]
weighted_sum = 0
for i, (s, p, gm) in enumerate(zip(metrics['sums'], metrics['products'], metrics['geometric_means'])):
    component = (s * p) / (gm + 1) if gm != 0 else s * p
    weighted_sum += component * weights[i]
    
# Process 4: Apply modulo and final transformation
interim_result = int(weighted_sum) % 1000

# Process 5: Bitwise operations
bit_pattern = (interim_result << 2) ^ 0xFF
final_result = bit_pattern & ((1 << 10) - 1)  # Mask to 10 bits

print(f"Result: {final_result}")