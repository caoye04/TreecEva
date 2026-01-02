from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise injection
def generate_noisy_signals(base_frequency, duration):
    signals = []
    for t in range(duration):
        clean_signal = int(math.sin(t * base_frequency) * 100)
        noise = (t ^ 0xABC) & 0xF
        signals.append(clean_signal + noise - 8)
    return signals

# Irrelevant helper - simulates temperature drift (not used in final result)
def calculate_thermal_drift(samples):
    drift = 0
    for i, s in enumerate(samples):
        if i % 3 == 0:
            drift += (s >> 2) ^ 7
    return abs(drift) % 500

# Misleading transformation - appears important but unused
def encrypt_sequence(seq, key):
    encrypted = []
    for val in seq:
        masked = (val ^ key) & 0xFF
        rotated = ((masked << 3) | (masked >> 5)) & 0xFF
        encrypted.append(rotated)
    return encrypted

# Core analysis function with distractors
def preprocess_signals(raw_signals):
    filtered = []
    outlier_count = 0
    running_checksum = 0
    
    for val in raw_signals:
        # Distraction: checksum accumulation with bit tricks
        running_checksum = (running_checksum ^ val) << 1
        if running_checksum > 10000:
            running_checksum = running_checksum % 997
            
        # Actual filtering logic
        if -120 < val < 120 and abs(val) % 7 != 0:  # Real filter condition
            filtered.append(abs(val) & 0x7F)  # Keep only lower 7 bits
        else:
            outlier_count += 1
            
    # Dead code path - never accessed due to prior filtering
    if outlier_count > 100:
        backup = [x | 0x80 for x in filtered]
        return backup
        
    return filtered

# Data aggregation with red herring structure
def group_by_phase(data):
    groups = defaultdict(list)
    phase_key = 0
    
    for d in data:
        phase_key = (phase_key + d) & 0x3
        groups[f'phase_{phase_key}'].append(d)
        
    # Irrelevant statistic
    sizes = [len(groups[k]) for k in groups]
    avg_size = sum(sizes) / len(sizes) if sizes else 0
    
    # Return all values sorted - actual use in next step
    combined = []
    for k in sorted(groups.keys()):
        combined.extend(sorted(groups[k], reverse=True))
    return combined

# Decoy analysis function - looks sophisticated but unused
def spectral_analysis(dataset):
    spectrum = defaultdict(int)
    for i in range(len(dataset) - 1):
        delta = dataset[i+1] - dataset[i]
        freq_bin = (delta * 3) ^ 0x15
        spectrum[freq_bin] += 1
    return dict(spectrum)

# Main pattern analyzer - this IS used
def analyze_pattern(processed_data, secret_offset):
    # Initialize multiple accumulators (some are distractions)
    entropy = 0.0
    trend_score = 0
    bit_population = 0
    cycle_detection = []
    
    # Real logic: sliding window XOR pattern detection
    for i in range(0, len(processed_data) - 2, 3):
        a, b, c = processed_data[i], processed_data[i+1], processed_data[i+2]
        
        # Meaningful transformation
        fused = (a ^ b) | c
        shifted = (fused << 2) & 0xFF
        adjusted = (shifted + secret_offset) % 256
        
        # Update real accumulator
        trend_score += adjusted
        
        # Distractor: entropy calculation that's never used
        binary_str = bin(adjusted).count('1')
        if binary_str > 0:
            prob = binary_str / 8
            entropy -= prob * math.log2(prob)
        
        # Red herring: cycle tracking with unused logic
        if len(cycle_detection) < 3:
            cycle_detection.append(adjusted % 16)
    
    # Secondary processing: count digit patterns (distraction)
    counter = Counter(str(trend_score))
    most_common_digit = counter.most_common(1)[0][1]
    
    # Final computation - depends only on trend_score and offset
    validation_key = (trend_score ^ secret_offset) & 0xFFFF
    confidence = validation_key % 89
    
    # The real answer derivation
    final_value = (validation_key + confidence) // 7
    
    # Dead return branch
    if final_value < 0:
        return bit_population  # Never reached
        
    return final_value

# Orchestration function with setup distractions
def run_diagnostics():
    # Generate primary signal data
    collected_signals = generate_noisy_signals(0.3, 256)
    
    # Irrelevant pre-checks
    null_count = sum(1 for x in collected_signals if x == 0)
    if null_count > 10:
        temp_adj = calculate_thermal_drift(collected_signals)
    
    # Real preprocessing path
    cleaned = preprocess_signals(collected_signals)
    
    # Misleading intermediate output
    dummy_hash = sum((i * v) ^ 0x55 for i, v in enumerate(cleaned[::4])) % 10000
    
    # Signal grouping - actually used
    arranged = group_by_phase(cleaned)
    
    # Unused spectral check
    if len(arranged) > 50:
        _ = spectral_analysis(arranged)
    
    # Critical encryption path that looks important but is bypassed
    system_key = 0xCAFE
    protected = encrypt_sequence(arranged, system_key)  # Computed but unused
    
    # ACTUAL critical analysis on ORIGINAL processed data
    final_diagnostic = analyze_pattern(collected_signals, system_key)
    
    # Multiple print statements with misleading labels
    print(f"Signal integrity: {dummy_hash}")
    print(f"Phase coherence: {sum(arranged[:5])}")
    print(f"Target result: {final_diagnostic}")

# Execute main process
run_diagnostics()