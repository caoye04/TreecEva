def analyze_pattern(seq):
    if not seq:
        return 0
    pivot = len(seq) // 2
    left = seq[:pivot]
    right = seq[pivot:]
    return (len(left) ^ len(right)) + analyze_pattern(left)


def validate_chunk(chunk):
    cleaned = ''.join(c for c in chunk if c.isalnum()).lower()
    if cleaned.startswith('err'):
        return None
    checksum = sum(ord(c) for i, c in enumerate(cleaned) if i % 2 == 0)
    return cleaned if checksum > 500 else None


def decode_sequence(raw):
    tokens = raw.split('|')
    segments = []
    temp_store = {}
    
    for idx, token in enumerate(tokens):
        stripped = token.strip()
        if len(stripped) < 3:
            continue
        processed = stripped.replace('*', '').replace('_', '')
        reversed_str = processed[::-1]
        
        # Irrelevant transformation branch (dead path)
        if 'debug' in processed.lower():
            debug_data = [ord(x) % 7 for x in processed]
            temp_store[idx] = sum(debug_data)

        segments.append(reversed_str)
    
    # Misleading aggregation
    total_length = sum(len(s) for s in segments)
    avg_pos = total_length / max(len(segments), 1) if segments else 0
    
    # Key distractor: unused complex computation
    decoy_result = 0
    for i in range(min(5, len(segments))):
        decoy_result += hash(segments[i]) % (i + 1) * 3
    
    return segments


def filter_active(items):
    active = []
    for item in items:
        if 'disable' not in item and 'null' not in item:
            active.append(item.upper())
    return active


def process_segments(chunks):
    validated = []
    for c in chunks:
        result = validate_chunk(c)
        if result:
            validated.append(result)
    
    # Red herring: complex but unused bitwise chain
    mask = 0
    for v in validated:
        mask ^= sum(ord(v[i]) << (i % 4) for i in range(0, min(6, len(v)), 2))
    mask = (mask & 0xFFFF) ^ (mask >> 16)
    
    # Actual logic begins here
    base_values = []
    for entry in validated:
        # Extract even-indexed chars, convert, and sum
        evens = [ord(char) for i, char in enumerate(entry) if i % 2 == 0]
        base_val = sum(evens) // len(evens) if evens else 0
        base_values.append(base_val)
    
    # Nested conditional logic with indirect influence
    adjusted = []
    for val in base_values:
        if val > 75:
            adjusted.append(val - 23)
        elif val > 60:
            adjusted.append(val + 12)
        else:
            adjusted.append(val * 2)
    
    # Final aggregation through recursive pattern analysis
    sequence_key = [x % 256 for x in adjusted]
    score_component = analyze_pattern(sequence_key)
    
    # Final score influenced by both length and recursive XOR depth
    final_score = score_component * len(validated) if validated else 0
    
    # Critical print for evaluation
    print(f"Result: {final_score}")
    return final_score

# Unused helper (distractor)
def merge_logs(log_list):
    combined = []
    for log in log_list:
        combined.extend(log.split(','))
    return list(set(combined))

# Setup fake data with mixed content
raw_input = "xYz*|Err_Invalid|null_chunk|AbC_def|*mNo_*|pQR_stu"

# Execution chain
chunks_raw = decode_sequence(raw_input)
filtered_parts = filter_active(chunks_raw)
validated_chunks = [c for c in chunks_raw if validate_chunk(c) is not None]  # re-validate for redundancy
final_score = process_segments(validated_chunks)
