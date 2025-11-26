from collections import Counter

account_balance = 1500
recent_transactions = [25, 60, 120, 45, 90, 30]
transaction_freq = Counter(recent_transactions)
most_common_amount = transaction_freq.most_common(1)[0][0]
recurring_payments = [80, 45, 120]
total_payment = sum(recurring_payments) + most_common_amount
remaining_balance = account_balance - total_payment
print(f"Target result: {remaining_balance}")