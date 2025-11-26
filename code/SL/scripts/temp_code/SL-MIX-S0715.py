def process_employee_data():
    employee_hours = [35, 42, 38, 40, 45]
    hourly_rate = 25
    
    # Calculate total hours worked
    total_hours = sum(employee_hours)
    
    # Calculate total payroll cost
    total_payroll = total_hours * hourly_rate
    
    # Apply overtime adjustment for hours over 40
    overtime_bonus = sum([(hours - 40) * 1.5 * hourly_rate for hours in employee_hours if hours > 40])
    
    # Calculate total sum including overtime
    total_sum = total_payroll + overtime_bonus
    
    # Apply company-wide adjustment factor
    adjustment_factor = 1.08
    final_total = total_sum * adjustment_factor
    
    # Debug info (distractor)
    debug_check = len(employee_hours)
    
    print(f"Result: {final_total}")

process_employee_data()