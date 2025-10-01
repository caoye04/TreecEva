#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize data structures
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
    double intermediate = pow(sum_matrix, 0.5);
    int rounded_val = static_cast<int>(round(intermediate));
    
    // Step 3: Manipulate strings
    string concatenated = "";
    for (const string& token : tokens) {
        reverse(token.begin(), token.end());
        concatenated += token;
    }
    
    // Step 4: Bitwise operations
    int bitwise_result = (rounded_val << 2) ^ 0xF;
    
    // Step 5: Complex calculation involving previous results
    int final_result = static_cast<int>(bitwise_result * log(sum_matrix)) + concatenated.length();
    
    // Output the result
    cout << "Result: " << final_result << endl;
    
    return 0;
}