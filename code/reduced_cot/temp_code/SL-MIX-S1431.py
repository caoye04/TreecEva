from collections import defaultdict

def log_transaction(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_transaction
def process_day(assets, day_transactions):
    for asset, change in day_transactions:
        assets[asset] += change
    return assets

portfolio_assets = defaultdict(int)
daily_operations = [
    [('AAPL', 10), ('GOOGL', 5)],
    [('AAPL', -3), ('MSFT', 7)],
    [('GOOGL', 2), ('TSLA', 4)],
    [('MSFT', -1), ('AAPL', 6)],
    [('TSLA', -2), ('GOOGL', 3)],
    [('AAPL', 2), ('MSFT', 5)],
    [('TSLA', 1), ('GOOGL', -4)]
]

for i, transactions in enumerate(daily_operations):
    portfolio_assets = process_day(portfolio_assets, transactions)
    if sum(portfolio_assets.values()) > 30:
        break

final_asset_count = sum(portfolio_assets.values())
print(f'Result: {final_asset_count}')