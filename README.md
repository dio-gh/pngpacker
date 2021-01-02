# pngpacker

## Overview

This script enables you to take any arbitrary file, turn it into a PNG image, or do the exact opposite. It's important to note that the script was written (intentionally) naively, so it doesn't do much validation of any kind. It's aimed to be a minimal example with some prop code to enable the non-programmers' usage of it.

## Dependencies

The script currently relies on NumPy and PyPNG. You'll need to get them through PIP if you don't have them already:

```sh
pip install numpy
pip install pypng
```

The script also requires Python 3.8+.

## Usage

The script is self-contained, so you only really need `pngpacker.py` from this repo. The before packing and after unpacking files *should be* the same, down to the bit. Source: tried it with a couple files and compared hashes, plus a healthy side of trust me bro.

```txt
Syntax: pngpacker.py <option> infile [outfile]
Options:
        --pack: packs the input file into a PNG
        --unpack: unpacks the input PNG to whatever file it used to be
```

### Example \#1 (packing)

```sh
./pngpacker.py --pack "sample.txt"
```

### Example \#2 (unpacking)

```sh
./pngpacker.py --unpack "sample.txt.png"
```

## Limitations and shortcomings

- the transformation is not streamed, so it may use **a lot** of memory (be careful with that)
- the transformation relies on PyPNG, so combined with the previous point this means it's a bit slow
- doesn't split the input for you based on a target filesize limit (gonna have to do that yourself)
- the header is pretty basic and bolted on, semi-intentionally (you might gonna need to refactor)
- there's not much validation, the script is pretty naive all-around
- the repo doesn't really have the regular python project structure, cause I wrote it all in Sublime

## License and contributions

Contributions, feature requests and issue reports are welcome, but [following the Python Coding Style Guide](https://www.python.org/dev/peps/pep-0008/), using common sense, and acting semi-professionally are expected.

I must also note, that for the time being, I'm satisfied with the state of this script and do not want to expand on it in any particular manner. However, if you do want to do so, these may be worthwhile points to address:

- creating a proper project structure that is typical with common python projects
- switching out PyPNG to something more performant, like the image lib in scikit
- implementing streamed processing
- implementing file splitting
- refactoring the code for it to be able to serialize arbitrary header structures into the PNGs
- cleaning up how cli parameters are processed

The license is MIT. See the `LICENSE` file for details.
