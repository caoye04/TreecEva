import itertools

def analyze_frequency(segment):
    # Irrelevant helper: counts frequency but only used for distraction
    freq = {}
    for ch in segment:
        freq[ch] = freq.get(ch, 0) + 1
    avg_freq = sum(freq.values()) / len(freq) if freq else 0
    return avg_freq

def extract_patterns(sequence):
    # Extracts consecutive repeating characters - semi-relevant
    patterns = []
    for k, g in itertools.groupby(sequence):
        group_len = len(list(g))
        if group_len > 1:
            patterns.append((k, group_len))
    return patterns

def validate_checksum(seq):
    # Dummy validation: computes a checksum but not actually needed
    checksum = 0
    for i, char in enumerate(seq):
        checksum += ord(char) * (i + 1)
    checksum %= 97
    return checksum == 42  # Never true in practice here, red herring

def process_sequence(stream):
    temp_buffer = []
    total_chars = 0
    repeated_segments = 0
    dummy_accumulator = 0  # Dead variable

    for i in range(0, len(stream), 3):
        chunk = stream[i:i+3]
        
        # Distraction: frequency analysis on each chunk
        _ = analyze_frequency(chunk)
        
        # Real logic begins: track total character count
        total_chars += len(chunk)
        
        # Check for repeating patterns in chunks
        patterns = extract_patterns(chunk)
        if patterns:
            repeated_segments += 1
        
        # More distraction: attempt validation that does nothing
        _ = validate_checksum(chunk)
        
        # Accumulate something irrelevant
        for c in chunk:
            dummy_accumulator += ord(c) % 7
    
    # Core computation buried in noise
    base_score = total_chars * repeated_segments
    
    # Additional layer: count how many times 'x' appears across all chunks
    x_positions = [i for i, c in enumerate(stream) if c == 'x']
    x_correction = len(x_positions) if x_positions else 0
    
    # Final logic: combine base score with position-based adjustment
    adjustment = 0
    for pos in x_positions:
        adjustment += (pos % 4) + 1
    
    final_count = base_score + x_correction - adjustment
    
    # Print required result
    print(f"Result: {final_count}")
    return final_count

data_stream = "axxbbccxddeexffgxhhixjklllxmmnno"
final_count = process_sequence(data_stream)