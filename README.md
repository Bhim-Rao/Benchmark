<p align="center">
  <img src="https://github.com/waldyr/Sublime-Installer/blob/master/sublime_text.png?raw=true" alt="Sublime's custom image"/>
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

## Usage

### Use these instructions for the python file

To Benchmark another file run the command
```sh
python benchmark.py your_file.py
```
> make sure to replace `your_file.py` with an existing filename. We've provided the example file `hello.py`
>> make sure your file is in the same directory as the program

### use these instructions for the executable

To Benchmark another file run the command
```sh
cd dist
benchmark your_file.py
```

Using our example file it should should output something like this: 
```yaml
0
64
256
...
63744256
63872064

52.0 ms
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
