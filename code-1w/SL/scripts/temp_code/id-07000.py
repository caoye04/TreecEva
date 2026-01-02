from collections import defaultdict, Counter

# Simulated sensor data aggregation for a distributed system health monitor
def collect_sensor_readings():
    readings = [
        ('node_01', 'cpu', 78), ('node_02', 'cpu', 85), ('node_03', 'cpu', 90),
        ('node_01', 'mem', 60), ('node_02', 'mem', 70), ('node_03', 'mem', 88),
        ('node_01', 'disk', 40), ('node_02', 'disk', 85), ('node_03', 'disk', 92)
    ]
    return readings

def build_health_map(readings):
    health_map = defaultdict(lambda: defaultdict(int))
    for node, resource, value in readings:
        health_map[node][resource] = value
    
    # Irrelevant transformation - distractor
    stats_summary = {node: dict(data) for node, data in health_map.items()}
    avg_cpu = sum(health_map[n]['cpu'] for n in health_map) / len(health_map)
    peak_memory = max(health_map[n]['mem'] for n in health_map)
    
    # Unused computation path - red herring
    def calculate_stress_score(node_data):
        return sum(v ** 0.5 for v in node_data.values()) * 1.5
    
    return health_map

def generate_thresholds():
    # Base thresholds
    base = {'cpu': 80, 'mem': 75, 'disk': 85}
    
    # Distractor: irrelevant derived thresholds
    secondary = {k: v + 10 for k, v in base.items()}
    fallback = {k: v - 5 for k, v in base.items()}
    
    # Actual thresholds used later
    active = {k: v + (5 if k == 'cpu' else 0) for k, v in base.items()}
    return active

def evaluate_node_status(metrics, limits):
    status_flags = []
    for resource, usage in metrics.items():
        threshold = limits[resource]
        # Complex conditional with misleading intermediate
        if usage > threshold:
            severity = 'CRITICAL' if usage > threshold + 10 else 'WARNING'
            status_flags.append((resource, severity))
        elif usage > threshold * 0.9:
            status_flags.append((resource, 'ELEVATED'))
        else:
            status_flags.append((resource, 'NORMAL'))
    
    # Redundant analysis - dead code path
    def assess_stability(flag_list):
        critical_count = len([f for f in flag_list if f[1] == 'CRITICAL'])
        return 'UNSTABLE' if critical_count > 1 else 'STABLE'
    
    return status_flags

def aggregate_diagnostics(node_statuses):
    # Count occurrences of each severity level
    severity_counter = Counter()
    resource_counter = Counter()
    
    for node, flags in node_statuses.items():
        for resource, severity in flags:
            severity_counter[severity] += 1
            resource_counter[resource] += 1
    
    # Complex derived metrics - some unused
    total_issues = sum(severity_counter.values())
    critical_weight = severity_counter['CRITICAL'] * 3
    warning_weight = severity_counter['WARNING'] * 1.5
    composite_risk = critical_weight + warning_weight
    
    # Decoy calculation - looks important but unused
    max_resource_load = max(resource_counter.values()) if resource_counter else 0
    distribution_entropy = 0.0
    if len(resource_counter) > 1:
        from math import log
        total = sum(resource_counter.values())
        distribution_entropy = -sum((count/total) * log(count/total) for count in resource_counter.values())
    
    return {
        'risk_score': composite_risk,
        'issue_count': total_issues,
        'breakdown': dict(severity_counter)
    }

def apply_calibration(diag, offset=0.75):
    # Modify risk score with calibration factor
    calibrated = diag.copy()
    raw_score = calibrated['risk_score']
    
    # Multi-step transformation
    adjusted = raw_score * 1.15 - offset * 2
    normalized = max(0, min(adjusted, 100))  # Clamp to 0-100
    
    # Distraction: alternate normalization path never taken
    def soft_normalize(value):
        return value / (1 + abs(value)) * 100
    
    calibrated['risk_score'] = round(normalized, 2)
    calibrated['calibration_applied'] = True
    return calibrated

def process_metrics(diagnostics, thresholds):
    # Final processing with conditional override logic
    score = diagnostics['risk_score']
    issues = diagnostics['issue_count']
    
    # Key decision logic with nested conditions
    if score >= 40 and issues >= 3:
        level = 3
    elif score >= 25 and issues >= 2:
        level = 2
    elif score >= 10:
        level = 1
    else:
        level = 0
    
    # Secondary adjustment based on hidden rule
    breakdown = diagnostics['breakdown']
    critical_count = breakdown.get('CRITICAL', 0)
    if critical_count >= 2 and 'disk' in [r for r, s in thresholds.items() if s < 90]:
        level = max(level, 3)  # Enforce minimum escalation
    
    # Final mapping to diagnostic code
    code_map = {0: 100, 1: 210, 2: 350, 3: 720}
    result_code = code_map.get(level, 100)
    
    # Distractor: unused alternative mapping
    legacy_codes = [(0, 99), (1, 198), (2, 301), (3, 605)]
    fallback_code = next((c for l, c in legacy_codes if l == level), 99)
    
    # Final computation
    multiplier = 1 + (critical_count * 0.1)
    final_value = int(result_code * multiplier)
    
    return final_value

# Main execution flow with decoy functions
readings = collect_sensor_readings()
health_data = build_health_map(readings)
thresholds = generate_thresholds()

def analyze_network_topology(nodes):
    # Dead function - never called, pure distraction
    topology_score = len(nodes) * 1.5
    redundancy_factor = 0.8 if len(nodes) > 2 else 0.3
    return topology_score * redundancy_factor

def forecast_failure_risk(history):
    # Another decoy - looks relevant but unused
    if not history:
        return 0.0
    trend = sum(history) / len(history)
    return round(trend * 0.25, 3)

# Build node statuses
node_statuses = {}
for node, metrics in health_data.items():
    node_statuses[node] = evaluate_node_status(metrics, thresholds)

diagnostics = aggregate_diagnostics(node_statuses)
calibrated_diagnostics = apply_calibration(diagnostics)
final_diagnostic = process_metrics(calibrated_diagnostics, thresholds)

print(f"Result: {final_diagnostic}")