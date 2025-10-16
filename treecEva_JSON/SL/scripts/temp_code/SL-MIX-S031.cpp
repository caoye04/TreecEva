#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <memory>
#include <bitset>
#include <algorithm>

int main() {
    // Simulated sensor data blocks
    std::vector<int> sensor_blocks = {0x1A3, 0x2F5, 0x3B9, 0x4C2, 0x5D7};
    
    // Shared pointer to store valid block checksums
    auto valid_checksums = std::make_shared<std::vector<int>>();
    
    // Token validation using bitwise operations
    for (const auto& block : sensor_blocks) {
        int mask = 0xFF;
        int token = block & mask;
        
        // Checksum: XOR all bytes and verify against a pattern
        std::bitset<8> byte1((token >> 4) & 0xF);
        std::bitset<8> byte2(token & 0xF);
        
        bool checksum_valid = (byte1.count() % 2 == 0) && (byte2.count() % 2 == 1);
        
        if (checksum_valid) {
            valid_checksums->push_back(token);
        }
    }
    
    // Compute environmental stability index
    int stability_index = 0;
    
    if (!valid_checksums->empty()) {
        // Logical operation to determine base stability
        bool high_stability = valid_checksums->size() > 3;
        bool moderate_stability = valid_checksums->size() >= 2 && valid_checksums->size() <= 3;
        
        // Matrix-like structure for weighted calculation
        int weights[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int weight_sum = 0;
        
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                weight_sum += weights[i][j];
            }
        }
        
        // Final index calculation
        if (high_stability) {
            stability_index = weight_sum * 3;
        } else if (moderate_stability) {
            stability_index = weight_sum * 2;
        } else {
            stability_index = weight_sum;
        }
        
        // Adjust for invalid blocks
        int invalid_count = sensor_blocks.size() - valid_checksums->size();
        stability_index -= (invalid_count * 5);
    }
    
    std::cout << "Result: " << stability_index << std::endl;
    return 0;
}