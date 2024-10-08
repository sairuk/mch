#!/usr/bin/env python3

import os
import argparse
from lib.gme import GME
from lib.mcd import MCD
from lib.mcs import MCS
from lib.raw import RAW

outputs = {
    "mcd": MCD, 
    "mcs": MCS,
    "raw": RAW
    }

def main(args):

    inputfile = args.i
    outmode = args.ot
    outdir = args.od

    if not os.path.exists(inputfile):
        raise FileNotFoundError(f"{inputfile} was not found")

    gme = GME()
    gme.process(inputfile)

    try:
        output = outputs[outmode](gme.savedict)
    except:
        print(f"{outmode} is not supported")
        exit(1)
    output.process()

    pathfile = os.path.splitext(inputfile)[0]
    for idx, key in enumerate(output.data.keys()):
        if len(output.data.keys()) > 1:
            fileno = f"{idx}".zfill(3)
            fileout = f"{pathfile}-{fileno}.{output.ext}"
        else:
            fileout = f"{pathfile}.{output.ext}"

        if outdir is not None and os.path.exists(outdir):
            basename = os.path.basename(fileout)
            fileout = os.path.join(outdir, basename)

        print(f"Writing: {fileout}")
        with open(fileout,"wb") as mcf:
            mcf.write(output.data[key])
    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='gme2mc')
    parser.add_argument("-i", help="Input file to process", required=True)
    parser.add_argument("-ot", help="Output method", choices=outputs.keys(), required=True)
    parser.add_argument("-od", help="Output path/directory", required=False)
    args = parser.parse_args()

    main(args)
