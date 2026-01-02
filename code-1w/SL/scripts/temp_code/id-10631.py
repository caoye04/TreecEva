def analyze_frequency(text):
    freq = {}
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            freq[lower_char] = freq.get(lower_char, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return [item[0] for item in sorted_freq]


def generate_weights(n):
    weights = []
    for i in range(1, n+1):
        weight = (i ** 2) / (n * (n + 1) / 2)
        weights.append(weight)
    return weights

def validate_sequence(seq):
    if not seq:
        return False
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            return False
    return True

def process_segments(data, limit):
    segments = data.split('|')
    temp_result = 0
    cumulative = []
    
    for seg in segments:
        stripped = seg.strip()
        if not stripped:
            continue
            
        # Real computation path
        length = len(stripped)
        vowel_count = sum(1 for c in stripped if c.lower() in 'aeiou')
        ratio = vowel_count / length if length > 0 else 0
        
        # Distractor: frequency analysis not used in final result
        _ = analyze_frequency(stripped)
        
        # Distractor: weight generation with no impact
        if length > limit:
            _ = generate_weights(length)

        # Conditional expression (required Python feature)
        score = (ratio * 100) if vowel_count > 0 else (length * 2)
        
        # State tracking with some irrelevant transformations
        transformed = [ord(c) % 10 for c in stripped]
        _ = validate_sequence(transformed)  # Dead function call
        
        temp_result += int(score)
        cumulative.append(temp_result)
    
    # Final manipulation
    adjustment = len(cumulative) * 3 if cumulative else 0
    final_score = temp_result + adjustment
    
    # Irrelevant sorting of cumulative history
    _ = sorted(cumulative, reverse=True)
    
    return final_score

# Main execution
raw_data = "Education|Philosophy|Neuroscience|Quantum|"  
threshold = 7
intermediate = raw_data.replace('e', 'E').replace('o', 'O')
segment_data = intermediate[:-1]  # Remove trailing |
final_score = process_segments(segment_data, threshold)
print(f"Result: {final_score}")