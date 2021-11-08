CC = gcc
CFLAGS = -g -Wall
BIN = exp_mod private_key

all: $(BIN)

%:%.c
	$(CC) $(CFLAGS) $< -o $@

mod:
	./exp_mod

pri:
	./private_key

clean:
	rm $(BIN)