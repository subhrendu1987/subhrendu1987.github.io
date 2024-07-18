# Variables
CC = gcc
CFLAGS = -Wall -Wextra -std=c11
TARGET = fibo
SRC = fib.c

# Default target
all: $(TARGET)

# Rule to build the target executable
$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

# Rule to clean up the build files
clean:
	rm -f $(TARGET) *.o

# Phony targets
.PHONY: all clean
