from collections import deque
import itertools

def encode_nucleotide(nucleotide):
    encoding_map = {'A': 0b00, 'T': 0b01, 'G': 0b10, 'C': 0b11}
    return encoding_map[nucleotide]

def decode_nucleotide(value):
    decoding_map = {0b00: 'A', 0b01: 'T', 0b10: 'G', 0b11: 'C'}
    return decoding_map[value]

class DNAMutationProcessor:
    def __init__(self, initial_strand):
        self.nucleotide_sequence = deque([encode_nucleotide(n) for n in initial_strand])
        self.mutation_stack = []
        self.checksum = 0
    
    def add_mutation_protocol(self, protocol_func):
        self.mutation_stack.append(protocol_func)
    
    def process_mutations(self):
        while self.mutation_stack:
            protocol = self.mutation_stack.pop()
            self.nucleotide_sequence = deque(protocol(list(self.nucleotide_sequence)))
        
    def calculate_checksum(self):
        self.checksum = 0
        for nucleotide_code in self.nucleotide_sequence:
            self.checksum ^= nucleotide_code
        return self.checksum

# Initialize processor with DNA strand
genome_processor = DNAMutationProcessor("ATGCATGC")

# Define mutation protocols
protocol_1 = lambda seq: [((x << 1) & 0b11) for x in seq]  # Bit shift left
protocol_2 = lambda seq: [x ^ 0b10 for x in seq]           # XOR with 10
protocol_3 = lambda seq: list(itertools.chain.from_iterable([[x, x] for x in seq]))  # Duplicate each

# Apply protocols in reverse order of definition (stack behavior)
genome_processor.add_mutation_protocol(protocol_3)
genome_processor.add_mutation_protocol(protocol_2)
genome_processor.add_mutation_protocol(protocol_1)

genome_processor.process_mutations()
strand_checksum = genome_processor.calculate_checksum()
print(f"Result: {strand_checksum}")