from collections import defaultdict, Counter
import math

# Simulated system log analysis with diagnostic reasoning

def preprocess_logs(raw_logs):
    processed = []
    for entry in raw_logs:
        timestamp, code, severity = entry
        if severity < 0 or code == "":
            continue
        category = "A" if code[0] in "ABC" else "X"
        processed.append((timestamp % 86400, category, severity))
    return processed

# Irrelevant helper - decoy function
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Distractor: unused aggregation
def aggregate_metrics(logs):
    stats = defaultdict(lambda: defaultdict(int))
    for t, cat, sev in logs:
        stats[cat]['count'] += 1
        stats[cat]['max_sev'] = max(stats[cat]['max_sev'], sev)
        stats[cat]['total_sev'] += sev
    return {k: dict(v) for k, v in stats.items()}

# Core logic buried among noise
def filter_anomalies(entries):
    anomalies = []
    for time, cat, sev in entries:
        # Only odd timestamps with high severity are anomalous
        if time % 2 == 1 and sev > 2:
            anomalies.append((time, sev))
    return anomalies

# Misleading intermediate transformation
def derive_temporal_weights(times):
    weights = []
    for t in times:
        w = (math.sin(t / 1000) ** 2) * 1.5
        weights.append(round(w, 3))
    return weights  # Never actually used

# Key analysis function
def analyze_patterns(log_data, flags):
    # Step 1: Extract categories
    categories = [cat for _, cat, _ in log_data]
    cat_count = Counter(categories)
    
    # Step 2: Find anomalies
    anomalies = filter_anomalies(log_data)
    anomaly_score = len(anomalies) * 2
    
    # Step 3: Process flag interactions
    flag_values = []
    for f in flags:
        if f.startswith('F'):
            flag_values.append(int(f[1:]) * 3)
        elif f.startswith('G'):
            flag_values.append(-int(f[1:]))
    
    flag_contribution = sum(f for f in flag_values if f > 0) - len([f for f in flag_values if f < 0])
    
    # Step 4: Apply conditional weight based on majority category
    primary_cat = cat_count.most_common(1)[0][0]
    base_score = anomaly_score + flag_contribution
    
    if primary_cat == "A" and base_score > 5:
        adjusted_score = base_score * 2
    elif primary_cat == "X" and len(anomalies) >= 3:
        adjusted_score = base_score + 7
    else:
        adjusted_score = base_score - 1
    
    # Step 5: Final adjustment based on hidden pattern
    severe_count = sum(1 for _, _, sev in log_data if sev >= 3)
    if severe_count >= 4 and 'F4' in flags:
        adjusted_score += 5
    
    # Final diagnostic is this adjusted score
    final_diagnostic = adjusted_score
    
    # DEAD CODE PATHS BELOW - red herrings
    debug_info = {}
    if final_diagnostic > 20:
        debug_info['level'] = 'CRITICAL'
        debug_info['priority'] = 1
    elif final_diagnostic > 10:
        debug_info['level'] = 'WARNING'
        debug_info['priority'] = 2
    else:
        debug_info['level'] = 'INFO'  # This runs but doesn't affect answer
        debug_info['priority'] = 3
    
    metadata_summary = {
        'entries': len(log_data),
        'anomalies_found': len(anomalies),
        'primary_category': primary_cat
    }
    
    return final_diagnostic

# Generate input data
raw_system_logs = [
    (1200, "ABX", 1),
    (3601, "BCD", 3),
    (7205, "XYZ", 2),
    (8001, "ACE", 4),
    (9000, "NONE", 3),
    (10503, "AAA", 5),
    (14400, "XXX", 1),
    (18005, "ABC", 4),
    (20001, "DEF", 2),
    (21607, "ABC", 5)
]

system_flags = ["F4", "G2", "F1", "F3"]

# Preprocessing chain
cleaned_logs = preprocess_logs(raw_system_logs)

# Dead computation - distractor
timestamps_only = [t for t, _, _ in cleaned_logs]
weight_profile = derive_temporal_weights(timestamps_only)  # Computed but unused

# Another irrelevant aggregation
log_stats = aggregate_metrics(cleaned_logs)
entropy_value = compute_entropy([c for _, c, _ in cleaned_logs])  # Interesting but unused

# Critical execution point
final_diagnostic = analyze_patterns(cleaned_logs, system_flags)

print(f"Result: {final_diagnostic}")