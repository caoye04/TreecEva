def process_segments(data, config):
    segment_key = config['primary'] + '_seg'
    raw_segment = data[segment_key]
    
    # Slice middle portion and apply modular scaling
    mid_slice = raw_segment[2:-2]
    scaled_values = [val % config['scale'] for val in mid_slice]
    
    # Conditional transformation based on threshold
    if sum(scaled_values) > config['threshold']:
        adjusted = [v * 1.5 for v in scaled_values]
    else:
        adjusted = [v + 5 for v in scaled_values]
    
    # Final aggregation with dictionary lookup weighting
    weights = {'A_seg': 2, 'B_seg': 3, 'C_seg': 1}
    weight = weights.get(segment_key, 1)
    result = int(sum(adjusted) * weight)
    
    # Irrelevant tracking variable (minimal distraction)
    stats = {'count': len(adjusted), 'active': True}
    
    return result

# Input setup
data = {
    'A_seg': [4, 8, 15, 16, 23, 42],
    'B_seg': [1, 2, 3],
    'C_seg': [5, 10]
}
config = {
    'primary': 'A',
    'scale': 10,
    'threshold': 20
}

result = process_segments(data, config)
print(f"Result: {result}")