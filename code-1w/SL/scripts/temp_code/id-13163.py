from collections import defaultdict, Counter
import math

def generate_noise(length):
    # Irrelevant function: simulates noise but not used in critical path
    return [math.sin(i * 0.5) for i in range(length)]

def preprocess_sensor(signal_data):
    # Distractor-heavy preprocessing with dead paths
    temp_map = defaultdict(float)
    magnitude = 0
    for val in signal_data:
        if val > 50:
            magnitude += val ** 0.5
        elif val < 10:
            magnitude -= val
    # Dead code path (never executed due to logic above)
    if len(signal_data) > 1000:
        return [x / magnitude for x in signal_data if x != 0]
    return [x for x in signal_data if x > 5]  # Actual relevant filter

def transform_sequence(seq):
    # Complex-looking transformation with irrelevant components
    shifted = [(x << 2) & 255 for x in seq]  # Bit manipulation red herring
    normalized = [x / 16 for x in shifted if x % 2 == 0]
    stats = Counter(normalized)
    entropy = 0
    for freq in stats.values():
        if freq > 1:
            entropy += freq * math.log(freq)
    # Entropy calculated but unused
    return [int(x) for x in normalized]  # Only this matters

def validate_checksum(data):
    # Misleading validation that looks important but is bypassed
    checksum = 0
    for i, x in enumerate(data):
        checksum ^= (x + i) % 256
    return checksum == 128  # Never actually checked in flow

def integrate_phase(readings):
    # Nested logic with conditional expression and distractors
    accumulator = 0
    phase_shift = 1
    for idx, reading in enumerate(readings):
        if idx % 7 == 0:
            phase_shift = -1 if reading % 2 else 1
        adjusted = reading * phase_shift
        accumulator += adjusted
        # Early termination red herring
        if accumulator > 10000:
            break  # This never triggers
    return accumulator + len(readings)

def analyze_readings(signals):
    # Final analysis with conditional expression and subtle logic
    base_score = sum(signals) // len(signals) if signals else 0
    variation = max(signals) - min(signals) if len(signals) > 1 else 0
    
    # Conditional expression determining final output
    penalty = variation * 0.1 if variation > 50 else variation * 0.05
    
    # Key computation
    raw_diagnostic = base_score - int(penalty)
    
    # Multiple decoy variables
    diagnostic_log = []
    diagnostic_log.append(f'Base: {base_score}')
    diagnostic_log.append(f'Variation: {variation}')
    diagnostic_log.append(f'Penalty: {penalty}')
    
    # Final result derived from non-obvious combination
    final_diagnostic = raw_diagnostic + (len(diagnostic_log) // 2)
    
    # Unused complex structure
    report_summary = {
        'entries': len(signals),
        'outliers': len([x for x in signals if x > 75]),
        'stable': all(x < 100 for x in signals),
        'checksum_valid': False
    }
    
    return final_diagnostic

# Simulated sensor data (deterministic)
data_stream = list(range(15, 85, 3))  # 15, 18, 21, ..., 84

# Irrelevant transformations
noise_floor = generate_noise(len(data_stream))
filtered_outliers = [x for x in data_stream if x % 5 != 0]  # Unused

# Critical processing path
processed_signals = preprocess_sensor(data_stream)
sanitized_data = transform_sequence(processed_signals)
accumulated_phase = integrate_phase(sanitized_data)

# Key statement
final_diagnostic = analyze_readings(processed_signals)

# Print result
print(f"Result: {final_diagnostic}")