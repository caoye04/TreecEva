#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct Point {
    int x;
    int y;
};

struct Rectangle {
    struct Point topLeft;
    struct Point bottomRight;
};

int calculateArea(struct Rectangle r) {
    int width = abs(r.bottomRight.x - r.topLeft.x);
    int height = abs(r.bottomRight.y - r.topLeft.y);
    return width * height;
}

int bitwiseTransform(int a, int b) {
    return (a << 2) ^ (b >> 1) & 0xFF;
}

int main() {
    // Initialize data structures
    struct Rectangle rects[3];
    
    rects[0].topLeft.x = 2;
    rects[0].topLeft.y = 10;
    rects[0].bottomRight.x = 8;
    rects[0].bottomRight.y = 4;
    
    rects[1].topLeft.x = -3;
    rects[1].topLeft.y = 7;
    rects[1].bottomRight.x = 5;
    rects[1].bottomRight.y = -1;
    
    rects[2].topLeft.x = 0;
    rects[2].topLeft.y = 0;
    rects[2].bottomRight.x = 10;
    rects[2].bottomRight.y = 10;
    
    // Perform calculations
    int areas[3];
    for(int i = 0; i < 3; i++) {
        areas[i] = calculateArea(rects[i]);
    }
    
    // Complex mathematical operations
    double trigResult = sin(M_PI/6) * cos(M_PI/3);
    int trigInt = (int)(trigResult * 1000); // Approximately 433
    
    // Bitwise operations
    int bitwise1 = bitwiseTransform(areas[0], areas[1]);
    int bitwise2 = bitwiseTransform(areas[1], areas[2]);
    
    // Conditional logic with multiple branches
    int conditionValue;
    if((areas[0] > areas[1]) && (areas[0] > areas[2])) {
        conditionValue = areas[0] * 2;
    } else if((areas[1] > areas[0]) && (areas[1] > areas[2])) {
        conditionValue = areas[1] * 3;
    } else {
        conditionValue = areas[2] * 4;
    }
    
    // String manipulation simulation using character arrays
    char buffer[50] = "RESULT";
    int bufferSum = 0;
    for(int i = 0; buffer[i] != '\0'; i++) {
        bufferSum += buffer[i];
    }
    
    // Nested calculations
    int intermediate1 = (bitwise1 ^ bitwise2) + trigInt;
    int intermediate2 = conditionValue - bufferSum;
    
    // FINAL COMPUTATION
    int result = (intermediate1 * intermediate2) % (areas[0] + areas[1] + areas[2]);
    
    printf("Result: %d\n", result);
    return 0;
}