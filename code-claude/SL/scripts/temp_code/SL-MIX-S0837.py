# Network packet analysis simulation
# Analyzing overlapping patterns in network traffic

def generate_fibonacci(limit):
    fib = [0, 1]
    while fib[-1] + fib[-2] <= limit:
        fib.append(fib[-1] + fib[-2])
    return set(fib)

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Simulate packet sequence analysis
packet_range = range(1, 100)
packet_ids = [23, 45, 67, 89, 12, 34, 56, 78, 90]

# Identify potential malicious patterns
suspicious_pattern = set([13, 21, 34, 55, 89])
harmless_pattern = set([12, 24, 36, 48, 60, 72, 84, 96])

# Analyze network traffic statistics
total_packets = 1000
error_rate = 0.05
false_positives = int(total_packets * error_rate)

# Check for protocol violations
protocol_flags = {'SYN': 1, 'ACK': 2, 'FIN': 4, 'RST': 8, 'PSH': 16, 'URG': 32}
invalid_combinations = set([(1, 4), (8, 2), (16, 8)])

# Track packet timing anomalies
timing_thresholds = {'low': 10, 'medium': 50, 'high': 100}
anomalous_packets = 0
for packet in packet_ids:
    if packet % timing_thresholds['medium'] < timing_thresholds['low']:
        anomalous_packets += 1

# Main analysis section
range_start = 1
range_end = 50

# Generate prime numbers in the specified range
primes_in_range = set()
for i in range(range_start, range_end + 1):
    if is_prime(i):
        primes_in_range.add(i)

# Generate Fibonacci numbers up to range end
fibonacci_set = generate_fibonacci(range_end)

# Identify suspicious packets that match both prime and Fibonacci patterns
potential_threats = set()
for i in packet_ids:
    if i in primes_in_range and i in fibonacci_set:
        potential_threats.add(i)

# Calculate metrics for various packet properties
protocol_metrics = {}
for flag, value in protocol_flags.items():
    protocol_metrics[flag] = value * anomalous_packets

# Identify overlap between prime numbers and Fibonacci numbers
unique_elements = len(primes_in_range & fibonacci_set)

# Calculate threat score based on various factors
threat_score = anomalous_packets * 10
if len(potential_threats) > 0:
    threat_score += len(potential_threats) * 25

# Apply false positive correction
adjusted_score = threat_score - false_positives
if adjusted_score < 0:
    adjusted_score = 0

# Final security assessment
security_risk = 'low'
if adjusted_score > 100:
    security_risk = 'high'
elif adjusted_score > 50:
    security_risk = 'medium'

print(f"Result: {unique_elements}")