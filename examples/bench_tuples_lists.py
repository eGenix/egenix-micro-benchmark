#!/usr/bin/env python3
"""
    Example micro benchmark for common tests for None

    Written by Marc-Andre Lemburg.
    Copyright (c) 2024, eGenix.com Software GmbH; mailto:info@egenix.com
    License: Apache-2.0
"""
import micro_benchmark

### Benchmarks

def bench_list_creation():

    # Init
    obj = range(100)

    # Bench
    x = list(obj)

    # Verify
    assert len(x) == 100

def bench_list_access():

    # Init
    obj = list(range(100))

    # Bench
    obj[8]
    obj[80]
    obj[0]
    obj[99]
    obj[40]
    obj[60]
    obj[20]
    obj[10]
    len(obj)

    # Verify
    assert len(obj) == 100

def bench_tuple_creation():

    # Init
    obj = range(100)

    # Bench
    x = tuple(obj)

    # Verify
    assert len(x) == 100

def bench_tuple_access():

    # Init
    obj = tuple(range(100))

    # Bench
    obj[8]
    obj[80]
    obj[0]
    obj[99]
    obj[40]
    obj[60]
    obj[20]
    obj[10]
    len(obj)

    # Verify
    assert len(obj) == 100

### CLI

if __name__ == '__main__':
    micro_benchmark.run(globals())
