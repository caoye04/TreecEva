#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

double compute_inner_value(int x, double y) {
    return pow(x, 2) + sin(y) * cos(y);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int n = matrix.size();
    int m = matrix[0].size();
    
    double accumulator = 0.0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if((i+j)%2 == 0){
                accumulator += sqrt(matrix[i][j]);
            } else {
                accumulator -= log(matrix[i][j]+1);
            }
        }
    }
    
    string key = "COMPUTE";
    int hash_val = 0;
    for(char c : key){
        hash_val = (hash_val * 31 + c) % 100;
    }
    
    bool flag1 = (accumulator > 10);
    bool flag2 = (hash_val < 50);
    
    double final_result = 0;
    if(flag1 && flag2){
        final_result = compute_inner_value( static_cast<int>(accumulator/10), M_PI/4 );
    } else if(flag1 || flag2){
        final_result = ceil(accumulator) * floor(static_cast<double>(hash_val)/7);
    } else {
        final_result = round(accumulator + hash_val);
    }
    
    cout << "Result: " << final_result << endl;
    return 0;
}