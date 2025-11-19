from collections import defaultdict
import itertools

def process_devices(device_ids):
    mask = 0b110101
    xor_results = []
    
    # Step 1: Apply XOR with rotating mask
    for i, device_id in enumerate(device_ids):
        rotated_mask = ((mask << (i % 5)) | (mask >> (5 - (i % 5)))) & 0b111111
        xor_result = device_id ^ rotated_mask
        xor_results.append(xor_result)
    
    # Step 2: Create hash map of value frequencies
    freq_map = defaultdict(int)
    for val in xor_results:
        freq_map[val] += 1
    
    # Step 3: Sort by frequency-weighted value (freq * value)
    sorted_vals = sorted(xor_results, key=lambda x: (freq_map[x], x))
    
    # Step 4: Bitwise compaction of top 3 values
    compacted = 0
    for i, val in enumerate(sorted_vals[-3:]):
        if i == 0:
            compacted = val
        else:
            compacted = (compacted << 4) | (val & 0xF)
    
    # Final encoding step
    encoded_priority = (compacted ^ 0xFF) & 0xFFF
    return encoded_priority

# Device identifiers from network logs
devices = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x1A, 0x2B]
encoded_priority = process_devices(devices)
print(f"Result: {encoded_priority}")