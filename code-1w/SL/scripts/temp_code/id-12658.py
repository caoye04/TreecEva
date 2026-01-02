from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed logging framework
timestamped_logs = [
    {'time': 100, 'level': 'ERROR', 'node': 'N1'},
    {'time': 105, 'level': 'WARN', 'node': 'N2'},
    {'time': 110, 'level': 'INFO', 'node': 'N1'},
    {'time': 115, 'level': 'ERROR', 'node': 'N3'},
    {'time': 120, 'level': 'DEBUG', 'node': 'N2'},
    {'time': 125, 'level': 'WARN', 'node': 'N1'},
    {'time': 130, 'level': 'ERROR', 'node': 'N2'},
    {'time': 135, 'level': 'INFO', 'node': 'N3'}
]

# Irrelevant aggregation: count per node (distractor)
node_counts = defaultdict(int)
for log in timestamped_logs:
    node_counts[log['node']] += 1

# Misleading metric: average time between logs (not used in final logic)
all_times = [log['time'] for log in timestamped_logs]
mean_time = sum(all_times) / len(all_times)
time_variance = sum((t - mean_time) ** 2 for t in all_times) / len(all_times)

# Relevant data extraction: error counts by level (used later)
level_counter = Counter(log['level'] for log in timestamped_logs)

# Simulated performance baseline thresholds (red herring structure)
baseline_thresholds = {
    'CRITICAL': 0.1,
    'ERROR': 0.3,
    'WARN': 0.5,
    'INFO': 0.7,
    'DEBUG': 0.9
}

# Decoy function: looks important but unused
def compute_health_factor(data):
    total = 0
    for entry in data:
        if entry['level'] == 'ERROR':
            total -= 10
        elif entry['level'] == 'WARN':
            total -= 5
    return max(0, 100 + total)

# Another decoy: complex transformation with no impact
decoy_matrix = [[i * j for j in range(3)] for i in range(3)]
transposed = list(zip(*decoy_matrix))

# Real processing begins: extract only ERROR and WARN for analysis
alert_logs = [log for log in timestamped_logs if log['level'] in ['ERROR', 'WARN']]

# Count per node for alert-level logs (actual relevant data)
alert_by_node = defaultdict(int)
for log in alert_logs:
    alert_by_node[log['node']] += 1

# Baseline for comparison: expected error rate per node
baseline = {'N1': 2, 'N2': 1, 'N3': 1}

# Secondary distractor: sort nodes by name (unused)
sorted_nodes = sorted(alert_by_node.keys())

# Function to evaluate true system performance
# Contains early returns and conditional logic


def analyze_stability(node_alerts, base):
    score = 100.0
    for node, observed in node_alerts.items():
        expected = base.get(node, 1)
        if observed > expected * 2:
            score -= 15.0
        elif observed > expected:
            score -= 8.0
        else:
            score += 5.0  # Efficient nodes boost score
    
        # Introduce modular arithmetic red herring
        temp_adjust = (observed % 3) * 2
        score -= temp_adjust  # Actually harmful adjustment, but looks intentional
    
        if score < 30:
            return 30  # Floor to prevent collapse
    return round(score, 4)

# Unused recursive helper (dead code path)
def recursively_count_errors(logs, index=0):
    if index >= len(logs):
        return 0
    count = 1 if logs[index]['level'] == 'ERROR' else 0
    return count + recursively_count_errors(logs, index + 1)

# Real evaluation function
metrics = dict(alert_by_node)  # Convert to plain dict

def evaluate_performance(met, base):
    # Apply stability analysis
    raw_score = analyze_stability(met, base)
    
    # Additional logic: penalty for total high severity
    total_alerts = sum(met.values())
    if total_alerts > 4:
        raw_score *= 0.9
    elif total_alerts == 0:
        raw_score *= 1.2
    else:
        raw_score *= 1.0
    
    # Distractor: use Counter for something irrelevant
    temp_counter = Counter(met)
    entropy = sum(math.log(v) if v > 0 else 0 for v in temp_counter.values())
    
    # Final adjustment based on entropy (looks sophisticated but minor effect)
    raw_score += min(entropy * 2, 10)
    
    # Normalize to integer scale
    return int(raw_score)

# Execute main logic
final_score = evaluate_performance(metrics, baseline)

# Print result as required
print(f"Target result: {final_score}")