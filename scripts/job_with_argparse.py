import sys
import argparse

if __name__ == "__main__":
    # define an argument parser
    parser = argparse.ArgumentParser(
        description="Applies a low-pass filter to the timeseries contained in the input file.",
        epilog="Please contact sam.cantrill@data61.csiro.au for further help."
    )
    parser.add_argument("--frequency",
        required=True,
        help="Frequency"
    )
    parser.add_argument("--filename",
        required=False,
        default="wave.csv",
        help="Filename to analyze"
    )

    # parse the system arguments
    args, unknown_args = parser.parse_known_args(sys.argv)
    print(args)
    print(unknown_args)

    # apply processing with args
    print(args.frequency)
    print(args.filename)
