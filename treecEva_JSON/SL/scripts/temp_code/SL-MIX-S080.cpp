#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize nested data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<string> tokens = {"abc", "def", "ghi"};
    
    // Step 1: Compute the sum of all elements in the matrix
    int sum_matrix = 0;
    for (const auto& row : matrix) {
        for (int val : row) {
            sum_matrix += val;
        }
    }
    
    // Step 2: Perform mathematical operations
    double intermediate = pow(sum_matrix, 2) + sqrt(144) - log(2.71828);
    
    // Step 3: Manipulate strings
    string concatenated = "";
    for (const string& token : tokens) {
        reverse(token.begin(), token.end());
        concatenated += token;
    }
    
    // Step 4: Compute hash-like value from string
    int string_hash = 0;
    for (char c : concatenated) {
        string_hash += static_cast<int>(c);
    }
    
    // Step 5: Bitwise operations
    int bitwise_result = (sum_matrix & string_hash) | (static_cast<int>(intermediate) ^ 0xFF);
    
    // Step 6: Final complex calculation
    int final_result = (bitwise_result * 3) % 1000 + static_cast<int>(sin(1.5708) * 1000);
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}