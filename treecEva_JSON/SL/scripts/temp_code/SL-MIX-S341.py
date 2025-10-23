from collections import deque

class PacketProcessor:
    def __init__(self):
        self.packet_stack = []
        self.key_queue = deque([0x1F, 0x2A, 0x3B, 0x4C])
        self.encryption_key = 0xAA
    
    def process_packets(self, packet_ids):
        for pid in packet_ids:
            # Push packet to stack
            self.packet_stack.append(pid)
            
            # Update encryption key using XOR with packet id and queue front
            if self.key_queue:
                modifier = self.key_queue.popleft()
                self.encryption_key ^= (pid & 0xFF) ^ modifier
                
                # Rotate queue element to end with bit shift
                shifted_modifier = ((modifier >> 1) | (modifier << 7)) & 0xFF
                self.key_queue.append(shifted_modifier)
        
        # Final key derivation uses stack popping and bitwise operations
        while self.packet_stack:
            popped_packet = self.packet_stack.pop()
            top_queue = self.key_queue.pop() if self.key_queue else 0
            self.encryption_key = (self.encryption_key ^ popped_packet ^ top_queue) & 0xFF
        
        return self.encryption_key

def main():
    processor = PacketProcessor()
    packet_sequence = [0xC5, 0x9A, 0xF2, 0x7D]
    final_decryption_key = processor.process_packets(packet_sequence)
    print(f"Result: {final_decryption_key}")

if __name__ == "__main__":
    main()