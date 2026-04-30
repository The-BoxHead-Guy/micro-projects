# Custom name for the final executable
TARGET = ../bin/hello
TARGET_CONDITIONALS = ../bin/conditionals

# The source file(s) to compile
SRC = hello.c
SRC_CONDITIONALS = conditionals.c

all: $(TARGET) $(TARGET_CONDITIONALS)

$(TARGET): $(SRC)
	gcc $(SRC) -o $(TARGET) -lcs50

$(TARGET_CONDITIONALS): $(SRC_CONDITIONALS)
	gcc $(SRC_CONDITIONALS) -o $(TARGET_CONDITIONALS) -lcs50

clean:
	rm -f $(TARGET) $(TARGET_CONDITIONALS)
