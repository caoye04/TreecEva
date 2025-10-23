#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <bitset>
#include <queue>

class DNAEncoder {
private:
    std::vector<int> encodedSequence;
    
public:
    DNAEncoder(const std::string& dna) {
        for (char c : dna) {
            switch(c) {
                case 'A': encodedSequence.push_back(0); break;
                case 'T': encodedSequence.push_back(1); break;
                case 'G': encodedSequence.push_back(2); break;
                case 'C': encodedSequence.push_back(3); break;
            }
        }
    }
    
    std::vector<int> getEncoded() const { return encodedSequence; }
    
    // Overload XOR operator for mutation simulation
    DNAEncoder operator^(const std::vector<int>& mask) const {
        DNAEncoder result("");
        for (size_t i = 0; i < encodedSequence.size(); ++i) {
            int maskedValue = encodedSequence[i] ^ mask[i % mask.size()];
            result.encodedSequence.push_back(maskedValue);
        }
        return result;
    }
    
    // Convert encoded sequence to decimal
    int toDecimal() const {
        int decimal = 0;
        for (int code : encodedSequence) {
            decimal = (decimal << 2) | code;
        }
        return decimal;
    }
};

int main() {
    // Original DNA sequence: ATGCAT
    DNAEncoder dna("ATGCAT");
    
    // Mutation mask: 101 (binary) = 5 (decimal)
    std::vector<int> mask = {1, 0, 1};
    
    // Apply mutation simulation
    DNAEncoder mutated = dna ^ mask;
    
    // Priority queue to process mutations in order
    std::priority_queue<int> mutationHeap;
    auto mutatedSequence = mutated.getEncoded();
    
    for (int code : mutatedSequence) {
        mutationHeap.push(code);
    }
    
    // Process mutations
    int finalCode = 0;
    int position = 0;
    std::vector<int> processedCodes(mutatedSequence.size());
    
    while (!mutationHeap.empty()) {
        processedCodes[position++] = mutationHeap.top();
        mutationHeap.pop();
    }
    
    // Reconstruct sequence with processed codes
    DNAEncoder finalDNA("");
    for (int code : processedCodes) {
        finalDNA = DNAEncoder("") ^ std::vector<int>(1, code);
        finalCode = (finalCode << 2) | code;
    }
    
    std::cout << "Result: " << finalCode << std::endl;
    return 0;
}