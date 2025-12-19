import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from normalize.bytes import normalize_bytes
from canonical.json import canonicalize_json
