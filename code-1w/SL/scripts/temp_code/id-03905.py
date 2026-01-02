def calculate_final_score(data):
    normalized = data.strip().lower()
    words = normalized.split()
    word_lengths = [len(word) for word in words]
    sorted_lengths = sorted(word_lengths)
    median_length = sorted_lengths[len(sorted_lengths) // 2]
    total_chars = sum(word_lengths)
    score = total_chars * median_length
    adjustment = 1 if 'bonus' in words else 0
    final_score = score + adjustment
    return final_score

raw_input = "Strategic Planning Session bonus feature launch"
final_score = calculate_final_score(raw_input)
print(f"Result: {final_score}")