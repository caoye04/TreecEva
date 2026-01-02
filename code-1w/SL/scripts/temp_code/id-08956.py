def preprocess_signal(samples):
    filtered = []
    noise_floor = 0.04
    for s in samples:
        if abs(s) > noise_floor:
            filtered.append(s * 1.85)
    return [round(f, 3) for f in filtered]

# Irrelevant helper (distractor)
def analyze_frequency_peaks(data):
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    return sorted(peaks, reverse=True)

# Unused transformation chain
def transform_legacy_format(seq):
    encoded = []
    for val in seq:
        encoded.append((val + 7) % 256)
    return encoded

# Core logic with distractors
def compute_integrity_value(data, mode="basic"):
    temp_buffer = []
    checksum = 0
    overflow_flag = False
    
    # Simulate multi-stage decoding
    for index, (key, value) in enumerate(zip(range(len(data)), data)):
        adjusted_index = (index + 3) % 7
        
        # Mode-specific processing
        if mode == "hybrid":
            intermediate = (value ^ key) + adjusted_index
            if intermediate > 100:
                intermediate = intermediate % 89
            temp_buffer.append(intermediate)
        else:
            temp_buffer.append(value * 2)
    
    # Secondary pass with modular arithmetic
    for i, val in enumerate(temp_buffer):
        if i % 3 == 0:
            checksum += (val * 7) % 13
        elif i % 4 == 0:
            checksum -= (val * 2) % 11
        else:
            checksum += val % 5
        
        # Overflow simulation (distractor)
        if checksum > 5000:
            overflow_flag = True
            checksum %= 1000

    # Decoy manipulation block (never alters final result)
    shadow_copy = temp_buffer.copy()
    for j in range(len(shadow_copy)-1, 0, -1):
        shadow_copy[j] = (shadow_copy[j] + shadow_copy[j-1]) % 256
    
    # Final computation
    for idx, v in enumerate(temp_buffer):
        checksum ^= (v + idx) % 17
    
    return checksum

# Extraneous data structure (red herring)
class SignalFrame:
    def __init__(self, timestamp, values):
        self.timestamp = timestamp
        self.raw_values = values
        self.processed = False

    def flag_reprocess(self):
        self.processed = False

# Unused enumeration pattern (distractor)
status_codes = ['OK', 'SYNC_LOST', 'WEAK_SIGNAL', 'NOISE_HIGH']
indexed_statuses = {i: status for i, status in enumerate(status_codes)}

# Input data (simulated sensor readings)
raw_samples = [12, 45, 67, 23, 89, 14, 77, 31, 50, 88, 29]
processed_samples = preprocess_signal([s * 0.62 for s in raw_samples])

# Generate transmission data via list comprehension with zip
indices = list(range(len(processed_samples)))
data_pairs = zip(indices, processed_samples)
transmission_data = [int((idx + val) * 3.1) for idx, val in data_pairs]

# Dead code path — appears important but unused
if len(transmission_data) > 10:
    scaled_data = [x * 2 for x in transmission_data]
else:
    scaled_data = transmission_data[:]

# Key statement
final_checksum = compute_integrity_value(transmission_data, mode="hybrid")

# Print result
print(f"Result: {final_checksum}")