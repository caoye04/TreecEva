import itertools

# Simulated system diagnostics from a distributed computing environment
def collect_metrics():
    nodes = [f'node_{i}' for i in range(1, 11)]
    base_loads = [78, 85, 90, 67, 88, 91, 76, 83, 79, 87]
    errors = [3, 1, 0, 5, 2, 0, 4, 1, 2, 0]
    uptime_hours = [987, 1002, 1010, 950, 998, 1012, 970, 990, 985, 1005]
    
    # Irrelevant aggregation - red herring
    avg_load = sum(base_loads) / len(base_loads)
    total_errors = sum(errors)
    total_uptime = sum(uptime_hours)
    efficiency_ratio = total_uptime / (total_errors + 1) if total_errors > 0 else 0

    # Distractor: complex but unused data structure
    historical_trends = {node: [] for node in nodes}
    for i in range(len(nodes)):
        trend = [base_loads[i] + j * (-1) ** j for j in range(5)]
        historical_trends[nodes[i]] = trend

    # Real data used later
    return list(zip(nodes, base_loads, errors, uptime_hours))


def filter_critical_nodes(metrics):
    # Filter out nodes with zero errors - misleading because not actually used in final logic
    critical = [m for m in metrics if m[2] > 0]
    return critical


def compute_health_factor(load, error_count, uptime):
    # Health decreases with load and errors, increases slightly with uptime
    base = 100 - load
    penalty = error_count * 8
    bonus = min(uptime // 100, 5)
    return max(base - penalty + bonus, 0)


def generate_combinations(data):
    # Use of itertools - relevant but partially distracting
    loads = [item[1] for item in data]
    combs = list(itertools.combinations(loads[:5], 2))  # Only first 5 for some reason
    
    # Compute pair scores - looks important but unused
    pair_scores = []
    for a, b in combs:
        diff = abs(a - b)
        score = 100 - diff
        pair_scores.append(score)
    
    # Another distractor: median of pair scores not used
    sorted_scores = sorted(pair_scores)
    mid = len(sorted_scores) // 2
    median_pair_score = (sorted_scores[mid] + sorted_scores[~mid]) / 2
    
    return median_pair_score  # Never actually used


def extract_stable_nodes(metrics):
    # Nodes with low error rate and high uptime
    stable = []
    for node, load, err, up in metrics:
        if err <= 1 and up > 980:
            stability_index = (100 - load) + (up // 100) - (err * 10)
            stable.append((node, stability_index))
    
    # Sort by index descending
    stable.sort(key=lambda x: x[1], reverse=True)
    return stable


def calculate_system_entropy(metrics):
    # Fake complexity: computes entropy-like value based on load distribution
    loads = [m[1] for m in metrics]
    mean_load = sum(loads) / len(loads)
    variance = sum((x - mean_load) ** 2 for x in loads) / len(loads)
    entropy = (variance ** 0.5) * 0.5
    return round(entropy, 3)


def evaluate_performance(diag_data):
    # Core logic hidden among distractions
    total_health = 0
    valid_nodes = 0
    
    # Key processing loop
    for entry in diag_data:
        _, load, errors, uptime = entry
        
        # This condition is actually never true due to data, but looks important
        if load > 95 and errors == 0:
            contribution = 15
        elif errors >= 3:
            contribution = 5
        else:
            # Real calculation path
            health = compute_health_factor(load, errors, uptime)
            normalized = health * 0.7  # Weighted contribution
            contribution = int(round(normalized))
        
        # Only nodes with uptime > 975 are counted - crucial but subtle
        if uptime > 975:
            total_health += contribution
            valid_nodes += 1
    
    # Final score computation - this is where answer comes from
    raw_score = total_health * valid_nodes if valid_nodes > 0 else 0
    
    # Distractor: alternative formula not used
    alt_score = total_health + (valid_nodes * 10)
    
    # Actual final transformation
    adjustment = len([d for d in diag_data if d[1] < 80])  # count of low-load nodes
    final_score = raw_score - adjustment * 2
    
    return final_score

# --- Execution Flow ---
data = collect_metrics()

# Irrelevant transformations
_ = filter_critical_nodes(data)
dummy_entropy = calculate_system_entropy(data)
_ = generate_combinations(data)
stable_list = extract_stable_nodes(data)

# Key statement
final_score = evaluate_performance(data)
print(f"Result: {final_score}")