def calculate_service_charges(amounts, fee_rate):
    irrelevant_data = [x * 2 for x in amounts if x > 50]
    misleading_total = sum(irrelevant_data) * 0.15
    charges = [amt * fee_rate for amt in amounts]
    return sum(charges)

def filter_active_accounts(users, funds):
    dummy_set = set(range(1, 20))
    temp_result = len(dummy_set.intersection(set(users)))
    active_accounts = [funds[i] for i in users if i < len(funds)]
    dead_code_check = sum(funds) * 0.33
    return active_accounts

def process_accounts(user_indices, account_funds, service_fee):
    base_calculation = sum(account_funds) // len(account_funds)
    active_funds = filter_active_accounts(user_indices, account_funds)
    total_service_fee = calculate_service_charges(active_funds, service_fee)
    
    misleading_intermediate = base_calculation * 1.25
    irrelevant_operation = (misleading_intermediate + total_service_fee) * 0.8
    
    total_active_funds = sum(active_funds)
    final_amount = total_active_funds - total_service_fee
    
    return final_amount

initial_funds = [1000, 2500, 1800, 3200, 950, 2100, 2750]
active_users = [0, 2, 3, 5]
service_fee = 0.02

unused_variable = [x * 3 for x in initial_funds if x < 2000]
distraction_calc = sum(unused_variable) * 0.07

final_balance = process_accounts(active_users, initial_funds, service_fee)
print(f"Target result: {final_balance}")