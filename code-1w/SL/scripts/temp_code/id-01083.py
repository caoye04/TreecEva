def analyze_text_data(text_blocks):
    char_count = 0
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    consonant_set = set('bcdfghjklmnpqrstvwxyz')
    block_stats = []

    for block in text_blocks:
        upper_block = block.upper()
        lower_block = block.lower()
        local_vowels = 0
        local_consonants = 0
        temp_shift = 0

        for char in block:
            if char.isalpha():
                char_count += 1
                if char.lower() in vowel_set:
                    local_vowels += 1
                elif char.lower() in consonant_set:
                    local_consonants += 1
            # Irrelevant bit manipulation distraction
            temp_shift = (temp_shift << 1) ^ ord(char)

        # Semi-relevant transformation
        processed_value = (local_vowels * 3) - (local_consonants // 2)
        block_stats.append(processed_value)

    # Distractor: unused variable and redundant computation
    total_shift_sum = sum([len(block) for block in text_blocks if len(block) > 5])

    def calculate_entropy(data_list):
        from math import log2
        abs_values = [abs(x) for x in data_list]
        total = sum(abs_values)
        if total == 0:
            return 0.0
        entropy = 0.0
        for v in abs_values:
            p = v / total
            if p > 0:
                entropy -= p * log2(p)
        return round(entropy, 4)

    entropy_metric = calculate_entropy(block_stats)

    # Core logic hidden among distractions
    metric_set = set(block_stats)
    baseline = {x for x in range(-10, 11)}

    # Key statement
    final_score = evaluate_performance(metric_set, baseline)
    
    return final_score


def evaluate_performance(metrics, base):
    overlap = metrics & base
    excess = metrics - base
    deficit = base - metrics
    
    score = len(overlap) * 10
    score -= len(excess) * 3
    score += len(deficit) % 7  # minor adjustment
    
    # Distractor: irrelevant recursion
    def recursive_checksum(n):
        if n <= 1:
            return n
        return recursive_checksum(n - 2) + (n % 4)
    
    _ = recursive_checksum(15)  # dead computation
    
    return score

# Execution entry point
text_samples = [
    "Dynamic reasoning over complex code",
    "Language model evaluation framework",
    "Enhanced cognitive load simulation"
]

result = analyze_text_data(text_samples)
print(f"Result: {result}")