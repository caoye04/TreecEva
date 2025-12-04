# Customer loyalty program analysis

def calculate_bonus(purchase_amount):
    # Calculate bonus points based on purchase amount
    if purchase_amount < 50:
        return purchase_amount * 0.5
    elif purchase_amount < 100:
        return purchase_amount * 0.75
    else:
        return purchase_amount * 1.0

# Customer data: (name, total purchases)
customers = [
    ("Alex", 120),
    ("Bella", 85),
    ("Carlos", 210),
    ("Dana", 45)
]

# Track special promotion eligibility
promotion_threshold = 150
eligible_for_promotion = []
for customer in customers:
    name, amount = customer
    if amount >= promotion_threshold:
        eligible_for_promotion.append(name)

# Calculate loyalty points for each customer
loyalty_points = {}
for customer in customers:
    name, amount = customer
    base_points = int(amount)
    bonus = calculate_bonus(amount)
    # Special character count bonus (marketing gimmick)
    char_bonus = sum(1 for c in name if c.lower() in 'aeiou') * 5
    loyalty_points[name] = base_points + int(bonus) + char_bonus

# Some analytics that don't affect the result
total_purchases = sum(amount for _, amount in customers)
average_purchase = total_purchases / len(customers) if customers else 0
purchase_range = max(amount for _, amount in customers) - min(amount for _, amount in customers)

# Sort customers by their loyalty points
sorted_customers = sorted(loyalty_points.items(), key=lambda x: x[1], reverse=True)

# Get the top customer's points
top_customer_points = sorted_customers[0][1] if len(sorted_customers) > 0 else 0

# Display result
print(f"Result: {top_customer_points}")