#!/bin/bash

bench() {
        echo "Benchmarking $@"
        perf stat -o ../benchmark.txt --append -r 10 "$@" > /dev/null 2>&1
}

rm -f benchmark.txt
touch benchmark.txt

cd 01 || exit
bench ../build/epp part1.epp
bench ../build/epp part2.epp

cd ../02 || exit
bench ../build/epp part1.epp
bench ../build/epp part2.epp

cd ../03 || exit
bench ../build/epp part1.epp
bench python part2.py

cd ../04 || exit
bench python part1.py
bench python part2.py

cd ../05 || exit
bench python part1.py
bench python part2.py

cd ../06 || exit
bench python part1.py
bench python part2.py

cd ../07 || exit
bench python part1.py
bench python part2.py

cd ../08 || exit
bench python part1.py
bench python part2.py

cd ../09 || exit
bench python part1.py
bench python part2.py

cd ../10 || exit
bench python part1.py
bench python part2.py

cd ../11 || exit
bench python part1.py
bench python part2.py

cd ../12 || exit
bench python part1.py
bench python part2.py

cd ../13 || exit
bench python part1.py
bench python part2.py

cd ../14 || exit
bench python part1.py
bench python part2.py

cd ../15 || exit
bench python part1.py
bench python part2.py

cd ../16 || exit
bench python part1.py
bench python part2.py

cd ../17 || exit
bench python part1.py
bench python part2.py

cd ../18 || exit
bench python part1.py
bench python part2.py

cd ../19 || exit
bench python part1.py
bench python part2.py

cd ../20 || exit
bench python part1.py
bench python part2.py

cd ../21 || exit
bench python part1.py
bench python part2.py

cd ../22 || exit
bench python part1.py
bench python part2.py

cd ../23 || exit
bench python part1.py
bench python part2.py

cd ../24 || exit
bench python part1.py
bench python part2.py

cd ../25 || exit
bench python part1.py
bench python part2.py
