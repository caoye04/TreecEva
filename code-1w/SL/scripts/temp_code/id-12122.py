import math

def preprocess_items(raw_list, threshold=5.0):
    temp_result = []
    outlier_count = 0
    for item in raw_list:
        if isinstance(item, str) and len(item) > 10:
            outlier_count += 1
            continue
        if isinstance(item, (int, float)) and item > threshold:
            temp_result.append(item * 0.9)
    return temp_result


def transform_coordinates(coords):
    # Irrelevant geometric transformation (dead-end function)
    transformed = []
    for x, y in coords:
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        transformed.append((r, theta))
    return transformed


def compute_entropy(data):
    # Distractor: computes entropy but not used in final path
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)


def analyze_patterns(sequence):
    pattern_metrics = {}
    running_sum = 0
    flip_flag = False
    
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            running_sum += val ** 2
        elif i % 2 == 0:
            running_sum -= val
        else:
            running_sum += abs(val) // 2
            
        if val > 15:
            flip_flag = not flip_flag
    
    pattern_metrics['sum_sq'] = running_sum
    pattern_metrics['flag_state'] = int(flip_flag)
    return pattern_metrics


def main_pipeline(input_data):
    # Step 1: Filtering and scaling
    stage_one = preprocess_items(input_data)
    
    # Dead-end assignment
    placeholder_matrix = [[i * j for j in range(3)] for i in range(3)]
    unused_stat = sum(sum(row) for row in placeholder_matrix)
    
    # Step 2: Pairwise zipping with offset indices
    indexed = list(enumerate(stage_one))
    paired = list(zip([x[1] for x in indexed], [x[0] for x in indexed]))
    
    # Step 3: Conditional filtering based on index parity
    filtered_pairs = []
    for val, idx in paired:
        if idx % 2 == 0:
            filtered_pairs.append(val + 1.5)
        else:
            filtered_pairs.append(val - 0.5)
    
    # Step 4: Simulate signal processing
    signal_buffer = []
    for v in filtered_pairs:
        if v < 8:
            signal_buffer.append(v * 1.8)
        elif v > 12:
            signal_buffer.append(v * 0.7)
        else:
            signal_buffer.append(v)
    
    # Step 5: Compute moving average of window size 2 (with overlap)
    smoothed = []
    for i in range(len(signal_buffer) - 1):
        avg_val = (signal_buffer[i] + signal_buffer[i+1]) / 2.0
        smoothed.append(avg_val)
    
    # Step 6: Apply modulo-based selection
    selected = []
    for i, val in enumerate(smoothed):
        if (i + 1) % 3 != 0:  # Skip every third element
            selected.append(val)
    
    # Step 7: Calculate statistical summary (only mean used later)
    stats = {
        'min': min(selected),
        'max': max(selected),
        'mean': sum(selected) / len(selected),
        'count': len(selected)
    }
    
    # Step 8: Secondary analysis on original structure
    dummy_coords = [(1, 2), (3, 4), (5, 6)]
    polar_form = transform_coordinates(dummy_coords)  # Unused
    
    # Step 9: Analyze bit patterns in indices (red herring)
    bit_analysis = 0
    for i in range(len(selected)):
        bit_analysis ^= (i & (i - 1))  # complex-looking but irrelevant
    
    # Step 10: Final aggregation
    processed_data = {
        'values': selected,
        'summary': stats,
        'auxiliary': {'bit_noise': bit_analysis, 'placeholder': unused_stat}
    }
    
    return processed_data


def aggregate_results(data_package):
    values = data_package['values']
    mean_val = data_package['summary']['mean']
    adjustment = 0.0
    
    for i, v in enumerate(values):
        if v > mean_val:
            adjustment += 0.3
        elif v < mean_val:
            adjustment -= 0.2
    
    base = sum(v ** 0.5 for v in values if v > 0)  # sum of square roots
    penalty = len([v for v in values if v < 10]) * 0.4
    final_score = round(base + adjustment - penalty, 6)
    
    # Critical print for traceability
    print(f"Result: {final_score}")
    return final_score

# --- Execution Entry Point ---
if __name__ == '__main__':
    raw_input_stream = [2, 'long_string_value', 7, 3, 16, 9, 'tiny', 11, 4]
    
    # Unused side computation: character frequency map
    char_freq = {}
    for entry in raw_input_stream:
        if isinstance(entry, str):
            for c in entry:
                char_freq[c] = char_freq.get(c, 0) + 1
    
    # Another decoy: combinatorics on indices
    index_pairs = [(a, b) for a in range(3) for b in range(3) if a != b]
    pair_product_sum = sum(a * b for a, b in index_pairs)
    
    # Core execution path
    data_context = main_pipeline(raw_input_stream)
    final_score = aggregate_results(data_context)