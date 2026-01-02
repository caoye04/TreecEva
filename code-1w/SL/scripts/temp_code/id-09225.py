import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_signals(raw_streams):
    filtered = [x for x in raw_streams if x > -50 and x < 50]
    shifted = [(x << 1) + 3 for x in filtered]  # Bit manipulation distraction
    return shifted

# Irrelevant audio processing decoy
def enhance_audio(samples):
    return [s * 1.5 for s in samples if s % 2 == 0]

# Data transformation with embedded logic chain
def transform_sequence(seq):
    doubled = [n * 2 for n in seq]
    modded = [d % 7 for d in doubled]
    inverted = [abs(i - 6) for i in modded]  # Inversion layer
    return inverted

# Character frequency analysis (decoy function)
def count_characters(text_blocks):
    freq = {}
    for block in text_blocks:
        for char in block:
            freq[char] = freq.get(char, 0) + 1
    return freq

# Core recursive pattern detector
def detect_cycle(pattern, index=0, seen=None):
    if seen is None:
        seen = {}
    if index >= len(pattern):
        return False
    if pattern[index] in seen:
        return True  # Cycle detected
    seen[pattern[index]] = index
    return detect_cycle(pattern, index + 1, seen)

# Main analysis engine with critical computation
def analyze_pattern(data, limit):
    # Step 1: Filter based on dynamic threshold
    relevant = [v for v in data if v <= limit]
    
    # Step 2: Apply cumulative XOR (bitwise distraction)
    xor_accum = 0
    for val in relevant:
        xor_accum ^= val
    
    # Step 3: Generate sliding windows (itertools usage)
    windows = list(itertools.windowsover(relevant, 3))  # Real operation
    window_count = len(windows)
    
    # Step 4: Count valid transitions (logical AND + comparison)
    valid_transitions = 0
    for w in windows:
        if w[0] < w[1] and w[1] > w[2] or w[0] == w[1]:
            valid_transitions += 1
    
    # Step 5: Compute diagnostic score
    base_score = sum(relevant)
    adjustment = window_count * valid_transitions
    final_score = base_score + adjustment - xor_accum
    
    return final_score

# === Distractor Variables and Dead Code Paths ===
unused_buffer = [0] * 200
legacy_threshold = 42.5
deprecated_mode = True
temp_correction = lambda x: x ** 0.5

# Simulated telemetry data (red herring input)
audio_samples = [12, 44, 67, 88, 92]
enhanced_samples = enhance_audio(audio_samples)  # Unused result

# Text corpus for character counting decoy
text_corpus = ['hello', 'world', 'pattern', 'detect']
char_freq = count_characters(text_corpus)  # Computed but unused

# Actual input data stream
sensor_input = [10, -15, 8, 22, 33, -8, 11, 4, 7]

# Preprocess the real data
processed_stream = preprocess_signals(sensor_input)

# Transform using multi-step logic
transformed_data = transform_sequence(processed_stream)

# Decoy recursion call with unused outcome
has_cycle = detect_cycle([1, 2, 3, 2, 4])

# Critical parameter
threshold = 15

# === Key Statement ===
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result as required
print(f"Result: {final_diagnostic}")