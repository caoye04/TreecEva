#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

struct Point {
    int x;
    int y;
};

struct Data {
    struct Point points[3];
    double values[2];
    char label[MAX_LEN];
};

int compute_hash(char *str) {
    int hash = 0;
    while (*str) {
        hash = (hash << 5) - hash + *str++;
        hash &= 0x7FFFFFFF; // Keep it positive
    }
    return hash;
}

double calculate_expression(double a, double b, int op) {
    switch(op) {
        case 0: return pow(a, b);
        case 1: return sqrt(fabs(a * b));
        case 2: return fmod(a, b + 1.0);
        default: return a + b;
    }
}

int main() {
    struct Data dataset;
    
    // Initialize points
    dataset.points[0].x = 5;
    dataset.points[0].y = -2;
    dataset.points[1].x = 3;
    dataset.points[1].y = 7;
    dataset.points[2].x = -4;
    dataset.points[2].y = 1;
    
    // Initialize values
    dataset.values[0] = 2.5;
    dataset.values[1] = -1.8;
    
    strcpy(dataset.label, "Test_Data_Structure");
    
    // Perform calculations
    int sum_x = 0;
    int product_y = 1;
    for(int i=0; i<3; i++) {
        sum_x += dataset.points[i].x;
        product_y *= dataset.points[i].y;
    }
    
    // Bitwise manipulation
    int mask = (sum_x & 0xF) | ((product_y >> 1) & 0xF0);
    mask ^= 0xAA;
    
    // Mathematical computation
    double expr_result = calculate_expression(dataset.values[0], dataset.values[1], mask % 3);
    
    // String processing
    int label_len = strlen(dataset.label);
    int hash_code = compute_hash(dataset.label);
    
    // Final calculation
    int intermediate = (hash_code & 0xFF) + label_len;
    double angle_rad = expr_result / 10.0;
    double sin_val = sin(angle_rad);
    
    int result = (intermediate ^ ((int)(sin_val * 1000))) & 0xFFFF;
    
    printf("Result: %d\n", result);
    return 0;
}