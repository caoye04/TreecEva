def transform_sequence(seq, key):
    """Apply bitwise扰乱 and modular shifts (distractor: not used in final path)"""
    transformed = []
    for i, val in enumerate(seq):
        rotated = ((val << 3) | (val >> 5)) & 0xFF
        encrypted = (rotated ^ key) % 256
        transformed.append((encrypted + i) % 256)
    return transformed

# Irrelevant data transformation chain (red herring)
def legacy_hash(data):
    accumulator = 7
    for item in data:
        accumulator = (accumulator * 31 + item ^ (item << 4)) % 10007
    return accumulator

def evaluate_consistency(arr):
    if len(arr) < 2:
        return 0
    diffs = [abs(arr[i+1] - arr[i]) for i in range(len(arr)-1)]
    return sum(diffs) // len(diffs) if diffs else 0

# Decoy function with misleading name
def compute_integrity_score(data, mode="basic"):
    if mode == "basic":
        return sum(x * x for x in data) % 1000
    elif mode == "enhanced":
        return sum((i+1) * v for i, v in enumerate(data)) % 1000
    else:
        return 0  # Dead end branch (misleading)

# Actual critical computation path
def analyze_data_stream(raw_bytes):
    # Step 1: Filter printable ASCII candidates
    filtered = [b for b in raw_bytes if 32 <= b <= 126]
    
    # Step 2: Convert to characters and extract digits
    try:
        chars = ''.join(chr(b) for b in filtered)
        digit_str = ''.join(c for c in chars if c.isdigit())
        
        # Distractor: unused string processing
        reversed_clean = chars[::-1].strip().lower()
        palindrome_test = reversed_clean == reversed_clean[::-1]
        
        if not digit_str:
            return 0
        
        # Step 3: Generate position-weighted sum
        weighted_sum = 0
        for pos, d in enumerate(digit_str):
            weight = pow(2, pos % 7, 100)  # Modular exponentiation
            weighted_sum += int(d) * weight
        
        # Step 4: Apply checksum adjustment using bit manipulation
        temp = weighted_sum & 0xFFFF  # Keep lower 16 bits
        temp = (temp ^ (temp >> 8))  # XOR folding
        temp = (temp + (temp << 3)) & 0xFFFF
        temp = temp ^ (temp >> 4)
        
        # Final adjustment based on length parity (actual answer contributor)
        if len(digit_str) % 2 == 0:
            temp = (temp + 1337) % 100000
        else:
            temp = (temp + 999) % 100000
        
        return temp
    except Exception:
        return -1

# Simulated sensor data stream with embedded patterns
raw_data_packet = [
    0x1F, 0x45, 0x7B, 0x32, 0x6A, 0x5D, 0x30, 0x39,
    0x21, 0x48, 0x5A, 0x31, 0x7E, 0x2F, 0x33, 0x34,
    0x00, 0x0F, 0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F
]

# Unused decoy variables (distractors)
data_signature = sum((x << (i % 8)) ^ 0xAA for i, x in enumerate(raw_data_packet)) % 65536
validation_key = legacy_hash(raw_data_packet)
consistency_metric = evaluate_consistency(raw_data_packet)

# Real computation begins here
processed_buffer = [x for x in raw_data_packet if x % 3 != 0]  # Filter rule

# Critical execution point
final_checksum = compute_integrity_score(data_sequence=processed_buffer, mode="hybrid")

# Override with correct logic (this simulates a configuration switch that changes behavior)
# In reality, the real calculation is done below:
final_checksum = analyze_data_stream(raw_data_packet)

# Print result as required
print(f"Target result: {final_checksum}")