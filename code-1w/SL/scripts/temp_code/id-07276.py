def analyze_productivity(logs):
    total_chars = sum(len(entry) for entry in logs)
    uppercase_count = sum(c.isupper() for entry in logs for c in entry)
    word_count = sum(entry.count(' ') + 1 for entry in logs)
    avg_word_length = total_chars / word_count if word_count else 0
    
    # Distractor: irrelevant linguistic analysis
    vowel_ratio = sum(c.lower() in 'aeiou' for entry in logs for c in entry) / total_chars if total_chars else 0
    palindrome_count = sum(1 for entry in logs if entry.strip().lower() == entry.strip().lower()[::-1])

    return {
        'total_chars': total_chars,
        'uppercase_ratio': uppercase_count / total_chars if total_chars else 0,
        'avg_word_length': avg_word_length,
        'vowel_ratio': vowel_ratio,
        'palindrome_count': palindrome_count
    }

logs = [
    "URGENT Meeting Today", 
    "Finalize REPORT by EOD", 
    "Code REVIEW scheduled", 
    "Deploy UPDATE immediately"
]

analysis = analyze_productivity(logs)
productivity = analysis['uppercase_ratio'] * 100
errors = len([c for entry in logs for c in entry if c.isdigit()])
efficiency = analysis['avg_word_length'] ** 2

# Misleading intermediate calculations
theoretical_max = len(max(logs, key=len)) * len(logs)
decay_factor = 0.95 ** len(logs)
phantom_metric = sum(ord(entry[0]) for entry in logs if entry) % 7

# Core logic embedded among distractions
def evaluate_performance(p, e, eff):
    base = p * (1 + eff / 10)
    penalty = e * 3.5
    if p > 15:
        base += 5
        if eff > 3:
            base += 3
    return int(base - penalty)

final_score = evaluate_performance(productivity, errors, efficiency)

# Output result as required
print(f"Result: {final_score}")