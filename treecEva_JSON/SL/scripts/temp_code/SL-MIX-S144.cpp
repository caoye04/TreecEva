#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <string>
#include <functional>
#include <vector>

class PacketHasher {
private:
    std::hash<std::string> hasher;
    
public:
    size_t compute_hash(const std::string& data) const {
        return hasher(data);
    }
    
    std::string transform_payload(const std::string& payload) const {
        std::string transformed;
        for (char c : payload) {
            transformed += static_cast<char>((c ^ 0x55) & 0x7F);
        }
        return transformed;
    }
};

constexpr size_t combine_hashes(size_t a, size_t b) {
    return (a << 5) ^ (a >> 27) ^ b;
}

int main() {
    PacketHasher packet_processor;
    std::priority_queue<size_t> hash_heap;
    
    std::vector<std::string> packet_payloads = {
        "ENCRYPTED_DATA_BLOCK_1",
        "SECURE_TRANSMISSION_HEADER",
        "AUTHENTICATION_SIGNATURE"
    };
    
    size_t verification_accumulator = 0x1337;
    bool integrity_check_passed = true;
    
    for (const auto& payload : packet_payloads) {
        std::string transformed = packet_processor.transform_payload(payload);
        size_t primary_hash = packet_processor.compute_hash(payload);
        size_t secondary_hash = packet_processor.compute_hash(transformed);
        
        if ((primary_hash > 0) && (secondary_hash > 0)) {
            size_t combined = combine_hashes(primary_hash, secondary_hash);
            hash_heap.push(combined);
            verification_accumulator ^= (combined & 0xFFFF);
        } else {
            integrity_check_passed = false;
        }
    }
    
    size_t heap_validation_sum = 0;
    int counter = 0;
    
    while (!hash_heap.empty() && counter < 2) {
        size_t top_hash = hash_heap.top();
        hash_heap.pop();
        
        if ((top_hash & 0xF) == 0) {
            heap_validation_sum += (top_hash >> 4);
        } else {
            heap_validation_sum += top_hash;
        }
        
        counter++;
    }
    
    size_t final_verification_code = 0;
    if (integrity_check_passed && (heap_validation_sum > 0)) {
        final_verification_code = (verification_accumulator << 8) | (heap_validation_sum & 0xFF);
    } else {
        final_verification_code = 0xDEADBEEF;
    }
    
    std::cout << "Result: " << final_verification_code << std::endl;
    return 0;
}