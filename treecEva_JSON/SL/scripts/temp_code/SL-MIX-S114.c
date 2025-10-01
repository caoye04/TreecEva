#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

struct DataPoint {
    double x;
    double y;
    int flags;
};

struct DataSet {
    struct DataPoint points[5];
    int count;
    char label[MAX_LEN];
};

double compute_weighted_sum(struct DataSet* dataset) {
    double sum = 0.0;
    for(int i = 0; i < dataset->count; i++) {
        double weight = (dataset->points[i].flags & 0x01) ? 2.0 : 0.5;
        sum += sqrt(pow(dataset->points[i].x, 2) + pow(dataset->points[i].y, 2)) * weight;
    }
    return sum;
}

void transform_points(struct DataSet* dataset) {
    for(int i = 0; i < dataset->count; i++) {
        if(dataset->points[i].x > 0 && dataset->points[i].y > 0) {
            dataset->points[i].x = log(dataset->points[i].x);
            dataset->points[i].y = log(dataset->points[i].y);
        } else {
            dataset->points[i].flags |= 0x02;
        }
    }
}

int main() {
    struct DataSet data = {
        .points = {
            {3.0, 4.0, 0},
            {-1.0, 2.0, 1},
            {5.0, 12.0, 0},
            {0.0, -3.0, 1},
            {8.0, 15.0, 0}
        },
        .count = 5,
        .label = "Test Dataset"
    };
    
    // Perform transformations on data points
    transform_points(&data);
    
    // Compute initial weighted sum
    double intermediate_result = compute_weighted_sum(&data);
    
    // Apply additional mathematical transformations
    int bit_operation = ((data.points[1].flags << 2) & 0x0F) ^ 0x0A;
    
    // Combine results with bit operations and mathematical functions
    double trig_component = sin(intermediate_result) * cos(bit_operation);
    
    // Final calculation incorporating string length as a factor
    int label_length = strlen(data.label);
    double result = ceil(intermediate_result) + floor(trig_component * 100) + (label_length << 2) + (bit_operation & 0x07);
    
    printf("Result: %.0f\n", result);
    return 0;
}