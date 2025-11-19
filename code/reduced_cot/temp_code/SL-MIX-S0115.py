import re
from collections import defaultdict
from statistics import mean, stdev
global_counter = 0
transaction_logs = [
    "TXN_001:USD:1250.75:CLEARED",
    "TXN_002:EUR:890.50:FLAGGED",
    "TXN_003:USD:3400.00:CLEARED",
    "TXN_004:GBP:150.25:CLEARED",
    "TXN_005:USD:9800.00:SUSPICIOUS",
    "TXN_006:USD:1200.30:CLEARED",
    "TXN_007:EUR:5600.80:FLAGGED",
    "TXN_008:USD:750.40:CLEARED",
    "TXN_009:USD:10250.00:SUSPICIOUS",
    "TXN_010:GBP:300.60:CLEARED"
]
amounts_by_currency = defaultdict(list)
suspicious_patterns = [r'SUSPICIOUS$', r'FLAGGED$']
for log_entry in transaction_logs:
    parts = log_entry.split(':')
    txn_id, currency, amount_str, status = parts
    amount = float(amount_str)
    amounts_by_currency[currency].append(amount)
    if any(re.search(pattern, log_entry) for pattern in suspicious_patterns):
        global_counter += 1
suspicious_score = 0
for currency, amounts in amounts_by_currency.items():
    if len(amounts) >= 2:
        avg_amount = mean(amounts)
        std_dev = stdev(amounts) if len(amounts) > 1 else 0
        max_amount = max(amounts)
        threshold = avg_amount + (std_dev * 1.5)
        if max_amount > threshold:
            suspicious_score += int(max_amount / 100)
final_adjustment = (lambda x: x * 2 if x > 5 else x + 3)(global_counter)
suspicious_score += final_adjustment
print(f"Result: {suspicious_score}")