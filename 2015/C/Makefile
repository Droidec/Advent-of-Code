# Compiler
CC = gcc
# Compilation flags
CFLAGS = -Wall -Wextra -Werror
# All sources
SRCS = $(wildcard */*.c)
# All binaries (substitution reference)
BINS = $(SRCS:.c=)

.PHONY: all run clean

all: $(BINS)

run:
	@for x in $(BINS);         \
	do                         \
		echo '=> Running' $$x; \
		./$$x;                 \
	done;

clean:
	rm -rf $(BINS)
