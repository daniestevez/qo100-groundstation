CFLAGS= -Wall -O2
LDFLAGS= -lLimeSuite

all: limesdr_linrad

limesdr_linrad: limesdr_linrad.o

clean:
	rm -rf limesdr_linrad *.o
