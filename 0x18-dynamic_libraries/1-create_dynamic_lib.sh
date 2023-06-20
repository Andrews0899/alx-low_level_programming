#!/bin/bash
gcc -Wall -wextra -Werror -pedantic -c -fPIAC *.c
gcc -shared -o liball.so *.o
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
