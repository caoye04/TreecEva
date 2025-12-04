base_salary = 75000
annual_bonus = 15000
tax_rate = 0.22
tax_deduction = base_salary * tax_rate
work_hours = 40
hourly_rate = base_salary / (52 * work_hours)
final_salary = base_salary + annual_bonus - tax_deduction
print(f"Result: {final_salary}")