import itertools

# Simulated bio-signal processing pipeline with red herrings
def preprocess_signal(raw_signal):
    filtered = [x for x in raw_signal if abs(x) > 0.5]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    return normalized

# Distractor function: not actually used in final computation
def deprecated_analysis(data):
    return sum(x ** 2 for x in data if x < 0.5)

# Core transformation function used in critical path
def apply_window(signal, window_size=4):
    windows = [signal[i:i+window_size] for i in range(len(signal)-window_size+1)]
    return [sum(w) / len(w) for w in windows]

# Decoy diagnostic using irrelevant metrics
def false_diagnostic(signal):
    peaks = sum(1 for i in range(1, len(signal)-1) if signal[i-1] < signal[i] > signal[i+1])
    roughness = sum(abs(signal[i+1] - signal[i]) for i in range(len(signal)-1))
    return peaks * 0.3 + roughness * 0.01

# Critical pattern analyzer (used in final result)
def analyze_pattern(seq, limit):
    # Generate all possible triplets using itertools
    triplet_combinations = list(itertools.combinations(seq[:6], 3))
    valid_patterns = 0
    for combo in triplet_combinations:
        a, b, c = sorted(combo)
        if b - a > 0.1 and c - b < 0.15 and (a + b + c) % 1 < 0.5:
            valid_patterns += 1
    
    # Misleading intermediate calculation (dead end)
    _temp_score = valid_patterns * 1.5
    adjustment = 0.0
    if valid_patterns > 10:
        adjustment = 0.25
    elif valid_patterns > 5:
        adjustment = 0.1
    else:
        adjustment = -0.05  # Unused branch

    # Final logic step: only this affects the answer
    base = valid_patterns * 7
    if limit > 0.3:
        base += 3
    else:
        base -= 2
    
    # Additional interference: unused conditional expression
    status_flag = 'high' if base > 20 else ('medium' if base > 10 else 'low')
    _aux_value = base if status_flag == 'high' else (base * 1.1)

    return int(base)

# Irrelevant data structure
system_log = {
    'timestamp': '2023-11-05',
    'user': 'researcher_02',
    'access_level': 'diagnostic',
    'cached_results': [12, 15, 17, 23],
    'last_run': None
}

# Unused recursive distractor
def recursive_distractor(n):
    if n <= 1:
        return 1
    return recursive_distractor(n-1) + recursive_distractor(n-2)

# Main execution flow
raw_input_stream = [0.1, 0.7, 0.3, 0.8, 0.6, 0.9, 0.2, 0.55, 0.75, 0.85]
denoised_signal = preprocess_signal(raw_input_stream)
transformed_data = apply_window(denoised_signal, window_size=3)

# Dead code path assignment
unused_intermediate = false_diagnostic(denoised_signal)

# Key control flow with conditional expression distraction
temp_limit = 0.35 if len(transformed_data) > 5 else 0.25
threshold = temp_limit > 0.3 and temp_limit or 0.2  # Conditional expression trick

# Actual critical statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print required result
print(f"Result: {final_diagnostic}")