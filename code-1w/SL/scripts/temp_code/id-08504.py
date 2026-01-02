import math

# Simulated sensor data processing pipeline with red herrings
def analyze_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.5]
    amplified = [x * 3.5 for x in filtered]
    return amplified

# Irrelevant auxiliary function (decoy)
def compute_entropy(data):
    total = 0
    for x in data:
        if x != 0:
            total -= x * math.log(abs(x))
    return round(total, 4)

# Core transformation logic
def transform_sequence(seq, key_offset):
    shifted = [(seq[i] + seq[(i+1)%len(seq)]) for i in range(len(seq))]
    modded = [val % (key_offset + 7) for val in shifted]
    return [val for val in modded if val % 2 == 1]  # Keep only odds

# Bit manipulation red herring
def obfuscate_id(n):
    n ^= 0xFEED
    n = (n << 3) & 0xFFFF
    n |= (n >> 5)
    return n & 0xFF

# Main processing chain
base_stream = [12, 3, 8, 1, 9, 4, 7]
decoy_labels = ['A', 'B', 'C', 'D', 'E']

# Step 1: Initial slicing and truncation
subset = base_stream[1:6]  # [3, 8, 1, 9, 4]

# Step 2: Apply transformation with offset
processed = transform_sequence(subset, len(decoy_labels))  # len=5 -> mod 12

# Step 3: Further slicing to extract middle elements
temp_chunk = processed[1:-1]  # Remove first and last

# Step 4: Conditional amplification
if sum(temp_chunk) > 10:
    temp_chunk = [x * 2 for x in temp_chunk]

# Step 5: Pack into tuple and simulate transmission
data_packet = (101, tuple(temp_chunk), 202)

# Step 6: Extract and flatten
transformed_chunk = list(data_packet[1])

# Dead code path - never executed but looks important
reconstructed = []
for item in transformed_chunk:
    reconstructed.append(item + 5)
    break  # Artificial exit

# Step 7: Real processing function
def process_data(arr):
    if not arr:
        return -1
    
    # Accumulate with alternating signs
    acc = 0
    for i, val in enumerate(arr):
        if i % 2 == 0:
            acc += val * 1.5
        else:
            acc -= val * 0.5
    
    # Final modulation
    return int(acc + 7) if acc > 0 else int(acc - 7)

# Step 8: Critical execution point
final_output = process_data(transformed_chunk)

# Irrelevant checksums
checksum_1 = sum(base_stream) % 256
dynamic_key = obfuscate_id(checksum_1)
entropy_val = compute_entropy([0.1, 0.3, 0.6])

# Output target result
print(f"Result: {final_output}")