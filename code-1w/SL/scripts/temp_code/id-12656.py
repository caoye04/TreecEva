import math

# Irrelevant constants and dummy configurations
dummy_config = {'mode': 'debug', 'version': '2.1.3', 'timeout': 300}
MAX_BUFFER_SIZE = 1024
DEBUG_MODE = True
LOG_INTERVAL = 15

# Distractor variables with plausible but unused computations
temp_cache = [i ** 2 for i in range(20)]
shadow_factor = sum(temp_cache) / len(temp_cache)
system_flag = False

# Simulated sensor data stream (real input)
data_stream = [3, 7, -2, 8, 1, 9, 5, 4]

# Misleading pre-processing that computes but doesn't affect final result
decoy_stats = {
    'mean': sum(data_stream) / len(data_stream),
    'peak': max(data_stream),
    'variance': sum((x - sum(data_stream)/len(data_stream))**2 for x in data_stream) / len(data_stream)
}

# Unused recursive function (dead code path)
def calculate_entropy(values, base=2):
    if len(values) <= 1:
        return 0
    midpoint = len(values) // 2
    return math.log(len(values)) + calculate_entropy(values[:midpoint], base)

# Threshold derived from irrelevant formula but actually used
threshold = int(math.sqrt(abs(sum(d for d in data_stream if d > 0))) // 1.5) if data_stream else 0

# Auxiliary function with conditional expression and distractors
def analyze_segment(segment):
    size = len(segment)
    weight = 1.5 if size >= threshold else 0.7
    total = sum(x for x in segment if x % 2 == 1)  # Sum of odd numbers only
    
    # Dummy normalization not used in output
    normalized = total / size if size > 0 else 0
    adjustment = (size * weight) - shadow_factor  # Uses shadow_factor as red herring
    
    return total + int(adjustment)  # adjustment barely affects due to shadow_factor scaling

# Main processing with nested logic and tuple unpacking
def process_results(stream, limit):
    chunks = []
    current_chunk = []
    
    for val in stream:
        current_chunk.append(val)
        # Conditional expression for chunk boundary decision
        if len(current_chunk) >= limit or (val < 0 and len(current_chunk) >= 2):
            chunks.append(tuple(current_chunk))
            current_chunk = []
    
    if current_chunk:
        chunks.append(tuple(current_chunk))
    
    # Accumulation with filtering
    accumulator = 0
    meta_data = []
    
    for idx, chunk in enumerate(chunks):
        # Real computation path
        chunk_sum = sum(chunk)
        chunk_max = max(chunk)
        
        # Decoy statistic stored but not used
        decoy_metric = chunk_sum * math.sin(math.pi * idx / 4) if idx % 2 == 0 else 0
        meta_data.append((chunk_sum, chunk_max, decoy_metric))
        
        # Actual contribution to result
        score = analyze_segment(chunk)
        
        # Conditional inclusion based on index
        multiplier = 2 if idx % 3 == 0 else 1
        accumulator += score * multiplier
    
    # Final transformation using only relevant accumulated value
    # All meta_data and decoy fields are ignored here
    final_score = accumulator * (1 + 0.1 * len(chunks))  # Scale by number of chunks
    
    # Red herring: system_flag check (never true)
    if system_flag and final_score > 100:
        return int(final_score / 2)
    
    return int(final_score)

# Execution point of interest
final_output = process_results(data_stream, threshold)

# Print result as required
print(f"Target result: {final_output}")