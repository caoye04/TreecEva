import math

# Simulated sensor data processing with red herrings and complex flow
def collect_readings():
    raw = [12, 15, 22, 8, 43, 31, 20, 18]
    offset = 7
    adjusted = [x + offset for x in raw]  # Irrelevant adjustment
    return raw

# Decoy transformation function that looks important but isn't used in critical path
def deprecated_filter(data):
    return [x for x in data if x > 15]

# Real transformation chain
def apply_window(signal):
    window = [0.25, 0.5, 0.75, 1.0, 0.75, 0.5, 0.25]
    padded = [0] * 3 + signal + [0] * 3
    filtered = []
    for i in range(len(signal)):
        val = sum(padded[i + j] * window[j] for j in range(7))
        filtered.append(round(val, 2))
    return filtered

# Bit manipulation distraction: simulates checksum but unused
def compute_legacy_checksum(arr):
    checksum = 0
    for num in arr:
        checksum ^= (num << 1) | (num >> 7)
    return checksum % 1000

# Sorting distraction with plausible but irrelevant analysis
def evaluate_stability(readings):
    sorted_vals = sorted(readings)
    variance_proxy = 0
    for i in range(1, len(sorted_vals)):
        variance_proxy += abs(sorted_vals[i] - sorted_vals[i-1])
    return variance_proxy // 3  # Red herring result

# Core recursive processing path
def recursively_compress(seq):
    if len(seq) <= 1:
        return seq[0] if seq else 0
    paired = [(seq[i] + seq[i+1]) // 2 for i in range(0, len(seq)-1, 2)]
    return recursively_compress(paired)

# Higher-order function distraction
create_analyzer = lambda base_shift: lambda x: [y + base_shift for y in x]
anomaly_detector = create_analyzer(3)  # Looks useful, never called

# Data enrichment with decoy fields
def enrich_dataset(clean_signal):
    timestamps = list(range(len(clean_signal)))
    metadata = {"version": "2.1", "source": "simulated", "active": True}
    records = []
    for t, val in zip(timestamps, clean_signal):
        record = {
            "ts": t,
            "value": val,
            "flags": 0,
            "derived": math.sqrt(val) if val > 0 else 0
        }
        records.append(record)
    return records

# Actual pattern analyzer using lambda and recursion
analyze_pattern = lambda data: sum(
    map(lambda x: x ** 2, 
        [recursively_compress(data[:4]), recursively_compress(data[4:])]
    )
)

# Main execution with multiple diversions
if __name__ == "__main__":
    readings = collect_readings()
    
    # Irrelevant stability check
    stability_score = evaluate_stability(readings)
    
    # Legacy checksum (dead computation)
    crypto_key = compute_legacy_checksum(readings)
    
    # Real signal processing begins
    processed = apply_window(readings)
    rounded_signal = [round(x) for x in processed]  # Smoothing
    
    # Enrichment step (distractor structure)
    enriched = enrich_dataset(rounded_signal)
    
    # Extract transformed data for actual analysis
    transformed_data = [int(rec["value"]) for rec in enriched] if enriched else rounded_signal
    
    # Critical statement containing answer
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Print required result
    print(f"Target result: {final_diagnostic}")