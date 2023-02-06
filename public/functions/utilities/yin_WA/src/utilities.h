#ifndef UTILITIES_H
#define UTILITIES_H

#include <stdio.h>
#include <stdlib.h>
#include <emscripten/emscripten.h>


int *EMSCRIPTEN_KEEPALIVE mallocMemory(int size);
void EMSCRIPTEN_KEEPALIVE freeMemory(int *array);

#endif
