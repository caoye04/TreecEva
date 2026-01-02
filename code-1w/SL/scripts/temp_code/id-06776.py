from collections import defaultdict
import math

def analyze_frequency(text):
    freq = defaultdict(int)
    for char in text.lower():
        if char.isalpha():
            freq[char] += 1
    return freq

def normalize_vector(vec):
    magnitude = math.sqrt(sum(x**2 for x in vec.values()))
    return {k: v / magnitude for k, v in vec.items()} if magnitude > 0 else vec

def calculate_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def filter_outliers(nums):
    if len(nums) < 2:
        return nums
    mean_val = sum(nums) / len(nums)
    std_dev = math.sqrt(sum((x - mean_val)**2 for x in nums) / len(nums))
    return [x for x in nums if abs(x - mean_val) <= 2 * std_dev]

def extract_vowel_consonant_ratio(freq_dict):
    vowels = sum(freq_dict[v] for v in 'aeiou' if v in freq_dict)
    consonants = sum(freq_dict[c] for c in freq_dict if c.isalpha() and c not in 'aeiou')
    return round(vowels / consonants if consonants != 0 else 0, 4)

def process_metrics(raw_data, importance_weights):
    # Step 1: Character frequency analysis
    char_freq = analyze_frequency(''.join(raw_data))
    
    # Irrelevant intermediate: vowel-consonant ratio (not used later)
    _ = extract_vowel_consonant_ratio(char_freq)
    
    # Step 2: Normalize frequencies
    norm_freq = normalize_vector(char_freq)
    
    # Step 3: Compute entropy of normalized distribution
    entropy_metric = calculate_entropy(list(norm_freq.values()))
    
    # Step 4: Prepare numeric metrics from string lengths
    lengths = [len(s) for s in raw_data]
    filtered_lengths = filter_outliers(lengths)
    avg_length = sum(filtered_lengths) / len(filtered_lengths) if filtered_lengths else 0
    
    # Step 5: Weighted combination of metrics
    weight_entropy = importance_weights.get('entropy', 0.6)
    weight_length = importance_weights.get('length', 0.4)
    
    # Distractor computation: unused statistical moment
    variance = sum((x - avg_length) ** 2 for x in filtered_lengths) / len(filtered_lengths) if filtered_lengths else 0
    skewness_proxy = sum((x - avg_length) ** 3 for x in filtered_lengths) / (len(filtered_lengths) * (variance ** 1.5)) if variance > 0 else 0
    
    # Final score calculation (only entropy and length matter)
    final_score = (entropy_metric * weight_entropy) + (avg_length * weight_length)
    
    # Debug-style irrelevant assignment
    debug_info = {'processed': True, 'version': '2.1', 'timestamp': 123456789}
    
    return round(final_score, 4)

# Main execution
if __name__ == '__main__':
    data = [
        'Quantum computing leverages superposition and entanglement.',
        'Classical algorithms cannot efficiently simulate quantum systems.',
        'Shor\'s algorithm factors large integers exponentially faster.',
        'Grover\'s search provides quadratic speedup for unstructured databases.',
        'Quantum error correction is vital for fault-tolerant computation.'
    ]
    
    weights = {
        'entropy': 0.65,
        'length': 0.35
    }
    
    # Red herring variable
    temp_results = [len(d.split()) for d in data]
    word_density = sum(temp_results) / len(data)
    
    # Key statement
    final_score = process_metrics(data, weights)
    
    print(f"Result: {final_score}")