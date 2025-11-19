from functools import reduce
from contextlib import contextmanager

data_log = []

@contextmanager
def transaction_logger(transaction_id):
    data_log.append(f"START:{transaction_id}")
    try:
        yield
    finally:
        data_log.append(f"END:{transaction_id}")

# Product movement records
movements = {
    'PROD-Alpha': [120, -45, 30, -15],
    'PROD-Beta': [200, -75, 50, -25, 10],
    'PROD-Gamma': [150, -60, 40, -30]
}

# Process transactions with logging
with transaction_logger('TXN-001'):
    adjusted_movements = {k: list(map(lambda x: x * 2 if x > 0 else x // 3, v)) for k, v in movements.items()}

with transaction_logger('TXN-002'):
    filtered_movements = {k: list(filter(lambda x: x != 0, v)) for k, v in adjusted_movements.items()}

with transaction_logger('TXN-003'):
    net_changes = {k: reduce(lambda acc, x: acc + x, v, 0) for k, v in filtered_movements.items()}

# Efficiency calculation
base_scores = {k: len(v) for k, v in movements.items()}
combined_metrics = {**net_changes, **{f"SCORE_{k}": v for k, v in base_scores.items()}}
efficiency_map = {k: str(v)[::-1] if isinstance(v, int) and v < 0 else str(v).upper() for k, v in combined_metrics.items()}
numeric_values = [int(s) for s in efficiency_map.values() if s.lstrip('-').isdigit()]
efficiency_score = sum(numeric_values) if numeric_values else 0

print(f"Result: {efficiency_score}")