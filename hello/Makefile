CC      = gcc
CFLAGS  = -g
RM      = rm -f


default: all

all: Hello

Hello: hello.c
	$(CC) $(CFLAGS) -o hello hello.c
	./hello

clean veryclean:
	$(RM) Hello