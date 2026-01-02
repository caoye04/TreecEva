from itertools import combinations

# Simulate employee task efficiency and error profiles
def calculate_efficiency(tasks_completed, hours):
    if hours == 0:
        return 0
    base_efficiency = tasks_completed / hours
    penalty = 0.1 * max(0, tasks_completed - 10)  # Diminishing returns
    return base_efficiency - penalty

def detect_anomaly(scores):
    mean = sum(scores) / len(scores)
    variance = sum((x - mean) ** 2 for x in scores) / len(scores)
    return variance > 25

def evaluate_risk(exposure_levels):
    risk_index = 0
    for level in exposure_levels:
        if level > 7:
            risk_index += 1.5
        elif level > 4:
            risk_index += 0.5
    return risk_index

def generate_pairs(elements):
    # Irrelevant helper: generates pairs but not used in final logic
    return list(combinations(elements, 2))

def main():
    # Core data
    tasks = [8, 12, 5, 15, 9]
    work_hours = [6, 8, 4, 10, 7]
    exposure = [3, 8, 6, 9, 5]

    # Step 1: Compute individual efficiencies
    efficiencies = []
    for i in range(len(tasks)):
        efficiency = calculate_efficiency(tasks[i], work_hours[i])
        efficiencies.append(round(efficiency, 2))
    
    # Step 2: Identify high-performing individuals (efficiency > 1.0)
    high_perf_count = 0
    for e in efficiencies:
        if e > 1.0:
            high_perf_count += 1

    # Step 3: Detect anomalous performance distribution
    anomaly_detected = detect_anomaly([tasks[i] for i in range(len(tasks)) if efficiencies[i] > 0.8])

    # Step 4: Evaluate overall risk from exposure
    risk_factor = evaluate_risk(exposure)

    # Distractor: unused combinatorial analysis
    names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    role_pairs = generate_pairs(names)  # Computed but never used
    pair_count = len(role_pairs)  # Dead variable

    # Step 5: Aggregate productivity (only those with balanced load)
    productivity = 0
    for i in range(len(tasks)):
        load_ratio = tasks[i] / max(work_hours[i], 1)
        if 0.8 <= load_ratio <= 1.5:
            productivity += tasks[i]

    # Step 6: Final evaluation using relevant factors only
    if anomaly_detected:
        productivity *= 0.9

    # Step 7: Key statement
    final_score = evaluate_performance(productivity, risk_factor)

    # Print result for extraction
    print(f"Result: {final_score}")

# Critical function - must be defined before use
def evaluate_performance(prod, risk):
    base = max(prod - risk * 2, 5)  # Minimum threshold
    bonus = 10 if prod > 30 else 0
    return base + bonus

# Execute
main()