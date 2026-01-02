import math

# Irrelevant helper function (dead code path)
def unused_calculator(x):
    return (x ** 2 + 3 * x + 1) % 7

# Decoy transformation chain
def decoy_transform(sequence):
    temp = [s[::-1] for s in sequence if len(s) > 3]
    temp = [t[1:-1] for t in temp]
    joined = ''.join(temp)
    split_parts = joined.split('a')
    return [len(p) for p in split_parts]

# Real processing components
def extract_numeric_segments(text_list):
    numeric_chunks = []
    for item in text_list:
        chunk = ''.join([c for c in item if c.isdigit()])
        if chunk:
            numeric_chunks.append(int(chunk))
    return numeric_chunks

def bitwise_conditional_shift(values, threshold):
    shifted = []
    for v in values:
        if v & 1:  # odd
            shifted.append(v << 2)
        elif v > threshold:
            shifted.append(v >> 1)
        else:
            shifted.append(v ^ 5)
    return shifted

def compute_weighted_sum(arr):
    weights = [math.cos(i * 0.1) for i in range(len(arr))]
    weighted = sum(arr[i] * weights[i] for i in range(len(arr)))
    return round(weighted, 6)

# Complex data transformation pipeline
def process_pipeline(stream):
    # Step 1: Extract numbers from strings
    raw_numbers = extract_numeric_segments(stream)
    
    # Distractor: unused intermediate
    reversed_stream = [s[::-1] for s in stream]
    meta_info = {i: len(s) for i, s in enumerate(stream)}
    del meta_info  # Simulate cleanup, irrelevant
    
    # Step 2: Filter and transform
    filtered = [x for x in raw_numbers if x % 2 == 0 and x > 10]
    
    # Distractor: redundant slicing
    slice_a = filtered[:]
    slice_b = filtered[1::2]
    _ = slice_a[::2]  # unused
    
    # Step 3: Bitwise manipulation
    transformed = bitwise_conditional_shift(filtered, 50)
    
    # Distractor: fake aggregation
    fake_agg = 0
    for i, val in enumerate(transformed):
        if i % 3 == 0:
            fake_agg += val * (i + 1)
    
    # Step 4: Real computation path
    cleaned = [t for t in transformed if t < 200]  # filter outliers
    
    # Step 5: Weighted summation with trigonometric weights
    result = compute_weighted_sum(cleaned)
    
    # Final adjustment based on length parity
    if len(cleaned) % 2 == 0:
        result -= 17.3
    else:
        result += 9.8
    
    return result

# Main execution
if __name__ == '__main__':
    # Input data stream (mixture of alphanumeric)
    data_stream = [
        'temp2load',
        'sys34init',
        'bus86reset',
        'io42ack',
        'page105fault',
        'seg204dump',
        'crc511check'
    ]
    
    # Irrelevant pre-processing
    indexed_data = list(enumerate(data_stream))
    zipped_pairs = list(zip(data_stream, [len(d) for d in data_stream]))
    _ = [z for z in zipped_pairs if z[1] > 7]
    
    # Critical execution point
    final_output = process_pipeline(data_stream)
    
    # Output result
    print(f"Result: {final_output}")