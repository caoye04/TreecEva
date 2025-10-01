#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    // Initialize complex nested data structure
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    
    int accumulator = 0;
    
    // Traverse matrix and perform operations
    for(size_t i=0; i<matrix.size(); ++i) {
        for(size_t j=0; j<matrix[i].size(); ++j) {
            int val = matrix[i][j];
            if(val % 2 == 0) {
                accumulator += val << 2;  // Left shift by 2 (equivalent to multiply by 4)
            } else {
                accumulator += static_cast<int>(pow(val, 2));
            }
        }
    }
    
    // Perform bit manipulations
    int shifted_val = accumulator >> 3;  // Right shift by 3 (equivalent to divide by 8)
    int masked_val = shifted_val & 0xFF; // Mask with 0xFF to keep lower 8 bits
    
    // String manipulation section
    string encoded = "HELLO";
    int char_sum = 0;
    for(char c : encoded) {
        char_sum += static_cast<int>(c);
    }
    
    // Final computation combining all previous results
    double sqrt_accum = sqrt(static_cast<double>(masked_val));
    int final_result = static_cast<int>(sqrt_accum) ^ (char_sum % 100);
    
    cout << "Result: " << final_result << endl;
    return 0;
}