from collections import defaultdict, Counter

# Simulated system telemetry and user interaction data
def collect_telemetry():
    raw_signals = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]
    timestamps = list(range(10))
    modes = ['active', 'idle', 'active', 'active', 'sleep', 'active', 'active', 'active', 'sleep', 'sleep']
    return raw_signals, timestamps, modes

# Misleading auxiliary function (dead code path - never called)
def analyze_bandwidth_usage(signals):
    total_bits = sum([x * 1024 for x in signals])
    avg_throughput = total_bits / len(signals) if signals else 0
    return avg_throughput

# Another decoy: irrelevant network simulation
def simulate_packet_flow(packets):
    dropped = 0
    for p in packets:
        if p % 13 == 0:
            dropped += 1
    retransmitted = dropped * 2
    efficiency = (len(packets) - dropped) / len(packets) if packets else 0
    return efficiency

# Core logic disguised among distractors
def extract_behavior_pattern(signals, mode_log):
    pattern = defaultdict(int)
    for s, m in zip(signals, mode_log):
        if s == 1 and m == 'active':
            pattern['engaged'] += 1
        elif s == 1 and m == 'idle':
            pattern['idle_wake'] += 1
        elif s == 0 and m == 'active':
            pattern['missed_opportunity'] += 1
    return dict(pattern)

# Distractor: unused transformation
def normalize_timestamps(ts):
    base = ts[0]
    return [t - base for t in ts]

# Key processing function with embedded logic chain
def compute_stability_index(pattern, window_size=3):
    keys = list(pattern.keys())
    if 'engaged' in pattern:
        base_engagement = pattern['engaged'] * 100
        fluctuations = abs(pattern.get('idle_wake', 0) - pattern.get('missed_opportunity', 0))
        penalty = fluctuations * 5
        # Nested conditional with bit manipulation red herring
        if penalty > 0:
            adjusted = base_engagement ^ 15  # Bitwise XOR as distraction
            if adjusted % 2 == 0:
                adjusted += 3
            penalty = penalty >> 1  # Right shift to reduce impact
        else:
            adjusted = base_engagement + 10
        stability = adjusted - penalty
        # Extra layer: floating point obfuscation
        stability = round(stability + 0.004567, 3)
        return stability
    return 50.0

# Decoy aggregation (never used)
def calculate_response_ratio(timestamps):
    if len(timestamps) < 2:
        return 0
    diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    return sum(diffs) / len(diffs)

# Main pipeline with multiple abstraction layers
def process_performance(metrics, user_profile):
    # Irrelevant feature extraction
    age_group = user_profile.get('age', 30) // 10 * 10
    risk_factor = 1 if age_group > 40 else 0.8

    # Real logic hidden in noise
    engagement_raw = metrics.get('engaged', 0)
    fallback_mode = metrics.get('idle_wake', 0) > metrics.get('missed_opportunity', 0)

    # Conditional branching with short-circuit evaluation
    base_value = engagement_raw * 100 if engagement_raw > 2 else (fallback_mode and 75 or 60)

    # String processing distraction
    category_str = user_profile.get('category', 'standard')
    flags = [c.upper() for c in category_str if c in 'aeiou']
    flag_sum = sum([ord(f) % 10 for f in flags])

    # Set operation distractor
    unique_flags = set(flags)
    bonus = len(unique_flags) * 7 if 'A' in unique_flags else 0

    # Critical calculation buried in noise
    primary_metric = base_value + bonus + flag_sum

    # Secondary adjustment using Counter (required feature)
    history = user_profile.get('history', [])
    hist_count = Counter(history)
    repeat_bonus = 0
    for k, v in hist_count.items():
        if v >= 3:
            repeat_bonus += 10

    # Final assembly with decoy arithmetic
    temp_result = primary_metric * risk_factor  # Slight reduction if older
    decay_correction = 1.0
    if 'sleep' in history:
        decay_correction = 0.95

    final_raw = temp_result + repeat_bonus * decay_correction

    # Dead code: complex but unused formula
    max_theoretical = 100 + (len(history) ** 0.5) * 20
    utilization = final_raw / max_theoretical if max_theoretical > 0 else 0

    # Actual answer computation
    final_score = int(round(final_raw - 28))  # Deterministic offset

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Global scope execution
if __name__ == '__main__':
    # Collect real data
    signals, ts, modes = collect_telemetry()
    
    # Build realistic input structure
    behavior = extract_behavior_pattern(signals, modes)
    
    # User profile with mixed relevant and irrelevant fields
    user_data = {
        'age': 28,
        'category': 'premium',
        'history': ['active', 'active', 'idle', 'active', 'sleep', 'active']
    }
    
    # Unused variables - red herrings
    bandwidth = analyze_bandwidth_usage(signals)
    packet_efficiency = simulate_packet_flow([1, 2, 3, 13, 26, 39])
    normalized_times = normalize_timestamps(ts)
    response_latency = calculate_response_ratio(ts)
    
    # Stability index calculated but only partially influential
    metrics = behavior.copy()
    stability = compute_stability_index(behavior)
    metrics['stability'] = stability
    
    # Key assignment statement
    final_score = process_performance(metrics, user_data)