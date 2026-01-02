def analyze_sequence(data):
    # Core diagnostic variables
    base_score = 0
    anomaly_penalty = 0
    redundancy_credit = 0

    # Irrelevant tracking (distractor)
    temporal_markers = []
    state_log = {}
    debug_trace = [0] * len(data)

    # Preprocess: character frequency analysis (partially relevant)
    char_freq = {}
    for c in data:
        char_freq[c] = char_freq.get(c, 0) + 1
    
    # Compute base score from uppercase letters (key path)
    for c in data:
        if c.isupper():
            base_score += ord(c) % 19

    # Anomaly detection: odd-positioned vowels trigger penalties (key path)
    vowels = 'aeiou'
    for i, c in enumerate(data):
        if c.lower() in vowels and i % 2 == 1:
            anomaly_penalty += 13

    # Redundancy credit for repeated lowercase (key path)
    last_char = ''
    for c in data:
        if c.islower() and c == last_char:
            redundancy_credit += 7
        last_char = c

    # === Distractor block: Dead logic path (never executed) ===
    def legacy_compat_mode(x):
        return x[::-1].encode('utf-8').hex()

    temp_result = []
    for i in range(len(data)):
        if i > len(data) * 2:  # Impossible condition
            temp_result.append(legacy_compat_mode(data[:i]))

    # === Misleading intermediate (looks important but unused) ===
    weighted_sum = 0
    for i, c in enumerate(data):
        weighted_sum += i * (ord(c) % 7)
    derived_factor = weighted_sum // max(len(data), 1)
    scaling_envelope = derived_factor * 2.5  # Never used

    # === Unused data structure manipulation ===
    history_map = {}
    for idx, ch in enumerate(data):
        key = f"item_{idx % 5}"
        if key not in history_map:
            history_map[key] = []
        history_map[key].append(ch.upper().replace('X', '_'))

    # === Real computation buried among distractions ===
    segment_product = 1
    valid_segments = 0
    for i in range(0, len(data) - 1, 3):
        if i + 1 < len(data):
            segment_product *= (ord(data[i]) - ord(data[i+1])) ** 2
            valid_segments += 1
    # Only used if valid_segments > 5, which it isn't in this case

    # === Key statement embedded in noise ===
    metadata_checksum = sum(ord(c) for c in data if c.isdigit())
    config_flag = len(char_freq) > 3
    final_diagnostic = base_score + anomaly_penalty - redundancy_credit

    # Final red herring: conditional that never fires
    if len(set(data)) == len(data) and False:  
        final_diagnostic = int(segment_product % 1000)

    # Output the actual answer
    print(f"Result: {final_diagnostic}")

# Input data with meaningful pattern
input_sequence = "BaaadBeefIdeaLoopsXYZ"
analyze_sequence(input_sequence)