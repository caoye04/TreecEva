def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return {i for i, is_prime in enumerate(sieve) if is_prime}

# Generate cubic numbers up to 1000
cubic_numbers = {x**3 for x in range(1, 11)}

# Identify prime numbers up to 1000
primes_up_to_1000 = generate_primes(1000)

# Find numbers that are both prime and cubic
prime_cubics = primes_up_to_1000 & cubic_numbers

# Generate even numbers with mirrored digits (e.g., 22, 44, 66) up to 1000
mirrored_evens = {x for x in range(10, 1000) if x % 11 == 0 and x % 2 == 0 and len(str(x)) == 2}

# Add irrelevant distraction variable
buffer_size = 256
packet_loss_rate = 0.015

# Core computation: count overlap between prime cubics and mirrored evens
final_overlap_count = len(prime_cubics & mirrored_evens)

print(f"Result: {final_overlap_count}")