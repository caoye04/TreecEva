def main():
    raw_input = 'sensor_42_active'
    threshold = 40

    # Extract numeric ID using string methods
    sensor_id_str = raw_input.split('_')[1]
    sensor_id = int(sensor_id_str)

    # Initial activation logic
    base_activation = sensor_id * 2 + 5

    # Apply nonlinear transformation via lambda
    enhance = lambda x: x ** 1.5 if x > 30 else x
    enhanced_activation = enhance(base_activation)

    # Bitwise integrity check (simulates hardware signal validation)
    checksum = (sensor_id ^ 0x1F) & 0x0F
    is_valid = checksum == 13

    # Conditional processing path
    if is_valid:
        processed_data = enhanced_activation + 100
    else:
        processed_data = enhanced_activation - 10

    # Final filtering function
    def final_filter(val):
        return int(val // 1.7) & 0xFF  # Scale down and clamp to byte range

    activation_score = final_filter(processed_data)

    # Irrelevant distraction: logging unrelated status
    system_status = 'OK'
    debug_flag = False

    print(f'Result: {activation_score}')

if __name__ == '__main__':
    main()