#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define GRID_SIZE 5

int compare(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

int main() {
    int elevation_map[GRID_SIZE][GRID_SIZE] = {
        {120, 150, 140, 130, 160},
        {145, 180, 175, 165, 155},
        {135, 170, 200, 190, 145},
        {125, 160, 185, 180, 135},
        {110, 140, 155, 165, 120}
    };
    
    int peak_candidates[GRID_SIZE * GRID_SIZE];
    int candidate_count = 0;
    
    // Identify potential peaks using neighbor comparison
    for(int i = 1; i < GRID_SIZE - 1; i++) {
        for(int j = 1; j < GRID_SIZE - 1; j++) {
            int current = elevation_map[i][j];
            if(current > elevation_map[i-1][j] && 
               current > elevation_map[i+1][j] && 
               current > elevation_map[i][j-1] && 
               current > elevation_map[i][j+1]) {
                peak_candidates[candidate_count++] = current;
            }
        }
    }
    
    // Sort candidates in descending order
    qsort(peak_candidates, candidate_count, sizeof(int), compare);
    
    // Count prominent peaks (those with at least 20 units elevation difference from neighbors)
    int prominent_peaks = 0;
    for(int i = 0; i < candidate_count; i++) {
        int is_prominent = 1;
        int current_peak = peak_candidates[i];
        
        // Find position of current peak in original map
        for(int r = 1; r < GRID_SIZE - 1; r++) {
            for(int c = 1; c < GRID_SIZE - 1; c++) {
                if(elevation_map[r][c] == current_peak) {
                    // Check if it's still a peak with stricter criteria
                    if(!(current_peak >= elevation_map[r-1][j] + 20 && 
                         current_peak >= elevation_map[r+1][j] + 20 && 
                         current_peak >= elevation_map[i][c-1] + 20 && 
                         current_peak >= elevation_map[i][c+1] + 20)) {
                        is_prominent = 0;
                    }
                    break;
                }
            }
            if(!is_prominent) break;
        }
        
        if(is_prominent) prominent_peaks++;
    }
    
    printf("Result: %d\n", prominent_peaks);
    return 0;
}