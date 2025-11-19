book_prices = {'fiction': 15, 'science': 25, 'history': 20}
selected_categories = ['fiction', 'history']
discount_threshold = 30
discount_rate = 0.1

# Calculate total bill using dictionary comprehension
total_bill = sum({cat: book_prices[cat] for cat in selected_categories}.values())

# Apply discount using short-circuit evaluation
final_bill = total_bill * (1 - discount_rate) if total_bill >= discount_threshold else total_bill

print(f'Result: {final_bill}')