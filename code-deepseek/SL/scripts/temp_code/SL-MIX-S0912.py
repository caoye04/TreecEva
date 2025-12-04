def compute_quality_metric(samples):
    # Distractor: unused quality check that looks important
    quality_threshold = 85.5
    temp_analysis = sum(len(str(s)) for s in samples) % 17
    
    # Main computation path with bitwise operations
    processed_data = []
    for sample in samples:
        # Red herring: unused computation
        fake_metric = (ord(sample[0]) << 2) & 0xFF
        
        # Actual processing - character analysis with case conversion
        char_count = Counter(sample.lower())
        vowel_weight = sum(char_count.get(v, 0) for v in 'aeiou')
        consonant_weight = len(sample) - vowel_weight
        
        # Bitwise XOR for obfuscation
        quality_factor = (vowel_weight ^ consonant_weight) & 0x1F
        processed_data.append(quality_factor)
    
    # Misleading intermediate calculation
    intermediate_sum = sum(processed_data) + temp_analysis
    
    # Dead code path that looks relevant
    if intermediate_sum > 100:
        backup_calc = intermediate_sum // 3
    else:
        backup_calc = intermediate_sum * 2
    
    # Final computation with modular arithmetic
    base_score = sum(processed_data)
    adjustment = (base_score % 7) * 3
    final_value = (base_score + adjustment) // len(processed_data)
    
    return final_value

# Sample data setup
from collections import Counter
data_samples = ['QualityCheck', 'AnalysisTool', 'MetricSystem', 'EvaluationKit']

# Multiple irrelevant variables for distraction
config_param = 42.7
cache_size = 1024
performance_flag = True
validation_set = ['TestA', 'TestB']

# Main execution
final_score = compute_quality_metric(data_samples)
print(f"Result: {final_score}")