def process_sensor_data():
    # Encoded sensor readings
    hex_readings = ['0x1A3', '0xFF', '0x2B4', '0x1C8']
    
    # Conversion map from hex to adjusted depth values
    conversion_map = {
        0x1A3: lambda x: (x >> 2) + 10,
        0xFF: lambda x: (x << 1) - 5,
        0x2B4: lambda x: x ^ 0xAA,
        0x1C8: lambda x: x | 0xF0
    }
    
    # Process readings using the conversion map
    processed_values = []
    for hex_val in hex_readings:
        dec_val = int(hex_val, 16)
        if dec_val in conversion_map:
            transformed = conversion_map[dec_val](dec_val)
            processed_values.append(transformed)
    
    # Aggregate function using closure
    def aggregate(offset):
        def inner(values):
            total = sum(values)
            return total + offset
        return inner
    
    # Apply aggregation with a context manager for logging
    class LogContext:
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_value, traceback):
            pass
        def log_and_adjust(self, val):
            adjustment_map = {0: 7, 1: -3, 2: 5, 3: -2}
            idx = len(processed_values) % 4
            return val + adjustment_map.get(idx, 0)
    
    with LogContext() as logger:
        agg_func = aggregate(100)
        aggregated_sum = agg_func(processed_values)
        final_depth = logger.log_and_adjust(aggregated_sum)
    
    print(f"Result: {final_depth}")

process_sensor_data()