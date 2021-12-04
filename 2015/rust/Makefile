# Compiler
RUSTC = rustc
# All sources
SRCS = $(wildcard */*.rs)
# All binaries (substitution reference)
BINS = $(SRCS:.rs=)

.PHONY: all run clean

all: $(BINS)

$(BINS) : $(SRCS)
	$(RUSTC) $< -o $@

run:
	@for x in $(BINS);         \
	do                         \
	    echo '=> Running' $$x; \
		./$$x;                 \
	done;

clean:
	rm -rf $(BINS)
