#!/usr/bin/env python3
"""
    decorators - for use with the micro_benchmark package

    Written by Marc-Andre Lemburg.
    Copyright (c) 2024, eGenix.com Software GmbH; mailto:info@egenix.com
    License: Apache-2.0

"""

### Decorators

def configure(iterations=None, name=None):

    """ Decorator to provide additional configuration for a benchmark
        function.

        iterations can be set to override the default for this function.

        name can be given to provide a more verbose name for the
        function. The name is used by pyperf when generating output and
        for recording the results in the JSON results file. It defaults
        to the function's name.

    """
    def wrapper(fct):
        if iterations is not None:
            fct.iterations = iterations
        if name is not None:
            fct.name = name
        return fct
    return wrapper

###

if __name__ == '__main__':

    @configure(iterations=100, name='Testing decoratiors')
    def bench_test():
        # Init
        n = 1000

        # Bench
        x0 = range(n)
        x1 = range(n)
        x2 = range(n)
        x3 = range(n)
        x4 = range(n)

        # Verify
        assert len(x0) == n
        assert len(x1) == n
        assert len(x2) == n
        assert len(x3) == n
        assert len(x4) == n

    from micro_benchmark import runtime
    runner = runtime.run(globals())
