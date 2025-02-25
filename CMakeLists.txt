cmake_minimum_required(VERSION 3.30)
project(Cryptography C)

set(CMAKE_C_STANDARD 11)

add_executable(Cryptography
    main.c
        week3/eea.c
        week3/gcd.c)
