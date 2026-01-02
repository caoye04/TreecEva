import math

# Irrelevant helper function (dead code path)
def unused_calculate_entropy(data):
    return -sum(p * math.log2(p) for p in data if p > 0)

# Decoy transformation function
def transform_sequence(seq):
    return [x ** 2 - 3 * x + 2 for x in seq if x % 2 == 0]

# Real processing function
def process_segments(segments, settings):
    accumulator = 0
    threshold = settings['base_threshold'] * math.sin(math.pi / 4)
    
    # Distractor: irrelevant list comprehension with string methods
    labels = ['seg_{}'.format(i+1) for i in range(len(segments))]
    cleaned_labels = [label.strip('_').upper().replace('SEG', 'SECTION') for label in labels]
    
    # Meaningful but obscured computation
    for idx, (val, flag) in enumerate(zip(segments, settings['flags'])):
        if flag:
            temp_val = val * (idx + 1)
            if temp_val > threshold:
                # Bit manipulation red herring
                masked = temp_val & int(threshold)
                adjusted = temp_val ^ int(math.log2(idx + 2))
                accumulator += int(adjusted)
            else:
                accumulator -= int(math.sqrt(abs(temp_val)) + 1)
        else:
            # Unused branch with misleading comment
            # This would adjust for drift, but flag prevents execution
            accumulator += val % 7
    
    # Complex but irrelevant tuple unpacking and reassignment
    meta_info = [('a', 1), ('b', 2), ('c', 3)]
    keys, values = zip(*meta_info)
    lookup = {k: v for k, v in zip(keys, values)}
    
    # Final adjustment using distractor variables
    scale = len(cleaned_labels) / (lookup['b'] or 1)
    final_value = accumulator * scale
    
    # Key assignment point
    final_output = int(final_value + 0.5)  # Round to nearest integer
    
    return final_output

# Main execution block
if __name__ == '__main__':
    # Input data with embedded distractions
    raw_stream = [2.1, 3.7, 1.4, 5.6, 2.3]
    segment_data = [int(x * 2) for x in raw_stream]  # Doubled values: [4, 7, 2, 11, 4]

    extra_metadata = {
        'version': '2.1-alpha',
        'tags': ['compute', 'legacy', ''],
        'active': True
    }
    
    # Filter out empty tags using string method (distractor)
    valid_tags = [tag.upper() for tag in extra_metadata['tags'] if tag.strip() != '']
    
    config = {
        'base_threshold': 6.5,
        'flags': [True, False, True, True, False],
        'mode': 'aggressive'
    }

    # Spurious bitwise operation chain (unused)
    magic_number = 0
    for i in range(5):
        magic_number ^= (i * 13) & 0xFF
    
    # Critical execution point
    final_output = process_segments(segment_data, config)
    
    # Output result
    print(f"Result: {final_output}")