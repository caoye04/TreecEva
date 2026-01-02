from collections import defaultdict

# Simulate network node transmission rates over time
def collect_transmission_data():
    data = [
        ('router_A', 4.2), ('switch_B', 2.1), ('router_A', 3.8),
        ('firewall_C', 1.5), ('switch_B', 2.9), ('router_A', 5.1)
    ]
    grouped = defaultdict(list)
    for node, rate in data:
        grouped[node].append(rate)
    return grouped

# Calculate average transmission rate per node
def compute_avg_rates(node_data):
    averages = {}
    for node, rates in node_data.items():
        averages[node] = round(sum(rates) / len(rates), 2)
    return averages

# Determine total effective load based on weighted contribution
def calculate_network_load(rate_dict):
    weights = {'router': 1.5, 'switch': 1.2, 'firewall': 1.0}
    total = 0.0
    for node, avg_rate in rate_dict.items():
        node_type = node.split('_')[0]
        weight = weights.get(node_type, 1.0)
        total += avg_rate * weight
    return round(total, 2)

# Execution flow
data_log = collect_transmission_data()
avg_transmission = compute_avg_rates(data_log)
total_load = calculate_network_load(avg_transmission)
print(f"Result: {total_load}")