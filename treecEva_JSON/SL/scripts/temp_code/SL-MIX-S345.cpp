#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

struct DNAHash {
    std::size_t operator()(const std::string& dna) const {
        std::size_t hash = 0;
        for (char c : dna) {
            hash = hash * 31 + c;
        }
        return hash;
    }
};

constexpr int classify_length(size_t len) {
    return (len < 10) ? 1 : (len < 20) ? 2 : 3;
}

int main() {
    std::string segment = "ATCGATCGATCGATCG";
    std::unordered_map<std::string, int, DNAHash> segment_map;
    
    // Transform the segment: reverse complement
    std::string transformed = segment;
    std::transform(transformed.begin(), transformed.end(), transformed.begin(), 
        [](char c) -> char {
            switch(c) {
                case 'A': return 'T';
                case 'T': return 'A';
                case 'C': return 'G';
                case 'G': return 'C';
                default: return c;
            }
        });
    std::reverse(transformed.begin(), transformed.end());
    
    // Logical operations to determine initial classification
    bool is_length_even = (segment.length() % 2 == 0);
    bool has_high_gc_content = (std::count(segment.begin(), segment.end(), 'G') + 
                               std::count(segment.begin(), segment.end(), 'C')) > (segment.length() / 2);
    
    int initial_classification = (is_length_even && has_high_gc_content) ? 10 : 
                                (is_length_even || has_high_gc_content) ? 5 : 0;
    
    // Comparison operations with hash values
    DNAHash hasher;
    size_t original_hash = hasher(segment);
    size_t transformed_hash = hasher(transformed);
    
    bool hash_comparison = (original_hash > transformed_hash);
    
    // Final classification logic
    int length_class = classify_length(segment.length());
    int final_classification = initial_classification + length_class;
    
    if (hash_comparison) {
        final_classification += 7;
    } else {
        final_classification -= 3;
    }
    
    std::cout << "Result: " << final_classification << std::endl;
    return 0;
}