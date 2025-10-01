#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    // Initialize a 2D vector with specific values
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    
    // Initialize variables
    int sum = 0;
    double product = 1.0;
    string text = "HELLO";
    
    // Nested loop to calculate sum and product
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            sum += matrix[i][j];
            product *= matrix[i][j];
        }
    }
    
    // Calculate the square root of the product and round it
    int rounded_sqrt = (int)round(sqrt(product));
    
    // String manipulation: convert each character to its ASCII value and sum them
    int ascii_sum = 0;
    for (char c : text) {
        ascii_sum += (int)c;
    }
    
    // Perform a bitwise operation: XOR the sum and ascii_sum
    int xor_result = sum ^ ascii_sum;
    
    // Calculate final result using a combination of all previous results
    int final_result = (rounded_sqrt + xor_result) % 1000;
    
    // Print the final result
    cout << "Result: " << final_result << endl;
    
    return 0;
}