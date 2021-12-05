# All sources
SRCS = $(wildcard */*.py)

.PHONY: run

run:
	@for x in $(SRCS);         \
	do                         \
		echo '=> Running' $$x; \
		python3 $$x;           \
	done;
