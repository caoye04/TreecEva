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
    char buffer[MAX_LEN];
};

int calculate_checksum(struct Data* d) {
    int checksum = 0;
    for (int i = 0; i < 3; i++) {
        checksum ^= (d->points[i].x & 0xFF) ^ (d->points[i].y & 0xFF);
    }
    for (int i = 0; i < 2; i++) {
        checksum ^= ((int)(d->values[i] * 100)) & 0xFF;
    }
    for (int i = 0; i < strlen(d->buffer); i++) {
        checksum ^= d->buffer[i] & 0xFF;
    }
    return checksum;
}

int main() {
    struct Data data;
    
    // Initialize points
    data.points[0].x = 15;
    data.points[0].y = 25;
    data.points[1].x = 35;
    data.points[1].y = 45;
    data.points[2].x = 55;
    data.points[2].y = 65;
    
    // Initialize values
    data.values[0] = sqrt(144.0) + pow(2.0, 3.0);
    data.values[1] = log(2.718281828) * 100.0;
    
    // Initialize buffer
    strcpy(data.buffer, "ComplexDataStructure");
    
    // Perform transformations
    for (int i = 0; i < 3; i++) {
        data.points[i].x <<= 1;  // Left shift by 1
        data.points[i].y >>= 1;  // Right shift by 1
    }
    
    for (int i = 0; i < 2; i++) {
        data.values[i] = floor(data.values[i] * 10.0) / 10.0;
    }
    
    // Concatenate length to buffer
    char temp[20];
    int len = strlen(data.buffer);
    sprintf(temp, "%d", len);
    strcat(data.buffer, temp);
    
    // Calculate final result
    int checksum = calculate_checksum(&data);
    int result = (checksum & 0xF0) >> 4;  // Extract upper nibble
    result *= (int)data.values[0];
    result += strlen(data.buffer);
    result ^= data.points[1].x;
    
    printf("Result: %d\n", result);
    return 0;
}