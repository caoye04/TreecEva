def preprocess_signal(raw):    
    # Irrelevant transformation
    normalized = [x * 0.95 for x in raw if x > 0]
    offset = sum(normalized) / len(normalized) if normalized else 0
    shifted = [x - offset for x in normalized]
    return shifted

# Distractor data
test_sequence = [120, -50, 30, 40, 50, -60, 70]
dummy_mask = [1 if x % 2 == 0 else 0 for x in range(15)]

# Real processing chain starts here
def encode_stream(data):
    filtered = [x for x in data if x > 25]
    squared = [x ** 2 for x in filtered]
    modded = [x % 19 for x in squared]
    return modded

def evaluate_stability(values):
    if not values:
        return 0
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return int(variance * 0.75)

flags = {'mode': 'strict', 'version': 2, 'debug': False}

# Another red herring function
def simulate_legacy_system(x):
    temp = 0
    for i in range(8):
        temp ^= (x + i) * 3
    return temp >> 2

# Core logic disguised among noise
auxiliary_buffer = []
for i in range(7):
    val = (i * i * 11) % 103
    auxiliary_buffer.append(val * 2 if val % 2 == 0 else val)

primary_input = [11, 13, 17, 19, 23, 29]
processed = preprocess_signal(primary_input)
encoded_data = encode_stream(processed)

# Decoy computation with string distraction
decoys = ['error', 'warning', 'info']
log_entry = ''.join([tag[0].upper() for tag in decoys])  # 'EWI'
count_chars = len(log_entry) * 100  # 300, irrelevant

# More misdirection
checksum = 0
for item in dummy_mask[:10]:
    checksum = (checksum * 31 + item) % 1000

# Conditional red herring
if flags['version'] > 1:
    adjustment = simulate_legacy_system(42)
else:
    adjustment = 1

# Actual critical computation path
def aggregate_metrics(seq, config):
    base = sum(seq)
    
    # String method used as distraction but also minor role
    mode_key = config['mode'].strip().lower()
    modifier = 2 if 'strict' in mode_key else 1
    
    # Bitwise mix with irrelevant shift
    masked_sum = base & 0xFF
    shifted_back = (masked_sum << 1) >> 1  # Canceling shifts
    
    # Real contribution: comparison and conditional arithmetic
    threshold = 40
    above_count = sum(1 for x in seq if x > threshold)
    
    # Critical calculation
    stability_score = evaluate_stability(seq)
    
    # Final composition with distractor operations
    temp_result = shifted_back + stability_score
    if above_count >= 2:
        temp_result *= modifier
    
    # Dead code branch (never reached due to data)
    if config.get('debug') and len(seq) < 5:
        temp_result -= 500  # never executed
    
    return temp_result

# Key assignment statement
final_diagnostic = aggregate_metrics(encoded_data, flags)

Result: {final_diagnostic}