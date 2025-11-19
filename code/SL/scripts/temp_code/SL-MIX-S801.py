def call_tracker(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.call_count += 1
        return result
    wrapper.call_count = 0
    return wrapper

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

@call_tracker
def compute_coprime_pairs(network_nodes):
    coprime_count = 0
    for i in range(len(network_nodes)):
        for j in range(i + 1, len(network_nodes)):
            if gcd(network_nodes[i], network_nodes[j]) == 1:
                coprime_count += 1
    return coprime_count

@call_tracker
def calculate_lcm_chain(numbers):
    if not numbers:
        return 0
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

# Network simulation data
active_nodes = [15, 28, 33, 46, 51]
secondary_nodes = {12, 25, 35, 49}

# Primary computation
primary_coprimes = compute_coprime_pairs(active_nodes)

# Secondary computation
lcm_result = calculate_lcm_chain(list(secondary_nodes))

# Topology scoring logic
is_connected = primary_coprimes > 10
has_redundancy = lcm_result < 10000
final_topology_score = 0

if is_connected and not has_redundancy:
    final_topology_score = primary_coprimes * 3
elif is_connected or has_redundancy:
    final_topology_score = primary_coprimes + lcm_result
else:
    final_topology_score = abs(primary_coprimes - lcm_result)

print(f"Result: {final_topology_score}")