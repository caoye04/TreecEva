from collections import defaultdict, Counter
import math

def collect_diagnostics():
    # Simulated sensor readings (real data)
    raw_readings = [14, 18, 22, 14, 18, 25, 22, 14, 18, 25, 30, 30]
    
    # Irrelevant signal processing (distractor)
    temp_buffer = []
    for x in raw_readings:
        if x > 20:
            temp_buffer.append(x * 1.5)
    
    # Real signal extraction (used later)
    collected_signals = []
    signal_count = defaultdict(int)
    for val in raw_readings:
        signal_count[val] += 1
        if val % 2 == 0 and val not in collected_signals:
            collected_signals.append(val)
    
    # Dead code path (misleading)
    def decode_legacy_format(data):
        return sum([d**2 for d in data if d < 19])
    legacy_score = decode_legacy_format(raw_readings)  # Unused
    
    # Decoy statistical analysis
    mean_val = sum(raw_readings) / len(raw_readings)
    variance_proxy = sum([(x - mean_val)**2 for x in raw_readings]) / len(raw_readings)
    entropy_approx = math.log(len(set(raw_readings))) * 100  # Not used
    
    # System key generation with red herring logic
    key_parts = []
    for i, count in enumerate(signal_count.values()):
        if i % 3 == 0:
            key_parts.append(count * 2)
        elif i % 3 == 1:
            key_parts.append(count + 1)
        else:
            key_parts.append(count ** 2)  # Some unused complexity
    
    # Actual system key used
    system_key = key_parts[0] + key_parts[1] - key_parts[2] if len(key_parts) >= 3 else 5
    
    # Another decoy function (never called in execution flow)
    def validate_checksum(data, key):
        total = sum(data)
        return total % key == 0
    
    # Core analysis function (depends on collected_signals and system_key)
    def analyze_pattern(signals, key):
        pattern_score = 0
        freq_counter = Counter(signals)
        
        # Logical chain with multiple steps
        for s in signals:
            if s < 20:
                pattern_score += freq_counter[s] * key
            else:
                pattern_score -= (s // 10) * (key % 3)
        
        # Additional conditional manipulation
        if len(signals) > 3:
            pattern_score += 10
        if key > 6:
            pattern_score *= 2
        
        # Red herring: irrelevant transformation
        dummy_transform = [math.sin(math.pi * x / 180) for x in signals]
        avg_dummy = sum(dummy_transform) / len(dummy_transform)  # Not used
        
        # Final adjustment based on set logic
        unique_pairs = set()
        for a in signals:
            for b in signals:
                if a != b and (a + b) % 5 == 0:
                    unique_pairs.add((min(a,b), max(a,b)))
        pattern_score += len(unique_pairs)
        
        return int(pattern_score)
    
    # Execution point of interest
    final_diagnostic = analyze_pattern(collected_signals, system_key)
    
    # Unrelated logging (dead code)
    log_entry = f"Diagnostics complete: {len(temp_buffer)} high-readings"
    
    return final_diagnostic

# Execute and print result
diag_result = collect_diagnostics()
print(f"Result: {diag_result}")