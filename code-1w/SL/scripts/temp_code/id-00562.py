def process_transaction(fees, data):
    base_amount = float(data['amount'])
    currency = data['currency']
    premium_user = data['premium']

    # Apply fee based on currency and user type
    fee_rate = fees[currency]
    if premium_user:
        fee_rate *= 0.5  # Premium users get 50% off fees

    transaction_fee = base_amount * fee_rate

    # Adjust for small transaction bonus (under 100)
    if base_amount < 100:
        bonus_credit = 5.0
    else:
        bonus_credit = 0.0

    # Final adjustment: fee deducted, bonus applied
    net_change = base_amount - transaction_fee + bonus_credit
    balance_adjustment = round(net_change, 2)

    # Irrelevant string operation (minimal interference)
    status_msg = f"Processed {currency.upper()} transaction.".replace('PROCESSED', 'DONE')
    
    return balance_adjustment

# Fee configuration per currency
tiered_fees = {'USD': 0.02, 'EUR': 0.025, 'GBP': 0.03}

# Transaction input
tx_data = {
    'amount': '85.0',
    'currency': 'EUR',
    'premium': True
}

# Execute computation
balance_adjustment = process_transaction(tiered_fees, tx_data)
print(f"Result: {balance_adjustment}")