def compute_adaptive_threshold(n):
    # Irrelevant helper that computes Fibonacci but is never used
    def fib(x):
        a, b = 0, 1
        for _ in range(x):
            a, b = b, a + b
        return a

    # Unused sequence generator (red herring)
    unused_sequence = [i ** 2 - i for i in range(n + 5) if i % 3 != 0]

    # Core data: generate prime indicators up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]

    # Distractor: complex-looking transformation with no impact
    decoy_matrix = [[(i * j) % 7 for j in range(4)] for i in range(5)]
    checksum = sum(sum(row) for row in decoy_matrix) % 13

    # Another dead-end calculation
    temp_offset = 0
    for k in range(3):
        temp_offset += (k + 1) * fib(k)  # fib(0)=0, fib(1)=1, fib(2)=1 → offset=0+2+3=5

    # Real logic begins: weight assignment based on inverse index and primality
    weights = []
    for i in range(1, n + 1):
        if is_prime[i]:
            weights.append(1.0 / i)
        else:
            weights.append(0.5 if i % 4 == 0 else 0.1)

    # Normalize weights using L1 norm
    total_weight = sum(abs(w) for w in weights)
    normalized_weights = [w / total_weight for w in weights]

    # Apply moving average filter (length 3) with padding
    smoothed = []
    padded = [normalized_weights[0]] + normalized_weights + [normalized_weights[-1]]
    for i in range(1, len(normalized_weights) + 1):
        window_avg = (padded[i-1] + padded[i] + padded[i+1]) / 3
        smoothed.append(window_avg)

    # Secondary transformation: exponential decay on smoothed values
    decayed = [smoothed[i] * (0.9 ** i) for i in range(len(smoothed))]

    # Filter out values below median (this modifies structure)
    median_val = sorted(decayed)[len(decayed)//2]
    filtered = [v for v in decayed if v >= median_val]

    # Truncate to first 10 elements, regardless of length
    final_weights = filtered[:10]

    # Introduce irrelevant floating point adjustments
    epsilon = 1e-8
    perturbation = sum((i + epsilon) / (1 + i * epsilon) for i in range(1, 6)) * 1e-6

    # Correction factor based on unused checksum and fib side computation
    correction_factor = (checksum + temp_offset + perturbation) / 12.0

    # KEY STATEMENT: this determines the answer
    threshold_balance = final_weights[-1] * correction_factor

    # Dead code path (never reached)
    if threshold_balance < 0:
        for x in unused_sequence:
            threshold_balance -= fib(int(x) % 10)

    # Output result as required
    print(f"Result: {threshold_balance}")
    return threshold_balance

# Execute with fixed input
result = compute_adaptive_threshold(15)