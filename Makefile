CFLAGS= -Wall -O3
LDFLAGS= -lLimeSuite

all: limesdr_linrad limesdr_linrad_phasediff

limesdr_linrad: limesdr_linrad.o

limesdr_linrad_phasediff: limesdr_linrad_phasediff.o

clean:
	rm -rf limesdr_linrad limesdr_linrad_phasediff *.o
