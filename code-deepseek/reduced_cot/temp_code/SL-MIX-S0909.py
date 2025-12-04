data_records = {'active': 25, 'pending': 12, 'completed': 38, 'cancelled': 7}
status_key = 'completed'
adjustment_factor = 2
processed_data = {k.upper(): v for k, v in data_records.items()}
status_key = status_key.upper()
final_count = processed_data.get(status_key, 0) * adjustment_factor
print(f"Result: {final_count}")