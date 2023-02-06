#include "utilities.h"
#include "Yin.h"
#include <stdio.h>
#include <stdint.h>

#ifdef __cplusplus
#define EXTERN extern "C"
#else
#define EXTERN
#endif


// Transform main in one function from EMSCRIPTEN_KEEPALIVE, 
// Obs, the var audio, now come from JS, and is one parameter of the function
// it return one float with the pitch

float EMSCRIPTEN_KEEPALIVE C_getPitch(float* audio, int sampleRate) {
   int buffer_length = 4096;
   Yin yin;
   float pitch;
   

   // convert float to int16_t
   // obs, the audio is a pointer to a float array

   int16_t* audio_int = (int16_t*)malloc(buffer_length * sizeof(int16_t));
   for (int i = 0; i < buffer_length; i++) {
		audio_int[i] = (int16_t)(audio[i] * 32767.0f);
	}

   // init yin
   Yin_init(&yin, buffer_length, 0.4);

   // get pitch
   pitch = Yin_getPitch(&yin, audio_int);

   // free memory
   Yin_free(&yin);


   // free memory
   free(audio);

   return pitch;
}
