#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    Point points[3];
    int count;
} Polygon;

int main() {
    Polygon poly;
    poly.count = 3;
    
    // Initialize points
    poly.points[0].x = 4;
    poly.points[0].y = 5;
    poly.points[1].x = 7;
    poly.points[1].y = 9;
    poly.points[2].x = 2;
    poly.points[2].y = 3;
    
    // Perform calculations
    int sum_x = 0;
    int sum_y = 0;
    for (int i = 0; i < poly.count; i++) {
        sum_x += poly.points[i].x;
        sum_y += poly.points[i].y;
    }
    
    // Bitwise operations
    int bitwise_result = (sum_x << 2) ^ (sum_y >> 1);
    
    // Mathematical operations
    double sqrt_val = sqrt((double)(bitwise_result));
    int rounded_sqrt = (int)round(sqrt_val);
    
    // String manipulation
    char buffer[MAX_LEN];
    snprintf(buffer, MAX_LEN, "%d", rounded_sqrt);
    int str_len = strlen(buffer);
    
    // Final calculation
    int final_result = (rounded_sqrt * str_len) + ((bitwise_result & 0xF) | 0x10);
    
    printf("Result: %d\n", final_result);
    return 0;
}