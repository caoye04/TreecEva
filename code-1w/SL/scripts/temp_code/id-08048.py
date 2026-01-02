def analyze_text_quality(text):
    if not text:
        return 0
    words = text.split()
    avg_length = sum(len(w) for w in words) / len(words) if words else 0
    upper_ratio = sum(1 for c in text if c.isupper()) / len(text)
    exclamation_score = text.count('!') * 10
    return avg_length * (1 - upper_ratio) + exclamation_score

# Irrelevant utility function (decoy)
def encrypt_data(data, key=3):
    return ''.join(chr((ord(c) + key) % 128) for c in data)

# Another decoy: network simulation (unused path)
def simulate_network_latency(size_mb):
    base = 20
    penalty = size_mb * 1.5
    jitter = 5
    return base + penalty + jitter

# Misleading preprocessing chain
def preprocess_record(record_str):
    clean = record_str.strip().lower()
    tokens = clean.split(',')
    parsed = [t.strip() for t in tokens]
    
    # Distraction: irrelevant transformations
    reversed_parts = [p[::-1] for p in parsed]
    encoded = [encrypt_data(p, 7) for p in parsed]
    
    # Only this part matters:
    try:
        values = [float(x) for x in parsed if x.replace('.', '').isdigit()]
    except:
        values = []
    return values

# Core logic buried in noise
def transform_dataset(raw_list):
    results = []
    for item in raw_list:
        if isinstance(item, str):
            nums = preprocess_record(item)
            if nums:
                # Real computation
                magnitude = max(nums) ** 0.5
                weight = len(nums) * 0.7
                score = magnitude * weight
                
                # Red herring: conditional that never triggers due to data
                if 'TEMP_FLAG_99' in item:
                    score *= 0.1  # dead path
                
                results.append(score)
        elif isinstance(item, list):
            # Alternate path: unused in actual input
            results.append(sum(item) / len(item))
    return results

# Distractor: complex but unused class
class DataNormalizer:
    def __init__(self, method='zscore'):
        self.method = method
        self.baseline = []
    
    def normalize(self, x):
        return x  # stub
    
    def batch_normalize(self, arr):
        mean_val = sum(arr) / len(arr)
        deviation = [(x - mean_val) for x in arr]
        return [d * 0.5 for d in deviation]

# Heavily obscured main pipeline
def calculate_final_score(input_data):
    # Step 1: Transform the data
    transformed = transform_dataset(input_data)
    
    # Step 2: Filter out low values (real logic)
    filtered = [x for x in transformed if x > 1.5]
    
    # Step 3: Apply decay factor based on length
    decay_factor = 0.95 ** len(transformed)
    adjusted = [val * decay_factor for val in filtered]
    
    # Step 4: Compute final metric
    if adjusted:
        raw_total = sum(adjusted)
        penalty = len(transformed) * 0.2
        bonus = analyze_text_quality("Signal detected!!!")  # uses '!'
        final = raw_total - penalty + bonus
    else:
        final = 0
    
    # Dead code branches with misleading variables
    debug_mode = False
    if debug_mode:  # never true
        print(f"Debug: {len(transformed)} items processed")
        audit_log = [f"item_{i}" for i in range(len(transformed))]
    
    temp_result = None
    if final > 100:
        temp_result = final / 2
    
    # Actual answer assignment
    final_score = int(round(final))
    return final_score

# Unused but plausible-looking initialization
config = {
    "version": "2.1-alpha",
    "timeout": 300,
    "debug_flags": ["TRACE_IO", "VERBOSE_PARSER"],
    "thresholds": {
        "critical": 90,
        "warning": 60
    }
}

# Input data designed to trigger specific paths
raw_input = [
    "sensor_1, 4.5, 8.2, 6.1, status_ok",
    "log_entry, 3.0, invalid_field, 9.8, 2.1",
    "error_404, no_data, 5.5, 7.3, 1.2, 8.8",
    "info, 2.3, 4.4, 6.6, 8.8, 10.1"
]

# Execution point of interest
final_score = calculate_final_score(raw_input)
print(f"Result: {final_score}")