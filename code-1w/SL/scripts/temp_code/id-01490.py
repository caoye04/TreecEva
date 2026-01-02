from collections import defaultdict, Counter
import math

# Simulated system telemetry processing with diagnostic analysis
def analyze_system_health(raw_readings, thresholds):
    # Irrelevant preprocessing: normalize signal (unused later)
    normalized = [round(x / max(raw_readings), 3) for x in raw_readings]
    
    # Core data structures
    event_log = defaultdict(int)
    timing_log = []
    system_flags = []
    
    # Simulate timestamped event classification
    for i, val in enumerate(raw_readings):
        if val > thresholds['critical']:
            category = 'OVERLOAD'
            event_log['high'] += 1
            timing_log.append((i, 'ALERT', val))
            if i % 3 == 0:
                system_flags.append('F1')
        elif val > thresholds['warning']:
            category = 'ELEVATED'
            event_log['mid'] += 1
            timing_log.append((i, 'WARN', val))
            if val > 85 and i % 2 == 0:
                system_flags.append('F2')
        else:
            category = 'NORMAL'
            event_log['low'] += 1
            
        # Dead logic branch: never affects output
        temp_adj = math.floor(val * 0.1) if category == 'OVERLOAD' else 0
        _ = [temp_adj * 2 for _ in range(2)]  # Unused computation

    # Red herring: complex but unused statistical summary
    mean_val = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    skewness = sum(((x - mean_val) ** 3) for x in raw_readings) / (len(raw_readings) * variance ** 1.5) if variance > 0 else 0
    
    # Distractor: build unused frequency map
    freq_dist = Counter(normalized)
    rare_events = [k for k, v in freq_dist.items() if v == 1]
    
    # Critical diagnostic aggregation function
    def aggregate_metrics(log_entries, flags):
        base_score = 0
        penalty = 0
        alert_count = 0
        
        for ts, level, value in log_entries:
            if level == 'ALERT':
                alert_count += 1
                base_score += value // 10
                if ts % 4 == 0:
                    penalty += 5
            elif level == 'WARN':
                base_score += value // 15
                if value > 90:
                    penalty += 2
        
        # Secondary adjustment based on flag patterns
        flag_score = 0
        if 'F1' in flags:
            flag_score += 8
        if 'F2' in flags and len(flags) > 2:
            flag_score += 12
        else:
            flag_score += 4
        
        # Complex interaction: score modulation via modular arithmetic
        mod_factor = (base_score + flag_score) % 7
        if mod_factor in [0, 6]:
            final_adjust = 3
        elif mod_factor > 3:
            final_adjust = -2
        else:
            final_adjust = 1
        
        # Final diagnostic calculation
        result = (base_score - penalty + flag_score) * 10 + final_adjust
        
        # Dead code: irrelevant transformation
        buffer = [result + i for i in range(5)]
        shifted = [(b >> 1) & 0xFF for b in buffer]  # Computation has no effect
        
        return result
    
    # Execution point of interest
    final_diagnostic = aggregate_metrics(timing_log, system_flags)
    
    # Unused advanced analysis (red herring)
    def deep_analysis(data):
        cumulative = 0
        for x in data:
            for shift in [1, 2]:
                cumulative += (x >> shift) ^ (x << 1) & 0xF
        return cumulative % 1000
    
    # Never called
    _ = deep_analysis(raw_readings)
    
    return final_diagnostic

# Simulated input data
readings = [78, 92, 88, 95, 76, 83, 91, 87, 73, 94]
safety_limits = {
    'warning': 80,
    'critical': 90
}

# Entry point
result = analyze_system_health(readings, safety_limits)
print(f"Target result: {result}")