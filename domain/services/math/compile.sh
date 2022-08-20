#!/usr/bin/env sh

TARGET=libmath
g++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) $TARGET.cc -o $TARGET$(python3-config --extension-suffix) -undefined dynamic_lookup
