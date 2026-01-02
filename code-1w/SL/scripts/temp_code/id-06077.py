import math

# Simulated sensor data and diagnostic system with heavy distractions
def generate_noise(length):
    return [math.sin(i * 0.5) + 0.5 * math.cos(i) for i in range(length)]

def apply_filter(signal, mode='low'):
    if mode == 'low':
        return [x * 0.9 for x in signal[:len(signal)//2]]
    else:
        return [abs(x) ** 0.5 for x in signal if x < 0]

def compute_entropy(data):
    # Irrelevant entropy calculation (dead end)
    freq_map = {}
    for d in data:
        freq_map[d] = freq_map.get(d, 0) + 1
    return -sum((freq / len(data)) * math.log2(freq / len(data)) 
                for freq in freq_map.values())

def extract_features(raw):
    # Distractor: complex feature extraction that isn't used
    features = []
    for i in range(1, len(raw)-1):
        delta = raw[i+1] - raw[i-1]
        if delta > 0.1:
            features.append(math.tanh(delta))
    return features or [0.0]

def validate_checksum(sequence):
    # Misleading validation not tied to final result
    checksum = sum(sequence[i] * (i + 1) for i in range(len(sequence)))
    return checksum % 7 == 0

def preprocess_input(raw_input):
    # Real preprocessing path
    cleaned = [x for x in raw_input if -2.0 <= x <= 2.0]
    normalized = [(x + 1.5) / 3.0 for x in cleaned]
    truncated = normalized[:100]
    return [round(x, 3) for x in truncated]

def transform_sequence(seq, key=1.0):
    # Unused transformation (red herring)
    return [math.exp(-x * key) for x in seq]

def count_transitions(data):
    # Decoy metric
    up = down = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]: up += 1
        elif data[i] < data[i-1]: down += 1
    return up - down

def analyze_signal(data):
    # Critical function containing key logic
    magnitude = sum(abs(x) for x in data)
    peak = max(data, default=0)
    base_score = magnitude * 100 + peak * 10
    
    # Conditional expression (required Python feature)
    adjustment = 5 if len(data) > 50 else -3
    
    # List comprehension (required Python feature)
    significant_components = [x for x in data if x > 0.5]
    
    enhancement = len(significant_components) * 2
    
    # Final computation chain
    intermediate = base_score + adjustment
    final_score = intermediate + enhancement
    
    # Early return simulation
    if final_score < 0:
        return 0
    
    return final_score

# --- Main execution with extensive interference ---

# Irrelevant constants
MAX_BUFFER_SIZE = 256
DEFAULT_TIMEOUT = 15.5
ACTIVE_CHANNELS = [1, 3, 4, 7]

# Generate realistic but distracting data
raw_sensor_stream = generate_noise(120)
noise_floor = compute_entropy(raw_sensor_stream)  # Computed but unused

# Apply real and fake processing
filtered_section = apply_filter(raw_sensor_stream, mode='low')
spurious_features = extract_features(filtered_section)  # Dead end

# Real processing path begins
primary_buffer = preprocess_input(raw_sensor_stream)

# Multiple irrelevant operations
checksum_valid = validate_checksum([int(x*10) for x in primary_buffer[::10]])
drift_analysis = count_transitions(primary_buffer)
dummy_transform = transform_sequence(primary_buffer, key=0.7)

# Key data structure used in answer
processed_data = primary_buffer  # This feeds into analyze_signal()

# Secondary distractor variables
system_state = 'NORMAL' if noise_floor > 3.0 else 'CALIBRATING'
active_filters = {i: f'filter_{i}' for i in ACTIVE_CHANNELS}

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

# Output required format
print(f"Result: {final_diagnostic}")