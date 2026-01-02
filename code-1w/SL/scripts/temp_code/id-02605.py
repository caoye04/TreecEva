from collections import defaultdict

def count_vowel_frequency(s):
    freq = defaultdict(int)
    for char in s:
        if char in 'aeiou':
            freq[char] += 1
    return freq

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def calculate_harmonic_sum(n):
    total = 0.0
    for i in range(1, n + 1):
        total += 1 / factorial(i)
    return total

# Irrelevant string for mild distraction (minimal interference)
text_sample = "machine learning models often use attention mechanisms"

# Key computation
result = calculate_harmonic_sum(5)

print(f"Result: {result}")