import itertools

def analyze_sequence(seq):
    # Irrelevant helper: computes average gap (not used in final logic)
    gaps = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    avg_gap = sum(gaps) / len(gaps) if gaps else 0

    # Relevant transformation: map to squared residuals from mean
    mean_val = sum(seq) / len(seq)
    residuals = [(x - mean_val)**2 for x in seq]
    return residuals

def validate_stability(data):
    # Distractor function: checks variance but returns boolean not used in core logic
    variance = sum(data) / len(data) if data else 0
    threshold = 500
    is_stable = variance < threshold
    debug_flag = True  # Dead variable
    return is_stable  # Not actually influencing final score

def calculate_performance(raw):
    # Step 1: Filter valid entries (positive and even)
    filtered = [x for x in raw if x > 0 and x % 2 == 0]

    # Step 2: Augment with mirrored negative values (semi-relevant, only first half used later)
    extended = filtered + [-x for x in filtered]

    # Step 3: Use itertools to generate pairwise products (only first 5 pairs used)
    pairs = list(itertools.pairwise(extended))
    products = [a * b for a, b in pairs]

    # Step 4: Apply conditional scaling: boost if product magnitude above threshold
    scaled = []
    for p in products:
        adjusted = p * 1.5 if abs(p) > 100 else p * 0.8  # Some boosted, others reduced
        scaled.append(adjusted)

    # Step 5: Take first 5 scaled values and compute root mean square
    sample = scaled[:5]
    sum_squares = sum(x**2 for x in sample)
    rms = (sum_squares / len(sample)) ** 0.5

    # Step 6: Apply case-based adjustment using conditional expression
    category = 'high' if rms > 40 else 'low'
    multiplier = 1.2 if category == 'high' else 0.9

    # Step 7: Final score calculation (this is the key result)
    base_score = rms * multiplier
    penalty = 0
    for x in filtered:
        if x > 50:
            penalty += x * 0.05  # Minor penalty for large values

    final_score = base_score - penalty

    # Irrelevant tracking variables
    max_scaled = max(scaled) if scaled else 0
    total_pairs = len(pairs)
    debug_log = f"Processed {total_pairs} pairs"

    return final_score

# Main execution
benchmark_data = [12, 45, 8, 62, -3, 16, 91, 7]
interim_results = analyze_sequence([10, 20, 30])  # Dead call, no side effects
stability = validate_stability(interim_results)  # Result not used
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")