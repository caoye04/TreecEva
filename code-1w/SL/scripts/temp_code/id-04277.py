def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def compute_entropy(s):
    from math import log2
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    total = len(s)
    entropy = 0
    for f in freq.values():
        p = f / total
        entropy -= p * log2(p)
    return round(entropy, 3)

# Unused transformation (dead code path)
def transform_data(arr):
    return [x ** 2 + 3 * x + 1 for x in arr if x % 2 == 0]

# Misleading statistical summary
def get_summary_stats(values):
    avg = sum(values) / len(values)
    peak = max(values)
    trough = min(values)
    spread = peak - trough
    # Distractor: returns multiple values, but only one used later
    return {
        'mean': avg,
        'high': peak,
        'low': trough,
        'range': spread,
        'median_guess': (peak + trough) / 2
    }

# Core logic obscured by noise
def filter_outliers(data, limit):
    clean = []
    for item in data:
        if isinstance(item, str):
            # String cleaning distraction
            cleaned_str = item.strip().lower().replace('_', '').replace('-', '')
            if cleaned_str.startswith('err') or len(cleaned_str) == 0:
                continue
            # Use string length as proxy (subtle but valid)
            clean.append(len(cleaned_str))
        elif isinstance(item, (int, float)):
            if abs(item) <= limit:
                clean.append(item)
    return clean

# Recursive signal extraction (critical path)
def extract_signals(logs, depth=0):
    if depth >= 3 or not logs:
        return [len(logs)]
    result = []
    for entry in logs:
        if isinstance(entry, list):
            nested = extract_signals(entry, depth + 1)
            result.extend(nested)
        elif isinstance(entry, dict):
            if 'signal' in entry and entry.get('active', False):
                result.append(entry['signal'])
    return result if result else [0]

# Main evaluation with hidden dependency on string processing
def evaluate_performance(log_entries, threshold):
    # Step 1: Filter raw entries
    filtered = filter_outliers(log_entries, threshold * 2)
    
    # Step 2: Extract recursive signals (key step)
    raw_signals = extract_signals(log_entries)
    signal_total = sum(raw_signals)
    
    # Step 3: Analyze pattern in derived metrics (real computation)
    pattern_data = [signal_total, len(filtered), threshold, len(str(threshold))]
    peaks = analyze_pattern(pattern_data)
    
    # Step 4: Apply conditional adjustment based on string-derived trait
    str_indicator = "performance_check".upper().replace('_', '').isupper()  # always True
    bonus = 5 if str_indicator else 0
    
    # Step 5: Use string method to determine multiplier
    trigger_word = "critical_alert"
    multiplier = 2 if 'alert' in trigger_word.split('_') else 1
    
    # Step 6: Final composition
    base_score = signal_total + peaks * 10 + bonus
    adjusted_score = base_score * multiplier
    
    # Step 7: Red herring normalization (unused)
    max_possible = 1000
    normalized = adjusted_score / max_possible
    
    # Step 8: Final output (this is the answer)
    final_score = int(adjusted_score)
    
    # Dead code: complex sorting that does nothing
    dummy_list = [3, 1, 4, 1, 5]
    dummy_list.sort(reverse=True)
    sorted_ascii = [ord(c) for c in trigger_word if c.isalpha()]
    sorted_ascii.sort()
    
    return final_score

# Setup input with mixed types and distractions
data_log = [
    10, -5, 20,
    ["ERR_NULL", "warn_retry", "info_ready"],
    {"signal": 7, "active": True},
    {"signal": 0, "active": False},
    ["_corrupted_", "valid_entry"],
    {"signal": 13, "active": True, "meta": [1, 2, 3]},
    "STATUS_OK",
    [1, [2, 3]],
    "debug_mode_off"
]

base_threshold = 12

# Execute main logic
calculated_metrics = get_summary_stats([10, 20, 30, 40])  # unused
entropy_value = compute_entropy("aabbc")  # irrelevant call

temp_transform = transform_data([1, 2, 3, 4, 5])  # dead transformation

final_score = evaluate_performance(data_log, base_threshold)
print(f"Result: {final_score}")