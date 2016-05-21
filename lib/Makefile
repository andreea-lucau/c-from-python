CC = gcc # C compiler
CFLAGS = -fPIC -Wall -Wextra -O2 -g # C flags
LDFLAGS = -shared  # linking flags
RM = rm -f  # rm command
TARGET_LIB = libstringprocessor.so # target lib

SRCS = stringprocessor.c # source files

.PHONY: all
all: ${TARGET_LIB}

$(TARGET_LIB): $(OBJS)
	$(CC) ${LDFLAGS} ${CFLAGS} -o $(TARGET_LIB) $(SRCS)

.PHONY: clean
clean:
	-${RM} ${TARGET_LIB}
