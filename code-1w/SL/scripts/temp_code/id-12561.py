import itertools

def analyze_text(text_block):
    # Irrelevant text analysis function (dead code path)
    words = text_block.split()
    word_lengths = [len(w) for w in words]
    avg_length = sum(word_lengths) / len(word_lengths) if words else 0
    return avg_length

def transform_data(data_seq):
    # Distractor: complex transformation with no impact on result
    shifted = [(x << 2) ^ 3 for x in data_seq]
    filtered = [y for y in shifted if y % 5 != 0]
    rolled = [filtered[-1]] + filtered[:-1] if filtered else []
    return rolled

def collect_metrics(raw_inputs):
    # Red herring metric collection
    base_values = [abs(x) + 2 for x in raw_inputs]
    temp_stats = {"max_val": max(base_values), "count": len(base_values)}
    processed = [b ** 0.5 for b in base_values]
    return processed

def compute_weighted_sum(items, weights):
    # Unused but plausible-looking function
    return sum(a * b for a, b in zip(items, weights))

def generate_key(signal):
    # Bit manipulation decoy
    key = 0
    for s in signal:
        key ^= (s * 7) & 0xF
        key = (key << 1) | (key >> 3)
    return key & 0xFF

def evaluate_performance(metrics):
    # Core logic hidden among distractions
    threshold = 4.75
    adjustment = 0.0
    
    # Real conditional logic chain (nested)
    if len(metrics) > 5:
        mean_metric = sum(metrics) / len(metrics)
        if mean_metric > threshold:
            adjustment += 15.0
            second_filter = [m for m in metrics if m > threshold]
            if len(second_filter) >= 3:
                # Further nested condition
                sorted_metrics = sorted(second_filter, reverse=True)
                top_three_avg = sum(sorted_metrics[:3]) / 3
                if top_three_avg > 5.0:
                    adjustment += 10.0
                    # Key branching point
                    for val in sorted_metrics:
                        if val > 6.0:
                            adjustment += 2.5
                            break
                else:
                    adjustment -= 5.0
        else:
            adjustment -= 8.0
    else:
        adjustment -= 20.0
    
    # Decoy operations below
    dummy_calc = sum([i * i for i in range(12)]) / 3.5  # Irrelevant math
    phantom_map = {k: k * 1.5 for k in range(7)}         # Dead dictionary
    unused_tuple = (dummy_calc, phantom_map[4], len(str(dummy_calc)))
    
    # Actual answer computation
    base_score = 100.0
    final_score = base_score + adjustment  # Critical assignment
    
    # More red herrings
    debug_info = f"Score adjusted by {adjustment:.1f} units."
    log_entry = debug_info.replace(".", "!").upper()
    padding = [0] * int(unused_tuple[2])
    
    return final_score

# Simulated input data
raw_signal = [1, 3, 7, 2, 8, 6, 9]
data_stream = [x * 1.1 for x in raw_signal]

# Irrelevant preprocessing
transformed_stream = transform_data([int(d) for d in data_stream])
analysis_result = analyze_text("Performance metrics are critical for evaluation")

# Real data preparation
cleaned_metrics = collect_metrics(raw_signal)
modified_metrics = [m + 0.2 for m in cleaned_metrics]
metric_set = [round(m, 2) for m in modified_metrics if m > 2.0]

# Add string processing distraction
tag_sequence = "abc-def-ghi-jkl"
segments = tag_sequence.upper().split('-')
segment_pairs = list(itertools.combinations(segments, 2))
pair_count = len(segment_pairs)

# Decoy function call
noise_key = generate_key(raw_signal)
weight_vector = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
suppress_warning = compute_weighted_sum(transformed_stream, weight_vector)

# Critical execution point
final_score = evaluate_performance(metric_set)
print(f"Result: {final_score}")