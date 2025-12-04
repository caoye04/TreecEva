account_data = {"savings": 1000, "status": "active", "account_id": "A12345", "opened_date": "2023-01-15"}
# Process account balance with interest based on status
interest_rate = 1.05 if account_data["status"] == "active" else 0.98
final_balance = account_data["savings"] * interest_rate
print(f"Final balance: {final_balance}")