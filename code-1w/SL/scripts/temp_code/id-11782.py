from collections import defaultdict
import itertools

# Simulate transaction sequences across multiple accounts
def analyze_financial_peak():
    transactions = [100, -50, 200, -180, 300, -250, 150, -120]
    account_log = defaultdict(list)
    temp_snapshot = []

    # Auxiliary tracking variables (some are distractions)
    volatility_index = 0
    total_fluctuation = 0
    debug_trace = []
    snapshot_interval = 3

    current_balance = 50
    peak_balance = current_balance
    recovery_phase = False

    for i, txn in enumerate(transactions):
        # Update balance
        current_balance += txn

        # Track peak balance
        peak_balance = current_balance if current_balance > peak_balance else peak_balance

        # Distractor logic: volatility tracking (not used in final answer)
        if i > 0:
            total_fluctuation += abs(txn)
            volatility_index = total_fluctuation / (i + 1)

        # Semi-relevant state tracking
        account_log['balance_history'].append(current_balance)
        if current_balance < 0:
            recovery_phase = True
            debug_trace.append((i, current_balance))

        # Dead code path (never executed under current data)
        if len(account_log['balance_history']) == 100:
            temp_snapshot = list(itertools.accumulate(transactions))

        # Irrelevant computation
        _ = sum(x * 0.1 for x in account_log['balance_history'] if x > 0)

        # Early break simulation (not triggered)
        if recovery_phase and current_balance > 200:
            break

    # Additional distraction: unused aggregation
    final_stats = {
        'avg': sum(account_log['balance_history']) / len(account_log['balance_history']),
        'min': min(account_log['balance_history']),
        'max': max(account_log['balance_history'])  # Redundant with peak_balance
    }

    # Print required result
    print(f"Target result: {peak_balance}")

analyze_financial_peak()