from collections import defaultdict, Counter
import math

# Simulate multi-stage industrial processing with quality filtering and resource optimization

def preprocess_input(raw_streams):
    stream_metrics = defaultdict(float)
    for idx, (name, data) in enumerate(raw_streams.items()):
        if 'contaminant' in data:
            level = data['contaminant']
            if level > 0.5:
                continue
        stream_metrics[name] += sum(data.get('elements', [])) * (1 - data.get('impurity', 0))
    return stream_metrics

# Irrelevant helper - looks important but unused in critical path
def deprecated_normalization(vec):
    norm = sum(x**2 for x in vec) ** 0.5
    return [x / norm for x in vec] if norm else vec

# Decoy function that appears related but is never called
def legacy_calibrate(x):
    return (x * 1.047) % 1.0

# Core transformation pipeline
def transform_elements(elements):
    transformed = []
    for val in elements:
        if val <= 0:
            continue
        # Apply non-linear response
        adjusted = math.log(val) * math.sin(val)
        if abs(adjusted) > 0.1:
            transformed.append(round(adjusted * 100) / 100)
    return transformed

# Data aggregation with distractor logic
def aggregate_batches(batch_list):
    summary_stats = {}
    total_weight = 0
    null_count = 0  # red herring

    for i, batch in enumerate(batch_list):
        weight = batch.get('weight', 1.0)
        readings = batch.get('readings', [])
        
        # Distractor: complex-looking but unused calculation
        entropy = 0
        freq = Counter(readings)
        for r in freq.values():
            if r > 0:
                entropy -= (r / len(readings)) * math.log(r / len(readings)) if len(readings) > 0 else 0
        
        # Relevant computation
        valid_readings = [r for r in readings if r > 0.2]
        if valid_readings:
            avg = sum(valid_readings) / len(valid_readings)
            summary_stats[f'batch_{i}'] = avg * weight
            total_weight += weight
    
    # Final weighted aggregation - this is used later
    if total_weight == 0:
        return 0.0
    return sum(summary_stats.values()) / total_weight

# Main processing with nested logic and decoy branches
def calculate_optimal_yield(data_map):
    intermediate_results = []
    buffer_store = []  # unused collection - distraction

    for key, values in data_map.items():
        if not isinstance(values, list) or len(values) == 0:
            continue
        
        # Filter using multiple conditions
        filtered = [v for v in values if v > 0.1 and math.sqrt(v) < 3.0]
        
        # Bit manipulation decoy - looks technical but irrelevant
        flag = len(filtered) & 1
        mask = (1 << 4) - 1
        masked = len(filtered) & mask
        
        # Real signal extraction
        if len(filtered) >= 3:
            # Use every second element after threshold
            selected = [filtered[i] for i in range(0, len(filtered), 2)]
            if selected:
                base_score = sum(selected) / len(selected)
                # Non-obvious correction factor from earlier stage
                adjustment = math.cos(len(values))
                intermediate_results.append(base_score + adjustment)
    
    # Critical: only one of these paths contributes to final answer
    if len(intermediate_results) > 2:
        # Use median-like behavior without actually sorting fully
        sorted_res = sorted(intermediate_results)
        mid_idx = len(sorted_res) // 2
        primary_estimate = sorted_res[mid_idx]
    else:
        # Dead branch - misleading fallback
        primary_estimate = sum(intermediate_results) / len(intermediate_results) if intermediate_results else 0.0

    # Final nonlinear scaling
    yield_value = (primary_estimate ** 2) * math.pi
    return round(yield_value, 6)

# Entry point with layered setup and noise
if __name__ == '__main__':
    # Raw input data - realistic domain structure
    raw_material_streams = {
        'stream_alpha': {'elements': [2.1, 3.5, 1.8], 'impurity': 0.12},
        'stream_beta': {'elements': [0.9, 1.3, 4.2, 5.1], 'impurity': 0.33, 'contaminant': 0.7},
        'stream_gamma': {'elements': [1.7, 2.9, 3.3, 4.0], 'impurity': 0.08},
        'stream_delta': {'elements': [], 'impurity': 0.5},
        'stream_epsilon': {'elements': [2.5, 1.9, 3.1], 'impurity': 0.15}
    }
    
    # Step 1: Preprocess streams
    cleaned_streams = preprocess_input(raw_material_streams)
    
    # Step 2: Transform each stream's data
    transformed_data = {}
    for name, value in cleaned_streams.items():
        # Wrap scalar into list for uniform handling
        dummy_elements = [value * 1.5] * 3
        transformed = transform_elements(dummy_elements)
        if transformed:
            transformed_data[name] = transformed
    
    # Step 3: Create batch-like structures (some invalid)
    batches = [
        {'weight': 2.0, 'readings': [0.15, 0.25, 0.35, 0.45]},
        {'weight': 1.5, 'readings': [0.05, 0.10, 0.20]},  # below threshold
        {'weight': 3.0, 'readings': [0.30, 0.32, 0.38, 0.41, 0.49]},
        {'weight': 1.0, 'readings': []}
    ]
    
    # Step 4: Aggregate batch metrics (used as side signal)
    batch_aggregate = aggregate_batches(batches)
    
    # Step 5: Prepare processed data for yield calculation
    processed_data = {}
    for label, vals in transformed_data.items():
        extended_vals = vals + [batch_aggregate]  # inject aggregate - subtle coupling
        processed_data[label] = [x + 0.1 for x in extended_vals]  # minor shift
    
    # Key statement: compute final yield
    final_yield = calculate_optimal_yield(processed_data)
    
    # Output result as required
    print(f"Target result: {final_yield}")