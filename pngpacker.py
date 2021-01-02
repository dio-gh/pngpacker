#!/usr/bin/env python3

from pathlib import Path
import math
import os
import sys
import png
import numpy as np

def fsize_to_hdr(fsize):
    fsize = fsize.to_bytes(8, byteorder="big")
    return [int.from_bytes(fsize[i:i+2], byteorder="big") for i in range(0,8,2)]

def hdr_to_fsize(hdr):
    temp = bytearray()
    for i in range(4):
        temp += hdr[i].to_bytes(2, byteorder="big")
    return int.from_bytes(temp, byteorder="big")

def pack(src, dst):
    cb = fsize_to_hdr(os.path.getsize(src))
    with open(src, "rb") as infile:
	    while val := infile.read(2):
	        cb.append(int.from_bytes(val, byteorder="big"))
    dim = math.ceil((len(cb) / 4) ** .5)
    cb.extend([0] * int((dim ** 2 - len(cb) / 4) * 4))
    img = np.array(cb).reshape(dim, dim * 4).tolist()
    png.from_array(img, mode="RGBA;16").save(dst)

def unpack(src, dst):
    x, y, chvals, meta = png.Reader(src).read_flat()
    fsize = hdr_to_fsize(chvals[:4])
    with open(dst, "wb") as outfile:
        for i in range(4, math.ceil(fsize / 2) + 4):
            if fsize % 2 == 0 or i != math.ceil(fsize / 2) + 3:
                outfile.write(chvals[i].to_bytes(2, byteorder="big"))
            else:
                outfile.write(chvals[i].to_bytes(1, byteorder="big"))

def print_usage():
    print("Syntax: " + Path(sys.argv[0]).name + " <option> infile [outfile]")
    print("Options:")
    print("\t--pack: packs the input file into a PNG")
    print("\t--unpack: unpacks the input PNG to whatever file it used to be")

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Invalid number of parameters passed.")
        print_usage()
        exit()
    if sys.argv[2].strip() == "" or not Path(sys.argv[2]).exists():
        print("No or invalid input filepath was passed.")
        print_usage()
        exit()
    if sys.argv[1] == "--pack":
        outname = sys.argv[2].strip() + ".png"
        if len(sys.argv) == 4:
            outname = sys.argv[3].strip()
        pack(sys.argv[2].strip(), outname)
    elif sys.argv[1] == "--unpack":
        outname = ""
        if sys.argv[2].strip().lower().endswith(".png"):
            outname = sys.argv[2].strip()[:-4]
        if len(sys.argv) == 4:
            outname = sys.argv[3].strip()
        unpack(sys.argv[2].strip(), outname)
    else:
        print("Invalid option passed.")
        print_usage()
        exit()

if __name__ == '__main__':
    main()
