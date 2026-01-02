def analyze_pattern(data, size):
    count_pairs = 0
    for i in range(len(data) - size + 1):
        segment = data[i:i+size]
        if segment[0] == segment[-1]:
            count_pairs += 1
    
    total_chars = len(data)
    avg_position = (len(data) - 1) / 2 if data else 0
    dummy_var = [x * 2 for x in range(3)]  # Irrelevant list comprehension
    unused_tuple = ("ignore", "this")
    
    result = count_pairs * 2 + total_chars // 5
    return int(result)

# Simulate DNA sequence motif analysis
sequence = "ACGTAGCTAGACGTA"
window_size = 4

# Track recurring patterns in genetic sequences
temp_value = sequence.count("A")
final_score = analyze_pattern(sequence, window_size)

print(f"Result: {final_score}")