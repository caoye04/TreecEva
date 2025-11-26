def process_data_files():
    file_status = {'config.txt': 'processed', 'data.csv': 'processed', 'logs.json': 'pending', 'backup.zip': 'processed'}
    processed_status = {}
    
    for filename, status in file_status.items():
        if status == 'processed':
            processed_status[filename] = True
        else:
            processed_status[filename] = False
    
    temp_counter = len(file_status)
    processing_count = sum(processed_status.values())
    
    print(f"Target result: {processing_count}")

process_data_files()