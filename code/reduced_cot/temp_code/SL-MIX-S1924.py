import re
from collections import defaultdict

def apply_rules(sentence, rules):
    words = sentence.split()
    transformed = []
    for word in words:
        modified = False
        for pattern, replacement in rules.items():
            if re.search(pattern, word):
                new_word = re.sub(pattern, replacement, word)
                transformed.append(new_word)
                modified = True
                break
        if not modified:
            transformed.append(word)
    return transformed

def calculate_complexity(words):
    n = len(words)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[1] = len(words[0])
    for i in range(2, n + 1):
        dp[i] = max(dp[i-1], dp[i-2] + len(words[i-1]))
    return dp[n]

# Rule definitions using regex patterns
transformation_rules = {
    r'ing$': 'ed',
    r'^un(.*)': r'in\1',
    r'(.)\1{2,}': r'\1\1'
}

input_text = "running unimportant bookkeeper unnecessary"
transformed_words = apply_rules(input_text, transformation_rules)
final_score = calculate_complexity(transformed_words)
print(f"Result: {final_score}")