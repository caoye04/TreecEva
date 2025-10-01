#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int base = 4;
    int exponent = 3;
    double power_result = pow(base, exponent);
    
    int xor_sum = 0;
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            xor_sum ^= matrix[i][j];
        }
    }
    
    string s = "compute";
    int ascii_sum = 0;
    for(char c : s){
        ascii_sum += static_cast<int>(c);
    }
    
    int combined = static_cast<int>(power_result) + xor_sum + ascii_sum;
    
    int bit_shifted = (combined << 2) | (combined >> 3);
    
    int prime_check = 29;
    bool is_prime = true;
    for(int i=2; i<=sqrt(prime_check); i++){
        if(prime_check % i == 0){
            is_prime = false;
            break;
        }
    }
    
    int result = bit_shifted;
    if(is_prime){
        result += prime_check * 2;
    } else {
        result -= prime_check;
    }
    
    cout << "Result: " << result << endl;
    return 0;
}