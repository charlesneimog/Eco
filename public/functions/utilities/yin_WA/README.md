### WebAssembly from C/Cpp

Simple repo to remind me how I can compile C code to work with the browser.

To compile `C` code we run this:

`emcc -o index.js main.c -O3 -s NO_EXIT_RUNTIME=1 -s "EXPORTED_RUNTIME_METHODS=['ccall']"`

To get `emcc` running, you need to check the link: https://emscripten.org/docs/getting_started/downloads.html

This example will print the result of the C function  Browser console, nothing more. It needs to be run on a server. It does not work opening the `index.html`.

