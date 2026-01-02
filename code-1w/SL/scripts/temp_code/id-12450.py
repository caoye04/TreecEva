def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for efficiency analysis."""
    if not data:
        return 0
    avg = sum(data) / len(data)
    return sum(1 for x in data if x > avg * threshold)

# Irrelevant data structures
task_weights = {'init': 0.1, 'process': 0.35, 'finalize': 0.15, 'cleanup': 0.05}
execution_log = ['start', 'init_done', 'processing', 'chunk_1', 'chunk_2', 'complete']

# Distractor variables
decoy_result = sum([i**2 for i in range(10)]) // 3
temp_cache = {i: pow(i, 3) for i in range(1, 8)}
metadata_flags = [True, False, True, True]

# Real computation begins here
baseline = [0.6, 0.8, 0.9, 0.7, 0.85]

metrics = [
    0.72,  # Slight underperformance
    0.81,  # Above average
    0.93,  # Strong
    0.68,  # Marginal
    0.87   # Above
]

# Unused recursive red herring
def binary_entropy(n, acc=0.0):
    if n <= 0:
        return acc
    return binary_entropy(n - 1, acc + (1 / (2 ** n)))

entropy_value = binary_entropy(5)  # Computed but unused

# Misleading transformation chain
trend_analysis = list(map(lambda x: round(x * 1.05, 2), metrics))
trend_analysis = [x for x in trend_analysis if x > 0.75]  # Filtered but unused later

# Core logic buried in distractions
def adjust_for_bias(val, factor=0.98):
    return val * factor if val > 0.8 else val * 1.02

adjusted_metrics = [adjust_for_bias(m) for m in metrics]

# Another decoy function with string methods — looks important
status_map = {}
for log_entry in execution_log:
    status_map[log_entry] = log_entry.upper().replace('_', '-')

# String-based distractor
system_status = ''.join([s[0] for s in execution_log]).lower()
system_status = system_status.replace('s', 'x')  # No impact

# Key conditional expression with early return red herring
def validate_integrity(checksum):
    if checksum < 0.5:
        return False
    elif checksum > 0.95:
        return False  # Unexpected but unreachable in this case
    return True

# Dead code path
if __debug__:
    debug_snapshot = {"metrics": metrics.copy(), "timestamp": 123456789}

# Relevant nested logic with min/max/average
bias_adjusted_avg = sum(adjusted_metrics) / len(adjusted_metrics)
peak_performance = max(adjusted_metrics)
consistency_floor = min(baseline) * 0.9

# Conditional override that doesn't trigger
if peak_performance > 0.95 and len(metrics) > 10:
    bias_adjusted_avg = 0.75

# Final evaluation logic — depends on adjusted average and baseline proximity
penalty = 0
for am in adjusted_metrics:
    if am < consistency_floor:
        penalty += 1

# The real answer derivation
base_score = bias_adjusted_avg * 100
penalty_deduction = penalty * 2.5

# This function call is critical
def evaluate_performance(am_list, base_ref):
    raw = sum(am_list) / len(am_list)
    ref_center = sum(base_ref) / len(base_ref)
    drift = abs(raw - ref_center)
    score = 90 - (drift * 100)
    if penalty > 0:
        score -= penalty_deduction
    if raw >= ref_center:
        bonus = 5 * (1 - drift)  # Small bonus if above baseline
        score += bonus
    return round(score, 4)

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Print required at end
print(f"Result: {final_score}")