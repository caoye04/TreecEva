def analyze_financial_flow(transactions, overheads):
    cumulative_gain = 0
    running_total = 0
    adjustment_sum = 0
    temp_buffer = []
    flagged_indices = []

    for idx, (amount, code) in enumerate(zip(transactions, overheads)):
        if amount > 0:
            cumulative_gain += amount * 0.95  # Apply fee

        if code % 3 == 0 and idx % 2 == 1:
            adjustment_sum += code // 4
            temp_buffer.append(code)

        running_total += amount

        # Irrelevant tracking
        if amount < 0 and code > 50:
            flagged_indices.append(idx)

    # Secondary loop with partial overlap
    outlier_count = 0
    for val in temp_buffer:
        if val > 20:
            outlier_count += 1

    # Dummy statistical check
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    variance_proxy = sum((x - avg_temp) ** 2 for x in temp_buffer) / len(temp_buffer) if temp_buffer else 0

    # Core computation embedded in noise
    threshold_balance = running_total - adjustment_sum

    # Unused derived metrics
    normalized_balance = threshold_balance / (outlier_count + 1)
    weighted_score = cumulative_gain * 0.8 + threshold_balance * 0.2

    # Final output
    print(f"Result: {threshold_balance}")

# Inputs
transaction_list = [120, -30, 200, -50, 180]
overhead_codes = [12, 55, 24, 63, 36]

analyze_financial_flow(transaction_list, overhead_codes)