def adjust_capacity(base, factor, status):
    temp = base * factor
    if status.strip().lower() == 'active':
        temp += 150
    elif status.strip().lower() == 'maintenance':
        temp -= 50
    return temp

base = 800
factor = 1.1
temporary_buffer = 37  # irrelevant variable (minimal distraction)
status = ' Active '\n
final_capacity = adjust_capacity(base, factor, status)
print(f"Result: {final_capacity}")