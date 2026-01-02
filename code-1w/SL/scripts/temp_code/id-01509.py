import itertools

def analyze_frequency(sequence):
    # Irrelevant helper: computes character frequency (not used in final result)
    freq = {}
    for char in sequence:
        freq[char] = freq.get(char, 0) + 1
    return freq

def validate_checksum(chunk):
    # Misleading function: looks important but unused
    return sum(chunk) % 256 == 0

def transform_block(x):
    # Core transformation: x -> (x ^ 3) + 7
    return (x ^ 3) + 7

def filter_relevant(stream):
    # Filters values that pass a specific bit condition (used)
    return [v for v in stream if (v & (v - 1)) == 0]  # Power of two check

def generate_lookup(keys):
    # Dead code path: generates mapping not used in main logic
    return {k: (k * 2) % 97 for k in keys}

def aggregate_window(values, size=4):
    # Sliding window average (distractor, not directly used)
    averages = []
    for i in range(len(values) - size + 1):
        averages.append(sum(values[i:i+size]) / size)
    return averages

def process_pipeline(data):
    # Main processing chain with multiple distractions
    
    # Step 1: Initial filtering (relevant)
    filtered = filter_relevant(data)
    
    # Step 2: Transform each element (relevant)
    transformed = list(map(transform_block, filtered))
    
    # Step 3: Simulate chunking (distractor variables)
    chunk_size = 3
    chunks = [transformed[i:i+chunk_size] for i in range(0, len(transformed), chunk_size)]
    chunk_sums = [sum(c) for c in chunks]  # Intermediate distractor
    
    # Step 4: Flatten and apply secondary mask (relevant)
    flattened = list(itertools.chain.from_iterable(chunks))
    masked = [flattened[i] for i in range(0, len(flattened), 2)]  # Take every other
    
    # Step 5: String-based encoding distraction
    encoded_str = ''.join([chr(97 + (v % 26)) for v in masked[:10]])  # 'a' to 'z' mapping
    reversed_chunks = [c[::-1] for c in chunks]  # Unused reversal
    
    # Step 6: Key aggregation (used)
    midpoint = len(masked) // 2
    upper_half = masked[:midpoint]
    lower_half = masked[midpoint:]
    
    # Step 7: Cross-half interaction (critical step)
    product_sum = 0
    for u, l in zip(upper_half, lower_half):
        product_sum += u * l
    
    # Step 8: Final adjustment using string property (surprisingly relevant)
    offset = len(encoded_str.split('a'))  # Number of 'a'-separated parts
    final_output = product_sum - offset
    
    # Print result as required
    print(f"Result: {final_output}")
    return final_output

# Simulated sensor data stream (deterministic input)
data_stream = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    12, 16, 24, 32, 48, 64, 128
]

# Dead initialization (red herring)
baseline_checksum = 42
lookup_table = generate_lookup([10, 20, 30])
analysis_log = analyze_frequency("abbcccaa")

# Execute main logic
final_output = process_pipeline(data_stream)