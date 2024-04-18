
# eGenix Micro Benchmark

*Note*: This is a first alpha version of the software and as of yet, unreleased. Things are most likely going to change at a higher rate until we've reached a point where a release is made.

## Abstract

This package provide a set of tools for easily writing micro benchmarks in Python.

It builds upon the [pyperf](https://pypi.org/project/pyperf/) package which is an evolution of the [pybench](https://github.com/python/cpython/tree/v3.6.15/Tools/pybench) tool, which was part of Python for a very long time (and was also authored by Marc-André Lemburg, just like this new package). pyperf comes with more modern ways of doing benchmarking and timing, with the aim of producing more stable results.

Since micro benchmarks will typically test language features which run at the nanosecond scale, it is necessary to duplicate the test several times in order to have the test case run longer than the timing machinery around it. The package offers a very elegant way to do this and also provides generic discovery functionality to make writing such benchmarks a breeze.

## Example

Here's an example micro benchmark module (bench_example.py):

```python
#!/usr/bin/env python3
import micro_benchmark

def bench_match_int():

    # Init
    obj = 1

    # Bench
    match obj:
        case float():
            type = 'float'
        case int():
            type = 'int'
        case _:
            pass

    # Verify
    assert type == 'int'

if __name__ == '__main__':
    micro_benchmark.run(globals())
```

## Concept

The *init* part is run to set up the variables for the main part, the *bench* part. This part is not measured.

The *bench* part is run inside a loop managed by pyperf lots of times to measure the performance. Since the for-loop used for this incurs some timing overhead as well, the *bench* part is repeated a certain number of times (this is called *iterations* in the context of this package).

The *verify* part is run after the bench part to check whether the bench part did in fact run correctly and as expected. This part is not measured.

## Preparing the venv

In order to prepare the virtual env needed for the package to run, edit the `Makefile` to your liking and then run:

```
make install-venv
source env.sh # for bash
source env.csh # for C-shell
make packages
```

(or use any other virtual tool you like :-))

## Running the benchmark

Invoking the benchmark is easy. Simply run it with Python:

```
python3 bench_example.py
```

The benchmark will take all the command line arguments pyperf supports, in addition to these extra ones added by the egenix-micro-benchmarks package:

- `--mb-filter=<regexp>`
  Only run those benchmark functions which match the given regular expression. The matching is done as a substring match, so e.g. using `--mb-filter="match"` will match the function in the example module.

The output will look something like this:

```
.....................
bench_match_int: Mean +- std dev: 105 ns +- 10 ns
```

giving you the time it tool to run a single iteration of the bench part, together with an indication how reliable this reading is by providing the standard deviation of the timings.

In some cases, pyperf may warn you about unstable results. Benchmarking typically works best on quiet machines which don't have anything much else to do.

## Roadmap

- [ ] Add a whole set of micro benchmarks (e.g. the ones from pybench)
- [ ] Release as a PyPI package

## Contact

For inquiries related to the package, please write to info@egenix.com
