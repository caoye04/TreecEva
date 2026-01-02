from collections import defaultdict, Counter

# Simulate system diagnostics with performance metrics
def analyze_logs(log_lines):
    severity_count = defaultdict(int)
    error_categories = []
    warning_flags = set()

    temp_buffer = []
    for line in log_lines:
        words = line.split()
        if 'ERROR' in words:
            severity_count['error'] += 1
            error_type = [w for w in words if w.isalpha() and w.lower() != 'error']
            if error_type:
                error_categories.append(error_type[0].lower())
            temp_buffer.append(line)  # Unused buffer (distractor)
        elif 'WARNING' in words:
            severity_count['warning'] += 1
            code_index = [i for i, w in enumerate(words) if w.isdigit()]
            if code_index:
                warning_flags.add(int(words[code_index[0]]))
        elif 'INFO' in words:
            severity_count['info'] += 1  # Logged but not used directly

    # Irrelevant aggregation (distractor)
    redundant_analysis = {k: v * 2 for k, v in severity_count.items() if k != 'info'}
    category_freq = Counter(error_categories)

    # Key metrics extraction
    efficiency = len(log_lines) / (severity_count['error'] + severity_count['warning'] + 1)
    critical_errors = severity_count['error']
    total_warnings = len(warning_flags)

    # Misleading intermediate calculation (not used)
    hypothetical_risk = sum(w ** 0.5 for w in warning_flags) if warning_flags else 0.0

    return efficiency, critical_errors, total_warnings

# Evaluation logic
def evaluate_performance(efficiency, errors, warnings):
    base_score = 100
    penalty = 0

    if efficiency < 2.0:
        penalty += 30
    elif efficiency < 4.0:
        penalty += 15

    if errors > 5:
        penalty += 25
    elif errors > 2:
        penalty += 10

    # Logical operation chain with short-circuiting
    if warnings >= 3 and (errors == 0 or efficiency > 3.0) and not (warnings % 2 == 1 and errors > 3):
        adjustment = -5
    else:
        adjustment = -15

    # Composite score calculation
    stability_factor = (100 - penalty + adjustment)
    final_score = int(base_score * (efficiency / 5.0) + stability_factor)

    # Dead code path (distractor)
    if False:
        final_score = max(final_score, 50)  # Never executed

    return final_score

# Simulated input data
log_entries = [
    "ERROR Network timeout detected on node 5",
    "WARNING 404 threshold exceeded",
    "ERROR Memory leak suspected in module X",
    "WARNING 502 resource contention",
    "INFO System heartbeat normal",
    "ERROR Disk I/O failure",
    "WARNING 404 high frequency logging",
    "ERROR Invalid pointer access",
    "ERROR Cache miss spike",
    "WARNING 601 timeout margin exceeded"
]

# Execute analysis
efficiency_metric, error_count, warning_count = analyze_logs(log_entries)
final_score = evaluate_performance(efficiency_metric, error_count, warning_count)

Result: {final_score}