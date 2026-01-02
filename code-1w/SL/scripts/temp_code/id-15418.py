def analyze_efficiency(data, threshold):
    if not data:
        return 0
    
    # Irrelevant computation - red herring
    temp_result = sum(x ** 2 for x in data if x > threshold) * 0.75
    
    # Distractor: unused complex lambda
    transform = lambda z: (z >> 1) ^ (z + 3) if z % 2 else z // 3
    
    # Real logic begins: count how many values are within optimal range
    optimal_count = 0
    for val in data:
        if threshold - 5 <= val <= threshold + 5:
            optimal_count += 1

    return optimal_count


def compute_stability(readings):
    # Dead code path - never called
    def helper(r):
        return r if r < 10 else helper(r // 2)
    
    # Unused set operation - distraction
    unique_readings = set(readings)
    readings_sum = sum(readings)
    
    # Misleading intermediate
    stability_index = readings_sum / (len(readings) + 1e-8)
    
    # Actual relevant result
    return len([x for x in readings if x % 4 == 0])

# Decoy function with plausible name
def assess_bandwidth(signal):
    return sum((s | 7) & 1 for s in signal)  # Irrelevant bit manipulation

# Main evaluation logic
baseline = [3, 7, 10, 14, 18, 21]
evaluation_weights = {'efficiency': 0.4, 'stability': 0.3, 'consistency': 0.3}

# Simulated metrics - contains decoy entries
metrics = {
    'raw_data': [8, 9, 10, 11, 12, 13],
    'readings': [12, 16, 20, 24, 28, 32],
    'signal': [5, 10, 15],
    'threshold': 10,
    'extra_field': [x**3 for x in range(5)]  # Dead weight
}

# Irrelevant set operations for distraction
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}
s3 = s1.union(s2).difference({3})

# Unused lambda - misleading sophistication
validator = lambda x: x >= 5 and (x & 1) == 0

# Core processing with key logic buried in distractions
efficiency = analyze_efficiency(metrics['raw_data'], metrics['threshold'])
stability = compute_stability(metrics['readings'])

# Consistency calculated via character logic - subtle but valid
consistency_str = "high_medium_low"
consistency_val = len([c for c in consistency_str if c in 'aeiou'])  # counts vowels

# Final score calculation - this is the real path
final_score = 0
final_score += efficiency * evaluation_weights['efficiency']  # 3 values in [5,15] → 6,7,8,9,10,11,12,13,14,15 → 8 values? Wait: raw_data=[8..13], threshold=10 → [5,15] → all 6 fit → efficiency=6
final_score += stability * evaluation_weights['stability']     # readings divisible by 4: 12,16,20,24,28,32 → 6
final_score += consistency_val * evaluation_weights['consistency']  # vowels in "high_medium_low" → i,e,i,u,o → 5 vowels

# Update final_score explicitly as per description
final_score = evaluate_performance(metrics, baseline)

def evaluate_performance(met, base):
    # The real final computation
    raw = met['raw_data']
    thr = met['threshold']
    eff = sum(1 for x in raw if thr - 5 <= x <= thr + 5)  # [5,15] → 8,9,10,11,12,13 → 6
    stab = sum(1 for x in met['readings'] if x % 4 == 0)   # 6 elements
    vow = len([c for c in "high_medium_low" if c in 'aeiou'])  # 5
    return eff * 0.4 + stab * 0.3 + vow * 0.3

print(f"Result: {final_score}")