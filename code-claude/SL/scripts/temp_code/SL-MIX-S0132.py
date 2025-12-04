# Warehouse optimization problem
# Calculate optimal container capacity based on item weights and constraints

weights = [15, 22, 8, 31, 27, 18, 12, 25]
volumes = [2.1, 3.5, 1.2, 4.8, 3.7, 2.5, 1.8, 3.2]

# Filter out weights that don't meet initial criteria
weight_threshold = 10
volume_threshold = 2.0

# Processing phase 1: weight analysis
weight_factors = list(map(lambda x: x % 7, weights))
weight_priority = sum(weight_factors)

# Apply volume adjustments
volume_adjustments = [round(v * 1.5, 1) for v in volumes]
discount_factor = 0.8

# Candidate weights calculation
filtered_weights = []
efficiency_scores = {}

# Process items with enumeration
for idx, (weight, volume, adj_volume) in enumerate(zip(weights, volumes, volume_adjustments)):
    # Calculate efficiency score - only used for reporting
    efficiency = weight / volume if volume > 0 else 0
    efficiency_scores[idx] = efficiency
    
    # Filter weights based on complex criteria
    if weight >= weight_threshold and volume >= volume_threshold:
        # Apply adjustment formula
        adjusted_weight = int(weight * (1 + (idx % 3) * 0.1))
        filtered_weights.append(adjusted_weight)

# Additional container specifications (not directly used in final calculation)
container_types = {'small': 20, 'medium': 30, 'large': 40}
container_costs = {'small': 100, 'medium': 150, 'large': 200}

# Set operations for tracking container combinations
used_combinations = set([3, 5, 8])
available_combinations = set([2, 3, 5, 8, 13])
valid_combinations = available_combinations - {2, 13}

# Find optimal weight capacity
total_filtered = sum(filtered_weights)
average_filtered = total_filtered / len(filtered_weights) if filtered_weights else 0

# Calculate max index - key calculation for finding optimal capacity
max_index = 0
for i in range(1, len(filtered_weights)):
    # Compare current with max, update if greater
    if filtered_weights[i] > filtered_weights[max_index]:
        max_index = i

# Set optimal capacity based on maximum filtered weight
optimal_capacity = filtered_weights[max_index]

print(f"Result: {optimal_capacity}")