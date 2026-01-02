import itertools

def analyze_purity(samples):
    purity_flags = []
    for s in samples:
        if len(s) < 3:
            purity_flags.append(False)
        else:
            avg_char = sum(ord(c) for c in s) / len(s)
            purity_flags.append(avg_char < 100)
    return purity_flags

def compute_entropy(data):
    # Irrelevant entropy calculation (distraction)
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

def filter_records(records, limits):
    # Dead code path - never actually used
    valid = []
    for r in records:
        if isinstance(r, str) and r.isalpha():
            valid.append(r.upper())
    return valid

def shift_sequence(seq, offset):
    # Unused transformation function (red herring)
    return seq[offset:] + seq[:offset]

def detect_anomalies(logs):
    # Misleading intermediate result
    counts = {k: logs.count(k) for k in set(logs)}
    anomalies = [k for k, v in counts.items() if v > 2]
    return sorted(anomalies)

def process_contaminants(samples, thresholds):
    # Core logic begins
    ascii_grades = []
    for sample in samples:
        # Compute weighted contamination score based on character frequency
        upper_count = len([c for c in sample if c.isupper()])
        digit_count = len([c for c in sample if c.isdigit()])
        special_count = len([c for c in sample if not c.isalnum()])
        base_score = upper_count * 7 + digit_count * 11 + special_count * 13
        normalized = base_score / (len(sample) if sample else 1)
        ascii_grades.append(round(normalized))
    
    # Aggregate using pairwise combinations (itertools usage)
    pairs = list(itertools.combinations(ascii_grades, 2))
    pair_sums = [abs(a - b) for a, b in pairs] if pairs else [0]
    stability_index = sum(pair_sums) // len(pair_sums)

    # Apply threshold filtering
    threshold_total = sum(thresholds)
    adjustment_factor = len([p for p in pair_sums if p > threshold_total // 4])
    
    # Conditional expression determines final behavior
    dispersion_score = max(pair_sums) if len(pair_sums) > 5 else min(pair_sums)

    # Final computation
    filtration_score = stability_index + adjustment_factor * 3 - dispersion_score
    
    # Print required output
    print(f"Result: {filtration_score}")
    return filtration_score

# Simulated water quality data (character sequences as contamination signatures)
water_samples = [
    "H2O_Cln!9", "Pur3-Tank", "AquaSafe_2023", "H2O_Flt#5", "ClearDrop!",
    "H2O_X7?", "UltraPure.", "Hydr8-Now", "H2O_Mix@3", "SafeWater$"]

threshold_levels = [5, 8, 12, 6, 9, 11, 7]

# Irrelevant preprocessing (distractor)
decoy_data = [f"X{str(i)*2}" for i in range(len(water_samples))]
shuffled = shift_sequence(decoy_data, 3)

# Unused anomaly detection
log_entries = ['A', 'B', 'A', 'C', 'B', 'A', 'D']
anomaly_list = detect_anomalies(log_entries)

# Entropy distraction
sample_text = "abccba"
entropy_value = compute_entropy(sample_text)

# Actual execution point
filtration_score = process_contaminants(water_samples, threshold_levels)