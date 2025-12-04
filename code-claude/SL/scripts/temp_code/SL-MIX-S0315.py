def calculate_bit_strength(signal):
    # Calculate signal strength based on binary representation
    binary = bin(signal)[2:]
    ones_count = binary.count('1')
    zeros_count = binary.count('0')
    # Misleading calculation that's not used
    strength_factor = ones_count * 3 - zeros_count * 2
    return ones_count - zeros_count

def analyze_frequency(signals):
    # Analyze frequency distribution (distractor function)
    frequency_map = {}
    for s in signals:
        if s % 7 == 0:
            frequency_map[s] = frequency_map.get(s, 0) + 2
        else:
            frequency_map[s] = frequency_map.get(s, 0) + 1
    return frequency_map

def calculate_priority(signals):
    if not signals:
        return 0
    
    # Relevant computation mixed with distractors
    base_value = sum(signals) // len(signals)
    
    # Misleading calculations
    harmonic_mean = len(signals) / sum(1/s if s != 0 else 0.001 for s in signals)
    variance = sum((s - base_value) ** 2 for s in signals) / len(signals)
    
    # Extract unique values (relevant)
    unique_signals = set(signals)
    unique_count = len(unique_signals)
    
    # Distractor operations
    signal_product = 1
    for s in signals[:3]:
        signal_product *= (s % 10)
    
    # The actual calculation that matters
    bit_scores = [calculate_bit_strength(s) for s in unique_signals]
    priority = base_value + sum(bit_scores)
    
    # More distractor calculations
    weighted_sum = sum(s * (i+1) for i, s in enumerate(sorted(signals)))
    normalized_factor = (weighted_sum % 100) / 25
    
    return priority

# Main signal processing pipeline
signal_data = [18, 23, 45, 12, 23, 42, 18, 36]
backup_signals = [10, 15, 20, 25, 30]
processing_flags = {'normalize': True, 'filter_duplicates': False, 'enhance': True}

# Misleading preprocessing
enhanced_signals = [s * 2 if processing_flags['enhance'] else s for s in signal_data]
if processing_flags['normalize']:
    max_signal = max(enhanced_signals)
    normalized_signals = [s / max_signal * 100 for s in enhanced_signals]
else:
    normalized_signals = enhanced_signals.copy()

# Signal filtering - part that matters
if processing_flags['filter_duplicates']:
    filtered_signals = list(set(signal_data))
else:
    filtered_signals = signal_data.copy()

# Distractor processing steps
lambda_transform = lambda x: x**2 - x + 41
transformed_signals = list(map(lambda_transform, normalized_signals))

# Quality metrics (distractor)
quality_index = sum(transformed_signals) / len(transformed_signals)
variance_metric = sum((s - quality_index)**2 for s in transformed_signals) / len(transformed_signals)

# The key calculation
priority_score = calculate_priority(filtered_signals)

# Distractor post-processing
if variance_metric > 1000:
    priority_score += 10
elif quality_index > 100:
    priority_score -= 5

print(f"Result: {priority_score}")