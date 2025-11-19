from collections import defaultdict

# Initialize daily sales
bread_sales = 60
pastry_sales = 70

# Check bonus condition: both items sold more than 50 units
bonus_condition = (bread_sales > 50) and (pastry_sales > 50)

# Apply bonus if condition is true
bonus_amount = 20 if bonus_condition else 0

total_expected_sales = bread_sales + pastry_sales + 2 * bonus_amount

print(f"Result: {total_expected_sales}")