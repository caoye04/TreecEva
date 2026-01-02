from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] + sequence[j] == 7:
                count += 1
    return count

def generate_pairs(data):
    # Irrelevant helper function - dead code path
    return list(combinations(data, 2))

def calculate_performance_rating():
    base_values = [3, 1, 4, 1, 5]
    temp_result = sum(x ** 2 for x in base_values if x % 2 == 1)
    
    # Distractor: complex-looking but unused computation
    aux_data = [x * 2 + 1 for x in base_values]
    _ = [aux_data[i] ^ aux_data[-i-1] for i in range(len(aux_data)//2)]
    
    # Real logic begins: find pairs summing to 7
    pair_count = analyze_pattern(base_values)
    
    # Apply conditional logic with lambda
    modifier = (lambda x: x * 1.5 if x > 3 else x * 0.8)(len(base_values))
    
    # Intermediate transformation
    transformed = list(map(lambda x: x // 2 + 1, base_values))
    total_shift = sum(transformed)
    
    # Another red herring: character counting in string representation
    str_rep = ''.join(map(str, base_values))
    digit_ones = str_rep.count('1')  # Slight distraction
    
    # Final accumulation
    raw_score = temp_result + pair_count * modifier
    adjustment = abs(total_shift - digit_ones * 2)
    final_score = int(raw_score - adjustment)
    
    return final_score

def main():
    # Misleading state tracking
    session_log = {'start': True, 'phase': 'analysis'}
    result = None
    
    # Key execution point
    final_score = calculate_performance_rating()
    
    # Print required output
    print(f"Target result: {final_score}")

if __name__ == "__main__":
    main()