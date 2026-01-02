from itertools import combinations

def analyze_pattern(sequence):
    char_freq = {}
    for char in sequence:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Distractor: unused frequency transformation
    normalized = {k: v / len(sequence) for k, v in char_freq.items()}
    
    # Relevant: count how many characters appear exactly twice
    double_chars = sum(1 for count in char_freq.values() if count == 2)
    
    # Distractor: irrelevant pair generation
    pairs = list(combinations(sequence, 2))
    long_pairs = [p for p in pairs if ord(p[1]) - ord(p[0]) > 2]

    return double_chars

def compute_aggregate(text_data, threshold):
    segments = text_data.split('|')
    total_weight = 0
    temp_buffer = []
    
    for seg in segments:
        stripped = seg.strip()
        
        # Conditional logic with side accumulation (semi-relevant)
        if len(stripped) > threshold:
            score = analyze_pattern(stripped)
            adjustment = 1 if stripped[0].islower() else -1
            total_weight += score * adjustment
            temp_buffer.append(stripped[:3])
        else:
            # Dead code path (rarely triggered)
            if 'x' in stripped:
                total_weight -= 1

    # Distractor: buffer processing that doesn't affect output
    unique_starts = set(temp_buffer)
    bonus = len(unique_starts) if len(unique_starts) % 2 == 0 else 0

    # Final computation (answer depends only on total_weight)
    final_score = total_weight + bonus  # bonus always 0 due to input
    return final_score

# Input constructed so bonus = 0 (unique_starts has odd length)
data_input = "aabb|ccdd|effe|ghhg|ijji"
result = compute_aggregate(data_input, 3)
Result: {result}