def prime_factors_count(n):
    count = 0
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            count += 1
            n //= d
        d += 1
    if n > 1:
        count += 1
    return count

def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

network_nodes = [12, 18, 24, 30, 36]
base_weights = {node: prime_factors_count(node) for node in network_nodes}
attenuation_factors = {node: node // 2 for node in network_nodes}

with open('temp_log.txt', 'w') as log_file:
    aggregate_reliability_index = 0
    for node_id in network_nodes:
        gcd_value = compute_gcd(node_id, sum(network_nodes))
        raw_score = base_weights[node_id] * (gcd_value if gcd_value > 1 else 1)
        dampened_score = raw_score ** (1 if attenuation_factors[node_id] % 2 == 0 else 0.5)
        final_score = int(dampened_score) if dampened_score >= 1 else 1
        aggregate_reliability_index += final_score
        log_file.write(f"Node {node_id}: {final_score}\n")

signal_quality_adjustment = 1 if aggregate_reliability_index % 3 == 0 else (2 if aggregate_reliability_index % 3 == 1 else 0)
aggregate_reliability_index = aggregate_reliability_index + signal_quality_adjustment
print(f"Result: {aggregate_reliability_index}")