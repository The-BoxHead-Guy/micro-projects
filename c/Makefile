# Custom name for the final executables
TARGET = ../bin/hello
TARGET_CONDITIONALS = ../bin/conditionals
TARGET_COMPARE = ../bin/compare
TARGET_AGREE = ../bin/agree
TARGET_CAT = ../bin/cat
TARGET_MARIO = ../bin/mario

# The source file(s) to compile
SRC = hello.c
SRC_CONDITIONALS = conditionals.c
SRC_COMPARE = compare.c
SRC_AGREE = agree.c
SRC_CAT = cat.c
SRC_MARIO = mario.c

all: $(TARGET) $(TARGET_CONDITIONALS) $(TARGET_COMPARE) $(TARGET_AGREE) $(TARGET_CAT) $(TARGET_MARIO)

$(TARGET): $(SRC)
	gcc $(SRC) -o $(TARGET) -lcs50

$(TARGET_CONDITIONALS): $(SRC_CONDITIONALS)
	gcc $(SRC_CONDITIONALS) -o $(TARGET_CONDITIONALS) -lcs50

$(TARGET_COMPARE): $(SRC_COMPARE)
	gcc $(SRC_COMPARE) -o $(TARGET_COMPARE) -lcs50

$(TARGET_AGREE): $(SRC_AGREE)
	gcc $(SRC_AGREE) -o $(TARGET_AGREE) -lcs50

$(TARGET_CAT): $(SRC_CAT)
	gcc $(SRC_CAT) -o $(TARGET_CAT) -lcs50

$(TARGET_MARIO): $(SRC_MARIO)
	gcc $(SRC_MARIO) -o $(TARGET_MARIO) -lcs50

clean:
	rm -f $(TARGET) $(TARGET_CONDITIONALS) $(TARGET_COMPARE) $(TARGET_AGREE) $(TARGET_CAT) $(TARGET_MARIO)
