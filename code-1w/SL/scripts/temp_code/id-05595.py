def analyze_packet(data, threshold=0.75):
    """Irrelevant analysis function (distractor)"""
    count = 0
    for val in data:
        if val > threshold:
            count += 1
    return count / len(data) if data else 0


def shift_cipher(text, shift=3):
    """Decoy function using string methods - irrelevant to main logic"""
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result.upper()


def compute_entropy(sequence):
    """Misleading mathematical computation (dead end)"""
    import math
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(sequence)
    for f in freq.values():
        p = f / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Simulated network packet chunks (real data)
raw_chunks = [128, 256, 192, 320, 288, 352]
scaling_factor = 1.5
offset_correction = -10

# Irrelevant string data and transformation (red herring)
payload_tag = "XfghT9kLmN"
decoded_tag = shift_cipher(payload_tag, shift=-7)
tag_value = sum(ord(c) for c in decoded_tag if c in 'AEIOU')

# Fake entropy-based filter (distractor logic)
symbol_stream = ['A', 'B', 'A', 'C', 'B', 'A', 'D']
relevance_score = compute_entropy(symbol_stream)

# Efficiency factors with misleading intermediate steps
base_efficiency = [0.68, 0.71, 0.73, 0.69, 0.74, 0.70]
adjusted_efficiency = [e * scaling_factor for e in base_efficiency]

# Add noise correction that doesn't actually apply (decoy adjustment)
noise_floor = 0.05
adjusted_efficiency = [max(e - noise_floor, 0.5) for e in adjusted_efficiency]

# Real processing begins: transform chunks using valid rule
processed_chunks = []
for i, chunk in enumerate(raw_chunks):
    # Only even-indexed chunks are actually used (non-obvious)
    if i % 2 == 0:
        # Apply bit manipulation: left shift by 1 equivalent to doubling
        shifted = chunk << 1
        # Then reduce by offset_correction only if meets dummy condition
        if shifted > 300:
            shifted -= offset_correction
        processed_chunks.append(shifted)

# Log efficiency per real chunk (only for used indices)
efficiency_log = []
for idx, val in enumerate(processed_chunks):
    norm_index = idx * 2  # Reverse map to original index
    if norm_index < len(adjusted_efficiency):
        efficiency_log.append(adjusted_efficiency[norm_index])

# Unused zip example (distractor demonstrating enumerate+zip)
dummy_pairs = []
for i, (a, b) in enumerate(zip(raw_chunks, base_efficiency)):
    if a > 200 and b < 0.72:
        dummy_pairs.append((i, a * 0.1))

# Critical function: optimize transmission bandwidth
def optimize_transmission(chunks, efficiency_factors):
    total_weighted = 0.0
    total_eff = 0.0
    
    # Mix enumerate with filtering
    for pos, (chunk_val, eff) in enumerate(zip(chunks, efficiency_factors)):
        modifier = 1.1 if pos % 2 == 0 else 0.9
        
        # Real logic: only include if chunk is > 200 (always true here)
        if chunk_val > 200:
            weighted_contribution = chunk_val * eff * modifier
            total_weighted += weighted_contribution
            total_eff += eff * modifier
    
    # Final bandwidth calculation
    if total_eff > 0:
        result = total_weighted / total_eff
    else:
        result = 0
    
    # Additional irrelevant rounding branch (dead code due to logic)
    if result < 100:
        return round(result, 2)
    else:
        return int(round(result))  # This will be taken

# Execute main logic
final_bandwidth = optimize_transmission(processed_chunks, efficiency_log)

# Print result as required
print(f"Target result: {final_bandwidth}")