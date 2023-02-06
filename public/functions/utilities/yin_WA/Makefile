# make file to use emcc to compile the C code to JavaScript
# emcc -o index.js src/index.c src/utilities.c -O3 -s NO_EXIT_RUNTIME=1 -s "EXPORTED_RUNTIME_METHODS=['ccall']"
# Allow Grow memory
# emcc -o public/CFunctions.js $(C_FILES) -O3 -s NO_EXIT_RUNTIME=1 -s "EXPORTED_RUNTIME_METHODS=['ccall']" 

C_FILES = $(wildcard src/*.c)

all: index.js

# Allow grow memory with ALLOW_MEMORY_GROWTH=1

index.js: $(C_FILES)
	emcc -o ../../flute/CFunctions.js $(C_FILES) -O3 -s NO_EXIT_RUNTIME=1 -s "EXPORTED_RUNTIME_METHODS=['ccall']"
	emcc -o ../../sax/CFunctions.js $(C_FILES) -O3 -s NO_EXIT_RUNTIME=1 -s "EXPORTED_RUNTIME_METHODS=['ccall']"
	emcc -o ../../guitar/CFunctions.js $(C_FILES) -O3 -s NO_EXIT_RUNTIME=1 -s "EXPORTED_RUNTIME_METHODS=['ccall']"
	emcc -o ../../cello/CFunctions.js $(C_FILES) -O3 -s NO_EXIT_RUNTIME=1 -s "EXPORTED_RUNTIME_METHODS=['ccall']"

	

	
	
