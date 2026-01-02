from collections import defaultdict, Counter
import math

def analyze_pattern(sequence):
    # Irrelevant helper function (dead code path)
    return sum(1 for a, b in zip(sequence, sequence[1:]) if a != b)

def transform_data(x):
    # Unused transformation (red herring)
    return int((x * 3.7 + 19) % 256)

def main():
    raw_samples = [18, 24, 15, 30, 27, 21, 9, 12, 33]
    
    # Distractor: complex but unused signal processing chain
    temp_cache = defaultdict(lambda: 0)
    for i, val in enumerate(raw_samples):
        temp_cache[f'idx_{i}'] = (val ** 2) % 17
    
    # Real computation begins: filtering significant signals
    threshold = 20
    strong_signals = [x for x in raw_samples if x > threshold]
    weak_signals = [x for x in raw_samples if x <= threshold]  # distractor
    
    # Bit manipulation red herring
    masked_values = []
    for s in strong_signals:
        masked = s & 0b1101  # irrelevant bit masking
        shifted = (masked << 2) | (s >> 3)  # decoy transformation
        masked_values.append(shifted)
    
    # String-based distraction
    status_flags = ['OK', 'ERR', 'OK', 'WARN', 'OK']
    flag_count = Counter(status_flags)  # collected but not used directly
    
    # Simulated calibration offset (unused)
    calibration_map = {}
    for i in range(5):
        calibration_map[f'level_{i}'] = round(math.sin(i * 0.5), 3)
    
    # Core logic disguised among distractions
    base_reference = 3
    normalized_signals = []
    for sig in strong_signals:
        # Actual normalization used in final result
        norm = sig / base_reference
        if norm.is_integer():
            normalized_signals.append(int(norm))
        else:
            normalized_signals.append(round(norm, 2))
    
    # Decoy list comprehension with string operations
    hex_labels = [f'SIG-{hex(x)[2:].upper()}' for x in raw_samples if x % 3 == 0]
    
    # Conditional expression with misleading branching
    mode = 'aggressive' if len(hex_labels) > 4 else 'conservative'
    adjustment_factor = 1.5 if 'a' in mode else 0.8  # never actually applied
    
    # Real processing function
    def process_readings(readings):
        total = 0
        for item in readings:
            if isinstance(item, int):
                total += item * 2
            elif isinstance(item, float):
                total += int(item)  # truncate and add
        # Inject fixed offset from unrelated calculation
        bonus = len([x for x in raw_samples if x % 3 == 0])  # count multiples of 3
        return total + bonus
    
    # Key assignment point
    final_diagnostic = process_readings(normalized_signals)
    
    # Dead code path: recursive distraction
    def recursive_trace(n, depth=0):
        if depth >= 3:
            return 0
        return n + recursive_trace(n // 2, depth + 1)
    
    # Unused final validation
    validation_checksum = 0
    for c in 'diagnostic_final_v1':
        validation_checksum += ord(c.lower()) % 7
    
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()