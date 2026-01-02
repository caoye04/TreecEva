import math

# Simulated bioinformatics data analysis pipeline
sample_reads = [248, 301, 192, 415, 267]
quality_scores = [0.88, 0.92, 0.75, 0.94, 0.81]
coverage_depth = [32, 45, 28, 51, 37]

def normalize(values):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [(x - mean_val) / std_dev for x in values]

def detect_outliers_zscore(data, threshold=2.0):
    z_scores = normalize(data)
    return {i for i, z in enumerate(z_scores) if abs(z) > threshold}

def compute_gc_content(read_length):
    # Simulated GC content based on read length
    return (read_length % 100) * 0.01

def calculate_enrichment_factor(observed, baseline=0.3):
    # Irrelevant function - decoy
    return (observed - baseline) / baseline

def generate_synthetic_controls(n):
    # Dead code path - never used
    return [math.sin(i * 0.5) for i in range(n)]

# Distractor: unused intermediate variables
raw_aggregate = sum(sample_reads) * 0.01
adjusted_threshold = 0.85 * max(quality_scores)
placeholder_matrix = [[0]*3 for _ in range(3)]

# Real processing begins
normalized_reads = normalize(sample_reads)
normalized_quality = normalize(quality_scores)

# Identify unreliable samples
outlier_indices_reads = detect_outliers_zscore(sample_reads)
outlier_indices_qual = detect_outliers_zscore(quality_scores)
unreliable_samples = outlier_indices_reads.union(outlier_indices_qual)

# Compute derived features
gc_contents = [compute_gc_content(r) for r in sample_reads]
enrichment_markers = [gc * q for gc, q in zip(gc_contents, quality_scores)]

# Simulated benchmark metrics (sets used for scoring)
precision_metric = sum(q for i, q in enumerate(normalized_quality) if i not in unreliable_samples)
sensitivity_metric = len([r for i, r in enumerate(normalized_reads) if i not in unreliable_samples and r > 0])
consistency_score = sum(1 for g in gc_contents if 0.3 <= g <= 0.7)
noise_level = sum(1 for i in range(len(sample_reads)) if i in unreliable_samples)

# Weight assignment (some weights are red herrings)
benchmark_weights = {
    'precision': 0.4,
    'sensitivity': 0.3,
    'consistency': 0.2,
    'noise_penalty': 0.0,  # Decoy weight - not actually used
    'stability': 0.1       # Another red herring
}

# Create metric set with relevant and irrelevant components
metric_set = {
    'precision': precision_metric,
    'sensitivity': sensitivity_metric,
    'consistency': consistency_score,
    'raw_read_count': sum(sample_reads),            # Irrelevant high-value distractor
    'average_quality': sum(quality_scores) / 5,     # Unused average
    'max_coverage': max(coverage_depth),            # Misleading extreme value
    'enrichment_factor': calculate_enrichment_factor(0.45)  # Decoy calculation
}

# Secondary distraction: complex but unused set operation
reference_metrics = {1, 2, 3, 4, 5}
overlap_check = reference_metrics.intersection({3, 4, 5, 6, 7})
disjoint_test = reference_metrics.isdisjoint({8, 9, 10})

# Core evaluation logic (only this part matters)
def evaluate_performance(metrics, weights):
    # Only use subset of keys that have non-zero weights
    actual_keys = {'precision', 'sensitivity', 'consistency'}
    score = 0.0
    for key in actual_keys:
        if key in metrics:
            w = weights[key]
            score += metrics[key] * w
    
    # Apply hidden correction based on noise
    noise_equivalent = metrics.get('noise_level', 0)  # Not in metric_set yet!
    corrected_score = score - (noise_equivalent * 0.05)
    
    # Backfill missing variable through indirect lookup
    all_available_keys = set(metrics.keys())
    if 'consistency' in all_available_keys:
        temp_store = {'temp': metrics['consistency']}
        del temp_store  # Obfuscation
    
    # Final adjustment using set existence check
    flag_comp = len(all_available_keys.difference({'raw_read_count', 'average_quality', 'max_coverage', 'enrichment_factor'}))
    if flag_comp >= 3:
        corrected_score += 0.1  # Small boost for sufficient valid metrics
    
    return corrected_score

# Insert missing key post-hoc to confuse tracing
metric_set['noise_level'] = noise_level

# Critical execution point
final_score = evaluate_performance(metric_set, benchmark_weights)

print(f"Result: {final_score}")