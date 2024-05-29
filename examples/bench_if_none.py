#!/usr/bin/env python3
"""
    Example micro benchmark for common tests for None

    Written by Marc-Andre Lemburg.
    Copyright (c) 2024, eGenix.com Software GmbH; mailto:info@egenix.com
    License: Apache-2.0
"""
import micro_benchmark

### Benchmarks

def bench_if_x_is_none():

    # Init
    obj = None

    # Bench
    if obj is None:
        check = 1
    else:
        check = 0

    # Verify
    assert check == 1

def bench_if_x_equals_none():

    # Init
    obj = None

    # Bench
    if obj == None:
        check = 1
    else:
        check = 0

    # Verify
    assert check == 1

def bench_if_not_x():

    # Init
    obj = None

    # Bench
    if not obj:
        check = 1
    else:
        check = 0

    # Verify
    assert check == 1

### CLI

if __name__ == '__main__':
    micro_benchmark.run(globals())
