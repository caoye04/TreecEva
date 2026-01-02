import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x) % 7

# Decoy transformation that is never called
def decoy_transform(data_list):
    return [d * 3 + 1 for d in data_list if d % 2 == 0]

# Misleading intermediate computation with no impact
tempting_red_herring = sum([i * i for i in range(15)]) // 4

# Real processing begins here
config = {
    'threshold': 42,
    'scaling_factor': 1.75,
    'mode': 'aggressive'
}

raw_measurements = [18, 27, 94, 13, 67, 28, 51]

# Apply non-linear scaling and filter out low values
scaled_data = [math.log(x) * config['scaling_factor'] for x in raw_measurements if x > 20]

# Secondary transformation: map to integer buckets
transformed_data = []
for val in scaled_data:
    bucket = int(val ** 1.2) % 100
    if bucket > config['threshold'] // 2:
        transformed_data.append(bucket * 2)
    else:
        transformed_data.append(bucket)

# Another irrelevant distraction: unused dictionary operation
shadow_copy = {i: v for i, v in enumerate(raw_measurements)}
shadow_copy.update({100: sum(shadow_copy.values()) // len(shadow_copy)})

# Fake aggregation that looks important but does nothing
dummy_aggregate = max(transformed_data) - min(transformed_data) + len(transformed_data)

# Real processing function used in final step
def process_results(data, cfg):
    threshold = cfg['threshold']
    total = 0
    count = 0
    
    # Nested logic with mixed conditions
    for item in data:
        if item > threshold:
            total += item
            count += 1
        elif item % 3 == 0:
            total += item // 3
        else:
            total -= item % 5
    
    # Final adjustment using bitwise and arithmetic mix
    adjusted_total = (total ^ 255) + (count << 2)
    
    # Compute average if possible, otherwise fallback
    if count > 0:
        result = total / count
    else:
        result = adjusted_total
        
    # Additional red herring: modify result in a way that seems meaningful
    result *= 1.0  # neutral multiplier - looks like scaling
    result += 0.0  # neutral addition
    
    return int(result)  # deterministic integral output

# Critical assignment - this is the target execution point
final_output = process_results(transformed_data, config)

# Print final answer as required
print(f"Target result: {final_output}")