from functools import reduce

class DnaProcessor:
    def __init__(self):
        self.ops_map = {
            'REV': lambda x: x[::-1],
            'CMP': lambda x: ''.join({'A':'T','T':'A','C':'G','G':'C'}[b] for b in x),
            'SHF': lambda x: x[1:] + x[0]
        }
        self.weights = [3**i for i in range(10)]
    
    def process(self, sequence, tags):
        current = sequence
        for tag in tags:
            if tag == 'BRK':
                break
            op = self.ops_map.get(tag)
            if op:
                current = op(current)
            elif tag.startswith('REP'):
                n = int(tag[3:])
                current = current * n
        return current
    
    def compute_checksum(self, seq):
        MOD = 1000000007
        return reduce(lambda acc, pair: (acc + pair[1] * self.weights[pair[0]]) % MOD, enumerate(map(ord, seq)), 0)

def main():
    processor = DnaProcessor()
    dna_seq = "ATCG"
    meta_tags = ['REV', 'CMP', 'SHF', 'REP2', 'BRK', 'CMP']
    transformed = processor.process(dna_seq, meta_tags)
    checksum = processor.compute_checksum(transformed)
    print(f"Result: {checksum}")

if __name__ == '__main__':
    main()