import argparse
import sys
from normalize.bytes import normalize_bytes
from canonical.json import canonical_json

def cli():
    parser = argparse.ArgumentParser(prog="bip2")
    parser.add_argument("cmd", help="command")
    parser.add_argument("file", nargs="?", help="input file")

    args = parser.parse_args()

    if not args.file:
        print("command requires a file", file=sys.stderr)
        sys.exit(1)

    raw = open(args.file, "rb").read()

    if args.cmd == "normalize":
        out = normalize_bytes(raw)
    elif args.cmd == "canonicalize":
        structured = canonical_json(raw)
        out = normalize_bytes(structured)
    else:
        print(f"Unknown command: {args.cmd}", file=sys.stderr)
        sys.exit(1)

    sys.stdout.buffer.write(out)

if __name__ == "__main__":
    cli()
