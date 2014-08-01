#args = 7 14781504
args = 10 17996771828415962

all:
	g++ -std=c++11 -O3 -o main idep_vertex.cpp
test: 
	time ./main  $(args)
clean:
	rm -vf main

# Normally this takes 8.97 seconds
# Recursive method takes 7.92 seconds
time: 
	time bash ./test.sh

