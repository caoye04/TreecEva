#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265

struct Position {
    unsigned int x : 10;  // 0-1023 meters
    unsigned int y : 10;  // 0-1023 meters
    unsigned int z : 6;   // 0-63 meters
};

struct Drone {
    struct Position pos;
    int id;
    struct Drone* next;
};

volatile int transmission_quota = 0;

// Calculates distance between two positions
double calculate_distance(struct Position a, struct Position b) {
    int dx = a.x - b.x;
    int dy = a.y - b.y;
    int dz = a.z - b.z;
    return sqrt(dx*dx + dy*dy + dz*dz);
}

int main() {
    // Initialize three drones with starting positions
    struct Drone drone1 = {{100, 200, 10}, 1, NULL};
    struct Drone drone2 = {{300, 400, 20}, 2, NULL};
    struct Drone drone3 = {{500, 600, 30}, 3, NULL};
    
    // Link them in a list
    drone1.next = &drone2;
    drone2.next = &drone3;
    
    struct Drone* current_drone = &drone1;
    struct Position previous_positions[3];
    int index = 0;
    
    // Simulate movement and greedy transmission scheduling
    while (current_drone != NULL) {
        previous_positions[index] = current_drone->pos;
        
        // Move drone diagonally upward
        if (current_drone->pos.x + 50 <= 1023) current_drone->pos.x += 50;
        if (current_drone->pos.y + 50 <= 1023) current_drone->pos.y += 50;
        if (current_drone->pos.z + 5 <= 63) current_drone->pos.z += 5;
        
        // Greedy decision: transmit only if moved significantly (>30 units)
        double distance = calculate_distance(previous_positions[index], current_drone->pos);
        if (distance > 30.0) {
            transmission_quota += (int)(distance / 10); // Allocate quota based on distance
        }
        
        current_drone = current_drone->next;
        index++;
    }
    
    // Adjust quota based on altitude (higher altitude = more efficient transmission)
    int total_altitude = drone1.pos.z + drone2.pos.z + drone3.pos.z;
    transmission_quota -= (total_altitude / 10);
    
    printf("Result: %d\n", transmission_quota);
    return 0;
}