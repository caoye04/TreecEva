from collections import defaultdict

def calculate_performance(accounts):
    balance_stats = defaultdict(int)
    for user, transactions in accounts.items():
        balance_stats['total_users'] += 1
        net = sum(transactions)
        if net > 0:
            balance_stats['profitable'] += 1
        balance_stats['net_sum'] += net

    accuracy = balance_stats['profitable'] / balance_stats['total_users']
    magnitude = abs(balance_stats['net_sum'])
    final_score = int(accuracy * 100) + (magnitude // 100)
    return final_score

# Simulated account data
accounts = {
    'trader_01': [200, -50, 300, -100],
    'trader_02': [-200, -100, 400, 50],
    'trader_03': [100, 100, 100],
    'trader_04': [-300, 200, -50, 400],
    'trader_05': [50, 50, -200]
}

# Auxiliary variable (minor distraction)
user_count_snapshot = len(accounts)

final_score = calculate_performance(accounts)
print(f"Result: {final_score}")