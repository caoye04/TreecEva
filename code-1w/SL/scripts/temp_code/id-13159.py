from collections import defaultdict

# Simulate system benchmark data with noise and metadata
def generate_benchmark_data():
    raw_scores = [88, 92, 76, 94, 85, 90, 83]
    timestamps = ['t1', 't2', 't3', 't4', 't5', 't6', 't7']
    categories = ['cpu', 'mem', 'io', 'cpu', 'net', 'mem', 'cpu']
    
    # Assemble clean data with extraneous calculations
    temp_offset = sum([x % 7 for x in raw_scores])  # Irrelevant offset
    scale_factor = len(timestamps) / (len(categories) - categories.count('cpu') + 1)
    
    data = []
    for i, score in enumerate(raw_scores):
        entry = {
            'id': i,
            'score': score + (i % 3),  # Artificial minor inflation
            'cat': categories[i],
            'ts': timestamps[i],
            'weight': 1.0 if categories[i] == 'cpu' else 0.8
        }
        data.append(entry)
    
    return data, scale_factor, temp_offset

# Analyze performance with distraction computations
def calculate_performance(data):
    category_total = defaultdict(float)
    category_count = defaultdict(int)
    cumulative_product = 1  # Unused accumulator (distraction)
    
    # Track max score per category (semi-relevant)
    max_scores = {}
    
    for item in data:
        cat = item['cat']
        score = item['score']
        weight = item['weight']
        
        # Update totals
        category_total[cat] += score * weight
        category_count[cat] += 1
        
        # Update max (not used later)
        if cat not in max_scores or score > max_scores[cat]:
            max_scores[cat] = score
        
        # Distracting computation
        cumulative_product *= (score % 10 + 1)
        if cumulative_product > 10000:
            cumulative_product = cumulative_product // 10
    
    # Compute weighted average across all entries
    total_weighted = 0
    total_entries = 0
    
    for i, item in enumerate(data):
        # Use enumerate to introduce index-based logic (some unused)
        bonus = 0.5 if i % 2 == 0 else 0  # Unused bonus term
        total_weighted += item['score'] * item['weight']
        total_entries += 1
    
    overall_avg = total_weighted / total_entries
    
    # Secondary metric: stability score based on consecutive differences
    diffs = []
    for i in range(1, len(data)):
        prev = data[i-1]['score']
        curr = data[i]['score']
        diffs.append(abs(curr - prev))
    
    stability_score = 10 - (sum(diffs) / len(diffs)) if diffs else 10
    
    # Final composite score with fixed formula
    base_component = overall_avg * 0.8
    stability_component = stability_score * 1.5
    final_score = int(base_component + stability_component)  # Deterministic integer result
    
    # Dead code path (never executed but looks relevant)
    if False:
        fallback = sum(category_total.values()) // len(category_total)
        final_score = max(final_score, fallback)
    
    return final_score

# Main execution
benchmark_data, factor, offset = generate_benchmark_data()

# Additional irrelevant processing
reversed_data = benchmark_data[::-1]  # Slicing without impact
enumerated_pairs = list(enumerate(zip(benchmark_data, reversed_data)))
dummy_counter = sum(1 for _ in filter(lambda x: x[1][0]['id'] % 2 == 0, enumerated_pairs))

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")