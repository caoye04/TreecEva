import itertools

# System health monitoring simulation with data transformation and pattern analysis

def collect_metrics(base_signal, threshold=50):
    return [x for x in base_signal if x > threshold]


def generate_sequence(seed, length):
    seq = [seed]
    for i in range(1, length):
        seq.append((seq[-1] * 17 + 25) % 101)
    return seq


def extract_features(raw_data):
    # Irrelevant feature extraction (red herring)
    magnitude = sum(abs(x) for x in raw_data)
    variance = sum((x - sum(raw_data)/len(raw_data))**2 for x in raw_data)
    peaks = [i for i in range(1, len(raw_data)-1) if raw_data[i] > raw_data[i-1] and raw_data[i] > raw_data[i+1]]
    return magnitude, variance, peaks


def transform_signal(data, factor=3, shift=7):
    # Actual relevant transformation
    shifted = [(x << 1) ^ shift for x in data]  # Bit manipulation: left shift and XOR
    wrapped = [x % 89 for x in shifted]
    return [x * factor for x in wrapped]


def validate_frame(sequence, mask=0xF):
    # Distractor function - not used in final computation
    checksum = 0
    for x in sequence:
        checksum ^= (x & mask)
    return checksum == 0x7D


def analyze_pattern(dataset, reference):
    # Core logic with multiple steps
    temp_state = 0
    for i, group in enumerate(itertools.zip_longest(dataset, reference)):
        a, b = group if group[1] is not None else (group[0], 0)
        
        # Conditional bit manipulation
        if i % 3 == 0:
            temp_state += (a ^ b) & 0xFF
        elif i % 3 == 1:
            temp_state -= (a + b) & 0x7F
        else:
            temp_state += ((a & 0x3F) | (b >> 2))
    
    # Final adjustment using tuple unpacking
    multiplier, offset = (3, -15)
    result = (temp_state * multiplier) + offset
    
    # Secondary path - dead code (distractor)
    if result < 0:
        backup = sum(itertools.accumulate([result % 10] * 5))
        result = backup  # Never executed due to logic flow
    
    return result

# --- Simulation Setup ---
base_input = [23, 45, 67, 89, 12, 34, 56, 78]
key_seed = 13

# Step 1: Collect metrics above threshold (filters to [67, 89, 56, 78])
filtered_data = collect_metrics(base_input)

# Step 2: Generate key sequence (length 8)
key_sequence = generate_sequence(key_seed, len(base_input))
# key_sequence becomes [13, 56, 69, 36, 75, 38, 9, 90, ... truncated to 8]

# Step 3: Extract irrelevant features (distractor computation)
mag, var, pks = extract_features(filtered_data)

# Step 4: Transform the filtered data (critical path)
transformed_data = transform_signal(filtered_data, factor=3, shift=7)
# transformed_data = [((x<<1)^7)%89*3 for x in [67,89,56,78]] → [3*(((134^7)%89)], ...]

# Step 5: Validate frame (unused result - red herring)
validation_result = validate_frame(transformed_data)

# Step 6: Analyze pattern using both datasets (main computation)
final_diagnostic = analyze_pattern(transformed_data, key_sequence)

# Output the target result
print(f"Target result: {final_diagnostic}")