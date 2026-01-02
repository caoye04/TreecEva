def preprocess_sequence(seq, mode='fast'):
    """Irrelevant preprocessing function for signal smoothing (dead code path)."""
    return [x * 0.95 for x in seq if x > 0]


def generate_checksum(data):
    """Decoy function: computes sum of squares but not used in main logic."""
    return sum(x ** 2 for x in data) % 1000


def validate_frame(frame):
    """Misleading validation check with unused result."""
    if len(frame) < 4:
        return False
    running_sum = 0
    for i in range(len(frame)):
        running_sum += frame[i] * (i + 1)
    return running_sum % 17 == 0


def count_transitions(signal):
    """Count zero-crossing transitions in signal."""
    if not signal:
        return 0
    transitions = 0
    for i in range(1, len(signal)):
        if (signal[i-1] < 0 <= signal[i]) or (signal[i-1] >= 0 > signal[i]):
            transitions += 1
    return transitions


def extract_features(raw_data, scale=1.0):
    """Apply scaling and extract magnitude peaks."""
    scaled = [int(x * scale) for x in raw_data]
    peaks = []
    for i in range(1, len(scaled) - 1):
        if scaled[i] > scaled[i-1] and scaled[i] > scaled[i+1]:
            peaks.append(scaled[i])
    return peaks


def analyze_signal(buffer, limit):
    """Core function: compute weighted diagnostic score based on feature set."""
    # Extract key features
    peak_magnitudes = extract_features(buffer, scale=1.8)
    total_energy = sum(abs(x) for x in buffer)
    
    # Compute transition count (used later)
    zero_crossings = count_transitions(buffer)
    
    # Irrelevant transformation chain
    temp_frame = [abs(x) ** 2 for x in buffer]
    temp_frame = [y for y in temp_frame if y > 5]
    temp_frame = [z // 2 for z in temp_frame]
    
    # Dummy checksum (distractor)
    _ = generate_checksum(temp_frame)
    
    # Simulate frame validation (result ignored)
    _ = validate_frame(temp_frame)
    
    # Character counting analog: convert energy to string and count even digits
    energy_str = str(int(total_energy))
    even_digit_count = sum(1 for c in energy_str if c in '02468')
    
    # Apply combinatorics: number of ways to choose 2 peaks from peak_magnitudes
    n_peaks = len(peak_magnitudes)
    peak_pairs = (n_peaks * (n_peaks - 1)) // 2 if n_peaks >= 2 else 0
    
    # Modular arithmetic on zero crossings
    modulated_transitions = (zero_crossings * 7) % 13
    
    # Main diagnostic formula (depends on multiple derived values)
    base_score = total_energy * 0.3
    peak_bonus = peak_pairs * 2.5
    transition_weight = modulated_transitions * 1.7
    digit_penalty = even_digit_count * 1.2
    
    intermediate_result = base_score + peak_bonus + transition_weight - digit_penalty
    
    # Final threshold adjustment
    if intermediate_result > limit:
        final_score = intermediate_result * 0.85
    else:
        final_score = intermediate_result * 1.15
    
    return int(final_score)

# Main execution block
if __name__ == '__main__':
    # Simulated sensor input (real data source)
    signal_stream = [-3, -1, 4, 7, -2, 5, 8, -6, 1, 9, -4, -2, 6]
    
    # Dead variables: irrelevant transformations
    normalized = [round(x / max(map(abs, signal_stream)), 2) for x in signal_stream]
    inverted = [x * -1 for x in signal_stream]
    filtered = [x for x in signal_stream if x % 2 != 0]
    
    # Unused pattern construction (string method red herring)
    pattern_str = ''.join([str(abs(x)) for x in signal_stream])
    masked_str = pattern_str.replace('4', 'X').replace('9', 'Y')
    char_frequency = {c: masked_str.count(c) for c in set(masked_str)}
    
    # Buffer assignment (relevant)
    pattern_buffer = [x * 2 for x in signal_stream if x != -2]  # Filter out -2
    
    # Threshold computation with distraction
    base_threshold = len(signal_stream) * 3
    offset = sum(1 for x in signal_stream if x > 0)
    decoy_threshold = (base_threshold + offset * 2) * 0.7
    threshold_level = base_threshold - offset  # Actual used value
    
    # Critical statement
    final_diagnostic = analyze_signal(pattern_buffer, threshold_level)
    
    # Print target result
    print(f"Result: {final_diagnostic}")