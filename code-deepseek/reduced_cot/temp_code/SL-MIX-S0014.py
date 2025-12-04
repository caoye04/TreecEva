def process_text_segments(text_data):
    # Helper function to process text segments
    segment_lengths = list(map(len, text_data.split()))
    char_counts = [sum(1 for c in seg if c.isalpha()) for seg in text_data.split()]
    bitwise_ops = [len(seg) & 0b111 for seg in text_data.split()]
    
    # Distractor calculations (unused in final result)
    vowel_counts = [sum(1 for c in seg.lower() if c in 'aeiou') for seg in text_data.split()]
    case_shifts = [seg.swapcase() for seg in text_data.split()]
    
    processed = []
    for i, seg in enumerate(text_data.split()):
        if len(seg) > 3:
            base_val = char_counts[i] * 2
            adjusted = base_val - (segment_lengths[i] % 4)
            processed.append(adjusted ^ bitwise_ops[i])
        else:
            # Dead code path - never executed with current input
            processed.append(vowel_counts[i] + 10)
    
    return processed

def analyze_data_patterns(processed_data):
    # Another helper with distractor operations
    data_sum = sum(processed_data)
    xor_result = 0
    for val in processed_data:
        xor_result ^= val
    
    # Misleading intermediate calculations
    avg_vowels = sum(val % 5 for val in processed_data)  # Unused
    pattern_shift = [val << 1 for val in processed_data]  # Unused
    
    return data_sum, xor_result

# Main execution
input_text = "Python Code Evaluation Benchmark Analysis"
data_chunks = process_text_segments(input_text)

# Irrelevant processing that doesn't affect final result
noise_data = [ord(c) for c in input_text[:5]]
noise_sum = sum(noise_data) | 0xFF  # Unused operation

processed_counts, pattern_key = analyze_data_patterns(data_chunks)

# Final computation with lambda and slicing
final_computation = lambda chunks, counts: (sum(chunks[-3:]) * 2) - (counts & 0b1111)
target_value = final_computation(data_chunks, processed_counts)

# Print result
print(f"Target result: {target_value}")