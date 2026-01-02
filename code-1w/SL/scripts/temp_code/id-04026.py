from collections import defaultdict, Counter

def preprocess_records(data_entries):
    processed = []
    temp_stats = defaultdict(int)
    for entry in data_entries:
        if not entry.strip():
            continue
        words = entry.lower().split()
        word_count = len(words)
        temp_stats['total_words'] += word_count
        temp_stats['entry_count'] += 1
        if word_count > 3:
            processed.append(entry.upper())
    return processed

def analyze_frequency(tokens):
    freq_map = {}
    for token in tokens:
        cleaned = ''.join(filter(str.isalpha, token))
        if cleaned:
            freq_map[cleaned] = freq_map.get(cleaned, 0) + 1
    sorted_keys = sorted(freq_map.keys())
    redundant_sum = sum(len(k) for k in sorted_keys)
    return freq_map

def calculate_final_score(dataset):
    score = 0
    char_counter = Counter()
    intermediate_values = []
    
    for item in dataset:
        length_factor = len(item)
        vowel_count = sum(1 for c in item if c in 'AEIOU')
        if length_factor > 5:
            adjustment = length_factor * 0.5
            intermediate_values.append(adjustment)
        else:
            adjustment = length_factor * 0.2
        score += vowel_count * adjustment
        
        for char in item:
            if char.isupper():
                char_counter[char] += 1
    
    # Irrelevant aggregation
    excess_total = sum(char_counter.values()) * 0.1
    intermediate_values.append(excess_total)
    
    # Actual logic step: finalize using specific pattern
    if len(intermediate_values) >= 3:
        peak = max(intermediate_values[:3])
        score -= peak  # deduction based on early peaks
    
    return int(score)

data_log = [
    "Signal Alpha active",
    "ERROR: retry limit exceeded",
    "Data stream stable",
    "Sync complete",
    "Update pending",
    "Initialization sequence"
]

processed_data = preprocess_records(data_log)
frequency_analysis = analyze_frequency(processed_data)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")