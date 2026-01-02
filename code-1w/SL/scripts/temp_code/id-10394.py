import itertools
from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings and complex flow
def preprocess_signal(raw):    
    offset = 2023
    scale = 3
    processed = [(x * scale + offset) % 100 for x in raw if x > 0]
    return [x for x in processed if x % 2 == 1]

def generate_sequence(seed):
    # Irrelevant sequence generator (dead-end path)
    seq = []
    a, b = 1, seed
    for _ in range(10):
        a, b = b, a + b + seed % 3
        seq.append(a % 50)
    return seq

def filter_outliers(data, threshold=15):
    # Misleading filter that's not actually used
    counts = Counter(data)
    return [k for k, v in counts.items() if v >= threshold]

def transform_chars(text):
    # Distractor: character analysis not directly contributing to result
    char_freq = defaultdict(int)
    for c in text:
        if c.isalpha():
            char_freq[c.lower()] += 1
    sorted_chars = sorted(char_freq.items(), key=lambda x: (-x[1], x[0]))
    return ''.join([c for c, _ in sorted_chars[:5]])

def compute_checksum(arr):
    # Unused checksum calculation (red herring)
    chk = 0
    for i, val in enumerate(arr):
        chk ^= (val + i) * 3
    return chk % 1000

def analyze_pattern(data, cfg):
    # Core logic buried in distractions
    base = cfg['base_shift']
    mode = cfg['mode']
    accumulator = 0
    
    # Real computation starts here — masked by noise above
    for i, val in enumerate(data):
        temp = val ^ base  # XOR with base shift
        if i % 2 == 0:
            temp = temp * 2 % 97
        else:
            temp = (temp + 17) % 97
        
        # Conditional branching based on mode
        if mode == 'strict' and temp > 50:
            temp = temp // 2
        elif mode == 'relaxed':
            temp = min(temp + 10, 80)
        
        accumulator += temp * (i + 1)
    
    # Final transformation
    accumulator = (accumulator * 13) % 99991
    
    # This is the actual answer variable
    final_diagnostic = accumulator + len(data)
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Input data
    raw_sensor_readings = [4, -2, 8, 0, 15, 3, 7, -1, 12, 6, 9, 5]
    config_params = {
        'base_shift': 23,
        'mode': 'strict',
        'version': '2.1a',
        'debug': False
    }
    diagnostic_code = "ERRX-92837"

    # Irrelevant preprocessing steps (distractors)
    signal_sequence = generate_sequence(7)
    filtered_codes = filter_outliers(signal_sequence, threshold=3)
    computed_integrity = compute_checksum(signal_sequence)
    letter_key = transform_chars(diagnostic_code)

    # Actual relevant pipeline
    cleaned = preprocess_signal(raw_sensor_readings)
    enhanced = [x + 10 for x in cleaned if x < 80]  # minor transform
    shifted = [x ^ 5 for x in enhanced]  # bitwise interference
    transformed_data = list(itertools.accumulate(shifted, lambda a, b: (a + b) % 50))

    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, config_params)
    
    # Output required format
    print(f"Result: {final_diagnostic}")