from itertools import combinations

# Simulate a network load analysis across clustered nodes
def analyze_network_load(n):
    base_loads = [i * 2 + 1 for i in range(n)]
    temp_offsets = [(i % 4) * 0.5 for i in range(n)]
    adjusted_loads = [base + off for base, off in zip(base_loads, temp_offsets)]

    # Generate all possible communication pairings between nodes
    comm_pairs = list(combinations(adjusted_loads, 2))
    pair_products = [a * b for a, b in comm_pairs]

    # Simulate time-series windowing (irrelevant to final result)
    sliding_sums = []
    for i in range(len(pair_products) - 2):
        sliding_sums.append(sum(pair_products[i:i+3]))

    # Dummy statistical tracking
    avg_product = sum(pair_products) / len(pair_products) if pair_products else 0
    variance_proxy = sum((p - avg_product) ** 2 for p in pair_products[:10]) if len(pair_products) > 10 else 0

    # Core calculation: aggregate per-node contribution across all pairs
    node_contributions = {i: 0 for i in range(n)}
    for idx, (a, b) in enumerate(combinations(range(n), 2)):
        load_a, load_b = adjusted_loads[a], adjusted_loads[b]
        node_contributions[a] += load_a * load_b
        node_contributions[b] += load_a * load_b

    aggregate_loads = list(node_contributions.values())

    # Misleading normalization step (not used in final answer)
    normalized_loads = [x / (max(aggregate_loads) or 1) for x in aggregate_loads]

    # Critical statement
    peak_capacity = max(aggregate_loads)

    # Red herring: secondary metric based on sorted order
    sorted_contributions = sorted(aggregate_loads, reverse=True)
    secondary_metric = sum(sorted_contributions[:3]) * 0.1  # unused

    return peak_capacity

# Execute simulation for 7 network nodes
result = analyze_network_load(7)
print(f"Result: {result}")