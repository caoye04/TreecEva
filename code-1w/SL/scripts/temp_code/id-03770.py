import math

# Irrelevant helper function (decoy)
def unused_helper(x):
    return x ** 3 + 2 * x - 1

# Another red herring function
def misleading_normalization(arr):
    mean = sum(arr) / len(arr)
    return [math.sin(x - mean) for x in arr]  # Not used in actual logic

# Distractor data
noise_data = [0.1, -0.5, 0.3, 0.7, -0.2]
duplicate_flags = [False, True, False, True, False]

# Unused transformation lambdas
temp_transform = lambda z: z if z > 0 else abs(z) * 0.5
identity_trap = lambda x: x  # Looks important but isn't used

# Real processing begins here
raw_values = [18, 24, 36, 42]
weights = [0.1, 0.3, 0.4, 0.2]

# Apply meaningful weighting with distraction from above
weighted_parts = []
for i in range(len(raw_values)):
    if i % 2 == 0:
        weighted_parts.append(raw_values[i] * weights[i] * 0.9)  # Slight decay on even indices
    else:
        weighted_parts.append(raw_values[i] * weights[i] * 1.1)  # Boost on odd indices

# Compute base score
base_score = sum(weighted_parts)

# Secondary metric (partially relevant)
efficiency_ratio = (max(raw_values) - min(raw_values)) / max(raw_values)

# Hidden adjustment factor based on bit manipulation (key insight buried)
binary_mask = 0b1010
adjustment_factor = bin(binary_mask & int(base_score % 17)).count('1')

# Complex conditional that depends on multiple prior values
if efficiency_ratio > 0.6:
    bonus = 15
elif base_score > 30 and adjustment_factor >= 2:
    bonus = 10
else:
    bonus = 5

# Simulate a "data validation" step (mostly irrelevant)
validation_log = []
for val in raw_values:
    status = 'valid' if val % 6 == 0 else 'flagged'
    validation_log.append({'value': val, 'status': status})

# Core calculation hidden among distractions
def calculate_composite_score(data):
    # Data is ignored; uses global state instead (misleading parameter)
    primary_component = base_score * (1 + efficiency_ratio * 0.25)
    secondary_component = bonus * adjustment_factor
    
    # Use lambda to obscure aggregation logic
    aggregator = lambda x, y: round(x + y, 4)
    intermediate = aggregator(primary_component, secondary_component)
    
    # Final nonlinear scaling
    if intermediate > 50:
        return math.log(intermediate) * adjustment_factor * 7
    else:
        return intermediate * 1.5

# Critical assignment point
data = {'values': [999, -1], 'meta': 'none'}  # Unused dummy input
final_score = calculate_composite_score(data)

# Output result as required
print(f"Target result: {final_score}")