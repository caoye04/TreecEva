import itertools
import statistics

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

def tokenize_log(log_line):
    return log_line.split(',')

@timing_decorator
def process_transactions(transaction_logs):
    amounts = []
    for log in transaction_logs:
        tokens = tokenize_log(log)
        if len(tokens) >= 3 and tokens[1] == 'SUCCESS':
            amount = float(tokens[2])
            if amount > 0:
                amounts.append(amount)
    return amounts

@timing_decorator
def calculate_risk_metrics(amounts):
    if not amounts:
        return 0
    mean_amount = statistics.mean(amounts)
    variance = statistics.variance(amounts) if len(amounts) > 1 else 0
    risk_factor = 1.5 if variance > 10000 else 1.0
    score = mean_amount * risk_factor
    return score

transaction_logs = [
    "TXN001,SUCCESS,1250.75,2023-05-15",
    "TXN002,FAILED,0.00,2023-05-15",
    "TXN003,SUCCESS,890.50,2023-05-16",
    "TXN004,SUCCESS,3500.00,2023-05-16",
    "TXN005,SUCCESS,950.25,2023-05-17",
    "TXN006,SUCCESS,1200.00,2023-05-17"
]

processed_amounts = process_transactions(transaction_logs)
risk_score = calculate_risk_metrics(processed_amounts)
print(f"Result: {risk_score}")