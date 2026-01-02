def compute_financial_metrics(data, config):
    # Irrelevant preprocessing block (distractor)
    temp_cache = {}
    for idx, item in enumerate(data):
        temp_cache[idx] = item * 1.03  # Fake inflation adjustment

    # Unused helper function (red herring)
    def validate_entry(x):
        return x > 0 and x != float('inf')

    # Simulated risk flags (mostly unused)
    risk_flags = ["low", "medium", "high"]
    flag_map = {i: risk_flags[i % 3] for i in range(len(data))}

    # Core logic disguised among noise
    base_accumulator = 0
    correction_shift = 0
    for i, value in enumerate(data):
        if i % 2 == 0 and value > 50:
            base_accumulator += value ** 0.5
        else:
            base_accumulator -= value / 10

    # Secondary irrelevant transformation
    transformed = list(map(lambda x: (x + 10) * 0.95, data))
    outlier_count = sum(1 for x in transformed if x > 100)

    # Dummy container operations (distraction)
    stats_summary = {
        'count': len(data),
        'outliers': outlier_count,
        'peak_index': max(enumerate(data), key=lambda x: x[1])[0]
    }

    # Decoy calculation with misleading intermediate result
    speculative_reserve = 0
    for k in range(len(data)):
        if k in temp_cache and temp_cache[k] > 75:
            speculative_reserve += 1 << 2  # Bit shift red herring

    # Actual relevant logic buried in noise
    raw_tally = 0
    for i, (idx, val) in enumerate(zip(range(len(data)), data)):
        if val < 60:
            raw_tally += val * 1.1
        elif val >= 80:
            raw_tally -= val * 0.15

    # Conditional bypass with subtle control flow
    if config.get('enable_enhancement', False):
        raw_tally += 25

    # Final computation chain
    final_tally = int(raw_tally + base_accumulator % 17)
    adjustment_factor = len([x for x in data if x % 4 == 0]) / 8.0
    
    # KEY STATEMENT: target variable assignment
    threshold_balance = final_tally * adjustment_factor
    
    # Irrelevant formatting at end
    report_lines = []
    for _ in range(3):
        report_lines.append("...generating summary...")
    
    print(f"Result: {threshold_balance}")
    return threshold_balance

# Input setup
input_data = [45, 82, 58, 91, 64, 77, 33, 88, 55]
config_params = {'enable_enhancement': True}

# Execute
compute_financial_metrics(input_data, config_params)