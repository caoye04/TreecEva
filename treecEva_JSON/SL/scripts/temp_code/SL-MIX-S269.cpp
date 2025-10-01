#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    // Initialize variables
    int x = 12, y = 7;
    double pi = 3.141592653589793;
    vector<vector<int>> matrix = {{2, 4, 8}, {16, 32, 64}, {128, 256, 512}};
    
    // Perform complex arithmetic and bitwise operations
    int a = (x << 2) + (y >> 1);  // Left shift x by 2, right shift y by 1
    int b = pow(2, 5) - sqrt(64);
    int c = matrix[1][2] & 0x3F;  // Bitwise AND with hexadecimal mask
    
    // Nested loop to manipulate matrix values
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if ((i + j) % 2 == 0) {
                matrix[i][j] ^= (a & 0xF);  // XOR with lower 4 bits of a
            } else {
                matrix[i][j] |= (b << 1);   // OR with b shifted left by 1
            }
        }
    }
    
    // String manipulation
    string s = "HELLO";
    int char_sum = 0;
    for (char ch : s) {
        char_sum += static_cast<int>(ch);
    }
    
    // Trigonometric computation
    double angle_rad = pi / 4.0;
    double sin_val = sin(angle_rad);
    double cos_val = cos(angle_rad);
    int trig_sum = static_cast<int>((sin_val + cos_val) * 1000);
    
    // Final calculation using all derived values
    int final_result = ((matrix[2][1] >> 3) + char_sum) ^ trig_sum;
    
    cout << "Result: " << final_result << endl;
    return 0;
}