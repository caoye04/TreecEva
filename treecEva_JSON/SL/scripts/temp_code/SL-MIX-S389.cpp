#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

double complex_calc(double x, int y) {
    double result = 0.0;
    for (int i = 1; i <= y; ++i) {
        result += pow(x, 1.0 / i);
    }
    return result;
}

int bitwise_transform(int a, int b) {
    return (a << 2) ^ (b >> 1) & 0xFF;
}

string process_string(const string& s) {
    string result = s;
    reverse(result.begin(), result.end());
    for (char& c : result) {
        if (islower(c)) c = toupper(c);
        else if (isupper(c)) c = tolower(c);
    }
    return result;
}

int main() {
    // Initial data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<double> values = {1.5, 2.7, 3.9, 4.1};
    
    // Step 1: Perform mathematical operations
    double sum = 0;
    for (double val : values) {
        sum += sin(val) * cos(val);
    }
    
    // Step 2: Manipulate matrix data
    int product = 1;
    for (auto& row : matrix) {
        for (int& elem : row) {
            elem = elem * 2 - 1;
            product *= elem;
        }
    }
    
    // Step 3: Complex calculation
    double calc_result = complex_calc(2.5, 4);
    
    // Step 4: Bitwise transformation
    int bit_result = bitwise_transform(15, 200);
    
    // Step 5: String processing
    string original = "ComplexEvaluation";
    string processed = process_string(original);
    
    // Step 6: Combine all results
    double intermediate = (sum * product) / calc_result;
    int final_result = static_cast<int>(intermediate) ^ bit_result;
    
    // Execution Point Y
    final_result += processed.length();
    
    cout << "Result: " << final_result << endl;
    return 0;
}