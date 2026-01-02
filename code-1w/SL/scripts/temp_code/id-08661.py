import math

def analyze_trend(data):
    # Irrelevant helper function (dead code path)
    return sum(x ** 2 for x in data if x > 0)

def preprocess_signal(signal):
    # Distractor: complex but unused transformation
    filtered = [x for x in signal if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    smoothed = [(normalized[i] + normalized[i-1]) / 2 for i in range(1, len(normalized))]
    return smoothed + [0] * (len(signal) - len(smoothed))

def transform_features(features):
    # Another decoy function with red herring logic
    transformed = []
    for f in features:
        if f < 0:
            transformed.append(math.log(abs(f) + 1) * -1)
        elif f == 0:
            transformed.append(0.5)
        else:
            transformed.append(math.sqrt(f))
    return transformed[::-1]

def calculate_entropy(seq):
    # Unused advanced calculation to mislead
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 4)

def evaluate_performance(metrics, weights):
    # Core relevant logic starts here
    base_scores = [m * 2 for m in metrics]  # Step 1: scale metrics
    adjusted = []
    for i, score in enumerate(base_scores):
        if i % 2 == 0:
            adjusted.append(score + 10)
        else:
            adjusted.append(score - 5)
    
    # Introduce modular arithmetic and conditional branching
    temp_result = 0
    for i in range(len(adjusted)):
        if adjusted[i] > 0:
            temp_result += (adjusted[i] ** 2) % 7  # Step 2: non-linear mod transform
        else:
            temp_result -= abs(adjusted[i]) % 5
    
    # Bit manipulation distraction embedded in real logic
    binary_flag = 0b1010
    shift_offset = (temp_result >> 2) & 0b111
    
    # Real dependency on prior result
    intermediate = temp_result ^ shift_offset  # Step 3: XOR with shifted bits
    
    # List slicing used meaningfully
    windowed = adjusted[1:6:2]  # Step 4: slice every other element from index 1 to 5
    
    # Conditional recursion (simple)
    def recursive_bonus(n):
        if n <= 1:
            return 1
        return n + recursive_bonus(n // 2)
    
    bonus = recursive_bonus(len(windowed))  # Step 5: recursive contribution
    
    # Weighted sum with distractor weights
    weighted_total = 0
    for i in range(len(windowed)):
        weighted_total += windowed[i] * weights[i % len(weights)]
    
    # Final composition
    final_score = intermediate + weighted_total + bonus  # Step 6-8+: combine all paths
    
    # Irrelevant print statements and unused vars
    debug_trace = [math.sin(x) for x in adjusted[:3]]
    max_window_value = max(windowed) if windowed else 0
    padding_factor = len(metrics) % 4
    
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input setup
    metrics = [3, -1, 4, 1, -5, 9, 2]
    weights = [0.5, 1.5, 2.0]

    # Unused variables - red herrings
    raw_data_stream = [0.1, -0.3, 0.4, 0.0, 0.2]
    calibration_sequence = list(range(7, 14))
    feature_set = [math.exp(i) for i in range(5)]
    signal_input = [-0.5, 0.8, -1.2, 0.9]

    # Critical statement
    final_score = evaluate_performance(metrics, weights)
    
    # Additional noise
    entropy_metric = calculate_entropy([1, 1, 0, 1, 0, 0, 1])
    processed_signal = preprocess_signal(signal_input)
    transformed_feats = transform_features(feature_set)
    trend_analysis = analyze_trend(calibration_sequence)

    print(f"Result: {final_score}")