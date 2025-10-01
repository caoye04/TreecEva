#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_ITER 5

struct Point {
    double x;
    double y;
};

struct CalculationData {
    struct Point points[3];
    int flags[3];
    double values[3][3];
};

double computeDistance(struct Point p1, struct Point p2) {
    return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
}

int main() {
    struct CalculationData data;
    
    // Initialize points
    data.points[0] = (struct Point){3.0, 4.0};
    data.points[1] = (struct Point){0.0, 0.0};
    data.points[2] = (struct Point){5.0, 12.0};
    
    // Initialize flags
    data.flags[0] = 1;
    data.flags[1] = 0;
    data.flags[2] = 1;
    
    // Initialize values matrix
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            data.values[i][j] = (i+1)*(j+1);
        }
    }
    
    double accumulator = 0.0;
    int counter = 0;
    
    // First processing loop
    for(int i=0; i<3; i++) {
        if(data.flags[i]) {
            accumulator += computeDistance(data.points[0], data.points[i]);
            counter++;
        }
    }
    
    // Modify values based on accumulator
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            if(i == j) {
                data.values[i][j] = accumulator * data.values[i][j];
            } else {
                data.values[i][j] = data.values[i][j] / 2.0;
            }
        }
    }
    
    // Second processing with nested loops
    double tempSum = 0.0;
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            tempSum += data.values[i][j];
        }
    }
    
    // Apply mathematical transformations
    double transformed = pow(tempSum, 1.0/3.0); // Cube root
    
    // Final computation sequence
    int iterations = 0;
    double result = transformed;
    
    while(iterations < MAX_ITER) {
        if(iterations % 2 == 0) {
            result = result * 1.5 + sin(result);
        } else {
            result = result / 2.0 + cos(result);
        }
        iterations++;
    }
    
    // Bitwise adjustment
    int intPart = (int)result;
    intPart = intPart ^ (intPart >> 1); // XOR with right shift
    result = (double)intPart + (result - (int)result);
    
    printf("Result: %.6f\n", result);
    return 0;
}