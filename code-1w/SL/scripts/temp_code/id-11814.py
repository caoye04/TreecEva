def analyze_pattern(sequence):
    count_a = 0
    count_b = 0
    temp_sum = 0
    for i, char in enumerate(sequence):
        if i % 2 == 0 and char == 'A':
            count_a += 1
            temp_sum += i
        elif char == 'B':
            count_b += 1
    # Irrelevant transformation
    transformed = [x * 2 for x in range(len(sequence)) if x % 3 == 0]
    adjustment = sum(transformed) // max(len(transformed), 1)
    return count_a - count_b + adjustment // 10


def validate_sequence(seq_list):
    scores = []
    for seq in seq_list:
        score = 0
        if len(seq) > 5:
            score += analyze_pattern(seq)
        else:
            score += len(seq)
        scores.append(score)
    return scores

def calculate_final_score(data, thresholds):
    raw_scores = validate_sequence(data)
    weighted_total = 0.0
    weight_factor = 1.5
    threshold_hit = False
    
    for idx, (score, thresh) in enumerate(zip(raw_scores, thresholds)):
        if score >= thresh:
            weighted_total += score * weight_factor
            threshold_hit = True
        else:
            weighted_total -= 1.5
    
    # Distractor: unused computation
    reversed_data = [s[::-1] for s in data]
    palindrome_count = sum(1 for s in reversed_data if s == s[::-1])
    
    # Another distractor loop
    cumulative_shift = 0
    for i in range(3):
        cumulative_shift += i ** 2
    
    final_score = int(weighted_total + 2 * int(threshold_hit))
    return final_score

# Main execution
if __name__ == "__main__":
    data = ["ABABA", "AABBA", "AAAAA", "BABAB"]
    thresholds = [3, 2, 4, 3]
    intermediate_result = [len(s) for s in data if 'B' in s]
    padding_value = sum(intermediate_result) % 7
    
    final_score = calculate_final_score(data, thresholds)
    print(f"Target result: {final_score}")