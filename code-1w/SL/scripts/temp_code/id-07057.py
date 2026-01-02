import math

# Irrelevant helper function (dead code path)
def deprecated_normalizer(x):
    return [val / sum(x) for val in x]  # Unused

# Misleading data transformation chain
def obscure_shift(seq, factor=3):
    shifted = []
    for i in range(len(seq)):
        shifted.append(seq[i] ^ (factor * i % 256))  # Bit manipulation red herring
    return shifted

# Decoy metric with plausible but unused logic
def legacy_score(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance) if variance > 0.1 else 0.1  # Not used in main flow

# Core processing pipeline
activation_threshold = 0.75
def evaluate_response(x):
    return x > activation_threshold

def filter_active(nodes, mask):
    return [node for node, m in zip(nodes, mask) if m]

def integrate_signals(data_stream):
    base_accum = 0
    for val in data_stream:
        if val < 0.1:
            continue
        base_accum += math.log(val) * 2.718
    return round(base_accum, 4)

# Primary transformation using lambda abstraction
data_enhancer = lambda seq: [round(math.sin(x) + 0.5, 3) for x in seq if x % 0.5 != 0.25]

# Secondary filter with conditional expression
apply_correction = lambda x: x * 1.5 if x < 0.5 else x * 0.9

def process_sequence(raw):
    intermediate = []
    for item in raw:
        transformed = apply_correction(item)
        if transformed > 0.3:
            intermediate.append(transformed)
    return intermediate

# Complex data generator with multiple layers
raw_input_data = [0.88, 0.12, 0.63, 0.91, 0.27, 0.45, 0.73]

expanded_data = []
for d in raw_input_data:
    expanded_data.extend([d, d * 0.82])  # Augmenting data

# Apply non-linear enhancement
target_data = data_enhancer(expanded_data)

# Mask generation with logical operations
bool_mask = list(map(evaluate_response, target_data))

# Simulated hardware feedback (irrelevant)
hw_status_flags = [1 if x & 3 == 1 else 0 for x in range(len(target_data))]  # Distractor

# Signal integration stage
processed_signal = integrate_signals(target_data)

# Data enrichment via tuple unpacking and reassignment
meta_stats = (len(target_data), sum(target_data), processed_signal)
count, total, signal_value = meta_stats
enriched_metric = (total * signal_value) / (count or 1)

# Conditional data refinement
refined_candidates = []
if enriched_metric > 1.5:
    refined_candidates = process_sequence(target_data)
else:
    fallback_set = [x * 0.5 for x in target_data]
    refined_candidates = fallback_set  # Dead branch due to actual metric

# Transform step with misleading naming
transformed_data = []
scaling_factor = 1.1
for val in refined_candidates:
    adjusted = val * scaling_factor
    if adjusted > 0.2:
        transformed_data.append(round(adjusted, 3))

# Spurious set operation (red herring)
unique_caps = set([int(x * 100) for x in transformed_data if x > 0.5])
duplicate_buffer = [x for x in transformed_data if transformed_data.count(x) > 1]  # Computationally wasteful

# Core decision logic hidden among distractions
def process_metrics(dataset, threshold):
    # Logical aggregation with nested conditionals
    active_units = 0
    suppression_count = 0
    for reading in dataset:
        if reading > threshold:
            active_units += 1
        elif reading < threshold * 0.4:
            suppression_count += 1
    
    # Composite health index calculation
    stability_index = (active_units - suppression_count) * math.pi
    
    # Final diagnostic based on derived state
    if active_units >= 3:
        diagnostic_score = math.floor(stability_index * 100) / 100
    else:
        diagnostic_score = math.ceil(stability_index * 50) / 50
    
    return diagnostic_score

# Execution point of interest
final_diagnostic = process_metrics(transformed_data, activation_threshold)

# Output requirement
print(f"Target result: {final_diagnostic}")