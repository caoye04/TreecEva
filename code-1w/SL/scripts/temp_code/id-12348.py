import math

# Simulated bioinformatics data processing pipeline
def analyze_sequence(seq_data):
    base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for char in seq_data:
        if char in base_counts:
            base_counts[char] += 1
    total = sum(base_counts.values())
    gc_content = (base_counts['G'] + base_counts['C']) / total if total > 0 else 0
    return gc_content, total

# Irrelevant helper - decoy function
def compute_phred_score(quality_str):
    scores = [ord(ch) - 33 for ch in quality_str]
    mean_score = sum(scores) / len(scores) if scores else 0
    return mean_score  # Not used in final calculation

# Data normalization (partially relevant)
def normalize_values(raw_list):
    if not raw_list:
        return []
    max_val = max(raw_list)
    return [round(x / max_val, 6) for x in raw_list] if max_val != 0 else [0] * len(raw_list)

# Complex metric aggregator with red herrings
def calculate_enrichment(scores, threshold=0.5):
    enriched = [s for s in scores if s > threshold]
    depleted = [s for s in scores if s <= threshold]
    ratio = len(enriched) / len(depleted) if len(depleted) > 0 else 0
    return ratio * 100

# Set-based feature extractor
def extract_unique_kmers(sequence, k=3):
    kmers = set()
    for i in range(len(sequence) - k + 1):
        kmers.add(sequence[i:i+k])
    return kmers

# Main evaluation logic with distractions
def evaluate_performance(metrics, data):
    # Distractor variables
    temp_result = 0
    accumulator = []
    dummy_cache = {}
    
    # Real computation begins
    raw_metrics = [x * 1.75 for x in data.get('inputs', [])]
    normalized = normalize_values(raw_metrics)
    
    # Conditional branching based on control flag
    control_mode = data.get('mode') == 'strict'
    if control_mode:
        filtered = [n for n in normalized if n > 0.1]
    else:
        filtered = [n for n in normalized if n >= 0.05]
    
    # Bit manipulation red herring
    mask = 0b1101
    masked_values = [int(f * 100) & mask for f in filtered]
    
    # Set operations (required python feature)
    set_a = {i for i in range(1, 10) if i % 2 == 0}
    set_b = {i for i in range(5, 15) if i % 3 == 0}
    intersection_size = len(set_a & set_b)  # Used later
    
    # Another decoy: complex unused transformation
    def transform_nested(arr):
        return [[math.sin(x) for x in arr] for _ in range(2)]
    
    # Real path: conditional summation with rounding
    base_score = 0
    for v in filtered:
        if v > 0.5:
            base_score += math.log(v * 10 + 1)
        elif v > 0.2:
            base_score += math.sqrt(v * 5)
        else:
            base_score += v * 3
    
    # Integer division and rounding
    adjustment = (int(base_score) // 2) + intersection_size
    
    # Final computation chain
    penalty = 0
    if 'flags' in data:
        active_flags = len([f for f in data['flags'] if f.startswith('F_')])
        penalty = active_flags * 0.8
    
    # Key assignment - target of question
    final_score = round(base_score + adjustment - penalty, 4)
    
    # Dead code path - never executed due to logic
    if len(dummy_cache) > 100:
        cleanup = sum([transform_nested([v])[0][0] for v in masked_values])
        final_score -= cleanup
    
    return final_score

# Simulated dataset
benchmark_data = {
    'inputs': [12, 8, 23, 5, 16],
    'mode': 'relaxed',
    'version': '2.1a',
    'flags': ['F_OPTIMIZE', 'F_VALIDATE', 'DEBUG_OFF']
}

# Metric set using set operations
metric_set = extract_unique_kmers('ATGCATGC', 3)

# Unused but plausible intermediate
sequence_analysis = analyze_sequence('GGCTAGCTAA')
phred = compute_phred_score("!#$%&'()*")

# Critical execution point
final_score = evaluate_performance(metric_set, benchmark_data)

# Output result as required
print(f"Target result: {final_score}")