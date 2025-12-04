def process_payments(payments, discount_function):
    subtotal = sum(payments.values())
    discount = discount_function(subtotal)
    return subtotal - discount

payment_data = {'customer_A': 150, 'customer_B': 275, 'customer_C': 180}
discount_func = lambda total: total * 0.1 if total > 500 else 0

final_total = process_payments(payment_data, discount_func)
print(f"Final total: {final_total}")