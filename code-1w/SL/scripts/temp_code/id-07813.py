def main():
    # Domain: Scoring system for prime-sensitive data with noise filtering
    data_stream = [12, 15, 17, 19, 21, 23, 25, 29, 31]
    filter_threshold = 18
    adjustment_factor = 3.5
    noise_floor = 0.1
    scaling_constant = 2.7

    # Irrelevant signal processing (distractor)
    normalized = list(map(lambda x: (x - min(data_stream)) / (max(data_stream) - min(data_stream)), data_stream))
    weighted_sum = sum([x * scaling_constant for x in normalized])

    # Core logic: extract primes above threshold
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    candidates = set()
    for val in data_stream:
        if val > filter_threshold:
            candidates.add(val)

    # Apply prime filtering
    prime_set = set(filter(is_prime, candidates))

    # Secondary distractor: frequency analysis of digits (unused)
    digit_freq = {}
    for num in data_stream:
        for digit in str(num):
            digit_freq[int(digit)] = digit_freq.get(int(digit), 0) + 1

    # Red herring: simulate unused correction matrix
    correction_matrix = [[i ^ j for j in range(3)] for i in range(3)]
    checksum = sum(sum(row) for row in correction_matrix) % 100

    # Key state tracking with distraction
    temp_results = []
    for p in prime_set:
        temp_results.append(p * adjustment_factor if p % 4 == 3 else p)

    # Unused backup calculation
    fallback_score = len(data_stream) * len(prime_set)

    # Critical function call
    def calculate_total(primes, factor):
        base = sum(primes)
        bonus = len(primes) * 10
        penalty = 0
        for p in primes:
            if p % 5 == 0:
                penalty += 5
        return int(base * factor) + bonus - penalty

    final_score = calculate_total(prime_set, adjustment_factor)

    # Output requirement
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()