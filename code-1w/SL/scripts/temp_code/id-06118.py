import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x * 2 for x in data if x % 3 == 0]

# Misleading transformation chain
def decoy_transform(sequence):
    temp = [math.sin(x) for x in sequence]
    scaled = [int(abs(t * 100)) for t in temp]
    return scaled  # Never actually used

# Real transformation logic
def apply_filter(values, threshold=5):
    return [v for v in values if v > threshold]

# Core processing function
def process_item(x, mode='enhanced'):
    if mode == 'basic':
        return x + 10
    else:
        return (x ** 2) - (x * 3) + 7

# Higher-order processor
def process_data(items, settings):
    result = 0
    multiplier = settings.get('factor', 1)
    offset = settings.get('offset', 0)
    
    # Nested list comprehension with filtering
    processed_items = [process_item(val, settings['mode']) for val in items if val % 2 == 1]
    
    # Accumulation with conditional adjustment
    for idx, val in enumerate(processed_items):
        if idx % 2 == 0:
            result += val * multiplier
        else:
            result -= val + offset
    
    # Secondary adjustment based on length
    if len(processed_items) > 3:
        result = int(result / 1.5)
    
    return result

# Auxiliary computation (distractor)
def compute_stats(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return {'mean': mean_val, 'variance': variance}  # Computed but unused

# Main execution flow
if __name__ == '__main__':
    raw_sequence = [2, 7, 4, 9, 6, 11, 8]
    
    # Irrelevant pre-processing (red herring)
    normalized = [round(x / max(raw_sequence), 3) for x in raw_sequence]
    inverted = [1 - n for n in normalized if n > 0.3]
    
    # Actual relevant transformation
    filtered = apply_filter(raw_sequence, threshold=5)
    transformed = [x + 1 for x in filtered]  # Critical preprocessing
    
    # Configuration with misleading keys
    config = {
        'factor': 2,
        'offset': 5,
        'mode': 'enhanced',
        'debug': True,
        'version': '2.1a',
        'threshold': 0  # Unused parameter
    }
    
    # Decoy call (no side effects)
    _ = decoy_transform(raw_sequence)
    
    # Statistical analysis (distractor - computed but not used)
    stats = compute_stats(raw_sequence)
    
    # Key statement: main processing step
    final_output = process_data(transformed, config)
    
    # Print result as required
    print(f"Target result: {final_output}")