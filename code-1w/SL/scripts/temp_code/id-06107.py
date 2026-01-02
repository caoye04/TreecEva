import math

# Irrelevant helper function (decoy)
def analyze_signal(x):
    return sum([i * 0.5 for i in x if i % 2 == 0])

# Misleading transformation chain
def transform_sequence(seq):
    temp_a = [x ** 2 for x in seq if x < 10]
    temp_b = [math.log(x + 1) for x in temp_a]
    shifted = [(x * 1.5) % 7 for x in temp_b]
    return shifted  # Unused result

# Core processing pipeline
def encode_frame(frame):
    a = sum(frame) // len(frame)
    b = max(frame) - min(frame)
    c = (a * 3) ^ b  # Bitwise mix
    return c

# Secondary path with red herring
stored_records = []
for k in range(5):
    record = {"id": k, "value": (k ** 3) - (2 * k)}
    stored_records.append(record)

# Dead-end accumulator (distractor)
total_offset = 0
for item in stored_records:
    total_offset += item["value"] * 0.1

def filter_and_aggregate(values):
    filtered = list(filter(lambda x: x > 5, values))
    return sum(filtered) // 2 if filtered else 0

# Main data processor
def process_pipeline(stream):
    # Step 1: Initial slicing and reduction
    segment = stream[3:9]  # Critical slice
    
    # Distractor: irrelevant list comprehension
    dummy_grid = [[i + j for j in range(3)] for i in segment if i % 4 == 0]
    
    # Step 2: Compute base metrics
    avg_val = sum(segment) / len(segment)
    rounded_base = int(avg_val)
    
    # Step 3: Apply encoding
    encoded = encode_frame(segment)
    
    # Step 4: Conditional override (never triggered, misleading)
    if any(x < 0 for x in segment):
        fallback = filter_and_aggregate(segment)
        return fallback
    
    # Step 5: Secondary transformation (irrelevant to final output)
    _ = transform_sequence(segment)
    
    # Step 6: Key accumulation with bitwise adjustment
    intermediate = (encoded << 2) + (rounded_base & 7)
    
    # Step 7: Final adjustment using summation logic
    adjustment = sum([i for i in segment if i % 3 == 0])
    final_value = intermediate - adjustment
    
    # Step 8: Final XOR correction based on length
    final_value ^= len(segment)
    
    return final_value

# Input data stream (carefully crafted)
data_stream = [12, 8, 3, 7, 9, 4, 6, 11, 2, 14, 5]

# Execute main logic
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")