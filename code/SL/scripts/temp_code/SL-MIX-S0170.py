data_records = {
    'A001': 45,
    'B002': 67,
    'C003': 23,
    'D004': 89,
    'E005': 12
}

primary_sum = sum([value for key, value in data_records.items() if key.startswith(('A', 'B', 'C'))])
temp_calc = primary_sum * 2  # Unused intermediate calculation
modifier = len([key for key in data_records.keys() if key.endswith('3')]) + 1
secondary_sum = sum([value for key, value in data_records.items() if value > 50])  # Unused calculation
adjustment = len(data_records) * 10
final_total = primary_sum * modifier - adjustment

print(f"Result: {final_total}")