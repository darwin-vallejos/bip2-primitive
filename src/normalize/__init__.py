import argparse
import sys
from normalize.bytes import normalize_bytes

def cli():
    parser = argparse.ArgumentParser(prog="bip2")
    parser.add_argument("cmd", help="command")
    parser.add_argument("file", nargs="?", help="input file")

    args = parser.parse_args()

    if args.cmd != "normalize":
        print(f"Unknown command: {args.cmd}", file=sys.stderr)
        sys.exit(1)

    if not args.file:
        print("normalize requires a file", file=sys.stderr)
        sys.exit(1)

    raw = open(args.file, "rb").read()
    out = normalize_bytes(raw)
    sys.stdout.buffer.write(out)

if __name__ == "__main__":
    cli()
