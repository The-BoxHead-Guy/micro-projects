# Custom name for the final executable
TARGET = ../bin/hello
TARGET_CONDITIONALS = ../bin/conditionals
TARGET_COMPARE = ../bin/compare

# The source file(s) to compile
SRC = hello.c
SRC_CONDITIONALS = conditionals.c
SRC_COMPARE = compare.c

all: $(TARGET) $(TARGET_CONDITIONALS) $(TARGET_COMPARE)

$(TARGET): $(SRC)
	gcc $(SRC) -o $(TARGET) -lcs50

$(TARGET_CONDITIONALS): $(SRC_CONDITIONALS)
	gcc $(SRC_CONDITIONALS) -o $(TARGET_CONDITIONALS) -lcs50

$(TARGET_COMPARE): $(SRC_COMPARE)
	gcc $(SRC_COMPARE) -o $(TARGET_COMPARE) -lcs50

clean:
	rm -f $(TARGET) $(TARGET_CONDITIONALS) $(TARGET_COMPARE)
