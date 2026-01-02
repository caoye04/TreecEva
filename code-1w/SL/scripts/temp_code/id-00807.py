def calculate_final_score(data):
    words = data.split()
    word_lengths = [len(word.strip('.,!?"')) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths)
    palindrome_count = 0
    for word in words:
        cleaned = word.lower().strip('.,!?"')
        if cleaned == cleaned[::-1] and len(cleaned) > 1:
            palindrome_count += 1
    complexity_bonus = 5 if palindrome_count >= 2 else 0
    score = int(avg_length * 10) + complexity_bonus
    return score

text_data = "A man a plan a canal Panama echoing wow radar"
dummy_variable_ignore = 999
score = calculate_final_score(text_data)
print(f"Result: {score}")