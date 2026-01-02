def calculate_efficiency(log, thresh):
    if not log.strip():
        return 0
    records = log.split(',')
    valid_count = 0
    total_value = 0
    for record in records:
        record = record.strip()
        if record.isdigit() and len(record) > 0:
            num = int(record)
            if num % 2 == 1:  # only odd numbers are valid
                valid_count += 1
                total_value += num
    if valid_count == 0:
        return 0
    avg = total_value / valid_count
    mod_result = int(avg) % thresh
    return int(avg) + mod_result

# Simulated sensor log with numeric values as strings
temperature_log = "15, 22, 33, 40, 55, , 67, 72"
threshold = 7
energy_output = calculate_efficiency(temperature_log, threshold)
print(f"Target result: {energy_output}")