def analyze_data(records):
    # Irrelevant data transformation
    processed = [r.strip().upper() for r in records if len(r) > 3]
    counts = {k: processed.count(k) for k in set(processed)}
    
    # Distractor: unused function
    def decrypt_key(key):
        return ''.join(chr(ord(c) - 1) for c in key)[::-1]
    
    # Another red herring: complex but unused calculation
    entropy = sum(-v/len(processed) * __import__('math').log2(v/len(processed)) for v in counts.values()) if processed else 0

    # Real logic begins: extract numeric metrics from record strings
    raw_metrics = []
    for record in records:
        parts = record.split(':')
        if len(parts) == 2 and parts[1].isdigit():
            raw_metrics.append(int(parts[1]))
    
    # Bit manipulation distractor
    masked_values = [m ^ 0xFF & 0x3F for m in raw_metrics]
    shifted_sum = sum((v << 2) | 0x1 for v in masked_values) % 1000

    # Tuple unpacking and zip usage (required)
    baseline = [75, 80, 85, 90]
    if len(raw_metrics) >= 4:
        paired = list(zip(raw_metrics[:4], baseline))
        adjustments = [abs(a - b) for a, b in paired]
    else:
        adjustments = [0] * len(raw_metrics)

    # Use of lambda and enumerate (required)
    apply_bonus = lambda idx, val: val + 5 if idx % 2 == 0 else val + 2
    enhanced = [apply_bonus(i, v) for i, v in enumerate(raw_metrics)]

    # Decoy control flow
    status_flags = []
    for x in enhanced:
        if x > 100:
            status_flags.append(0b1000)
        elif x > 90:
            status_flags.append(0b0100)
        elif x > 80:
            status_flags.append(0b0010)
        else:
            status_flags.append(0b0001)
    
    # Actual performance metric calculation
    # Only this path contributes to final answer
    primary_metrics = [m * 1.1 for m in raw_metrics if m >= 70]  # Only consider passing scores
    if len(primary_metrics) == 0:
        primary_metrics.append(50)

    weight_map = [0.2, 0.3, 0.3, 0.2]  # weights for top 4 values
    sorted_metrics = sorted(primary_metrics, reverse=True)[:4]
    while len(sorted_metrics) < 4:
        sorted_metrics.append(70)  # default filler

    def evaluate_performance(metrics, weights):
        # Final computation with weighted sum
        total = sum(m * w for m, w in zip(metrics, weights))
        penalty = 0
        # Apply penalty if any original score below 70
        for r in records:
            if ':' in r and r.split(':')[1].isdigit():
                if int(r.split(':')[1]) < 70:
                    penalty += 2.5
        return round(total - penalty, 4)

    # Critical assignment point
    final_score = evaluate_performance(sorted_metrics, weight_map)

    # Dead code branch (never reached due to structure)
    if False:
        fallback = [ord(c) % 10 for c in str(shifted_sum)]
        final_score = sum(fallback) * 100

    # Output result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
student_records = [
    "hw:88", "quiz:76", "midterm:68", "final:92", "extra:45"
]

# Execute
analyze_data(student_records)