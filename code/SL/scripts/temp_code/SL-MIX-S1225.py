def visit_tracker(func):
    visited_pairs = set()
    def wrapper(a, b):
        pair = tuple(sorted([a, b]))
        if pair in visited_pairs:
            return False
        visited_pairs.add(pair)
        return func(a, b)
    return wrapper

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

@visit_tracker
def are_coprime(m, n):
    return gcd(m, n) == 1

network_nodes = [12, 18, 25, 30, 35, 42, 49, 56]
coprime_counter = 0
visited_map = {}

for i in range(len(network_nodes)):
    current_node = network_nodes[i]
    visited_map[current_node] = set()
    for j in range(i+1, len(network_nodes)):
        other_node = network_nodes[j]
        if are_coprime(current_node, other_node):
            coprime_counter += 1
            visited_map[current_node].add(other_node)
        if coprime_counter > 10:
            break
    if coprime_counter > 10:
        break

print(f"Result: {coprime_counter}")