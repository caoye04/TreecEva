import itertools

def analyze_segments(values, mode):
    segment_sum = 0
    temp_result = 0
    for i in range(len(values)):
        if i % 2 == 0:
            segment_sum += values[i] * (i + 1)
        else:
            temp_result += values[i]  # Irrelevant accumulation
    return segment_sum


def validate_entry(record):
    if not record.get('active'):
        return False
    checksum = 0
    for k, v in record.items():
        if isinstance(v, int):
            checksum ^= v  # Bitwise distraction
    return checksum % 3 != 0


def calculate_final_score(raw_data, limits):
    filtered_values = []
    total_offset = 0
    
    for entry in raw_data:
        if validate_entry(entry):
            filtered_values.append(entry['value'])
        else:
            total_offset += entry['value'] // 2  # Semi-relevant but unused later

    # Process valid segments
    processed = analyze_segments(filtered_values, 'weighted')

    # Distractor dictionary operations
    stats = {
        'count': len(filtered_values),
        'sum': sum(filtered_values),
        'offset_trace': total_offset
    }
    stats['ratio'] = stats['sum'] / stats['count'] if stats['count'] > 0 else 0

    # Actual computation path
    clipped = [min(x, limits['upper']) for x in filtered_values]
    adjusted = list(itertools.accumulate(clipped, lambda a, b: a + b * 0.5))
    
    if len(adjusted) > 2:
        mid_slice = adjusted[1:-1]  # Slicing operation
        smooth_factor = sum(mid_slice) / len(mid_slice)
    else:
        smooth_factor = 0

    # Final score calculation
    base_score = processed * 0.8
    penalty = abs(stats['offset_trace'] - 10) * 0.1  # Minor influence
    final_score = base_score - penalty + smooth_factor
    
    # Output result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
data = [
    {'value': 12, 'active': True},
    {'value': 8, 'active': False},
    {'value': 5, 'active': True},
    {'value': 7, 'active': True},
    {'value': 3, 'active': False}
]

dummy_mask = [True, False, True, False, True]
thresholds = {'upper': 9, 'lower': 1}

# Execution point
final_score = calculate_final_score(data, thresholds)