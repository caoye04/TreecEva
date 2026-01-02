from collections import Counter

def analyze_transitions(sequence):
    transitions = []
    counts = Counter(sequence)
    total = len(sequence)
    mid_point = total // 2
    
    # Irrelevant transformation (distractor)
    shifted = [chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in sequence[:mid_point]]
    shifted_str = ''.join(shifted)
    
    # Relevant logic: count adjacent letter transitions
    for i in range(len(sequence) - 1):
        if sequence[i] != sequence[i+1]:
            transitions.append((sequence[i], sequence[i+1]))
    
    return transitions, counts, shifted_str

def filter_symmetric(pairs):
    symmetric = []
    for a, b in pairs:
        if ord(a) + ord(b) == 219:  # 'a' + 'z' = 219, 'b' + 'y' = 219, etc.
            symmetric.append((a, b))
    return symmetric

def compute_ranking(pairs):
    rank = 0
    for a, b in pairs:
        rank += (ord(b) - ord(a)) * 2
    return max(rank, 10)

def main():
    input_data = "abccbaabcddcbaa"
    
    # Step 1: Analyze character transitions
    trans_pairs, freqs, dummy_str = analyze_transitions(input_data)
    
    # Step 2: Extract only symmetric transition pairs (e.g., a-z, b-y)
    balanced_pairs = filter_symmetric(trans_pairs)
    
    # Step 3: Compute final score based on ranking function
    temp_value = sum(freqs.values()) % 50  # Distractor computation
    extra_calc = len(dummy_str) * 2  # Unused variable
    final_score = compute_ranking(balanced_pairs)
    
    # Print result for evaluation
    print(f"Result: {final_score}")
    
    return final_score

if __name__ == "__main__":
    main()