import math

# Simulated sensor array diagnostics with heavy interference

def collect_readings():
    raw_samples = [i * 0.7854 for i in range(1, 17)]
    offset = 0.123
    adjusted = [math.sin(x + offset) for x in raw_samples]
    return adjusted

# Irrelevant auxiliary function (dead code path)
def legacy_calibrate(data):
    scale_factor = 1.05
    return [x * scale_factor - 0.01 for x in data[:8]]

# Decoy transformation with misleading intermediate result
def false_transform(seq):
    temp_vals = [abs(math.cos(x)) ** 2 for x in seq]
    checksum = sum(temp_vals) / len(temp_vals)
    # This looks important but is never used
    derived_key = int(checksum * 1000) % 97
    return [v * 0.9 for v in temp_vals]

# Actual preprocessing step (relevant)
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    normalized = [x - mean_val for x in signal]
    squared_sum = sum(x*x for x in normalized)
    if squared_sum > 0:
        return [x / math.sqrt(squared_sum) for x in normalized]
    return normalized

# Unused complex structure (distractor)
class DiagnosticBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0.0] * size
        self.index = 0

    def push(self, val):
        self.buffer[self.index] = val
        self.index = (self.index + 1) % self.size

    def get_stats(self):
        return {
            'min': min(self.buffer),
            'max': max(self.buffer),
            'avg': sum(self.buffer) / self.size
        }

# Bit manipulation red herring
def encode_flags(status_code):
    flag_set = 0
    flag_set |= (status_code & 1) << 3
    flag_set |= (status_code & 2) << 1
    flag_set |= (status_code & 4) >> 1
    # Complex-looking but unused
    return flag_set ^ 0b1010

# Data transformation chain (relevant)
def transform_readings(readings):
    # Apply windowing function
    windowed = [readings[i] * (1 - math.cos(2 * math.pi * i / len(readings))) for i in range(len(readings))]
    # Filter out every third element (decimation)
    filtered = [windowed[i] for i in range(len(windowed)) if i % 3 != 2]
    # Downsample and scale
    downsampled = [filtered[i] for i in range(0, len(filtered), 2)]
    return [x * 2.5 for x in downsampled]

# Core processing logic (relevant)
def analyze_pattern(sequence):
    if len(sequence) < 4:
        return 0.0
    
    # Compute pairwise products
    products = [sequence[i] * sequence[i+1] for i in range(len(sequence)-1)]
    
    # Find peaks above threshold
    threshold = sum(products) / len(products) * 0.5
    peaks = [p for p in products if p > threshold]
    
    # Weighted contribution
    total = 0.0
    for i, p in enumerate(peaks):
        weight = math.exp(-i * 0.3)
        total += p * weight
    
    return total

# Main processing pipeline (relevant)
def process_metrics(data, config):
    stage1 = [x * config['gain'] for x in data]
    stage2 = [math.tanh(x) for x in stage1]
    
    # Conditional enhancement
    if config['enhance']:
        enhanced = []
        for i in range(len(stage2)):
            if i > 0 and i < len(stage2) - 1:
                neighbor_avg = (stage2[i-1] + stage2[i+1]) / 2
                enhanced.append(stage2[i] * 1.2 if stage2[i] > neighbor_avg else stage2[i] * 0.8)
            else:
                enhanced.append(stage2[i])
        stage2 = enhanced
    
    # Final integration
    integrated = sum(x * (0.9 ** i) for i, x in enumerate(reversed(stage2)))
    return round(integrated * 1000) / 1000

# Global configuration (mixed relevant/irrelevant parameters)
config = {
    'gain': 1.7,
    'enhance': True,
    'sampling_rate': 44100,
    'buffer_size': 2048,
    'timeout_ms': 500,
    'debug_mode': False,
    'calibration_cycle': 3
}

# Auxiliary computation (distractor)
reference_map = {i: math.log(i + 1) for i in range(1, 13)}
sync_matrix = [[i*j % 7 for j in range(4)] for i in range(4)]
trace_checksum = sum(sum(row) for row in sync_matrix) % 101

# Primary execution flow
if __name__ == "__main__":
    # Step 1: Collect raw data
    raw_input = collect_readings()
    
    # Step 2: Normalize signal (relevant)
    normalized_input = normalize_signal(raw_input)
    
    # Step 3: Transform readings (relevant)
    transformed_data = transform_readings(normalized_input)
    
    # Step 4: Run false analysis (red herring - result ignored)
    dummy_results = false_transform(raw_input)
    anomaly_score = sum(dummy_results) / len(dummy_results)
    
    # Step 5: Generate unused diagnostic buffer
    diag_buffer = DiagnosticBuffer(8)
    for val in raw_input[:8]:
        diag_buffer.push(val * 0.01)
    
    # Step 6: Compute irrelevant encoded flags
    system_status = 5
    encoded_diagnostics = encode_flags(system_status)
    
    # Step 7: Perform actual metric processing (key statement)
    final_diagnostic = process_metrics(transformed_data, config)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")