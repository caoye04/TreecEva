import itertools

def analyze_frequency(text_blocks):
    frequency_map = {}
    for block in text_blocks:
        cleaned = ''.join(ch.lower() for ch in block if ch.isalnum())
        for char in cleaned:
            frequency_map[char] = frequency_map.get(char, 0) + 1
    return frequency_map

def extract_vowel_runs(text_blocks):
    vowel_runs = []
    for block in text_blocks:
        current_run = 0
        for ch in block.lower():
            if ch in 'aeiou':
                current_run += 1
            else:
                if current_run > 0:
                    vowel_runs.append(current_run)
                current_run = 0
        if current_run > 0:
            vowel_runs.append(current_run)
    return vowel_runs

def compute_final_score(data_map):
    base = data_map['consonant_count']
    bonus = len(data_map['frequent_chars'])
    penalty = sum(1 for x in data_map['vowel_runs'] if x >= 3)
    adjustment = data_map['entropy'] * 10
    intermediate = (base + bonus) * 1.5 - penalty * 2
    final_score = int(intermediate + adjustment)
    return final_score

def dummy_statistical_analysis(seq):
    mean = sum(seq) / len(seq)
    variance = sum((x - mean) ** 2 for x in seq) / len(seq)
    return {'mean': mean, 'variance': variance}

def main():
    raw_logs = [
        "User1: Session started at 09:15AM",
        "Error: Failed login attempt from IP 192.168.1.105",
        "Success: Authentication passed for admin",
        "Data export initiated - format=CSV, size=256KB"
    ]

    # Irrelevant preprocessing step (distraction)
    timestamp_tokens = [entry.split(' ')[0] for entry in raw_logs if ':' in entry]
    action_keywords = {"started", "failed", "success", "initiated"}
    keyword_flags = [any(kw in log.lower() for kw in action_keywords) for log in raw_logs]

    # Core analysis (relevant)
    char_freq = analyze_frequency(raw_logs)
    vowel_runs = extract_vowel_runs(raw_logs)

    # Compute auxiliary metrics (some relevant, some not)
    vowels = set('aeiou')
    consonant_count = sum(count for char, count in char_freq.items() if char not in vowels)
    frequent_chars = [ch for ch, cnt in char_freq.items() if cnt > 2]

    # Dummy entropy-like calculation (semi-relevant)
    counts = list(char_freq.values())
    total = sum(counts)
    probabilities = [c / total for c in counts]
    entropy = -sum(p * p for p in probabilities)  # Simplified pseudo-entropy

    # Use itertools to generate unused combinations (distractor)
    _ = list(itertools.combinations_with_replacement(frequent_chars, 2))

    # Unused statistical analysis on vowel runs (dead code path)
    if len(vowel_runs) > 5:
        stats = dummy_statistical_analysis(vowel_runs)
    else:
        stats = {'mean': 0, 'variance': 0}  # Not used

    # Prepare data for scoring
    processed_data = {
        'consonant_count': consonant_count,
        'frequent_chars': frequent_chars,
        'vowel_runs': vowel_runs,
        'entropy': entropy
    }

    # Key statement
    final_score = compute_final_score(processed_data)

    # Print result
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()