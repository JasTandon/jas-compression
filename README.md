# JAS - Custom Text Compression Format

[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](htmlcov/index.html)

JAS is a Python-based, word-level text compression tool using dictionary encoding, run-length encoding (RLE), and case flagging.

## Features

- Custom `.jas` binary format for text compression
- Case-insensitive compression with case flags for accurate restoration
- Supports plain text, JSON, CSV, code, subtitles, and more
- Command-line interface:
  - `jas compress <input> <output>`
  - `jas decompress <input> <output>`
  - `jas debug <input>`
- Extensive tests with coverage reports

## Installation

To install from PyPI:
```bash
pip install jas

## For development:

git clone https://github.com/yourusername/jas.git
cd jas
pip install -e .

## Usage

- Compress a file:
jas compress input.txt output.jas

- Decompress:
jas decompress output.jas result.txt

- Debug Tokenization:
jas debug input.txt

## Running Tests
Use the provided Makefile:

make test
make coverage

## License
MIT License


---

### 12. `Makefile`
```makefile
.PHONY: test coverage clean

test:
	pytest -v

coverage:
	coverage run -m pytest
	coverage report -m
	coverage html
	@echo "Open htmlcov/index.html to view the coverage report."

clean:
	rm -rf .pytest_cache __pycache__ .coverage htmlcov dist build *.egg-info

