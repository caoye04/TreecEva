from collections import Counter

initial_deposits = [1500, 2200, 800, 3100, 1200, 950]
processing_fees = [25, 40, 15, 60, 20, 30]
bonus_codes = ['B50', 'B25', 'B100', 'B75', 'B50', 'B25']

bonus_map = {'B50': 50, 'B25': 25, 'B100': 100, 'B75': 75}
account_balances = []

# Calculate net amounts after fees and bonuses
for i in range(len(initial_deposits)):
    net_amount = initial_deposits[i] - processing_fees[i]
    if bonus_codes[i] in bonus_map:
        net_amount += bonus_map[bonus_codes[i]]
    account_balances.append(net_amount)

# Some intermediate calculations that don't affect final result
total_fees = sum(processing_fees)
average_bonus = sum(bonus_map.values()) / len(bonus_map)

# Sort balances and get final result
sorted_balances = sorted(account_balances)
final_balance = sorted_balances[-1]

print(f"Target result: {final_balance}")