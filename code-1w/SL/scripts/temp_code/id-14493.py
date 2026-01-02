from collections import defaultdict

# Simulate benchmarking results across multiple test phases
def run_diagnostics(config, thresholds):
    diagnostics = []
    temp_log = []
    for i in range(len(config)):
        score = (config[i] * 3.7) + 2
        adjusted = score * (0.95 if i % 2 == 0 else 1.05)
        temp_log.append(adjusted)
        if adjusted > thresholds.get(i, 50):
            diagnostics.append((i, adjusted))
    return diagnostics

# Analyze phase consistency using sliding window
def analyze_consistency(logs):
    if len(logs) < 3:
        return 0
    streak = 0
    max_streak = 0
    for j in range(2, len(logs)):
        if logs[j] > logs[j-1] > logs[j-2]:
            streak += 1
        else:
            max_streak = max(max_streak, streak)
            streak = 0
    return max(max_streak, streak)

# Main performance calculator
def calculate_performance(runs):
    history = defaultdict(float)
    total_offset = 0.0
    peak_magnitude = 0
    
    for idx, run in enumerate(runs):
        # Irrelevant accumulation (distractor)
        total_offset += (idx * 0.1) % 0.5
        
        base = sum(run) / len(run)
        bonus = 0
        
        # Apply conditional bonuses based on pattern
        if len(run) > 4 and base > 15:
            bonus += 5.5
        elif base > 20:
            bonus += 3.2
            
        # Track only last two runs for history (semi-relevant)
        if idx >= len(runs) - 2:
            smoothed = (base * 0.8) + bonus
            history[f'run_{idx}'] = smoothed
    
    # Secondary computation that looks important but isn't used directly
    outlier_check = [v for v in history.values() if v > 10]
    valid_count = len(outlier_check)
    
    # Actual scoring logic
    raw_score = sum(history.values())
    adjustment_factor = 0.9 if valid_count < 2 else 1.1
    
    # Final computation
    final = int(raw_score * adjustment_factor)
    
    # Dead code path (misleading)
    if final < 0:
        final = -final * 2
        
    return final

# Configuration setup
benchmark_config = [8, 12, 10, 15, 18]
threshold_settings = {0: 40, 2: 38, 4: 50}

# Run initial diagnostics (results not fully used)
diag_results = run_diagnostics(benchmark_config, threshold_settings)

# Generate benchmark runs (core data)
benchmark_runs = [
    [10, 14, 16, 12],
    [18, 20, 22, 19, 21],
    [25, 15, 10],
    [20, 24, 23, 26, 21, 19]
]

# Consistency analysis on unrelated data (distractor)
consistency_metric = analyze_consistency([x for x in range(8)])

# Critical execution point
final_score = calculate_performance(benchmark_runs)

print(f"Result: {final_score}")