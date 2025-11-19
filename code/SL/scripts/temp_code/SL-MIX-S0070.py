from collections import namedtuple

# Sales record for one day
Sale = namedtuple('Sale', ['customer_id', 'sourdough_sales', 'croissant_sales'])

daily_records = [
    Sale(customer_id=101, sourdough_sales=75, croissant_sales=20),
    Sale(customer_id=102, sourdough_sales=50, croissant_sales=30),
    Sale(customer_id=103, sourdough_sales=65, croissant_sales=15),
    Sale(customer_id=104, sourdough_sales=40, croissant_sales=45),
    Sale(customer_id=105, sourdough_sales=80, croissant_sales=10)
]

# Calculate loyalty points and check discount qualification
qualifying_customers = 0
for record in daily_records:
    total_spent = record.sourdough_sales + record.croissant_sales
    loyalty_points = total_spent // 5
    if loyalty_points >= 10 and record.sourdough_sales > 60:
        qualifying_customers += 1

print(f"Result: {qualifying_customers}")