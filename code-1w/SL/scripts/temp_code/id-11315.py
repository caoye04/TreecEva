def analyze_subsystem_integrity(raw_logs):
    checksum = 0
    for i, log in enumerate(raw_logs):
        if i % 2 == 0:
            checksum += sum(ord(c) for c in log) % 7
    return checksum


def compute_entropy(sequence):
    from math import log2
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    total = len(sequence)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

# Irrelevant helper - looks important but unused in critical path
def predict_failure_rate(age_years, usage_cycles):
    base = 0.02 * age_years
    stress = (usage_cycles / 10000) ** 1.5
    return min(base + stress, 1.0)

# Decoy function that simulates load but doesn't affect final result
def simulate_network_jitter(delays):
    adjusted = [d * 1.15 for d in delays if d > 0]
    avg_jitter = sum(adjusted) / len(adjusted) if adjusted else 0
    normalized = [a / (avg_jitter + 1e-6) for a in adjusted]
    return [round(n, 3) for n in normalized]

# Misleading preprocessing step with red herring output
def extract_metadata(header_string):
    parts = header_string.split('|')
    timestamps = [p for p in parts if p.isdigit()]
    codes = [p for p in parts if len(p) == 3 and p.isalpha()]
    priority = sum(int(t) % 10 for t in timestamps) if timestamps else 0
    # Following line appears important but is not used later
    diagnostic_flag = f"ERR-{priority}" if priority > 5 else "OK"
    return priority, len(codes)

# Core logic buried among distractors
def aggregate_metrics(scores, load):
    weighted_sum = 0.0
    adjustment_factor = 1.0
    
    if len(scores) >= 3:
        sorted_scores = sorted(scores, reverse=True)
        top_three_avg = sum(sorted_scores[:3]) / 3
        adjustment_factor = 0.8 + (top_three_avg / 100) * 0.2
    
    base_aggregate = sum(s * (i + 1) for i, s in enumerate(scores))
    load_penalty = max(0, load - 75) * 0.5
    
    intermediate = base_aggregate * adjustment_factor - load_penalty
    
    # Critical non-linear transformation
    if intermediate > 100:
        intermediate = 90 + (intermediate - 100) * 0.5
    elif intermediate < 30:
        intermediate = 30 + (intermediate - 30) * 0.3
    
    return round(intermediate, 2)

# Unused data structure - creates illusion of complexity
class SystemState:
    def __init__(self, id_val, status_code):
        self.id = id_val
        self.status = status_code
        self.timestamp = None
        self.checksum = 0

    def validate(self):
        return self.status in ['ACTIVE', 'STANDBY']

# Real execution begins here
if __name__ == '__main__':
    # Input data - some are relevant, others are distractions
    sensor_readings = [23.1, 24.5, 22.8, 25.0, 23.9, 24.2]
    raw_log_data = ["START|2023", "DATA|CHK", "END|999", "META|ABC"]
    network_delays = [-1.0, 0.0, 12.5, 15.3, 10.2, -0.5, 14.8]
    header_info = "INIT|2024|XYZ|777|END"
    
    # Step 1: Extract entropy from readings (red herring)
    rounded_values = [int(x) for x in sensor_readings]
    reading_entropy = compute_entropy(rounded_values)
    
    # Step 2: Analyze logs (used to calculate checksum below)
    log_integrity = analyze_subsystem_integrity(raw_log_data)
    
    # Step 3: Extract metadata (partially used)
    meta_priority, code_count = extract_metadata(header_info)
    
    # Step 4: Simulate network (dead end)
    jitter_profile = simulate_network_jitter(network_delays)
    
    # Step 5: Create decoy objects (irrelevant)
    states = [SystemState(i, ['ACTIVE','STANDBY'][i%2]) for i in range(3)]
    for s in states:
        s.timestamp = 1000 + (log_integrity * meta_priority)
        s.checksum = sum(ord(c) for c in s.status) % 256
    
    # Step 6: Generate reliability scores (critical path starts)
    base_score = 65 + (meta_priority * 2)  # meta_priority = 14 → 65+28=93
    dynamic_boost = int(reading_entropy * 3)  # entropy ≈ 2.32 → boost ≈ 6
    fallback_offset = code_count * 4  # code_count = 1 → 4
    
    reliability_scores = [
        base_score,
        base_score + dynamic_boost,
        base_score + 5,
        base_score + fallback_offset,
        91  # hardcoded high performer
    ]
    
    # Step 7: System load influenced by integrity check
    system_load = 60 + (log_integrity * 3)  # log_integrity = (sum of even-indexed log hashes) % 7
        # log[0]: "START|2023" → sum ord % 7 = (S+T+A+R+T+2+0+2+3) % 7
        # S=83,T=84,A=65,R=82 → 83+84+65+82+84+50+48+50+51 = 537 → 537%7=2
        # so log_integrity = 2 → system_load = 66
    
    # Step 8: The key computation
    final_diagnostic = aggregate_metrics(reliability_scores, system_load)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")