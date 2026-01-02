def process_timestamps(log_entries):
    # Irrelevant function: processes strings but not used in final result
    cleaned = []
    for entry in log_entries:
        if 'ERROR' in entry:
            cleaned.append(entry.strip().upper())
    return [len(c) for c in cleaned]


def decode_shift_cipher(text):
    # Distractor function: performs character shifting (unused)
    result = ''
    for char in text:
        if char.isalpha():
            shift = 13
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def analyze_pattern(seq):
    # Dead-end analysis with misleading intermediate values
    peak_count = 0
    trend = []
    for i in range(1, len(seq)-1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            peak_count += 1
            trend.append(i)
    magnitude = sum([seq[t] for t in trend]) if trend else 0
    return peak_count * magnitude  # Not used


def validate_sequence(nums):
    # Complex validation with red herring logic
    if len(nums) < 5:
        return False
    sorted_check = sorted(nums)
    duplicates = len(nums) - len(set(nums))
    checksum = sum(n*n for n in nums[:4]) % 17
    return checksum == 10 and duplicates <= 2


def compute_weighted_sum(records, factor):
    # Heavily nested logic with partial relevance
    total = 0
    weights = [0.1, 0.2, 0.3, 0.4]
    adjustments = []
    
    for i, record in enumerate(records):
        temp_val = 0
        if isinstance(record, dict) and 'value' in record:
            raw = record['value']
            if raw > 0:
                for w in weights:
                    temp_val += raw * w
            else:
                temp_val = abs(raw) ** 0.5
            adjustments.append(temp_val * 0.05)
        total += temp_val
    
    # Only this line matters for final answer
    total += factor * len(adjustments)
    return int(total)


def evaluate_performance(log, threshold):
    score = 0
    critical_values = []
    
    # Real computation begins
    for item in log:
        if isinstance(item, str):
            # Use string method to extract numeric part
            digits = ''.join([c for c in item if c.isdigit()])
            if digits:
                num = int(digits)
                if num % 2 == 0:
                    score += num // 4
                else:
                    score -= num % 3
        elif isinstance(item, int):
            critical_values.append(item)
    
    # Core calculation path
    filtered = [v for v in critical_values if v > threshold]
    if filtered:
        average = sum(filtered) / len(filtered)
        score += int(average)
    
    # Secondary adjustment using string length side-channel
    metadata_tag = "perf_log_2024"
    tag_value = len(metadata_tag.replace('_', ''))  # 11
    score += tag_value
    
    # Final interference: recursive decoy that doesn't affect output
    def decoy_accumulate(n):
        if n <= 1:
            return 1
        return n + decoy_accumulate(n-2)  # Never called
    
    return score

# Main execution
if __name__ == '__main__':
    data_log = [
        'error_204', 'warning_105', 'info_308',
        42, 55, 68, 77,  # Integers mixed in
        'debug_112', 'fatal_309',
        83, 91
    ]
    
    base_threshold = 50
    
    # Irrelevant preliminary calls (distractors)
    _ = process_timestamps(data_log)
    _ = decode_shift_cipher('hello world')
    _ = analyze_pattern([3, 6, 2, 7, 5, 9, 1])
    _ = validate_sequence([4, 7, 4, 9, 2])
    
    # Semi-relevant but not final
    interim = compute_weighted_sum([
        {'value': 20}, {'value': 30}, {'value': -10}
    ], 2)
    
    # Key statement
    final_score = evaluate_performance(data_log, base_threshold)
    
    print(f"Target result: {final_score}")