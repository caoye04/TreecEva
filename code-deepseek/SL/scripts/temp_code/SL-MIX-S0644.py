current_balance = 1250
transaction_amount = 300
transaction_type = "deposit"
account_status = "active"
user_id = 78945
net_balance = current_balance + transaction_amount if transaction_type == "deposit" else current_balance - transaction_amount
print(f"Result: {net_balance}")