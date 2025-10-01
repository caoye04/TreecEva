#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // Initialize variables
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int accumulator = 0;
    double temp_val = 0.0;
    string encoded = "HELLO";
    int bitmask = 0xF0;
    int shift_val = 2;
    int xor_key = 0x5A;
    
    // Step 1: Process matrix diagonals
    for(int i=0; i<3; i++) {
        accumulator += matrix[i][i];
    }
    
    // Step 2: Apply mathematical transformation
    temp_val = pow(accumulator, 1.5);
    
    // Step 3: Bitwise operations
    int masked = ((int)temp_val) & bitmask;
    int shifted = masked >> shift_val;
    int xored = shifted ^ xor_key;
    
    // Step 4: String processing
    reverse(encoded.begin(), encoded.end());
    int str_sum = 0;
    for(char c : encoded) {
        str_sum += (int)c;
    }
    
    // Step 5: Final computation combining all values
    int final_result = (xored * 3) + (str_sum % 7) - (int)(sin(3.14159/2) * 100);
    
    cout << "Result: " << final_result << endl;
    return 0;
}