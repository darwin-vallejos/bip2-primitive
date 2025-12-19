import argparse
import sys

def cli():
    parser = argparse.ArgumentParser(prog="bip2")
    parser.add_argument("cmd", help="command")
    args = parser.parse_args()

    print(f"Unknown command: {args.cmd}", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    cli()
