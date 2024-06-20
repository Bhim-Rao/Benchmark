<p align="center">
  <img src="https://github.com/Bhim-Rao/Benchmark/blob/main/assets/Benchmark-Logo.png?raw=true" alt="Benxhmark Logo"/>
</p>

# Benchmark
This project is a python script to test how long another program takes to run

## Requirements

- Python 3.x

## Installation

Clone the repository:

```sh
git clone https://github.com/Bhim-Rao/Benchmark.git
cd benchmark
```

## Quickstart

### To Benchmark a file using the python script run the command
```sh
python benchmark.py your_file.py
```

### To Benchmark a file using the executable run the command
```sh
cd dist
benchmark your_file.py
```

> make sure to replace `your_file.py` with an existing filename. We've provided the example file `hello.py`
>> make sure your file is in the same directory as the program

### Using our example file it should should output something like this: 
```yaml
0
64
256
...
63744256
63872064

52.0 ms
```

## Usage
usage: benchmark [option] ... [file]
-p     : ignores print statements from the running file
-s     : outputs elapsed time in seconds
-ms    : outputs elapsed time in milliseconds
-mcs   : outputs elapsed time in microseconds
-r num : run's the code `num` times

Arguments:
file   : program to be benchmarked

## License

This project is licensed under the MIT License - see the LICENSE file for details.
