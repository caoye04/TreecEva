import math

# Simulated sensor data and diagnostic system with heavy distractions
def preprocess_signal(raw):    
    temp_buffer = [x * 1.05 for x in raw if x > 0]  # Irrelevant amplification
    offset = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    normalized = [(x - offset) * 0.9 for x in temp_buffer]  # Distractor path
    return [abs(x) for x in raw]  # Actual relevant processing: take absolute values only

# Dead function - never called but looks important
def legacy_filter(sequence):
    return [x for x in sequence if x % 2 == 1]

# Auxiliary transformation that seems useful but isn't used in main flow
def frequency_shift(data, factor=2.1):
    return [math.sin(x * factor) for x in data]

# Real processing begins here — deceptively simple
transform = lambda x: x ** 2 if x > 1 else x + 1

def integrate_diagnostics(metrics):
    base_score = 0
    for val in metrics:
        if val > 2:
            base_score += int(math.log(val, 2))
        elif val == 2:
            base_score += 3
        else:
            base_score += 1
    return base_score

# Set operations used as distraction
def generate_reference_set(bounds):
    full_range = set(range(bounds[0], bounds[1]))
    exclusions = {x for x in full_range if x % 7 == 0}
    return full_range - exclusions  # Unused result

# Core analysis with misleading complexity
intermediate_flags = []
def flag_anomalies(seq):
    global intermediate_flags
    threshold = max(seq) * 0.6
    flags = []
    for i, x in enumerate(seq):
        if x > threshold and i % 2 == 0:
            flags.append(i * 2)
        elif x < 1:
            flags.append(-i)
    intermediate_flags = flags  # Side effect, but not used later
    return len(flags) > 0

# Main analyzer — depends only on specific transformations
def analyze_signal(data):
    # Step 1: Transform each element using lambda
    stage1 = [transform(x) for x in data]
    
    # Step 2: Filter only those above 1.5
    stage2 = [x for x in stage1 if x > 1.5]
    
    # Step 3: Map via custom logic
    mapped = []
    for x in stage2:
        if x > 4:
            mapped.append(int(x / 2))
        else:
            mapped.append(int(x))
    
    # Step 4: Use set to remove duplicates (critical step)
    unique_mapped = list(set(mapped))
    
    # Step 5: Sort and reverse
    unique_mapped.sort(reverse=True)
    
    # Step 6: Apply cumulative operation
    accum = 0
    for i, v in enumerate(unique_mapped):
        accum += v * (i + 1)
    
    # Step 7: Add checksum from unused components (but only fixed offset)
    checksum = 7  # Hardcoded red herring; looks like it should be computed
    
    # Final computation
    result = accum + checksum
    
    # Decoy branches below — never reached due to structure
    if len(unique_mapped) > 10:
        fallback = sum(unique_mapped) // 2
        return fallback  # Not triggered
    
    return result

# Irrelevant string processing block (distractor)
def encode_sequence(seq):
    binary_strings = [''.join('1' if (x >> i) & 1 else '0' for i in range(7,-1,-1)) for x in seq]
    flipped = [s[::-1] for s in binary_strings]
    hex_codes = [hex(int(f, 2))[2:] for f in flipped]
    upper_codes = [c.upper() for c in hex_codes]
    return ''.join(upper_codes)

# Unused recursive function — looks important
def recursive_reduce(n, acc=[]):
    if n <= 1:
        return acc
    acc.append(n // 2)
    return recursive_reduce(n // 2, acc)

# Global decoy variables
system_status = 'STANDBY'
calibration_data = {"gain": 1.02, "offset": -0.5, "active": False}
diagnostic_log = []

# Entry point
if __name__ == "__main__":
    # Initial sensor readings
    raw_sensor_input = [0.5, -1.2, 3.0, 4.5, -3.0, 2.1, 6.0, 1.8]
    
    # Preprocessing chain
    cleaned = preprocess_signal(raw_sensor_input)
    processed_data = [round(x, 2) for x in cleaned]  # Final input to analyzer
    
    # Diagnostic execution
    final_diagnostic = analyze_signal(processed_data)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")