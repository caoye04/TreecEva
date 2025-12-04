def calculate_crypto_metrics(assets, transaction_log):
    # Distractor function - irrelevant to final calculation
    total_volume = sum(transaction_log.values()) * 0.85
    avg_trade = total_volume / len(transaction_log) if transaction_log else 0
    market_cap = assets.get('bitcoin', 0) * 45000 + assets.get('ethereum', 0) * 3000
    return market_cap + total_volume

def apply_crypto_operations(principal, operations, conditions):
    # Main calculation logic
    volatility_multiplier = conditions.get('volatility_index', 1.0)
    leverage_factor = conditions.get('leverage', 1)
    
    # Distractor variables and operations
    temp_balance = principal * 2.5  # Misleading intermediate
    pending_transactions = operations.get('pending', [])
    completed_trades = operations.get('completed', {})
    
    # Actual calculation path
    base_return = principal
    for trade_type, amount in completed_trades.items():
        if trade_type == 'long':
            base_return += amount * 0.15 * leverage_factor
        elif trade_type == 'short':
            base_return -= amount * 0.12 * volatility_multiplier
    
    # More distractions
    unrealized_gains = len(pending_transactions) * principal * 0.03
    portfolio_diversity = len(set(operations.keys())) / 4
    
    # Final balance calculation
    final_amount = base_return * volatility_multiplier
    
    # Dead code path - never executed
    if len(pending_transactions) > 10:
        final_amount *= 1.1
    
    return int(final_amount)

# Initial setup
principal = 10000
operations_data = {
    'completed': {'long': 5000, 'short': 3000},
    'pending': ['trade_A', 'trade_B']
}
market_conditions = {'volatility_index': 1.2, 'leverage': 2}

# Distractor calculations
portfolio_metrics = calculate_crypto_metrics({'bitcoin': 2, 'ethereum': 5}, {'BTC': 10000, 'ETH': 8000})
market_analysis = portfolio_metrics * 0.75  # Never used

# Key execution
final_balance = apply_crypto_operations(principal, operations_data, market_conditions)

# Additional irrelevant operations
projected_growth = final_balance * 1.25
risk_score = len(operations_data['pending']) * 15

print(f"Target result: {final_balance}")