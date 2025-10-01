#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int base_value = 0;
    
    // Step 1: Compute sum of diagonal elements
    for (int i = 0; i < 3; ++i) {
        base_value += matrix[i][i];
    }
    
    // Step 2: Bitwise transformation
    int shifted = (base_value << 2) ^ 0xF;
    
    // Step 3: Mathematical computation
    double temp = pow(shifted, 1.5);
    int modulated = static_cast<int>(floor(temp)) % 100;
    
    // Step 4: String encoding simulation
    string key = "COMPUTE";
    int hash = 0;
    for (char c : key) {
        hash = (hash * 31 + c) & 0xFF;
    }
    
    // Step 5: Final aggregation
    int final_result = (modulated + hash) ^ 0xAA;
    
    cout << "Result: " << final_result << endl;
    return 0;
}