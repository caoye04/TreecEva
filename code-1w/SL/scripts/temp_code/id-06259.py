from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulate a data processing pipeline with multiple stages and distractions
def process_signals(raw_data):
    # Irrelevant transformation: reverse and convert case (distractor)
    reversed_data = [s[::-1].swapcase() for s in raw_data]
    
    # Real computation begins: count character frequencies per string
    freq_map = [Counter(s) for s in raw_data]
    
    # Extract numeric weights from each string based on position and char
    weights = []
    for s in raw_data:
        w = 0
        for i, c in enumerate(s):
            w += (i + 1) * (ord(c.lower()) - ord('a') + 1)
        weights.append(w)
    
    return weights

# Decoy function – looks important but unused
def deprecated_checksum(data):
    acc = 0
    for x in data:
        acc = (acc * 31 + x) % 997
    return acc

# Another red herring: complex but dead code path
unused_buffer = [0] * 100
for i in range(len(unused_buffer)):
    unused_buffer[i] = (i * i + 3 * i + 7) % 256

# Main logic disguised among noise
raw_input = ['signalA', 'pulseB', 'waveC', 'burstD', 'toneE']

# Step 1: Process signals to get weighted values
weighted_values = process_signals(raw_input)

# Step 2: Apply bitmask filtering (only some bits matter)
masked_values = [w & 0xFF for w in weighted_values]  # Use only lowest byte

# Step 3: Accumulate sum with offset based on length
summation = sum(masked_values)
offset = len(raw_input) * 4

# Step 4: Introduce distractor variables that look related
shadow_sum = sum(w & 0xFFFF for w in weighted_values)  # misleading wider mask
phantom_ratio = shadow_sum / (summation + 1) if summation != -1 else 0  # decoy metric

# Step 5: Frequency analysis side-channel (irrelevant)
all_chars = ''.join(raw_input)
char_freq = Counter(all_chars)
dominant_char_value = ord(max(char_freq, key=char_freq.get))

# Step 6: Bit manipulation chain with red herrings
bit_scramble = 0
for v in masked_values:
    bit_scramble ^= v
    bit_scramble = (bit_scramble << 1) | (bit_scramble >> 7)
    bit_scramble &= 0xFF

# Step 7: Conditional adjustment (never triggers - dead logic)
if any(v > 1000 for v in weighted_values):  # never true
    offset -= 50
else:
    pass  # neutralize

# Step 8: Real finalization logic buried here
def finalize(total, shift):
    temp = (total << 2) ^ shift
    temp ^= (temp >> 4)
    temp &= 0x3FFFF  # limit to 18 bits
    return temp + 13  # deterministic offset

# Step 9: Compute target variable
checksum = finalize(summation, offset)

# Step 10: Print result as required
print(f"Result: {checksum}")