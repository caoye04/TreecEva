def analyze_sequence(data):
    primes = []
    temp_sum = 0
    for num in data:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            temp_sum += num
    avg_prime = temp_sum / len(primes) if primes else 0
    return [x > avg_prime for x in data]

sequence = [11, 14, 17, 22, 23, 26, 29, 33]
prime_flags = analyze_sequence(sequence)

weights = [3, -1, 2, 0, 4, 1, -2, 5]

# Distractor: Irrelevant string processing
text_data = "evaluation_metrics_v2"
masked = ''.join([c if c not in 'aeiou' else '*' for c in text_data])
entropy_approx = len(masked.replace('*', '')) / len(masked)

# Distractor: Unused helper function
divisibility_check = lambda x, y: x % y == 0 and y % 2 == 1

# Semi-relevant transformation
scaled_weights = [w * 1.5 for w in weights if w != 0]

# Another distractor: dead-end set operation
unique_weights = set(weights)
duplicate_check = len(weights) != len(unique_weights)

# Core logic hidden among distractions
def calculate_total(flags, wts):
    base = 0
    bonus = 0
    for i, flag in enumerate(flags):
        if flag:
            base += wts[i]
            if i % 3 == 0:
                bonus += 2
    return base + bonus

intermediate_result = sum(scaled_weights) / len(scaled_weights)

# Key statement
final_score = calculate_total(prime_flags, weights)

# Additional red herring: tuple unpacking with unused values
stats_summary = (temp_sum, avg_prime, entropy_approx)
(*_, meta_entropy) = stats_summary

print(f"Result: {final_score}")