def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_squares_of_digits(n):
    return sum(int(digit)**2 for digit in str(n))

candidate_frequencies = [i for i in range(10, 100)]
resonant_frequencies = []

for freq in candidate_frequencies:
    if is_prime(freq):
        digit_square_sum = sum_of_squares_of_digits(freq)
        if is_prime(digit_square_sum):
            resonant_frequencies.append(freq)
            if len(resonant_frequencies) == 3:
                break

third_resonant = resonant_frequencies[2] if len(resonant_frequencies) >= 3 else None
print(f"Result: {third_resonant}")