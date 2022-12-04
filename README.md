# Advent of Code 2022 - Solutions

*This repository contains my solutions for [AOC2022](https://adventofcode.com/2022).*

The solutions for the first two days are written in [exa++](https://github.com/njmuggio/exaplusplus).
I discovered a major bug with a non-trivial fix in the exa++ interpreter, so I switched to (shoddy) python starting on day 3.

The code for the exa++ interpreter is a submodule of this repository. To build:

```sh
cmake -S exaplusplus -B bin
cmake --build bin
```

To run a solution (day 1, part 2 in this example):

```sh
cd 01
../bin/epp 01/part2.epp
```
