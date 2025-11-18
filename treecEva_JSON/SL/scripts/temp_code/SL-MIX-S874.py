from functools import reduce

class AudioProcessor:
    def __init__(self, modulus):
        self.modulus = modulus
        self.checksum = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def process_frame(self, frame_data):
        # Calculate frame checksum using modular arithmetic
        frame_checksum = sum(frame_data) % self.modulus
        
        # Apply logical operations to determine if frame is valid
        is_valid = (frame_checksum > 0) and (frame_checksum < self.modulus//2)
        
        # Update overall checksum only for valid frames
        if is_valid:
            self.checksum = (self.checksum + frame_checksum) % self.modulus
        else:
            self.checksum = (self.checksum ^ frame_checksum) % self.modulus
        
        return is_valid

def calculate_frame_metrics(frames):
    with AudioProcessor(modulus=256) as processor:
        # Use functional programming to process frames
        validity_flags = list(map(processor.process_frame, frames))
        
        # Count valid frames using filter
        valid_count = len(list(filter(lambda x: x, validity_flags)))
        
        # Apply additional transformation using reduce
        transformed_checksum = reduce(lambda acc, frame: (acc + sum(frame)) % 256, frames, 0)
        
        # Combine metrics with logical operations
        if valid_count > len(frames)//2 and transformed_checksum != 0:
            final_checksum = (processor.checksum & transformed_checksum) | valid_count
        else:
            final_checksum = (processor.checksum | transformed_checksum) ^ valid_count
            
    return final_checksum

# Test data representing audio frames
audio_frames = [
    [15, 22, 33, 47],      # Frame 1
    [8, 16, 32, 64],       # Frame 2
    [5, 10, 15, 20],       # Frame 3
    [100, 120, 140],       # Frame 4
    [7, 14, 21, 28]        # Frame 5
]

final_checksum = calculate_frame_metrics(audio_frames)
print(f"Result: {final_checksum}")