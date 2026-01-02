from collections import defaultdict, Counter
import math

def preprocess_waveform(samples):
    # Irrelevant preprocessing step (not used in final result)
    normalized = [s / max(samples) for s in samples]
    filtered = [x for x in normalized if x > 0.1]
    return [math.sin(x * math.pi) for x in filtered]

def generate_sequence(length, base=3):
    # Distractor: generates Fibonacci-like sequence but unused
    seq = [1, 1]
    for i in range(2, length + 5):
        seq.append((seq[-1] + seq[-2]) % base)
    return seq

def detect_anomalies(log_entries):
    # Dead code path — never called
    counts = defaultdict(int)
    for entry in log_entries:
        counts[entry['type']] += 1
    return {k: v for k, v in counts.items() if v > 1}

def shift_pattern(pattern, offset):
    # Used in main logic
    return [pattern[(i - offset) % len(pattern)] for i in range(len(pattern))]

def evaluate_entropy(seq):
    # Misleading intermediate metric (looks important but isn't final)
    freq = Counter(seq)
    total = len(seq)
    entropy = -sum((count / total) * math.log2(count / total) for count in freq.values())
    return round(entropy, 6)

def integrate_phase(signal, phase_key):
    # Relevant transformation
    adjusted = []
    for i, val in enumerate(signal):
        adjusted.append(val * (phase_key ^ i) % 7)
    return sum(adjusted)

def analyze_signal(buffer, factor):
    # Core function with key logic
    if not buffer:
        return 0
    
    # Apply shift based on factor
    shifted = shift_pattern(buffer, factor % len(buffer))
    
    # Extract odd-positioned elements
    subset = [v for i, v in enumerate(shifted) if i % 2 == 1]
    
    # Transform using bit manipulation
    transformed = []
    for x in subset:
        temp = (x << 2) ^ 5
        if temp > 10:
            temp = temp // 3
        transformed.append(temp)
    
    # Final aggregation
    cumulative = 0
    for idx, val in enumerate(transformed):
        cumulative += val * (idx + 1)
    
    # Secondary adjustment using XOR folding
    hex_rep = hex(cumulative ^ factor)
    digit_sum = sum(int(c, 16) for c in hex_rep[2:] if c.isdigit())
    
    return cumulative + digit_sum

# Main execution flow
if __name__ == '__main__':
    # Input data
    raw_input = [4, 7, 2, 9, 5, 8]
    config_flag = 13
    calibration_factor = 17
    
    # Irrelevant operations (distractors)
    stats_log = [{'type': 'IO', 'time': t} for t in range(10, 30, 3)]
    _ = detect_anomalies(stats_log)
    
    # Unused sequence generation
    fib_mask = generate_sequence(10, base=5)
    
    # Real signal path
    pattern_buffer = []
    for i, val in enumerate(raw_input):
        if val % 2 == 0:
            pattern_buffer.append(val + i)
        else:
            pattern_buffer.append(val - (i % 3))
    
    # Another distraction: entropy calculation on modified buffer
    shifted_copy = shift_pattern(pattern_buffer, 2)
    _ = evaluate_entropy(shifted_copy)
    
    # Key statement
    final_diagnostic = analyze_signal(pattern_buffer, calibration_factor)
    
    # Print result
    print(f"Target result: {final_diagnostic}")