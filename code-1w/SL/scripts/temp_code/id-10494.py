def main():
    # Simulate a dynamic sequence influenced by modular arithmetic and conditional filtering
    raw_data = [x * x for x in range(15) if x % 3 != 0]
    offset = sum([x for x in raw_data if x > 50]) // 7 if len(raw_data) > 10 else 0

    # Apply transformation with lambda-based filter
    transform = lambda val: (val + offset) % 17
    temp_sequence = [transform(x) for x in raw_data]

    # Threshold function to detect significant fluctuations
    threshold_func = lambda x: x > 10

    # Misleading auxiliary computation (dead-end, not used in final logic)
    anomaly_count = 0
    for i in range(len(temp_sequence)):
        if i > 0 and temp_sequence[i] - temp_sequence[i-1] > 5:
            anomaly_count += 1
    derived_metric = anomaly_count * 13 % 19  # Unused red herring

    # Secondary irrelevant structure: tracking parity runs
    parity_runs = []
    current_run = 0
    for val in temp_sequence:
        if val % 2 == 0:
            current_run += 1
        else:
            if current_run > 0:
                parity_runs.append(current_run)
            current_run = 0
    if current_run > 0:
        parity_runs.append(current_run)

    average_run = sum(parity_runs) / len(parity_runs) if parity_runs else 0  # Distractor

    # Core logic: calculate equilibrium score based on threshold compliance
    def calculate_equilibrium(seq, condition):
        score = 0
        for i in range(1, len(seq)):
            if condition(seq[i]) and seq[i] != seq[i-1]:
                score += seq[i] - seq[i-1]
            elif seq[i] == seq[i-1]:
                score -= 1
        return score + len(seq)

    # Key execution point
    equilibrium_score = calculate_equilibrium(temp_sequence, threshold_func)

    # Print result as required
    print(f"Result: {equilibrium_score}")

if __name__ == "__main__":
    main()