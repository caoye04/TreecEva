from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i, val in enumerate(sequence):
        if i > 0 and sequence[i] > sequence[i-1]:
            trend.append(1)
        elif i > 0 and sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Distractor: Analyze subsequences that aren't used later
    subseq_anomalies = 0
    for length in range(2, 4):
        for combo in combinations(trend, length):
            if sum(combo) == 0:
                subseq_anomalies += 1

    # Real logic: Count ascending pairs
    asc_pairs = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            asc_pairs += 1

    return asc_pairs

def compute_statistics(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    peak = max(data)
    
    # Irrelevant transformation
    shifted = [x * 1.5 + 2 for x in data]
    fake_entropy = sum(x * x for x in shifted) % 100
    
    return mean, variance, peak

def main():
    # Input dataset
    readings = [12, 15, 10, 23, 18, 25, 30, 22]
    
    # Step 1: Pattern analysis
    pattern_strength = analyze_pattern(readings)
    
    # Step 2: Statistical summary (some values unused)
    avg, var, max_val = compute_statistics(readings)
    
    # Step 3: Weighted contribution
    weight_a = 0.6
    weight_b = 0.4
    
    # Misleading intermediate calculation
    temp_estimate = (avg * max_val) / (var + 1) if var != 0 else avg
    debug_trace = [temp_estimate * i for i in range(3)]  # Dead code
    
    # Core logic: Combine pattern strength with adjusted mean
    adjusted_mean = avg * (1 + pattern_strength / len(readings))
    
    # Final score computation
    final_score = int(weight_a * adjusted_mean + weight_b * pattern_strength)
    
    # Step 4: Red herring validation check (not affecting result)
    valid = True
    for idx, value in enumerate(readings):
        if idx > 0 and abs(value - readings[idx-1]) > 10:
            valid &= (value > 20)
    
    # Output result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()