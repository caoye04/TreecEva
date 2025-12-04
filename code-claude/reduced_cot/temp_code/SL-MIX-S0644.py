import itertools
import math

def analyze_text_security(message):
    # Calculate character frequency for encryption analysis
    char_freq = {}
    for char in message:
        if char.isalpha():
            char_freq[char.lower()] = char_freq.get(char.lower(), 0) + 1
    
    # Misleading security metrics
    entropy_score = sum(freq * math.log2(freq) for freq in char_freq.values() if freq > 0)
    vulnerability_index = len(message) / len(char_freq) if char_freq else 0
    
    # Extract numerical values from the message (distractor)
    numerical_values = [ord(c) - 96 for c in message.lower() if c.isalpha()]
    
    return sum(numerical_values) if numerical_values else 0

# Simulated network packet data (distractor)
packet_headers = [
    (192, 168, 1, 1),
    (10, 0, 0, 1),
    (172, 16, 0, 1)
]

# Calculating network metrics (distractor)
network_complexity = sum(sum(header) for header in packet_headers) // 3
redundancy_factor = len(packet_headers) * 2

# Main security analysis
message = "cybersecurity"
security_score = analyze_text_security(message)

# Finding prime factors of a number (relevant to the final answer)
def find_prime_factors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        
        # Early exit for efficiency (distractor)
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break
            
    return factors

# Packet transmission simulation (distractor)
transmission_status = [True, False, True, True, False]
packet_loss = transmission_status.count(False) / len(transmission_status)

# Security strength calculation
target_number = 210  # 2*3*5*7
prime_factors = find_prime_factors(target_number)

# Misleading calculations
alternative_strength = security_score * packet_loss
false_metric = sum(prime_factors) * network_complexity % 100

# Conditional calculation with prime factors
encryption_strength = sum(prime_factors) // 2 if sum(prime_factors) > 100 else sum(prime_factors)

# More misleading operations with itertools
combinations = list(itertools.combinations(prime_factors, 2))
permutations = list(itertools.permutations([1, 2, 3], 2))

# Distractor calculation that seems important
final_security_metric = network_complexity + len(combinations) - len(permutations) + encryption_strength

# Misleading print that looks like the answer
print(f"Network security index: {final_security_metric}")

# The actual target result
print(f"Result: {encryption_strength}")