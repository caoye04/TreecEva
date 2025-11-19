class SignalSimulator:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass

mask_pattern = 0b11001010
input_signal = 0b10110110
control_flag = True
error_condition = False

with SignalSimulator() as sim:
    if control_flag and not error_condition:
        intermediate_result = input_signal ^ mask_pattern
    else:
        intermediate_result = 0
    
    if intermediate_result or error_condition:
        validated_signal = intermediate_result & mask_pattern
    else:
        validated_signal = 0

print(f"Result: {validated_signal}")