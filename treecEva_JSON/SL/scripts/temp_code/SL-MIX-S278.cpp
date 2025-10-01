#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    // Initialize variables
    int x = 15, y = 28;
    double pi = 3.141592653589793;
    vector<vector<int>> matrix = {{2, 4, 8}, {16, 32, 64}, {128, 256, 512}};
    
    // Step 1: Perform bitwise operations
    int a = x & y;
    int b = x | y;
    int c = x ^ y;
    int d = (a << 2) + (b >> 3);
    
    // Step 2: Mathematical operations
    double angle_rad = pi / 4;
    double sin_val = sin(angle_rad);
    double cos_val = cos(angle_rad);
    double tan_val = tan(angle_rad);
    
    // Step 3: Nested data access and manipulation
    int sum_elements = 0;
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = 0; j < matrix[i].size(); ++j) {
            sum_elements += matrix[i][j] * (i + 1) * (j + 1);
        }
    }
    
    // Step 4: String manipulation
    string s1 = "Hello";
    string s2 = "World";
    string combined = s1 + s2;
    int str_length = combined.length();
    
    // Step 5: Complex calculation using previous results
    double intermediate = pow(sin_val, 3) * sqrt(sum_elements) + log(static_cast<double>(str_length));
    
    // Step 6: Final computation
    int final_result = static_cast<int>(intermediate) ^ d ^ c;
    
    cout << "Result: " << final_result << endl;
    return 0;
}