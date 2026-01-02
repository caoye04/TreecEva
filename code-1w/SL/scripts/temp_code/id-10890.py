def analyze_pattern(sequence):
    return sum(1 for i in sequence if i % 3 == 0)

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return x > 0 and bin(x).count('1') % 2 == 0

# Distractor variables
temp_offset = 772
buffer_limit = 1024
dummy_mask = 0xFF

# Real configuration
class Config:
    def __init__(self):
        self.threshold = 42
        self.mode = 'adaptive'
        self.debug = False

def transform_entry(val, key):
    if isinstance(val, str):
        # Use string method (lower)
        processed = val.lower().replace(' ', '')
        return len(processed) if 'x' in processed else len(processed) * 2
    return val ** 2 if val < 50 else val - 10

def collect_diagnostics(data_list):
    stats = {"even_count": 0, "prime_hint": 0, "length_sum": 0}
    for item in data_list:
        if isinstance(item, int):
            stats["even_count"] += (item % 2 == 0)
            # Prime-like check (not exact primes, just a red herring)
            if item > 1 and all(item % n != 0 for n in range(2, int(item**0.5))):
                stats["prime_hint"] += 1
        elif isinstance(item, str):
            # Use string method (split)
            words = item.split(',')
            stats["length_sum"] += sum(len(w.strip()) for w in words)
    return stats

def filter_critical(entries, limit):
    # Bit manipulation red herring
    mask = (1 << 5) - 1
    result = []
    for e in entries:
        if isinstance(e, int) and (e & mask) == (limit & mask):
            result.append(e * 2)
    return result or [limit * 3]

def process_metrics(log_data, cfg):
    # Step 1: Transform values using mixed logic
    transformed = [transform_entry(v, k) for k, v in enumerate(log_data)]
    
    # Step 2: Collect diagnostic metadata (some used later)
    diagnostics = collect_diagnostics(transformed)
    
    # Step 3: Filter based on bitwise pattern (distractor)
    filtered = filter_critical(transformed, cfg.threshold)
    
    # Step 4: Analyze control pattern (irrelevant to final result)
    pattern_score = analyze_pattern(list(range(5, 30, 4)))
    
    # Step 5: Build frequency map of transformed numeric results
    freq_map = {}
    for v in transformed:
        if isinstance(v, int):
            freq_map[v] = freq_map.get(v, 0) + 1
    
    # Step 6: Compute weighted score based on frequencies and even count
    weight = 0
    for val, cnt in freq_map.items():
        if cnt > 1:
            weight += val // (cnt + 1)
    
    # Step 7: Apply conditional expression with string method distraction
    mode_factor = 2 if cfg.mode == 'adaptive' and any(isinstance(i, str) for i in log_data) else 1
    temp_string = "a,b,c,x,y,z"
    split_check = len(temp_string.split(','))  # distractor
    
    # Step 8: Final computation - combines weight, even_count, and threshold
    # Only this line matters for the answer
    final_diagnostic = weight + diagnostics["even_count"] * cfg.threshold // mode_factor
    
    # Dead code path with decoy assignment
    if final_diagnostic < 0:
        final_diagnostic = -1 * dummy_mask
    
    return final_diagnostic

# Main execution
config = Config()
log_data = [12, "user input", 45, "query,x1", 18, 27, "data reset", 36]
final_diagnostic = process_metrics(log_data, config)
print(f"Target result: {final_diagnostic}")