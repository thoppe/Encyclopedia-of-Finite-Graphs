CC=gcc
CFLAGS=-O3 -Wall
CFLAGS=-O3 -pedantic -std=iso9899:1999 -Wall 

tutte_bhkk: tutte_bhkk.o
	$(CC) -o tutte_bhkk tutte_bhkk.o -lgmp

clean:
	rm -f *~ *.o  tutte_bhkk test/test-out/test?

test: tutte_bhkk
	perl test/expand.pl test/small-graphs/graphs5.txt | ./tutte_bhkk | perl test/compress.pl > test/test-out/test5
	diff test/test-out/test5 test/test-out/ref5
	perl test/expand.pl test/small-graphs/graphs6.txt | ./tutte_bhkk | perl test/compress.pl > test/test-out/test6
	diff test/test-out/test6 test/test-out/ref6
	perl test/expand.pl test/small-graphs/graphs7.txt | ./tutte_bhkk | perl test/compress.pl > test/test-out/test7
	diff test/test-out/test7 test/test-out/ref7
	python tutte.py -t

release: clean
	cd .. && tar -zcf tar --exclude="\.svn" tutte_bhkk/tutte_bhkk1.0.tar.gz tutte_bhkk/Makefile tutte_bhkk/tutte_bhkk.c tutte_bhkk/tutte.py tutte_bhkk/test/compress.pl tutte_bhkk/test/expand.pl tutte_bhkk/test/small-graphs/* tutte_bhkk/test/test-out/* tutte_bhkk/INSTALL tutte_bhkk/README

