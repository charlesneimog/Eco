# Run Makefile inside public/functions/utilities to build functions

# Build all functions

all: build

# run make inside public/functions/utilities

build:
	@echo "Building Web Assembly functions..."
	@cd public/functions/utilities/yin_WA/ && make
