def process_transaction(initial_amount, processing_fee, reward_bonus):
    primary_account = initial_amount * 2
    secondary_account = primary_account // 3
    temp_fee = processing_fee + 5
    bonus = reward_bonus - 2
    # Distractor operations that don't affect final result
    unused_calc = secondary_account * temp_fee
    intermediate = bonus + 10
    final_balance = primary_account - temp_fee + bonus
    print(f"Result: {final_balance}")

initial_deposit = 150
service_charge = 8
loyalty_points = 25
process_transaction(initial_deposit, service_charge, loyalty_points)