unit_test: unit_test.o assignment.o
	gcc -Wall -Werror -pedantic -std=c11 -o unit_test unit_test.o assignment.o

unit_test.o: unit_test.c assignment.h
	gcc -Wall -Werror -pedantic -std=c11 -c unit_test.c

assignment.o: assignment.c assignment.h
	gcc -Wall -Werror -pedantic -std=c11 -c mnist.c

clean:
	rm -f assignment.o unit_test.o unit_test
