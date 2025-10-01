#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_SIZE 10

struct DataPoint {
    double x;
    double y;
    int flag;
};

typedef struct {
    struct DataPoint points[MAX_SIZE];
    int count;
} DataSet;

int calculateFlags(DataSet* dataset) {
    int total = 0;
    for(int i = 0; i < dataset->count; i++) {
        if(dataset->points[i].flag > 0) {
            total += (int)(dataset->points[i].x * dataset->points[i].y);
        }
    }
    return total;
}

double computeDistance(struct DataPoint a, struct DataPoint b) {
    double dx = a.x - b.x;
    double dy = a.y - b.y;
    return sqrt(dx*dx + dy*dy);
}

int main() {
    DataSet data = {
        .points = {
            {.x=3.0, .y=4.0, .flag=1},
            {.x=0.0, .y=0.0, .flag=-1},
            {.x=5.0, .y=12.0, .flag=2},
            {.x=-3.0, .y=4.0, .flag=1},
            {.x=7.0, .y=-24.0, .flag=0},
            {.x=8.0, .y=15.0, .flag=3},
            {.x=0.0, .y=0.0, .flag=0},
            {.x=9.0, .y=-12.0, .flag=-1},
            {.x=-5.0, .y=12.0, .flag=1},
            {.x=0.0, .y=0.0, .flag=0}
        },
        .count = MAX_SIZE
    };
    
    // Modify some data points based on conditions
    for(int i = 0; i < data.count; i++) {
        if(data.points[i].flag <= 0) {
            data.points[i].x = fabs(data.points[i].x);
            data.points[i].y = fabs(data.points[i].y);
        }
        
        if(i % 3 == 0) {
            data.points[i].flag = data.points[i].flag ^ 1;
        }
    }
    
    // Calculate distances between consecutive valid points
    double totalDistance = 0.0;
    int validCount = 0;
    
    for(int i = 0; i < data.count - 1; i++) {
        if(data.points[i].flag > 0 && data.points[i+1].flag > 0) {
            totalDistance += computeDistance(data.points[i], data.points[i+1]);
            validCount++;
        }
    }
    
    // Perform bit shifting operations on flags
    int flagProduct = 1;
    for(int i = 0; i < data.count; i++) {
        if(data.points[i].flag > 0) {
            flagProduct <<= data.points[i].flag;
        }
    }
    
    // Calculate final result using multiple operations
    int flagSum = calculateFlags(&data);
    double avgDistance = validCount > 0 ? totalDistance / validCount : 0.0;
    
    long long result = (long long)(flagSum * avgDistance) & (flagProduct | 0xF0);
    result = result ^ (long long)(totalDistance * 10);
    
    // Apply modulus to keep result in reasonable range
    result = result % 1000000;
    
    printf("Result: %lld\n", result);
    return 0;
}