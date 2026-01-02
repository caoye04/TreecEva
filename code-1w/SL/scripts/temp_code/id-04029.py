from collections import defaultdict, Counter

def analyze_transitions(sequence):
    transitions = defaultdict(int)
    for i in range(len(sequence) - 1):
        pair = (sequence[i], sequence[i+1])
        transitions[pair] += 1
    return transitions

def calculate_entropy(counts):
    total = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        prob = count / total
        entropy -= prob * __import__('math').log2(prob)
    return entropy

def calculate_final_score(log, weight_map):
    # Irrelevant pre-processing: character frequency counting
    char_freq = Counter(''.join(log))
    total_chars = sum(char_freq.values())
    avg_length = sum(len(entry) for entry in log) / len(log)
    
    # Misleading intermediate calculation with dead-end variables
    temp_scores = []
    for entry in log:
        score = 0
        for ch in entry:
            if ch.isalpha():
                score += ord(ch.lower()) % 5
        temp_scores.append(score)
    
    # Actual relevant logic begins: transition analysis
    full_sequence = ''.join(log)
    transition_counts = analyze_transitions(full_sequence)
    transition_entropy = calculate_entropy(transition_counts)
    
    # Secondary distraction: unused nested loop over weight combinations
    dummy_result = 0
    for k in weight_map:
        for i in range(2):
            for j in range(2):
                dummy_result += (i * j) % 3
    
    # Core scoring logic using weighted components
    base_score = transition_entropy * weight_map['entropy']
    length_bonus = avg_length * weight_map['length']
    complexity_penalty = len(set(full_sequence)) * weight_map['uniqueness']
    
    # Final computation
    final_score = base_score + length_bonus - complexity_penalty
    
    # Print required output format
    print(f"Result: {final_score}")
    return final_score

# Input data
weights = {
    'entropy': 1.7,
    'length': 0.8,
    'uniqueness': 0.3
}

data_log = [
    "x9mK", "Lp3n", "qR7t", "sV2w",
    "uX5y", "zA8b", "cD1e", "fG4h"
]

# Execution point
final_score = calculate_final_score(data_log, weights)