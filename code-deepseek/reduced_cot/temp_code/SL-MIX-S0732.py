processed_items = ['data_file_1.csv', 'data_file_2.txt', 'config.json', 'output.log', 'backup.dat']
valid_items = [item for item in processed_items if item.endswith(('.csv', '.json', '.dat'))]
temp_count = len(processed_items)
backup_check = len([item for item in processed_items if 'backup' in item])
final_ratio = len(valid_items) / len(processed_items) * 100
print(f"Result: {final_ratio}")