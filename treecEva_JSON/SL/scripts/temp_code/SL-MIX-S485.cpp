#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int accumulator = 0;
    double temp = 0.0;
    string s = "COMPUTE";
    
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            if((i+j)%2 == 0){
                accumulator += matrix[i][j];
            }
        }
    }
    
    temp = pow(accumulator, 2);
    
    int xor_result = 0;
    for(char c : s){
        xor_result ^= static_cast<int>(c);
    }
    
    int bit_shift_val = (xor_result >> 2) & 0xF;
    
    double log_val = log(temp + 1);
    
    int final_result = static_cast<int>(floor(log_val)) + bit_shift_val;
    
    cout << "Result: " << final_result << endl;
    return 0;
}