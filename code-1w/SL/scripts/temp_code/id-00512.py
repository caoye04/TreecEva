import itertools

# Simulated sensor fusion system for environmental monitoring
# Real data processing with extensive red herrings and irrelevant transformations

def normalize readings):
    max_val = max(readings)
    return [x / max_val for x in readings]

def calculate_entropy(data):
    # Irrelevant entropy calculation (dead-end function)
    from math import log2
    total = sum(data)
    probabilities = [x / total for x in data if x > 0]
    return -sum(p * log2(p) for p in probabilities)

def apply_filter(signal, kernel=[0.25, 0.5, 0.25]):
    # Unused signal processing filter
    result = []
    for i in range(1, len(signal)-1):
        conv = signal[i-1]*kernel[0] + signal[i]*kernel[1] + signal[i+1]*kernel[2]
        result.append(conv)
    return result

def analyze_pattern(seq):
    # Distractor: pattern analysis that isn't used in final logic
    runs = 0
    for i in range(1, len(seq)):
        if seq[i] != seq[i-1]:
            runs += 1
    return runs % 7

def generate_combinations(values):
    # Creates combinatorial distraction
    combs = []
    for r in range(2, 4):
        combs.extend(itertools.combinations(values, r))
    return len(combs)  # This result is never used

def assess_risk_level(value):
    # Misleading risk assessment not used in final score
    if value < 30:
        return 'LOW'
    elif value < 70:
        return 'MEDIUM'
    else:
        return 'HIGH'

# Core evaluation logic buried among distractions
weights = [0.4, 0.3, 0.2, 0.1]

# Simulated input metrics (real data)
metrics = [
    85,     # air_quality_index (critical)
    42,     # humidity_pct (relevant)
    19,     # temperature_c (relevant)
    67      # noise_level_db (relevant)
]

# Extensive irrelevant preprocessing
raw_data = [78, 92, 65, 88, 71]
scaled_data = normalize(raw_data)
decoy_entropy = calculate_entropy(scaled_data)
filtered_signal = apply_filter(raw_data)
pattern_runs = analyze_pattern([1,1,0,0,1,1,1])
combination_count = generate_combinations([3,6,9,12])

# Fake risk assessments to mislead reasoning
risk_air = assess_risk_level(metrics[0])
risk_humidity = assess_risk_level(metrics[1])
risk_temp = assess_risk_level(metrics[2])
risk_noise = assess_risk_level(metrics[3])

# Decoy statistical calculations
mean_metric = sum(metrics) / len(metrics)
weighted_sum_decoy = sum(m * w for m, w in zip(metrics, [0.1, 0.2, 0.3, 0.4]))  # wrong weights!

# Actual core logic (obscured by context)
def evaluate_performance(mets, wts):
    # Normalize metrics to 0-100 scale if needed (already are)
    adjusted = []
    for i, val in enumerate(mets):
        if i == 0:  # air quality: higher is worse
            adjusted.append(100 - val)
        elif i == 2:  # temperature: optimal around 20
            deviation = abs(val - 20)
            score = max(0, 100 - deviation * 5)
            adjusted.append(score)
        else:  # humidity and noise: lower is better
            adjusted.append(100 - val)
    
    # Apply correct weights
    final = sum(val * weight for val, weight in zip(adjusted, wts))
    return round(final, 4)

# Key computation
intermediate_check = list(itertools.accumulate(metrics, lambda a,b: (a+b)//2))
verification_key = intermediate_check[-1] * 2  # Red herring check

# Critical statement
final_score = evaluate_performance(metrics, weights)

# Output required result
print(f"Result: {final_score}")