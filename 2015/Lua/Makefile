# All sources
SRCS = $(wildcard */*.lua)

.PHONY: run

run:
	@for x in $(SRCS);         \
	do                         \
		echo '=> Running' $$x; \
		lua $$x;           \
	done;
