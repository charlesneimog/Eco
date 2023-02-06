#include "utilities.h"

// write function to malloc memory
int * EMSCRIPTEN_KEEPALIVE mallocMemory(int size) {
    int *array = (int *)malloc(size * sizeof(int));
    return array;
}


// write function to free memory
void EMSCRIPTEN_KEEPALIVE freeMemory(int *array) {
    free(array);
}
