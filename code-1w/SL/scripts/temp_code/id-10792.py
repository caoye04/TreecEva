from collections import defaultdict
from itertools import groupby
import math

def analyze_traffic(data):
    # Irrelevant function: simulates network traffic analysis
    counts = defaultdict(int)
    for item in data:
        counts[item['source']] += 1
    return dict(counts)

def compute_checksum(sequence):
    # Distractor: computes XOR checksum (not used in final result)
    checksum = 0
    for val in sequence:
        checksum ^= int(val * 100) % 256
    return checksum

def preprocess_logs(entries):
    # Decoy transformation: modifies case and strips spaces (some irrelevant)
    processed = []
    temp_store = []
    for e in entries:
        line = e.replace('  ', ' ').strip().lower()
        if 'error' in line:
            temp_store.append(line)  # Dead storage path
        cleaned = line.replace('failed', 'rejected').replace('success', 'accepted')
        processed.append(cleaned.title())  # Only title casing matters later
    return processed

def extract_metrics(log_lines):
    # Extracts character counts and word patterns (partial relevance)
    stats = defaultdict(int)
    total_chars = 0
    uppercase_count = 0
    
    for line in log_lines:
        total_chars += len(line)
        uppercase_count += sum(1 for c in line if c.isupper())
        words = line.split()
        for w in words:
            if len(w) > 4:
                stats['long_words'] += 1

    # Red herring computation
    fake_entropy = math.log(total_chars + 1) * 0.7 if total_chars > 0 else 0
    stats['fake_metric'] = int(fake_entropy * 100)

    stats['total_chars'] = total_chars
    stats['uppercase_ratio'] = round(uppercase_count / total_chars, 6) if total_chars else 0
    return stats

def calculate_weighted_score(freq_map, base):
    # Complex scoring with misleading branches
    score = 0
    multiplier = 1.0
    
    if freq_map.get('long_words', 0) > base * 2:
        multiplier *= 1.2
    elif freq_map.get('long_words', 0) < base:
        multiplier *= 0.85
    else:
        multiplier *= 1.05

    # Bit manipulation decoy
    encoded_base = (base << 2) ^ 15
    encoded_base = (encoded_base & 255) | 100

    # Actual relevant calculation
    char_score = freq_map.get('total_chars', 0) // 10
    ratio_bonus = int(freq_map.get('uppercase_ratio', 0) * 1000)
    
    # Key formula
    score += char_score * multiplier
    score += ratio_bonus

    # Unused conditional branch (misleading)
    if freq_map.get('fake_metric', 0) > 50:
        anomaly_correction = math.sin(score % 3.14)
        score -= int(anomaly_correction * 10)

    return int(score)

def evaluate_performance(raw_logs, threshold):
    # Core function with layered distractions

    # Step 1: Preprocess logs (only title case matters)
    formatted_logs = preprocess_logs(raw_logs)
    
    # Step 2: Extract metrics (some are red herrings)
    metrics = extract_metrics(formatted_logs)
    
    # Step 3: Analyze word frequency groups (irrelevant grouping)
    sorted_logs = sorted(formatted_logs, key=lambda x: len(x.split()))
    grouped = {k: list(g) for k, g in groupby(sorted_logs, key=lambda x: len(x.split()))}
    avg_group_size = sum(len(v) for v in grouped.values()) / len(grouped) if grouped else 0

    # Step 4: Compute distractor checksum
    dummy_sequence = [math.cos(i * 0.1) for i in range(len(raw_logs))]
    _ = compute_checksum(dummy_sequence)  # Result ignored

    # Step 5: Calculate score using only part of the data
    base_level = int(threshold * 1.5)
    raw_score = calculate_weighted_score(metrics, base_level)

    # Step 6: Apply meaningless bit shifts
    final_score = raw_score
    for _ in range(2):
        final_score = ((final_score << 1) | (final_score >> 7)) & 0xFFFF

    # Step 7: Normalize within realistic range
    final_score = final_score % 99999

    # THIS IS THE TARGET VARIABLE
    return final_score

# Main execution block
if __name__ == '__main__':
    # Simulated system log entries (realistic domain)
    log_entries = [
        'User Login Success',
        'FILE TRANSFER FAILED due to timeout',
        'System Reboot Initiated by Admin',
        'CRITICAL ERROR: Memory Overflow Detected',
        'Network Packet Loss High but Recovered',
        'Authentication Successful for User ID 4567',
        'DATABASE QUERY OPTIMIZED Automatically'
    ]

    # Baseline parameter
    baseline = 4

    # Irrelevant data structure
    traffic_data = [
        {'source': '192.168.1.10', 'dest': 'server-a', 'bytes': 1500},
        {'source': '192.168.1.11', 'dest': 'server-b', 'bytes': 2300},
        {'source': '192.168.1.10', 'dest': 'server-c', 'bytes': 800}
    ]
    _ = analyze_traffic(traffic_data)  # Unused result

    # Critical execution point
    final_score = evaluate_performance(log_entries, baseline)
    
    print(f"Target result: {final_score}")