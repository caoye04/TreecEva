#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

double recursive_calc(int n, double base) {
    if (n <= 1) return base;
    double val = recursive_calc(n - 1, base);
    if (n % 3 == 0) {
        return val * log(n);
    } else if (n % 3 == 1) {
        return val + sin(n);
    } else {
        return val - cos(n);
    }
}

int main() {
    int arr[5][5] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 24, 25}};
    int flat_arr[25];
    int idx = 0;
    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            flat_arr[idx++] = arr[i][j];
        }
    }
    
    double sum_log = 0;
    for(int i=0; i<25; i++){
        if((flat_arr[i] & 1) == 1){ // Check if odd
            sum_log += log(static_cast<double>(flat_arr[i]));
        }
    }
    
    int x = 12, y = 8;
    int xor_val = x ^ y;
    int shifted = xor_val << 2;
    
    char str[] = "complexity";
    int str_len = strlen(str);
    int mask = 0xFF;
    int masked_len = str_len & mask;
    
    double base_val = static_cast<double>(shifted + masked_len);
    double recursive_result = recursive_calc(6, base_val);
    
    double final_result = round(recursive_result + sum_log);
    cout << "Result: " << static_cast<long long>(final_result) << endl;
    return 0;
}