import math

# Simulated satellite telemetry data processing with noise filtering and signal encoding
def collect_telemetry_data():
    raw_samples = [i * 0.5 for i in range(20)]
    noise_floor = 3.7
    filtered = []
    for x in raw_samples:
        if x > 2.0:
            adjusted = x - noise_floor + (x % 1.3)
            if adjusted > 0: 
                filtered.append(adjusted)
    return filtered[:12]

# Irrelevant auxiliary function - dead code path (distractor)
def calculate_orbit_decay(t):
    decay = 0
    for i in range(1, t+1):
        decay += i * 0.001
    return decay

def generate_checksum(data):
    # Simple XOR-based checksum (used later)
    checksum = 0
    for val in data:
        int_val = int(val * 10) & 0xFF
        checksum ^= int_val
    return checksum

# Signal quantization with slicing and bit manipulation
def quantize_signal(data):
    quantized = []
    for val in data:
        q_val = int(val * 16) & 0xFFFF
        if q_val % 2 == 0:
            q_val ^= 0xAAAA
        else:
            q_val ^= 0x5555
        quantized.append(q_val)
    return quantized

# Misleading transformation - not used in final result (red herring)
def apply_frequency_shift(signal, shift_factor):
    shifted = []
    for s in signal:
        shifted.append(s * (1.0 + shift_factor / 100))
    return shifted

# Main processing chain
def segment_signal(signal):
    mid = len(signal) // 2
    first_half = signal[:mid]
    second_half = signal[mid:]
    # Nested slicing with reversal (relevant)
    return [first_half[::-1], second_half[1:], second_half[:-1]]

# Encryption simulation using dictionary-based substitution
encryption_map = {i: ((i * 3) ^ 0x1F) % 256 for i in range(256)}
def encrypt_value(val, key):
    high_byte = (val >> 8) & 0xFF
    low_byte = val & 0xFF
    encrypted_high = encryption_map.get(high_byte, high_byte)
    encrypted_low = encryption_map.get(low_byte, low_byte)
    return (encrypted_high << 8) | encrypted_low

def decrypt_value(val, key):
    # Unused function - decoy
    return val

def process_transmission(chunks, key):
    flat_data = []
    for chunk in chunks:
        if len(chunk) > 3:
            # Use only specific slice
            segment = chunk[1:4]
            for item in segment:
                flat_data.append(item)
    # Apply encryption
    encrypted_values = [encrypt_value(v, key) for v in flat_data]
    # Aggregate using bitwise and arithmetic combination
    aggregate = 0
    for ev in encrypted_values:
        aggregate += (ev ^ 0x303) & 0xFFFF
    # Final scaling based on checksum (from original data)
    base_sum = sum(flat_data)
    correction = base_sum / (len(flat_data) + 1)
    final = (aggregate // 100) - int(correction)
    return final

# Orchestration
if __name__ == "__main__":
    # Step 1: Collect sensor data
    telemetry = collect_telemetry_data()  # Real data source
    
    # Step 2: Generate metadata (irrelevant)
    acquisition_time = 1678823400
    packet_id = "SAT-XII-8840"
    orbit_data = [calculate_orbit_decay(100)] * 5  # Dead-end computation
    
    # Step 3: Quantize signal values
    digital_signal = quantize_signal(telemetry)
    
    # Step 4: Segment into transmission chunks
    signal_chunks = segment_signal(digital_signal)
    
    # Step 5: Simulate encryption key (constant for determinism)
    encryption_key = 17
    
    # Step 6: Apply irrelevant frequency shift (result discarded)
    shifted_chunks = apply_frequency_shift(digital_signal, 2.5)
    
    # Step 7: Compute checksum for logging (not used in output but looks important)
    log_checksum = generate_checksum(telemetry)
    telemetry_metadata = {
        'length': len(telemetry),
        'checksum': log_checksum,
        'version': '2.1a'
    }
    
    # Step 8: Process final transmission (critical execution point)
    final_signal = process_transmission(signal_chunks, encryption_key)
    
    # Output result
    print(f"Result: {final_signal}")