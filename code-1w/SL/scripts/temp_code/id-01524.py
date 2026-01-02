def calculate_final_score(content, extra):
    words = content.split()
    word_count = len(words)
    char_count = sum(len(w) for w in words)
    avg_length = char_count / word_count if word_count > 0 else 0
    
    # Count how many words are capitalized
    capitalized = sum(1 for w in words if w[0].isupper())
    
    # Base score from average word length and bonus
    base_score = avg_length * 10
    adjustment = capitalized * 2
    final_score = base_score + adjustment + extra
    
    return int(final_score)

# Irrelevant variable (minimal distraction for intervention level 4)
temp_log = "Processing complete"

text = "The Quick Brown Fox Jumps Over The Lazy Dog"
bonus = 7
score = calculate_final_score(text, bonus)
print(f"Result: {score}")