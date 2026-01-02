from collections import defaultdict, Counter
import itertools

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    signals = []
    for i in range(150):
        signals.append({
            'id': i,
            'power_draw': (i * 17) % 97 + (i % 3),
            'temp_spike': (i * 53) % 89,
            'status_flag': i % 4,
            'checksum': (i ^ (i << 1)) & 0xFF
        })
    return signals

# Irrelevant auxiliary function - dead code path
def decrypt_payload(data):
    acc = 0
    for i in range(len(data)):
        acc += (data[i]['id'] ^ data[i]['checksum']) % 13
    return acc * 2  # Never actually used

# Misleading preprocessing step with partial relevance
def filter_anomalies(telemetry):
    anomalies = []
    temp_stats = defaultdict(int)
    power_outliers = 0

    for entry in telemetry:
        temp_stats[entry['temp_spike'] // 10] += 1
        if entry['power_draw'] > 90:
            power_outliers += 1
        if entry['status_flag'] == 3 and entry['temp_spike'] > 80:
            anomalies.append(entry['id'])
    
    # Distractor: complex but unused structure
    freq_counter = Counter(temp_stats.values())
    rare_bins = [k for k, v in freq_counter.items() if v < 2]

    # Only this line matters: returns ids where status=3 and high temp
    return anomalies

# Core logic obscured by multiple layers
def extract_signatures(telemetry):
    sig_groups = defaultdict(list)
    for t in telemetry:
        bucket = (t['power_draw'] // 25) + (t['status_flag'] * 2)
        sig_groups[bucket].append(t['temp_spike'] % 7)
    
    # Real transformation: computes product of group modal remainders
    modal_remainders_product = 1
    for group in sig_groups.values():
        count = Counter(group)
        mode_val = max(count.keys(), key=lambda x: count[x])
        modal_remainders_product *= mode_val + 1  # Avoid zero
    
    return modal_remainders_product

# Secondary irrelevant accumulator
def compute_health_score(telemetry):
    score = 0
    for t in telemetry:
        if t['checksum'] % 7 == 0:
            score += t['status_flag']
        elif t['id'] % 11 == 0:
            score -= 1
    return score  # Not used anywhere

# Decoy state tracker
class DiagnosticsBuffer:
    def __init__(self):
        self.buffer = []
        self.checkpoint = None
    
    def append(self, val):
        self.buffer.append(val % 1000)
    
    def finalize(self):
        return sum(x**2 for x in self.buffer) % 100  # Unused result

# Main processing pipeline
def process_metrics(entries, threshold):
    # Step 1: Extract signature from power/temp correlation
    sig_value = extract_signatures(entries)
    
    # Step 2: Collect diagnostic anomalies (only some are used)
    flagged_ids = filter_anomalies(entries)
    
    # Step 3: Compute cumulative hash (distraction)
    total_hash = 0
    for eid in flagged_ids:
        total_hash ^= (eid * 31) % 1000
    
    # Step 4: Use only length of anomaly list as weight
    anomaly_weight = len(flagged_ids) if len(flagged_ids) > 5 else 1
    
    # Step 5: Generate synthetic time-series windows (unused)
    time_windows = []    
    for i in range(0, len(entries), 10):
        window = entries[i:i+10]
        avg_power = sum(w['power_draw'] for w in window) / len(window)
        time_windows.append({'start': i, 'avg': avg_power, 'peak': max(w['temp_spike'] for w in window)})
    
    # Step 6: Build frequency cross-tab (distractor)
    flag_dist = defaultdict(int)
    for e in entries:
        flag_dist[e['status_flag']] += 1
    
    # Step 7: Compute rolling checksum dependency (irrelevant)
    rolling_key = 0
    for i, e in enumerate(entries):
        if i % 23 == 0:
            rolling_key += e['checksum'] % 17
    
    # Step 8: Actual critical calculation
    base_metric = sig_value  # From modal remainder product
    adjustment_factor = 1
    for prime in [2, 3, 5, 7, 11]:
        if anomaly_weight % prime == 0:
            adjustment_factor *= prime
    
    # Final computation
    intermediate = (base_metric * adjustment_factor) + (anomaly_weight ** 2)
    final_diagnostic = (intermediate % threshold) * 3
    
    # Red herring: buffer collection
    dbuf = DiagnosticsBuffer()
    for t in time_windows[:5]:
        dbuf.append(int(t['avg']))
    
    return final_diagnostic

# Orchestration with decoy calls
telemetry_data = generate_telemetry()

# Irrelevant health assessment
health_diag = compute_health_score(telemetry_data)

# Unused decryption attempt
payload_key = decrypt_payload(telemetry_data)

# Actual execution point
system_threshold = 983
final_diagnostic = process_metrics(telemetry_data, system_threshold)

print(f"Target result: {final_diagnostic}")