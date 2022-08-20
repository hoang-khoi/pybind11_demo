#include <pybind11/pybind11.h>

long fibonacci(long n) {
    if (n == 0 || n == 1) {
        return n;
    }

    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Note: binding code should be separate from the logical ones.
PYBIND11_MODULE(libmath, m) {
    m.doc() = "A stupid mathematics module in fancy C.";
    m.def("fibonacci", &fibonacci, "Calculate the fibonacci sequence");
}
