import math

def normalize_signal(x):
    # Irrelevant signal processing function (dead code path)
    return sum([i ** 0.5 for i in x if i > 0]) / len(x)

def decode_frame(frame):
    # Misleading decoding logic that isn't used in final computation
    decoded = []
    for c in frame:
        if c.isalpha():
            decoded.append(ord(c.lower()) - ord('a') + 1)
    return sum(decoded) % 17

def process_segment(data, factor):
    # Real but obfuscated transformation: applies bit manipulation and scaling
    temp_val = 0
    for i in range(len(data)):
        if i % 2 == 0:
            temp_val += (data[i] << 2) ^ factor
        else:
            temp_val -= (data[i] >> 1) & factor
    return abs(temp_val)

def segment_data(stream):
    # Splits raw byte stream into chunks – only some are used later
    chunk_size = 3
    chunks = [stream[i:i+chunk_size] for i in range(0, len(stream), chunk_size)]
    checksum = 0
    for c in chunks:
        if len(c) == 3:
            checksum ^= c[0] * c[1] + c[2]
    # Distraction: unused variable
    encoded_checksum = ''.join([chr((checksum % 26) + ord('A')) for _ in range(3)])
    return chunks  # Return all segments

def validate_purity(segments):
    # Core logic hidden among distractions: computes score based on XOR chain
    result = 0
    calibration_mask = 13
    debug_flags = set()
    
    for idx, seg in enumerate(segments):
        if len(seg) < 2:
            continue
        # Real operation: accumulates transformed values
        segment_value = seg[0] ^ seg[-1]
        if idx % 3 == 0:
            segment_value = segment_value ** 2
        else:
            segment_value = int(math.sqrt(abs(segment_value) + 1)) * (-1 if segment_value < 0 else 1)
        
        # Key update step (non-obvious due to surrounding noise)
        result ^= segment_value
        
        # Distractor: builds unused flag set
        if result > 100:
            debug_flags.add(f"high_alert_{idx}")
        elif result < -50:
            debug_flags.add(f"low_critical_{idx}")
    
    # Another red herring: string manipulation with no impact
    status_msg = "System " + "OK".lower() + " at " + str(len(debug_flags)) + " points"
    status_msg = status_msg.replace(" ", "_").upper()
    
    return result

# Simulated raw data stream – deterministic input
raw_stream = [12, 8, 4, 15, 30, 7, 21, 11]
calibration_factor = 5

# Dead function call – looks important but unused
signal_strength = normalize_signal(raw_stream)

# Unused decoding operation – misleading intermediate
frame_code = decode_frame('ZX19')

# Critical execution point: this line determines the answer
filtration_score = validate_purity(process_sequence(segment_data(raw_stream), calibration_factor))

# Helper function that was missing earlier – now defined
def process_sequence(chunks, mask):
    processed = []n    for chunk in chunks:
        modified = []
        for val in chunk:
            # Apply bitwise transformation masked by calibration
            new_val = (val ^ mask) & 0xFF
            if new_val % 2 == 0:
                new_val = new_val // 2
            modified.append(new_val)
        processed.append(modified)
    return processed

# Print final result as required
print(f"Result: {filtration_score}")