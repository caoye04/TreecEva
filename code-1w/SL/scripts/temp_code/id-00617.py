from collections import defaultdict
import math

def analyze_focus_patterns(data):
    # Irrelevant helper: computes entropy (not used in final result)
    total = sum(data)
    entropy = 0
    for x in data:
        if x > 0:
            p = x / total
            entropy -= p * math.log(p)
    return entropy

def evaluate_performance(levels):
    # Core logic with distractions
    stats = defaultdict(int)
    temp_buffer = [0] * len(levels)
    cumulative_shift = 0
    
    for i, val in enumerate(levels):
        shifted = val ^ 7  # XOR with constant (distraction)
        temp_buffer[i] = shifted
        if val % 2 == 1:
            stats['odd_count'] += 1
        stats['running_total'] += val
        
        # Real logic step: track values above threshold
        if val > 8:
            stats['high_focus'] += 1
            
        # Distractor: complex but unused bitwise accumulation
        cumulative_shift = (cumulative_shift << 1) ^ shifted
    
    # Semi-relevant transformation
    adjusted_high = max(stats['high_focus'], 1) * 2
    
    # Dead code path (never executed due to data range)
    outlier_flag = False
    for v in levels:
        if v < 0 or v > 100:
            outlier_flag = True
            break
    
    # Actual answer derivation (hidden among distractions)
    base_score = stats['running_total'] // stats['odd_count'] if stats['odd_count'] else 0
    bonus = 5 if adjusted_high >= 6 else 0
    final = base_score + bonus
    
    # More red herring variables
    predicted_trend = "stable" if stats['odd_count'] > len(levels) / 2.5 else "variable"
    compression_key = sum(temp_buffer) % 13
    
    return final

# Main execution
concentration_levels = [9, 6, 10, 7, 8, 9, 5]

# Unused pre-processing (distractor)
data_snapshot = concentration_levels.copy()
data_snapshot.reverse()
smoothed_data = [round((a + b) / 2) for a, b in zip(concentration_levels, data_snapshot)]

# Key computation
final_score = evaluate_performance(concentration_levels)

# Output result
print(f"Result: {final_score}")