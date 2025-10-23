from collections import defaultdict

def fibonacci_hash(n, mod=1000):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, (a + b) % mod
    return b

# Connection logs processing
successful_attempts = defaultdict(int)
failed_attempts = defaultdict(int)

logs = [
    ('192.168.1.10', True),
    ('192.168.1.15', False),
    ('192.168.1.10', True),
    ('192.168.1.20', False),
    ('192.168.1.15', True),
    ('192.168.1.10', False),
    ('192.168.1.25', True)
]

for ip, success in logs:
    if success and ip not in failed_attempts:
        successful_attempts[ip] += 1
    elif not success:
        failed_attempts[ip] += 1
        if successful_attempts[ip]:
            del successful_attempts[ip]

# Security score calculation
base_weights = {ip: fibonacci_hash(i+5) for i, ip in enumerate(successful_attempts)}
success_bonus = {ip: count * 10 for ip, count in successful_attempts.items()}
penalty_scores = {ip: fibonacci_hash(count+3) for ip, count in failed_attempts.items()}

weighted_successes = {ip: base_weights[ip] + success_bonus[ip] for ip in successful_attempts}
merged_scores = {**weighted_successes, **penalty_scores}

final_security_score = sum(merged_scores.values())

# Apply short-circuit correction factor
if len(successful_attempts) > len(failed_attempts) and any(x > 1 for x in successful_attempts.values()):
    final_security_score *= 2
elif len(failed_attempts) >= len(successful_attempts):
    final_security_score //= 2

print(f"Result: {final_security_score}")