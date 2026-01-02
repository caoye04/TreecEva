def analyze_pattern(data):
    # Auxiliary calculation with distractions
    temp_sum = sum(x ** 0.5 for x in data if x % 2 == 0)
    offset = len([x for x in data if x > 10])
    adjusted = [x + offset for x in data]

    # Real computation begins
    filtered = [x for x in adjusted if x < 15]
    return filtered


def validate_sequence(seq):
    # Irrelevant validation logic (not actually used in final path)
    if not seq:
        return False
    cumulative = 0
    for i, val in enumerate(seq):
        cumulative += val
        if cumulative > 50:
            break
    return cumulative % 7 == 0


def process_segments(segments, thresholds):
    result = 0
    history = set()
    
    for i, seg in enumerate(segments):
        # Compute segment signature using XOR and index
        sig = 0
        for val in seg:
            sig ^= val + i
        
        # Track seen signatures (only some are used)
        history.add(sig)
        
        # Misleading control flow with early continue
        if sig < 5:
            result -= 1
            continue
        
        # Core logic: use threshold pairing via zip
        for t_idx, (seg_val, thresh) in enumerate(zip(seg, thresholds)):
            if seg_val >= thresh:
                # Apply bitwise adjustment
                adjusted_val = seg_val & (~thresh)  # Bitwise clear bits
                result += adjusted_val ^ t_idx     # XOR with position

        # Dead code: this condition never triggers due to data constraints
        if len(seg) > 100:
            fallback = sum(history) // len(history)
            result += fallback

    # Secondary processing on history set (distractor)
    extras = {h + 10 for h in history if h % 3 == 0}
    bonus = sum(extras) % 19 if extras else 0

    # Final adjustment: only depends on core result
    result += len(history) % 5
    return result

# Main execution
if __name__ == "__main__":
    segments = [
        [4, 7, 6],
        [8, 5],
        [6, 9, 7, 3]
    ]
    thresholds = [5, 6, 4]

    # Distraction: unused variable assignments
    snapshot = [sum(seg) for seg in segments]
    stats = {i: len(seg) for i, seg in enumerate(segments)}
    metadata = {"version": "2.1", "mode": "batch"}

    # Key data transformation
    cleaned = analyze_pattern([elem for sublist in segments for elem in sublist])
    
    # Validate (but unused return value)
    valid = validate_sequence(cleaned)

    # Critical statement
    result = process_segments(segments, thresholds)
    
    # Output target result
    print(f"Result: {result}")