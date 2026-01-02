def analyze_sensor_data(raw_stream, calibration_key):
    # Irrelevant preprocessing: character frequency analysis (distractor)
    char_freq = {}
    for char in raw_stream:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Misleading transformation: base-64 style encoding (dead path)
    encoded_hint = ''.join([chr((ord(c) % 26) + 97) for c in raw_stream[:10]])

    # Real data processing begins: extract numeric pulses
    numeric_pulses = [int(c) for c in raw_stream if c.isdigit()]
    
    # Decoy statistical analysis
    mean_pulse = sum(numeric_pulses) / len(numeric_pulses) if numeric_pulses else 0
    variance_proxy = sum((x - mean_pulse) ** 2 for x in numeric_pulses) / len(numeric_pulses) if numeric_pulses else 0

    # Critical signal filtering using bitwise masking (relevant)
    filtered_signals = []
    mask = calibration_key & 0xFF
    for i, val in enumerate(numeric_pulses):
        if i % 3 == 0:
            processed = val ^ mask  # XOR with key fragment
            filtered_signals.append(processed)

    # Secondary decoy: string-based pattern search
    pattern_match_count = 0
    for i in range(len(raw_stream) - 3):
        if raw_stream[i:i+4] == 'X9Z1':
            pattern_match_count += 1

    # Real aggregation: sum of filtered signals above threshold
    significant_readings = [x for x in filtered_signals if x > 5]
    aggregate_score = sum(significant_readings)

    # Use of enumerate and zip: position-weighted adjustment (relevant)
    weights = [i+1 for i in range(len(significant_readings))]
    weighted_offsets = []
    for idx, (val, weight) in enumerate(zip(significant_readings, weights)):
        weighted_offsets.append(val * weight)
    
    # Another distraction: unused recursive function
    def recursive_trace(n):
        if n <= 1:
            return 1
        return recursive_trace(n-1) + recursive_trace(n-2)
    
    # Unused complex structure
    class DiagnosticFrame:
        def __init__(self, code, level):
            self.code = code
            self.level = level
    
    frame_stack = [DiagnosticFrame(f'F{i}', i*10) for i in range(len(numeric_pulses))]

    # Correction factor derived from calibration key properties
    key_digit_sum = sum(int(d) for d in str(calibration_key) if d.isdigit())
    parity_flag = bin(calibration_key).count('1') % 2
    correction_factor = key_digit_sum * (1 if parity_flag else -1)

    # Final computation (key statement)
    final_diagnostic = aggregate_score + correction_factor

    # Red herring: irrelevant print simulation
    debug_log = f'DIAG: {len(filtered_signals)} signals, offset {correction_factor}'

    # Actual output
    print(f'Target result: {final_diagnostic}')

# Execute with realistic inputs
data_stream = 'A7B9C3X9Z1D5E8F2G1H6'
key = 24681
analyze_sensor_data(data_stream, key)