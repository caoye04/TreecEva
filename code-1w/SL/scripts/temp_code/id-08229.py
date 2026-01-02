from collections import defaultdict
import math

# Simulated sensor data processing system for a distributed IoT network
def collect_diagnostics():
    raw_readings = [145, 278, 93, 412, 88, 305, 177, 223, 64, 398]
    device_ids = ['D07', 'D12', 'D03', 'D22', 'D15', 'D19', 'D08', 'D11', 'D05', 'D25']
    timestamps = list(range(1000, 1010))
    
    # Irrelevant aggregation: frequency count (distractor)
    freq_count = defaultdict(int)
    for val in raw_readings:
        freq_count[val // 50] += 1
    
    # Misleading transformation: exponential smoothing with arbitrary decay (dead path)
    smoothed = []
    alpha = 0.3
    if raw_readings:
        smoothed.append(raw_readings[0])
        for i in range(1, len(raw_readings)):
            smoothed.append(alpha * raw_readings[i] + (1 - alpha) * smoothed[-1])
    
    # Key data structure initialization (relevant)
    health_sequence = [x % 100 for x in raw_readings if x > 100]
    
    # Decoy function definition (never called, distractor)
    def analyze_pattern(seq):
        return sum(x * (i+1) for i, x in enumerate(seq)) / len(seq) if seq else 0
    
    # Irrelevant statistical calculation (red herring)
    mean_val = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    std_dev = math.sqrt(variance)
    
    # Complex but unused conditional block (dead code path)
    alert_flags = []
    if std_dev > 100:
        for i, val in enumerate(raw_readings):
            if val > mean_val + std_dev:
                alert_flags.append((device_ids[i], timestamps[i]))

    # Another irrelevant computation: pairwise differences (distractor)
    pairwise_diffs = [abs(raw_readings[i] - raw_readings[i+1]) for i in range(len(raw_readings)-1)]
    spike_count = sum(1 for d in pairwise_diffs if d > 100)

    # Real threshold logic obscured among noise
    base_threshold = 85
    adjustment_factor = len([x for x in health_sequence if x > 50])
    dynamic_adjustment = 1 + (adjustment_factor * 0.05)
    
    # Threshold map built using relevant and irrelevant components
    threshold_map = {
        'critical': base_threshold * dynamic_adjustment,
        'warning': base_threshold * 0.8,
        'info': 30
    }
    
    # Hidden logic: counting how many exceed dynamically adjusted critical level
    critical_limit = threshold_map['critical']
    over_threshold = sum(1 for x in health_sequence if x >= critical_limit)
    
    # Core processing function defined inside to increase nesting and distraction
    def process_metrics(seq, thresholds):
        # Secondary irrelevant filtering
        filtered = [x for x in seq if x >= thresholds['info']]
        
        # Unused intermediate calculation
        avg_filtered = sum(filtered) / len(filtered) if filtered else 0
        
        # Another decoy data structure
        stats_summary = {
            'count': len(filtered),
            'max': max(filtered) if filtered else 0,
            'min': min(filtered) if filtered else 0
        }
        
        # Red herring: trigonometric manipulation (no effect on result)
        angle_radians = math.pi * avg_filtered / 180
        trig_weight = abs(math.sin(angle_radians) + math.cos(angle_radians * 0.5))
        
        # Actual answer derivation hidden in complex expression
        # Final diagnostic is product of over-threshold count and adjustment factor
        # But obfuscated within nested conditionals and calculations
        if len(seq) > 5:
            if over_threshold > 0:
                base_score = over_threshold * 100
                penalty = 0
                for x in seq:
                    if x < 20:
                        penalty += 5
                final_value = base_score - penalty
                # This branch contains the real logic
                scaling = int(dynamic_adjustment * 10)  # 15 in this case
                return final_value + scaling
            else:
                return 50
        else:
            return sum(seq) % 100
            
    # Execution point of interest
    final_diagnostic = process_metrics(health_sequence, threshold_map)
    
    # Additional unrelated variable (distraction)
    summary_report = f"Devices: {len(device_ids)}, Readings: {len(raw_readings)}"
    
    # Output requirement
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Entry point
result = collect_diagnostics()